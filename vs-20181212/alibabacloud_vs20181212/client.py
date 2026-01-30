# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_vs20181212 import models as main_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('vs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_vs_pull_stream_info_config_with_options(
        self,
        request: main_models.AddVsPullStreamInfoConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddVsPullStreamInfoConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.always):
            query['Always'] = request.always
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.source_url):
            query['SourceUrl'] = request.source_url
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddVsPullStreamInfoConfig',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddVsPullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_vs_pull_stream_info_config_with_options_async(
        self,
        request: main_models.AddVsPullStreamInfoConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddVsPullStreamInfoConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.always):
            query['Always'] = request.always
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.source_url):
            query['SourceUrl'] = request.source_url
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddVsPullStreamInfoConfig',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddVsPullStreamInfoConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_vs_pull_stream_info_config(
        self,
        request: main_models.AddVsPullStreamInfoConfigRequest,
    ) -> main_models.AddVsPullStreamInfoConfigResponse:
        runtime = RuntimeOptions()
        return self.add_vs_pull_stream_info_config_with_options(request, runtime)

    async def add_vs_pull_stream_info_config_async(
        self,
        request: main_models.AddVsPullStreamInfoConfigRequest,
    ) -> main_models.AddVsPullStreamInfoConfigResponse:
        runtime = RuntimeOptions()
        return await self.add_vs_pull_stream_info_config_with_options_async(request, runtime)

    def associate_rendering_project_instances_with_options(
        self,
        tmp_req: main_models.AssociateRenderingProjectInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateRenderingProjectInstancesResponse:
        tmp_req.validate()
        request = main_models.AssociateRenderingProjectInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateRenderingProjectInstances',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateRenderingProjectInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_rendering_project_instances_with_options_async(
        self,
        tmp_req: main_models.AssociateRenderingProjectInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateRenderingProjectInstancesResponse:
        tmp_req.validate()
        request = main_models.AssociateRenderingProjectInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateRenderingProjectInstances',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateRenderingProjectInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_rendering_project_instances(
        self,
        request: main_models.AssociateRenderingProjectInstancesRequest,
    ) -> main_models.AssociateRenderingProjectInstancesResponse:
        runtime = RuntimeOptions()
        return self.associate_rendering_project_instances_with_options(request, runtime)

    async def associate_rendering_project_instances_async(
        self,
        request: main_models.AssociateRenderingProjectInstancesRequest,
    ) -> main_models.AssociateRenderingProjectInstancesResponse:
        runtime = RuntimeOptions()
        return await self.associate_rendering_project_instances_with_options_async(request, runtime)

    def batch_bind_directories_with_options(
        self,
        request: main_models.BatchBindDirectoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchBindDirectoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchBindDirectories',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchBindDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_bind_directories_with_options_async(
        self,
        request: main_models.BatchBindDirectoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchBindDirectoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchBindDirectories',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchBindDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_bind_directories(
        self,
        request: main_models.BatchBindDirectoriesRequest,
    ) -> main_models.BatchBindDirectoriesResponse:
        runtime = RuntimeOptions()
        return self.batch_bind_directories_with_options(request, runtime)

    async def batch_bind_directories_async(
        self,
        request: main_models.BatchBindDirectoriesRequest,
    ) -> main_models.BatchBindDirectoriesResponse:
        runtime = RuntimeOptions()
        return await self.batch_bind_directories_with_options_async(request, runtime)

    def batch_bind_parent_platform_devices_with_options(
        self,
        request: main_models.BatchBindParentPlatformDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchBindParentPlatformDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchBindParentPlatformDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchBindParentPlatformDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_bind_parent_platform_devices_with_options_async(
        self,
        request: main_models.BatchBindParentPlatformDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchBindParentPlatformDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchBindParentPlatformDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchBindParentPlatformDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_bind_parent_platform_devices(
        self,
        request: main_models.BatchBindParentPlatformDevicesRequest,
    ) -> main_models.BatchBindParentPlatformDevicesResponse:
        runtime = RuntimeOptions()
        return self.batch_bind_parent_platform_devices_with_options(request, runtime)

    async def batch_bind_parent_platform_devices_async(
        self,
        request: main_models.BatchBindParentPlatformDevicesRequest,
    ) -> main_models.BatchBindParentPlatformDevicesResponse:
        runtime = RuntimeOptions()
        return await self.batch_bind_parent_platform_devices_with_options_async(request, runtime)

    def batch_bind_purchased_devices_with_options(
        self,
        request: main_models.BatchBindPurchasedDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchBindPurchasedDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchBindPurchasedDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchBindPurchasedDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_bind_purchased_devices_with_options_async(
        self,
        request: main_models.BatchBindPurchasedDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchBindPurchasedDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchBindPurchasedDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchBindPurchasedDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_bind_purchased_devices(
        self,
        request: main_models.BatchBindPurchasedDevicesRequest,
    ) -> main_models.BatchBindPurchasedDevicesResponse:
        runtime = RuntimeOptions()
        return self.batch_bind_purchased_devices_with_options(request, runtime)

    async def batch_bind_purchased_devices_async(
        self,
        request: main_models.BatchBindPurchasedDevicesRequest,
    ) -> main_models.BatchBindPurchasedDevicesResponse:
        runtime = RuntimeOptions()
        return await self.batch_bind_purchased_devices_with_options_async(request, runtime)

    def batch_bind_template_with_options(
        self,
        request: main_models.BatchBindTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchBindTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apply_all):
            query['ApplyAll'] = request.apply_all
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.replace):
            query['Replace'] = request.replace
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchBindTemplate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchBindTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_bind_template_with_options_async(
        self,
        request: main_models.BatchBindTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchBindTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apply_all):
            query['ApplyAll'] = request.apply_all
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.replace):
            query['Replace'] = request.replace
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchBindTemplate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchBindTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_bind_template(
        self,
        request: main_models.BatchBindTemplateRequest,
    ) -> main_models.BatchBindTemplateResponse:
        runtime = RuntimeOptions()
        return self.batch_bind_template_with_options(request, runtime)

    async def batch_bind_template_async(
        self,
        request: main_models.BatchBindTemplateRequest,
    ) -> main_models.BatchBindTemplateResponse:
        runtime = RuntimeOptions()
        return await self.batch_bind_template_with_options_async(request, runtime)

    def batch_bind_templates_with_options(
        self,
        request: main_models.BatchBindTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchBindTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apply_all):
            query['ApplyAll'] = request.apply_all
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.replace):
            query['Replace'] = request.replace
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchBindTemplates',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchBindTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_bind_templates_with_options_async(
        self,
        request: main_models.BatchBindTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchBindTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apply_all):
            query['ApplyAll'] = request.apply_all
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.replace):
            query['Replace'] = request.replace
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchBindTemplates',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchBindTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_bind_templates(
        self,
        request: main_models.BatchBindTemplatesRequest,
    ) -> main_models.BatchBindTemplatesResponse:
        runtime = RuntimeOptions()
        return self.batch_bind_templates_with_options(request, runtime)

    async def batch_bind_templates_async(
        self,
        request: main_models.BatchBindTemplatesRequest,
    ) -> main_models.BatchBindTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.batch_bind_templates_with_options_async(request, runtime)

    def batch_delete_devices_with_options(
        self,
        request: main_models.BatchDeleteDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_devices_with_options_async(
        self,
        request: main_models.BatchDeleteDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_devices(
        self,
        request: main_models.BatchDeleteDevicesRequest,
    ) -> main_models.BatchDeleteDevicesResponse:
        runtime = RuntimeOptions()
        return self.batch_delete_devices_with_options(request, runtime)

    async def batch_delete_devices_async(
        self,
        request: main_models.BatchDeleteDevicesRequest,
    ) -> main_models.BatchDeleteDevicesResponse:
        runtime = RuntimeOptions()
        return await self.batch_delete_devices_with_options_async(request, runtime)

    def batch_delete_vs_domain_configs_with_options(
        self,
        request: main_models.BatchDeleteVsDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteVsDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.function_names):
            query['FunctionNames'] = request.function_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteVsDomainConfigs',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteVsDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_vs_domain_configs_with_options_async(
        self,
        request: main_models.BatchDeleteVsDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteVsDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.function_names):
            query['FunctionNames'] = request.function_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteVsDomainConfigs',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteVsDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_vs_domain_configs(
        self,
        request: main_models.BatchDeleteVsDomainConfigsRequest,
    ) -> main_models.BatchDeleteVsDomainConfigsResponse:
        runtime = RuntimeOptions()
        return self.batch_delete_vs_domain_configs_with_options(request, runtime)

    async def batch_delete_vs_domain_configs_async(
        self,
        request: main_models.BatchDeleteVsDomainConfigsRequest,
    ) -> main_models.BatchDeleteVsDomainConfigsResponse:
        runtime = RuntimeOptions()
        return await self.batch_delete_vs_domain_configs_with_options_async(request, runtime)

    def batch_forbid_vs_stream_with_options(
        self,
        request: main_models.BatchForbidVsStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchForbidVsStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not DaraCore.is_null(request.oneshot):
            query['Oneshot'] = request.oneshot
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resume_time):
            query['ResumeTime'] = request.resume_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchForbidVsStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchForbidVsStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_forbid_vs_stream_with_options_async(
        self,
        request: main_models.BatchForbidVsStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchForbidVsStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not DaraCore.is_null(request.oneshot):
            query['Oneshot'] = request.oneshot
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resume_time):
            query['ResumeTime'] = request.resume_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchForbidVsStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchForbidVsStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_forbid_vs_stream(
        self,
        request: main_models.BatchForbidVsStreamRequest,
    ) -> main_models.BatchForbidVsStreamResponse:
        runtime = RuntimeOptions()
        return self.batch_forbid_vs_stream_with_options(request, runtime)

    async def batch_forbid_vs_stream_async(
        self,
        request: main_models.BatchForbidVsStreamRequest,
    ) -> main_models.BatchForbidVsStreamResponse:
        runtime = RuntimeOptions()
        return await self.batch_forbid_vs_stream_with_options_async(request, runtime)

    def batch_resume_vs_stream_with_options(
        self,
        request: main_models.BatchResumeVsStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchResumeVsStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchResumeVsStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchResumeVsStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_resume_vs_stream_with_options_async(
        self,
        request: main_models.BatchResumeVsStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchResumeVsStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchResumeVsStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchResumeVsStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_resume_vs_stream(
        self,
        request: main_models.BatchResumeVsStreamRequest,
    ) -> main_models.BatchResumeVsStreamResponse:
        runtime = RuntimeOptions()
        return self.batch_resume_vs_stream_with_options(request, runtime)

    async def batch_resume_vs_stream_async(
        self,
        request: main_models.BatchResumeVsStreamRequest,
    ) -> main_models.BatchResumeVsStreamResponse:
        runtime = RuntimeOptions()
        return await self.batch_resume_vs_stream_with_options_async(request, runtime)

    def batch_set_vs_domain_configs_with_options(
        self,
        request: main_models.BatchSetVsDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSetVsDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.functions):
            query['Functions'] = request.functions
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchSetVsDomainConfigs',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSetVsDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_vs_domain_configs_with_options_async(
        self,
        request: main_models.BatchSetVsDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSetVsDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not DaraCore.is_null(request.functions):
            query['Functions'] = request.functions
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchSetVsDomainConfigs',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSetVsDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_vs_domain_configs(
        self,
        request: main_models.BatchSetVsDomainConfigsRequest,
    ) -> main_models.BatchSetVsDomainConfigsResponse:
        runtime = RuntimeOptions()
        return self.batch_set_vs_domain_configs_with_options(request, runtime)

    async def batch_set_vs_domain_configs_async(
        self,
        request: main_models.BatchSetVsDomainConfigsRequest,
    ) -> main_models.BatchSetVsDomainConfigsResponse:
        runtime = RuntimeOptions()
        return await self.batch_set_vs_domain_configs_with_options_async(request, runtime)

    def batch_start_devices_with_options(
        self,
        request: main_models.BatchStartDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStartDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStartDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStartDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_start_devices_with_options_async(
        self,
        request: main_models.BatchStartDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStartDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStartDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStartDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_start_devices(
        self,
        request: main_models.BatchStartDevicesRequest,
    ) -> main_models.BatchStartDevicesResponse:
        runtime = RuntimeOptions()
        return self.batch_start_devices_with_options(request, runtime)

    async def batch_start_devices_async(
        self,
        request: main_models.BatchStartDevicesRequest,
    ) -> main_models.BatchStartDevicesResponse:
        runtime = RuntimeOptions()
        return await self.batch_start_devices_with_options_async(request, runtime)

    def batch_start_streams_with_options(
        self,
        request: main_models.BatchStartStreamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStartStreamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStartStreams',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStartStreamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_start_streams_with_options_async(
        self,
        request: main_models.BatchStartStreamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStartStreamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStartStreams',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStartStreamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_start_streams(
        self,
        request: main_models.BatchStartStreamsRequest,
    ) -> main_models.BatchStartStreamsResponse:
        runtime = RuntimeOptions()
        return self.batch_start_streams_with_options(request, runtime)

    async def batch_start_streams_async(
        self,
        request: main_models.BatchStartStreamsRequest,
    ) -> main_models.BatchStartStreamsResponse:
        runtime = RuntimeOptions()
        return await self.batch_start_streams_with_options_async(request, runtime)

    def batch_stop_devices_with_options(
        self,
        request: main_models.BatchStopDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStopDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStopDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStopDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_stop_devices_with_options_async(
        self,
        request: main_models.BatchStopDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStopDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStopDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStopDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_stop_devices(
        self,
        request: main_models.BatchStopDevicesRequest,
    ) -> main_models.BatchStopDevicesResponse:
        runtime = RuntimeOptions()
        return self.batch_stop_devices_with_options(request, runtime)

    async def batch_stop_devices_async(
        self,
        request: main_models.BatchStopDevicesRequest,
    ) -> main_models.BatchStopDevicesResponse:
        runtime = RuntimeOptions()
        return await self.batch_stop_devices_with_options_async(request, runtime)

    def batch_stop_streams_with_options(
        self,
        request: main_models.BatchStopStreamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStopStreamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStopStreams',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStopStreamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_stop_streams_with_options_async(
        self,
        request: main_models.BatchStopStreamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchStopStreamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchStopStreams',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchStopStreamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_stop_streams(
        self,
        request: main_models.BatchStopStreamsRequest,
    ) -> main_models.BatchStopStreamsResponse:
        runtime = RuntimeOptions()
        return self.batch_stop_streams_with_options(request, runtime)

    async def batch_stop_streams_async(
        self,
        request: main_models.BatchStopStreamsRequest,
    ) -> main_models.BatchStopStreamsResponse:
        runtime = RuntimeOptions()
        return await self.batch_stop_streams_with_options_async(request, runtime)

    def batch_unbind_directories_with_options(
        self,
        request: main_models.BatchUnbindDirectoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUnbindDirectoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchUnbindDirectories',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUnbindDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_unbind_directories_with_options_async(
        self,
        request: main_models.BatchUnbindDirectoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUnbindDirectoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchUnbindDirectories',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUnbindDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_unbind_directories(
        self,
        request: main_models.BatchUnbindDirectoriesRequest,
    ) -> main_models.BatchUnbindDirectoriesResponse:
        runtime = RuntimeOptions()
        return self.batch_unbind_directories_with_options(request, runtime)

    async def batch_unbind_directories_async(
        self,
        request: main_models.BatchUnbindDirectoriesRequest,
    ) -> main_models.BatchUnbindDirectoriesResponse:
        runtime = RuntimeOptions()
        return await self.batch_unbind_directories_with_options_async(request, runtime)

    def batch_unbind_parent_platform_devices_with_options(
        self,
        request: main_models.BatchUnbindParentPlatformDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUnbindParentPlatformDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchUnbindParentPlatformDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUnbindParentPlatformDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_unbind_parent_platform_devices_with_options_async(
        self,
        request: main_models.BatchUnbindParentPlatformDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUnbindParentPlatformDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchUnbindParentPlatformDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUnbindParentPlatformDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_unbind_parent_platform_devices(
        self,
        request: main_models.BatchUnbindParentPlatformDevicesRequest,
    ) -> main_models.BatchUnbindParentPlatformDevicesResponse:
        runtime = RuntimeOptions()
        return self.batch_unbind_parent_platform_devices_with_options(request, runtime)

    async def batch_unbind_parent_platform_devices_async(
        self,
        request: main_models.BatchUnbindParentPlatformDevicesRequest,
    ) -> main_models.BatchUnbindParentPlatformDevicesResponse:
        runtime = RuntimeOptions()
        return await self.batch_unbind_parent_platform_devices_with_options_async(request, runtime)

    def batch_unbind_purchased_devices_with_options(
        self,
        request: main_models.BatchUnbindPurchasedDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUnbindPurchasedDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchUnbindPurchasedDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUnbindPurchasedDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_unbind_purchased_devices_with_options_async(
        self,
        request: main_models.BatchUnbindPurchasedDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUnbindPurchasedDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchUnbindPurchasedDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUnbindPurchasedDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_unbind_purchased_devices(
        self,
        request: main_models.BatchUnbindPurchasedDevicesRequest,
    ) -> main_models.BatchUnbindPurchasedDevicesResponse:
        runtime = RuntimeOptions()
        return self.batch_unbind_purchased_devices_with_options(request, runtime)

    async def batch_unbind_purchased_devices_async(
        self,
        request: main_models.BatchUnbindPurchasedDevicesRequest,
    ) -> main_models.BatchUnbindPurchasedDevicesResponse:
        runtime = RuntimeOptions()
        return await self.batch_unbind_purchased_devices_with_options_async(request, runtime)

    def batch_unbind_template_with_options(
        self,
        request: main_models.BatchUnbindTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUnbindTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchUnbindTemplate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUnbindTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_unbind_template_with_options_async(
        self,
        request: main_models.BatchUnbindTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUnbindTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchUnbindTemplate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUnbindTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_unbind_template(
        self,
        request: main_models.BatchUnbindTemplateRequest,
    ) -> main_models.BatchUnbindTemplateResponse:
        runtime = RuntimeOptions()
        return self.batch_unbind_template_with_options(request, runtime)

    async def batch_unbind_template_async(
        self,
        request: main_models.BatchUnbindTemplateRequest,
    ) -> main_models.BatchUnbindTemplateResponse:
        runtime = RuntimeOptions()
        return await self.batch_unbind_template_with_options_async(request, runtime)

    def batch_unbind_templates_with_options(
        self,
        request: main_models.BatchUnbindTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUnbindTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchUnbindTemplates',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUnbindTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_unbind_templates_with_options_async(
        self,
        request: main_models.BatchUnbindTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUnbindTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchUnbindTemplates',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUnbindTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_unbind_templates(
        self,
        request: main_models.BatchUnbindTemplatesRequest,
    ) -> main_models.BatchUnbindTemplatesResponse:
        runtime = RuntimeOptions()
        return self.batch_unbind_templates_with_options(request, runtime)

    async def batch_unbind_templates_async(
        self,
        request: main_models.BatchUnbindTemplatesRequest,
    ) -> main_models.BatchUnbindTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.batch_unbind_templates_with_options_async(request, runtime)

    def bind_directory_with_options(
        self,
        request: main_models.BindDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindDirectory',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_directory_with_options_async(
        self,
        request: main_models.BindDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindDirectory',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_directory(
        self,
        request: main_models.BindDirectoryRequest,
    ) -> main_models.BindDirectoryResponse:
        runtime = RuntimeOptions()
        return self.bind_directory_with_options(request, runtime)

    async def bind_directory_async(
        self,
        request: main_models.BindDirectoryRequest,
    ) -> main_models.BindDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.bind_directory_with_options_async(request, runtime)

    def bind_parent_platform_device_with_options(
        self,
        request: main_models.BindParentPlatformDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindParentPlatformDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindParentPlatformDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindParentPlatformDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_parent_platform_device_with_options_async(
        self,
        request: main_models.BindParentPlatformDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindParentPlatformDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindParentPlatformDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindParentPlatformDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_parent_platform_device(
        self,
        request: main_models.BindParentPlatformDeviceRequest,
    ) -> main_models.BindParentPlatformDeviceResponse:
        runtime = RuntimeOptions()
        return self.bind_parent_platform_device_with_options(request, runtime)

    async def bind_parent_platform_device_async(
        self,
        request: main_models.BindParentPlatformDeviceRequest,
    ) -> main_models.BindParentPlatformDeviceResponse:
        runtime = RuntimeOptions()
        return await self.bind_parent_platform_device_with_options_async(request, runtime)

    def bind_purchased_device_with_options(
        self,
        request: main_models.BindPurchasedDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindPurchasedDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindPurchasedDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindPurchasedDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_purchased_device_with_options_async(
        self,
        request: main_models.BindPurchasedDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindPurchasedDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindPurchasedDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindPurchasedDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_purchased_device(
        self,
        request: main_models.BindPurchasedDeviceRequest,
    ) -> main_models.BindPurchasedDeviceResponse:
        runtime = RuntimeOptions()
        return self.bind_purchased_device_with_options(request, runtime)

    async def bind_purchased_device_async(
        self,
        request: main_models.BindPurchasedDeviceRequest,
    ) -> main_models.BindPurchasedDeviceResponse:
        runtime = RuntimeOptions()
        return await self.bind_purchased_device_with_options_async(request, runtime)

    def bind_template_with_options(
        self,
        request: main_models.BindTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apply_all):
            query['ApplyAll'] = request.apply_all
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.replace):
            query['Replace'] = request.replace
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindTemplate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_template_with_options_async(
        self,
        request: main_models.BindTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.apply_all):
            query['ApplyAll'] = request.apply_all
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.replace):
            query['Replace'] = request.replace
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindTemplate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_template(
        self,
        request: main_models.BindTemplateRequest,
    ) -> main_models.BindTemplateResponse:
        runtime = RuntimeOptions()
        return self.bind_template_with_options(request, runtime)

    async def bind_template_async(
        self,
        request: main_models.BindTemplateRequest,
    ) -> main_models.BindTemplateResponse:
        runtime = RuntimeOptions()
        return await self.bind_template_with_options_async(request, runtime)

    def continuous_adjust_with_options(
        self,
        request: main_models.ContinuousAdjustRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContinuousAdjustResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.focus):
            query['Focus'] = request.focus
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.iris):
            query['Iris'] = request.iris
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ContinuousAdjust',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinuousAdjustResponse(),
            self.call_api(params, req, runtime)
        )

    async def continuous_adjust_with_options_async(
        self,
        request: main_models.ContinuousAdjustRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContinuousAdjustResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.focus):
            query['Focus'] = request.focus
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.iris):
            query['Iris'] = request.iris
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ContinuousAdjust',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinuousAdjustResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continuous_adjust(
        self,
        request: main_models.ContinuousAdjustRequest,
    ) -> main_models.ContinuousAdjustResponse:
        runtime = RuntimeOptions()
        return self.continuous_adjust_with_options(request, runtime)

    async def continuous_adjust_async(
        self,
        request: main_models.ContinuousAdjustRequest,
    ) -> main_models.ContinuousAdjustResponse:
        runtime = RuntimeOptions()
        return await self.continuous_adjust_with_options_async(request, runtime)

    def continuous_move_with_options(
        self,
        request: main_models.ContinuousMoveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContinuousMoveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pan):
            query['Pan'] = request.pan
        if not DaraCore.is_null(request.tilt):
            query['Tilt'] = request.tilt
        if not DaraCore.is_null(request.zoom):
            query['Zoom'] = request.zoom
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ContinuousMove',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinuousMoveResponse(),
            self.call_api(params, req, runtime)
        )

    async def continuous_move_with_options_async(
        self,
        request: main_models.ContinuousMoveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContinuousMoveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pan):
            query['Pan'] = request.pan
        if not DaraCore.is_null(request.tilt):
            query['Tilt'] = request.tilt
        if not DaraCore.is_null(request.zoom):
            query['Zoom'] = request.zoom
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ContinuousMove',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinuousMoveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continuous_move(
        self,
        request: main_models.ContinuousMoveRequest,
    ) -> main_models.ContinuousMoveResponse:
        runtime = RuntimeOptions()
        return self.continuous_move_with_options(request, runtime)

    async def continuous_move_async(
        self,
        request: main_models.ContinuousMoveRequest,
    ) -> main_models.ContinuousMoveResponse:
        runtime = RuntimeOptions()
        return await self.continuous_move_with_options_async(request, runtime)

    def create_device_with_options(
        self,
        request: main_models.CreateDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_method):
            query['AlarmMethod'] = request.alarm_method
        if not DaraCore.is_null(request.auto_directory):
            query['AutoDirectory'] = request.auto_directory
        if not DaraCore.is_null(request.auto_pos):
            query['AutoPos'] = request.auto_pos
        if not DaraCore.is_null(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.dsn):
            query['Dsn'] = request.dsn
        if not DaraCore.is_null(request.gb_id):
            query['GbId'] = request.gb_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.latitude):
            query['Latitude'] = request.latitude
        if not DaraCore.is_null(request.longitude):
            query['Longitude'] = request.longitude
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.pos_interval):
            query['PosInterval'] = request.pos_interval
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_device_with_options_async(
        self,
        request: main_models.CreateDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_method):
            query['AlarmMethod'] = request.alarm_method
        if not DaraCore.is_null(request.auto_directory):
            query['AutoDirectory'] = request.auto_directory
        if not DaraCore.is_null(request.auto_pos):
            query['AutoPos'] = request.auto_pos
        if not DaraCore.is_null(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.dsn):
            query['Dsn'] = request.dsn
        if not DaraCore.is_null(request.gb_id):
            query['GbId'] = request.gb_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.latitude):
            query['Latitude'] = request.latitude
        if not DaraCore.is_null(request.longitude):
            query['Longitude'] = request.longitude
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.pos_interval):
            query['PosInterval'] = request.pos_interval
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_device(
        self,
        request: main_models.CreateDeviceRequest,
    ) -> main_models.CreateDeviceResponse:
        runtime = RuntimeOptions()
        return self.create_device_with_options(request, runtime)

    async def create_device_async(
        self,
        request: main_models.CreateDeviceRequest,
    ) -> main_models.CreateDeviceResponse:
        runtime = RuntimeOptions()
        return await self.create_device_with_options_async(request, runtime)

    def create_device_alarm_with_options(
        self,
        request: main_models.CreateDeviceAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeviceAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm):
            query['Alarm'] = request.alarm
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.expire):
            query['Expire'] = request.expire
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.sub_alarm):
            query['SubAlarm'] = request.sub_alarm
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeviceAlarm',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeviceAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_device_alarm_with_options_async(
        self,
        request: main_models.CreateDeviceAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeviceAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm):
            query['Alarm'] = request.alarm
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.expire):
            query['Expire'] = request.expire
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.sub_alarm):
            query['SubAlarm'] = request.sub_alarm
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeviceAlarm',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeviceAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_device_alarm(
        self,
        request: main_models.CreateDeviceAlarmRequest,
    ) -> main_models.CreateDeviceAlarmResponse:
        runtime = RuntimeOptions()
        return self.create_device_alarm_with_options(request, runtime)

    async def create_device_alarm_async(
        self,
        request: main_models.CreateDeviceAlarmRequest,
    ) -> main_models.CreateDeviceAlarmResponse:
        runtime = RuntimeOptions()
        return await self.create_device_alarm_with_options_async(request, runtime)

    def create_directory_with_options(
        self,
        request: main_models.CreateDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDirectory',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_directory_with_options_async(
        self,
        request: main_models.CreateDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDirectory',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_directory(
        self,
        request: main_models.CreateDirectoryRequest,
    ) -> main_models.CreateDirectoryResponse:
        runtime = RuntimeOptions()
        return self.create_directory_with_options(request, runtime)

    async def create_directory_async(
        self,
        request: main_models.CreateDirectoryRequest,
    ) -> main_models.CreateDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.create_directory_with_options_async(request, runtime)

    def create_group_with_options(
        self,
        request: main_models.CreateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app):
            query['App'] = request.app
        if not DaraCore.is_null(request.callback):
            query['Callback'] = request.callback
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.in_protocol):
            query['InProtocol'] = request.in_protocol
        if not DaraCore.is_null(request.lazy_pull):
            query['LazyPull'] = request.lazy_pull
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not DaraCore.is_null(request.push_domain):
            query['PushDomain'] = request.push_domain
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: main_models.CreateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app):
            query['App'] = request.app
        if not DaraCore.is_null(request.callback):
            query['Callback'] = request.callback
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.in_protocol):
            query['InProtocol'] = request.in_protocol
        if not DaraCore.is_null(request.lazy_pull):
            query['LazyPull'] = request.lazy_pull
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not DaraCore.is_null(request.push_domain):
            query['PushDomain'] = request.push_domain
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group(
        self,
        request: main_models.CreateGroupRequest,
    ) -> main_models.CreateGroupResponse:
        runtime = RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    async def create_group_async(
        self,
        request: main_models.CreateGroupRequest,
    ) -> main_models.CreateGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_group_with_options_async(request, runtime)

    def create_parent_platform_with_options(
        self,
        request: main_models.CreateParentPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateParentPlatformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not DaraCore.is_null(request.client_auth):
            query['ClientAuth'] = request.client_auth
        if not DaraCore.is_null(request.client_password):
            query['ClientPassword'] = request.client_password
        if not DaraCore.is_null(request.client_username):
            query['ClientUsername'] = request.client_username
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.gb_id):
            query['GbId'] = request.gb_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateParentPlatform',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateParentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_parent_platform_with_options_async(
        self,
        request: main_models.CreateParentPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateParentPlatformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not DaraCore.is_null(request.client_auth):
            query['ClientAuth'] = request.client_auth
        if not DaraCore.is_null(request.client_password):
            query['ClientPassword'] = request.client_password
        if not DaraCore.is_null(request.client_username):
            query['ClientUsername'] = request.client_username
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.gb_id):
            query['GbId'] = request.gb_id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateParentPlatform',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateParentPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_parent_platform(
        self,
        request: main_models.CreateParentPlatformRequest,
    ) -> main_models.CreateParentPlatformResponse:
        runtime = RuntimeOptions()
        return self.create_parent_platform_with_options(request, runtime)

    async def create_parent_platform_async(
        self,
        request: main_models.CreateParentPlatformRequest,
    ) -> main_models.CreateParentPlatformResponse:
        runtime = RuntimeOptions()
        return await self.create_parent_platform_with_options_async(request, runtime)

    def create_rendering_data_package_with_options(
        self,
        request: main_models.CreateRenderingDataPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRenderingDataPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_billing_cycle):
            query['InstanceBillingCycle'] = request.instance_billing_cycle
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRenderingDataPackage',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRenderingDataPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rendering_data_package_with_options_async(
        self,
        request: main_models.CreateRenderingDataPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRenderingDataPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_billing_cycle):
            query['InstanceBillingCycle'] = request.instance_billing_cycle
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRenderingDataPackage',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRenderingDataPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rendering_data_package(
        self,
        request: main_models.CreateRenderingDataPackageRequest,
    ) -> main_models.CreateRenderingDataPackageResponse:
        runtime = RuntimeOptions()
        return self.create_rendering_data_package_with_options(request, runtime)

    async def create_rendering_data_package_async(
        self,
        request: main_models.CreateRenderingDataPackageRequest,
    ) -> main_models.CreateRenderingDataPackageResponse:
        runtime = RuntimeOptions()
        return await self.create_rendering_data_package_with_options_async(request, runtime)

    def create_rendering_instance_with_options(
        self,
        tmp_req: main_models.CreateRenderingInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRenderingInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateRenderingInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attributes):
            request.attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        if not DaraCore.is_null(tmp_req.client_info):
            request.client_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_info, 'ClientInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.attributes_shrink):
            query['Attributes'] = request.attributes_shrink
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.client_info_shrink):
            query['ClientInfo'] = request.client_info_shrink
        if not DaraCore.is_null(request.instance_billing_cycle):
            query['InstanceBillingCycle'] = request.instance_billing_cycle
        if not DaraCore.is_null(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.internet_max_bandwidth):
            query['InternetMaxBandwidth'] = request.internet_max_bandwidth
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.rendering_spec):
            query['RenderingSpec'] = request.rendering_spec
        if not DaraCore.is_null(request.storage_size):
            query['StorageSize'] = request.storage_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRenderingInstance',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRenderingInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rendering_instance_with_options_async(
        self,
        tmp_req: main_models.CreateRenderingInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRenderingInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateRenderingInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attributes):
            request.attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        if not DaraCore.is_null(tmp_req.client_info):
            request.client_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_info, 'ClientInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.attributes_shrink):
            query['Attributes'] = request.attributes_shrink
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.client_info_shrink):
            query['ClientInfo'] = request.client_info_shrink
        if not DaraCore.is_null(request.instance_billing_cycle):
            query['InstanceBillingCycle'] = request.instance_billing_cycle
        if not DaraCore.is_null(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not DaraCore.is_null(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not DaraCore.is_null(request.internet_max_bandwidth):
            query['InternetMaxBandwidth'] = request.internet_max_bandwidth
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.rendering_spec):
            query['RenderingSpec'] = request.rendering_spec
        if not DaraCore.is_null(request.storage_size):
            query['StorageSize'] = request.storage_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRenderingInstance',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRenderingInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rendering_instance(
        self,
        request: main_models.CreateRenderingInstanceRequest,
    ) -> main_models.CreateRenderingInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_rendering_instance_with_options(request, runtime)

    async def create_rendering_instance_async(
        self,
        request: main_models.CreateRenderingInstanceRequest,
    ) -> main_models.CreateRenderingInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_rendering_instance_with_options_async(request, runtime)

    def create_rendering_instance_gateway_with_options(
        self,
        request: main_models.CreateRenderingInstanceGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRenderingInstanceGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_instance_id):
            query['GatewayInstanceId'] = request.gateway_instance_id
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRenderingInstanceGateway',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRenderingInstanceGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rendering_instance_gateway_with_options_async(
        self,
        request: main_models.CreateRenderingInstanceGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRenderingInstanceGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_instance_id):
            query['GatewayInstanceId'] = request.gateway_instance_id
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRenderingInstanceGateway',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRenderingInstanceGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rendering_instance_gateway(
        self,
        request: main_models.CreateRenderingInstanceGatewayRequest,
    ) -> main_models.CreateRenderingInstanceGatewayResponse:
        runtime = RuntimeOptions()
        return self.create_rendering_instance_gateway_with_options(request, runtime)

    async def create_rendering_instance_gateway_async(
        self,
        request: main_models.CreateRenderingInstanceGatewayRequest,
    ) -> main_models.CreateRenderingInstanceGatewayResponse:
        runtime = RuntimeOptions()
        return await self.create_rendering_instance_gateway_with_options_async(request, runtime)

    def create_rendering_project_with_options(
        self,
        tmp_req: main_models.CreateRenderingProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRenderingProjectResponse:
        tmp_req.validate()
        request = main_models.CreateRenderingProjectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.session_attribs):
            request.session_attribs_shrink = Utils.array_to_string_with_specified_style(tmp_req.session_attribs, 'SessionAttribs', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.session_attribs_shrink):
            query['SessionAttribs'] = request.session_attribs_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRenderingProject',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRenderingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rendering_project_with_options_async(
        self,
        tmp_req: main_models.CreateRenderingProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRenderingProjectResponse:
        tmp_req.validate()
        request = main_models.CreateRenderingProjectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.session_attribs):
            request.session_attribs_shrink = Utils.array_to_string_with_specified_style(tmp_req.session_attribs, 'SessionAttribs', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.session_attribs_shrink):
            query['SessionAttribs'] = request.session_attribs_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRenderingProject',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRenderingProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rendering_project(
        self,
        request: main_models.CreateRenderingProjectRequest,
    ) -> main_models.CreateRenderingProjectResponse:
        runtime = RuntimeOptions()
        return self.create_rendering_project_with_options(request, runtime)

    async def create_rendering_project_async(
        self,
        request: main_models.CreateRenderingProjectRequest,
    ) -> main_models.CreateRenderingProjectResponse:
        runtime = RuntimeOptions()
        return await self.create_rendering_project_with_options_async(request, runtime)

    def create_stream_snapshot_with_options(
        self,
        request: main_models.CreateStreamSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStreamSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.location):
            query['Location'] = request.location
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStreamSnapshot',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStreamSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_stream_snapshot_with_options_async(
        self,
        request: main_models.CreateStreamSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStreamSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.location):
            query['Location'] = request.location
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStreamSnapshot',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStreamSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_stream_snapshot(
        self,
        request: main_models.CreateStreamSnapshotRequest,
    ) -> main_models.CreateStreamSnapshotResponse:
        runtime = RuntimeOptions()
        return self.create_stream_snapshot_with_options(request, runtime)

    async def create_stream_snapshot_async(
        self,
        request: main_models.CreateStreamSnapshotRequest,
    ) -> main_models.CreateStreamSnapshotResponse:
        runtime = RuntimeOptions()
        return await self.create_stream_snapshot_with_options_async(request, runtime)

    def create_template_with_options(
        self,
        request: main_models.CreateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callback):
            query['Callback'] = request.callback
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_format):
            query['FileFormat'] = request.file_format
        if not DaraCore.is_null(request.flv):
            query['Flv'] = request.flv
        if not DaraCore.is_null(request.hls_m3u_8):
            query['HlsM3u8'] = request.hls_m3u_8
        if not DaraCore.is_null(request.hls_ts):
            query['HlsTs'] = request.hls_ts
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.jpg_on_demand):
            query['JpgOnDemand'] = request.jpg_on_demand
        if not DaraCore.is_null(request.jpg_overwrite):
            query['JpgOverwrite'] = request.jpg_overwrite
        if not DaraCore.is_null(request.jpg_sequence):
            query['JpgSequence'] = request.jpg_sequence
        if not DaraCore.is_null(request.mp_4):
            query['Mp4'] = request.mp_4
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.retention):
            query['Retention'] = request.retention
        if not DaraCore.is_null(request.trans_configs_json):
            query['TransConfigsJSON'] = request.trans_configs_json
        if not DaraCore.is_null(request.trigger):
            query['Trigger'] = request.trigger
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: main_models.CreateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callback):
            query['Callback'] = request.callback
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_format):
            query['FileFormat'] = request.file_format
        if not DaraCore.is_null(request.flv):
            query['Flv'] = request.flv
        if not DaraCore.is_null(request.hls_m3u_8):
            query['HlsM3u8'] = request.hls_m3u_8
        if not DaraCore.is_null(request.hls_ts):
            query['HlsTs'] = request.hls_ts
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.jpg_on_demand):
            query['JpgOnDemand'] = request.jpg_on_demand
        if not DaraCore.is_null(request.jpg_overwrite):
            query['JpgOverwrite'] = request.jpg_overwrite
        if not DaraCore.is_null(request.jpg_sequence):
            query['JpgSequence'] = request.jpg_sequence
        if not DaraCore.is_null(request.mp_4):
            query['Mp4'] = request.mp_4
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.retention):
            query['Retention'] = request.retention
        if not DaraCore.is_null(request.trans_configs_json):
            query['TransConfigsJSON'] = request.trans_configs_json
        if not DaraCore.is_null(request.trigger):
            query['Trigger'] = request.trigger
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    async def create_template_async(
        self,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_template_with_options_async(request, runtime)

    def delete_cloud_app_with_options(
        self,
        request: main_models.DeleteCloudAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudApp',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_app_with_options_async(
        self,
        request: main_models.DeleteCloudAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudApp',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_app(
        self,
        request: main_models.DeleteCloudAppRequest,
    ) -> main_models.DeleteCloudAppResponse:
        runtime = RuntimeOptions()
        return self.delete_cloud_app_with_options(request, runtime)

    async def delete_cloud_app_async(
        self,
        request: main_models.DeleteCloudAppRequest,
    ) -> main_models.DeleteCloudAppResponse:
        runtime = RuntimeOptions()
        return await self.delete_cloud_app_with_options_async(request, runtime)

    def delete_device_with_options(
        self,
        request: main_models.DeleteDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_device_with_options_async(
        self,
        request: main_models.DeleteDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_device(
        self,
        request: main_models.DeleteDeviceRequest,
    ) -> main_models.DeleteDeviceResponse:
        runtime = RuntimeOptions()
        return self.delete_device_with_options(request, runtime)

    async def delete_device_async(
        self,
        request: main_models.DeleteDeviceRequest,
    ) -> main_models.DeleteDeviceResponse:
        runtime = RuntimeOptions()
        return await self.delete_device_with_options_async(request, runtime)

    def delete_directory_with_options(
        self,
        request: main_models.DeleteDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDirectory',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_directory_with_options_async(
        self,
        request: main_models.DeleteDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDirectory',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_directory(
        self,
        request: main_models.DeleteDirectoryRequest,
    ) -> main_models.DeleteDirectoryResponse:
        runtime = RuntimeOptions()
        return self.delete_directory_with_options(request, runtime)

    async def delete_directory_async(
        self,
        request: main_models.DeleteDirectoryRequest,
    ) -> main_models.DeleteDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.delete_directory_with_options_async(request, runtime)

    def delete_file_with_options(
        self,
        request: main_models.DeleteFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFile',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_with_options_async(
        self,
        request: main_models.DeleteFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFile',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_file(
        self,
        request: main_models.DeleteFileRequest,
    ) -> main_models.DeleteFileResponse:
        runtime = RuntimeOptions()
        return self.delete_file_with_options(request, runtime)

    async def delete_file_async(
        self,
        request: main_models.DeleteFileRequest,
    ) -> main_models.DeleteFileResponse:
        runtime = RuntimeOptions()
        return await self.delete_file_with_options_async(request, runtime)

    def delete_group_with_options(
        self,
        request: main_models.DeleteGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroup',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        request: main_models.DeleteGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroup',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group(
        self,
        request: main_models.DeleteGroupRequest,
    ) -> main_models.DeleteGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    async def delete_group_async(
        self,
        request: main_models.DeleteGroupRequest,
    ) -> main_models.DeleteGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_group_with_options_async(request, runtime)

    def delete_parent_platform_with_options(
        self,
        request: main_models.DeleteParentPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteParentPlatformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteParentPlatform',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteParentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_parent_platform_with_options_async(
        self,
        request: main_models.DeleteParentPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteParentPlatformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteParentPlatform',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteParentPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_parent_platform(
        self,
        request: main_models.DeleteParentPlatformRequest,
    ) -> main_models.DeleteParentPlatformResponse:
        runtime = RuntimeOptions()
        return self.delete_parent_platform_with_options(request, runtime)

    async def delete_parent_platform_async(
        self,
        request: main_models.DeleteParentPlatformRequest,
    ) -> main_models.DeleteParentPlatformResponse:
        runtime = RuntimeOptions()
        return await self.delete_parent_platform_with_options_async(request, runtime)

    def delete_preset_with_options(
        self,
        request: main_models.DeletePresetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePresetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preset_id):
            query['PresetId'] = request.preset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePreset',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePresetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_preset_with_options_async(
        self,
        request: main_models.DeletePresetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePresetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preset_id):
            query['PresetId'] = request.preset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePreset',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePresetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_preset(
        self,
        request: main_models.DeletePresetRequest,
    ) -> main_models.DeletePresetResponse:
        runtime = RuntimeOptions()
        return self.delete_preset_with_options(request, runtime)

    async def delete_preset_async(
        self,
        request: main_models.DeletePresetRequest,
    ) -> main_models.DeletePresetResponse:
        runtime = RuntimeOptions()
        return await self.delete_preset_with_options_async(request, runtime)

    def delete_public_key_with_options(
        self,
        request: main_models.DeletePublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_name):
            query['KeyName'] = request.key_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePublicKey',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_public_key_with_options_async(
        self,
        request: main_models.DeletePublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_name):
            query['KeyName'] = request.key_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePublicKey',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_public_key(
        self,
        request: main_models.DeletePublicKeyRequest,
    ) -> main_models.DeletePublicKeyResponse:
        runtime = RuntimeOptions()
        return self.delete_public_key_with_options(request, runtime)

    async def delete_public_key_async(
        self,
        request: main_models.DeletePublicKeyRequest,
    ) -> main_models.DeletePublicKeyResponse:
        runtime = RuntimeOptions()
        return await self.delete_public_key_with_options_async(request, runtime)

    def delete_rendering_instance_configuration_with_options(
        self,
        tmp_req: main_models.DeleteRenderingInstanceConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRenderingInstanceConfigurationResponse:
        tmp_req.validate()
        request = main_models.DeleteRenderingInstanceConfigurationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.configuration):
            request.configuration_shrink = Utils.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        body = {}
        if not DaraCore.is_null(request.configuration_shrink):
            body['Configuration'] = request.configuration_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRenderingInstanceConfiguration',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRenderingInstanceConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rendering_instance_configuration_with_options_async(
        self,
        tmp_req: main_models.DeleteRenderingInstanceConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRenderingInstanceConfigurationResponse:
        tmp_req.validate()
        request = main_models.DeleteRenderingInstanceConfigurationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.configuration):
            request.configuration_shrink = Utils.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        body = {}
        if not DaraCore.is_null(request.configuration_shrink):
            body['Configuration'] = request.configuration_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRenderingInstanceConfiguration',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRenderingInstanceConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rendering_instance_configuration(
        self,
        request: main_models.DeleteRenderingInstanceConfigurationRequest,
    ) -> main_models.DeleteRenderingInstanceConfigurationResponse:
        runtime = RuntimeOptions()
        return self.delete_rendering_instance_configuration_with_options(request, runtime)

    async def delete_rendering_instance_configuration_async(
        self,
        request: main_models.DeleteRenderingInstanceConfigurationRequest,
    ) -> main_models.DeleteRenderingInstanceConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.delete_rendering_instance_configuration_with_options_async(request, runtime)

    def delete_rendering_instance_gateway_with_options(
        self,
        request: main_models.DeleteRenderingInstanceGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRenderingInstanceGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRenderingInstanceGateway',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRenderingInstanceGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rendering_instance_gateway_with_options_async(
        self,
        request: main_models.DeleteRenderingInstanceGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRenderingInstanceGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRenderingInstanceGateway',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRenderingInstanceGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rendering_instance_gateway(
        self,
        request: main_models.DeleteRenderingInstanceGatewayRequest,
    ) -> main_models.DeleteRenderingInstanceGatewayResponse:
        runtime = RuntimeOptions()
        return self.delete_rendering_instance_gateway_with_options(request, runtime)

    async def delete_rendering_instance_gateway_async(
        self,
        request: main_models.DeleteRenderingInstanceGatewayRequest,
    ) -> main_models.DeleteRenderingInstanceGatewayResponse:
        runtime = RuntimeOptions()
        return await self.delete_rendering_instance_gateway_with_options_async(request, runtime)

    def delete_rendering_instance_settings_with_options(
        self,
        tmp_req: main_models.DeleteRenderingInstanceSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRenderingInstanceSettingsResponse:
        tmp_req.validate()
        request = main_models.DeleteRenderingInstanceSettingsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attribute_names):
            request.attribute_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.attribute_names, 'AttributeNames', 'json')
        query = {}
        if not DaraCore.is_null(request.attribute_names_shrink):
            query['AttributeNames'] = request.attribute_names_shrink
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRenderingInstanceSettings',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRenderingInstanceSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rendering_instance_settings_with_options_async(
        self,
        tmp_req: main_models.DeleteRenderingInstanceSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRenderingInstanceSettingsResponse:
        tmp_req.validate()
        request = main_models.DeleteRenderingInstanceSettingsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attribute_names):
            request.attribute_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.attribute_names, 'AttributeNames', 'json')
        query = {}
        if not DaraCore.is_null(request.attribute_names_shrink):
            query['AttributeNames'] = request.attribute_names_shrink
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRenderingInstanceSettings',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRenderingInstanceSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rendering_instance_settings(
        self,
        request: main_models.DeleteRenderingInstanceSettingsRequest,
    ) -> main_models.DeleteRenderingInstanceSettingsResponse:
        runtime = RuntimeOptions()
        return self.delete_rendering_instance_settings_with_options(request, runtime)

    async def delete_rendering_instance_settings_async(
        self,
        request: main_models.DeleteRenderingInstanceSettingsRequest,
    ) -> main_models.DeleteRenderingInstanceSettingsResponse:
        runtime = RuntimeOptions()
        return await self.delete_rendering_instance_settings_with_options_async(request, runtime)

    def delete_rendering_project_with_options(
        self,
        request: main_models.DeleteRenderingProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRenderingProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRenderingProject',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRenderingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rendering_project_with_options_async(
        self,
        request: main_models.DeleteRenderingProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRenderingProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRenderingProject',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRenderingProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rendering_project(
        self,
        request: main_models.DeleteRenderingProjectRequest,
    ) -> main_models.DeleteRenderingProjectResponse:
        runtime = RuntimeOptions()
        return self.delete_rendering_project_with_options(request, runtime)

    async def delete_rendering_project_async(
        self,
        request: main_models.DeleteRenderingProjectRequest,
    ) -> main_models.DeleteRenderingProjectResponse:
        runtime = RuntimeOptions()
        return await self.delete_rendering_project_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: main_models.DeleteTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: main_models.DeleteTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        request: main_models.DeleteTemplateRequest,
    ) -> main_models.DeleteTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: main_models.DeleteTemplateRequest,
    ) -> main_models.DeleteTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def delete_vs_pull_stream_info_config_with_options(
        self,
        request: main_models.DeleteVsPullStreamInfoConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVsPullStreamInfoConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVsPullStreamInfoConfig',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVsPullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vs_pull_stream_info_config_with_options_async(
        self,
        request: main_models.DeleteVsPullStreamInfoConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVsPullStreamInfoConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVsPullStreamInfoConfig',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVsPullStreamInfoConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vs_pull_stream_info_config(
        self,
        request: main_models.DeleteVsPullStreamInfoConfigRequest,
    ) -> main_models.DeleteVsPullStreamInfoConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_vs_pull_stream_info_config_with_options(request, runtime)

    async def delete_vs_pull_stream_info_config_async(
        self,
        request: main_models.DeleteVsPullStreamInfoConfigRequest,
    ) -> main_models.DeleteVsPullStreamInfoConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_vs_pull_stream_info_config_with_options_async(request, runtime)

    def delete_vs_streams_notify_url_config_with_options(
        self,
        request: main_models.DeleteVsStreamsNotifyUrlConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVsStreamsNotifyUrlConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVsStreamsNotifyUrlConfig',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVsStreamsNotifyUrlConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vs_streams_notify_url_config_with_options_async(
        self,
        request: main_models.DeleteVsStreamsNotifyUrlConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVsStreamsNotifyUrlConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVsStreamsNotifyUrlConfig',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVsStreamsNotifyUrlConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vs_streams_notify_url_config(
        self,
        request: main_models.DeleteVsStreamsNotifyUrlConfigRequest,
    ) -> main_models.DeleteVsStreamsNotifyUrlConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_vs_streams_notify_url_config_with_options(request, runtime)

    async def delete_vs_streams_notify_url_config_async(
        self,
        request: main_models.DeleteVsStreamsNotifyUrlConfigRequest,
    ) -> main_models.DeleteVsStreamsNotifyUrlConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_vs_streams_notify_url_config_with_options_async(request, runtime)

    def describe_account_stat_with_options(
        self,
        request: main_models.DescribeAccountStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccountStat',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_stat_with_options_async(
        self,
        request: main_models.DescribeAccountStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccountStat',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_stat(
        self,
        request: main_models.DescribeAccountStatRequest,
    ) -> main_models.DescribeAccountStatResponse:
        runtime = RuntimeOptions()
        return self.describe_account_stat_with_options(request, runtime)

    async def describe_account_stat_async(
        self,
        request: main_models.DescribeAccountStatRequest,
    ) -> main_models.DescribeAccountStatResponse:
        runtime = RuntimeOptions()
        return await self.describe_account_stat_with_options_async(request, runtime)

    def describe_device_with_options(
        self,
        request: main_models.DescribeDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.include_directory):
            query['IncludeDirectory'] = request.include_directory
        if not DaraCore.is_null(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_device_with_options_async(
        self,
        request: main_models.DescribeDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.include_directory):
            query['IncludeDirectory'] = request.include_directory
        if not DaraCore.is_null(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_device(
        self,
        request: main_models.DescribeDeviceRequest,
    ) -> main_models.DescribeDeviceResponse:
        runtime = RuntimeOptions()
        return self.describe_device_with_options(request, runtime)

    async def describe_device_async(
        self,
        request: main_models.DescribeDeviceRequest,
    ) -> main_models.DescribeDeviceResponse:
        runtime = RuntimeOptions()
        return await self.describe_device_with_options_async(request, runtime)

    def describe_device_channels_with_options(
        self,
        request: main_models.DescribeDeviceChannelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeviceChannelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeviceChannels',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeviceChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_device_channels_with_options_async(
        self,
        request: main_models.DescribeDeviceChannelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeviceChannelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeviceChannels',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeviceChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_device_channels(
        self,
        request: main_models.DescribeDeviceChannelsRequest,
    ) -> main_models.DescribeDeviceChannelsResponse:
        runtime = RuntimeOptions()
        return self.describe_device_channels_with_options(request, runtime)

    async def describe_device_channels_async(
        self,
        request: main_models.DescribeDeviceChannelsRequest,
    ) -> main_models.DescribeDeviceChannelsResponse:
        runtime = RuntimeOptions()
        return await self.describe_device_channels_with_options_async(request, runtime)

    def describe_device_gateway_with_options(
        self,
        request: main_models.DescribeDeviceGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeviceGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.expire):
            query['Expire'] = request.expire
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeviceGateway',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeviceGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_device_gateway_with_options_async(
        self,
        request: main_models.DescribeDeviceGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeviceGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.expire):
            query['Expire'] = request.expire
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeviceGateway',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeviceGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_device_gateway(
        self,
        request: main_models.DescribeDeviceGatewayRequest,
    ) -> main_models.DescribeDeviceGatewayResponse:
        runtime = RuntimeOptions()
        return self.describe_device_gateway_with_options(request, runtime)

    async def describe_device_gateway_async(
        self,
        request: main_models.DescribeDeviceGatewayRequest,
    ) -> main_models.DescribeDeviceGatewayResponse:
        runtime = RuntimeOptions()
        return await self.describe_device_gateway_with_options_async(request, runtime)

    def describe_device_urlwith_options(
        self,
        request: main_models.DescribeDeviceURLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeviceURLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth):
            query['Auth'] = request.auth
        if not DaraCore.is_null(request.expire):
            query['Expire'] = request.expire
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.stream):
            query['Stream'] = request.stream
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeviceURL',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeviceURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_device_urlwith_options_async(
        self,
        request: main_models.DescribeDeviceURLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeviceURLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth):
            query['Auth'] = request.auth
        if not DaraCore.is_null(request.expire):
            query['Expire'] = request.expire
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.stream):
            query['Stream'] = request.stream
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeviceURL',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeviceURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_device_url(
        self,
        request: main_models.DescribeDeviceURLRequest,
    ) -> main_models.DescribeDeviceURLResponse:
        runtime = RuntimeOptions()
        return self.describe_device_urlwith_options(request, runtime)

    async def describe_device_url_async(
        self,
        request: main_models.DescribeDeviceURLRequest,
    ) -> main_models.DescribeDeviceURLResponse:
        runtime = RuntimeOptions()
        return await self.describe_device_urlwith_options_async(request, runtime)

    def describe_devices_with_options(
        self,
        request: main_models.DescribeDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.dsn):
            query['Dsn'] = request.dsn
        if not DaraCore.is_null(request.gb_id):
            query['GbId'] = request.gb_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.include_directory):
            query['IncludeDirectory'] = request.include_directory
        if not DaraCore.is_null(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_devices_with_options_async(
        self,
        request: main_models.DescribeDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.dsn):
            query['Dsn'] = request.dsn
        if not DaraCore.is_null(request.gb_id):
            query['GbId'] = request.gb_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.include_directory):
            query['IncludeDirectory'] = request.include_directory
        if not DaraCore.is_null(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_devices(
        self,
        request: main_models.DescribeDevicesRequest,
    ) -> main_models.DescribeDevicesResponse:
        runtime = RuntimeOptions()
        return self.describe_devices_with_options(request, runtime)

    async def describe_devices_async(
        self,
        request: main_models.DescribeDevicesRequest,
    ) -> main_models.DescribeDevicesResponse:
        runtime = RuntimeOptions()
        return await self.describe_devices_with_options_async(request, runtime)

    def describe_directories_with_options(
        self,
        request: main_models.DescribeDirectoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDirectoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.no_pagination):
            query['NoPagination'] = request.no_pagination
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDirectories',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_directories_with_options_async(
        self,
        request: main_models.DescribeDirectoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDirectoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.no_pagination):
            query['NoPagination'] = request.no_pagination
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDirectories',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_directories(
        self,
        request: main_models.DescribeDirectoriesRequest,
    ) -> main_models.DescribeDirectoriesResponse:
        runtime = RuntimeOptions()
        return self.describe_directories_with_options(request, runtime)

    async def describe_directories_async(
        self,
        request: main_models.DescribeDirectoriesRequest,
    ) -> main_models.DescribeDirectoriesResponse:
        runtime = RuntimeOptions()
        return await self.describe_directories_with_options_async(request, runtime)

    def describe_directory_with_options(
        self,
        request: main_models.DescribeDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDirectory',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_directory_with_options_async(
        self,
        request: main_models.DescribeDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDirectory',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_directory(
        self,
        request: main_models.DescribeDirectoryRequest,
    ) -> main_models.DescribeDirectoryResponse:
        runtime = RuntimeOptions()
        return self.describe_directory_with_options(request, runtime)

    async def describe_directory_async(
        self,
        request: main_models.DescribeDirectoryRequest,
    ) -> main_models.DescribeDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.describe_directory_with_options_async(request, runtime)

    def describe_group_with_options(
        self,
        request: main_models.DescribeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroup',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_with_options_async(
        self,
        request: main_models.DescribeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroup',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group(
        self,
        request: main_models.DescribeGroupRequest,
    ) -> main_models.DescribeGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_group_with_options(request, runtime)

    async def describe_group_async(
        self,
        request: main_models.DescribeGroupRequest,
    ) -> main_models.DescribeGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_group_with_options_async(request, runtime)

    def describe_groups_with_options(
        self,
        request: main_models.DescribeGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.in_protocol):
            query['InProtocol'] = request.in_protocol
        if not DaraCore.is_null(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroups',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_groups_with_options_async(
        self,
        request: main_models.DescribeGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.in_protocol):
            query['InProtocol'] = request.in_protocol
        if not DaraCore.is_null(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroups',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_groups(
        self,
        request: main_models.DescribeGroupsRequest,
    ) -> main_models.DescribeGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_groups_with_options(request, runtime)

    async def describe_groups_async(
        self,
        request: main_models.DescribeGroupsRequest,
    ) -> main_models.DescribeGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_groups_with_options_async(request, runtime)

    def describe_parent_platform_with_options(
        self,
        request: main_models.DescribeParentPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParentPlatformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParentPlatform',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parent_platform_with_options_async(
        self,
        request: main_models.DescribeParentPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParentPlatformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParentPlatform',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParentPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parent_platform(
        self,
        request: main_models.DescribeParentPlatformRequest,
    ) -> main_models.DescribeParentPlatformResponse:
        runtime = RuntimeOptions()
        return self.describe_parent_platform_with_options(request, runtime)

    async def describe_parent_platform_async(
        self,
        request: main_models.DescribeParentPlatformRequest,
    ) -> main_models.DescribeParentPlatformResponse:
        runtime = RuntimeOptions()
        return await self.describe_parent_platform_with_options_async(request, runtime)

    def describe_parent_platform_devices_with_options(
        self,
        request: main_models.DescribeParentPlatformDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParentPlatformDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParentPlatformDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParentPlatformDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parent_platform_devices_with_options_async(
        self,
        request: main_models.DescribeParentPlatformDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParentPlatformDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParentPlatformDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParentPlatformDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parent_platform_devices(
        self,
        request: main_models.DescribeParentPlatformDevicesRequest,
    ) -> main_models.DescribeParentPlatformDevicesResponse:
        runtime = RuntimeOptions()
        return self.describe_parent_platform_devices_with_options(request, runtime)

    async def describe_parent_platform_devices_async(
        self,
        request: main_models.DescribeParentPlatformDevicesRequest,
    ) -> main_models.DescribeParentPlatformDevicesResponse:
        runtime = RuntimeOptions()
        return await self.describe_parent_platform_devices_with_options_async(request, runtime)

    def describe_parent_platforms_with_options(
        self,
        request: main_models.DescribeParentPlatformsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParentPlatformsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gb_id):
            query['GbId'] = request.gb_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParentPlatforms',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParentPlatformsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parent_platforms_with_options_async(
        self,
        request: main_models.DescribeParentPlatformsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParentPlatformsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gb_id):
            query['GbId'] = request.gb_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParentPlatforms',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParentPlatformsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parent_platforms(
        self,
        request: main_models.DescribeParentPlatformsRequest,
    ) -> main_models.DescribeParentPlatformsResponse:
        runtime = RuntimeOptions()
        return self.describe_parent_platforms_with_options(request, runtime)

    async def describe_parent_platforms_async(
        self,
        request: main_models.DescribeParentPlatformsRequest,
    ) -> main_models.DescribeParentPlatformsResponse:
        runtime = RuntimeOptions()
        return await self.describe_parent_platforms_with_options_async(request, runtime)

    def describe_presets_with_options(
        self,
        request: main_models.DescribePresetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePresetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePresets',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePresetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_presets_with_options_async(
        self,
        request: main_models.DescribePresetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePresetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePresets',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePresetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_presets(
        self,
        request: main_models.DescribePresetsRequest,
    ) -> main_models.DescribePresetsResponse:
        runtime = RuntimeOptions()
        return self.describe_presets_with_options(request, runtime)

    async def describe_presets_async(
        self,
        request: main_models.DescribePresetsRequest,
    ) -> main_models.DescribePresetsResponse:
        runtime = RuntimeOptions()
        return await self.describe_presets_with_options_async(request, runtime)

    def describe_publish_stream_status_with_options(
        self,
        request: main_models.DescribePublishStreamStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePublishStreamStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePublishStreamStatus',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePublishStreamStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_publish_stream_status_with_options_async(
        self,
        request: main_models.DescribePublishStreamStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePublishStreamStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePublishStreamStatus',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePublishStreamStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_publish_stream_status(
        self,
        request: main_models.DescribePublishStreamStatusRequest,
    ) -> main_models.DescribePublishStreamStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_publish_stream_status_with_options(request, runtime)

    async def describe_publish_stream_status_async(
        self,
        request: main_models.DescribePublishStreamStatusRequest,
    ) -> main_models.DescribePublishStreamStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_publish_stream_status_with_options_async(request, runtime)

    def describe_purchased_device_with_options(
        self,
        request: main_models.DescribePurchasedDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePurchasedDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePurchasedDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePurchasedDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_device_with_options_async(
        self,
        request: main_models.DescribePurchasedDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePurchasedDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePurchasedDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePurchasedDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_device(
        self,
        request: main_models.DescribePurchasedDeviceRequest,
    ) -> main_models.DescribePurchasedDeviceResponse:
        runtime = RuntimeOptions()
        return self.describe_purchased_device_with_options(request, runtime)

    async def describe_purchased_device_async(
        self,
        request: main_models.DescribePurchasedDeviceRequest,
    ) -> main_models.DescribePurchasedDeviceResponse:
        runtime = RuntimeOptions()
        return await self.describe_purchased_device_with_options_async(request, runtime)

    def describe_purchased_devices_with_options(
        self,
        request: main_models.DescribePurchasedDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePurchasedDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not DaraCore.is_null(request.sub_type):
            query['SubType'] = request.sub_type
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePurchasedDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePurchasedDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_devices_with_options_async(
        self,
        request: main_models.DescribePurchasedDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePurchasedDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not DaraCore.is_null(request.sub_type):
            query['SubType'] = request.sub_type
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePurchasedDevices',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePurchasedDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_devices(
        self,
        request: main_models.DescribePurchasedDevicesRequest,
    ) -> main_models.DescribePurchasedDevicesResponse:
        runtime = RuntimeOptions()
        return self.describe_purchased_devices_with_options(request, runtime)

    async def describe_purchased_devices_async(
        self,
        request: main_models.DescribePurchasedDevicesRequest,
    ) -> main_models.DescribePurchasedDevicesResponse:
        runtime = RuntimeOptions()
        return await self.describe_purchased_devices_with_options_async(request, runtime)

    def describe_records_with_options(
        self,
        request: main_models.DescribeRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.private_bucket):
            query['PrivateBucket'] = request.private_bucket
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.stream_id):
            query['StreamId'] = request.stream_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecords',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_records_with_options_async(
        self,
        request: main_models.DescribeRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.private_bucket):
            query['PrivateBucket'] = request.private_bucket
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.stream_id):
            query['StreamId'] = request.stream_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecords',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_records(
        self,
        request: main_models.DescribeRecordsRequest,
    ) -> main_models.DescribeRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_records_with_options(request, runtime)

    async def describe_records_async(
        self,
        request: main_models.DescribeRecordsRequest,
    ) -> main_models.DescribeRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_records_with_options_async(request, runtime)

    def describe_rendering_instance_with_options(
        self,
        request: main_models.DescribeRenderingInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRenderingInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRenderingInstance',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRenderingInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rendering_instance_with_options_async(
        self,
        request: main_models.DescribeRenderingInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRenderingInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRenderingInstance',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRenderingInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rendering_instance(
        self,
        request: main_models.DescribeRenderingInstanceRequest,
    ) -> main_models.DescribeRenderingInstanceResponse:
        runtime = RuntimeOptions()
        return self.describe_rendering_instance_with_options(request, runtime)

    async def describe_rendering_instance_async(
        self,
        request: main_models.DescribeRenderingInstanceRequest,
    ) -> main_models.DescribeRenderingInstanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_rendering_instance_with_options_async(request, runtime)

    def describe_rendering_instance_configuration_with_options(
        self,
        tmp_req: main_models.DescribeRenderingInstanceConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRenderingInstanceConfigurationResponse:
        tmp_req.validate()
        request = main_models.DescribeRenderingInstanceConfigurationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.configuration):
            request.configuration_shrink = Utils.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRenderingInstanceConfiguration',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRenderingInstanceConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rendering_instance_configuration_with_options_async(
        self,
        tmp_req: main_models.DescribeRenderingInstanceConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRenderingInstanceConfigurationResponse:
        tmp_req.validate()
        request = main_models.DescribeRenderingInstanceConfigurationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.configuration):
            request.configuration_shrink = Utils.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRenderingInstanceConfiguration',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRenderingInstanceConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rendering_instance_configuration(
        self,
        request: main_models.DescribeRenderingInstanceConfigurationRequest,
    ) -> main_models.DescribeRenderingInstanceConfigurationResponse:
        runtime = RuntimeOptions()
        return self.describe_rendering_instance_configuration_with_options(request, runtime)

    async def describe_rendering_instance_configuration_async(
        self,
        request: main_models.DescribeRenderingInstanceConfigurationRequest,
    ) -> main_models.DescribeRenderingInstanceConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.describe_rendering_instance_configuration_with_options_async(request, runtime)

    def describe_rendering_instance_settings_with_options(
        self,
        tmp_req: main_models.DescribeRenderingInstanceSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRenderingInstanceSettingsResponse:
        tmp_req.validate()
        request = main_models.DescribeRenderingInstanceSettingsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attribute_names):
            request.attribute_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.attribute_names, 'AttributeNames', 'json')
        query = {}
        if not DaraCore.is_null(request.attribute_names_shrink):
            query['AttributeNames'] = request.attribute_names_shrink
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRenderingInstanceSettings',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRenderingInstanceSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rendering_instance_settings_with_options_async(
        self,
        tmp_req: main_models.DescribeRenderingInstanceSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRenderingInstanceSettingsResponse:
        tmp_req.validate()
        request = main_models.DescribeRenderingInstanceSettingsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attribute_names):
            request.attribute_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.attribute_names, 'AttributeNames', 'json')
        query = {}
        if not DaraCore.is_null(request.attribute_names_shrink):
            query['AttributeNames'] = request.attribute_names_shrink
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRenderingInstanceSettings',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRenderingInstanceSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rendering_instance_settings(
        self,
        request: main_models.DescribeRenderingInstanceSettingsRequest,
    ) -> main_models.DescribeRenderingInstanceSettingsResponse:
        runtime = RuntimeOptions()
        return self.describe_rendering_instance_settings_with_options(request, runtime)

    async def describe_rendering_instance_settings_async(
        self,
        request: main_models.DescribeRenderingInstanceSettingsRequest,
    ) -> main_models.DescribeRenderingInstanceSettingsResponse:
        runtime = RuntimeOptions()
        return await self.describe_rendering_instance_settings_with_options_async(request, runtime)

    def describe_rendering_session_with_options(
        self,
        request: main_models.DescribeRenderingSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRenderingSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRenderingSession',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRenderingSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rendering_session_with_options_async(
        self,
        request: main_models.DescribeRenderingSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRenderingSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRenderingSession',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRenderingSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rendering_session(
        self,
        request: main_models.DescribeRenderingSessionRequest,
    ) -> main_models.DescribeRenderingSessionResponse:
        runtime = RuntimeOptions()
        return self.describe_rendering_session_with_options(request, runtime)

    async def describe_rendering_session_async(
        self,
        request: main_models.DescribeRenderingSessionRequest,
    ) -> main_models.DescribeRenderingSessionResponse:
        runtime = RuntimeOptions()
        return await self.describe_rendering_session_with_options_async(request, runtime)

    def describe_stream_with_options(
        self,
        request: main_models.DescribeStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_stream_with_options_async(
        self,
        request: main_models.DescribeStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_stream(
        self,
        request: main_models.DescribeStreamRequest,
    ) -> main_models.DescribeStreamResponse:
        runtime = RuntimeOptions()
        return self.describe_stream_with_options(request, runtime)

    async def describe_stream_async(
        self,
        request: main_models.DescribeStreamRequest,
    ) -> main_models.DescribeStreamResponse:
        runtime = RuntimeOptions()
        return await self.describe_stream_with_options_async(request, runtime)

    def describe_stream_urlwith_options(
        self,
        request: main_models.DescribeStreamURLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStreamURLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth):
            query['Auth'] = request.auth
        if not DaraCore.is_null(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.expire):
            query['Expire'] = request.expire
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.transcode):
            query['Transcode'] = request.transcode
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStreamURL',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStreamURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_stream_urlwith_options_async(
        self,
        request: main_models.DescribeStreamURLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStreamURLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth):
            query['Auth'] = request.auth
        if not DaraCore.is_null(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.expire):
            query['Expire'] = request.expire
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.transcode):
            query['Transcode'] = request.transcode
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStreamURL',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStreamURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_stream_url(
        self,
        request: main_models.DescribeStreamURLRequest,
    ) -> main_models.DescribeStreamURLResponse:
        runtime = RuntimeOptions()
        return self.describe_stream_urlwith_options(request, runtime)

    async def describe_stream_url_async(
        self,
        request: main_models.DescribeStreamURLRequest,
    ) -> main_models.DescribeStreamURLResponse:
        runtime = RuntimeOptions()
        return await self.describe_stream_urlwith_options_async(request, runtime)

    def describe_stream_vod_list_with_options(
        self,
        request: main_models.DescribeStreamVodListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStreamVodListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStreamVodList',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStreamVodListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_stream_vod_list_with_options_async(
        self,
        request: main_models.DescribeStreamVodListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStreamVodListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStreamVodList',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStreamVodListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_stream_vod_list(
        self,
        request: main_models.DescribeStreamVodListRequest,
    ) -> main_models.DescribeStreamVodListResponse:
        runtime = RuntimeOptions()
        return self.describe_stream_vod_list_with_options(request, runtime)

    async def describe_stream_vod_list_async(
        self,
        request: main_models.DescribeStreamVodListRequest,
    ) -> main_models.DescribeStreamVodListResponse:
        runtime = RuntimeOptions()
        return await self.describe_stream_vod_list_with_options_async(request, runtime)

    def describe_streams_with_options(
        self,
        request: main_models.DescribeStreamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStreamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app):
            query['App'] = request.app
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStreams',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStreamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_streams_with_options_async(
        self,
        request: main_models.DescribeStreamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStreamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app):
            query['App'] = request.app
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStreams',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStreamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_streams(
        self,
        request: main_models.DescribeStreamsRequest,
    ) -> main_models.DescribeStreamsResponse:
        runtime = RuntimeOptions()
        return self.describe_streams_with_options(request, runtime)

    async def describe_streams_async(
        self,
        request: main_models.DescribeStreamsRequest,
    ) -> main_models.DescribeStreamsResponse:
        runtime = RuntimeOptions()
        return await self.describe_streams_with_options_async(request, runtime)

    def describe_template_with_options(
        self,
        request: main_models.DescribeTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_template_with_options_async(
        self,
        request: main_models.DescribeTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_template(
        self,
        request: main_models.DescribeTemplateRequest,
    ) -> main_models.DescribeTemplateResponse:
        runtime = RuntimeOptions()
        return self.describe_template_with_options(request, runtime)

    async def describe_template_async(
        self,
        request: main_models.DescribeTemplateRequest,
    ) -> main_models.DescribeTemplateResponse:
        runtime = RuntimeOptions()
        return await self.describe_template_with_options_async(request, runtime)

    def describe_templates_with_options(
        self,
        request: main_models.DescribeTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplates',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_templates_with_options_async(
        self,
        request: main_models.DescribeTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplates',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_templates(
        self,
        request: main_models.DescribeTemplatesRequest,
    ) -> main_models.DescribeTemplatesResponse:
        runtime = RuntimeOptions()
        return self.describe_templates_with_options(request, runtime)

    async def describe_templates_async(
        self,
        request: main_models.DescribeTemplatesRequest,
    ) -> main_models.DescribeTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.describe_templates_with_options_async(request, runtime)

    def describe_vod_stream_urlwith_options(
        self,
        request: main_models.DescribeVodStreamURLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodStreamURLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodStreamURL',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodStreamURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_stream_urlwith_options_async(
        self,
        request: main_models.DescribeVodStreamURLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVodStreamURLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVodStreamURL',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVodStreamURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_stream_url(
        self,
        request: main_models.DescribeVodStreamURLRequest,
    ) -> main_models.DescribeVodStreamURLResponse:
        runtime = RuntimeOptions()
        return self.describe_vod_stream_urlwith_options(request, runtime)

    async def describe_vod_stream_url_async(
        self,
        request: main_models.DescribeVodStreamURLRequest,
    ) -> main_models.DescribeVodStreamURLResponse:
        runtime = RuntimeOptions()
        return await self.describe_vod_stream_urlwith_options_async(request, runtime)

    def describe_vs_certificate_detail_with_options(
        self,
        request: main_models.DescribeVsCertificateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsCertificateDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsCertificateDetail',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_certificate_detail_with_options_async(
        self,
        request: main_models.DescribeVsCertificateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsCertificateDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsCertificateDetail',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsCertificateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_certificate_detail(
        self,
        request: main_models.DescribeVsCertificateDetailRequest,
    ) -> main_models.DescribeVsCertificateDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_certificate_detail_with_options(request, runtime)

    async def describe_vs_certificate_detail_async(
        self,
        request: main_models.DescribeVsCertificateDetailRequest,
    ) -> main_models.DescribeVsCertificateDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_certificate_detail_with_options_async(request, runtime)

    def describe_vs_certificate_list_with_options(
        self,
        request: main_models.DescribeVsCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsCertificateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsCertificateList',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_certificate_list_with_options_async(
        self,
        request: main_models.DescribeVsCertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsCertificateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsCertificateList',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_certificate_list(
        self,
        request: main_models.DescribeVsCertificateListRequest,
    ) -> main_models.DescribeVsCertificateListResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_certificate_list_with_options(request, runtime)

    async def describe_vs_certificate_list_async(
        self,
        request: main_models.DescribeVsCertificateListRequest,
    ) -> main_models.DescribeVsCertificateListResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_certificate_list_with_options_async(request, runtime)

    def describe_vs_devices_data_with_options(
        self,
        request: main_models.DescribeVsDevicesDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDevicesDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDevicesData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDevicesDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_devices_data_with_options_async(
        self,
        request: main_models.DescribeVsDevicesDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDevicesDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDevicesData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDevicesDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_devices_data(
        self,
        request: main_models.DescribeVsDevicesDataRequest,
    ) -> main_models.DescribeVsDevicesDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_devices_data_with_options(request, runtime)

    async def describe_vs_devices_data_async(
        self,
        request: main_models.DescribeVsDevicesDataRequest,
    ) -> main_models.DescribeVsDevicesDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_devices_data_with_options_async(request, runtime)

    def describe_vs_domain_bps_data_with_options(
        self,
        request: main_models.DescribeVsDomainBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainBpsData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_bps_data_with_options_async(
        self,
        request: main_models.DescribeVsDomainBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainBpsData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_bps_data(
        self,
        request: main_models.DescribeVsDomainBpsDataRequest,
    ) -> main_models.DescribeVsDomainBpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_domain_bps_data_with_options(request, runtime)

    async def describe_vs_domain_bps_data_async(
        self,
        request: main_models.DescribeVsDomainBpsDataRequest,
    ) -> main_models.DescribeVsDomainBpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_domain_bps_data_with_options_async(request, runtime)

    def describe_vs_domain_certificate_info_with_options(
        self,
        request: main_models.DescribeVsDomainCertificateInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainCertificateInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainCertificateInfo',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainCertificateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_certificate_info_with_options_async(
        self,
        request: main_models.DescribeVsDomainCertificateInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainCertificateInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainCertificateInfo',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainCertificateInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_certificate_info(
        self,
        request: main_models.DescribeVsDomainCertificateInfoRequest,
    ) -> main_models.DescribeVsDomainCertificateInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_domain_certificate_info_with_options(request, runtime)

    async def describe_vs_domain_certificate_info_async(
        self,
        request: main_models.DescribeVsDomainCertificateInfoRequest,
    ) -> main_models.DescribeVsDomainCertificateInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_domain_certificate_info_with_options_async(request, runtime)

    def describe_vs_domain_configs_with_options(
        self,
        request: main_models.DescribeVsDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_names):
            query['FunctionNames'] = request.function_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainConfigs',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_configs_with_options_async(
        self,
        request: main_models.DescribeVsDomainConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.function_names):
            query['FunctionNames'] = request.function_names
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainConfigs',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_configs(
        self,
        request: main_models.DescribeVsDomainConfigsRequest,
    ) -> main_models.DescribeVsDomainConfigsResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_domain_configs_with_options(request, runtime)

    async def describe_vs_domain_configs_async(
        self,
        request: main_models.DescribeVsDomainConfigsRequest,
    ) -> main_models.DescribeVsDomainConfigsResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_domain_configs_with_options_async(request, runtime)

    def describe_vs_domain_detail_with_options(
        self,
        request: main_models.DescribeVsDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainDetail',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_detail_with_options_async(
        self,
        request: main_models.DescribeVsDomainDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainDetail',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_detail(
        self,
        request: main_models.DescribeVsDomainDetailRequest,
    ) -> main_models.DescribeVsDomainDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_domain_detail_with_options(request, runtime)

    async def describe_vs_domain_detail_async(
        self,
        request: main_models.DescribeVsDomainDetailRequest,
    ) -> main_models.DescribeVsDomainDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_domain_detail_with_options_async(request, runtime)

    def describe_vs_domain_pv_data_with_options(
        self,
        request: main_models.DescribeVsDomainPvDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainPvDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainPvData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainPvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_pv_data_with_options_async(
        self,
        request: main_models.DescribeVsDomainPvDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainPvDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainPvData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainPvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_pv_data(
        self,
        request: main_models.DescribeVsDomainPvDataRequest,
    ) -> main_models.DescribeVsDomainPvDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_domain_pv_data_with_options(request, runtime)

    async def describe_vs_domain_pv_data_async(
        self,
        request: main_models.DescribeVsDomainPvDataRequest,
    ) -> main_models.DescribeVsDomainPvDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_domain_pv_data_with_options_async(request, runtime)

    def describe_vs_domain_pv_uv_data_with_options(
        self,
        request: main_models.DescribeVsDomainPvUvDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainPvUvDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainPvUvData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainPvUvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_pv_uv_data_with_options_async(
        self,
        request: main_models.DescribeVsDomainPvUvDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainPvUvDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainPvUvData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainPvUvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_pv_uv_data(
        self,
        request: main_models.DescribeVsDomainPvUvDataRequest,
    ) -> main_models.DescribeVsDomainPvUvDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_domain_pv_uv_data_with_options(request, runtime)

    async def describe_vs_domain_pv_uv_data_async(
        self,
        request: main_models.DescribeVsDomainPvUvDataRequest,
    ) -> main_models.DescribeVsDomainPvUvDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_domain_pv_uv_data_with_options_async(request, runtime)

    def describe_vs_domain_record_data_with_options(
        self,
        request: main_models.DescribeVsDomainRecordDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainRecordDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainRecordData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainRecordDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_record_data_with_options_async(
        self,
        request: main_models.DescribeVsDomainRecordDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainRecordDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainRecordData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainRecordDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_record_data(
        self,
        request: main_models.DescribeVsDomainRecordDataRequest,
    ) -> main_models.DescribeVsDomainRecordDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_domain_record_data_with_options(request, runtime)

    async def describe_vs_domain_record_data_async(
        self,
        request: main_models.DescribeVsDomainRecordDataRequest,
    ) -> main_models.DescribeVsDomainRecordDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_domain_record_data_with_options_async(request, runtime)

    def describe_vs_domain_region_data_with_options(
        self,
        request: main_models.DescribeVsDomainRegionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainRegionDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainRegionData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainRegionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_region_data_with_options_async(
        self,
        request: main_models.DescribeVsDomainRegionDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainRegionDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainRegionData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainRegionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_region_data(
        self,
        request: main_models.DescribeVsDomainRegionDataRequest,
    ) -> main_models.DescribeVsDomainRegionDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_domain_region_data_with_options(request, runtime)

    async def describe_vs_domain_region_data_async(
        self,
        request: main_models.DescribeVsDomainRegionDataRequest,
    ) -> main_models.DescribeVsDomainRegionDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_domain_region_data_with_options_async(request, runtime)

    def describe_vs_domain_req_bps_data_with_options(
        self,
        request: main_models.DescribeVsDomainReqBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainReqBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainReqBpsData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainReqBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_req_bps_data_with_options_async(
        self,
        request: main_models.DescribeVsDomainReqBpsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainReqBpsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainReqBpsData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainReqBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_req_bps_data(
        self,
        request: main_models.DescribeVsDomainReqBpsDataRequest,
    ) -> main_models.DescribeVsDomainReqBpsDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_domain_req_bps_data_with_options(request, runtime)

    async def describe_vs_domain_req_bps_data_async(
        self,
        request: main_models.DescribeVsDomainReqBpsDataRequest,
    ) -> main_models.DescribeVsDomainReqBpsDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_domain_req_bps_data_with_options_async(request, runtime)

    def describe_vs_domain_req_traffic_data_with_options(
        self,
        request: main_models.DescribeVsDomainReqTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainReqTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainReqTrafficData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainReqTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_req_traffic_data_with_options_async(
        self,
        request: main_models.DescribeVsDomainReqTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainReqTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainReqTrafficData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainReqTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_req_traffic_data(
        self,
        request: main_models.DescribeVsDomainReqTrafficDataRequest,
    ) -> main_models.DescribeVsDomainReqTrafficDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_domain_req_traffic_data_with_options(request, runtime)

    async def describe_vs_domain_req_traffic_data_async(
        self,
        request: main_models.DescribeVsDomainReqTrafficDataRequest,
    ) -> main_models.DescribeVsDomainReqTrafficDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_domain_req_traffic_data_with_options_async(request, runtime)

    def describe_vs_domain_snapshot_data_with_options(
        self,
        request: main_models.DescribeVsDomainSnapshotDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainSnapshotDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainSnapshotData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainSnapshotDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_snapshot_data_with_options_async(
        self,
        request: main_models.DescribeVsDomainSnapshotDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainSnapshotDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainSnapshotData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainSnapshotDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_snapshot_data(
        self,
        request: main_models.DescribeVsDomainSnapshotDataRequest,
    ) -> main_models.DescribeVsDomainSnapshotDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_domain_snapshot_data_with_options(request, runtime)

    async def describe_vs_domain_snapshot_data_async(
        self,
        request: main_models.DescribeVsDomainSnapshotDataRequest,
    ) -> main_models.DescribeVsDomainSnapshotDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_domain_snapshot_data_with_options_async(request, runtime)

    def describe_vs_domain_traffic_data_with_options(
        self,
        request: main_models.DescribeVsDomainTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainTrafficData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_traffic_data_with_options_async(
        self,
        request: main_models.DescribeVsDomainTrafficDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainTrafficDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not DaraCore.is_null(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainTrafficData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_traffic_data(
        self,
        request: main_models.DescribeVsDomainTrafficDataRequest,
    ) -> main_models.DescribeVsDomainTrafficDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_domain_traffic_data_with_options(request, runtime)

    async def describe_vs_domain_traffic_data_async(
        self,
        request: main_models.DescribeVsDomainTrafficDataRequest,
    ) -> main_models.DescribeVsDomainTrafficDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_domain_traffic_data_with_options_async(request, runtime)

    def describe_vs_domain_uv_data_with_options(
        self,
        request: main_models.DescribeVsDomainUvDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainUvDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainUvData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainUvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_uv_data_with_options_async(
        self,
        request: main_models.DescribeVsDomainUvDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsDomainUvDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsDomainUvData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsDomainUvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_uv_data(
        self,
        request: main_models.DescribeVsDomainUvDataRequest,
    ) -> main_models.DescribeVsDomainUvDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_domain_uv_data_with_options(request, runtime)

    async def describe_vs_domain_uv_data_async(
        self,
        request: main_models.DescribeVsDomainUvDataRequest,
    ) -> main_models.DescribeVsDomainUvDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_domain_uv_data_with_options_async(request, runtime)

    def describe_vs_pull_stream_info_config_with_options(
        self,
        request: main_models.DescribeVsPullStreamInfoConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsPullStreamInfoConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsPullStreamInfoConfig',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsPullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_pull_stream_info_config_with_options_async(
        self,
        request: main_models.DescribeVsPullStreamInfoConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsPullStreamInfoConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsPullStreamInfoConfig',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsPullStreamInfoConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_pull_stream_info_config(
        self,
        request: main_models.DescribeVsPullStreamInfoConfigRequest,
    ) -> main_models.DescribeVsPullStreamInfoConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_pull_stream_info_config_with_options(request, runtime)

    async def describe_vs_pull_stream_info_config_async(
        self,
        request: main_models.DescribeVsPullStreamInfoConfigRequest,
    ) -> main_models.DescribeVsPullStreamInfoConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_pull_stream_info_config_with_options_async(request, runtime)

    def describe_vs_streams_notify_url_config_with_options(
        self,
        request: main_models.DescribeVsStreamsNotifyUrlConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsStreamsNotifyUrlConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsStreamsNotifyUrlConfig',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsStreamsNotifyUrlConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_streams_notify_url_config_with_options_async(
        self,
        request: main_models.DescribeVsStreamsNotifyUrlConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsStreamsNotifyUrlConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsStreamsNotifyUrlConfig',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsStreamsNotifyUrlConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_streams_notify_url_config(
        self,
        request: main_models.DescribeVsStreamsNotifyUrlConfigRequest,
    ) -> main_models.DescribeVsStreamsNotifyUrlConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_streams_notify_url_config_with_options(request, runtime)

    async def describe_vs_streams_notify_url_config_async(
        self,
        request: main_models.DescribeVsStreamsNotifyUrlConfigRequest,
    ) -> main_models.DescribeVsStreamsNotifyUrlConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_streams_notify_url_config_with_options_async(request, runtime)

    def describe_vs_streams_online_list_with_options(
        self,
        request: main_models.DescribeVsStreamsOnlineListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsStreamsOnlineListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.stream_name):
            query['StreamName'] = request.stream_name
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsStreamsOnlineList',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsStreamsOnlineListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_streams_online_list_with_options_async(
        self,
        request: main_models.DescribeVsStreamsOnlineListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsStreamsOnlineListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.stream_name):
            query['StreamName'] = request.stream_name
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsStreamsOnlineList',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsStreamsOnlineListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_streams_online_list(
        self,
        request: main_models.DescribeVsStreamsOnlineListRequest,
    ) -> main_models.DescribeVsStreamsOnlineListResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_streams_online_list_with_options(request, runtime)

    async def describe_vs_streams_online_list_async(
        self,
        request: main_models.DescribeVsStreamsOnlineListRequest,
    ) -> main_models.DescribeVsStreamsOnlineListResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_streams_online_list_with_options_async(request, runtime)

    def describe_vs_streams_publish_list_with_options(
        self,
        request: main_models.DescribeVsStreamsPublishListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsStreamsPublishListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.stream_name):
            query['StreamName'] = request.stream_name
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsStreamsPublishList',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsStreamsPublishListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_streams_publish_list_with_options_async(
        self,
        request: main_models.DescribeVsStreamsPublishListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsStreamsPublishListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.stream_name):
            query['StreamName'] = request.stream_name
        if not DaraCore.is_null(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsStreamsPublishList',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsStreamsPublishListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_streams_publish_list(
        self,
        request: main_models.DescribeVsStreamsPublishListRequest,
    ) -> main_models.DescribeVsStreamsPublishListResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_streams_publish_list_with_options(request, runtime)

    async def describe_vs_streams_publish_list_async(
        self,
        request: main_models.DescribeVsStreamsPublishListRequest,
    ) -> main_models.DescribeVsStreamsPublishListResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_streams_publish_list_with_options_async(request, runtime)

    def describe_vs_top_domains_by_flow_with_options(
        self,
        request: main_models.DescribeVsTopDomainsByFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsTopDomainsByFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsTopDomainsByFlow',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsTopDomainsByFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_top_domains_by_flow_with_options_async(
        self,
        request: main_models.DescribeVsTopDomainsByFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsTopDomainsByFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsTopDomainsByFlow',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsTopDomainsByFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_top_domains_by_flow(
        self,
        request: main_models.DescribeVsTopDomainsByFlowRequest,
    ) -> main_models.DescribeVsTopDomainsByFlowResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_top_domains_by_flow_with_options(request, runtime)

    async def describe_vs_top_domains_by_flow_async(
        self,
        request: main_models.DescribeVsTopDomainsByFlowRequest,
    ) -> main_models.DescribeVsTopDomainsByFlowResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_top_domains_by_flow_with_options_async(request, runtime)

    def describe_vs_up_peak_publish_stream_data_with_options(
        self,
        request: main_models.DescribeVsUpPeakPublishStreamDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsUpPeakPublishStreamDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_switch):
            query['DomainSwitch'] = request.domain_switch
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsUpPeakPublishStreamData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsUpPeakPublishStreamDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_up_peak_publish_stream_data_with_options_async(
        self,
        request: main_models.DescribeVsUpPeakPublishStreamDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsUpPeakPublishStreamDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_switch):
            query['DomainSwitch'] = request.domain_switch
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsUpPeakPublishStreamData',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsUpPeakPublishStreamDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_up_peak_publish_stream_data(
        self,
        request: main_models.DescribeVsUpPeakPublishStreamDataRequest,
    ) -> main_models.DescribeVsUpPeakPublishStreamDataResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_up_peak_publish_stream_data_with_options(request, runtime)

    async def describe_vs_up_peak_publish_stream_data_async(
        self,
        request: main_models.DescribeVsUpPeakPublishStreamDataRequest,
    ) -> main_models.DescribeVsUpPeakPublishStreamDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_up_peak_publish_stream_data_with_options_async(request, runtime)

    def describe_vs_user_resource_package_with_options(
        self,
        request: main_models.DescribeVsUserResourcePackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsUserResourcePackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsUserResourcePackage',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsUserResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_user_resource_package_with_options_async(
        self,
        request: main_models.DescribeVsUserResourcePackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsUserResourcePackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsUserResourcePackage',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsUserResourcePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_user_resource_package(
        self,
        request: main_models.DescribeVsUserResourcePackageRequest,
    ) -> main_models.DescribeVsUserResourcePackageResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_user_resource_package_with_options(request, runtime)

    async def describe_vs_user_resource_package_async(
        self,
        request: main_models.DescribeVsUserResourcePackageRequest,
    ) -> main_models.DescribeVsUserResourcePackageResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_user_resource_package_with_options_async(request, runtime)

    def describe_vs_verify_content_with_options(
        self,
        request: main_models.DescribeVsVerifyContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsVerifyContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsVerifyContent',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsVerifyContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_verify_content_with_options_async(
        self,
        request: main_models.DescribeVsVerifyContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVsVerifyContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsVerifyContent',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVsVerifyContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_verify_content(
        self,
        request: main_models.DescribeVsVerifyContentRequest,
    ) -> main_models.DescribeVsVerifyContentResponse:
        runtime = RuntimeOptions()
        return self.describe_vs_verify_content_with_options(request, runtime)

    async def describe_vs_verify_content_async(
        self,
        request: main_models.DescribeVsVerifyContentRequest,
    ) -> main_models.DescribeVsVerifyContentResponse:
        runtime = RuntimeOptions()
        return await self.describe_vs_verify_content_with_options_async(request, runtime)

    def disassociate_rendering_project_instances_with_options(
        self,
        tmp_req: main_models.DisassociateRenderingProjectInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateRenderingProjectInstancesResponse:
        tmp_req.validate()
        request = main_models.DisassociateRenderingProjectInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateRenderingProjectInstances',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateRenderingProjectInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_rendering_project_instances_with_options_async(
        self,
        tmp_req: main_models.DisassociateRenderingProjectInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateRenderingProjectInstancesResponse:
        tmp_req.validate()
        request = main_models.DisassociateRenderingProjectInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateRenderingProjectInstances',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateRenderingProjectInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_rendering_project_instances(
        self,
        request: main_models.DisassociateRenderingProjectInstancesRequest,
    ) -> main_models.DisassociateRenderingProjectInstancesResponse:
        runtime = RuntimeOptions()
        return self.disassociate_rendering_project_instances_with_options(request, runtime)

    async def disassociate_rendering_project_instances_async(
        self,
        request: main_models.DisassociateRenderingProjectInstancesRequest,
    ) -> main_models.DisassociateRenderingProjectInstancesResponse:
        runtime = RuntimeOptions()
        return await self.disassociate_rendering_project_instances_with_options_async(request, runtime)

    def forbid_vs_stream_with_options(
        self,
        request: main_models.ForbidVsStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ForbidVsStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not DaraCore.is_null(request.oneshot):
            query['Oneshot'] = request.oneshot
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resume_time):
            query['ResumeTime'] = request.resume_time
        if not DaraCore.is_null(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ForbidVsStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ForbidVsStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def forbid_vs_stream_with_options_async(
        self,
        request: main_models.ForbidVsStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ForbidVsStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not DaraCore.is_null(request.oneshot):
            query['Oneshot'] = request.oneshot
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resume_time):
            query['ResumeTime'] = request.resume_time
        if not DaraCore.is_null(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ForbidVsStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ForbidVsStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def forbid_vs_stream(
        self,
        request: main_models.ForbidVsStreamRequest,
    ) -> main_models.ForbidVsStreamResponse:
        runtime = RuntimeOptions()
        return self.forbid_vs_stream_with_options(request, runtime)

    async def forbid_vs_stream_async(
        self,
        request: main_models.ForbidVsStreamRequest,
    ) -> main_models.ForbidVsStreamResponse:
        runtime = RuntimeOptions()
        return await self.forbid_vs_stream_with_options_async(request, runtime)

    def get_rendering_instance_commands_status_with_options(
        self,
        request: main_models.GetRenderingInstanceCommandsStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRenderingInstanceCommandsStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cmd_id):
            query['CmdId'] = request.cmd_id
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRenderingInstanceCommandsStatus',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRenderingInstanceCommandsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rendering_instance_commands_status_with_options_async(
        self,
        request: main_models.GetRenderingInstanceCommandsStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRenderingInstanceCommandsStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cmd_id):
            query['CmdId'] = request.cmd_id
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRenderingInstanceCommandsStatus',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRenderingInstanceCommandsStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rendering_instance_commands_status(
        self,
        request: main_models.GetRenderingInstanceCommandsStatusRequest,
    ) -> main_models.GetRenderingInstanceCommandsStatusResponse:
        runtime = RuntimeOptions()
        return self.get_rendering_instance_commands_status_with_options(request, runtime)

    async def get_rendering_instance_commands_status_async(
        self,
        request: main_models.GetRenderingInstanceCommandsStatusRequest,
    ) -> main_models.GetRenderingInstanceCommandsStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_rendering_instance_commands_status_with_options_async(request, runtime)

    def get_rendering_instance_streaming_info_with_options(
        self,
        request: main_models.GetRenderingInstanceStreamingInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRenderingInstanceStreamingInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRenderingInstanceStreamingInfo',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRenderingInstanceStreamingInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rendering_instance_streaming_info_with_options_async(
        self,
        request: main_models.GetRenderingInstanceStreamingInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRenderingInstanceStreamingInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRenderingInstanceStreamingInfo',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRenderingInstanceStreamingInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rendering_instance_streaming_info(
        self,
        request: main_models.GetRenderingInstanceStreamingInfoRequest,
    ) -> main_models.GetRenderingInstanceStreamingInfoResponse:
        runtime = RuntimeOptions()
        return self.get_rendering_instance_streaming_info_with_options(request, runtime)

    async def get_rendering_instance_streaming_info_async(
        self,
        request: main_models.GetRenderingInstanceStreamingInfoRequest,
    ) -> main_models.GetRenderingInstanceStreamingInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_rendering_instance_streaming_info_with_options_async(request, runtime)

    def get_rendering_project_instance_state_metrics_with_options(
        self,
        request: main_models.GetRenderingProjectInstanceStateMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRenderingProjectInstanceStateMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRenderingProjectInstanceStateMetrics',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRenderingProjectInstanceStateMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rendering_project_instance_state_metrics_with_options_async(
        self,
        request: main_models.GetRenderingProjectInstanceStateMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRenderingProjectInstanceStateMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRenderingProjectInstanceStateMetrics',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRenderingProjectInstanceStateMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rendering_project_instance_state_metrics(
        self,
        request: main_models.GetRenderingProjectInstanceStateMetricsRequest,
    ) -> main_models.GetRenderingProjectInstanceStateMetricsResponse:
        runtime = RuntimeOptions()
        return self.get_rendering_project_instance_state_metrics_with_options(request, runtime)

    async def get_rendering_project_instance_state_metrics_async(
        self,
        request: main_models.GetRenderingProjectInstanceStateMetricsRequest,
    ) -> main_models.GetRenderingProjectInstanceStateMetricsResponse:
        runtime = RuntimeOptions()
        return await self.get_rendering_project_instance_state_metrics_with_options_async(request, runtime)

    def goto_preset_with_options(
        self,
        request: main_models.GotoPresetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GotoPresetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preset_id):
            query['PresetId'] = request.preset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GotoPreset',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GotoPresetResponse(),
            self.call_api(params, req, runtime)
        )

    async def goto_preset_with_options_async(
        self,
        request: main_models.GotoPresetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GotoPresetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preset_id):
            query['PresetId'] = request.preset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GotoPreset',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GotoPresetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def goto_preset(
        self,
        request: main_models.GotoPresetRequest,
    ) -> main_models.GotoPresetResponse:
        runtime = RuntimeOptions()
        return self.goto_preset_with_options(request, runtime)

    async def goto_preset_async(
        self,
        request: main_models.GotoPresetRequest,
    ) -> main_models.GotoPresetResponse:
        runtime = RuntimeOptions()
        return await self.goto_preset_with_options_async(request, runtime)

    def install_cloud_app_with_options(
        self,
        tmp_req: main_models.InstallCloudAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallCloudAppResponse:
        tmp_req.validate()
        request = main_models.InstallCloudAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.patch_id):
            query['PatchId'] = request.patch_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not DaraCore.is_null(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallCloudApp',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallCloudAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_cloud_app_with_options_async(
        self,
        tmp_req: main_models.InstallCloudAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallCloudAppResponse:
        tmp_req.validate()
        request = main_models.InstallCloudAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.patch_id):
            query['PatchId'] = request.patch_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not DaraCore.is_null(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallCloudApp',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallCloudAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_cloud_app(
        self,
        request: main_models.InstallCloudAppRequest,
    ) -> main_models.InstallCloudAppResponse:
        runtime = RuntimeOptions()
        return self.install_cloud_app_with_options(request, runtime)

    async def install_cloud_app_async(
        self,
        request: main_models.InstallCloudAppRequest,
    ) -> main_models.InstallCloudAppResponse:
        runtime = RuntimeOptions()
        return await self.install_cloud_app_with_options_async(request, runtime)

    def list_cloud_app_installations_with_options(
        self,
        request: main_models.ListCloudAppInstallationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudAppInstallationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudAppInstallations',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudAppInstallationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_app_installations_with_options_async(
        self,
        request: main_models.ListCloudAppInstallationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudAppInstallationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudAppInstallations',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudAppInstallationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_app_installations(
        self,
        request: main_models.ListCloudAppInstallationsRequest,
    ) -> main_models.ListCloudAppInstallationsResponse:
        runtime = RuntimeOptions()
        return self.list_cloud_app_installations_with_options(request, runtime)

    async def list_cloud_app_installations_async(
        self,
        request: main_models.ListCloudAppInstallationsRequest,
    ) -> main_models.ListCloudAppInstallationsResponse:
        runtime = RuntimeOptions()
        return await self.list_cloud_app_installations_with_options_async(request, runtime)

    def list_cloud_app_patches_with_options(
        self,
        request: main_models.ListCloudAppPatchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudAppPatchesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.patch_id):
            query['PatchId'] = request.patch_id
        if not DaraCore.is_null(request.patch_name):
            query['PatchName'] = request.patch_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudAppPatches',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudAppPatchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_app_patches_with_options_async(
        self,
        request: main_models.ListCloudAppPatchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudAppPatchesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.patch_id):
            query['PatchId'] = request.patch_id
        if not DaraCore.is_null(request.patch_name):
            query['PatchName'] = request.patch_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudAppPatches',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudAppPatchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_app_patches(
        self,
        request: main_models.ListCloudAppPatchesRequest,
    ) -> main_models.ListCloudAppPatchesResponse:
        runtime = RuntimeOptions()
        return self.list_cloud_app_patches_with_options(request, runtime)

    async def list_cloud_app_patches_async(
        self,
        request: main_models.ListCloudAppPatchesRequest,
    ) -> main_models.ListCloudAppPatchesResponse:
        runtime = RuntimeOptions()
        return await self.list_cloud_app_patches_with_options_async(request, runtime)

    def list_cloud_apps_with_options(
        self,
        request: main_models.ListCloudAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudAppsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudApps',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_apps_with_options_async(
        self,
        request: main_models.ListCloudAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudAppsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudApps',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_apps(
        self,
        request: main_models.ListCloudAppsRequest,
    ) -> main_models.ListCloudAppsResponse:
        runtime = RuntimeOptions()
        return self.list_cloud_apps_with_options(request, runtime)

    async def list_cloud_apps_async(
        self,
        request: main_models.ListCloudAppsRequest,
    ) -> main_models.ListCloudAppsResponse:
        runtime = RuntimeOptions()
        return await self.list_cloud_apps_with_options_async(request, runtime)

    def list_file_push_statuses_with_options(
        self,
        request: main_models.ListFilePushStatusesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFilePushStatusesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFilePushStatuses',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFilePushStatusesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_file_push_statuses_with_options_async(
        self,
        request: main_models.ListFilePushStatusesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFilePushStatusesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFilePushStatuses',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFilePushStatusesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_file_push_statuses(
        self,
        request: main_models.ListFilePushStatusesRequest,
    ) -> main_models.ListFilePushStatusesResponse:
        runtime = RuntimeOptions()
        return self.list_file_push_statuses_with_options(request, runtime)

    async def list_file_push_statuses_async(
        self,
        request: main_models.ListFilePushStatusesRequest,
    ) -> main_models.ListFilePushStatusesResponse:
        runtime = RuntimeOptions()
        return await self.list_file_push_statuses_with_options_async(request, runtime)

    def list_files_with_options(
        self,
        request: main_models.ListFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFilesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFiles',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_files_with_options_async(
        self,
        request: main_models.ListFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFilesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFiles',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_files(
        self,
        request: main_models.ListFilesRequest,
    ) -> main_models.ListFilesResponse:
        runtime = RuntimeOptions()
        return self.list_files_with_options(request, runtime)

    async def list_files_async(
        self,
        request: main_models.ListFilesRequest,
    ) -> main_models.ListFilesResponse:
        runtime = RuntimeOptions()
        return await self.list_files_with_options_async(request, runtime)

    def list_public_keys_with_options(
        self,
        request: main_models.ListPublicKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPublicKeysResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPublicKeys',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPublicKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_public_keys_with_options_async(
        self,
        request: main_models.ListPublicKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPublicKeysResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPublicKeys',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPublicKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_public_keys(
        self,
        request: main_models.ListPublicKeysRequest,
    ) -> main_models.ListPublicKeysResponse:
        runtime = RuntimeOptions()
        return self.list_public_keys_with_options(request, runtime)

    async def list_public_keys_async(
        self,
        request: main_models.ListPublicKeysRequest,
    ) -> main_models.ListPublicKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_public_keys_with_options_async(request, runtime)

    def list_rendering_data_packages_with_options(
        self,
        request: main_models.ListRenderingDataPackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRenderingDataPackagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.data_package_id):
            query['DataPackageId'] = request.data_package_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRenderingDataPackages',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRenderingDataPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rendering_data_packages_with_options_async(
        self,
        request: main_models.ListRenderingDataPackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRenderingDataPackagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.data_package_id):
            query['DataPackageId'] = request.data_package_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRenderingDataPackages',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRenderingDataPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rendering_data_packages(
        self,
        request: main_models.ListRenderingDataPackagesRequest,
    ) -> main_models.ListRenderingDataPackagesResponse:
        runtime = RuntimeOptions()
        return self.list_rendering_data_packages_with_options(request, runtime)

    async def list_rendering_data_packages_async(
        self,
        request: main_models.ListRenderingDataPackagesRequest,
    ) -> main_models.ListRenderingDataPackagesResponse:
        runtime = RuntimeOptions()
        return await self.list_rendering_data_packages_with_options_async(request, runtime)

    def list_rendering_instance_gateway_with_options(
        self,
        request: main_models.ListRenderingInstanceGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRenderingInstanceGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.gateway_instance_id):
            query['GatewayInstanceId'] = request.gateway_instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRenderingInstanceGateway',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRenderingInstanceGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rendering_instance_gateway_with_options_async(
        self,
        request: main_models.ListRenderingInstanceGatewayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRenderingInstanceGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.gateway_instance_id):
            query['GatewayInstanceId'] = request.gateway_instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRenderingInstanceGateway',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRenderingInstanceGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rendering_instance_gateway(
        self,
        request: main_models.ListRenderingInstanceGatewayRequest,
    ) -> main_models.ListRenderingInstanceGatewayResponse:
        runtime = RuntimeOptions()
        return self.list_rendering_instance_gateway_with_options(request, runtime)

    async def list_rendering_instance_gateway_async(
        self,
        request: main_models.ListRenderingInstanceGatewayRequest,
    ) -> main_models.ListRenderingInstanceGatewayResponse:
        runtime = RuntimeOptions()
        return await self.list_rendering_instance_gateway_with_options_async(request, runtime)

    def list_rendering_instances_with_options(
        self,
        request: main_models.ListRenderingInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRenderingInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRenderingInstances',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRenderingInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rendering_instances_with_options_async(
        self,
        request: main_models.ListRenderingInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRenderingInstancesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRenderingInstances',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRenderingInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rendering_instances(
        self,
        request: main_models.ListRenderingInstancesRequest,
    ) -> main_models.ListRenderingInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_rendering_instances_with_options(request, runtime)

    async def list_rendering_instances_async(
        self,
        request: main_models.ListRenderingInstancesRequest,
    ) -> main_models.ListRenderingInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_rendering_instances_with_options_async(request, runtime)

    def list_rendering_project_instances_with_options(
        self,
        request: main_models.ListRenderingProjectInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRenderingProjectInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRenderingProjectInstances',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRenderingProjectInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rendering_project_instances_with_options_async(
        self,
        request: main_models.ListRenderingProjectInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRenderingProjectInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRenderingProjectInstances',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRenderingProjectInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rendering_project_instances(
        self,
        request: main_models.ListRenderingProjectInstancesRequest,
    ) -> main_models.ListRenderingProjectInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_rendering_project_instances_with_options(request, runtime)

    async def list_rendering_project_instances_async(
        self,
        request: main_models.ListRenderingProjectInstancesRequest,
    ) -> main_models.ListRenderingProjectInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_rendering_project_instances_with_options_async(request, runtime)

    def list_rendering_projects_with_options(
        self,
        request: main_models.ListRenderingProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRenderingProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRenderingProjects',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRenderingProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rendering_projects_with_options_async(
        self,
        request: main_models.ListRenderingProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRenderingProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRenderingProjects',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRenderingProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rendering_projects(
        self,
        request: main_models.ListRenderingProjectsRequest,
    ) -> main_models.ListRenderingProjectsResponse:
        runtime = RuntimeOptions()
        return self.list_rendering_projects_with_options(request, runtime)

    async def list_rendering_projects_async(
        self,
        request: main_models.ListRenderingProjectsRequest,
    ) -> main_models.ListRenderingProjectsResponse:
        runtime = RuntimeOptions()
        return await self.list_rendering_projects_with_options_async(request, runtime)

    def list_rendering_sessions_with_options(
        self,
        request: main_models.ListRenderingSessionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRenderingSessionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.patch_id):
            query['PatchId'] = request.patch_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRenderingSessions',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRenderingSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rendering_sessions_with_options_async(
        self,
        request: main_models.ListRenderingSessionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRenderingSessionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.patch_id):
            query['PatchId'] = request.patch_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRenderingSessions',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRenderingSessionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rendering_sessions(
        self,
        request: main_models.ListRenderingSessionsRequest,
    ) -> main_models.ListRenderingSessionsResponse:
        runtime = RuntimeOptions()
        return self.list_rendering_sessions_with_options(request, runtime)

    async def list_rendering_sessions_async(
        self,
        request: main_models.ListRenderingSessionsRequest,
    ) -> main_models.ListRenderingSessionsResponse:
        runtime = RuntimeOptions()
        return await self.list_rendering_sessions_with_options_async(request, runtime)

    def manage_login_with_options(
        self,
        request: main_models.ManageLoginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManageLoginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_name):
            query['ActionName'] = request.action_name
        if not DaraCore.is_null(request.key_group):
            query['KeyGroup'] = request.key_group
        if not DaraCore.is_null(request.key_name):
            query['KeyName'] = request.key_name
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ManageLogin',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManageLoginResponse(),
            self.call_api(params, req, runtime)
        )

    async def manage_login_with_options_async(
        self,
        request: main_models.ManageLoginRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManageLoginResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_name):
            query['ActionName'] = request.action_name
        if not DaraCore.is_null(request.key_group):
            query['KeyGroup'] = request.key_group
        if not DaraCore.is_null(request.key_name):
            query['KeyName'] = request.key_name
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ManageLogin',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManageLoginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manage_login(
        self,
        request: main_models.ManageLoginRequest,
    ) -> main_models.ManageLoginResponse:
        runtime = RuntimeOptions()
        return self.manage_login_with_options(request, runtime)

    async def manage_login_async(
        self,
        request: main_models.ManageLoginRequest,
    ) -> main_models.ManageLoginResponse:
        runtime = RuntimeOptions()
        return await self.manage_login_with_options_async(request, runtime)

    def modify_device_with_options(
        self,
        request: main_models.ModifyDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_method):
            query['AlarmMethod'] = request.alarm_method
        if not DaraCore.is_null(request.auto_directory):
            query['AutoDirectory'] = request.auto_directory
        if not DaraCore.is_null(request.auto_pos):
            query['AutoPos'] = request.auto_pos
        if not DaraCore.is_null(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.gb_id):
            query['GbId'] = request.gb_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.latitude):
            query['Latitude'] = request.latitude
        if not DaraCore.is_null(request.longitude):
            query['Longitude'] = request.longitude
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.pos_interval):
            query['PosInterval'] = request.pos_interval
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_device_with_options_async(
        self,
        request: main_models.ModifyDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_method):
            query['AlarmMethod'] = request.alarm_method
        if not DaraCore.is_null(request.auto_directory):
            query['AutoDirectory'] = request.auto_directory
        if not DaraCore.is_null(request.auto_pos):
            query['AutoPos'] = request.auto_pos
        if not DaraCore.is_null(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.gb_id):
            query['GbId'] = request.gb_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.latitude):
            query['Latitude'] = request.latitude
        if not DaraCore.is_null(request.longitude):
            query['Longitude'] = request.longitude
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.pos_interval):
            query['PosInterval'] = request.pos_interval
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_device(
        self,
        request: main_models.ModifyDeviceRequest,
    ) -> main_models.ModifyDeviceResponse:
        runtime = RuntimeOptions()
        return self.modify_device_with_options(request, runtime)

    async def modify_device_async(
        self,
        request: main_models.ModifyDeviceRequest,
    ) -> main_models.ModifyDeviceResponse:
        runtime = RuntimeOptions()
        return await self.modify_device_with_options_async(request, runtime)

    def modify_device_alarm_with_options(
        self,
        request: main_models.ModifyDeviceAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDeviceAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDeviceAlarm',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDeviceAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_device_alarm_with_options_async(
        self,
        request: main_models.ModifyDeviceAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDeviceAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDeviceAlarm',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDeviceAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_device_alarm(
        self,
        request: main_models.ModifyDeviceAlarmRequest,
    ) -> main_models.ModifyDeviceAlarmResponse:
        runtime = RuntimeOptions()
        return self.modify_device_alarm_with_options(request, runtime)

    async def modify_device_alarm_async(
        self,
        request: main_models.ModifyDeviceAlarmRequest,
    ) -> main_models.ModifyDeviceAlarmResponse:
        runtime = RuntimeOptions()
        return await self.modify_device_alarm_with_options_async(request, runtime)

    def modify_device_capture_with_options(
        self,
        request: main_models.ModifyDeviceCaptureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDeviceCaptureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.image):
            query['Image'] = request.image
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.video):
            query['Video'] = request.video
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDeviceCapture',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDeviceCaptureResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_device_capture_with_options_async(
        self,
        request: main_models.ModifyDeviceCaptureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDeviceCaptureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.image):
            query['Image'] = request.image
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.video):
            query['Video'] = request.video
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDeviceCapture',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDeviceCaptureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_device_capture(
        self,
        request: main_models.ModifyDeviceCaptureRequest,
    ) -> main_models.ModifyDeviceCaptureResponse:
        runtime = RuntimeOptions()
        return self.modify_device_capture_with_options(request, runtime)

    async def modify_device_capture_async(
        self,
        request: main_models.ModifyDeviceCaptureRequest,
    ) -> main_models.ModifyDeviceCaptureResponse:
        runtime = RuntimeOptions()
        return await self.modify_device_capture_with_options_async(request, runtime)

    def modify_device_channels_with_options(
        self,
        request: main_models.ModifyDeviceChannelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDeviceChannelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channels):
            query['Channels'] = request.channels
        if not DaraCore.is_null(request.device_status):
            query['DeviceStatus'] = request.device_status
        if not DaraCore.is_null(request.dsn):
            query['Dsn'] = request.dsn
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDeviceChannels',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDeviceChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_device_channels_with_options_async(
        self,
        request: main_models.ModifyDeviceChannelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDeviceChannelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channels):
            query['Channels'] = request.channels
        if not DaraCore.is_null(request.device_status):
            query['DeviceStatus'] = request.device_status
        if not DaraCore.is_null(request.dsn):
            query['Dsn'] = request.dsn
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDeviceChannels',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDeviceChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_device_channels(
        self,
        request: main_models.ModifyDeviceChannelsRequest,
    ) -> main_models.ModifyDeviceChannelsResponse:
        runtime = RuntimeOptions()
        return self.modify_device_channels_with_options(request, runtime)

    async def modify_device_channels_async(
        self,
        request: main_models.ModifyDeviceChannelsRequest,
    ) -> main_models.ModifyDeviceChannelsResponse:
        runtime = RuntimeOptions()
        return await self.modify_device_channels_with_options_async(request, runtime)

    def modify_directory_with_options(
        self,
        request: main_models.ModifyDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDirectory',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_directory_with_options_async(
        self,
        request: main_models.ModifyDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDirectory',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_directory(
        self,
        request: main_models.ModifyDirectoryRequest,
    ) -> main_models.ModifyDirectoryResponse:
        runtime = RuntimeOptions()
        return self.modify_directory_with_options(request, runtime)

    async def modify_directory_async(
        self,
        request: main_models.ModifyDirectoryRequest,
    ) -> main_models.ModifyDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.modify_directory_with_options_async(request, runtime)

    def modify_group_with_options(
        self,
        request: main_models.ModifyGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callback):
            query['Callback'] = request.callback
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.in_protocol):
            query['InProtocol'] = request.in_protocol
        if not DaraCore.is_null(request.lazy_pull):
            query['LazyPull'] = request.lazy_pull
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not DaraCore.is_null(request.push_domain):
            query['PushDomain'] = request.push_domain
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyGroup',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_group_with_options_async(
        self,
        request: main_models.ModifyGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callback):
            query['Callback'] = request.callback
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.in_protocol):
            query['InProtocol'] = request.in_protocol
        if not DaraCore.is_null(request.lazy_pull):
            query['LazyPull'] = request.lazy_pull
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not DaraCore.is_null(request.push_domain):
            query['PushDomain'] = request.push_domain
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyGroup',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_group(
        self,
        request: main_models.ModifyGroupRequest,
    ) -> main_models.ModifyGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_group_with_options(request, runtime)

    async def modify_group_async(
        self,
        request: main_models.ModifyGroupRequest,
    ) -> main_models.ModifyGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_group_with_options_async(request, runtime)

    def modify_parent_platform_with_options(
        self,
        request: main_models.ModifyParentPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyParentPlatformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not DaraCore.is_null(request.client_auth):
            query['ClientAuth'] = request.client_auth
        if not DaraCore.is_null(request.client_password):
            query['ClientPassword'] = request.client_password
        if not DaraCore.is_null(request.client_username):
            query['ClientUsername'] = request.client_username
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.gb_id):
            query['GbId'] = request.gb_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyParentPlatform',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyParentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_parent_platform_with_options_async(
        self,
        request: main_models.ModifyParentPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyParentPlatformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not DaraCore.is_null(request.client_auth):
            query['ClientAuth'] = request.client_auth
        if not DaraCore.is_null(request.client_password):
            query['ClientPassword'] = request.client_password
        if not DaraCore.is_null(request.client_username):
            query['ClientUsername'] = request.client_username
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.gb_id):
            query['GbId'] = request.gb_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyParentPlatform',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyParentPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_parent_platform(
        self,
        request: main_models.ModifyParentPlatformRequest,
    ) -> main_models.ModifyParentPlatformResponse:
        runtime = RuntimeOptions()
        return self.modify_parent_platform_with_options(request, runtime)

    async def modify_parent_platform_async(
        self,
        request: main_models.ModifyParentPlatformRequest,
    ) -> main_models.ModifyParentPlatformResponse:
        runtime = RuntimeOptions()
        return await self.modify_parent_platform_with_options_async(request, runtime)

    def modify_rendering_charge_type_with_options(
        self,
        request: main_models.ModifyRenderingChargeTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRenderingChargeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.instance_billing_cycle):
            query['InstanceBillingCycle'] = request.instance_billing_cycle
        if not DaraCore.is_null(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRenderingChargeType',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRenderingChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rendering_charge_type_with_options_async(
        self,
        request: main_models.ModifyRenderingChargeTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRenderingChargeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.instance_billing_cycle):
            query['InstanceBillingCycle'] = request.instance_billing_cycle
        if not DaraCore.is_null(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRenderingChargeType',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRenderingChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rendering_charge_type(
        self,
        request: main_models.ModifyRenderingChargeTypeRequest,
    ) -> main_models.ModifyRenderingChargeTypeResponse:
        runtime = RuntimeOptions()
        return self.modify_rendering_charge_type_with_options(request, runtime)

    async def modify_rendering_charge_type_async(
        self,
        request: main_models.ModifyRenderingChargeTypeRequest,
    ) -> main_models.ModifyRenderingChargeTypeResponse:
        runtime = RuntimeOptions()
        return await self.modify_rendering_charge_type_with_options_async(request, runtime)

    def modify_rendering_instance_with_options(
        self,
        request: main_models.ModifyRenderingInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRenderingInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not DaraCore.is_null(request.rendering_spec):
            query['RenderingSpec'] = request.rendering_spec
        if not DaraCore.is_null(request.storage_size):
            query['StorageSize'] = request.storage_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRenderingInstance',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRenderingInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rendering_instance_with_options_async(
        self,
        request: main_models.ModifyRenderingInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRenderingInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not DaraCore.is_null(request.rendering_spec):
            query['RenderingSpec'] = request.rendering_spec
        if not DaraCore.is_null(request.storage_size):
            query['StorageSize'] = request.storage_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRenderingInstance',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRenderingInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rendering_instance(
        self,
        request: main_models.ModifyRenderingInstanceRequest,
    ) -> main_models.ModifyRenderingInstanceResponse:
        runtime = RuntimeOptions()
        return self.modify_rendering_instance_with_options(request, runtime)

    async def modify_rendering_instance_async(
        self,
        request: main_models.ModifyRenderingInstanceRequest,
    ) -> main_models.ModifyRenderingInstanceResponse:
        runtime = RuntimeOptions()
        return await self.modify_rendering_instance_with_options_async(request, runtime)

    def modify_rendering_instance_attribute_with_options(
        self,
        request: main_models.ModifyRenderingInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRenderingInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRenderingInstanceAttribute',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRenderingInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rendering_instance_attribute_with_options_async(
        self,
        request: main_models.ModifyRenderingInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRenderingInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRenderingInstanceAttribute',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRenderingInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rendering_instance_attribute(
        self,
        request: main_models.ModifyRenderingInstanceAttributeRequest,
    ) -> main_models.ModifyRenderingInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_rendering_instance_attribute_with_options(request, runtime)

    async def modify_rendering_instance_attribute_async(
        self,
        request: main_models.ModifyRenderingInstanceAttributeRequest,
    ) -> main_models.ModifyRenderingInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_rendering_instance_attribute_with_options_async(request, runtime)

    def modify_rendering_instance_bandwidth_with_options(
        self,
        request: main_models.ModifyRenderingInstanceBandwidthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRenderingInstanceBandwidthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_egress_bandwidth):
            query['MaxEgressBandwidth'] = request.max_egress_bandwidth
        if not DaraCore.is_null(request.max_ingress_bandwidth):
            query['MaxIngressBandwidth'] = request.max_ingress_bandwidth
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRenderingInstanceBandwidth',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRenderingInstanceBandwidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rendering_instance_bandwidth_with_options_async(
        self,
        request: main_models.ModifyRenderingInstanceBandwidthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRenderingInstanceBandwidthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_egress_bandwidth):
            query['MaxEgressBandwidth'] = request.max_egress_bandwidth
        if not DaraCore.is_null(request.max_ingress_bandwidth):
            query['MaxIngressBandwidth'] = request.max_ingress_bandwidth
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRenderingInstanceBandwidth',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRenderingInstanceBandwidthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rendering_instance_bandwidth(
        self,
        request: main_models.ModifyRenderingInstanceBandwidthRequest,
    ) -> main_models.ModifyRenderingInstanceBandwidthResponse:
        runtime = RuntimeOptions()
        return self.modify_rendering_instance_bandwidth_with_options(request, runtime)

    async def modify_rendering_instance_bandwidth_async(
        self,
        request: main_models.ModifyRenderingInstanceBandwidthRequest,
    ) -> main_models.ModifyRenderingInstanceBandwidthResponse:
        runtime = RuntimeOptions()
        return await self.modify_rendering_instance_bandwidth_with_options_async(request, runtime)

    def modify_template_with_options(
        self,
        request: main_models.ModifyTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callback):
            query['Callback'] = request.callback
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_format):
            query['FileFormat'] = request.file_format
        if not DaraCore.is_null(request.flv):
            query['Flv'] = request.flv
        if not DaraCore.is_null(request.hls_m3u_8):
            query['HlsM3u8'] = request.hls_m3u_8
        if not DaraCore.is_null(request.hls_ts):
            query['HlsTs'] = request.hls_ts
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.jpg_on_demand):
            query['JpgOnDemand'] = request.jpg_on_demand
        if not DaraCore.is_null(request.jpg_overwrite):
            query['JpgOverwrite'] = request.jpg_overwrite
        if not DaraCore.is_null(request.jpg_sequence):
            query['JpgSequence'] = request.jpg_sequence
        if not DaraCore.is_null(request.mp_4):
            query['Mp4'] = request.mp_4
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.retention):
            query['Retention'] = request.retention
        if not DaraCore.is_null(request.trans_configs_json):
            query['TransConfigsJSON'] = request.trans_configs_json
        if not DaraCore.is_null(request.trigger):
            query['Trigger'] = request.trigger
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTemplate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_template_with_options_async(
        self,
        request: main_models.ModifyTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callback):
            query['Callback'] = request.callback
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_format):
            query['FileFormat'] = request.file_format
        if not DaraCore.is_null(request.flv):
            query['Flv'] = request.flv
        if not DaraCore.is_null(request.hls_m3u_8):
            query['HlsM3u8'] = request.hls_m3u_8
        if not DaraCore.is_null(request.hls_ts):
            query['HlsTs'] = request.hls_ts
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.jpg_on_demand):
            query['JpgOnDemand'] = request.jpg_on_demand
        if not DaraCore.is_null(request.jpg_overwrite):
            query['JpgOverwrite'] = request.jpg_overwrite
        if not DaraCore.is_null(request.jpg_sequence):
            query['JpgSequence'] = request.jpg_sequence
        if not DaraCore.is_null(request.mp_4):
            query['Mp4'] = request.mp_4
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.retention):
            query['Retention'] = request.retention
        if not DaraCore.is_null(request.trans_configs_json):
            query['TransConfigsJSON'] = request.trans_configs_json
        if not DaraCore.is_null(request.trigger):
            query['Trigger'] = request.trigger
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTemplate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_template(
        self,
        request: main_models.ModifyTemplateRequest,
    ) -> main_models.ModifyTemplateResponse:
        runtime = RuntimeOptions()
        return self.modify_template_with_options(request, runtime)

    async def modify_template_async(
        self,
        request: main_models.ModifyTemplateRequest,
    ) -> main_models.ModifyTemplateResponse:
        runtime = RuntimeOptions()
        return await self.modify_template_with_options_async(request, runtime)

    def open_vs_service_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.OpenVsServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'OpenVsService',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenVsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_vs_service_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.OpenVsServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'OpenVsService',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenVsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_vs_service(self) -> main_models.OpenVsServiceResponse:
        runtime = RuntimeOptions()
        return self.open_vs_service_with_options(runtime)

    async def open_vs_service_async(self) -> main_models.OpenVsServiceResponse:
        runtime = RuntimeOptions()
        return await self.open_vs_service_with_options_async(runtime)

    def push_file_with_options(
        self,
        request: main_models.PushFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushFile',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_file_with_options_async(
        self,
        request: main_models.PushFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushFile',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_file(
        self,
        request: main_models.PushFileRequest,
    ) -> main_models.PushFileResponse:
        runtime = RuntimeOptions()
        return self.push_file_with_options(request, runtime)

    async def push_file_async(
        self,
        request: main_models.PushFileRequest,
    ) -> main_models.PushFileResponse:
        runtime = RuntimeOptions()
        return await self.push_file_with_options_async(request, runtime)

    def reboot_rendering_instance_with_options(
        self,
        request: main_models.RebootRenderingInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootRenderingInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootRenderingInstance',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootRenderingInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_rendering_instance_with_options_async(
        self,
        request: main_models.RebootRenderingInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootRenderingInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootRenderingInstance',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootRenderingInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_rendering_instance(
        self,
        request: main_models.RebootRenderingInstanceRequest,
    ) -> main_models.RebootRenderingInstanceResponse:
        runtime = RuntimeOptions()
        return self.reboot_rendering_instance_with_options(request, runtime)

    async def reboot_rendering_instance_async(
        self,
        request: main_models.RebootRenderingInstanceRequest,
    ) -> main_models.RebootRenderingInstanceResponse:
        runtime = RuntimeOptions()
        return await self.reboot_rendering_instance_with_options_async(request, runtime)

    def reboot_rendering_server_with_options(
        self,
        tmp_req: main_models.RebootRenderingServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootRenderingServerResponse:
        tmp_req.validate()
        request = main_models.RebootRenderingServerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootRenderingServer',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootRenderingServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_rendering_server_with_options_async(
        self,
        tmp_req: main_models.RebootRenderingServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootRenderingServerResponse:
        tmp_req.validate()
        request = main_models.RebootRenderingServerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RebootRenderingServer',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootRenderingServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_rendering_server(
        self,
        request: main_models.RebootRenderingServerRequest,
    ) -> main_models.RebootRenderingServerResponse:
        runtime = RuntimeOptions()
        return self.reboot_rendering_server_with_options(request, runtime)

    async def reboot_rendering_server_async(
        self,
        request: main_models.RebootRenderingServerRequest,
    ) -> main_models.RebootRenderingServerResponse:
        runtime = RuntimeOptions()
        return await self.reboot_rendering_server_with_options_async(request, runtime)

    def recover_rendering_data_package_with_options(
        self,
        request: main_models.RecoverRenderingDataPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecoverRenderingDataPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_package_id):
            query['DataPackageId'] = request.data_package_id
        if not DaraCore.is_null(request.load_mode):
            query['LoadMode'] = request.load_mode
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecoverRenderingDataPackage',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecoverRenderingDataPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def recover_rendering_data_package_with_options_async(
        self,
        request: main_models.RecoverRenderingDataPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecoverRenderingDataPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_package_id):
            query['DataPackageId'] = request.data_package_id
        if not DaraCore.is_null(request.load_mode):
            query['LoadMode'] = request.load_mode
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecoverRenderingDataPackage',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecoverRenderingDataPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recover_rendering_data_package(
        self,
        request: main_models.RecoverRenderingDataPackageRequest,
    ) -> main_models.RecoverRenderingDataPackageResponse:
        runtime = RuntimeOptions()
        return self.recover_rendering_data_package_with_options(request, runtime)

    async def recover_rendering_data_package_async(
        self,
        request: main_models.RecoverRenderingDataPackageRequest,
    ) -> main_models.RecoverRenderingDataPackageResponse:
        runtime = RuntimeOptions()
        return await self.recover_rendering_data_package_with_options_async(request, runtime)

    def refresh_rendering_instance_streaming_with_options(
        self,
        tmp_req: main_models.RefreshRenderingInstanceStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshRenderingInstanceStreamingResponse:
        tmp_req.validate()
        request = main_models.RefreshRenderingInstanceStreamingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.client_info):
            request.client_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_info, 'ClientInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.client_info_shrink):
            query['ClientInfo'] = request.client_info_shrink
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshRenderingInstanceStreaming',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshRenderingInstanceStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_rendering_instance_streaming_with_options_async(
        self,
        tmp_req: main_models.RefreshRenderingInstanceStreamingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshRenderingInstanceStreamingResponse:
        tmp_req.validate()
        request = main_models.RefreshRenderingInstanceStreamingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.client_info):
            request.client_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_info, 'ClientInfo', 'json')
        query = {}
        if not DaraCore.is_null(request.client_info_shrink):
            query['ClientInfo'] = request.client_info_shrink
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshRenderingInstanceStreaming',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshRenderingInstanceStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_rendering_instance_streaming(
        self,
        request: main_models.RefreshRenderingInstanceStreamingRequest,
    ) -> main_models.RefreshRenderingInstanceStreamingResponse:
        runtime = RuntimeOptions()
        return self.refresh_rendering_instance_streaming_with_options(request, runtime)

    async def refresh_rendering_instance_streaming_async(
        self,
        request: main_models.RefreshRenderingInstanceStreamingRequest,
    ) -> main_models.RefreshRenderingInstanceStreamingResponse:
        runtime = RuntimeOptions()
        return await self.refresh_rendering_instance_streaming_with_options_async(request, runtime)

    def release_rendering_data_package_with_options(
        self,
        request: main_models.ReleaseRenderingDataPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseRenderingDataPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_package_id):
            query['DataPackageId'] = request.data_package_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseRenderingDataPackage',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseRenderingDataPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_rendering_data_package_with_options_async(
        self,
        request: main_models.ReleaseRenderingDataPackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseRenderingDataPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_package_id):
            query['DataPackageId'] = request.data_package_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseRenderingDataPackage',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseRenderingDataPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_rendering_data_package(
        self,
        request: main_models.ReleaseRenderingDataPackageRequest,
    ) -> main_models.ReleaseRenderingDataPackageResponse:
        runtime = RuntimeOptions()
        return self.release_rendering_data_package_with_options(request, runtime)

    async def release_rendering_data_package_async(
        self,
        request: main_models.ReleaseRenderingDataPackageRequest,
    ) -> main_models.ReleaseRenderingDataPackageResponse:
        runtime = RuntimeOptions()
        return await self.release_rendering_data_package_with_options_async(request, runtime)

    def release_rendering_instance_with_options(
        self,
        request: main_models.ReleaseRenderingInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseRenderingInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseRenderingInstance',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseRenderingInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_rendering_instance_with_options_async(
        self,
        request: main_models.ReleaseRenderingInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseRenderingInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseRenderingInstance',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseRenderingInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_rendering_instance(
        self,
        request: main_models.ReleaseRenderingInstanceRequest,
    ) -> main_models.ReleaseRenderingInstanceResponse:
        runtime = RuntimeOptions()
        return self.release_rendering_instance_with_options(request, runtime)

    async def release_rendering_instance_async(
        self,
        request: main_models.ReleaseRenderingInstanceRequest,
    ) -> main_models.ReleaseRenderingInstanceResponse:
        runtime = RuntimeOptions()
        return await self.release_rendering_instance_with_options_async(request, runtime)

    def renew_rendering_instance_with_options(
        self,
        request: main_models.RenewRenderingInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewRenderingInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewRenderingInstance',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewRenderingInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_rendering_instance_with_options_async(
        self,
        request: main_models.RenewRenderingInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewRenderingInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewRenderingInstance',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewRenderingInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_rendering_instance(
        self,
        request: main_models.RenewRenderingInstanceRequest,
    ) -> main_models.RenewRenderingInstanceResponse:
        runtime = RuntimeOptions()
        return self.renew_rendering_instance_with_options(request, runtime)

    async def renew_rendering_instance_async(
        self,
        request: main_models.RenewRenderingInstanceRequest,
    ) -> main_models.RenewRenderingInstanceResponse:
        runtime = RuntimeOptions()
        return await self.renew_rendering_instance_with_options_async(request, runtime)

    def reset_rendering_instance_with_options(
        self,
        request: main_models.ResetRenderingInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetRenderingInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_name):
            query['ActionName'] = request.action_name
        if not DaraCore.is_null(request.data_package_id):
            query['DataPackageId'] = request.data_package_id
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetRenderingInstance',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetRenderingInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_rendering_instance_with_options_async(
        self,
        request: main_models.ResetRenderingInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetRenderingInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_name):
            query['ActionName'] = request.action_name
        if not DaraCore.is_null(request.data_package_id):
            query['DataPackageId'] = request.data_package_id
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetRenderingInstance',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetRenderingInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_rendering_instance(
        self,
        request: main_models.ResetRenderingInstanceRequest,
    ) -> main_models.ResetRenderingInstanceResponse:
        runtime = RuntimeOptions()
        return self.reset_rendering_instance_with_options(request, runtime)

    async def reset_rendering_instance_async(
        self,
        request: main_models.ResetRenderingInstanceRequest,
    ) -> main_models.ResetRenderingInstanceResponse:
        runtime = RuntimeOptions()
        return await self.reset_rendering_instance_with_options_async(request, runtime)

    def resume_vs_stream_with_options(
        self,
        request: main_models.ResumeVsStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeVsStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeVsStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeVsStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_vs_stream_with_options_async(
        self,
        request: main_models.ResumeVsStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeVsStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeVsStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeVsStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_vs_stream(
        self,
        request: main_models.ResumeVsStreamRequest,
    ) -> main_models.ResumeVsStreamResponse:
        runtime = RuntimeOptions()
        return self.resume_vs_stream_with_options(request, runtime)

    async def resume_vs_stream_async(
        self,
        request: main_models.ResumeVsStreamRequest,
    ) -> main_models.ResumeVsStreamResponse:
        runtime = RuntimeOptions()
        return await self.resume_vs_stream_with_options_async(request, runtime)

    def send_rendering_instance_commands_with_options(
        self,
        request: main_models.SendRenderingInstanceCommandsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendRenderingInstanceCommandsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        body = {}
        if not DaraCore.is_null(request.commands):
            body['Commands'] = request.commands
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendRenderingInstanceCommands',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendRenderingInstanceCommandsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_rendering_instance_commands_with_options_async(
        self,
        request: main_models.SendRenderingInstanceCommandsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendRenderingInstanceCommandsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        body = {}
        if not DaraCore.is_null(request.commands):
            body['Commands'] = request.commands
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendRenderingInstanceCommands',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendRenderingInstanceCommandsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_rendering_instance_commands(
        self,
        request: main_models.SendRenderingInstanceCommandsRequest,
    ) -> main_models.SendRenderingInstanceCommandsResponse:
        runtime = RuntimeOptions()
        return self.send_rendering_instance_commands_with_options(request, runtime)

    async def send_rendering_instance_commands_async(
        self,
        request: main_models.SendRenderingInstanceCommandsRequest,
    ) -> main_models.SendRenderingInstanceCommandsResponse:
        runtime = RuntimeOptions()
        return await self.send_rendering_instance_commands_with_options_async(request, runtime)

    def set_preset_with_options(
        self,
        request: main_models.SetPresetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPresetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preset_id):
            query['PresetId'] = request.preset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPreset',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPresetResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_preset_with_options_async(
        self,
        request: main_models.SetPresetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPresetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preset_id):
            query['PresetId'] = request.preset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPreset',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPresetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_preset(
        self,
        request: main_models.SetPresetRequest,
    ) -> main_models.SetPresetResponse:
        runtime = RuntimeOptions()
        return self.set_preset_with_options(request, runtime)

    async def set_preset_async(
        self,
        request: main_models.SetPresetRequest,
    ) -> main_models.SetPresetResponse:
        runtime = RuntimeOptions()
        return await self.set_preset_with_options_async(request, runtime)

    def set_vs_domain_certificate_with_options(
        self,
        request: main_models.SetVsDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetVsDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_type):
            query['CertType'] = request.cert_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.force_set):
            query['ForceSet'] = request.force_set
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not DaraCore.is_null(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not DaraCore.is_null(request.sslpub):
            query['SSLPub'] = request.sslpub
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetVsDomainCertificate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetVsDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_vs_domain_certificate_with_options_async(
        self,
        request: main_models.SetVsDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetVsDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_name):
            query['CertName'] = request.cert_name
        if not DaraCore.is_null(request.cert_type):
            query['CertType'] = request.cert_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.force_set):
            query['ForceSet'] = request.force_set
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not DaraCore.is_null(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not DaraCore.is_null(request.sslpub):
            query['SSLPub'] = request.sslpub
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetVsDomainCertificate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetVsDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_vs_domain_certificate(
        self,
        request: main_models.SetVsDomainCertificateRequest,
    ) -> main_models.SetVsDomainCertificateResponse:
        runtime = RuntimeOptions()
        return self.set_vs_domain_certificate_with_options(request, runtime)

    async def set_vs_domain_certificate_async(
        self,
        request: main_models.SetVsDomainCertificateRequest,
    ) -> main_models.SetVsDomainCertificateResponse:
        runtime = RuntimeOptions()
        return await self.set_vs_domain_certificate_with_options_async(request, runtime)

    def set_vs_streams_notify_url_config_with_options(
        self,
        request: main_models.SetVsStreamsNotifyUrlConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetVsStreamsNotifyUrlConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetVsStreamsNotifyUrlConfig',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetVsStreamsNotifyUrlConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_vs_streams_notify_url_config_with_options_async(
        self,
        request: main_models.SetVsStreamsNotifyUrlConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetVsStreamsNotifyUrlConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetVsStreamsNotifyUrlConfig',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetVsStreamsNotifyUrlConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_vs_streams_notify_url_config(
        self,
        request: main_models.SetVsStreamsNotifyUrlConfigRequest,
    ) -> main_models.SetVsStreamsNotifyUrlConfigResponse:
        runtime = RuntimeOptions()
        return self.set_vs_streams_notify_url_config_with_options(request, runtime)

    async def set_vs_streams_notify_url_config_async(
        self,
        request: main_models.SetVsStreamsNotifyUrlConfigRequest,
    ) -> main_models.SetVsStreamsNotifyUrlConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_vs_streams_notify_url_config_with_options_async(request, runtime)

    def start_device_with_options(
        self,
        request: main_models.StartDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_device_with_options_async(
        self,
        request: main_models.StartDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_device(
        self,
        request: main_models.StartDeviceRequest,
    ) -> main_models.StartDeviceResponse:
        runtime = RuntimeOptions()
        return self.start_device_with_options(request, runtime)

    async def start_device_async(
        self,
        request: main_models.StartDeviceRequest,
    ) -> main_models.StartDeviceResponse:
        runtime = RuntimeOptions()
        return await self.start_device_with_options_async(request, runtime)

    def start_parent_platform_with_options(
        self,
        request: main_models.StartParentPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartParentPlatformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartParentPlatform',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartParentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_parent_platform_with_options_async(
        self,
        request: main_models.StartParentPlatformRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartParentPlatformResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartParentPlatform',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartParentPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_parent_platform(
        self,
        request: main_models.StartParentPlatformRequest,
    ) -> main_models.StartParentPlatformResponse:
        runtime = RuntimeOptions()
        return self.start_parent_platform_with_options(request, runtime)

    async def start_parent_platform_async(
        self,
        request: main_models.StartParentPlatformRequest,
    ) -> main_models.StartParentPlatformResponse:
        runtime = RuntimeOptions()
        return await self.start_parent_platform_with_options_async(request, runtime)

    def start_publish_stream_with_options(
        self,
        request: main_models.StartPublishStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartPublishStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.publish_url):
            query['PublishUrl'] = request.publish_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartPublishStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartPublishStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_publish_stream_with_options_async(
        self,
        request: main_models.StartPublishStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartPublishStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.publish_url):
            query['PublishUrl'] = request.publish_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartPublishStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartPublishStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_publish_stream(
        self,
        request: main_models.StartPublishStreamRequest,
    ) -> main_models.StartPublishStreamResponse:
        runtime = RuntimeOptions()
        return self.start_publish_stream_with_options(request, runtime)

    async def start_publish_stream_async(
        self,
        request: main_models.StartPublishStreamRequest,
    ) -> main_models.StartPublishStreamResponse:
        runtime = RuntimeOptions()
        return await self.start_publish_stream_with_options_async(request, runtime)

    def start_record_stream_with_options(
        self,
        request: main_models.StartRecordStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartRecordStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app):
            query['App'] = request.app
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_domain):
            query['PlayDomain'] = request.play_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartRecordStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartRecordStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_record_stream_with_options_async(
        self,
        request: main_models.StartRecordStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartRecordStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app):
            query['App'] = request.app
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_domain):
            query['PlayDomain'] = request.play_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartRecordStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartRecordStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_record_stream(
        self,
        request: main_models.StartRecordStreamRequest,
    ) -> main_models.StartRecordStreamResponse:
        runtime = RuntimeOptions()
        return self.start_record_stream_with_options(request, runtime)

    async def start_record_stream_async(
        self,
        request: main_models.StartRecordStreamRequest,
    ) -> main_models.StartRecordStreamResponse:
        runtime = RuntimeOptions()
        return await self.start_record_stream_with_options_async(request, runtime)

    def start_rendering_session_with_options(
        self,
        tmp_req: main_models.StartRenderingSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartRenderingSessionResponse:
        tmp_req.validate()
        request = main_models.StartRenderingSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.client_params):
            request.client_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_params, 'ClientParams', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_params_shrink):
            query['ClientParams'] = request.client_params_shrink
        if not DaraCore.is_null(request.patch_id):
            query['PatchId'] = request.patch_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartRenderingSession',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartRenderingSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_rendering_session_with_options_async(
        self,
        tmp_req: main_models.StartRenderingSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartRenderingSessionResponse:
        tmp_req.validate()
        request = main_models.StartRenderingSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.client_params):
            request.client_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_params, 'ClientParams', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_params_shrink):
            query['ClientParams'] = request.client_params_shrink
        if not DaraCore.is_null(request.patch_id):
            query['PatchId'] = request.patch_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartRenderingSession',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartRenderingSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_rendering_session(
        self,
        request: main_models.StartRenderingSessionRequest,
    ) -> main_models.StartRenderingSessionResponse:
        runtime = RuntimeOptions()
        return self.start_rendering_session_with_options(request, runtime)

    async def start_rendering_session_async(
        self,
        request: main_models.StartRenderingSessionRequest,
    ) -> main_models.StartRenderingSessionResponse:
        runtime = RuntimeOptions()
        return await self.start_rendering_session_with_options_async(request, runtime)

    def start_stream_with_options(
        self,
        request: main_models.StartStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_stream_with_options_async(
        self,
        request: main_models.StartStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_stream(
        self,
        request: main_models.StartStreamRequest,
    ) -> main_models.StartStreamResponse:
        runtime = RuntimeOptions()
        return self.start_stream_with_options(request, runtime)

    async def start_stream_async(
        self,
        request: main_models.StartStreamRequest,
    ) -> main_models.StartStreamResponse:
        runtime = RuntimeOptions()
        return await self.start_stream_with_options_async(request, runtime)

    def start_transfer_stream_with_options(
        self,
        request: main_models.StartTransferStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartTransferStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.transcode):
            query['Transcode'] = request.transcode
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartTransferStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartTransferStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_transfer_stream_with_options_async(
        self,
        request: main_models.StartTransferStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartTransferStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.transcode):
            query['Transcode'] = request.transcode
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartTransferStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartTransferStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_transfer_stream(
        self,
        request: main_models.StartTransferStreamRequest,
    ) -> main_models.StartTransferStreamResponse:
        runtime = RuntimeOptions()
        return self.start_transfer_stream_with_options(request, runtime)

    async def start_transfer_stream_async(
        self,
        request: main_models.StartTransferStreamRequest,
    ) -> main_models.StartTransferStreamResponse:
        runtime = RuntimeOptions()
        return await self.start_transfer_stream_with_options_async(request, runtime)

    def stop_adjust_with_options(
        self,
        request: main_models.StopAdjustRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAdjustResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.focus):
            query['Focus'] = request.focus
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.iris):
            query['Iris'] = request.iris
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopAdjust',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAdjustResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_adjust_with_options_async(
        self,
        request: main_models.StopAdjustRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAdjustResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.focus):
            query['Focus'] = request.focus
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.iris):
            query['Iris'] = request.iris
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopAdjust',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAdjustResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_adjust(
        self,
        request: main_models.StopAdjustRequest,
    ) -> main_models.StopAdjustResponse:
        runtime = RuntimeOptions()
        return self.stop_adjust_with_options(request, runtime)

    async def stop_adjust_async(
        self,
        request: main_models.StopAdjustRequest,
    ) -> main_models.StopAdjustResponse:
        runtime = RuntimeOptions()
        return await self.stop_adjust_with_options_async(request, runtime)

    def stop_device_with_options(
        self,
        request: main_models.StopDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_device_with_options_async(
        self,
        request: main_models.StopDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_device(
        self,
        request: main_models.StopDeviceRequest,
    ) -> main_models.StopDeviceResponse:
        runtime = RuntimeOptions()
        return self.stop_device_with_options(request, runtime)

    async def stop_device_async(
        self,
        request: main_models.StopDeviceRequest,
    ) -> main_models.StopDeviceResponse:
        runtime = RuntimeOptions()
        return await self.stop_device_with_options_async(request, runtime)

    def stop_move_with_options(
        self,
        request: main_models.StopMoveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopMoveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pan):
            query['Pan'] = request.pan
        if not DaraCore.is_null(request.tilt):
            query['Tilt'] = request.tilt
        if not DaraCore.is_null(request.zoom):
            query['Zoom'] = request.zoom
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopMove',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopMoveResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_move_with_options_async(
        self,
        request: main_models.StopMoveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopMoveResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pan):
            query['Pan'] = request.pan
        if not DaraCore.is_null(request.tilt):
            query['Tilt'] = request.tilt
        if not DaraCore.is_null(request.zoom):
            query['Zoom'] = request.zoom
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopMove',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopMoveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_move(
        self,
        request: main_models.StopMoveRequest,
    ) -> main_models.StopMoveResponse:
        runtime = RuntimeOptions()
        return self.stop_move_with_options(request, runtime)

    async def stop_move_async(
        self,
        request: main_models.StopMoveRequest,
    ) -> main_models.StopMoveResponse:
        runtime = RuntimeOptions()
        return await self.stop_move_with_options_async(request, runtime)

    def stop_publish_stream_with_options(
        self,
        request: main_models.StopPublishStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopPublishStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopPublishStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopPublishStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_publish_stream_with_options_async(
        self,
        request: main_models.StopPublishStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopPublishStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopPublishStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopPublishStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_publish_stream(
        self,
        request: main_models.StopPublishStreamRequest,
    ) -> main_models.StopPublishStreamResponse:
        runtime = RuntimeOptions()
        return self.stop_publish_stream_with_options(request, runtime)

    async def stop_publish_stream_async(
        self,
        request: main_models.StopPublishStreamRequest,
    ) -> main_models.StopPublishStreamResponse:
        runtime = RuntimeOptions()
        return await self.stop_publish_stream_with_options_async(request, runtime)

    def stop_record_stream_with_options(
        self,
        request: main_models.StopRecordStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopRecordStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app):
            query['App'] = request.app
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_domain):
            query['PlayDomain'] = request.play_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopRecordStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopRecordStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_record_stream_with_options_async(
        self,
        request: main_models.StopRecordStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopRecordStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app):
            query['App'] = request.app
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_domain):
            query['PlayDomain'] = request.play_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopRecordStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopRecordStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_record_stream(
        self,
        request: main_models.StopRecordStreamRequest,
    ) -> main_models.StopRecordStreamResponse:
        runtime = RuntimeOptions()
        return self.stop_record_stream_with_options(request, runtime)

    async def stop_record_stream_async(
        self,
        request: main_models.StopRecordStreamRequest,
    ) -> main_models.StopRecordStreamResponse:
        runtime = RuntimeOptions()
        return await self.stop_record_stream_with_options_async(request, runtime)

    def stop_rendering_session_with_options(
        self,
        request: main_models.StopRenderingSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopRenderingSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopRenderingSession',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopRenderingSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_rendering_session_with_options_async(
        self,
        request: main_models.StopRenderingSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopRenderingSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopRenderingSession',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopRenderingSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_rendering_session(
        self,
        request: main_models.StopRenderingSessionRequest,
    ) -> main_models.StopRenderingSessionResponse:
        runtime = RuntimeOptions()
        return self.stop_rendering_session_with_options(request, runtime)

    async def stop_rendering_session_async(
        self,
        request: main_models.StopRenderingSessionRequest,
    ) -> main_models.StopRenderingSessionResponse:
        runtime = RuntimeOptions()
        return await self.stop_rendering_session_with_options_async(request, runtime)

    def stop_stream_with_options(
        self,
        request: main_models.StopStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_stream_with_options_async(
        self,
        request: main_models.StopStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_stream(
        self,
        request: main_models.StopStreamRequest,
    ) -> main_models.StopStreamResponse:
        runtime = RuntimeOptions()
        return self.stop_stream_with_options(request, runtime)

    async def stop_stream_async(
        self,
        request: main_models.StopStreamRequest,
    ) -> main_models.StopStreamResponse:
        runtime = RuntimeOptions()
        return await self.stop_stream_with_options_async(request, runtime)

    def stop_transfer_stream_with_options(
        self,
        request: main_models.StopTransferStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopTransferStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.transcode):
            query['Transcode'] = request.transcode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopTransferStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTransferStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_transfer_stream_with_options_async(
        self,
        request: main_models.StopTransferStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopTransferStreamResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.transcode):
            query['Transcode'] = request.transcode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopTransferStream',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTransferStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_transfer_stream(
        self,
        request: main_models.StopTransferStreamRequest,
    ) -> main_models.StopTransferStreamResponse:
        runtime = RuntimeOptions()
        return self.stop_transfer_stream_with_options(request, runtime)

    async def stop_transfer_stream_async(
        self,
        request: main_models.StopTransferStreamRequest,
    ) -> main_models.StopTransferStreamResponse:
        runtime = RuntimeOptions()
        return await self.stop_transfer_stream_with_options_async(request, runtime)

    def sync_catalogs_with_options(
        self,
        request: main_models.SyncCatalogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncCatalogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncCatalogs',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncCatalogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_catalogs_with_options_async(
        self,
        request: main_models.SyncCatalogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncCatalogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncCatalogs',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncCatalogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_catalogs(
        self,
        request: main_models.SyncCatalogsRequest,
    ) -> main_models.SyncCatalogsResponse:
        runtime = RuntimeOptions()
        return self.sync_catalogs_with_options(request, runtime)

    async def sync_catalogs_async(
        self,
        request: main_models.SyncCatalogsRequest,
    ) -> main_models.SyncCatalogsResponse:
        runtime = RuntimeOptions()
        return await self.sync_catalogs_with_options_async(request, runtime)

    def unbind_directory_with_options(
        self,
        request: main_models.UnbindDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindDirectory',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_directory_with_options_async(
        self,
        request: main_models.UnbindDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindDirectory',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_directory(
        self,
        request: main_models.UnbindDirectoryRequest,
    ) -> main_models.UnbindDirectoryResponse:
        runtime = RuntimeOptions()
        return self.unbind_directory_with_options(request, runtime)

    async def unbind_directory_async(
        self,
        request: main_models.UnbindDirectoryRequest,
    ) -> main_models.UnbindDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.unbind_directory_with_options_async(request, runtime)

    def unbind_parent_platform_device_with_options(
        self,
        request: main_models.UnbindParentPlatformDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindParentPlatformDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindParentPlatformDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindParentPlatformDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_parent_platform_device_with_options_async(
        self,
        request: main_models.UnbindParentPlatformDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindParentPlatformDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindParentPlatformDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindParentPlatformDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_parent_platform_device(
        self,
        request: main_models.UnbindParentPlatformDeviceRequest,
    ) -> main_models.UnbindParentPlatformDeviceResponse:
        runtime = RuntimeOptions()
        return self.unbind_parent_platform_device_with_options(request, runtime)

    async def unbind_parent_platform_device_async(
        self,
        request: main_models.UnbindParentPlatformDeviceRequest,
    ) -> main_models.UnbindParentPlatformDeviceResponse:
        runtime = RuntimeOptions()
        return await self.unbind_parent_platform_device_with_options_async(request, runtime)

    def unbind_purchased_device_with_options(
        self,
        request: main_models.UnbindPurchasedDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindPurchasedDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindPurchasedDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindPurchasedDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_purchased_device_with_options_async(
        self,
        request: main_models.UnbindPurchasedDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindPurchasedDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindPurchasedDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindPurchasedDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_purchased_device(
        self,
        request: main_models.UnbindPurchasedDeviceRequest,
    ) -> main_models.UnbindPurchasedDeviceResponse:
        runtime = RuntimeOptions()
        return self.unbind_purchased_device_with_options(request, runtime)

    async def unbind_purchased_device_async(
        self,
        request: main_models.UnbindPurchasedDeviceRequest,
    ) -> main_models.UnbindPurchasedDeviceResponse:
        runtime = RuntimeOptions()
        return await self.unbind_purchased_device_with_options_async(request, runtime)

    def unbind_template_with_options(
        self,
        request: main_models.UnbindTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindTemplate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_template_with_options_async(
        self,
        request: main_models.UnbindTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindTemplate',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_template(
        self,
        request: main_models.UnbindTemplateRequest,
    ) -> main_models.UnbindTemplateResponse:
        runtime = RuntimeOptions()
        return self.unbind_template_with_options(request, runtime)

    async def unbind_template_async(
        self,
        request: main_models.UnbindTemplateRequest,
    ) -> main_models.UnbindTemplateResponse:
        runtime = RuntimeOptions()
        return await self.unbind_template_with_options_async(request, runtime)

    def uninstall_cloud_app_with_options(
        self,
        tmp_req: main_models.UninstallCloudAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallCloudAppResponse:
        tmp_req.validate()
        request = main_models.UninstallCloudAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.patch_id):
            query['PatchId'] = request.patch_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not DaraCore.is_null(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UninstallCloudApp',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallCloudAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_cloud_app_with_options_async(
        self,
        tmp_req: main_models.UninstallCloudAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallCloudAppResponse:
        tmp_req.validate()
        request = main_models.UninstallCloudAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.patch_id):
            query['PatchId'] = request.patch_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not DaraCore.is_null(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UninstallCloudApp',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallCloudAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_cloud_app(
        self,
        request: main_models.UninstallCloudAppRequest,
    ) -> main_models.UninstallCloudAppResponse:
        runtime = RuntimeOptions()
        return self.uninstall_cloud_app_with_options(request, runtime)

    async def uninstall_cloud_app_async(
        self,
        request: main_models.UninstallCloudAppRequest,
    ) -> main_models.UninstallCloudAppResponse:
        runtime = RuntimeOptions()
        return await self.uninstall_cloud_app_with_options_async(request, runtime)

    def unlock_device_with_options(
        self,
        request: main_models.UnlockDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnlockDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnlockDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnlockDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_device_with_options_async(
        self,
        request: main_models.UnlockDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnlockDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnlockDevice',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnlockDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_device(
        self,
        request: main_models.UnlockDeviceRequest,
    ) -> main_models.UnlockDeviceResponse:
        runtime = RuntimeOptions()
        return self.unlock_device_with_options(request, runtime)

    async def unlock_device_async(
        self,
        request: main_models.UnlockDeviceRequest,
    ) -> main_models.UnlockDeviceResponse:
        runtime = RuntimeOptions()
        return await self.unlock_device_with_options_async(request, runtime)

    def update_cloud_app_info_with_options(
        self,
        tmp_req: main_models.UpdateCloudAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudAppInfoResponse:
        tmp_req.validate()
        request = main_models.UpdateCloudAppInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.patch):
            request.patch_shrink = Utils.array_to_string_with_specified_style(tmp_req.patch, 'Patch', 'json')
        if not DaraCore.is_null(tmp_req.pkg_labels):
            request.pkg_labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.pkg_labels, 'PkgLabels', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.pkg_labels_shrink):
            query['PkgLabels'] = request.pkg_labels_shrink
        if not DaraCore.is_null(request.stable_patch_id):
            query['StablePatchId'] = request.stable_patch_id
        body = {}
        if not DaraCore.is_null(request.patch_shrink):
            body['Patch'] = request.patch_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudAppInfo',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_app_info_with_options_async(
        self,
        tmp_req: main_models.UpdateCloudAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudAppInfoResponse:
        tmp_req.validate()
        request = main_models.UpdateCloudAppInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.patch):
            request.patch_shrink = Utils.array_to_string_with_specified_style(tmp_req.patch, 'Patch', 'json')
        if not DaraCore.is_null(tmp_req.pkg_labels):
            request.pkg_labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.pkg_labels, 'PkgLabels', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.pkg_labels_shrink):
            query['PkgLabels'] = request.pkg_labels_shrink
        if not DaraCore.is_null(request.stable_patch_id):
            query['StablePatchId'] = request.stable_patch_id
        body = {}
        if not DaraCore.is_null(request.patch_shrink):
            body['Patch'] = request.patch_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudAppInfo',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudAppInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_app_info(
        self,
        request: main_models.UpdateCloudAppInfoRequest,
    ) -> main_models.UpdateCloudAppInfoResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_app_info_with_options(request, runtime)

    async def update_cloud_app_info_async(
        self,
        request: main_models.UpdateCloudAppInfoRequest,
    ) -> main_models.UpdateCloudAppInfoResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_app_info_with_options_async(request, runtime)

    def update_file_info_with_options(
        self,
        request: main_models.UpdateFileInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFileInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFileInfo',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFileInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_file_info_with_options_async(
        self,
        request: main_models.UpdateFileInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFileInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFileInfo',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFileInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_file_info(
        self,
        request: main_models.UpdateFileInfoRequest,
    ) -> main_models.UpdateFileInfoResponse:
        runtime = RuntimeOptions()
        return self.update_file_info_with_options(request, runtime)

    async def update_file_info_async(
        self,
        request: main_models.UpdateFileInfoRequest,
    ) -> main_models.UpdateFileInfoResponse:
        runtime = RuntimeOptions()
        return await self.update_file_info_with_options_async(request, runtime)

    def update_rendering_instance_configuration_with_options(
        self,
        tmp_req: main_models.UpdateRenderingInstanceConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRenderingInstanceConfigurationResponse:
        tmp_req.validate()
        request = main_models.UpdateRenderingInstanceConfigurationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.configuration):
            request.configuration_shrink = Utils.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        body = {}
        if not DaraCore.is_null(request.configuration_shrink):
            body['Configuration'] = request.configuration_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRenderingInstanceConfiguration',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRenderingInstanceConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rendering_instance_configuration_with_options_async(
        self,
        tmp_req: main_models.UpdateRenderingInstanceConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRenderingInstanceConfigurationResponse:
        tmp_req.validate()
        request = main_models.UpdateRenderingInstanceConfigurationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.configuration):
            request.configuration_shrink = Utils.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        body = {}
        if not DaraCore.is_null(request.configuration_shrink):
            body['Configuration'] = request.configuration_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRenderingInstanceConfiguration',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRenderingInstanceConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rendering_instance_configuration(
        self,
        request: main_models.UpdateRenderingInstanceConfigurationRequest,
    ) -> main_models.UpdateRenderingInstanceConfigurationResponse:
        runtime = RuntimeOptions()
        return self.update_rendering_instance_configuration_with_options(request, runtime)

    async def update_rendering_instance_configuration_async(
        self,
        request: main_models.UpdateRenderingInstanceConfigurationRequest,
    ) -> main_models.UpdateRenderingInstanceConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.update_rendering_instance_configuration_with_options_async(request, runtime)

    def update_rendering_instance_settings_with_options(
        self,
        tmp_req: main_models.UpdateRenderingInstanceSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRenderingInstanceSettingsResponse:
        tmp_req.validate()
        request = main_models.UpdateRenderingInstanceSettingsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.settings):
            request.settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.settings, 'Settings', 'json')
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not DaraCore.is_null(request.settings_shrink):
            query['Settings'] = request.settings_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRenderingInstanceSettings',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRenderingInstanceSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rendering_instance_settings_with_options_async(
        self,
        tmp_req: main_models.UpdateRenderingInstanceSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRenderingInstanceSettingsResponse:
        tmp_req.validate()
        request = main_models.UpdateRenderingInstanceSettingsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.settings):
            request.settings_shrink = Utils.array_to_string_with_specified_style(tmp_req.settings, 'Settings', 'json')
        query = {}
        if not DaraCore.is_null(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not DaraCore.is_null(request.settings_shrink):
            query['Settings'] = request.settings_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRenderingInstanceSettings',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRenderingInstanceSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rendering_instance_settings(
        self,
        request: main_models.UpdateRenderingInstanceSettingsRequest,
    ) -> main_models.UpdateRenderingInstanceSettingsResponse:
        runtime = RuntimeOptions()
        return self.update_rendering_instance_settings_with_options(request, runtime)

    async def update_rendering_instance_settings_async(
        self,
        request: main_models.UpdateRenderingInstanceSettingsRequest,
    ) -> main_models.UpdateRenderingInstanceSettingsResponse:
        runtime = RuntimeOptions()
        return await self.update_rendering_instance_settings_with_options_async(request, runtime)

    def update_rendering_project_with_options(
        self,
        tmp_req: main_models.UpdateRenderingProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRenderingProjectResponse:
        tmp_req.validate()
        request = main_models.UpdateRenderingProjectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.session_attribs):
            request.session_attribs_shrink = Utils.array_to_string_with_specified_style(tmp_req.session_attribs, 'SessionAttribs', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.session_attribs_shrink):
            query['SessionAttribs'] = request.session_attribs_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRenderingProject',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRenderingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rendering_project_with_options_async(
        self,
        tmp_req: main_models.UpdateRenderingProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRenderingProjectResponse:
        tmp_req.validate()
        request = main_models.UpdateRenderingProjectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.session_attribs):
            request.session_attribs_shrink = Utils.array_to_string_with_specified_style(tmp_req.session_attribs, 'SessionAttribs', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.session_attribs_shrink):
            query['SessionAttribs'] = request.session_attribs_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRenderingProject',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRenderingProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rendering_project(
        self,
        request: main_models.UpdateRenderingProjectRequest,
    ) -> main_models.UpdateRenderingProjectResponse:
        runtime = RuntimeOptions()
        return self.update_rendering_project_with_options(request, runtime)

    async def update_rendering_project_async(
        self,
        request: main_models.UpdateRenderingProjectRequest,
    ) -> main_models.UpdateRenderingProjectResponse:
        runtime = RuntimeOptions()
        return await self.update_rendering_project_with_options_async(request, runtime)

    def update_vs_pull_stream_info_config_with_options(
        self,
        request: main_models.UpdateVsPullStreamInfoConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVsPullStreamInfoConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.always):
            query['Always'] = request.always
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.source_url):
            query['SourceUrl'] = request.source_url
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVsPullStreamInfoConfig',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVsPullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vs_pull_stream_info_config_with_options_async(
        self,
        request: main_models.UpdateVsPullStreamInfoConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVsPullStreamInfoConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.always):
            query['Always'] = request.always
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.source_url):
            query['SourceUrl'] = request.source_url
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVsPullStreamInfoConfig',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVsPullStreamInfoConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vs_pull_stream_info_config(
        self,
        request: main_models.UpdateVsPullStreamInfoConfigRequest,
    ) -> main_models.UpdateVsPullStreamInfoConfigResponse:
        runtime = RuntimeOptions()
        return self.update_vs_pull_stream_info_config_with_options(request, runtime)

    async def update_vs_pull_stream_info_config_async(
        self,
        request: main_models.UpdateVsPullStreamInfoConfigRequest,
    ) -> main_models.UpdateVsPullStreamInfoConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_vs_pull_stream_info_config_with_options_async(request, runtime)

    def upload_cloud_app_with_options(
        self,
        tmp_req: main_models.UploadCloudAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadCloudAppResponse:
        tmp_req.validate()
        request = main_models.UploadCloudAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.pkg_labels):
            request.pkg_labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.pkg_labels, 'PkgLabels', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_version):
            query['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.download_url):
            query['DownloadUrl'] = request.download_url
        if not DaraCore.is_null(request.md_5):
            query['Md5'] = request.md_5
        if not DaraCore.is_null(request.pkg_format):
            query['PkgFormat'] = request.pkg_format
        if not DaraCore.is_null(request.pkg_labels_shrink):
            query['PkgLabels'] = request.pkg_labels_shrink
        if not DaraCore.is_null(request.pkg_type):
            query['PkgType'] = request.pkg_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadCloudApp',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadCloudAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_cloud_app_with_options_async(
        self,
        tmp_req: main_models.UploadCloudAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadCloudAppResponse:
        tmp_req.validate()
        request = main_models.UploadCloudAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.pkg_labels):
            request.pkg_labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.pkg_labels, 'PkgLabels', 'json')
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_version):
            query['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.download_url):
            query['DownloadUrl'] = request.download_url
        if not DaraCore.is_null(request.md_5):
            query['Md5'] = request.md_5
        if not DaraCore.is_null(request.pkg_format):
            query['PkgFormat'] = request.pkg_format
        if not DaraCore.is_null(request.pkg_labels_shrink):
            query['PkgLabels'] = request.pkg_labels_shrink
        if not DaraCore.is_null(request.pkg_type):
            query['PkgType'] = request.pkg_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadCloudApp',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadCloudAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_cloud_app(
        self,
        request: main_models.UploadCloudAppRequest,
    ) -> main_models.UploadCloudAppResponse:
        runtime = RuntimeOptions()
        return self.upload_cloud_app_with_options(request, runtime)

    async def upload_cloud_app_async(
        self,
        request: main_models.UploadCloudAppRequest,
    ) -> main_models.UploadCloudAppResponse:
        runtime = RuntimeOptions()
        return await self.upload_cloud_app_with_options_async(request, runtime)

    def upload_file_with_options(
        self,
        request: main_models.UploadFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.md_5):
            query['Md5'] = request.md_5
        if not DaraCore.is_null(request.origin_url):
            query['OriginUrl'] = request.origin_url
        if not DaraCore.is_null(request.target_path):
            query['TargetPath'] = request.target_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadFile',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_file_with_options_async(
        self,
        request: main_models.UploadFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.md_5):
            query['Md5'] = request.md_5
        if not DaraCore.is_null(request.origin_url):
            query['OriginUrl'] = request.origin_url
        if not DaraCore.is_null(request.target_path):
            query['TargetPath'] = request.target_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadFile',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_file(
        self,
        request: main_models.UploadFileRequest,
    ) -> main_models.UploadFileResponse:
        runtime = RuntimeOptions()
        return self.upload_file_with_options(request, runtime)

    async def upload_file_async(
        self,
        request: main_models.UploadFileRequest,
    ) -> main_models.UploadFileResponse:
        runtime = RuntimeOptions()
        return await self.upload_file_with_options_async(request, runtime)

    def upload_public_key_with_options(
        self,
        request: main_models.UploadPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.key_group):
            query['KeyGroup'] = request.key_group
        if not DaraCore.is_null(request.key_name):
            query['KeyName'] = request.key_name
        if not DaraCore.is_null(request.key_type):
            query['KeyType'] = request.key_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadPublicKey',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_public_key_with_options_async(
        self,
        request: main_models.UploadPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.key_group):
            query['KeyGroup'] = request.key_group
        if not DaraCore.is_null(request.key_name):
            query['KeyName'] = request.key_name
        if not DaraCore.is_null(request.key_type):
            query['KeyType'] = request.key_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadPublicKey',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_public_key(
        self,
        request: main_models.UploadPublicKeyRequest,
    ) -> main_models.UploadPublicKeyResponse:
        runtime = RuntimeOptions()
        return self.upload_public_key_with_options(request, runtime)

    async def upload_public_key_async(
        self,
        request: main_models.UploadPublicKeyRequest,
    ) -> main_models.UploadPublicKeyResponse:
        runtime = RuntimeOptions()
        return await self.upload_public_key_with_options_async(request, runtime)

    def verify_vs_domain_owner_with_options(
        self,
        request: main_models.VerifyVsDomainOwnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyVsDomainOwnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyVsDomainOwner',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyVsDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_vs_domain_owner_with_options_async(
        self,
        request: main_models.VerifyVsDomainOwnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyVsDomainOwnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyVsDomainOwner',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyVsDomainOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_vs_domain_owner(
        self,
        request: main_models.VerifyVsDomainOwnerRequest,
    ) -> main_models.VerifyVsDomainOwnerResponse:
        runtime = RuntimeOptions()
        return self.verify_vs_domain_owner_with_options(request, runtime)

    async def verify_vs_domain_owner_async(
        self,
        request: main_models.VerifyVsDomainOwnerRequest,
    ) -> main_models.VerifyVsDomainOwnerResponse:
        runtime = RuntimeOptions()
        return await self.verify_vs_domain_owner_with_options_async(request, runtime)
