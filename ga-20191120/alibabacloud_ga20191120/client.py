# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ga20191120 import models as main_models
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
        self._endpoint = self.get_endpoint('ga', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddEntriesToAcl',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddEntriesToAcl',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateAclsWithListener',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateAclsWithListener',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.certificates):
            query['Certificates'] = request.certificates
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateAdditionalCertificatesWithListener',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.certificates):
            query['Certificates'] = request.certificates
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateAdditionalCertificatesWithListener',
            version = '2019-11-20',
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

    def associate_resources_with_options(
        self,
        request: main_models.AssociateResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.associated_mode):
            query['AssociatedMode'] = request.associated_mode
        if not DaraCore.is_null(request.associated_resource_id):
            query['AssociatedResourceId'] = request.associated_resource_id
        if not DaraCore.is_null(request.associated_resource_region_id):
            query['AssociatedResourceRegionId'] = request.associated_resource_region_id
        if not DaraCore.is_null(request.associated_resource_type):
            query['AssociatedResourceType'] = request.associated_resource_type
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateResources',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_resources_with_options_async(
        self,
        request: main_models.AssociateResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.associated_mode):
            query['AssociatedMode'] = request.associated_mode
        if not DaraCore.is_null(request.associated_resource_id):
            query['AssociatedResourceId'] = request.associated_resource_id
        if not DaraCore.is_null(request.associated_resource_region_id):
            query['AssociatedResourceRegionId'] = request.associated_resource_region_id
        if not DaraCore.is_null(request.associated_resource_type):
            query['AssociatedResourceType'] = request.associated_resource_type
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateResources',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_resources(
        self,
        request: main_models.AssociateResourcesRequest,
    ) -> main_models.AssociateResourcesResponse:
        runtime = RuntimeOptions()
        return self.associate_resources_with_options(request, runtime)

    async def associate_resources_async(
        self,
        request: main_models.AssociateResourcesRequest,
    ) -> main_models.AssociateResourcesResponse:
        runtime = RuntimeOptions()
        return await self.associate_resources_with_options_async(request, runtime)

    def attach_ddos_to_accelerator_with_options(
        self,
        request: main_models.AttachDdosToAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachDdosToAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.ddos_config_list):
            query['DdosConfigList'] = request.ddos_config_list
        if not DaraCore.is_null(request.ddos_id):
            query['DdosId'] = request.ddos_id
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachDdosToAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachDdosToAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_ddos_to_accelerator_with_options_async(
        self,
        request: main_models.AttachDdosToAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachDdosToAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.ddos_config_list):
            query['DdosConfigList'] = request.ddos_config_list
        if not DaraCore.is_null(request.ddos_id):
            query['DdosId'] = request.ddos_id
        if not DaraCore.is_null(request.ddos_region_id):
            query['DdosRegionId'] = request.ddos_region_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachDdosToAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachDdosToAcceleratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_ddos_to_accelerator(
        self,
        request: main_models.AttachDdosToAcceleratorRequest,
    ) -> main_models.AttachDdosToAcceleratorResponse:
        runtime = RuntimeOptions()
        return self.attach_ddos_to_accelerator_with_options(request, runtime)

    async def attach_ddos_to_accelerator_async(
        self,
        request: main_models.AttachDdosToAcceleratorRequest,
    ) -> main_models.AttachDdosToAcceleratorResponse:
        runtime = RuntimeOptions()
        return await self.attach_ddos_to_accelerator_with_options_async(request, runtime)

    def attach_log_store_to_endpoint_group_with_options(
        self,
        request: main_models.AttachLogStoreToEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachLogStoreToEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.access_log_record_customized_header_list):
            query['AccessLogRecordCustomizedHeaderList'] = request.access_log_record_customized_header_list
        if not DaraCore.is_null(request.access_log_record_customized_headers_enabled):
            query['AccessLogRecordCustomizedHeadersEnabled'] = request.access_log_record_customized_headers_enabled
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_ids):
            query['EndpointGroupIds'] = request.endpoint_group_ids
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sls_log_store_name):
            query['SlsLogStoreName'] = request.sls_log_store_name
        if not DaraCore.is_null(request.sls_project_name):
            query['SlsProjectName'] = request.sls_project_name
        if not DaraCore.is_null(request.sls_region_id):
            query['SlsRegionId'] = request.sls_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachLogStoreToEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachLogStoreToEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_log_store_to_endpoint_group_with_options_async(
        self,
        request: main_models.AttachLogStoreToEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachLogStoreToEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.access_log_record_customized_header_list):
            query['AccessLogRecordCustomizedHeaderList'] = request.access_log_record_customized_header_list
        if not DaraCore.is_null(request.access_log_record_customized_headers_enabled):
            query['AccessLogRecordCustomizedHeadersEnabled'] = request.access_log_record_customized_headers_enabled
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_ids):
            query['EndpointGroupIds'] = request.endpoint_group_ids
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sls_log_store_name):
            query['SlsLogStoreName'] = request.sls_log_store_name
        if not DaraCore.is_null(request.sls_project_name):
            query['SlsProjectName'] = request.sls_project_name
        if not DaraCore.is_null(request.sls_region_id):
            query['SlsRegionId'] = request.sls_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachLogStoreToEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachLogStoreToEndpointGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_log_store_to_endpoint_group(
        self,
        request: main_models.AttachLogStoreToEndpointGroupRequest,
    ) -> main_models.AttachLogStoreToEndpointGroupResponse:
        runtime = RuntimeOptions()
        return self.attach_log_store_to_endpoint_group_with_options(request, runtime)

    async def attach_log_store_to_endpoint_group_async(
        self,
        request: main_models.AttachLogStoreToEndpointGroupRequest,
    ) -> main_models.AttachLogStoreToEndpointGroupResponse:
        runtime = RuntimeOptions()
        return await self.attach_log_store_to_endpoint_group_with_options_async(request, runtime)

    def bandwidth_package_add_accelerator_with_options(
        self,
        request: main_models.BandwidthPackageAddAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BandwidthPackageAddAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BandwidthPackageAddAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BandwidthPackageAddAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def bandwidth_package_add_accelerator_with_options_async(
        self,
        request: main_models.BandwidthPackageAddAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BandwidthPackageAddAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BandwidthPackageAddAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BandwidthPackageAddAcceleratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bandwidth_package_add_accelerator(
        self,
        request: main_models.BandwidthPackageAddAcceleratorRequest,
    ) -> main_models.BandwidthPackageAddAcceleratorResponse:
        runtime = RuntimeOptions()
        return self.bandwidth_package_add_accelerator_with_options(request, runtime)

    async def bandwidth_package_add_accelerator_async(
        self,
        request: main_models.BandwidthPackageAddAcceleratorRequest,
    ) -> main_models.BandwidthPackageAddAcceleratorResponse:
        runtime = RuntimeOptions()
        return await self.bandwidth_package_add_accelerator_with_options_async(request, runtime)

    def bandwidth_package_remove_accelerator_with_options(
        self,
        request: main_models.BandwidthPackageRemoveAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BandwidthPackageRemoveAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BandwidthPackageRemoveAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BandwidthPackageRemoveAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def bandwidth_package_remove_accelerator_with_options_async(
        self,
        request: main_models.BandwidthPackageRemoveAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BandwidthPackageRemoveAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BandwidthPackageRemoveAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BandwidthPackageRemoveAcceleratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bandwidth_package_remove_accelerator(
        self,
        request: main_models.BandwidthPackageRemoveAcceleratorRequest,
    ) -> main_models.BandwidthPackageRemoveAcceleratorResponse:
        runtime = RuntimeOptions()
        return self.bandwidth_package_remove_accelerator_with_options(request, runtime)

    async def bandwidth_package_remove_accelerator_async(
        self,
        request: main_models.BandwidthPackageRemoveAcceleratorRequest,
    ) -> main_models.BandwidthPackageRemoveAcceleratorResponse:
        runtime = RuntimeOptions()
        return await self.bandwidth_package_remove_accelerator_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def config_endpoint_probe_with_options(
        self,
        request: main_models.ConfigEndpointProbeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigEndpointProbeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.probe_port):
            query['ProbePort'] = request.probe_port
        if not DaraCore.is_null(request.probe_protocol):
            query['ProbeProtocol'] = request.probe_protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigEndpointProbe',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigEndpointProbeResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_endpoint_probe_with_options_async(
        self,
        request: main_models.ConfigEndpointProbeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigEndpointProbeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.probe_port):
            query['ProbePort'] = request.probe_port
        if not DaraCore.is_null(request.probe_protocol):
            query['ProbeProtocol'] = request.probe_protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigEndpointProbe',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigEndpointProbeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_endpoint_probe(
        self,
        request: main_models.ConfigEndpointProbeRequest,
    ) -> main_models.ConfigEndpointProbeResponse:
        runtime = RuntimeOptions()
        return self.config_endpoint_probe_with_options(request, runtime)

    async def config_endpoint_probe_async(
        self,
        request: main_models.ConfigEndpointProbeRequest,
    ) -> main_models.ConfigEndpointProbeResponse:
        runtime = RuntimeOptions()
        return await self.config_endpoint_probe_with_options_async(request, runtime)

    def create_accelerator_with_options(
        self,
        request: main_models.CreateAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.bandwidth_billing_type):
            query['BandwidthBillingType'] = request.bandwidth_billing_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not DaraCore.is_null(request.ip_set_config):
            query['IpSetConfig'] = request.ip_set_config
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_accelerator_with_options_async(
        self,
        request: main_models.CreateAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.bandwidth_billing_type):
            query['BandwidthBillingType'] = request.bandwidth_billing_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not DaraCore.is_null(request.ip_set_config):
            query['IpSetConfig'] = request.ip_set_config
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAcceleratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_accelerator(
        self,
        request: main_models.CreateAcceleratorRequest,
    ) -> main_models.CreateAcceleratorResponse:
        runtime = RuntimeOptions()
        return self.create_accelerator_with_options(request, runtime)

    async def create_accelerator_async(
        self,
        request: main_models.CreateAcceleratorRequest,
    ) -> main_models.CreateAcceleratorResponse:
        runtime = RuntimeOptions()
        return await self.create_accelerator_with_options_async(request, runtime)

    def create_acl_with_options(
        self,
        request: main_models.CreateAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_entries):
            query['AclEntries'] = request.acl_entries
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAcl',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.acl_entries):
            query['AclEntries'] = request.acl_entries
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAcl',
            version = '2019-11-20',
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

    def create_application_monitor_with_options(
        self,
        request: main_models.CreateApplicationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.detect_enable):
            query['DetectEnable'] = request.detect_enable
        if not DaraCore.is_null(request.detect_threshold):
            query['DetectThreshold'] = request.detect_threshold
        if not DaraCore.is_null(request.detect_times):
            query['DetectTimes'] = request.detect_times
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.options_json):
            query['OptionsJson'] = request.options_json
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationMonitor',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_monitor_with_options_async(
        self,
        request: main_models.CreateApplicationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.detect_enable):
            query['DetectEnable'] = request.detect_enable
        if not DaraCore.is_null(request.detect_threshold):
            query['DetectThreshold'] = request.detect_threshold
        if not DaraCore.is_null(request.detect_times):
            query['DetectTimes'] = request.detect_times
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.options_json):
            query['OptionsJson'] = request.options_json
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationMonitor',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_monitor(
        self,
        request: main_models.CreateApplicationMonitorRequest,
    ) -> main_models.CreateApplicationMonitorResponse:
        runtime = RuntimeOptions()
        return self.create_application_monitor_with_options(request, runtime)

    async def create_application_monitor_async(
        self,
        request: main_models.CreateApplicationMonitorRequest,
    ) -> main_models.CreateApplicationMonitorResponse:
        runtime = RuntimeOptions()
        return await self.create_application_monitor_with_options_async(request, runtime)

    def create_bandwidth_package_with_options(
        self,
        request: main_models.CreateBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not DaraCore.is_null(request.billing_type):
            query['BillingType'] = request.billing_type
        if not DaraCore.is_null(request.cbn_geographic_region_id_a):
            query['CbnGeographicRegionIdA'] = request.cbn_geographic_region_id_a
        if not DaraCore.is_null(request.cbn_geographic_region_id_b):
            query['CbnGeographicRegionIdB'] = request.cbn_geographic_region_id_b
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.ratio):
            query['Ratio'] = request.ratio
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBandwidthPackage',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_bandwidth_package_with_options_async(
        self,
        request: main_models.CreateBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not DaraCore.is_null(request.billing_type):
            query['BillingType'] = request.billing_type
        if not DaraCore.is_null(request.cbn_geographic_region_id_a):
            query['CbnGeographicRegionIdA'] = request.cbn_geographic_region_id_a
        if not DaraCore.is_null(request.cbn_geographic_region_id_b):
            query['CbnGeographicRegionIdB'] = request.cbn_geographic_region_id_b
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.ratio):
            query['Ratio'] = request.ratio
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBandwidthPackage',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBandwidthPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_bandwidth_package(
        self,
        request: main_models.CreateBandwidthPackageRequest,
    ) -> main_models.CreateBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return self.create_bandwidth_package_with_options(request, runtime)

    async def create_bandwidth_package_async(
        self,
        request: main_models.CreateBandwidthPackageRequest,
    ) -> main_models.CreateBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return await self.create_bandwidth_package_with_options_async(request, runtime)

    def create_basic_accelerate_ip_with_options(
        self,
        request: main_models.CreateBasicAccelerateIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBasicAccelerateIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBasicAccelerateIp',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBasicAccelerateIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_basic_accelerate_ip_with_options_async(
        self,
        request: main_models.CreateBasicAccelerateIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBasicAccelerateIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBasicAccelerateIp',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBasicAccelerateIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_basic_accelerate_ip(
        self,
        request: main_models.CreateBasicAccelerateIpRequest,
    ) -> main_models.CreateBasicAccelerateIpResponse:
        runtime = RuntimeOptions()
        return self.create_basic_accelerate_ip_with_options(request, runtime)

    async def create_basic_accelerate_ip_async(
        self,
        request: main_models.CreateBasicAccelerateIpRequest,
    ) -> main_models.CreateBasicAccelerateIpResponse:
        runtime = RuntimeOptions()
        return await self.create_basic_accelerate_ip_with_options_async(request, runtime)

    def create_basic_accelerate_ip_endpoint_relation_with_options(
        self,
        request: main_models.CreateBasicAccelerateIpEndpointRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBasicAccelerateIpEndpointRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBasicAccelerateIpEndpointRelation',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBasicAccelerateIpEndpointRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_basic_accelerate_ip_endpoint_relation_with_options_async(
        self,
        request: main_models.CreateBasicAccelerateIpEndpointRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBasicAccelerateIpEndpointRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBasicAccelerateIpEndpointRelation',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBasicAccelerateIpEndpointRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_basic_accelerate_ip_endpoint_relation(
        self,
        request: main_models.CreateBasicAccelerateIpEndpointRelationRequest,
    ) -> main_models.CreateBasicAccelerateIpEndpointRelationResponse:
        runtime = RuntimeOptions()
        return self.create_basic_accelerate_ip_endpoint_relation_with_options(request, runtime)

    async def create_basic_accelerate_ip_endpoint_relation_async(
        self,
        request: main_models.CreateBasicAccelerateIpEndpointRelationRequest,
    ) -> main_models.CreateBasicAccelerateIpEndpointRelationResponse:
        runtime = RuntimeOptions()
        return await self.create_basic_accelerate_ip_endpoint_relation_with_options_async(request, runtime)

    def create_basic_accelerate_ip_endpoint_relations_with_options(
        self,
        request: main_models.CreateBasicAccelerateIpEndpointRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBasicAccelerateIpEndpointRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_ip_endpoint_relations):
            query['AccelerateIpEndpointRelations'] = request.accelerate_ip_endpoint_relations
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBasicAccelerateIpEndpointRelations',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBasicAccelerateIpEndpointRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_basic_accelerate_ip_endpoint_relations_with_options_async(
        self,
        request: main_models.CreateBasicAccelerateIpEndpointRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBasicAccelerateIpEndpointRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_ip_endpoint_relations):
            query['AccelerateIpEndpointRelations'] = request.accelerate_ip_endpoint_relations
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBasicAccelerateIpEndpointRelations',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBasicAccelerateIpEndpointRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_basic_accelerate_ip_endpoint_relations(
        self,
        request: main_models.CreateBasicAccelerateIpEndpointRelationsRequest,
    ) -> main_models.CreateBasicAccelerateIpEndpointRelationsResponse:
        runtime = RuntimeOptions()
        return self.create_basic_accelerate_ip_endpoint_relations_with_options(request, runtime)

    async def create_basic_accelerate_ip_endpoint_relations_async(
        self,
        request: main_models.CreateBasicAccelerateIpEndpointRelationsRequest,
    ) -> main_models.CreateBasicAccelerateIpEndpointRelationsResponse:
        runtime = RuntimeOptions()
        return await self.create_basic_accelerate_ip_endpoint_relations_with_options_async(request, runtime)

    def create_basic_accelerator_with_options(
        self,
        request: main_models.CreateBasicAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBasicAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not DaraCore.is_null(request.bandwidth_billing_type):
            query['BandwidthBillingType'] = request.bandwidth_billing_type
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBasicAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBasicAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_basic_accelerator_with_options_async(
        self,
        request: main_models.CreateBasicAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBasicAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not DaraCore.is_null(request.bandwidth_billing_type):
            query['BandwidthBillingType'] = request.bandwidth_billing_type
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBasicAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBasicAcceleratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_basic_accelerator(
        self,
        request: main_models.CreateBasicAcceleratorRequest,
    ) -> main_models.CreateBasicAcceleratorResponse:
        runtime = RuntimeOptions()
        return self.create_basic_accelerator_with_options(request, runtime)

    async def create_basic_accelerator_async(
        self,
        request: main_models.CreateBasicAcceleratorRequest,
    ) -> main_models.CreateBasicAcceleratorResponse:
        runtime = RuntimeOptions()
        return await self.create_basic_accelerator_with_options_async(request, runtime)

    def create_basic_endpoint_with_options(
        self,
        request: main_models.CreateBasicEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBasicEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_address):
            query['EndpointAddress'] = request.endpoint_address
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_sub_address):
            query['EndpointSubAddress'] = request.endpoint_sub_address
        if not DaraCore.is_null(request.endpoint_sub_address_type):
            query['EndpointSubAddressType'] = request.endpoint_sub_address_type
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.endpoint_zone_id):
            query['EndpointZoneId'] = request.endpoint_zone_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBasicEndpoint',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBasicEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_basic_endpoint_with_options_async(
        self,
        request: main_models.CreateBasicEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBasicEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_address):
            query['EndpointAddress'] = request.endpoint_address
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_sub_address):
            query['EndpointSubAddress'] = request.endpoint_sub_address
        if not DaraCore.is_null(request.endpoint_sub_address_type):
            query['EndpointSubAddressType'] = request.endpoint_sub_address_type
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.endpoint_zone_id):
            query['EndpointZoneId'] = request.endpoint_zone_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBasicEndpoint',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBasicEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_basic_endpoint(
        self,
        request: main_models.CreateBasicEndpointRequest,
    ) -> main_models.CreateBasicEndpointResponse:
        runtime = RuntimeOptions()
        return self.create_basic_endpoint_with_options(request, runtime)

    async def create_basic_endpoint_async(
        self,
        request: main_models.CreateBasicEndpointRequest,
    ) -> main_models.CreateBasicEndpointResponse:
        runtime = RuntimeOptions()
        return await self.create_basic_endpoint_with_options_async(request, runtime)

    def create_basic_endpoint_group_with_options(
        self,
        request: main_models.CreateBasicEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBasicEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.endpoint_address):
            query['EndpointAddress'] = request.endpoint_address
        if not DaraCore.is_null(request.endpoint_group_region):
            query['EndpointGroupRegion'] = request.endpoint_group_region
        if not DaraCore.is_null(request.endpoint_sub_address):
            query['EndpointSubAddress'] = request.endpoint_sub_address
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBasicEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBasicEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_basic_endpoint_group_with_options_async(
        self,
        request: main_models.CreateBasicEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBasicEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.endpoint_address):
            query['EndpointAddress'] = request.endpoint_address
        if not DaraCore.is_null(request.endpoint_group_region):
            query['EndpointGroupRegion'] = request.endpoint_group_region
        if not DaraCore.is_null(request.endpoint_sub_address):
            query['EndpointSubAddress'] = request.endpoint_sub_address
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBasicEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBasicEndpointGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_basic_endpoint_group(
        self,
        request: main_models.CreateBasicEndpointGroupRequest,
    ) -> main_models.CreateBasicEndpointGroupResponse:
        runtime = RuntimeOptions()
        return self.create_basic_endpoint_group_with_options(request, runtime)

    async def create_basic_endpoint_group_async(
        self,
        request: main_models.CreateBasicEndpointGroupRequest,
    ) -> main_models.CreateBasicEndpointGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_basic_endpoint_group_with_options_async(request, runtime)

    def create_basic_endpoints_with_options(
        self,
        request: main_models.CreateBasicEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBasicEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoints):
            query['Endpoints'] = request.endpoints
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBasicEndpoints',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBasicEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_basic_endpoints_with_options_async(
        self,
        request: main_models.CreateBasicEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBasicEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoints):
            query['Endpoints'] = request.endpoints
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBasicEndpoints',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBasicEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_basic_endpoints(
        self,
        request: main_models.CreateBasicEndpointsRequest,
    ) -> main_models.CreateBasicEndpointsResponse:
        runtime = RuntimeOptions()
        return self.create_basic_endpoints_with_options(request, runtime)

    async def create_basic_endpoints_async(
        self,
        request: main_models.CreateBasicEndpointsRequest,
    ) -> main_models.CreateBasicEndpointsResponse:
        runtime = RuntimeOptions()
        return await self.create_basic_endpoints_with_options_async(request, runtime)

    def create_basic_ip_set_with_options(
        self,
        request: main_models.CreateBasicIpSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBasicIpSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_region_id):
            query['AccelerateRegionId'] = request.accelerate_region_id
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.isp_type):
            query['IspType'] = request.isp_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBasicIpSet',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBasicIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_basic_ip_set_with_options_async(
        self,
        request: main_models.CreateBasicIpSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBasicIpSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_region_id):
            query['AccelerateRegionId'] = request.accelerate_region_id
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.isp_type):
            query['IspType'] = request.isp_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBasicIpSet',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBasicIpSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_basic_ip_set(
        self,
        request: main_models.CreateBasicIpSetRequest,
    ) -> main_models.CreateBasicIpSetResponse:
        runtime = RuntimeOptions()
        return self.create_basic_ip_set_with_options(request, runtime)

    async def create_basic_ip_set_async(
        self,
        request: main_models.CreateBasicIpSetRequest,
    ) -> main_models.CreateBasicIpSetResponse:
        runtime = RuntimeOptions()
        return await self.create_basic_ip_set_with_options_async(request, runtime)

    def create_custom_routing_endpoint_group_destinations_with_options(
        self,
        request: main_models.CreateCustomRoutingEndpointGroupDestinationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomRoutingEndpointGroupDestinationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.destination_configurations):
            query['DestinationConfigurations'] = request.destination_configurations
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomRoutingEndpointGroupDestinations',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomRoutingEndpointGroupDestinationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_routing_endpoint_group_destinations_with_options_async(
        self,
        request: main_models.CreateCustomRoutingEndpointGroupDestinationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomRoutingEndpointGroupDestinationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.destination_configurations):
            query['DestinationConfigurations'] = request.destination_configurations
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomRoutingEndpointGroupDestinations',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomRoutingEndpointGroupDestinationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_routing_endpoint_group_destinations(
        self,
        request: main_models.CreateCustomRoutingEndpointGroupDestinationsRequest,
    ) -> main_models.CreateCustomRoutingEndpointGroupDestinationsResponse:
        runtime = RuntimeOptions()
        return self.create_custom_routing_endpoint_group_destinations_with_options(request, runtime)

    async def create_custom_routing_endpoint_group_destinations_async(
        self,
        request: main_models.CreateCustomRoutingEndpointGroupDestinationsRequest,
    ) -> main_models.CreateCustomRoutingEndpointGroupDestinationsResponse:
        runtime = RuntimeOptions()
        return await self.create_custom_routing_endpoint_group_destinations_with_options_async(request, runtime)

    def create_custom_routing_endpoint_groups_with_options(
        self,
        request: main_models.CreateCustomRoutingEndpointGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomRoutingEndpointGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_group_configurations):
            query['EndpointGroupConfigurations'] = request.endpoint_group_configurations
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomRoutingEndpointGroups',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomRoutingEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_routing_endpoint_groups_with_options_async(
        self,
        request: main_models.CreateCustomRoutingEndpointGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomRoutingEndpointGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_group_configurations):
            query['EndpointGroupConfigurations'] = request.endpoint_group_configurations
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomRoutingEndpointGroups',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomRoutingEndpointGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_routing_endpoint_groups(
        self,
        request: main_models.CreateCustomRoutingEndpointGroupsRequest,
    ) -> main_models.CreateCustomRoutingEndpointGroupsResponse:
        runtime = RuntimeOptions()
        return self.create_custom_routing_endpoint_groups_with_options(request, runtime)

    async def create_custom_routing_endpoint_groups_async(
        self,
        request: main_models.CreateCustomRoutingEndpointGroupsRequest,
    ) -> main_models.CreateCustomRoutingEndpointGroupsResponse:
        runtime = RuntimeOptions()
        return await self.create_custom_routing_endpoint_groups_with_options_async(request, runtime)

    def create_custom_routing_endpoint_traffic_policies_with_options(
        self,
        request: main_models.CreateCustomRoutingEndpointTrafficPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomRoutingEndpointTrafficPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.policy_configurations):
            query['PolicyConfigurations'] = request.policy_configurations
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomRoutingEndpointTrafficPolicies',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomRoutingEndpointTrafficPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_routing_endpoint_traffic_policies_with_options_async(
        self,
        request: main_models.CreateCustomRoutingEndpointTrafficPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomRoutingEndpointTrafficPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.policy_configurations):
            query['PolicyConfigurations'] = request.policy_configurations
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomRoutingEndpointTrafficPolicies',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomRoutingEndpointTrafficPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_routing_endpoint_traffic_policies(
        self,
        request: main_models.CreateCustomRoutingEndpointTrafficPoliciesRequest,
    ) -> main_models.CreateCustomRoutingEndpointTrafficPoliciesResponse:
        runtime = RuntimeOptions()
        return self.create_custom_routing_endpoint_traffic_policies_with_options(request, runtime)

    async def create_custom_routing_endpoint_traffic_policies_async(
        self,
        request: main_models.CreateCustomRoutingEndpointTrafficPoliciesRequest,
    ) -> main_models.CreateCustomRoutingEndpointTrafficPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.create_custom_routing_endpoint_traffic_policies_with_options_async(request, runtime)

    def create_custom_routing_endpoints_with_options(
        self,
        request: main_models.CreateCustomRoutingEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomRoutingEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_configurations):
            query['EndpointConfigurations'] = request.endpoint_configurations
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomRoutingEndpoints',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomRoutingEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_routing_endpoints_with_options_async(
        self,
        request: main_models.CreateCustomRoutingEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomRoutingEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_configurations):
            query['EndpointConfigurations'] = request.endpoint_configurations
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomRoutingEndpoints',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomRoutingEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_routing_endpoints(
        self,
        request: main_models.CreateCustomRoutingEndpointsRequest,
    ) -> main_models.CreateCustomRoutingEndpointsResponse:
        runtime = RuntimeOptions()
        return self.create_custom_routing_endpoints_with_options(request, runtime)

    async def create_custom_routing_endpoints_async(
        self,
        request: main_models.CreateCustomRoutingEndpointsRequest,
    ) -> main_models.CreateCustomRoutingEndpointsResponse:
        runtime = RuntimeOptions()
        return await self.create_custom_routing_endpoints_with_options_async(request, runtime)

    def create_domain_with_options(
        self,
        request: main_models.CreateDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_ids):
            query['AcceleratorIds'] = request.accelerator_ids
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomain',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        request: main_models.CreateDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_ids):
            query['AcceleratorIds'] = request.accelerator_ids
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomain',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain(
        self,
        request: main_models.CreateDomainRequest,
    ) -> main_models.CreateDomainResponse:
        runtime = RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    async def create_domain_async(
        self,
        request: main_models.CreateDomainRequest,
    ) -> main_models.CreateDomainResponse:
        runtime = RuntimeOptions()
        return await self.create_domain_with_options_async(request, runtime)

    def create_endpoint_group_with_options(
        self,
        request: main_models.CreateEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_configurations):
            query['EndpointConfigurations'] = request.endpoint_configurations
        if not DaraCore.is_null(request.endpoint_group_region):
            query['EndpointGroupRegion'] = request.endpoint_group_region
        if not DaraCore.is_null(request.endpoint_group_type):
            query['EndpointGroupType'] = request.endpoint_group_type
        if not DaraCore.is_null(request.endpoint_ip_version):
            query['EndpointIpVersion'] = request.endpoint_ip_version
        if not DaraCore.is_null(request.endpoint_protocol_version):
            query['EndpointProtocolVersion'] = request.endpoint_protocol_version
        if not DaraCore.is_null(request.endpoint_request_protocol):
            query['EndpointRequestProtocol'] = request.endpoint_request_protocol
        if not DaraCore.is_null(request.health_check_enabled):
            query['HealthCheckEnabled'] = request.health_check_enabled
        if not DaraCore.is_null(request.health_check_host):
            query['HealthCheckHost'] = request.health_check_host
        if not DaraCore.is_null(request.health_check_interval_seconds):
            query['HealthCheckIntervalSeconds'] = request.health_check_interval_seconds
        if not DaraCore.is_null(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not DaraCore.is_null(request.health_check_port):
            query['HealthCheckPort'] = request.health_check_port
        if not DaraCore.is_null(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.port_overrides):
            query['PortOverrides'] = request.port_overrides
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.threshold_count):
            query['ThresholdCount'] = request.threshold_count
        if not DaraCore.is_null(request.traffic_percentage):
            query['TrafficPercentage'] = request.traffic_percentage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_endpoint_group_with_options_async(
        self,
        request: main_models.CreateEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_configurations):
            query['EndpointConfigurations'] = request.endpoint_configurations
        if not DaraCore.is_null(request.endpoint_group_region):
            query['EndpointGroupRegion'] = request.endpoint_group_region
        if not DaraCore.is_null(request.endpoint_group_type):
            query['EndpointGroupType'] = request.endpoint_group_type
        if not DaraCore.is_null(request.endpoint_ip_version):
            query['EndpointIpVersion'] = request.endpoint_ip_version
        if not DaraCore.is_null(request.endpoint_protocol_version):
            query['EndpointProtocolVersion'] = request.endpoint_protocol_version
        if not DaraCore.is_null(request.endpoint_request_protocol):
            query['EndpointRequestProtocol'] = request.endpoint_request_protocol
        if not DaraCore.is_null(request.health_check_enabled):
            query['HealthCheckEnabled'] = request.health_check_enabled
        if not DaraCore.is_null(request.health_check_host):
            query['HealthCheckHost'] = request.health_check_host
        if not DaraCore.is_null(request.health_check_interval_seconds):
            query['HealthCheckIntervalSeconds'] = request.health_check_interval_seconds
        if not DaraCore.is_null(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not DaraCore.is_null(request.health_check_port):
            query['HealthCheckPort'] = request.health_check_port
        if not DaraCore.is_null(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.port_overrides):
            query['PortOverrides'] = request.port_overrides
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.threshold_count):
            query['ThresholdCount'] = request.threshold_count
        if not DaraCore.is_null(request.traffic_percentage):
            query['TrafficPercentage'] = request.traffic_percentage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEndpointGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_endpoint_group(
        self,
        request: main_models.CreateEndpointGroupRequest,
    ) -> main_models.CreateEndpointGroupResponse:
        runtime = RuntimeOptions()
        return self.create_endpoint_group_with_options(request, runtime)

    async def create_endpoint_group_async(
        self,
        request: main_models.CreateEndpointGroupRequest,
    ) -> main_models.CreateEndpointGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_endpoint_group_with_options_async(request, runtime)

    def create_endpoint_groups_with_options(
        self,
        request: main_models.CreateEndpointGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEndpointGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.endpoint_group_configurations):
            body_flat['EndpointGroupConfigurations'] = request.endpoint_group_configurations
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEndpointGroups',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_endpoint_groups_with_options_async(
        self,
        request: main_models.CreateEndpointGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEndpointGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.endpoint_group_configurations):
            body_flat['EndpointGroupConfigurations'] = request.endpoint_group_configurations
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEndpointGroups',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEndpointGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_endpoint_groups(
        self,
        request: main_models.CreateEndpointGroupsRequest,
    ) -> main_models.CreateEndpointGroupsResponse:
        runtime = RuntimeOptions()
        return self.create_endpoint_groups_with_options(request, runtime)

    async def create_endpoint_groups_async(
        self,
        request: main_models.CreateEndpointGroupsRequest,
    ) -> main_models.CreateEndpointGroupsResponse:
        runtime = RuntimeOptions()
        return await self.create_endpoint_groups_with_options_async(request, runtime)

    def create_forwarding_rules_with_options(
        self,
        request: main_models.CreateForwardingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateForwardingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.forwarding_rules):
            body_flat['ForwardingRules'] = request.forwarding_rules
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateForwardingRules',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateForwardingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_forwarding_rules_with_options_async(
        self,
        request: main_models.CreateForwardingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateForwardingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.forwarding_rules):
            body_flat['ForwardingRules'] = request.forwarding_rules
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateForwardingRules',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateForwardingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_forwarding_rules(
        self,
        request: main_models.CreateForwardingRulesRequest,
    ) -> main_models.CreateForwardingRulesResponse:
        runtime = RuntimeOptions()
        return self.create_forwarding_rules_with_options(request, runtime)

    async def create_forwarding_rules_async(
        self,
        request: main_models.CreateForwardingRulesRequest,
    ) -> main_models.CreateForwardingRulesResponse:
        runtime = RuntimeOptions()
        return await self.create_forwarding_rules_with_options_async(request, runtime)

    def create_ip_sets_with_options(
        self,
        request: main_models.CreateIpSetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIpSetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_region):
            query['AccelerateRegion'] = request.accelerate_region
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIpSets',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIpSetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ip_sets_with_options_async(
        self,
        request: main_models.CreateIpSetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIpSetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_region):
            query['AccelerateRegion'] = request.accelerate_region
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIpSets',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIpSetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ip_sets(
        self,
        request: main_models.CreateIpSetsRequest,
    ) -> main_models.CreateIpSetsResponse:
        runtime = RuntimeOptions()
        return self.create_ip_sets_with_options(request, runtime)

    async def create_ip_sets_async(
        self,
        request: main_models.CreateIpSetsRequest,
    ) -> main_models.CreateIpSetsResponse:
        runtime = RuntimeOptions()
        return await self.create_ip_sets_with_options_async(request, runtime)

    def create_listener_with_options(
        self,
        request: main_models.CreateListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.certificates):
            query['Certificates'] = request.certificates
        if not DaraCore.is_null(request.client_affinity):
            query['ClientAffinity'] = request.client_affinity
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.custom_routing_endpoint_group_configurations):
            query['CustomRoutingEndpointGroupConfigurations'] = request.custom_routing_endpoint_group_configurations
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.endpoint_group_configurations):
            query['EndpointGroupConfigurations'] = request.endpoint_group_configurations
        if not DaraCore.is_null(request.http_version):
            query['HttpVersion'] = request.http_version
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.port_ranges):
            query['PortRanges'] = request.port_ranges
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.xforwarded_for_config):
            query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateListener',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.certificates):
            query['Certificates'] = request.certificates
        if not DaraCore.is_null(request.client_affinity):
            query['ClientAffinity'] = request.client_affinity
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.custom_routing_endpoint_group_configurations):
            query['CustomRoutingEndpointGroupConfigurations'] = request.custom_routing_endpoint_group_configurations
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.endpoint_group_configurations):
            query['EndpointGroupConfigurations'] = request.endpoint_group_configurations
        if not DaraCore.is_null(request.http_version):
            query['HttpVersion'] = request.http_version
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.port_ranges):
            query['PortRanges'] = request.port_ranges
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not DaraCore.is_null(request.security_policy_id):
            query['SecurityPolicyId'] = request.security_policy_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.xforwarded_for_config):
            query['XForwardedForConfig'] = request.xforwarded_for_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateListener',
            version = '2019-11-20',
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

    def create_spare_ips_with_options(
        self,
        request: main_models.CreateSpareIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSpareIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.spare_ips):
            query['SpareIps'] = request.spare_ips
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSpareIps',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSpareIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_spare_ips_with_options_async(
        self,
        request: main_models.CreateSpareIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSpareIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.spare_ips):
            query['SpareIps'] = request.spare_ips
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSpareIps',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSpareIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_spare_ips(
        self,
        request: main_models.CreateSpareIpsRequest,
    ) -> main_models.CreateSpareIpsResponse:
        runtime = RuntimeOptions()
        return self.create_spare_ips_with_options(request, runtime)

    async def create_spare_ips_async(
        self,
        request: main_models.CreateSpareIpsRequest,
    ) -> main_models.CreateSpareIpsResponse:
        runtime = RuntimeOptions()
        return await self.create_spare_ips_with_options_async(request, runtime)

    def delete_accelerator_with_options(
        self,
        request: main_models.DeleteAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_accelerator_with_options_async(
        self,
        request: main_models.DeleteAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAcceleratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_accelerator(
        self,
        request: main_models.DeleteAcceleratorRequest,
    ) -> main_models.DeleteAcceleratorResponse:
        runtime = RuntimeOptions()
        return self.delete_accelerator_with_options(request, runtime)

    async def delete_accelerator_async(
        self,
        request: main_models.DeleteAcceleratorRequest,
    ) -> main_models.DeleteAcceleratorResponse:
        runtime = RuntimeOptions()
        return await self.delete_accelerator_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAcl',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAcl',
            version = '2019-11-20',
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

    def delete_application_monitor_with_options(
        self,
        request: main_models.DeleteApplicationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationMonitor',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_monitor_with_options_async(
        self,
        request: main_models.DeleteApplicationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationMonitor',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application_monitor(
        self,
        request: main_models.DeleteApplicationMonitorRequest,
    ) -> main_models.DeleteApplicationMonitorResponse:
        runtime = RuntimeOptions()
        return self.delete_application_monitor_with_options(request, runtime)

    async def delete_application_monitor_async(
        self,
        request: main_models.DeleteApplicationMonitorRequest,
    ) -> main_models.DeleteApplicationMonitorResponse:
        runtime = RuntimeOptions()
        return await self.delete_application_monitor_with_options_async(request, runtime)

    def delete_bandwidth_package_with_options(
        self,
        request: main_models.DeleteBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBandwidthPackage',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_bandwidth_package_with_options_async(
        self,
        request: main_models.DeleteBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBandwidthPackage',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBandwidthPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_bandwidth_package(
        self,
        request: main_models.DeleteBandwidthPackageRequest,
    ) -> main_models.DeleteBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return self.delete_bandwidth_package_with_options(request, runtime)

    async def delete_bandwidth_package_async(
        self,
        request: main_models.DeleteBandwidthPackageRequest,
    ) -> main_models.DeleteBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return await self.delete_bandwidth_package_with_options_async(request, runtime)

    def delete_basic_accelerate_ip_with_options(
        self,
        request: main_models.DeleteBasicAccelerateIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBasicAccelerateIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBasicAccelerateIp',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBasicAccelerateIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_basic_accelerate_ip_with_options_async(
        self,
        request: main_models.DeleteBasicAccelerateIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBasicAccelerateIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBasicAccelerateIp',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBasicAccelerateIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_basic_accelerate_ip(
        self,
        request: main_models.DeleteBasicAccelerateIpRequest,
    ) -> main_models.DeleteBasicAccelerateIpResponse:
        runtime = RuntimeOptions()
        return self.delete_basic_accelerate_ip_with_options(request, runtime)

    async def delete_basic_accelerate_ip_async(
        self,
        request: main_models.DeleteBasicAccelerateIpRequest,
    ) -> main_models.DeleteBasicAccelerateIpResponse:
        runtime = RuntimeOptions()
        return await self.delete_basic_accelerate_ip_with_options_async(request, runtime)

    def delete_basic_accelerate_ip_endpoint_relation_with_options(
        self,
        request: main_models.DeleteBasicAccelerateIpEndpointRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBasicAccelerateIpEndpointRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBasicAccelerateIpEndpointRelation',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBasicAccelerateIpEndpointRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_basic_accelerate_ip_endpoint_relation_with_options_async(
        self,
        request: main_models.DeleteBasicAccelerateIpEndpointRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBasicAccelerateIpEndpointRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBasicAccelerateIpEndpointRelation',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBasicAccelerateIpEndpointRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_basic_accelerate_ip_endpoint_relation(
        self,
        request: main_models.DeleteBasicAccelerateIpEndpointRelationRequest,
    ) -> main_models.DeleteBasicAccelerateIpEndpointRelationResponse:
        runtime = RuntimeOptions()
        return self.delete_basic_accelerate_ip_endpoint_relation_with_options(request, runtime)

    async def delete_basic_accelerate_ip_endpoint_relation_async(
        self,
        request: main_models.DeleteBasicAccelerateIpEndpointRelationRequest,
    ) -> main_models.DeleteBasicAccelerateIpEndpointRelationResponse:
        runtime = RuntimeOptions()
        return await self.delete_basic_accelerate_ip_endpoint_relation_with_options_async(request, runtime)

    def delete_basic_accelerator_with_options(
        self,
        request: main_models.DeleteBasicAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBasicAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBasicAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBasicAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_basic_accelerator_with_options_async(
        self,
        request: main_models.DeleteBasicAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBasicAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBasicAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBasicAcceleratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_basic_accelerator(
        self,
        request: main_models.DeleteBasicAcceleratorRequest,
    ) -> main_models.DeleteBasicAcceleratorResponse:
        runtime = RuntimeOptions()
        return self.delete_basic_accelerator_with_options(request, runtime)

    async def delete_basic_accelerator_async(
        self,
        request: main_models.DeleteBasicAcceleratorRequest,
    ) -> main_models.DeleteBasicAcceleratorResponse:
        runtime = RuntimeOptions()
        return await self.delete_basic_accelerator_with_options_async(request, runtime)

    def delete_basic_endpoint_with_options(
        self,
        request: main_models.DeleteBasicEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBasicEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBasicEndpoint',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBasicEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_basic_endpoint_with_options_async(
        self,
        request: main_models.DeleteBasicEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBasicEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBasicEndpoint',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBasicEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_basic_endpoint(
        self,
        request: main_models.DeleteBasicEndpointRequest,
    ) -> main_models.DeleteBasicEndpointResponse:
        runtime = RuntimeOptions()
        return self.delete_basic_endpoint_with_options(request, runtime)

    async def delete_basic_endpoint_async(
        self,
        request: main_models.DeleteBasicEndpointRequest,
    ) -> main_models.DeleteBasicEndpointResponse:
        runtime = RuntimeOptions()
        return await self.delete_basic_endpoint_with_options_async(request, runtime)

    def delete_basic_endpoint_group_with_options(
        self,
        request: main_models.DeleteBasicEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBasicEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBasicEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBasicEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_basic_endpoint_group_with_options_async(
        self,
        request: main_models.DeleteBasicEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBasicEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBasicEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBasicEndpointGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_basic_endpoint_group(
        self,
        request: main_models.DeleteBasicEndpointGroupRequest,
    ) -> main_models.DeleteBasicEndpointGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_basic_endpoint_group_with_options(request, runtime)

    async def delete_basic_endpoint_group_async(
        self,
        request: main_models.DeleteBasicEndpointGroupRequest,
    ) -> main_models.DeleteBasicEndpointGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_basic_endpoint_group_with_options_async(request, runtime)

    def delete_basic_ip_set_with_options(
        self,
        request: main_models.DeleteBasicIpSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBasicIpSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBasicIpSet',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBasicIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_basic_ip_set_with_options_async(
        self,
        request: main_models.DeleteBasicIpSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBasicIpSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBasicIpSet',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBasicIpSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_basic_ip_set(
        self,
        request: main_models.DeleteBasicIpSetRequest,
    ) -> main_models.DeleteBasicIpSetResponse:
        runtime = RuntimeOptions()
        return self.delete_basic_ip_set_with_options(request, runtime)

    async def delete_basic_ip_set_async(
        self,
        request: main_models.DeleteBasicIpSetRequest,
    ) -> main_models.DeleteBasicIpSetResponse:
        runtime = RuntimeOptions()
        return await self.delete_basic_ip_set_with_options_async(request, runtime)

    def delete_custom_routing_endpoint_group_destinations_with_options(
        self,
        request: main_models.DeleteCustomRoutingEndpointGroupDestinationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomRoutingEndpointGroupDestinationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.destination_ids):
            query['DestinationIds'] = request.destination_ids
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomRoutingEndpointGroupDestinations',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomRoutingEndpointGroupDestinationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_routing_endpoint_group_destinations_with_options_async(
        self,
        request: main_models.DeleteCustomRoutingEndpointGroupDestinationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomRoutingEndpointGroupDestinationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.destination_ids):
            query['DestinationIds'] = request.destination_ids
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomRoutingEndpointGroupDestinations',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomRoutingEndpointGroupDestinationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_routing_endpoint_group_destinations(
        self,
        request: main_models.DeleteCustomRoutingEndpointGroupDestinationsRequest,
    ) -> main_models.DeleteCustomRoutingEndpointGroupDestinationsResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_routing_endpoint_group_destinations_with_options(request, runtime)

    async def delete_custom_routing_endpoint_group_destinations_async(
        self,
        request: main_models.DeleteCustomRoutingEndpointGroupDestinationsRequest,
    ) -> main_models.DeleteCustomRoutingEndpointGroupDestinationsResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_routing_endpoint_group_destinations_with_options_async(request, runtime)

    def delete_custom_routing_endpoint_groups_with_options(
        self,
        request: main_models.DeleteCustomRoutingEndpointGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomRoutingEndpointGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_group_ids):
            query['EndpointGroupIds'] = request.endpoint_group_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomRoutingEndpointGroups',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomRoutingEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_routing_endpoint_groups_with_options_async(
        self,
        request: main_models.DeleteCustomRoutingEndpointGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomRoutingEndpointGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_group_ids):
            query['EndpointGroupIds'] = request.endpoint_group_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomRoutingEndpointGroups',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomRoutingEndpointGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_routing_endpoint_groups(
        self,
        request: main_models.DeleteCustomRoutingEndpointGroupsRequest,
    ) -> main_models.DeleteCustomRoutingEndpointGroupsResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_routing_endpoint_groups_with_options(request, runtime)

    async def delete_custom_routing_endpoint_groups_async(
        self,
        request: main_models.DeleteCustomRoutingEndpointGroupsRequest,
    ) -> main_models.DeleteCustomRoutingEndpointGroupsResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_routing_endpoint_groups_with_options_async(request, runtime)

    def delete_custom_routing_endpoint_traffic_policies_with_options(
        self,
        request: main_models.DeleteCustomRoutingEndpointTrafficPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomRoutingEndpointTrafficPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.policy_ids):
            query['PolicyIds'] = request.policy_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomRoutingEndpointTrafficPolicies',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomRoutingEndpointTrafficPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_routing_endpoint_traffic_policies_with_options_async(
        self,
        request: main_models.DeleteCustomRoutingEndpointTrafficPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomRoutingEndpointTrafficPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.policy_ids):
            query['PolicyIds'] = request.policy_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomRoutingEndpointTrafficPolicies',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomRoutingEndpointTrafficPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_routing_endpoint_traffic_policies(
        self,
        request: main_models.DeleteCustomRoutingEndpointTrafficPoliciesRequest,
    ) -> main_models.DeleteCustomRoutingEndpointTrafficPoliciesResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_routing_endpoint_traffic_policies_with_options(request, runtime)

    async def delete_custom_routing_endpoint_traffic_policies_async(
        self,
        request: main_models.DeleteCustomRoutingEndpointTrafficPoliciesRequest,
    ) -> main_models.DeleteCustomRoutingEndpointTrafficPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_routing_endpoint_traffic_policies_with_options_async(request, runtime)

    def delete_custom_routing_endpoints_with_options(
        self,
        request: main_models.DeleteCustomRoutingEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomRoutingEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_ids):
            query['EndpointIds'] = request.endpoint_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomRoutingEndpoints',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomRoutingEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_routing_endpoints_with_options_async(
        self,
        request: main_models.DeleteCustomRoutingEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomRoutingEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_ids):
            query['EndpointIds'] = request.endpoint_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomRoutingEndpoints',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomRoutingEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_routing_endpoints(
        self,
        request: main_models.DeleteCustomRoutingEndpointsRequest,
    ) -> main_models.DeleteCustomRoutingEndpointsResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_routing_endpoints_with_options(request, runtime)

    async def delete_custom_routing_endpoints_async(
        self,
        request: main_models.DeleteCustomRoutingEndpointsRequest,
    ) -> main_models.DeleteCustomRoutingEndpointsResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_routing_endpoints_with_options_async(request, runtime)

    def delete_domain_accelerator_relation_with_options(
        self,
        request: main_models.DeleteDomainAcceleratorRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainAcceleratorRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_ids):
            query['AcceleratorIds'] = request.accelerator_ids
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomainAcceleratorRelation',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainAcceleratorRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_accelerator_relation_with_options_async(
        self,
        request: main_models.DeleteDomainAcceleratorRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainAcceleratorRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_ids):
            query['AcceleratorIds'] = request.accelerator_ids
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomainAcceleratorRelation',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainAcceleratorRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_accelerator_relation(
        self,
        request: main_models.DeleteDomainAcceleratorRelationRequest,
    ) -> main_models.DeleteDomainAcceleratorRelationResponse:
        runtime = RuntimeOptions()
        return self.delete_domain_accelerator_relation_with_options(request, runtime)

    async def delete_domain_accelerator_relation_async(
        self,
        request: main_models.DeleteDomainAcceleratorRelationRequest,
    ) -> main_models.DeleteDomainAcceleratorRelationResponse:
        runtime = RuntimeOptions()
        return await self.delete_domain_accelerator_relation_with_options_async(request, runtime)

    def delete_endpoint_group_with_options(
        self,
        request: main_models.DeleteEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_endpoint_group_with_options_async(
        self,
        request: main_models.DeleteEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEndpointGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_endpoint_group(
        self,
        request: main_models.DeleteEndpointGroupRequest,
    ) -> main_models.DeleteEndpointGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_endpoint_group_with_options(request, runtime)

    async def delete_endpoint_group_async(
        self,
        request: main_models.DeleteEndpointGroupRequest,
    ) -> main_models.DeleteEndpointGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_endpoint_group_with_options_async(request, runtime)

    def delete_endpoint_groups_with_options(
        self,
        request: main_models.DeleteEndpointGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEndpointGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_group_ids):
            query['EndpointGroupIds'] = request.endpoint_group_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEndpointGroups',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_endpoint_groups_with_options_async(
        self,
        request: main_models.DeleteEndpointGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEndpointGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_group_ids):
            query['EndpointGroupIds'] = request.endpoint_group_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEndpointGroups',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEndpointGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_endpoint_groups(
        self,
        request: main_models.DeleteEndpointGroupsRequest,
    ) -> main_models.DeleteEndpointGroupsResponse:
        runtime = RuntimeOptions()
        return self.delete_endpoint_groups_with_options(request, runtime)

    async def delete_endpoint_groups_async(
        self,
        request: main_models.DeleteEndpointGroupsRequest,
    ) -> main_models.DeleteEndpointGroupsResponse:
        runtime = RuntimeOptions()
        return await self.delete_endpoint_groups_with_options_async(request, runtime)

    def delete_forwarding_rules_with_options(
        self,
        request: main_models.DeleteForwardingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteForwardingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.forwarding_rule_ids):
            query['ForwardingRuleIds'] = request.forwarding_rule_ids
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteForwardingRules',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteForwardingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_forwarding_rules_with_options_async(
        self,
        request: main_models.DeleteForwardingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteForwardingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.forwarding_rule_ids):
            query['ForwardingRuleIds'] = request.forwarding_rule_ids
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteForwardingRules',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteForwardingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_forwarding_rules(
        self,
        request: main_models.DeleteForwardingRulesRequest,
    ) -> main_models.DeleteForwardingRulesResponse:
        runtime = RuntimeOptions()
        return self.delete_forwarding_rules_with_options(request, runtime)

    async def delete_forwarding_rules_async(
        self,
        request: main_models.DeleteForwardingRulesRequest,
    ) -> main_models.DeleteForwardingRulesResponse:
        runtime = RuntimeOptions()
        return await self.delete_forwarding_rules_with_options_async(request, runtime)

    def delete_ip_set_with_options(
        self,
        request: main_models.DeleteIpSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpSet',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ip_set_with_options_async(
        self,
        request: main_models.DeleteIpSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpSet',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ip_set(
        self,
        request: main_models.DeleteIpSetRequest,
    ) -> main_models.DeleteIpSetResponse:
        runtime = RuntimeOptions()
        return self.delete_ip_set_with_options(request, runtime)

    async def delete_ip_set_async(
        self,
        request: main_models.DeleteIpSetRequest,
    ) -> main_models.DeleteIpSetResponse:
        runtime = RuntimeOptions()
        return await self.delete_ip_set_with_options_async(request, runtime)

    def delete_ip_sets_with_options(
        self,
        request: main_models.DeleteIpSetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpSetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_set_ids):
            query['IpSetIds'] = request.ip_set_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpSets',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpSetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ip_sets_with_options_async(
        self,
        request: main_models.DeleteIpSetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIpSetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_set_ids):
            query['IpSetIds'] = request.ip_set_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIpSets',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIpSetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ip_sets(
        self,
        request: main_models.DeleteIpSetsRequest,
    ) -> main_models.DeleteIpSetsResponse:
        runtime = RuntimeOptions()
        return self.delete_ip_sets_with_options(request, runtime)

    async def delete_ip_sets_async(
        self,
        request: main_models.DeleteIpSetsRequest,
    ) -> main_models.DeleteIpSetsResponse:
        runtime = RuntimeOptions()
        return await self.delete_ip_sets_with_options_async(request, runtime)

    def delete_listener_with_options(
        self,
        request: main_models.DeleteListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteListener',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteListener',
            version = '2019-11-20',
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

    def delete_spare_ips_with_options(
        self,
        request: main_models.DeleteSpareIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSpareIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.spare_ips):
            query['SpareIps'] = request.spare_ips
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSpareIps',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSpareIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_spare_ips_with_options_async(
        self,
        request: main_models.DeleteSpareIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSpareIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.spare_ips):
            query['SpareIps'] = request.spare_ips
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSpareIps',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSpareIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_spare_ips(
        self,
        request: main_models.DeleteSpareIpsRequest,
    ) -> main_models.DeleteSpareIpsResponse:
        runtime = RuntimeOptions()
        return self.delete_spare_ips_with_options(request, runtime)

    async def delete_spare_ips_async(
        self,
        request: main_models.DeleteSpareIpsRequest,
    ) -> main_models.DeleteSpareIpsResponse:
        runtime = RuntimeOptions()
        return await self.delete_spare_ips_with_options_async(request, runtime)

    def describe_accelerator_with_options(
        self,
        request: main_models.DescribeAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accelerator_with_options_async(
        self,
        request: main_models.DescribeAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAcceleratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accelerator(
        self,
        request: main_models.DescribeAcceleratorRequest,
    ) -> main_models.DescribeAcceleratorResponse:
        runtime = RuntimeOptions()
        return self.describe_accelerator_with_options(request, runtime)

    async def describe_accelerator_async(
        self,
        request: main_models.DescribeAcceleratorRequest,
    ) -> main_models.DescribeAcceleratorResponse:
        runtime = RuntimeOptions()
        return await self.describe_accelerator_with_options_async(request, runtime)

    def describe_accelerator_auto_renew_attribute_with_options(
        self,
        request: main_models.DescribeAcceleratorAutoRenewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAcceleratorAutoRenewAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAcceleratorAutoRenewAttribute',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAcceleratorAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accelerator_auto_renew_attribute_with_options_async(
        self,
        request: main_models.DescribeAcceleratorAutoRenewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAcceleratorAutoRenewAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAcceleratorAutoRenewAttribute',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAcceleratorAutoRenewAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accelerator_auto_renew_attribute(
        self,
        request: main_models.DescribeAcceleratorAutoRenewAttributeRequest,
    ) -> main_models.DescribeAcceleratorAutoRenewAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_accelerator_auto_renew_attribute_with_options(request, runtime)

    async def describe_accelerator_auto_renew_attribute_async(
        self,
        request: main_models.DescribeAcceleratorAutoRenewAttributeRequest,
    ) -> main_models.DescribeAcceleratorAutoRenewAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_accelerator_auto_renew_attribute_with_options_async(request, runtime)

    def describe_accelerator_service_status_with_options(
        self,
        request: main_models.DescribeAcceleratorServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAcceleratorServiceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAcceleratorServiceStatus',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAcceleratorServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accelerator_service_status_with_options_async(
        self,
        request: main_models.DescribeAcceleratorServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAcceleratorServiceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAcceleratorServiceStatus',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAcceleratorServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accelerator_service_status(
        self,
        request: main_models.DescribeAcceleratorServiceStatusRequest,
    ) -> main_models.DescribeAcceleratorServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_accelerator_service_status_with_options(request, runtime)

    async def describe_accelerator_service_status_async(
        self,
        request: main_models.DescribeAcceleratorServiceStatusRequest,
    ) -> main_models.DescribeAcceleratorServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_accelerator_service_status_with_options_async(request, runtime)

    def describe_application_monitor_with_options(
        self,
        request: main_models.DescribeApplicationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationMonitor',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_monitor_with_options_async(
        self,
        request: main_models.DescribeApplicationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationMonitor',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_monitor(
        self,
        request: main_models.DescribeApplicationMonitorRequest,
    ) -> main_models.DescribeApplicationMonitorResponse:
        runtime = RuntimeOptions()
        return self.describe_application_monitor_with_options(request, runtime)

    async def describe_application_monitor_async(
        self,
        request: main_models.DescribeApplicationMonitorRequest,
    ) -> main_models.DescribeApplicationMonitorResponse:
        runtime = RuntimeOptions()
        return await self.describe_application_monitor_with_options_async(request, runtime)

    def describe_bandwidth_package_with_options(
        self,
        request: main_models.DescribeBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBandwidthPackage',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_bandwidth_package_with_options_async(
        self,
        request: main_models.DescribeBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBandwidthPackage',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBandwidthPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_bandwidth_package(
        self,
        request: main_models.DescribeBandwidthPackageRequest,
    ) -> main_models.DescribeBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return self.describe_bandwidth_package_with_options(request, runtime)

    async def describe_bandwidth_package_async(
        self,
        request: main_models.DescribeBandwidthPackageRequest,
    ) -> main_models.DescribeBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return await self.describe_bandwidth_package_with_options_async(request, runtime)

    def describe_bandwidth_package_auto_renew_attribute_with_options(
        self,
        request: main_models.DescribeBandwidthPackageAutoRenewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBandwidthPackageAutoRenewAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBandwidthPackageAutoRenewAttribute',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBandwidthPackageAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_bandwidth_package_auto_renew_attribute_with_options_async(
        self,
        request: main_models.DescribeBandwidthPackageAutoRenewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBandwidthPackageAutoRenewAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBandwidthPackageAutoRenewAttribute',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBandwidthPackageAutoRenewAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_bandwidth_package_auto_renew_attribute(
        self,
        request: main_models.DescribeBandwidthPackageAutoRenewAttributeRequest,
    ) -> main_models.DescribeBandwidthPackageAutoRenewAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_bandwidth_package_auto_renew_attribute_with_options(request, runtime)

    async def describe_bandwidth_package_auto_renew_attribute_async(
        self,
        request: main_models.DescribeBandwidthPackageAutoRenewAttributeRequest,
    ) -> main_models.DescribeBandwidthPackageAutoRenewAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_bandwidth_package_auto_renew_attribute_with_options_async(request, runtime)

    def describe_commodity_with_options(
        self,
        request: main_models.DescribeCommodityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCommodityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCommodity',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCommodityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_commodity_with_options_async(
        self,
        request: main_models.DescribeCommodityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCommodityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCommodity',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCommodityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_commodity(
        self,
        request: main_models.DescribeCommodityRequest,
    ) -> main_models.DescribeCommodityResponse:
        runtime = RuntimeOptions()
        return self.describe_commodity_with_options(request, runtime)

    async def describe_commodity_async(
        self,
        request: main_models.DescribeCommodityRequest,
    ) -> main_models.DescribeCommodityResponse:
        runtime = RuntimeOptions()
        return await self.describe_commodity_with_options_async(request, runtime)

    def describe_commodity_price_with_options(
        self,
        request: main_models.DescribeCommodityPriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCommodityPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.orders):
            query['Orders'] = request.orders
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCommodityPrice',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCommodityPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_commodity_price_with_options_async(
        self,
        request: main_models.DescribeCommodityPriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCommodityPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.orders):
            query['Orders'] = request.orders
        if not DaraCore.is_null(request.promotion_option_no):
            query['PromotionOptionNo'] = request.promotion_option_no
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCommodityPrice',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCommodityPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_commodity_price(
        self,
        request: main_models.DescribeCommodityPriceRequest,
    ) -> main_models.DescribeCommodityPriceResponse:
        runtime = RuntimeOptions()
        return self.describe_commodity_price_with_options(request, runtime)

    async def describe_commodity_price_async(
        self,
        request: main_models.DescribeCommodityPriceRequest,
    ) -> main_models.DescribeCommodityPriceResponse:
        runtime = RuntimeOptions()
        return await self.describe_commodity_price_with_options_async(request, runtime)

    def describe_custom_routing_end_point_traffic_policy_with_options(
        self,
        request: main_models.DescribeCustomRoutingEndPointTrafficPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomRoutingEndPointTrafficPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomRoutingEndPointTrafficPolicy',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomRoutingEndPointTrafficPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_routing_end_point_traffic_policy_with_options_async(
        self,
        request: main_models.DescribeCustomRoutingEndPointTrafficPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomRoutingEndPointTrafficPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomRoutingEndPointTrafficPolicy',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomRoutingEndPointTrafficPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_routing_end_point_traffic_policy(
        self,
        request: main_models.DescribeCustomRoutingEndPointTrafficPolicyRequest,
    ) -> main_models.DescribeCustomRoutingEndPointTrafficPolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_custom_routing_end_point_traffic_policy_with_options(request, runtime)

    async def describe_custom_routing_end_point_traffic_policy_async(
        self,
        request: main_models.DescribeCustomRoutingEndPointTrafficPolicyRequest,
    ) -> main_models.DescribeCustomRoutingEndPointTrafficPolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_custom_routing_end_point_traffic_policy_with_options_async(request, runtime)

    def describe_custom_routing_endpoint_with_options(
        self,
        request: main_models.DescribeCustomRoutingEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomRoutingEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_group):
            query['EndpointGroup'] = request.endpoint_group
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomRoutingEndpoint',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomRoutingEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_routing_endpoint_with_options_async(
        self,
        request: main_models.DescribeCustomRoutingEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomRoutingEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_group):
            query['EndpointGroup'] = request.endpoint_group
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomRoutingEndpoint',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomRoutingEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_routing_endpoint(
        self,
        request: main_models.DescribeCustomRoutingEndpointRequest,
    ) -> main_models.DescribeCustomRoutingEndpointResponse:
        runtime = RuntimeOptions()
        return self.describe_custom_routing_endpoint_with_options(request, runtime)

    async def describe_custom_routing_endpoint_async(
        self,
        request: main_models.DescribeCustomRoutingEndpointRequest,
    ) -> main_models.DescribeCustomRoutingEndpointResponse:
        runtime = RuntimeOptions()
        return await self.describe_custom_routing_endpoint_with_options_async(request, runtime)

    def describe_custom_routing_endpoint_group_with_options(
        self,
        request: main_models.DescribeCustomRoutingEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomRoutingEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomRoutingEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomRoutingEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_routing_endpoint_group_with_options_async(
        self,
        request: main_models.DescribeCustomRoutingEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomRoutingEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomRoutingEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomRoutingEndpointGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_routing_endpoint_group(
        self,
        request: main_models.DescribeCustomRoutingEndpointGroupRequest,
    ) -> main_models.DescribeCustomRoutingEndpointGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_custom_routing_endpoint_group_with_options(request, runtime)

    async def describe_custom_routing_endpoint_group_async(
        self,
        request: main_models.DescribeCustomRoutingEndpointGroupRequest,
    ) -> main_models.DescribeCustomRoutingEndpointGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_custom_routing_endpoint_group_with_options_async(request, runtime)

    def describe_custom_routing_endpoint_group_destinations_with_options(
        self,
        request: main_models.DescribeCustomRoutingEndpointGroupDestinationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomRoutingEndpointGroupDestinationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.destination_id):
            query['DestinationId'] = request.destination_id
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomRoutingEndpointGroupDestinations',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomRoutingEndpointGroupDestinationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_routing_endpoint_group_destinations_with_options_async(
        self,
        request: main_models.DescribeCustomRoutingEndpointGroupDestinationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomRoutingEndpointGroupDestinationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.destination_id):
            query['DestinationId'] = request.destination_id
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomRoutingEndpointGroupDestinations',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomRoutingEndpointGroupDestinationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_routing_endpoint_group_destinations(
        self,
        request: main_models.DescribeCustomRoutingEndpointGroupDestinationsRequest,
    ) -> main_models.DescribeCustomRoutingEndpointGroupDestinationsResponse:
        runtime = RuntimeOptions()
        return self.describe_custom_routing_endpoint_group_destinations_with_options(request, runtime)

    async def describe_custom_routing_endpoint_group_destinations_async(
        self,
        request: main_models.DescribeCustomRoutingEndpointGroupDestinationsRequest,
    ) -> main_models.DescribeCustomRoutingEndpointGroupDestinationsResponse:
        runtime = RuntimeOptions()
        return await self.describe_custom_routing_endpoint_group_destinations_with_options_async(request, runtime)

    def describe_endpoint_group_with_options(
        self,
        request: main_models.DescribeEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_endpoint_group_with_options_async(
        self,
        request: main_models.DescribeEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEndpointGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_endpoint_group(
        self,
        request: main_models.DescribeEndpointGroupRequest,
    ) -> main_models.DescribeEndpointGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_endpoint_group_with_options(request, runtime)

    async def describe_endpoint_group_async(
        self,
        request: main_models.DescribeEndpointGroupRequest,
    ) -> main_models.DescribeEndpointGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_endpoint_group_with_options_async(request, runtime)

    def describe_ip_set_with_options(
        self,
        request: main_models.DescribeIpSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpSet',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_set_with_options_async(
        self,
        request: main_models.DescribeIpSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpSet',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_set(
        self,
        request: main_models.DescribeIpSetRequest,
    ) -> main_models.DescribeIpSetResponse:
        runtime = RuntimeOptions()
        return self.describe_ip_set_with_options(request, runtime)

    async def describe_ip_set_async(
        self,
        request: main_models.DescribeIpSetRequest,
    ) -> main_models.DescribeIpSetResponse:
        runtime = RuntimeOptions()
        return await self.describe_ip_set_with_options_async(request, runtime)

    def describe_listener_with_options(
        self,
        request: main_models.DescribeListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeListenerResponse:
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
            action = 'DescribeListener',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_listener_with_options_async(
        self,
        request: main_models.DescribeListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeListenerResponse:
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
            action = 'DescribeListener',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_listener(
        self,
        request: main_models.DescribeListenerRequest,
    ) -> main_models.DescribeListenerResponse:
        runtime = RuntimeOptions()
        return self.describe_listener_with_options(request, runtime)

    async def describe_listener_async(
        self,
        request: main_models.DescribeListenerRequest,
    ) -> main_models.DescribeListenerResponse:
        runtime = RuntimeOptions()
        return await self.describe_listener_with_options_async(request, runtime)

    def describe_log_store_of_endpoint_group_with_options(
        self,
        request: main_models.DescribeLogStoreOfEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogStoreOfEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogStoreOfEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogStoreOfEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_store_of_endpoint_group_with_options_async(
        self,
        request: main_models.DescribeLogStoreOfEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogStoreOfEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogStoreOfEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogStoreOfEndpointGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_store_of_endpoint_group(
        self,
        request: main_models.DescribeLogStoreOfEndpointGroupRequest,
    ) -> main_models.DescribeLogStoreOfEndpointGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_log_store_of_endpoint_group_with_options(request, runtime)

    async def describe_log_store_of_endpoint_group_async(
        self,
        request: main_models.DescribeLogStoreOfEndpointGroupRequest,
    ) -> main_models.DescribeLogStoreOfEndpointGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_log_store_of_endpoint_group_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-11-20',
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

    def detach_ddos_from_accelerator_with_options(
        self,
        request: main_models.DetachDdosFromAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachDdosFromAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.ddos_config_list):
            query['DdosConfigList'] = request.ddos_config_list
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachDdosFromAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachDdosFromAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_ddos_from_accelerator_with_options_async(
        self,
        request: main_models.DetachDdosFromAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachDdosFromAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.ddos_config_list):
            query['DdosConfigList'] = request.ddos_config_list
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachDdosFromAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachDdosFromAcceleratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_ddos_from_accelerator(
        self,
        request: main_models.DetachDdosFromAcceleratorRequest,
    ) -> main_models.DetachDdosFromAcceleratorResponse:
        runtime = RuntimeOptions()
        return self.detach_ddos_from_accelerator_with_options(request, runtime)

    async def detach_ddos_from_accelerator_async(
        self,
        request: main_models.DetachDdosFromAcceleratorRequest,
    ) -> main_models.DetachDdosFromAcceleratorResponse:
        runtime = RuntimeOptions()
        return await self.detach_ddos_from_accelerator_with_options_async(request, runtime)

    def detach_log_store_from_endpoint_group_with_options(
        self,
        request: main_models.DetachLogStoreFromEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachLogStoreFromEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_ids):
            query['EndpointGroupIds'] = request.endpoint_group_ids
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachLogStoreFromEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachLogStoreFromEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_log_store_from_endpoint_group_with_options_async(
        self,
        request: main_models.DetachLogStoreFromEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachLogStoreFromEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_ids):
            query['EndpointGroupIds'] = request.endpoint_group_ids
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachLogStoreFromEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachLogStoreFromEndpointGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_log_store_from_endpoint_group(
        self,
        request: main_models.DetachLogStoreFromEndpointGroupRequest,
    ) -> main_models.DetachLogStoreFromEndpointGroupResponse:
        runtime = RuntimeOptions()
        return self.detach_log_store_from_endpoint_group_with_options(request, runtime)

    async def detach_log_store_from_endpoint_group_async(
        self,
        request: main_models.DetachLogStoreFromEndpointGroupRequest,
    ) -> main_models.DetachLogStoreFromEndpointGroupResponse:
        runtime = RuntimeOptions()
        return await self.detach_log_store_from_endpoint_group_with_options_async(request, runtime)

    def detect_application_monitor_with_options(
        self,
        request: main_models.DetectApplicationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectApplicationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectApplicationMonitor',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectApplicationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_application_monitor_with_options_async(
        self,
        request: main_models.DetectApplicationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectApplicationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectApplicationMonitor',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectApplicationMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_application_monitor(
        self,
        request: main_models.DetectApplicationMonitorRequest,
    ) -> main_models.DetectApplicationMonitorResponse:
        runtime = RuntimeOptions()
        return self.detect_application_monitor_with_options(request, runtime)

    async def detect_application_monitor_async(
        self,
        request: main_models.DetectApplicationMonitorRequest,
    ) -> main_models.DetectApplicationMonitorResponse:
        runtime = RuntimeOptions()
        return await self.detect_application_monitor_with_options_async(request, runtime)

    def disable_application_monitor_with_options(
        self,
        request: main_models.DisableApplicationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationMonitor',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_monitor_with_options_async(
        self,
        request: main_models.DisableApplicationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationMonitor',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_monitor(
        self,
        request: main_models.DisableApplicationMonitorRequest,
    ) -> main_models.DisableApplicationMonitorResponse:
        runtime = RuntimeOptions()
        return self.disable_application_monitor_with_options(request, runtime)

    async def disable_application_monitor_async(
        self,
        request: main_models.DisableApplicationMonitorRequest,
    ) -> main_models.DisableApplicationMonitorResponse:
        runtime = RuntimeOptions()
        return await self.disable_application_monitor_with_options_async(request, runtime)

    def disassociate_resources_with_options(
        self,
        request: main_models.DisassociateResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.associated_resource_id):
            query['AssociatedResourceId'] = request.associated_resource_id
        if not DaraCore.is_null(request.associated_resource_region_id):
            query['AssociatedResourceRegionId'] = request.associated_resource_region_id
        if not DaraCore.is_null(request.associated_resource_type):
            query['AssociatedResourceType'] = request.associated_resource_type
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateResources',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_resources_with_options_async(
        self,
        request: main_models.DisassociateResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.associated_resource_id):
            query['AssociatedResourceId'] = request.associated_resource_id
        if not DaraCore.is_null(request.associated_resource_region_id):
            query['AssociatedResourceRegionId'] = request.associated_resource_region_id
        if not DaraCore.is_null(request.associated_resource_type):
            query['AssociatedResourceType'] = request.associated_resource_type
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateResources',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_resources(
        self,
        request: main_models.DisassociateResourcesRequest,
    ) -> main_models.DisassociateResourcesResponse:
        runtime = RuntimeOptions()
        return self.disassociate_resources_with_options(request, runtime)

    async def disassociate_resources_async(
        self,
        request: main_models.DisassociateResourcesRequest,
    ) -> main_models.DisassociateResourcesResponse:
        runtime = RuntimeOptions()
        return await self.disassociate_resources_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DissociateAclsFromListener',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DissociateAclsFromListener',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DissociateAdditionalCertificatesFromListener',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.domains):
            query['Domains'] = request.domains
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DissociateAdditionalCertificatesFromListener',
            version = '2019-11-20',
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

    def enable_application_monitor_with_options(
        self,
        request: main_models.EnableApplicationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationMonitor',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_monitor_with_options_async(
        self,
        request: main_models.EnableApplicationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationMonitor',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_monitor(
        self,
        request: main_models.EnableApplicationMonitorRequest,
    ) -> main_models.EnableApplicationMonitorResponse:
        runtime = RuntimeOptions()
        return self.enable_application_monitor_with_options(request, runtime)

    async def enable_application_monitor_async(
        self,
        request: main_models.EnableApplicationMonitorRequest,
    ) -> main_models.EnableApplicationMonitorResponse:
        runtime = RuntimeOptions()
        return await self.enable_application_monitor_with_options_async(request, runtime)

    def get_acl_with_options(
        self,
        request: main_models.GetAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAcl',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_acl_with_options_async(
        self,
        request: main_models.GetAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAcl',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_acl(
        self,
        request: main_models.GetAclRequest,
    ) -> main_models.GetAclResponse:
        runtime = RuntimeOptions()
        return self.get_acl_with_options(request, runtime)

    async def get_acl_async(
        self,
        request: main_models.GetAclRequest,
    ) -> main_models.GetAclResponse:
        runtime = RuntimeOptions()
        return await self.get_acl_with_options_async(request, runtime)

    def get_basic_accelerate_ip_with_options(
        self,
        request: main_models.GetBasicAccelerateIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBasicAccelerateIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBasicAccelerateIp',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBasicAccelerateIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_basic_accelerate_ip_with_options_async(
        self,
        request: main_models.GetBasicAccelerateIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBasicAccelerateIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBasicAccelerateIp',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBasicAccelerateIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_basic_accelerate_ip(
        self,
        request: main_models.GetBasicAccelerateIpRequest,
    ) -> main_models.GetBasicAccelerateIpResponse:
        runtime = RuntimeOptions()
        return self.get_basic_accelerate_ip_with_options(request, runtime)

    async def get_basic_accelerate_ip_async(
        self,
        request: main_models.GetBasicAccelerateIpRequest,
    ) -> main_models.GetBasicAccelerateIpResponse:
        runtime = RuntimeOptions()
        return await self.get_basic_accelerate_ip_with_options_async(request, runtime)

    def get_basic_accelerate_ip_endpoint_relation_with_options(
        self,
        request: main_models.GetBasicAccelerateIpEndpointRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBasicAccelerateIpEndpointRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBasicAccelerateIpEndpointRelation',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBasicAccelerateIpEndpointRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_basic_accelerate_ip_endpoint_relation_with_options_async(
        self,
        request: main_models.GetBasicAccelerateIpEndpointRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBasicAccelerateIpEndpointRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBasicAccelerateIpEndpointRelation',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBasicAccelerateIpEndpointRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_basic_accelerate_ip_endpoint_relation(
        self,
        request: main_models.GetBasicAccelerateIpEndpointRelationRequest,
    ) -> main_models.GetBasicAccelerateIpEndpointRelationResponse:
        runtime = RuntimeOptions()
        return self.get_basic_accelerate_ip_endpoint_relation_with_options(request, runtime)

    async def get_basic_accelerate_ip_endpoint_relation_async(
        self,
        request: main_models.GetBasicAccelerateIpEndpointRelationRequest,
    ) -> main_models.GetBasicAccelerateIpEndpointRelationResponse:
        runtime = RuntimeOptions()
        return await self.get_basic_accelerate_ip_endpoint_relation_with_options_async(request, runtime)

    def get_basic_accelerate_ip_idle_count_with_options(
        self,
        request: main_models.GetBasicAccelerateIpIdleCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBasicAccelerateIpIdleCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBasicAccelerateIpIdleCount',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBasicAccelerateIpIdleCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_basic_accelerate_ip_idle_count_with_options_async(
        self,
        request: main_models.GetBasicAccelerateIpIdleCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBasicAccelerateIpIdleCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBasicAccelerateIpIdleCount',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBasicAccelerateIpIdleCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_basic_accelerate_ip_idle_count(
        self,
        request: main_models.GetBasicAccelerateIpIdleCountRequest,
    ) -> main_models.GetBasicAccelerateIpIdleCountResponse:
        runtime = RuntimeOptions()
        return self.get_basic_accelerate_ip_idle_count_with_options(request, runtime)

    async def get_basic_accelerate_ip_idle_count_async(
        self,
        request: main_models.GetBasicAccelerateIpIdleCountRequest,
    ) -> main_models.GetBasicAccelerateIpIdleCountResponse:
        runtime = RuntimeOptions()
        return await self.get_basic_accelerate_ip_idle_count_with_options_async(request, runtime)

    def get_basic_accelerator_with_options(
        self,
        request: main_models.GetBasicAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBasicAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBasicAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBasicAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_basic_accelerator_with_options_async(
        self,
        request: main_models.GetBasicAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBasicAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBasicAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBasicAcceleratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_basic_accelerator(
        self,
        request: main_models.GetBasicAcceleratorRequest,
    ) -> main_models.GetBasicAcceleratorResponse:
        runtime = RuntimeOptions()
        return self.get_basic_accelerator_with_options(request, runtime)

    async def get_basic_accelerator_async(
        self,
        request: main_models.GetBasicAcceleratorRequest,
    ) -> main_models.GetBasicAcceleratorResponse:
        runtime = RuntimeOptions()
        return await self.get_basic_accelerator_with_options_async(request, runtime)

    def get_basic_endpoint_with_options(
        self,
        request: main_models.GetBasicEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBasicEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBasicEndpoint',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBasicEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_basic_endpoint_with_options_async(
        self,
        request: main_models.GetBasicEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBasicEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBasicEndpoint',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBasicEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_basic_endpoint(
        self,
        request: main_models.GetBasicEndpointRequest,
    ) -> main_models.GetBasicEndpointResponse:
        runtime = RuntimeOptions()
        return self.get_basic_endpoint_with_options(request, runtime)

    async def get_basic_endpoint_async(
        self,
        request: main_models.GetBasicEndpointRequest,
    ) -> main_models.GetBasicEndpointResponse:
        runtime = RuntimeOptions()
        return await self.get_basic_endpoint_with_options_async(request, runtime)

    def get_basic_endpoint_group_with_options(
        self,
        request: main_models.GetBasicEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBasicEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBasicEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBasicEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_basic_endpoint_group_with_options_async(
        self,
        request: main_models.GetBasicEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBasicEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBasicEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBasicEndpointGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_basic_endpoint_group(
        self,
        request: main_models.GetBasicEndpointGroupRequest,
    ) -> main_models.GetBasicEndpointGroupResponse:
        runtime = RuntimeOptions()
        return self.get_basic_endpoint_group_with_options(request, runtime)

    async def get_basic_endpoint_group_async(
        self,
        request: main_models.GetBasicEndpointGroupRequest,
    ) -> main_models.GetBasicEndpointGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_basic_endpoint_group_with_options_async(request, runtime)

    def get_basic_ip_set_with_options(
        self,
        request: main_models.GetBasicIpSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBasicIpSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBasicIpSet',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBasicIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_basic_ip_set_with_options_async(
        self,
        request: main_models.GetBasicIpSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBasicIpSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBasicIpSet',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBasicIpSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_basic_ip_set(
        self,
        request: main_models.GetBasicIpSetRequest,
    ) -> main_models.GetBasicIpSetResponse:
        runtime = RuntimeOptions()
        return self.get_basic_ip_set_with_options(request, runtime)

    async def get_basic_ip_set_async(
        self,
        request: main_models.GetBasicIpSetRequest,
    ) -> main_models.GetBasicIpSetResponse:
        runtime = RuntimeOptions()
        return await self.get_basic_ip_set_with_options_async(request, runtime)

    def get_global_accelerator_resources_with_options(
        self,
        request: main_models.GetGlobalAcceleratorResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGlobalAcceleratorResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.associated_resource_id):
            query['AssociatedResourceId'] = request.associated_resource_id
        if not DaraCore.is_null(request.associated_resource_region_id):
            query['AssociatedResourceRegionId'] = request.associated_resource_region_id
        if not DaraCore.is_null(request.associated_resource_type):
            query['AssociatedResourceType'] = request.associated_resource_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGlobalAcceleratorResources',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGlobalAcceleratorResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_global_accelerator_resources_with_options_async(
        self,
        request: main_models.GetGlobalAcceleratorResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGlobalAcceleratorResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.associated_resource_id):
            query['AssociatedResourceId'] = request.associated_resource_id
        if not DaraCore.is_null(request.associated_resource_region_id):
            query['AssociatedResourceRegionId'] = request.associated_resource_region_id
        if not DaraCore.is_null(request.associated_resource_type):
            query['AssociatedResourceType'] = request.associated_resource_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGlobalAcceleratorResources',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGlobalAcceleratorResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_global_accelerator_resources(
        self,
        request: main_models.GetGlobalAcceleratorResourcesRequest,
    ) -> main_models.GetGlobalAcceleratorResourcesResponse:
        runtime = RuntimeOptions()
        return self.get_global_accelerator_resources_with_options(request, runtime)

    async def get_global_accelerator_resources_async(
        self,
        request: main_models.GetGlobalAcceleratorResourcesRequest,
    ) -> main_models.GetGlobalAcceleratorResourcesResponse:
        runtime = RuntimeOptions()
        return await self.get_global_accelerator_resources_with_options_async(request, runtime)

    def get_health_status_with_options(
        self,
        request: main_models.GetHealthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHealthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
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
            action = 'GetHealthStatus',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_health_status_with_options_async(
        self,
        request: main_models.GetHealthStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHealthStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
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
            action = 'GetHealthStatus',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_health_status(
        self,
        request: main_models.GetHealthStatusRequest,
    ) -> main_models.GetHealthStatusResponse:
        runtime = RuntimeOptions()
        return self.get_health_status_with_options(request, runtime)

    async def get_health_status_async(
        self,
        request: main_models.GetHealthStatusRequest,
    ) -> main_models.GetHealthStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_health_status_with_options_async(request, runtime)

    def get_invalid_domain_count_with_options(
        self,
        request: main_models.GetInvalidDomainCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInvalidDomainCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInvalidDomainCount',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInvalidDomainCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_invalid_domain_count_with_options_async(
        self,
        request: main_models.GetInvalidDomainCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInvalidDomainCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInvalidDomainCount',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInvalidDomainCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_invalid_domain_count(
        self,
        request: main_models.GetInvalidDomainCountRequest,
    ) -> main_models.GetInvalidDomainCountResponse:
        runtime = RuntimeOptions()
        return self.get_invalid_domain_count_with_options(request, runtime)

    async def get_invalid_domain_count_async(
        self,
        request: main_models.GetInvalidDomainCountRequest,
    ) -> main_models.GetInvalidDomainCountResponse:
        runtime = RuntimeOptions()
        return await self.get_invalid_domain_count_with_options_async(request, runtime)

    def get_ipsets_bandwidth_limit_with_options(
        self,
        request: main_models.GetIpsetsBandwidthLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIpsetsBandwidthLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIpsetsBandwidthLimit',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIpsetsBandwidthLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ipsets_bandwidth_limit_with_options_async(
        self,
        request: main_models.GetIpsetsBandwidthLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIpsetsBandwidthLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIpsetsBandwidthLimit',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIpsetsBandwidthLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ipsets_bandwidth_limit(
        self,
        request: main_models.GetIpsetsBandwidthLimitRequest,
    ) -> main_models.GetIpsetsBandwidthLimitResponse:
        runtime = RuntimeOptions()
        return self.get_ipsets_bandwidth_limit_with_options(request, runtime)

    async def get_ipsets_bandwidth_limit_async(
        self,
        request: main_models.GetIpsetsBandwidthLimitRequest,
    ) -> main_models.GetIpsetsBandwidthLimitResponse:
        runtime = RuntimeOptions()
        return await self.get_ipsets_bandwidth_limit_with_options_async(request, runtime)

    def get_spare_ip_with_options(
        self,
        request: main_models.GetSpareIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSpareIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.spare_ip):
            query['SpareIp'] = request.spare_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSpareIp',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSpareIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spare_ip_with_options_async(
        self,
        request: main_models.GetSpareIpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSpareIpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.spare_ip):
            query['SpareIp'] = request.spare_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSpareIp',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSpareIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spare_ip(
        self,
        request: main_models.GetSpareIpRequest,
    ) -> main_models.GetSpareIpResponse:
        runtime = RuntimeOptions()
        return self.get_spare_ip_with_options(request, runtime)

    async def get_spare_ip_async(
        self,
        request: main_models.GetSpareIpRequest,
    ) -> main_models.GetSpareIpResponse:
        runtime = RuntimeOptions()
        return await self.get_spare_ip_with_options_async(request, runtime)

    def list_accelerate_areas_with_options(
        self,
        request: main_models.ListAccelerateAreasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccelerateAreasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccelerateAreas',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccelerateAreasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_accelerate_areas_with_options_async(
        self,
        request: main_models.ListAccelerateAreasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccelerateAreasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccelerateAreas',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccelerateAreasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_accelerate_areas(
        self,
        request: main_models.ListAccelerateAreasRequest,
    ) -> main_models.ListAccelerateAreasResponse:
        runtime = RuntimeOptions()
        return self.list_accelerate_areas_with_options(request, runtime)

    async def list_accelerate_areas_async(
        self,
        request: main_models.ListAccelerateAreasRequest,
    ) -> main_models.ListAccelerateAreasResponse:
        runtime = RuntimeOptions()
        return await self.list_accelerate_areas_with_options_async(request, runtime)

    def list_accelerators_with_options(
        self,
        request: main_models.ListAcceleratorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAcceleratorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccelerators',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAcceleratorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_accelerators_with_options_async(
        self,
        request: main_models.ListAcceleratorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAcceleratorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccelerators',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAcceleratorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_accelerators(
        self,
        request: main_models.ListAcceleratorsRequest,
    ) -> main_models.ListAcceleratorsResponse:
        runtime = RuntimeOptions()
        return self.list_accelerators_with_options(request, runtime)

    async def list_accelerators_async(
        self,
        request: main_models.ListAcceleratorsRequest,
    ) -> main_models.ListAcceleratorsResponse:
        runtime = RuntimeOptions()
        return await self.list_accelerators_with_options_async(request, runtime)

    def list_acls_with_options(
        self,
        request: main_models.ListAclsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAclsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_ids):
            query['AclIds'] = request.acl_ids
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAcls',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.acl_name):
            query['AclName'] = request.acl_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAcls',
            version = '2019-11-20',
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

    def list_application_monitor_with_options(
        self,
        request: main_models.ListApplicationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationMonitor',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_monitor_with_options_async(
        self,
        request: main_models.ListApplicationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationMonitor',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_monitor(
        self,
        request: main_models.ListApplicationMonitorRequest,
    ) -> main_models.ListApplicationMonitorResponse:
        runtime = RuntimeOptions()
        return self.list_application_monitor_with_options(request, runtime)

    async def list_application_monitor_async(
        self,
        request: main_models.ListApplicationMonitorRequest,
    ) -> main_models.ListApplicationMonitorResponse:
        runtime = RuntimeOptions()
        return await self.list_application_monitor_with_options_async(request, runtime)

    def list_application_monitor_detect_result_with_options(
        self,
        request: main_models.ListApplicationMonitorDetectResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationMonitorDetectResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationMonitorDetectResult',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationMonitorDetectResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_monitor_detect_result_with_options_async(
        self,
        request: main_models.ListApplicationMonitorDetectResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationMonitorDetectResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationMonitorDetectResult',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationMonitorDetectResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_monitor_detect_result(
        self,
        request: main_models.ListApplicationMonitorDetectResultRequest,
    ) -> main_models.ListApplicationMonitorDetectResultResponse:
        runtime = RuntimeOptions()
        return self.list_application_monitor_detect_result_with_options(request, runtime)

    async def list_application_monitor_detect_result_async(
        self,
        request: main_models.ListApplicationMonitorDetectResultRequest,
    ) -> main_models.ListApplicationMonitorDetectResultResponse:
        runtime = RuntimeOptions()
        return await self.list_application_monitor_detect_result_with_options_async(request, runtime)

    def list_available_accelerate_areas_with_options(
        self,
        request: main_models.ListAvailableAccelerateAreasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableAccelerateAreasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableAccelerateAreas',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableAccelerateAreasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_accelerate_areas_with_options_async(
        self,
        request: main_models.ListAvailableAccelerateAreasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableAccelerateAreasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.access_mode):
            query['AccessMode'] = request.access_mode
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableAccelerateAreas',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableAccelerateAreasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_accelerate_areas(
        self,
        request: main_models.ListAvailableAccelerateAreasRequest,
    ) -> main_models.ListAvailableAccelerateAreasResponse:
        runtime = RuntimeOptions()
        return self.list_available_accelerate_areas_with_options(request, runtime)

    async def list_available_accelerate_areas_async(
        self,
        request: main_models.ListAvailableAccelerateAreasRequest,
    ) -> main_models.ListAvailableAccelerateAreasResponse:
        runtime = RuntimeOptions()
        return await self.list_available_accelerate_areas_with_options_async(request, runtime)

    def list_available_busi_regions_with_options(
        self,
        request: main_models.ListAvailableBusiRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableBusiRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableBusiRegions',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableBusiRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_busi_regions_with_options_async(
        self,
        request: main_models.ListAvailableBusiRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableBusiRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableBusiRegions',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableBusiRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_busi_regions(
        self,
        request: main_models.ListAvailableBusiRegionsRequest,
    ) -> main_models.ListAvailableBusiRegionsResponse:
        runtime = RuntimeOptions()
        return self.list_available_busi_regions_with_options(request, runtime)

    async def list_available_busi_regions_async(
        self,
        request: main_models.ListAvailableBusiRegionsRequest,
    ) -> main_models.ListAvailableBusiRegionsResponse:
        runtime = RuntimeOptions()
        return await self.list_available_busi_regions_with_options_async(request, runtime)

    def list_bandwidth_packages_with_options(
        self,
        request: main_models.ListBandwidthPackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBandwidthPackagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBandwidthPackages',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBandwidthPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bandwidth_packages_with_options_async(
        self,
        request: main_models.ListBandwidthPackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBandwidthPackagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBandwidthPackages',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBandwidthPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_bandwidth_packages(
        self,
        request: main_models.ListBandwidthPackagesRequest,
    ) -> main_models.ListBandwidthPackagesResponse:
        runtime = RuntimeOptions()
        return self.list_bandwidth_packages_with_options(request, runtime)

    async def list_bandwidth_packages_async(
        self,
        request: main_models.ListBandwidthPackagesRequest,
    ) -> main_models.ListBandwidthPackagesResponse:
        runtime = RuntimeOptions()
        return await self.list_bandwidth_packages_with_options_async(request, runtime)

    def list_bandwidthackages_with_options(
        self,
        request: main_models.ListBandwidthackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBandwidthackagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBandwidthackages',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBandwidthackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bandwidthackages_with_options_async(
        self,
        request: main_models.ListBandwidthackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBandwidthackagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBandwidthackages',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBandwidthackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_bandwidthackages(
        self,
        request: main_models.ListBandwidthackagesRequest,
    ) -> main_models.ListBandwidthackagesResponse:
        runtime = RuntimeOptions()
        return self.list_bandwidthackages_with_options(request, runtime)

    async def list_bandwidthackages_async(
        self,
        request: main_models.ListBandwidthackagesRequest,
    ) -> main_models.ListBandwidthackagesResponse:
        runtime = RuntimeOptions()
        return await self.list_bandwidthackages_with_options_async(request, runtime)

    def list_basic_accelerate_ip_endpoint_relations_with_options(
        self,
        request: main_models.ListBasicAccelerateIpEndpointRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBasicAccelerateIpEndpointRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBasicAccelerateIpEndpointRelations',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBasicAccelerateIpEndpointRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_basic_accelerate_ip_endpoint_relations_with_options_async(
        self,
        request: main_models.ListBasicAccelerateIpEndpointRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBasicAccelerateIpEndpointRelationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBasicAccelerateIpEndpointRelations',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBasicAccelerateIpEndpointRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_basic_accelerate_ip_endpoint_relations(
        self,
        request: main_models.ListBasicAccelerateIpEndpointRelationsRequest,
    ) -> main_models.ListBasicAccelerateIpEndpointRelationsResponse:
        runtime = RuntimeOptions()
        return self.list_basic_accelerate_ip_endpoint_relations_with_options(request, runtime)

    async def list_basic_accelerate_ip_endpoint_relations_async(
        self,
        request: main_models.ListBasicAccelerateIpEndpointRelationsRequest,
    ) -> main_models.ListBasicAccelerateIpEndpointRelationsResponse:
        runtime = RuntimeOptions()
        return await self.list_basic_accelerate_ip_endpoint_relations_with_options_async(request, runtime)

    def list_basic_accelerate_ips_with_options(
        self,
        request: main_models.ListBasicAccelerateIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBasicAccelerateIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_ip_address):
            query['AccelerateIpAddress'] = request.accelerate_ip_address
        if not DaraCore.is_null(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBasicAccelerateIps',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBasicAccelerateIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_basic_accelerate_ips_with_options_async(
        self,
        request: main_models.ListBasicAccelerateIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBasicAccelerateIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate_ip_address):
            query['AccelerateIpAddress'] = request.accelerate_ip_address
        if not DaraCore.is_null(request.accelerate_ip_id):
            query['AccelerateIpId'] = request.accelerate_ip_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBasicAccelerateIps',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBasicAccelerateIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_basic_accelerate_ips(
        self,
        request: main_models.ListBasicAccelerateIpsRequest,
    ) -> main_models.ListBasicAccelerateIpsResponse:
        runtime = RuntimeOptions()
        return self.list_basic_accelerate_ips_with_options(request, runtime)

    async def list_basic_accelerate_ips_async(
        self,
        request: main_models.ListBasicAccelerateIpsRequest,
    ) -> main_models.ListBasicAccelerateIpsResponse:
        runtime = RuntimeOptions()
        return await self.list_basic_accelerate_ips_with_options_async(request, runtime)

    def list_basic_accelerators_with_options(
        self,
        request: main_models.ListBasicAcceleratorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBasicAcceleratorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBasicAccelerators',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBasicAcceleratorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_basic_accelerators_with_options_async(
        self,
        request: main_models.ListBasicAcceleratorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBasicAcceleratorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBasicAccelerators',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBasicAcceleratorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_basic_accelerators(
        self,
        request: main_models.ListBasicAcceleratorsRequest,
    ) -> main_models.ListBasicAcceleratorsResponse:
        runtime = RuntimeOptions()
        return self.list_basic_accelerators_with_options(request, runtime)

    async def list_basic_accelerators_async(
        self,
        request: main_models.ListBasicAcceleratorsRequest,
    ) -> main_models.ListBasicAcceleratorsResponse:
        runtime = RuntimeOptions()
        return await self.list_basic_accelerators_with_options_async(request, runtime)

    def list_basic_endpoints_with_options(
        self,
        request: main_models.ListBasicEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBasicEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBasicEndpoints',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBasicEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_basic_endpoints_with_options_async(
        self,
        request: main_models.ListBasicEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBasicEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBasicEndpoints',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBasicEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_basic_endpoints(
        self,
        request: main_models.ListBasicEndpointsRequest,
    ) -> main_models.ListBasicEndpointsResponse:
        runtime = RuntimeOptions()
        return self.list_basic_endpoints_with_options(request, runtime)

    async def list_basic_endpoints_async(
        self,
        request: main_models.ListBasicEndpointsRequest,
    ) -> main_models.ListBasicEndpointsResponse:
        runtime = RuntimeOptions()
        return await self.list_basic_endpoints_with_options_async(request, runtime)

    def list_busi_regions_with_options(
        self,
        request: main_models.ListBusiRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBusiRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBusiRegions',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBusiRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_busi_regions_with_options_async(
        self,
        request: main_models.ListBusiRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBusiRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBusiRegions',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBusiRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_busi_regions(
        self,
        request: main_models.ListBusiRegionsRequest,
    ) -> main_models.ListBusiRegionsResponse:
        runtime = RuntimeOptions()
        return self.list_busi_regions_with_options(request, runtime)

    async def list_busi_regions_async(
        self,
        request: main_models.ListBusiRegionsRequest,
    ) -> main_models.ListBusiRegionsResponse:
        runtime = RuntimeOptions()
        return await self.list_busi_regions_with_options_async(request, runtime)

    def list_common_areas_with_options(
        self,
        request: main_models.ListCommonAreasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCommonAreasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.is_epg):
            query['IsEpg'] = request.is_epg
        if not DaraCore.is_null(request.is_ip_set):
            query['IsIpSet'] = request.is_ip_set
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCommonAreas',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCommonAreasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_common_areas_with_options_async(
        self,
        request: main_models.ListCommonAreasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCommonAreasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not DaraCore.is_null(request.is_epg):
            query['IsEpg'] = request.is_epg
        if not DaraCore.is_null(request.is_ip_set):
            query['IsIpSet'] = request.is_ip_set
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCommonAreas',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCommonAreasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_common_areas(
        self,
        request: main_models.ListCommonAreasRequest,
    ) -> main_models.ListCommonAreasResponse:
        runtime = RuntimeOptions()
        return self.list_common_areas_with_options(request, runtime)

    async def list_common_areas_async(
        self,
        request: main_models.ListCommonAreasRequest,
    ) -> main_models.ListCommonAreasResponse:
        runtime = RuntimeOptions()
        return await self.list_common_areas_with_options_async(request, runtime)

    def list_custom_routing_endpoint_group_destinations_with_options(
        self,
        request: main_models.ListCustomRoutingEndpointGroupDestinationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomRoutingEndpointGroupDestinationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.from_port):
            query['FromPort'] = request.from_port
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.protocols):
            query['Protocols'] = request.protocols
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.to_port):
            query['ToPort'] = request.to_port
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomRoutingEndpointGroupDestinations',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomRoutingEndpointGroupDestinationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_routing_endpoint_group_destinations_with_options_async(
        self,
        request: main_models.ListCustomRoutingEndpointGroupDestinationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomRoutingEndpointGroupDestinationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.from_port):
            query['FromPort'] = request.from_port
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.protocols):
            query['Protocols'] = request.protocols
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.to_port):
            query['ToPort'] = request.to_port
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomRoutingEndpointGroupDestinations',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomRoutingEndpointGroupDestinationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_routing_endpoint_group_destinations(
        self,
        request: main_models.ListCustomRoutingEndpointGroupDestinationsRequest,
    ) -> main_models.ListCustomRoutingEndpointGroupDestinationsResponse:
        runtime = RuntimeOptions()
        return self.list_custom_routing_endpoint_group_destinations_with_options(request, runtime)

    async def list_custom_routing_endpoint_group_destinations_async(
        self,
        request: main_models.ListCustomRoutingEndpointGroupDestinationsRequest,
    ) -> main_models.ListCustomRoutingEndpointGroupDestinationsResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_routing_endpoint_group_destinations_with_options_async(request, runtime)

    def list_custom_routing_endpoint_groups_with_options(
        self,
        request: main_models.ListCustomRoutingEndpointGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomRoutingEndpointGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.access_log_switch):
            query['AccessLogSwitch'] = request.access_log_switch
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomRoutingEndpointGroups',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomRoutingEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_routing_endpoint_groups_with_options_async(
        self,
        request: main_models.ListCustomRoutingEndpointGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomRoutingEndpointGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.access_log_switch):
            query['AccessLogSwitch'] = request.access_log_switch
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomRoutingEndpointGroups',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomRoutingEndpointGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_routing_endpoint_groups(
        self,
        request: main_models.ListCustomRoutingEndpointGroupsRequest,
    ) -> main_models.ListCustomRoutingEndpointGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_custom_routing_endpoint_groups_with_options(request, runtime)

    async def list_custom_routing_endpoint_groups_async(
        self,
        request: main_models.ListCustomRoutingEndpointGroupsRequest,
    ) -> main_models.ListCustomRoutingEndpointGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_routing_endpoint_groups_with_options_async(request, runtime)

    def list_custom_routing_endpoint_traffic_policies_with_options(
        self,
        request: main_models.ListCustomRoutingEndpointTrafficPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomRoutingEndpointTrafficPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomRoutingEndpointTrafficPolicies',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomRoutingEndpointTrafficPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_routing_endpoint_traffic_policies_with_options_async(
        self,
        request: main_models.ListCustomRoutingEndpointTrafficPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomRoutingEndpointTrafficPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomRoutingEndpointTrafficPolicies',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomRoutingEndpointTrafficPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_routing_endpoint_traffic_policies(
        self,
        request: main_models.ListCustomRoutingEndpointTrafficPoliciesRequest,
    ) -> main_models.ListCustomRoutingEndpointTrafficPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_custom_routing_endpoint_traffic_policies_with_options(request, runtime)

    async def list_custom_routing_endpoint_traffic_policies_async(
        self,
        request: main_models.ListCustomRoutingEndpointTrafficPoliciesRequest,
    ) -> main_models.ListCustomRoutingEndpointTrafficPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_routing_endpoint_traffic_policies_with_options_async(request, runtime)

    def list_custom_routing_endpoints_with_options(
        self,
        request: main_models.ListCustomRoutingEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomRoutingEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomRoutingEndpoints',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomRoutingEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_routing_endpoints_with_options_async(
        self,
        request: main_models.ListCustomRoutingEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomRoutingEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomRoutingEndpoints',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomRoutingEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_routing_endpoints(
        self,
        request: main_models.ListCustomRoutingEndpointsRequest,
    ) -> main_models.ListCustomRoutingEndpointsResponse:
        runtime = RuntimeOptions()
        return self.list_custom_routing_endpoints_with_options(request, runtime)

    async def list_custom_routing_endpoints_async(
        self,
        request: main_models.ListCustomRoutingEndpointsRequest,
    ) -> main_models.ListCustomRoutingEndpointsResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_routing_endpoints_with_options_async(request, runtime)

    def list_custom_routing_port_mappings_with_options(
        self,
        request: main_models.ListCustomRoutingPortMappingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomRoutingPortMappingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomRoutingPortMappings',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomRoutingPortMappingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_routing_port_mappings_with_options_async(
        self,
        request: main_models.ListCustomRoutingPortMappingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomRoutingPortMappingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomRoutingPortMappings',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomRoutingPortMappingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_routing_port_mappings(
        self,
        request: main_models.ListCustomRoutingPortMappingsRequest,
    ) -> main_models.ListCustomRoutingPortMappingsResponse:
        runtime = RuntimeOptions()
        return self.list_custom_routing_port_mappings_with_options(request, runtime)

    async def list_custom_routing_port_mappings_async(
        self,
        request: main_models.ListCustomRoutingPortMappingsRequest,
    ) -> main_models.ListCustomRoutingPortMappingsResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_routing_port_mappings_with_options_async(request, runtime)

    def list_custom_routing_port_mappings_by_destination_with_options(
        self,
        request: main_models.ListCustomRoutingPortMappingsByDestinationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomRoutingPortMappingsByDestinationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.destination_address):
            query['DestinationAddress'] = request.destination_address
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomRoutingPortMappingsByDestination',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomRoutingPortMappingsByDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_routing_port_mappings_by_destination_with_options_async(
        self,
        request: main_models.ListCustomRoutingPortMappingsByDestinationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomRoutingPortMappingsByDestinationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.destination_address):
            query['DestinationAddress'] = request.destination_address
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomRoutingPortMappingsByDestination',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomRoutingPortMappingsByDestinationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_routing_port_mappings_by_destination(
        self,
        request: main_models.ListCustomRoutingPortMappingsByDestinationRequest,
    ) -> main_models.ListCustomRoutingPortMappingsByDestinationResponse:
        runtime = RuntimeOptions()
        return self.list_custom_routing_port_mappings_by_destination_with_options(request, runtime)

    async def list_custom_routing_port_mappings_by_destination_async(
        self,
        request: main_models.ListCustomRoutingPortMappingsByDestinationRequest,
    ) -> main_models.ListCustomRoutingPortMappingsByDestinationResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_routing_port_mappings_by_destination_with_options_async(request, runtime)

    def list_domains_with_options(
        self,
        request: main_models.ListDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDomains',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_domains_with_options_async(
        self,
        request: main_models.ListDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDomains',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_domains(
        self,
        request: main_models.ListDomainsRequest,
    ) -> main_models.ListDomainsResponse:
        runtime = RuntimeOptions()
        return self.list_domains_with_options(request, runtime)

    async def list_domains_async(
        self,
        request: main_models.ListDomainsRequest,
    ) -> main_models.ListDomainsResponse:
        runtime = RuntimeOptions()
        return await self.list_domains_with_options_async(request, runtime)

    def list_endpoint_group_ip_address_cidr_blocks_with_options(
        self,
        request: main_models.ListEndpointGroupIpAddressCidrBlocksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEndpointGroupIpAddressCidrBlocksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.endpoint_group_region):
            query['EndpointGroupRegion'] = request.endpoint_group_region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEndpointGroupIpAddressCidrBlocks',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEndpointGroupIpAddressCidrBlocksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_endpoint_group_ip_address_cidr_blocks_with_options_async(
        self,
        request: main_models.ListEndpointGroupIpAddressCidrBlocksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEndpointGroupIpAddressCidrBlocksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.endpoint_group_region):
            query['EndpointGroupRegion'] = request.endpoint_group_region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEndpointGroupIpAddressCidrBlocks',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEndpointGroupIpAddressCidrBlocksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_endpoint_group_ip_address_cidr_blocks(
        self,
        request: main_models.ListEndpointGroupIpAddressCidrBlocksRequest,
    ) -> main_models.ListEndpointGroupIpAddressCidrBlocksResponse:
        runtime = RuntimeOptions()
        return self.list_endpoint_group_ip_address_cidr_blocks_with_options(request, runtime)

    async def list_endpoint_group_ip_address_cidr_blocks_async(
        self,
        request: main_models.ListEndpointGroupIpAddressCidrBlocksRequest,
    ) -> main_models.ListEndpointGroupIpAddressCidrBlocksResponse:
        runtime = RuntimeOptions()
        return await self.list_endpoint_group_ip_address_cidr_blocks_with_options_async(request, runtime)

    def list_endpoint_groups_with_options(
        self,
        request: main_models.ListEndpointGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEndpointGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.access_log_switch):
            query['AccessLogSwitch'] = request.access_log_switch
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_group_type):
            query['EndpointGroupType'] = request.endpoint_group_type
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEndpointGroups',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_endpoint_groups_with_options_async(
        self,
        request: main_models.ListEndpointGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEndpointGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.access_log_switch):
            query['AccessLogSwitch'] = request.access_log_switch
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_group_type):
            query['EndpointGroupType'] = request.endpoint_group_type
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEndpointGroups',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEndpointGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_endpoint_groups(
        self,
        request: main_models.ListEndpointGroupsRequest,
    ) -> main_models.ListEndpointGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_endpoint_groups_with_options(request, runtime)

    async def list_endpoint_groups_async(
        self,
        request: main_models.ListEndpointGroupsRequest,
    ) -> main_models.ListEndpointGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_endpoint_groups_with_options_async(request, runtime)

    def list_forwarding_rules_with_options(
        self,
        request: main_models.ListForwardingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListForwardingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.forwarding_rule_id):
            query['ForwardingRuleId'] = request.forwarding_rule_id
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListForwardingRules',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListForwardingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_forwarding_rules_with_options_async(
        self,
        request: main_models.ListForwardingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListForwardingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.forwarding_rule_id):
            query['ForwardingRuleId'] = request.forwarding_rule_id
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListForwardingRules',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListForwardingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_forwarding_rules(
        self,
        request: main_models.ListForwardingRulesRequest,
    ) -> main_models.ListForwardingRulesResponse:
        runtime = RuntimeOptions()
        return self.list_forwarding_rules_with_options(request, runtime)

    async def list_forwarding_rules_async(
        self,
        request: main_models.ListForwardingRulesRequest,
    ) -> main_models.ListForwardingRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_forwarding_rules_with_options_async(request, runtime)

    def list_ip_sets_with_options(
        self,
        request: main_models.ListIpSetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpSetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpSets',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpSetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ip_sets_with_options_async(
        self,
        request: main_models.ListIpSetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIpSetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIpSets',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIpSetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ip_sets(
        self,
        request: main_models.ListIpSetsRequest,
    ) -> main_models.ListIpSetsResponse:
        runtime = RuntimeOptions()
        return self.list_ip_sets_with_options(request, runtime)

    async def list_ip_sets_async(
        self,
        request: main_models.ListIpSetsRequest,
    ) -> main_models.ListIpSetsResponse:
        runtime = RuntimeOptions()
        return await self.list_ip_sets_with_options_async(request, runtime)

    def list_isp_types_with_options(
        self,
        request: main_models.ListIspTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIspTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not DaraCore.is_null(request.business_region_id):
            query['BusinessRegionId'] = request.business_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIspTypes',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIspTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_isp_types_with_options_async(
        self,
        request: main_models.ListIspTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIspTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not DaraCore.is_null(request.business_region_id):
            query['BusinessRegionId'] = request.business_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIspTypes',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIspTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_isp_types(
        self,
        request: main_models.ListIspTypesRequest,
    ) -> main_models.ListIspTypesResponse:
        runtime = RuntimeOptions()
        return self.list_isp_types_with_options(request, runtime)

    async def list_isp_types_async(
        self,
        request: main_models.ListIspTypesRequest,
    ) -> main_models.ListIspTypesResponse:
        runtime = RuntimeOptions()
        return await self.list_isp_types_with_options_async(request, runtime)

    def list_listener_certificates_with_options(
        self,
        request: main_models.ListListenerCertificatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListListenerCertificatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListListenerCertificates',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListListenerCertificates',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListListeners',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListListeners',
            version = '2019-11-20',
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

    def list_spare_ips_with_options(
        self,
        request: main_models.ListSpareIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSpareIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSpareIps',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSpareIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_spare_ips_with_options_async(
        self,
        request: main_models.ListSpareIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSpareIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSpareIps',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSpareIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_spare_ips(
        self,
        request: main_models.ListSpareIpsRequest,
    ) -> main_models.ListSpareIpsResponse:
        runtime = RuntimeOptions()
        return self.list_spare_ips_with_options(request, runtime)

    async def list_spare_ips_async(
        self,
        request: main_models.ListSpareIpsRequest,
    ) -> main_models.ListSpareIpsResponse:
        runtime = RuntimeOptions()
        return await self.list_spare_ips_with_options_async(request, runtime)

    def list_system_security_policies_with_options(
        self,
        request: main_models.ListSystemSecurityPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSystemSecurityPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSystemSecurityPolicies',
            version = '2019-11-20',
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
        request: main_models.ListSystemSecurityPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSystemSecurityPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSystemSecurityPolicies',
            version = '2019-11-20',
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

    def list_system_security_policies(
        self,
        request: main_models.ListSystemSecurityPoliciesRequest,
    ) -> main_models.ListSystemSecurityPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_system_security_policies_with_options(request, runtime)

    async def list_system_security_policies_async(
        self,
        request: main_models.ListSystemSecurityPoliciesRequest,
    ) -> main_models.ListSystemSecurityPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_system_security_policies_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
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
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
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
            version = '2019-11-20',
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

    def open_accelerator_service_with_options(
        self,
        request: main_models.OpenAcceleratorServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenAcceleratorServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenAcceleratorService',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenAcceleratorServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_accelerator_service_with_options_async(
        self,
        request: main_models.OpenAcceleratorServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenAcceleratorServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenAcceleratorService',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenAcceleratorServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_accelerator_service(
        self,
        request: main_models.OpenAcceleratorServiceRequest,
    ) -> main_models.OpenAcceleratorServiceResponse:
        runtime = RuntimeOptions()
        return self.open_accelerator_service_with_options(request, runtime)

    async def open_accelerator_service_async(
        self,
        request: main_models.OpenAcceleratorServiceRequest,
    ) -> main_models.OpenAcceleratorServiceResponse:
        runtime = RuntimeOptions()
        return await self.open_accelerator_service_with_options_async(request, runtime)

    def query_cross_border_approval_status_with_options(
        self,
        request: main_models.QueryCrossBorderApprovalStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCrossBorderApprovalStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCrossBorderApprovalStatus',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCrossBorderApprovalStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cross_border_approval_status_with_options_async(
        self,
        request: main_models.QueryCrossBorderApprovalStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCrossBorderApprovalStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCrossBorderApprovalStatus',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCrossBorderApprovalStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cross_border_approval_status(
        self,
        request: main_models.QueryCrossBorderApprovalStatusRequest,
    ) -> main_models.QueryCrossBorderApprovalStatusResponse:
        runtime = RuntimeOptions()
        return self.query_cross_border_approval_status_with_options(request, runtime)

    async def query_cross_border_approval_status_async(
        self,
        request: main_models.QueryCrossBorderApprovalStatusRequest,
    ) -> main_models.QueryCrossBorderApprovalStatusResponse:
        runtime = RuntimeOptions()
        return await self.query_cross_border_approval_status_with_options_async(request, runtime)

    def remove_entries_from_acl_with_options(
        self,
        request: main_models.RemoveEntriesFromAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveEntriesFromAclResponse:
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveEntriesFromAcl',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.acl_entries):
            query['AclEntries'] = request.acl_entries
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveEntriesFromAcl',
            version = '2019-11-20',
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

    def replace_bandwidth_package_with_options(
        self,
        request: main_models.ReplaceBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.target_bandwidth_package_id):
            query['TargetBandwidthPackageId'] = request.target_bandwidth_package_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceBandwidthPackage',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_bandwidth_package_with_options_async(
        self,
        request: main_models.ReplaceBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.target_bandwidth_package_id):
            query['TargetBandwidthPackageId'] = request.target_bandwidth_package_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceBandwidthPackage',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceBandwidthPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_bandwidth_package(
        self,
        request: main_models.ReplaceBandwidthPackageRequest,
    ) -> main_models.ReplaceBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return self.replace_bandwidth_package_with_options(request, runtime)

    async def replace_bandwidth_package_async(
        self,
        request: main_models.ReplaceBandwidthPackageRequest,
    ) -> main_models.ReplaceBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return await self.replace_bandwidth_package_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
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
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
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
            version = '2019-11-20',
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
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
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
            action = 'UntagResources',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
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
            action = 'UntagResources',
            version = '2019-11-20',
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

    def update_accelerator_with_options(
        self,
        request: main_models.UpdateAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_accelerator_with_options_async(
        self,
        request: main_models.UpdateAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAcceleratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_accelerator(
        self,
        request: main_models.UpdateAcceleratorRequest,
    ) -> main_models.UpdateAcceleratorResponse:
        runtime = RuntimeOptions()
        return self.update_accelerator_with_options(request, runtime)

    async def update_accelerator_async(
        self,
        request: main_models.UpdateAcceleratorRequest,
    ) -> main_models.UpdateAcceleratorResponse:
        runtime = RuntimeOptions()
        return await self.update_accelerator_with_options_async(request, runtime)

    def update_accelerator_auto_renew_attribute_with_options(
        self,
        request: main_models.UpdateAcceleratorAutoRenewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAcceleratorAutoRenewAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAcceleratorAutoRenewAttribute',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAcceleratorAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_accelerator_auto_renew_attribute_with_options_async(
        self,
        request: main_models.UpdateAcceleratorAutoRenewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAcceleratorAutoRenewAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAcceleratorAutoRenewAttribute',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAcceleratorAutoRenewAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_accelerator_auto_renew_attribute(
        self,
        request: main_models.UpdateAcceleratorAutoRenewAttributeRequest,
    ) -> main_models.UpdateAcceleratorAutoRenewAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_accelerator_auto_renew_attribute_with_options(request, runtime)

    async def update_accelerator_auto_renew_attribute_async(
        self,
        request: main_models.UpdateAcceleratorAutoRenewAttributeRequest,
    ) -> main_models.UpdateAcceleratorAutoRenewAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_accelerator_auto_renew_attribute_with_options_async(request, runtime)

    def update_accelerator_confirm_with_options(
        self,
        request: main_models.UpdateAcceleratorConfirmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAcceleratorConfirmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAcceleratorConfirm',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAcceleratorConfirmResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_accelerator_confirm_with_options_async(
        self,
        request: main_models.UpdateAcceleratorConfirmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAcceleratorConfirmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAcceleratorConfirm',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAcceleratorConfirmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_accelerator_confirm(
        self,
        request: main_models.UpdateAcceleratorConfirmRequest,
    ) -> main_models.UpdateAcceleratorConfirmResponse:
        runtime = RuntimeOptions()
        return self.update_accelerator_confirm_with_options(request, runtime)

    async def update_accelerator_confirm_async(
        self,
        request: main_models.UpdateAcceleratorConfirmRequest,
    ) -> main_models.UpdateAcceleratorConfirmResponse:
        runtime = RuntimeOptions()
        return await self.update_accelerator_confirm_with_options_async(request, runtime)

    def update_accelerator_cross_border_mode_with_options(
        self,
        request: main_models.UpdateAcceleratorCrossBorderModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAcceleratorCrossBorderModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_border_mode):
            query['CrossBorderMode'] = request.cross_border_mode
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAcceleratorCrossBorderMode',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAcceleratorCrossBorderModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_accelerator_cross_border_mode_with_options_async(
        self,
        request: main_models.UpdateAcceleratorCrossBorderModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAcceleratorCrossBorderModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_border_mode):
            query['CrossBorderMode'] = request.cross_border_mode
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAcceleratorCrossBorderMode',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAcceleratorCrossBorderModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_accelerator_cross_border_mode(
        self,
        request: main_models.UpdateAcceleratorCrossBorderModeRequest,
    ) -> main_models.UpdateAcceleratorCrossBorderModeResponse:
        runtime = RuntimeOptions()
        return self.update_accelerator_cross_border_mode_with_options(request, runtime)

    async def update_accelerator_cross_border_mode_async(
        self,
        request: main_models.UpdateAcceleratorCrossBorderModeRequest,
    ) -> main_models.UpdateAcceleratorCrossBorderModeResponse:
        runtime = RuntimeOptions()
        return await self.update_accelerator_cross_border_mode_with_options_async(request, runtime)

    def update_accelerator_cross_border_status_with_options(
        self,
        request: main_models.UpdateAcceleratorCrossBorderStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAcceleratorCrossBorderStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_border_status):
            query['CrossBorderStatus'] = request.cross_border_status
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAcceleratorCrossBorderStatus',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAcceleratorCrossBorderStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_accelerator_cross_border_status_with_options_async(
        self,
        request: main_models.UpdateAcceleratorCrossBorderStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAcceleratorCrossBorderStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_border_status):
            query['CrossBorderStatus'] = request.cross_border_status
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAcceleratorCrossBorderStatus',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAcceleratorCrossBorderStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_accelerator_cross_border_status(
        self,
        request: main_models.UpdateAcceleratorCrossBorderStatusRequest,
    ) -> main_models.UpdateAcceleratorCrossBorderStatusResponse:
        runtime = RuntimeOptions()
        return self.update_accelerator_cross_border_status_with_options(request, runtime)

    async def update_accelerator_cross_border_status_async(
        self,
        request: main_models.UpdateAcceleratorCrossBorderStatusRequest,
    ) -> main_models.UpdateAcceleratorCrossBorderStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_accelerator_cross_border_status_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAclAttribute',
            version = '2019-11-20',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAclAttribute',
            version = '2019-11-20',
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

    def update_additional_certificate_with_listener_with_options(
        self,
        request: main_models.UpdateAdditionalCertificateWithListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAdditionalCertificateWithListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
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
            action = 'UpdateAdditionalCertificateWithListener',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAdditionalCertificateWithListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_additional_certificate_with_listener_with_options_async(
        self,
        request: main_models.UpdateAdditionalCertificateWithListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAdditionalCertificateWithListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
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
            action = 'UpdateAdditionalCertificateWithListener',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAdditionalCertificateWithListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_additional_certificate_with_listener(
        self,
        request: main_models.UpdateAdditionalCertificateWithListenerRequest,
    ) -> main_models.UpdateAdditionalCertificateWithListenerResponse:
        runtime = RuntimeOptions()
        return self.update_additional_certificate_with_listener_with_options(request, runtime)

    async def update_additional_certificate_with_listener_async(
        self,
        request: main_models.UpdateAdditionalCertificateWithListenerRequest,
    ) -> main_models.UpdateAdditionalCertificateWithListenerResponse:
        runtime = RuntimeOptions()
        return await self.update_additional_certificate_with_listener_with_options_async(request, runtime)

    def update_application_monitor_with_options(
        self,
        request: main_models.UpdateApplicationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.detect_enable):
            query['DetectEnable'] = request.detect_enable
        if not DaraCore.is_null(request.detect_threshold):
            query['DetectThreshold'] = request.detect_threshold
        if not DaraCore.is_null(request.detect_times):
            query['DetectTimes'] = request.detect_times
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.options_json):
            query['OptionsJson'] = request.options_json
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationMonitor',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_monitor_with_options_async(
        self,
        request: main_models.UpdateApplicationMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.detect_enable):
            query['DetectEnable'] = request.detect_enable
        if not DaraCore.is_null(request.detect_threshold):
            query['DetectThreshold'] = request.detect_threshold
        if not DaraCore.is_null(request.detect_times):
            query['DetectTimes'] = request.detect_times
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.options_json):
            query['OptionsJson'] = request.options_json
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationMonitor',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_monitor(
        self,
        request: main_models.UpdateApplicationMonitorRequest,
    ) -> main_models.UpdateApplicationMonitorResponse:
        runtime = RuntimeOptions()
        return self.update_application_monitor_with_options(request, runtime)

    async def update_application_monitor_async(
        self,
        request: main_models.UpdateApplicationMonitorRequest,
    ) -> main_models.UpdateApplicationMonitorResponse:
        runtime = RuntimeOptions()
        return await self.update_application_monitor_with_options_async(request, runtime)

    def update_bandwidth_packaga_auto_renew_attribute_with_options(
        self,
        request: main_models.UpdateBandwidthPackagaAutoRenewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBandwidthPackagaAutoRenewAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBandwidthPackagaAutoRenewAttribute',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBandwidthPackagaAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_bandwidth_packaga_auto_renew_attribute_with_options_async(
        self,
        request: main_models.UpdateBandwidthPackagaAutoRenewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBandwidthPackagaAutoRenewAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_duration):
            query['AutoRenewDuration'] = request.auto_renew_duration
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBandwidthPackagaAutoRenewAttribute',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBandwidthPackagaAutoRenewAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_bandwidth_packaga_auto_renew_attribute(
        self,
        request: main_models.UpdateBandwidthPackagaAutoRenewAttributeRequest,
    ) -> main_models.UpdateBandwidthPackagaAutoRenewAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_bandwidth_packaga_auto_renew_attribute_with_options(request, runtime)

    async def update_bandwidth_packaga_auto_renew_attribute_async(
        self,
        request: main_models.UpdateBandwidthPackagaAutoRenewAttributeRequest,
    ) -> main_models.UpdateBandwidthPackagaAutoRenewAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_bandwidth_packaga_auto_renew_attribute_with_options_async(request, runtime)

    def update_bandwidth_package_with_options(
        self,
        request: main_models.UpdateBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBandwidthPackage',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBandwidthPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_bandwidth_package_with_options_async(
        self,
        request: main_models.UpdateBandwidthPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBandwidthPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_use_coupon):
            query['AutoUseCoupon'] = request.auto_use_coupon
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.bandwidth_package_id):
            query['BandwidthPackageId'] = request.bandwidth_package_id
        if not DaraCore.is_null(request.bandwidth_type):
            query['BandwidthType'] = request.bandwidth_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBandwidthPackage',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBandwidthPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_bandwidth_package(
        self,
        request: main_models.UpdateBandwidthPackageRequest,
    ) -> main_models.UpdateBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return self.update_bandwidth_package_with_options(request, runtime)

    async def update_bandwidth_package_async(
        self,
        request: main_models.UpdateBandwidthPackageRequest,
    ) -> main_models.UpdateBandwidthPackageResponse:
        runtime = RuntimeOptions()
        return await self.update_bandwidth_package_with_options_async(request, runtime)

    def update_basic_accelerator_with_options(
        self,
        request: main_models.UpdateBasicAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBasicAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBasicAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBasicAcceleratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_basic_accelerator_with_options_async(
        self,
        request: main_models.UpdateBasicAcceleratorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBasicAcceleratorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBasicAccelerator',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBasicAcceleratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_basic_accelerator(
        self,
        request: main_models.UpdateBasicAcceleratorRequest,
    ) -> main_models.UpdateBasicAcceleratorResponse:
        runtime = RuntimeOptions()
        return self.update_basic_accelerator_with_options(request, runtime)

    async def update_basic_accelerator_async(
        self,
        request: main_models.UpdateBasicAcceleratorRequest,
    ) -> main_models.UpdateBasicAcceleratorResponse:
        runtime = RuntimeOptions()
        return await self.update_basic_accelerator_with_options_async(request, runtime)

    def update_basic_endpoint_with_options(
        self,
        request: main_models.UpdateBasicEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBasicEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBasicEndpoint',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBasicEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_basic_endpoint_with_options_async(
        self,
        request: main_models.UpdateBasicEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBasicEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBasicEndpoint',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBasicEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_basic_endpoint(
        self,
        request: main_models.UpdateBasicEndpointRequest,
    ) -> main_models.UpdateBasicEndpointResponse:
        runtime = RuntimeOptions()
        return self.update_basic_endpoint_with_options(request, runtime)

    async def update_basic_endpoint_async(
        self,
        request: main_models.UpdateBasicEndpointRequest,
    ) -> main_models.UpdateBasicEndpointResponse:
        runtime = RuntimeOptions()
        return await self.update_basic_endpoint_with_options_async(request, runtime)

    def update_basic_endpoint_group_with_options(
        self,
        request: main_models.UpdateBasicEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBasicEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.endpoint_address):
            query['EndpointAddress'] = request.endpoint_address
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_sub_address):
            query['EndpointSubAddress'] = request.endpoint_sub_address
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBasicEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBasicEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_basic_endpoint_group_with_options_async(
        self,
        request: main_models.UpdateBasicEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBasicEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.endpoint_address):
            query['EndpointAddress'] = request.endpoint_address
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_sub_address):
            query['EndpointSubAddress'] = request.endpoint_sub_address
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBasicEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBasicEndpointGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_basic_endpoint_group(
        self,
        request: main_models.UpdateBasicEndpointGroupRequest,
    ) -> main_models.UpdateBasicEndpointGroupResponse:
        runtime = RuntimeOptions()
        return self.update_basic_endpoint_group_with_options(request, runtime)

    async def update_basic_endpoint_group_async(
        self,
        request: main_models.UpdateBasicEndpointGroupRequest,
    ) -> main_models.UpdateBasicEndpointGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_basic_endpoint_group_with_options_async(request, runtime)

    def update_basic_ip_set_with_options(
        self,
        request: main_models.UpdateBasicIpSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBasicIpSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBasicIpSet',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBasicIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_basic_ip_set_with_options_async(
        self,
        request: main_models.UpdateBasicIpSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBasicIpSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBasicIpSet',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBasicIpSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_basic_ip_set(
        self,
        request: main_models.UpdateBasicIpSetRequest,
    ) -> main_models.UpdateBasicIpSetResponse:
        runtime = RuntimeOptions()
        return self.update_basic_ip_set_with_options(request, runtime)

    async def update_basic_ip_set_async(
        self,
        request: main_models.UpdateBasicIpSetRequest,
    ) -> main_models.UpdateBasicIpSetResponse:
        runtime = RuntimeOptions()
        return await self.update_basic_ip_set_with_options_async(request, runtime)

    def update_custom_routing_endpoint_group_attribute_with_options(
        self,
        request: main_models.UpdateCustomRoutingEndpointGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomRoutingEndpointGroupAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomRoutingEndpointGroupAttribute',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomRoutingEndpointGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_routing_endpoint_group_attribute_with_options_async(
        self,
        request: main_models.UpdateCustomRoutingEndpointGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomRoutingEndpointGroupAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomRoutingEndpointGroupAttribute',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomRoutingEndpointGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_routing_endpoint_group_attribute(
        self,
        request: main_models.UpdateCustomRoutingEndpointGroupAttributeRequest,
    ) -> main_models.UpdateCustomRoutingEndpointGroupAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_custom_routing_endpoint_group_attribute_with_options(request, runtime)

    async def update_custom_routing_endpoint_group_attribute_async(
        self,
        request: main_models.UpdateCustomRoutingEndpointGroupAttributeRequest,
    ) -> main_models.UpdateCustomRoutingEndpointGroupAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_custom_routing_endpoint_group_attribute_with_options_async(request, runtime)

    def update_custom_routing_endpoint_group_destinations_with_options(
        self,
        request: main_models.UpdateCustomRoutingEndpointGroupDestinationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomRoutingEndpointGroupDestinationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.destination_configurations):
            query['DestinationConfigurations'] = request.destination_configurations
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomRoutingEndpointGroupDestinations',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomRoutingEndpointGroupDestinationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_routing_endpoint_group_destinations_with_options_async(
        self,
        request: main_models.UpdateCustomRoutingEndpointGroupDestinationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomRoutingEndpointGroupDestinationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.destination_configurations):
            query['DestinationConfigurations'] = request.destination_configurations
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomRoutingEndpointGroupDestinations',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomRoutingEndpointGroupDestinationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_routing_endpoint_group_destinations(
        self,
        request: main_models.UpdateCustomRoutingEndpointGroupDestinationsRequest,
    ) -> main_models.UpdateCustomRoutingEndpointGroupDestinationsResponse:
        runtime = RuntimeOptions()
        return self.update_custom_routing_endpoint_group_destinations_with_options(request, runtime)

    async def update_custom_routing_endpoint_group_destinations_async(
        self,
        request: main_models.UpdateCustomRoutingEndpointGroupDestinationsRequest,
    ) -> main_models.UpdateCustomRoutingEndpointGroupDestinationsResponse:
        runtime = RuntimeOptions()
        return await self.update_custom_routing_endpoint_group_destinations_with_options_async(request, runtime)

    def update_custom_routing_endpoint_traffic_policies_with_options(
        self,
        request: main_models.UpdateCustomRoutingEndpointTrafficPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomRoutingEndpointTrafficPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.policy_configurations):
            query['PolicyConfigurations'] = request.policy_configurations
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomRoutingEndpointTrafficPolicies',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomRoutingEndpointTrafficPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_routing_endpoint_traffic_policies_with_options_async(
        self,
        request: main_models.UpdateCustomRoutingEndpointTrafficPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomRoutingEndpointTrafficPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_id):
            query['EndpointId'] = request.endpoint_id
        if not DaraCore.is_null(request.policy_configurations):
            query['PolicyConfigurations'] = request.policy_configurations
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomRoutingEndpointTrafficPolicies',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomRoutingEndpointTrafficPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_routing_endpoint_traffic_policies(
        self,
        request: main_models.UpdateCustomRoutingEndpointTrafficPoliciesRequest,
    ) -> main_models.UpdateCustomRoutingEndpointTrafficPoliciesResponse:
        runtime = RuntimeOptions()
        return self.update_custom_routing_endpoint_traffic_policies_with_options(request, runtime)

    async def update_custom_routing_endpoint_traffic_policies_async(
        self,
        request: main_models.UpdateCustomRoutingEndpointTrafficPoliciesRequest,
    ) -> main_models.UpdateCustomRoutingEndpointTrafficPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.update_custom_routing_endpoint_traffic_policies_with_options_async(request, runtime)

    def update_custom_routing_endpoints_with_options(
        self,
        request: main_models.UpdateCustomRoutingEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomRoutingEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_configurations):
            query['EndpointConfigurations'] = request.endpoint_configurations
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomRoutingEndpoints',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomRoutingEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_routing_endpoints_with_options_async(
        self,
        request: main_models.UpdateCustomRoutingEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomRoutingEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_configurations):
            query['EndpointConfigurations'] = request.endpoint_configurations
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomRoutingEndpoints',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomRoutingEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_routing_endpoints(
        self,
        request: main_models.UpdateCustomRoutingEndpointsRequest,
    ) -> main_models.UpdateCustomRoutingEndpointsResponse:
        runtime = RuntimeOptions()
        return self.update_custom_routing_endpoints_with_options(request, runtime)

    async def update_custom_routing_endpoints_async(
        self,
        request: main_models.UpdateCustomRoutingEndpointsRequest,
    ) -> main_models.UpdateCustomRoutingEndpointsResponse:
        runtime = RuntimeOptions()
        return await self.update_custom_routing_endpoints_with_options_async(request, runtime)

    def update_domain_with_options(
        self,
        request: main_models.UpdateDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.target_domain):
            query['TargetDomain'] = request.target_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomain',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_with_options_async(
        self,
        request: main_models.UpdateDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.target_domain):
            query['TargetDomain'] = request.target_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomain',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain(
        self,
        request: main_models.UpdateDomainRequest,
    ) -> main_models.UpdateDomainResponse:
        runtime = RuntimeOptions()
        return self.update_domain_with_options(request, runtime)

    async def update_domain_async(
        self,
        request: main_models.UpdateDomainRequest,
    ) -> main_models.UpdateDomainResponse:
        runtime = RuntimeOptions()
        return await self.update_domain_with_options_async(request, runtime)

    def update_domain_state_with_options(
        self,
        request: main_models.UpdateDomainStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomainState',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_state_with_options_async(
        self,
        request: main_models.UpdateDomainStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomainState',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain_state(
        self,
        request: main_models.UpdateDomainStateRequest,
    ) -> main_models.UpdateDomainStateResponse:
        runtime = RuntimeOptions()
        return self.update_domain_state_with_options(request, runtime)

    async def update_domain_state_async(
        self,
        request: main_models.UpdateDomainStateRequest,
    ) -> main_models.UpdateDomainStateResponse:
        runtime = RuntimeOptions()
        return await self.update_domain_state_with_options_async(request, runtime)

    def update_endpoint_group_with_options(
        self,
        request: main_models.UpdateEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.endpoint_configurations):
            query['EndpointConfigurations'] = request.endpoint_configurations
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_group_region):
            query['EndpointGroupRegion'] = request.endpoint_group_region
        if not DaraCore.is_null(request.endpoint_ip_version):
            query['EndpointIpVersion'] = request.endpoint_ip_version
        if not DaraCore.is_null(request.endpoint_protocol_version):
            query['EndpointProtocolVersion'] = request.endpoint_protocol_version
        if not DaraCore.is_null(request.endpoint_request_protocol):
            query['EndpointRequestProtocol'] = request.endpoint_request_protocol
        if not DaraCore.is_null(request.health_check_enabled):
            query['HealthCheckEnabled'] = request.health_check_enabled
        if not DaraCore.is_null(request.health_check_host):
            query['HealthCheckHost'] = request.health_check_host
        if not DaraCore.is_null(request.health_check_interval_seconds):
            query['HealthCheckIntervalSeconds'] = request.health_check_interval_seconds
        if not DaraCore.is_null(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not DaraCore.is_null(request.health_check_port):
            query['HealthCheckPort'] = request.health_check_port
        if not DaraCore.is_null(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.port_overrides):
            query['PortOverrides'] = request.port_overrides
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.threshold_count):
            query['ThresholdCount'] = request.threshold_count
        if not DaraCore.is_null(request.traffic_percentage):
            query['TrafficPercentage'] = request.traffic_percentage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEndpointGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_endpoint_group_with_options_async(
        self,
        request: main_models.UpdateEndpointGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEndpointGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.endpoint_configurations):
            query['EndpointConfigurations'] = request.endpoint_configurations
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.endpoint_group_region):
            query['EndpointGroupRegion'] = request.endpoint_group_region
        if not DaraCore.is_null(request.endpoint_ip_version):
            query['EndpointIpVersion'] = request.endpoint_ip_version
        if not DaraCore.is_null(request.endpoint_protocol_version):
            query['EndpointProtocolVersion'] = request.endpoint_protocol_version
        if not DaraCore.is_null(request.endpoint_request_protocol):
            query['EndpointRequestProtocol'] = request.endpoint_request_protocol
        if not DaraCore.is_null(request.health_check_enabled):
            query['HealthCheckEnabled'] = request.health_check_enabled
        if not DaraCore.is_null(request.health_check_host):
            query['HealthCheckHost'] = request.health_check_host
        if not DaraCore.is_null(request.health_check_interval_seconds):
            query['HealthCheckIntervalSeconds'] = request.health_check_interval_seconds
        if not DaraCore.is_null(request.health_check_path):
            query['HealthCheckPath'] = request.health_check_path
        if not DaraCore.is_null(request.health_check_port):
            query['HealthCheckPort'] = request.health_check_port
        if not DaraCore.is_null(request.health_check_protocol):
            query['HealthCheckProtocol'] = request.health_check_protocol
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.port_overrides):
            query['PortOverrides'] = request.port_overrides
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.threshold_count):
            query['ThresholdCount'] = request.threshold_count
        if not DaraCore.is_null(request.traffic_percentage):
            query['TrafficPercentage'] = request.traffic_percentage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEndpointGroup',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEndpointGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_endpoint_group(
        self,
        request: main_models.UpdateEndpointGroupRequest,
    ) -> main_models.UpdateEndpointGroupResponse:
        runtime = RuntimeOptions()
        return self.update_endpoint_group_with_options(request, runtime)

    async def update_endpoint_group_async(
        self,
        request: main_models.UpdateEndpointGroupRequest,
    ) -> main_models.UpdateEndpointGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_endpoint_group_with_options_async(request, runtime)

    def update_endpoint_group_attribute_with_options(
        self,
        request: main_models.UpdateEndpointGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEndpointGroupAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEndpointGroupAttribute',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEndpointGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_endpoint_group_attribute_with_options_async(
        self,
        request: main_models.UpdateEndpointGroupAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEndpointGroupAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEndpointGroupAttribute',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEndpointGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_endpoint_group_attribute(
        self,
        request: main_models.UpdateEndpointGroupAttributeRequest,
    ) -> main_models.UpdateEndpointGroupAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_endpoint_group_attribute_with_options(request, runtime)

    async def update_endpoint_group_attribute_async(
        self,
        request: main_models.UpdateEndpointGroupAttributeRequest,
    ) -> main_models.UpdateEndpointGroupAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_endpoint_group_attribute_with_options_async(request, runtime)

    def update_endpoint_groups_with_options(
        self,
        request: main_models.UpdateEndpointGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEndpointGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_group_configurations):
            query['EndpointGroupConfigurations'] = request.endpoint_group_configurations
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEndpointGroups',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEndpointGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_endpoint_groups_with_options_async(
        self,
        request: main_models.UpdateEndpointGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEndpointGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.endpoint_group_configurations):
            query['EndpointGroupConfigurations'] = request.endpoint_group_configurations
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEndpointGroups',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEndpointGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_endpoint_groups(
        self,
        request: main_models.UpdateEndpointGroupsRequest,
    ) -> main_models.UpdateEndpointGroupsResponse:
        runtime = RuntimeOptions()
        return self.update_endpoint_groups_with_options(request, runtime)

    async def update_endpoint_groups_async(
        self,
        request: main_models.UpdateEndpointGroupsRequest,
    ) -> main_models.UpdateEndpointGroupsResponse:
        runtime = RuntimeOptions()
        return await self.update_endpoint_groups_with_options_async(request, runtime)

    def update_forwarding_rules_with_options(
        self,
        request: main_models.UpdateForwardingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateForwardingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.forwarding_rules):
            query['ForwardingRules'] = request.forwarding_rules
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateForwardingRules',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateForwardingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_forwarding_rules_with_options_async(
        self,
        request: main_models.UpdateForwardingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateForwardingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.forwarding_rules):
            query['ForwardingRules'] = request.forwarding_rules
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateForwardingRules',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateForwardingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_forwarding_rules(
        self,
        request: main_models.UpdateForwardingRulesRequest,
    ) -> main_models.UpdateForwardingRulesResponse:
        runtime = RuntimeOptions()
        return self.update_forwarding_rules_with_options(request, runtime)

    async def update_forwarding_rules_async(
        self,
        request: main_models.UpdateForwardingRulesRequest,
    ) -> main_models.UpdateForwardingRulesResponse:
        runtime = RuntimeOptions()
        return await self.update_forwarding_rules_with_options_async(request, runtime)

    def update_ip_set_with_options(
        self,
        request: main_models.UpdateIpSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIpSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIpSet',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIpSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ip_set_with_options_async(
        self,
        request: main_models.UpdateIpSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIpSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ip_set_id):
            query['IpSetId'] = request.ip_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIpSet',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIpSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ip_set(
        self,
        request: main_models.UpdateIpSetRequest,
    ) -> main_models.UpdateIpSetResponse:
        runtime = RuntimeOptions()
        return self.update_ip_set_with_options(request, runtime)

    async def update_ip_set_async(
        self,
        request: main_models.UpdateIpSetRequest,
    ) -> main_models.UpdateIpSetResponse:
        runtime = RuntimeOptions()
        return await self.update_ip_set_with_options_async(request, runtime)

    def update_ip_sets_with_options(
        self,
        request: main_models.UpdateIpSetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIpSetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_sets):
            query['IpSets'] = request.ip_sets
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIpSets',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIpSetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ip_sets_with_options_async(
        self,
        request: main_models.UpdateIpSetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIpSetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_sets):
            query['IpSets'] = request.ip_sets
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIpSets',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIpSetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ip_sets(
        self,
        request: main_models.UpdateIpSetsRequest,
    ) -> main_models.UpdateIpSetsResponse:
        runtime = RuntimeOptions()
        return self.update_ip_sets_with_options(request, runtime)

    async def update_ip_sets_async(
        self,
        request: main_models.UpdateIpSetsRequest,
    ) -> main_models.UpdateIpSetsResponse:
        runtime = RuntimeOptions()
        return await self.update_ip_sets_with_options_async(request, runtime)

    def update_listener_with_options(
        self,
        request: main_models.UpdateListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_ports):
            query['BackendPorts'] = request.backend_ports
        if not DaraCore.is_null(request.certificates):
            query['Certificates'] = request.certificates
        if not DaraCore.is_null(request.client_affinity):
            query['ClientAffinity'] = request.client_affinity
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.http_version):
            query['HttpVersion'] = request.http_version
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.port_ranges):
            query['PortRanges'] = request.port_ranges
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.proxy_protocol):
            query['ProxyProtocol'] = request.proxy_protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
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
            action = 'UpdateListener',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateListenerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_listener_with_options_async(
        self,
        request: main_models.UpdateListenerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateListenerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_ports):
            query['BackendPorts'] = request.backend_ports
        if not DaraCore.is_null(request.certificates):
            query['Certificates'] = request.certificates
        if not DaraCore.is_null(request.client_affinity):
            query['ClientAffinity'] = request.client_affinity
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.http_version):
            query['HttpVersion'] = request.http_version
        if not DaraCore.is_null(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.port_ranges):
            query['PortRanges'] = request.port_ranges
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        if not DaraCore.is_null(request.proxy_protocol):
            query['ProxyProtocol'] = request.proxy_protocol
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
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
            action = 'UpdateListener',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateListenerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_listener(
        self,
        request: main_models.UpdateListenerRequest,
    ) -> main_models.UpdateListenerResponse:
        runtime = RuntimeOptions()
        return self.update_listener_with_options(request, runtime)

    async def update_listener_async(
        self,
        request: main_models.UpdateListenerRequest,
    ) -> main_models.UpdateListenerResponse:
        runtime = RuntimeOptions()
        return await self.update_listener_with_options_async(request, runtime)

    def update_log_store_config_with_options(
        self,
        request: main_models.UpdateLogStoreConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogStoreConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.access_log_record_customized_header_list):
            query['AccessLogRecordCustomizedHeaderList'] = request.access_log_record_customized_header_list
        if not DaraCore.is_null(request.access_log_record_customized_headers_enabled):
            query['AccessLogRecordCustomizedHeadersEnabled'] = request.access_log_record_customized_headers_enabled
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sls_log_store_name):
            query['SlsLogStoreName'] = request.sls_log_store_name
        if not DaraCore.is_null(request.sls_project_name):
            query['SlsProjectName'] = request.sls_project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogStoreConfig',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLogStoreConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_log_store_config_with_options_async(
        self,
        request: main_models.UpdateLogStoreConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLogStoreConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerator_id):
            query['AcceleratorId'] = request.accelerator_id
        if not DaraCore.is_null(request.access_log_record_customized_header_list):
            query['AccessLogRecordCustomizedHeaderList'] = request.access_log_record_customized_header_list
        if not DaraCore.is_null(request.access_log_record_customized_headers_enabled):
            query['AccessLogRecordCustomizedHeadersEnabled'] = request.access_log_record_customized_headers_enabled
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.endpoint_group_id):
            query['EndpointGroupId'] = request.endpoint_group_id
        if not DaraCore.is_null(request.listener_id):
            query['ListenerId'] = request.listener_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sls_log_store_name):
            query['SlsLogStoreName'] = request.sls_log_store_name
        if not DaraCore.is_null(request.sls_project_name):
            query['SlsProjectName'] = request.sls_project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLogStoreConfig',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLogStoreConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_log_store_config(
        self,
        request: main_models.UpdateLogStoreConfigRequest,
    ) -> main_models.UpdateLogStoreConfigResponse:
        runtime = RuntimeOptions()
        return self.update_log_store_config_with_options(request, runtime)

    async def update_log_store_config_async(
        self,
        request: main_models.UpdateLogStoreConfigRequest,
    ) -> main_models.UpdateLogStoreConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_log_store_config_with_options_async(request, runtime)

    def update_service_managed_control_with_options(
        self,
        request: main_models.UpdateServiceManagedControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceManagedControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_managed):
            query['ServiceManaged'] = request.service_managed
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceManagedControl',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceManagedControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_managed_control_with_options_async(
        self,
        request: main_models.UpdateServiceManagedControlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceManagedControlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_managed):
            query['ServiceManaged'] = request.service_managed
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceManagedControl',
            version = '2019-11-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceManagedControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_managed_control(
        self,
        request: main_models.UpdateServiceManagedControlRequest,
    ) -> main_models.UpdateServiceManagedControlResponse:
        runtime = RuntimeOptions()
        return self.update_service_managed_control_with_options(request, runtime)

    async def update_service_managed_control_async(
        self,
        request: main_models.UpdateServiceManagedControlRequest,
    ) -> main_models.UpdateServiceManagedControlResponse:
        runtime = RuntimeOptions()
        return await self.update_service_managed_control_with_options_async(request, runtime)
