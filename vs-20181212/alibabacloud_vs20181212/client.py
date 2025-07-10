# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_vs20181212 import models as vs_20181212_models
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
        self._signature_algorithm = 'v2'
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_vs_pull_stream_info_config_with_options(
        self,
        request: vs_20181212_models.AddVsPullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.AddVsPullStreamInfoConfigResponse:
        """
        @param request: AddVsPullStreamInfoConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddVsPullStreamInfoConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.always):
            query['Always'] = request.always
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_url):
            query['SourceUrl'] = request.source_url
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVsPullStreamInfoConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.AddVsPullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_vs_pull_stream_info_config_with_options_async(
        self,
        request: vs_20181212_models.AddVsPullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.AddVsPullStreamInfoConfigResponse:
        """
        @param request: AddVsPullStreamInfoConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddVsPullStreamInfoConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.always):
            query['Always'] = request.always
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_url):
            query['SourceUrl'] = request.source_url
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVsPullStreamInfoConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.AddVsPullStreamInfoConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_vs_pull_stream_info_config(
        self,
        request: vs_20181212_models.AddVsPullStreamInfoConfigRequest,
    ) -> vs_20181212_models.AddVsPullStreamInfoConfigResponse:
        """
        @param request: AddVsPullStreamInfoConfigRequest
        @return: AddVsPullStreamInfoConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_vs_pull_stream_info_config_with_options(request, runtime)

    async def add_vs_pull_stream_info_config_async(
        self,
        request: vs_20181212_models.AddVsPullStreamInfoConfigRequest,
    ) -> vs_20181212_models.AddVsPullStreamInfoConfigResponse:
        """
        @param request: AddVsPullStreamInfoConfigRequest
        @return: AddVsPullStreamInfoConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_vs_pull_stream_info_config_with_options_async(request, runtime)

    def associate_rendering_project_instances_with_options(
        self,
        tmp_req: vs_20181212_models.AssociateRenderingProjectInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.AssociateRenderingProjectInstancesResponse:
        """
        @summary 云应用服务实例与项目进行关联。
        
        @description ## 请求说明
        - 该接口用于将满足特定条件的实例与指定项目进行关联。
        
        @param tmp_req: AssociateRenderingProjectInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateRenderingProjectInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.AssociateRenderingProjectInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateRenderingProjectInstances',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.AssociateRenderingProjectInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_rendering_project_instances_with_options_async(
        self,
        tmp_req: vs_20181212_models.AssociateRenderingProjectInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.AssociateRenderingProjectInstancesResponse:
        """
        @summary 云应用服务实例与项目进行关联。
        
        @description ## 请求说明
        - 该接口用于将满足特定条件的实例与指定项目进行关联。
        
        @param tmp_req: AssociateRenderingProjectInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateRenderingProjectInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.AssociateRenderingProjectInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateRenderingProjectInstances',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.AssociateRenderingProjectInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_rendering_project_instances(
        self,
        request: vs_20181212_models.AssociateRenderingProjectInstancesRequest,
    ) -> vs_20181212_models.AssociateRenderingProjectInstancesResponse:
        """
        @summary 云应用服务实例与项目进行关联。
        
        @description ## 请求说明
        - 该接口用于将满足特定条件的实例与指定项目进行关联。
        
        @param request: AssociateRenderingProjectInstancesRequest
        @return: AssociateRenderingProjectInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_rendering_project_instances_with_options(request, runtime)

    async def associate_rendering_project_instances_async(
        self,
        request: vs_20181212_models.AssociateRenderingProjectInstancesRequest,
    ) -> vs_20181212_models.AssociateRenderingProjectInstancesResponse:
        """
        @summary 云应用服务实例与项目进行关联。
        
        @description ## 请求说明
        - 该接口用于将满足特定条件的实例与指定项目进行关联。
        
        @param request: AssociateRenderingProjectInstancesRequest
        @return: AssociateRenderingProjectInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.associate_rendering_project_instances_with_options_async(request, runtime)

    def batch_bind_directories_with_options(
        self,
        request: vs_20181212_models.BatchBindDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchBindDirectoriesResponse:
        """
        @param request: BatchBindDirectoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchBindDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchBindDirectories',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_bind_directories_with_options_async(
        self,
        request: vs_20181212_models.BatchBindDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchBindDirectoriesResponse:
        """
        @param request: BatchBindDirectoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchBindDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchBindDirectories',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_bind_directories(
        self,
        request: vs_20181212_models.BatchBindDirectoriesRequest,
    ) -> vs_20181212_models.BatchBindDirectoriesResponse:
        """
        @param request: BatchBindDirectoriesRequest
        @return: BatchBindDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_directories_with_options(request, runtime)

    async def batch_bind_directories_async(
        self,
        request: vs_20181212_models.BatchBindDirectoriesRequest,
    ) -> vs_20181212_models.BatchBindDirectoriesResponse:
        """
        @param request: BatchBindDirectoriesRequest
        @return: BatchBindDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_bind_directories_with_options_async(request, runtime)

    def batch_bind_parent_platform_devices_with_options(
        self,
        request: vs_20181212_models.BatchBindParentPlatformDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchBindParentPlatformDevicesResponse:
        """
        @param request: BatchBindParentPlatformDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchBindParentPlatformDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchBindParentPlatformDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindParentPlatformDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_bind_parent_platform_devices_with_options_async(
        self,
        request: vs_20181212_models.BatchBindParentPlatformDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchBindParentPlatformDevicesResponse:
        """
        @param request: BatchBindParentPlatformDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchBindParentPlatformDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchBindParentPlatformDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindParentPlatformDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_bind_parent_platform_devices(
        self,
        request: vs_20181212_models.BatchBindParentPlatformDevicesRequest,
    ) -> vs_20181212_models.BatchBindParentPlatformDevicesResponse:
        """
        @param request: BatchBindParentPlatformDevicesRequest
        @return: BatchBindParentPlatformDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_parent_platform_devices_with_options(request, runtime)

    async def batch_bind_parent_platform_devices_async(
        self,
        request: vs_20181212_models.BatchBindParentPlatformDevicesRequest,
    ) -> vs_20181212_models.BatchBindParentPlatformDevicesResponse:
        """
        @param request: BatchBindParentPlatformDevicesRequest
        @return: BatchBindParentPlatformDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_bind_parent_platform_devices_with_options_async(request, runtime)

    def batch_bind_purchased_devices_with_options(
        self,
        request: vs_20181212_models.BatchBindPurchasedDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchBindPurchasedDevicesResponse:
        """
        @param request: BatchBindPurchasedDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchBindPurchasedDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchBindPurchasedDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindPurchasedDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_bind_purchased_devices_with_options_async(
        self,
        request: vs_20181212_models.BatchBindPurchasedDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchBindPurchasedDevicesResponse:
        """
        @param request: BatchBindPurchasedDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchBindPurchasedDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchBindPurchasedDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindPurchasedDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_bind_purchased_devices(
        self,
        request: vs_20181212_models.BatchBindPurchasedDevicesRequest,
    ) -> vs_20181212_models.BatchBindPurchasedDevicesResponse:
        """
        @param request: BatchBindPurchasedDevicesRequest
        @return: BatchBindPurchasedDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_purchased_devices_with_options(request, runtime)

    async def batch_bind_purchased_devices_async(
        self,
        request: vs_20181212_models.BatchBindPurchasedDevicesRequest,
    ) -> vs_20181212_models.BatchBindPurchasedDevicesResponse:
        """
        @param request: BatchBindPurchasedDevicesRequest
        @return: BatchBindPurchasedDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_bind_purchased_devices_with_options_async(request, runtime)

    def batch_bind_template_with_options(
        self,
        request: vs_20181212_models.BatchBindTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchBindTemplateResponse:
        """
        @param request: BatchBindTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchBindTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_all):
            query['ApplyAll'] = request.apply_all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.replace):
            query['Replace'] = request.replace
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchBindTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_bind_template_with_options_async(
        self,
        request: vs_20181212_models.BatchBindTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchBindTemplateResponse:
        """
        @param request: BatchBindTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchBindTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_all):
            query['ApplyAll'] = request.apply_all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.replace):
            query['Replace'] = request.replace
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchBindTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_bind_template(
        self,
        request: vs_20181212_models.BatchBindTemplateRequest,
    ) -> vs_20181212_models.BatchBindTemplateResponse:
        """
        @param request: BatchBindTemplateRequest
        @return: BatchBindTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_template_with_options(request, runtime)

    async def batch_bind_template_async(
        self,
        request: vs_20181212_models.BatchBindTemplateRequest,
    ) -> vs_20181212_models.BatchBindTemplateResponse:
        """
        @param request: BatchBindTemplateRequest
        @return: BatchBindTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_bind_template_with_options_async(request, runtime)

    def batch_bind_templates_with_options(
        self,
        request: vs_20181212_models.BatchBindTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchBindTemplatesResponse:
        """
        @param request: BatchBindTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchBindTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_all):
            query['ApplyAll'] = request.apply_all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.replace):
            query['Replace'] = request.replace
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchBindTemplates',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_bind_templates_with_options_async(
        self,
        request: vs_20181212_models.BatchBindTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchBindTemplatesResponse:
        """
        @param request: BatchBindTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchBindTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_all):
            query['ApplyAll'] = request.apply_all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.replace):
            query['Replace'] = request.replace
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchBindTemplates',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_bind_templates(
        self,
        request: vs_20181212_models.BatchBindTemplatesRequest,
    ) -> vs_20181212_models.BatchBindTemplatesResponse:
        """
        @param request: BatchBindTemplatesRequest
        @return: BatchBindTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_templates_with_options(request, runtime)

    async def batch_bind_templates_async(
        self,
        request: vs_20181212_models.BatchBindTemplatesRequest,
    ) -> vs_20181212_models.BatchBindTemplatesResponse:
        """
        @param request: BatchBindTemplatesRequest
        @return: BatchBindTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_bind_templates_with_options_async(request, runtime)

    def batch_delete_devices_with_options(
        self,
        request: vs_20181212_models.BatchDeleteDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchDeleteDevicesResponse:
        """
        @param request: BatchDeleteDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchDeleteDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_devices_with_options_async(
        self,
        request: vs_20181212_models.BatchDeleteDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchDeleteDevicesResponse:
        """
        @param request: BatchDeleteDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchDeleteDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_devices(
        self,
        request: vs_20181212_models.BatchDeleteDevicesRequest,
    ) -> vs_20181212_models.BatchDeleteDevicesResponse:
        """
        @param request: BatchDeleteDevicesRequest
        @return: BatchDeleteDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_devices_with_options(request, runtime)

    async def batch_delete_devices_async(
        self,
        request: vs_20181212_models.BatchDeleteDevicesRequest,
    ) -> vs_20181212_models.BatchDeleteDevicesResponse:
        """
        @param request: BatchDeleteDevicesRequest
        @return: BatchDeleteDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_devices_with_options_async(request, runtime)

    def batch_delete_vs_domain_configs_with_options(
        self,
        request: vs_20181212_models.BatchDeleteVsDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchDeleteVsDomainConfigsResponse:
        """
        @param request: BatchDeleteVsDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteVsDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteVsDomainConfigs',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchDeleteVsDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_vs_domain_configs_with_options_async(
        self,
        request: vs_20181212_models.BatchDeleteVsDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchDeleteVsDomainConfigsResponse:
        """
        @param request: BatchDeleteVsDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteVsDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteVsDomainConfigs',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchDeleteVsDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_vs_domain_configs(
        self,
        request: vs_20181212_models.BatchDeleteVsDomainConfigsRequest,
    ) -> vs_20181212_models.BatchDeleteVsDomainConfigsResponse:
        """
        @param request: BatchDeleteVsDomainConfigsRequest
        @return: BatchDeleteVsDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_vs_domain_configs_with_options(request, runtime)

    async def batch_delete_vs_domain_configs_async(
        self,
        request: vs_20181212_models.BatchDeleteVsDomainConfigsRequest,
    ) -> vs_20181212_models.BatchDeleteVsDomainConfigsResponse:
        """
        @param request: BatchDeleteVsDomainConfigsRequest
        @return: BatchDeleteVsDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_vs_domain_configs_with_options_async(request, runtime)

    def batch_forbid_vs_stream_with_options(
        self,
        request: vs_20181212_models.BatchForbidVsStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchForbidVsStreamResponse:
        """
        @param request: BatchForbidVsStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchForbidVsStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not UtilClient.is_unset(request.oneshot):
            query['Oneshot'] = request.oneshot
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resume_time):
            query['ResumeTime'] = request.resume_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchForbidVsStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchForbidVsStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_forbid_vs_stream_with_options_async(
        self,
        request: vs_20181212_models.BatchForbidVsStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchForbidVsStreamResponse:
        """
        @param request: BatchForbidVsStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchForbidVsStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not UtilClient.is_unset(request.oneshot):
            query['Oneshot'] = request.oneshot
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resume_time):
            query['ResumeTime'] = request.resume_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchForbidVsStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchForbidVsStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_forbid_vs_stream(
        self,
        request: vs_20181212_models.BatchForbidVsStreamRequest,
    ) -> vs_20181212_models.BatchForbidVsStreamResponse:
        """
        @param request: BatchForbidVsStreamRequest
        @return: BatchForbidVsStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_forbid_vs_stream_with_options(request, runtime)

    async def batch_forbid_vs_stream_async(
        self,
        request: vs_20181212_models.BatchForbidVsStreamRequest,
    ) -> vs_20181212_models.BatchForbidVsStreamResponse:
        """
        @param request: BatchForbidVsStreamRequest
        @return: BatchForbidVsStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_forbid_vs_stream_with_options_async(request, runtime)

    def batch_resume_vs_stream_with_options(
        self,
        request: vs_20181212_models.BatchResumeVsStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchResumeVsStreamResponse:
        """
        @param request: BatchResumeVsStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchResumeVsStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchResumeVsStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchResumeVsStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_resume_vs_stream_with_options_async(
        self,
        request: vs_20181212_models.BatchResumeVsStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchResumeVsStreamResponse:
        """
        @param request: BatchResumeVsStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchResumeVsStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchResumeVsStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchResumeVsStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_resume_vs_stream(
        self,
        request: vs_20181212_models.BatchResumeVsStreamRequest,
    ) -> vs_20181212_models.BatchResumeVsStreamResponse:
        """
        @param request: BatchResumeVsStreamRequest
        @return: BatchResumeVsStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_resume_vs_stream_with_options(request, runtime)

    async def batch_resume_vs_stream_async(
        self,
        request: vs_20181212_models.BatchResumeVsStreamRequest,
    ) -> vs_20181212_models.BatchResumeVsStreamResponse:
        """
        @param request: BatchResumeVsStreamRequest
        @return: BatchResumeVsStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_resume_vs_stream_with_options_async(request, runtime)

    def batch_set_vs_domain_configs_with_options(
        self,
        request: vs_20181212_models.BatchSetVsDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchSetVsDomainConfigsResponse:
        """
        @param request: BatchSetVsDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSetVsDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSetVsDomainConfigs',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchSetVsDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_vs_domain_configs_with_options_async(
        self,
        request: vs_20181212_models.BatchSetVsDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchSetVsDomainConfigsResponse:
        """
        @param request: BatchSetVsDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSetVsDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSetVsDomainConfigs',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchSetVsDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_vs_domain_configs(
        self,
        request: vs_20181212_models.BatchSetVsDomainConfigsRequest,
    ) -> vs_20181212_models.BatchSetVsDomainConfigsResponse:
        """
        @param request: BatchSetVsDomainConfigsRequest
        @return: BatchSetVsDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_set_vs_domain_configs_with_options(request, runtime)

    async def batch_set_vs_domain_configs_async(
        self,
        request: vs_20181212_models.BatchSetVsDomainConfigsRequest,
    ) -> vs_20181212_models.BatchSetVsDomainConfigsResponse:
        """
        @param request: BatchSetVsDomainConfigsRequest
        @return: BatchSetVsDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_vs_domain_configs_with_options_async(request, runtime)

    def batch_start_devices_with_options(
        self,
        request: vs_20181212_models.BatchStartDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchStartDevicesResponse:
        """
        @param request: BatchStartDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStartDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStartDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchStartDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_start_devices_with_options_async(
        self,
        request: vs_20181212_models.BatchStartDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchStartDevicesResponse:
        """
        @param request: BatchStartDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStartDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStartDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchStartDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_start_devices(
        self,
        request: vs_20181212_models.BatchStartDevicesRequest,
    ) -> vs_20181212_models.BatchStartDevicesResponse:
        """
        @param request: BatchStartDevicesRequest
        @return: BatchStartDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_start_devices_with_options(request, runtime)

    async def batch_start_devices_async(
        self,
        request: vs_20181212_models.BatchStartDevicesRequest,
    ) -> vs_20181212_models.BatchStartDevicesResponse:
        """
        @param request: BatchStartDevicesRequest
        @return: BatchStartDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_start_devices_with_options_async(request, runtime)

    def batch_start_streams_with_options(
        self,
        request: vs_20181212_models.BatchStartStreamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchStartStreamsResponse:
        """
        @param request: BatchStartStreamsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStartStreamsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStartStreams',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchStartStreamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_start_streams_with_options_async(
        self,
        request: vs_20181212_models.BatchStartStreamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchStartStreamsResponse:
        """
        @param request: BatchStartStreamsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStartStreamsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStartStreams',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchStartStreamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_start_streams(
        self,
        request: vs_20181212_models.BatchStartStreamsRequest,
    ) -> vs_20181212_models.BatchStartStreamsResponse:
        """
        @param request: BatchStartStreamsRequest
        @return: BatchStartStreamsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_start_streams_with_options(request, runtime)

    async def batch_start_streams_async(
        self,
        request: vs_20181212_models.BatchStartStreamsRequest,
    ) -> vs_20181212_models.BatchStartStreamsResponse:
        """
        @param request: BatchStartStreamsRequest
        @return: BatchStartStreamsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_start_streams_with_options_async(request, runtime)

    def batch_stop_devices_with_options(
        self,
        request: vs_20181212_models.BatchStopDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchStopDevicesResponse:
        """
        @param request: BatchStopDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStopDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStopDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchStopDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_stop_devices_with_options_async(
        self,
        request: vs_20181212_models.BatchStopDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchStopDevicesResponse:
        """
        @param request: BatchStopDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStopDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStopDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchStopDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_stop_devices(
        self,
        request: vs_20181212_models.BatchStopDevicesRequest,
    ) -> vs_20181212_models.BatchStopDevicesResponse:
        """
        @param request: BatchStopDevicesRequest
        @return: BatchStopDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_devices_with_options(request, runtime)

    async def batch_stop_devices_async(
        self,
        request: vs_20181212_models.BatchStopDevicesRequest,
    ) -> vs_20181212_models.BatchStopDevicesResponse:
        """
        @param request: BatchStopDevicesRequest
        @return: BatchStopDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_stop_devices_with_options_async(request, runtime)

    def batch_stop_streams_with_options(
        self,
        request: vs_20181212_models.BatchStopStreamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchStopStreamsResponse:
        """
        @param request: BatchStopStreamsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStopStreamsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStopStreams',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchStopStreamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_stop_streams_with_options_async(
        self,
        request: vs_20181212_models.BatchStopStreamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchStopStreamsResponse:
        """
        @param request: BatchStopStreamsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchStopStreamsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStopStreams',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchStopStreamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_stop_streams(
        self,
        request: vs_20181212_models.BatchStopStreamsRequest,
    ) -> vs_20181212_models.BatchStopStreamsResponse:
        """
        @param request: BatchStopStreamsRequest
        @return: BatchStopStreamsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_streams_with_options(request, runtime)

    async def batch_stop_streams_async(
        self,
        request: vs_20181212_models.BatchStopStreamsRequest,
    ) -> vs_20181212_models.BatchStopStreamsResponse:
        """
        @param request: BatchStopStreamsRequest
        @return: BatchStopStreamsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_stop_streams_with_options_async(request, runtime)

    def batch_unbind_directories_with_options(
        self,
        request: vs_20181212_models.BatchUnbindDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchUnbindDirectoriesResponse:
        """
        @param request: BatchUnbindDirectoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUnbindDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUnbindDirectories',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_unbind_directories_with_options_async(
        self,
        request: vs_20181212_models.BatchUnbindDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchUnbindDirectoriesResponse:
        """
        @param request: BatchUnbindDirectoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUnbindDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUnbindDirectories',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_unbind_directories(
        self,
        request: vs_20181212_models.BatchUnbindDirectoriesRequest,
    ) -> vs_20181212_models.BatchUnbindDirectoriesResponse:
        """
        @param request: BatchUnbindDirectoriesRequest
        @return: BatchUnbindDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_directories_with_options(request, runtime)

    async def batch_unbind_directories_async(
        self,
        request: vs_20181212_models.BatchUnbindDirectoriesRequest,
    ) -> vs_20181212_models.BatchUnbindDirectoriesResponse:
        """
        @param request: BatchUnbindDirectoriesRequest
        @return: BatchUnbindDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_unbind_directories_with_options_async(request, runtime)

    def batch_unbind_parent_platform_devices_with_options(
        self,
        request: vs_20181212_models.BatchUnbindParentPlatformDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchUnbindParentPlatformDevicesResponse:
        """
        @param request: BatchUnbindParentPlatformDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUnbindParentPlatformDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUnbindParentPlatformDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindParentPlatformDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_unbind_parent_platform_devices_with_options_async(
        self,
        request: vs_20181212_models.BatchUnbindParentPlatformDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchUnbindParentPlatformDevicesResponse:
        """
        @param request: BatchUnbindParentPlatformDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUnbindParentPlatformDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUnbindParentPlatformDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindParentPlatformDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_unbind_parent_platform_devices(
        self,
        request: vs_20181212_models.BatchUnbindParentPlatformDevicesRequest,
    ) -> vs_20181212_models.BatchUnbindParentPlatformDevicesResponse:
        """
        @param request: BatchUnbindParentPlatformDevicesRequest
        @return: BatchUnbindParentPlatformDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_parent_platform_devices_with_options(request, runtime)

    async def batch_unbind_parent_platform_devices_async(
        self,
        request: vs_20181212_models.BatchUnbindParentPlatformDevicesRequest,
    ) -> vs_20181212_models.BatchUnbindParentPlatformDevicesResponse:
        """
        @param request: BatchUnbindParentPlatformDevicesRequest
        @return: BatchUnbindParentPlatformDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_unbind_parent_platform_devices_with_options_async(request, runtime)

    def batch_unbind_purchased_devices_with_options(
        self,
        request: vs_20181212_models.BatchUnbindPurchasedDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchUnbindPurchasedDevicesResponse:
        """
        @param request: BatchUnbindPurchasedDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUnbindPurchasedDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUnbindPurchasedDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindPurchasedDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_unbind_purchased_devices_with_options_async(
        self,
        request: vs_20181212_models.BatchUnbindPurchasedDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchUnbindPurchasedDevicesResponse:
        """
        @param request: BatchUnbindPurchasedDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUnbindPurchasedDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUnbindPurchasedDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindPurchasedDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_unbind_purchased_devices(
        self,
        request: vs_20181212_models.BatchUnbindPurchasedDevicesRequest,
    ) -> vs_20181212_models.BatchUnbindPurchasedDevicesResponse:
        """
        @param request: BatchUnbindPurchasedDevicesRequest
        @return: BatchUnbindPurchasedDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_purchased_devices_with_options(request, runtime)

    async def batch_unbind_purchased_devices_async(
        self,
        request: vs_20181212_models.BatchUnbindPurchasedDevicesRequest,
    ) -> vs_20181212_models.BatchUnbindPurchasedDevicesResponse:
        """
        @param request: BatchUnbindPurchasedDevicesRequest
        @return: BatchUnbindPurchasedDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_unbind_purchased_devices_with_options_async(request, runtime)

    def batch_unbind_template_with_options(
        self,
        request: vs_20181212_models.BatchUnbindTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchUnbindTemplateResponse:
        """
        @param request: BatchUnbindTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUnbindTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUnbindTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_unbind_template_with_options_async(
        self,
        request: vs_20181212_models.BatchUnbindTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchUnbindTemplateResponse:
        """
        @param request: BatchUnbindTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUnbindTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUnbindTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_unbind_template(
        self,
        request: vs_20181212_models.BatchUnbindTemplateRequest,
    ) -> vs_20181212_models.BatchUnbindTemplateResponse:
        """
        @param request: BatchUnbindTemplateRequest
        @return: BatchUnbindTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_template_with_options(request, runtime)

    async def batch_unbind_template_async(
        self,
        request: vs_20181212_models.BatchUnbindTemplateRequest,
    ) -> vs_20181212_models.BatchUnbindTemplateResponse:
        """
        @param request: BatchUnbindTemplateRequest
        @return: BatchUnbindTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_unbind_template_with_options_async(request, runtime)

    def batch_unbind_templates_with_options(
        self,
        request: vs_20181212_models.BatchUnbindTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchUnbindTemplatesResponse:
        """
        @param request: BatchUnbindTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUnbindTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUnbindTemplates',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_unbind_templates_with_options_async(
        self,
        request: vs_20181212_models.BatchUnbindTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BatchUnbindTemplatesResponse:
        """
        @param request: BatchUnbindTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUnbindTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUnbindTemplates',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_unbind_templates(
        self,
        request: vs_20181212_models.BatchUnbindTemplatesRequest,
    ) -> vs_20181212_models.BatchUnbindTemplatesResponse:
        """
        @param request: BatchUnbindTemplatesRequest
        @return: BatchUnbindTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_templates_with_options(request, runtime)

    async def batch_unbind_templates_async(
        self,
        request: vs_20181212_models.BatchUnbindTemplatesRequest,
    ) -> vs_20181212_models.BatchUnbindTemplatesResponse:
        """
        @param request: BatchUnbindTemplatesRequest
        @return: BatchUnbindTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_unbind_templates_with_options_async(request, runtime)

    def bind_directory_with_options(
        self,
        request: vs_20181212_models.BindDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BindDirectoryResponse:
        """
        @param request: BindDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BindDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_directory_with_options_async(
        self,
        request: vs_20181212_models.BindDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BindDirectoryResponse:
        """
        @param request: BindDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BindDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_directory(
        self,
        request: vs_20181212_models.BindDirectoryRequest,
    ) -> vs_20181212_models.BindDirectoryResponse:
        """
        @param request: BindDirectoryRequest
        @return: BindDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_directory_with_options(request, runtime)

    async def bind_directory_async(
        self,
        request: vs_20181212_models.BindDirectoryRequest,
    ) -> vs_20181212_models.BindDirectoryResponse:
        """
        @param request: BindDirectoryRequest
        @return: BindDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_directory_with_options_async(request, runtime)

    def bind_parent_platform_device_with_options(
        self,
        request: vs_20181212_models.BindParentPlatformDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BindParentPlatformDeviceResponse:
        """
        @param request: BindParentPlatformDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindParentPlatformDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindParentPlatformDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BindParentPlatformDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_parent_platform_device_with_options_async(
        self,
        request: vs_20181212_models.BindParentPlatformDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BindParentPlatformDeviceResponse:
        """
        @param request: BindParentPlatformDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindParentPlatformDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindParentPlatformDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BindParentPlatformDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_parent_platform_device(
        self,
        request: vs_20181212_models.BindParentPlatformDeviceRequest,
    ) -> vs_20181212_models.BindParentPlatformDeviceResponse:
        """
        @param request: BindParentPlatformDeviceRequest
        @return: BindParentPlatformDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_parent_platform_device_with_options(request, runtime)

    async def bind_parent_platform_device_async(
        self,
        request: vs_20181212_models.BindParentPlatformDeviceRequest,
    ) -> vs_20181212_models.BindParentPlatformDeviceResponse:
        """
        @param request: BindParentPlatformDeviceRequest
        @return: BindParentPlatformDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_parent_platform_device_with_options_async(request, runtime)

    def bind_purchased_device_with_options(
        self,
        request: vs_20181212_models.BindPurchasedDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BindPurchasedDeviceResponse:
        """
        @param request: BindPurchasedDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindPurchasedDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindPurchasedDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BindPurchasedDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_purchased_device_with_options_async(
        self,
        request: vs_20181212_models.BindPurchasedDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BindPurchasedDeviceResponse:
        """
        @param request: BindPurchasedDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindPurchasedDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindPurchasedDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BindPurchasedDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_purchased_device(
        self,
        request: vs_20181212_models.BindPurchasedDeviceRequest,
    ) -> vs_20181212_models.BindPurchasedDeviceResponse:
        """
        @param request: BindPurchasedDeviceRequest
        @return: BindPurchasedDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_purchased_device_with_options(request, runtime)

    async def bind_purchased_device_async(
        self,
        request: vs_20181212_models.BindPurchasedDeviceRequest,
    ) -> vs_20181212_models.BindPurchasedDeviceResponse:
        """
        @param request: BindPurchasedDeviceRequest
        @return: BindPurchasedDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_purchased_device_with_options_async(request, runtime)

    def bind_template_with_options(
        self,
        request: vs_20181212_models.BindTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BindTemplateResponse:
        """
        @param request: BindTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_all):
            query['ApplyAll'] = request.apply_all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.replace):
            query['Replace'] = request.replace
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BindTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_template_with_options_async(
        self,
        request: vs_20181212_models.BindTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.BindTemplateResponse:
        """
        @param request: BindTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_all):
            query['ApplyAll'] = request.apply_all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.replace):
            query['Replace'] = request.replace
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BindTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_template(
        self,
        request: vs_20181212_models.BindTemplateRequest,
    ) -> vs_20181212_models.BindTemplateResponse:
        """
        @param request: BindTemplateRequest
        @return: BindTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_template_with_options(request, runtime)

    async def bind_template_async(
        self,
        request: vs_20181212_models.BindTemplateRequest,
    ) -> vs_20181212_models.BindTemplateResponse:
        """
        @param request: BindTemplateRequest
        @return: BindTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_template_with_options_async(request, runtime)

    def continuous_adjust_with_options(
        self,
        request: vs_20181212_models.ContinuousAdjustRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ContinuousAdjustResponse:
        """
        @param request: ContinuousAdjustRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContinuousAdjustResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.focus):
            query['Focus'] = request.focus
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.iris):
            query['Iris'] = request.iris
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinuousAdjust',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ContinuousAdjustResponse(),
            self.call_api(params, req, runtime)
        )

    async def continuous_adjust_with_options_async(
        self,
        request: vs_20181212_models.ContinuousAdjustRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ContinuousAdjustResponse:
        """
        @param request: ContinuousAdjustRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContinuousAdjustResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.focus):
            query['Focus'] = request.focus
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.iris):
            query['Iris'] = request.iris
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinuousAdjust',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ContinuousAdjustResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continuous_adjust(
        self,
        request: vs_20181212_models.ContinuousAdjustRequest,
    ) -> vs_20181212_models.ContinuousAdjustResponse:
        """
        @param request: ContinuousAdjustRequest
        @return: ContinuousAdjustResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.continuous_adjust_with_options(request, runtime)

    async def continuous_adjust_async(
        self,
        request: vs_20181212_models.ContinuousAdjustRequest,
    ) -> vs_20181212_models.ContinuousAdjustResponse:
        """
        @param request: ContinuousAdjustRequest
        @return: ContinuousAdjustResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.continuous_adjust_with_options_async(request, runtime)

    def continuous_move_with_options(
        self,
        request: vs_20181212_models.ContinuousMoveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ContinuousMoveResponse:
        """
        @param request: ContinuousMoveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContinuousMoveResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pan):
            query['Pan'] = request.pan
        if not UtilClient.is_unset(request.tilt):
            query['Tilt'] = request.tilt
        if not UtilClient.is_unset(request.zoom):
            query['Zoom'] = request.zoom
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinuousMove',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ContinuousMoveResponse(),
            self.call_api(params, req, runtime)
        )

    async def continuous_move_with_options_async(
        self,
        request: vs_20181212_models.ContinuousMoveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ContinuousMoveResponse:
        """
        @param request: ContinuousMoveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContinuousMoveResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pan):
            query['Pan'] = request.pan
        if not UtilClient.is_unset(request.tilt):
            query['Tilt'] = request.tilt
        if not UtilClient.is_unset(request.zoom):
            query['Zoom'] = request.zoom
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinuousMove',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ContinuousMoveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continuous_move(
        self,
        request: vs_20181212_models.ContinuousMoveRequest,
    ) -> vs_20181212_models.ContinuousMoveResponse:
        """
        @param request: ContinuousMoveRequest
        @return: ContinuousMoveResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.continuous_move_with_options(request, runtime)

    async def continuous_move_async(
        self,
        request: vs_20181212_models.ContinuousMoveRequest,
    ) -> vs_20181212_models.ContinuousMoveResponse:
        """
        @param request: ContinuousMoveRequest
        @return: ContinuousMoveResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.continuous_move_with_options_async(request, runtime)

    def create_device_with_options(
        self,
        request: vs_20181212_models.CreateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateDeviceResponse:
        """
        @param request: CreateDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_method):
            query['AlarmMethod'] = request.alarm_method
        if not UtilClient.is_unset(request.auto_directory):
            query['AutoDirectory'] = request.auto_directory
        if not UtilClient.is_unset(request.auto_pos):
            query['AutoPos'] = request.auto_pos
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.dsn):
            query['Dsn'] = request.dsn
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.latitude):
            query['Latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            query['Longitude'] = request.longitude
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.pos_interval):
            query['PosInterval'] = request.pos_interval
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_device_with_options_async(
        self,
        request: vs_20181212_models.CreateDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateDeviceResponse:
        """
        @param request: CreateDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_method):
            query['AlarmMethod'] = request.alarm_method
        if not UtilClient.is_unset(request.auto_directory):
            query['AutoDirectory'] = request.auto_directory
        if not UtilClient.is_unset(request.auto_pos):
            query['AutoPos'] = request.auto_pos
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.dsn):
            query['Dsn'] = request.dsn
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.latitude):
            query['Latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            query['Longitude'] = request.longitude
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.pos_interval):
            query['PosInterval'] = request.pos_interval
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_device(
        self,
        request: vs_20181212_models.CreateDeviceRequest,
    ) -> vs_20181212_models.CreateDeviceResponse:
        """
        @param request: CreateDeviceRequest
        @return: CreateDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_device_with_options(request, runtime)

    async def create_device_async(
        self,
        request: vs_20181212_models.CreateDeviceRequest,
    ) -> vs_20181212_models.CreateDeviceResponse:
        """
        @param request: CreateDeviceRequest
        @return: CreateDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_device_with_options_async(request, runtime)

    def create_device_alarm_with_options(
        self,
        request: vs_20181212_models.CreateDeviceAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateDeviceAlarmResponse:
        """
        @param request: CreateDeviceAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeviceAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm):
            query['Alarm'] = request.alarm
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.expire):
            query['Expire'] = request.expire
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.sub_alarm):
            query['SubAlarm'] = request.sub_alarm
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDeviceAlarm',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateDeviceAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_device_alarm_with_options_async(
        self,
        request: vs_20181212_models.CreateDeviceAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateDeviceAlarmResponse:
        """
        @param request: CreateDeviceAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeviceAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm):
            query['Alarm'] = request.alarm
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.expire):
            query['Expire'] = request.expire
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.sub_alarm):
            query['SubAlarm'] = request.sub_alarm
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDeviceAlarm',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateDeviceAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_device_alarm(
        self,
        request: vs_20181212_models.CreateDeviceAlarmRequest,
    ) -> vs_20181212_models.CreateDeviceAlarmResponse:
        """
        @param request: CreateDeviceAlarmRequest
        @return: CreateDeviceAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_device_alarm_with_options(request, runtime)

    async def create_device_alarm_async(
        self,
        request: vs_20181212_models.CreateDeviceAlarmRequest,
    ) -> vs_20181212_models.CreateDeviceAlarmResponse:
        """
        @param request: CreateDeviceAlarmRequest
        @return: CreateDeviceAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_device_alarm_with_options_async(request, runtime)

    def create_directory_with_options(
        self,
        request: vs_20181212_models.CreateDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateDirectoryResponse:
        """
        @param request: CreateDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_directory_with_options_async(
        self,
        request: vs_20181212_models.CreateDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateDirectoryResponse:
        """
        @param request: CreateDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_directory(
        self,
        request: vs_20181212_models.CreateDirectoryRequest,
    ) -> vs_20181212_models.CreateDirectoryResponse:
        """
        @param request: CreateDirectoryRequest
        @return: CreateDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_directory_with_options(request, runtime)

    async def create_directory_async(
        self,
        request: vs_20181212_models.CreateDirectoryRequest,
    ) -> vs_20181212_models.CreateDirectoryResponse:
        """
        @param request: CreateDirectoryRequest
        @return: CreateDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_directory_with_options_async(request, runtime)

    def create_group_with_options(
        self,
        request: vs_20181212_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateGroupResponse:
        """
        @param request: CreateGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.in_protocol):
            query['InProtocol'] = request.in_protocol
        if not UtilClient.is_unset(request.lazy_pull):
            query['LazyPull'] = request.lazy_pull
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.push_domain):
            query['PushDomain'] = request.push_domain
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: vs_20181212_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateGroupResponse:
        """
        @param request: CreateGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.in_protocol):
            query['InProtocol'] = request.in_protocol
        if not UtilClient.is_unset(request.lazy_pull):
            query['LazyPull'] = request.lazy_pull
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.push_domain):
            query['PushDomain'] = request.push_domain
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group(
        self,
        request: vs_20181212_models.CreateGroupRequest,
    ) -> vs_20181212_models.CreateGroupResponse:
        """
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    async def create_group_async(
        self,
        request: vs_20181212_models.CreateGroupRequest,
    ) -> vs_20181212_models.CreateGroupResponse:
        """
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_group_with_options_async(request, runtime)

    def create_parent_platform_with_options(
        self,
        request: vs_20181212_models.CreateParentPlatformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateParentPlatformResponse:
        """
        @param request: CreateParentPlatformRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateParentPlatformResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.client_auth):
            query['ClientAuth'] = request.client_auth
        if not UtilClient.is_unset(request.client_password):
            query['ClientPassword'] = request.client_password
        if not UtilClient.is_unset(request.client_username):
            query['ClientUsername'] = request.client_username
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateParentPlatform',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateParentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_parent_platform_with_options_async(
        self,
        request: vs_20181212_models.CreateParentPlatformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateParentPlatformResponse:
        """
        @param request: CreateParentPlatformRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateParentPlatformResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.client_auth):
            query['ClientAuth'] = request.client_auth
        if not UtilClient.is_unset(request.client_password):
            query['ClientPassword'] = request.client_password
        if not UtilClient.is_unset(request.client_username):
            query['ClientUsername'] = request.client_username
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateParentPlatform',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateParentPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_parent_platform(
        self,
        request: vs_20181212_models.CreateParentPlatformRequest,
    ) -> vs_20181212_models.CreateParentPlatformResponse:
        """
        @param request: CreateParentPlatformRequest
        @return: CreateParentPlatformResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_parent_platform_with_options(request, runtime)

    async def create_parent_platform_async(
        self,
        request: vs_20181212_models.CreateParentPlatformRequest,
    ) -> vs_20181212_models.CreateParentPlatformResponse:
        """
        @param request: CreateParentPlatformRequest
        @return: CreateParentPlatformResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_parent_platform_with_options_async(request, runtime)

    def create_rendering_data_package_with_options(
        self,
        request: vs_20181212_models.CreateRenderingDataPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateRenderingDataPackageResponse:
        """
        @summary 创建云渲染数据包
        
        @param request: CreateRenderingDataPackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRenderingDataPackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRenderingDataPackage',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateRenderingDataPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rendering_data_package_with_options_async(
        self,
        request: vs_20181212_models.CreateRenderingDataPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateRenderingDataPackageResponse:
        """
        @summary 创建云渲染数据包
        
        @param request: CreateRenderingDataPackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRenderingDataPackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRenderingDataPackage',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateRenderingDataPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rendering_data_package(
        self,
        request: vs_20181212_models.CreateRenderingDataPackageRequest,
    ) -> vs_20181212_models.CreateRenderingDataPackageResponse:
        """
        @summary 创建云渲染数据包
        
        @param request: CreateRenderingDataPackageRequest
        @return: CreateRenderingDataPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_rendering_data_package_with_options(request, runtime)

    async def create_rendering_data_package_async(
        self,
        request: vs_20181212_models.CreateRenderingDataPackageRequest,
    ) -> vs_20181212_models.CreateRenderingDataPackageResponse:
        """
        @summary 创建云渲染数据包
        
        @param request: CreateRenderingDataPackageRequest
        @return: CreateRenderingDataPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_rendering_data_package_with_options_async(request, runtime)

    def create_rendering_instance_with_options(
        self,
        tmp_req: vs_20181212_models.CreateRenderingInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateRenderingInstanceResponse:
        """
        @summary 申请云渲染资源实例
        
        @param tmp_req: CreateRenderingInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRenderingInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.CreateRenderingInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_info):
            request.client_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_info, 'ClientInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.client_info_shrink):
            query['ClientInfo'] = request.client_info_shrink
        if not UtilClient.is_unset(request.instance_billing_cycle):
            query['InstanceBillingCycle'] = request.instance_billing_cycle
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth):
            query['InternetMaxBandwidth'] = request.internet_max_bandwidth
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.rendering_spec):
            query['RenderingSpec'] = request.rendering_spec
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRenderingInstance',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateRenderingInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rendering_instance_with_options_async(
        self,
        tmp_req: vs_20181212_models.CreateRenderingInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateRenderingInstanceResponse:
        """
        @summary 申请云渲染资源实例
        
        @param tmp_req: CreateRenderingInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRenderingInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.CreateRenderingInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_info):
            request.client_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_info, 'ClientInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.client_info_shrink):
            query['ClientInfo'] = request.client_info_shrink
        if not UtilClient.is_unset(request.instance_billing_cycle):
            query['InstanceBillingCycle'] = request.instance_billing_cycle
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth):
            query['InternetMaxBandwidth'] = request.internet_max_bandwidth
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.rendering_spec):
            query['RenderingSpec'] = request.rendering_spec
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRenderingInstance',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateRenderingInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rendering_instance(
        self,
        request: vs_20181212_models.CreateRenderingInstanceRequest,
    ) -> vs_20181212_models.CreateRenderingInstanceResponse:
        """
        @summary 申请云渲染资源实例
        
        @param request: CreateRenderingInstanceRequest
        @return: CreateRenderingInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_rendering_instance_with_options(request, runtime)

    async def create_rendering_instance_async(
        self,
        request: vs_20181212_models.CreateRenderingInstanceRequest,
    ) -> vs_20181212_models.CreateRenderingInstanceResponse:
        """
        @summary 申请云渲染资源实例
        
        @param request: CreateRenderingInstanceRequest
        @return: CreateRenderingInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_rendering_instance_with_options_async(request, runtime)

    def create_rendering_instance_gateway_with_options(
        self,
        request: vs_20181212_models.CreateRenderingInstanceGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateRenderingInstanceGatewayResponse:
        """
        @summary 创建自定义网关
        
        @param request: CreateRenderingInstanceGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRenderingInstanceGatewayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_instance_id):
            query['GatewayInstanceId'] = request.gateway_instance_id
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRenderingInstanceGateway',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateRenderingInstanceGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rendering_instance_gateway_with_options_async(
        self,
        request: vs_20181212_models.CreateRenderingInstanceGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateRenderingInstanceGatewayResponse:
        """
        @summary 创建自定义网关
        
        @param request: CreateRenderingInstanceGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRenderingInstanceGatewayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_instance_id):
            query['GatewayInstanceId'] = request.gateway_instance_id
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRenderingInstanceGateway',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateRenderingInstanceGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rendering_instance_gateway(
        self,
        request: vs_20181212_models.CreateRenderingInstanceGatewayRequest,
    ) -> vs_20181212_models.CreateRenderingInstanceGatewayResponse:
        """
        @summary 创建自定义网关
        
        @param request: CreateRenderingInstanceGatewayRequest
        @return: CreateRenderingInstanceGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_rendering_instance_gateway_with_options(request, runtime)

    async def create_rendering_instance_gateway_async(
        self,
        request: vs_20181212_models.CreateRenderingInstanceGatewayRequest,
    ) -> vs_20181212_models.CreateRenderingInstanceGatewayResponse:
        """
        @summary 创建自定义网关
        
        @param request: CreateRenderingInstanceGatewayRequest
        @return: CreateRenderingInstanceGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_rendering_instance_gateway_with_options_async(request, runtime)

    def create_rendering_project_with_options(
        self,
        tmp_req: vs_20181212_models.CreateRenderingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateRenderingProjectResponse:
        """
        @summary 创建一个新的云应用服务项目，并设置相关属性。
        
        @param tmp_req: CreateRenderingProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRenderingProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.CreateRenderingProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.session_attribs):
            request.session_attribs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.session_attribs, 'SessionAttribs', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.session_attribs_shrink):
            query['SessionAttribs'] = request.session_attribs_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRenderingProject',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateRenderingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rendering_project_with_options_async(
        self,
        tmp_req: vs_20181212_models.CreateRenderingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateRenderingProjectResponse:
        """
        @summary 创建一个新的云应用服务项目，并设置相关属性。
        
        @param tmp_req: CreateRenderingProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRenderingProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.CreateRenderingProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.session_attribs):
            request.session_attribs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.session_attribs, 'SessionAttribs', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.session_attribs_shrink):
            query['SessionAttribs'] = request.session_attribs_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRenderingProject',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateRenderingProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rendering_project(
        self,
        request: vs_20181212_models.CreateRenderingProjectRequest,
    ) -> vs_20181212_models.CreateRenderingProjectResponse:
        """
        @summary 创建一个新的云应用服务项目，并设置相关属性。
        
        @param request: CreateRenderingProjectRequest
        @return: CreateRenderingProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_rendering_project_with_options(request, runtime)

    async def create_rendering_project_async(
        self,
        request: vs_20181212_models.CreateRenderingProjectRequest,
    ) -> vs_20181212_models.CreateRenderingProjectResponse:
        """
        @summary 创建一个新的云应用服务项目，并设置相关属性。
        
        @param request: CreateRenderingProjectRequest
        @return: CreateRenderingProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_rendering_project_with_options_async(request, runtime)

    def create_stream_snapshot_with_options(
        self,
        request: vs_20181212_models.CreateStreamSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateStreamSnapshotResponse:
        """
        @param request: CreateStreamSnapshotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStreamSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.location):
            query['Location'] = request.location
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStreamSnapshot',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateStreamSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_stream_snapshot_with_options_async(
        self,
        request: vs_20181212_models.CreateStreamSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateStreamSnapshotResponse:
        """
        @param request: CreateStreamSnapshotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStreamSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.location):
            query['Location'] = request.location
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStreamSnapshot',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateStreamSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_stream_snapshot(
        self,
        request: vs_20181212_models.CreateStreamSnapshotRequest,
    ) -> vs_20181212_models.CreateStreamSnapshotResponse:
        """
        @param request: CreateStreamSnapshotRequest
        @return: CreateStreamSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_stream_snapshot_with_options(request, runtime)

    async def create_stream_snapshot_async(
        self,
        request: vs_20181212_models.CreateStreamSnapshotRequest,
    ) -> vs_20181212_models.CreateStreamSnapshotResponse:
        """
        @param request: CreateStreamSnapshotRequest
        @return: CreateStreamSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_stream_snapshot_with_options_async(request, runtime)

    def create_template_with_options(
        self,
        request: vs_20181212_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateTemplateResponse:
        """
        @param request: CreateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_format):
            query['FileFormat'] = request.file_format
        if not UtilClient.is_unset(request.flv):
            query['Flv'] = request.flv
        if not UtilClient.is_unset(request.hls_m3u_8):
            query['HlsM3u8'] = request.hls_m3u_8
        if not UtilClient.is_unset(request.hls_ts):
            query['HlsTs'] = request.hls_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.jpg_on_demand):
            query['JpgOnDemand'] = request.jpg_on_demand
        if not UtilClient.is_unset(request.jpg_overwrite):
            query['JpgOverwrite'] = request.jpg_overwrite
        if not UtilClient.is_unset(request.jpg_sequence):
            query['JpgSequence'] = request.jpg_sequence
        if not UtilClient.is_unset(request.mp_4):
            query['Mp4'] = request.mp_4
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.trans_configs_json):
            query['TransConfigsJSON'] = request.trans_configs_json
        if not UtilClient.is_unset(request.trigger):
            query['Trigger'] = request.trigger
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: vs_20181212_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.CreateTemplateResponse:
        """
        @param request: CreateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_format):
            query['FileFormat'] = request.file_format
        if not UtilClient.is_unset(request.flv):
            query['Flv'] = request.flv
        if not UtilClient.is_unset(request.hls_m3u_8):
            query['HlsM3u8'] = request.hls_m3u_8
        if not UtilClient.is_unset(request.hls_ts):
            query['HlsTs'] = request.hls_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.jpg_on_demand):
            query['JpgOnDemand'] = request.jpg_on_demand
        if not UtilClient.is_unset(request.jpg_overwrite):
            query['JpgOverwrite'] = request.jpg_overwrite
        if not UtilClient.is_unset(request.jpg_sequence):
            query['JpgSequence'] = request.jpg_sequence
        if not UtilClient.is_unset(request.mp_4):
            query['Mp4'] = request.mp_4
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.trans_configs_json):
            query['TransConfigsJSON'] = request.trans_configs_json
        if not UtilClient.is_unset(request.trigger):
            query['Trigger'] = request.trigger
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: vs_20181212_models.CreateTemplateRequest,
    ) -> vs_20181212_models.CreateTemplateResponse:
        """
        @param request: CreateTemplateRequest
        @return: CreateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    async def create_template_async(
        self,
        request: vs_20181212_models.CreateTemplateRequest,
    ) -> vs_20181212_models.CreateTemplateResponse:
        """
        @param request: CreateTemplateRequest
        @return: CreateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_template_with_options_async(request, runtime)

    def delete_cloud_app_with_options(
        self,
        request: vs_20181212_models.DeleteCloudAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteCloudAppResponse:
        """
        @summary 删除云应用
        
        @param request: DeleteCloudAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudApp',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteCloudAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_app_with_options_async(
        self,
        request: vs_20181212_models.DeleteCloudAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteCloudAppResponse:
        """
        @summary 删除云应用
        
        @param request: DeleteCloudAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCloudAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudApp',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteCloudAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_app(
        self,
        request: vs_20181212_models.DeleteCloudAppRequest,
    ) -> vs_20181212_models.DeleteCloudAppResponse:
        """
        @summary 删除云应用
        
        @param request: DeleteCloudAppRequest
        @return: DeleteCloudAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cloud_app_with_options(request, runtime)

    async def delete_cloud_app_async(
        self,
        request: vs_20181212_models.DeleteCloudAppRequest,
    ) -> vs_20181212_models.DeleteCloudAppResponse:
        """
        @summary 删除云应用
        
        @param request: DeleteCloudAppRequest
        @return: DeleteCloudAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cloud_app_with_options_async(request, runtime)

    def delete_device_with_options(
        self,
        request: vs_20181212_models.DeleteDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteDeviceResponse:
        """
        @param request: DeleteDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_device_with_options_async(
        self,
        request: vs_20181212_models.DeleteDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteDeviceResponse:
        """
        @param request: DeleteDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_device(
        self,
        request: vs_20181212_models.DeleteDeviceRequest,
    ) -> vs_20181212_models.DeleteDeviceResponse:
        """
        @param request: DeleteDeviceRequest
        @return: DeleteDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_device_with_options(request, runtime)

    async def delete_device_async(
        self,
        request: vs_20181212_models.DeleteDeviceRequest,
    ) -> vs_20181212_models.DeleteDeviceResponse:
        """
        @param request: DeleteDeviceRequest
        @return: DeleteDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_device_with_options_async(request, runtime)

    def delete_directory_with_options(
        self,
        request: vs_20181212_models.DeleteDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteDirectoryResponse:
        """
        @param request: DeleteDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_directory_with_options_async(
        self,
        request: vs_20181212_models.DeleteDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteDirectoryResponse:
        """
        @param request: DeleteDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_directory(
        self,
        request: vs_20181212_models.DeleteDirectoryRequest,
    ) -> vs_20181212_models.DeleteDirectoryResponse:
        """
        @param request: DeleteDirectoryRequest
        @return: DeleteDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_directory_with_options(request, runtime)

    async def delete_directory_async(
        self,
        request: vs_20181212_models.DeleteDirectoryRequest,
    ) -> vs_20181212_models.DeleteDirectoryResponse:
        """
        @param request: DeleteDirectoryRequest
        @return: DeleteDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_directory_with_options_async(request, runtime)

    def delete_file_with_options(
        self,
        request: vs_20181212_models.DeleteFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteFileResponse:
        """
        @summary 删除文件对象。
        
        @param request: DeleteFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_with_options_async(
        self,
        request: vs_20181212_models.DeleteFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteFileResponse:
        """
        @summary 删除文件对象。
        
        @param request: DeleteFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFile',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_file(
        self,
        request: vs_20181212_models.DeleteFileRequest,
    ) -> vs_20181212_models.DeleteFileResponse:
        """
        @summary 删除文件对象。
        
        @param request: DeleteFileRequest
        @return: DeleteFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_file_with_options(request, runtime)

    async def delete_file_async(
        self,
        request: vs_20181212_models.DeleteFileRequest,
    ) -> vs_20181212_models.DeleteFileResponse:
        """
        @summary 删除文件对象。
        
        @param request: DeleteFileRequest
        @return: DeleteFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_file_with_options_async(request, runtime)

    def delete_group_with_options(
        self,
        request: vs_20181212_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteGroupResponse:
        """
        @param request: DeleteGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        request: vs_20181212_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteGroupResponse:
        """
        @param request: DeleteGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group(
        self,
        request: vs_20181212_models.DeleteGroupRequest,
    ) -> vs_20181212_models.DeleteGroupResponse:
        """
        @param request: DeleteGroupRequest
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    async def delete_group_async(
        self,
        request: vs_20181212_models.DeleteGroupRequest,
    ) -> vs_20181212_models.DeleteGroupResponse:
        """
        @param request: DeleteGroupRequest
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_with_options_async(request, runtime)

    def delete_parent_platform_with_options(
        self,
        request: vs_20181212_models.DeleteParentPlatformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteParentPlatformResponse:
        """
        @param request: DeleteParentPlatformRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteParentPlatformResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteParentPlatform',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteParentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_parent_platform_with_options_async(
        self,
        request: vs_20181212_models.DeleteParentPlatformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteParentPlatformResponse:
        """
        @param request: DeleteParentPlatformRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteParentPlatformResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteParentPlatform',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteParentPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_parent_platform(
        self,
        request: vs_20181212_models.DeleteParentPlatformRequest,
    ) -> vs_20181212_models.DeleteParentPlatformResponse:
        """
        @param request: DeleteParentPlatformRequest
        @return: DeleteParentPlatformResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_parent_platform_with_options(request, runtime)

    async def delete_parent_platform_async(
        self,
        request: vs_20181212_models.DeleteParentPlatformRequest,
    ) -> vs_20181212_models.DeleteParentPlatformResponse:
        """
        @param request: DeleteParentPlatformRequest
        @return: DeleteParentPlatformResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_parent_platform_with_options_async(request, runtime)

    def delete_preset_with_options(
        self,
        request: vs_20181212_models.DeletePresetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeletePresetResponse:
        """
        @param request: DeletePresetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePresetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preset_id):
            query['PresetId'] = request.preset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePreset',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeletePresetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_preset_with_options_async(
        self,
        request: vs_20181212_models.DeletePresetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeletePresetResponse:
        """
        @param request: DeletePresetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePresetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preset_id):
            query['PresetId'] = request.preset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePreset',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeletePresetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_preset(
        self,
        request: vs_20181212_models.DeletePresetRequest,
    ) -> vs_20181212_models.DeletePresetResponse:
        """
        @param request: DeletePresetRequest
        @return: DeletePresetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_preset_with_options(request, runtime)

    async def delete_preset_async(
        self,
        request: vs_20181212_models.DeletePresetRequest,
    ) -> vs_20181212_models.DeletePresetResponse:
        """
        @param request: DeletePresetRequest
        @return: DeletePresetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_preset_with_options_async(request, runtime)

    def delete_public_key_with_options(
        self,
        request: vs_20181212_models.DeletePublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeletePublicKeyResponse:
        """
        @summary 删除公钥信息
        
        @param request: DeletePublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePublicKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_name):
            query['KeyName'] = request.key_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePublicKey',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeletePublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_public_key_with_options_async(
        self,
        request: vs_20181212_models.DeletePublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeletePublicKeyResponse:
        """
        @summary 删除公钥信息
        
        @param request: DeletePublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePublicKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_name):
            query['KeyName'] = request.key_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePublicKey',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeletePublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_public_key(
        self,
        request: vs_20181212_models.DeletePublicKeyRequest,
    ) -> vs_20181212_models.DeletePublicKeyResponse:
        """
        @summary 删除公钥信息
        
        @param request: DeletePublicKeyRequest
        @return: DeletePublicKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_public_key_with_options(request, runtime)

    async def delete_public_key_async(
        self,
        request: vs_20181212_models.DeletePublicKeyRequest,
    ) -> vs_20181212_models.DeletePublicKeyResponse:
        """
        @summary 删除公钥信息
        
        @param request: DeletePublicKeyRequest
        @return: DeletePublicKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_public_key_with_options_async(request, runtime)

    def delete_rendering_instance_configuration_with_options(
        self,
        tmp_req: vs_20181212_models.DeleteRenderingInstanceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteRenderingInstanceConfigurationResponse:
        """
        @summary 删除云渲染实例配置参数
        
        @param tmp_req: DeleteRenderingInstanceConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRenderingInstanceConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.DeleteRenderingInstanceConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configuration):
            request.configuration_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        body = {}
        if not UtilClient.is_unset(request.configuration_shrink):
            body['Configuration'] = request.configuration_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRenderingInstanceConfiguration',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteRenderingInstanceConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rendering_instance_configuration_with_options_async(
        self,
        tmp_req: vs_20181212_models.DeleteRenderingInstanceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteRenderingInstanceConfigurationResponse:
        """
        @summary 删除云渲染实例配置参数
        
        @param tmp_req: DeleteRenderingInstanceConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRenderingInstanceConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.DeleteRenderingInstanceConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configuration):
            request.configuration_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        body = {}
        if not UtilClient.is_unset(request.configuration_shrink):
            body['Configuration'] = request.configuration_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRenderingInstanceConfiguration',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteRenderingInstanceConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rendering_instance_configuration(
        self,
        request: vs_20181212_models.DeleteRenderingInstanceConfigurationRequest,
    ) -> vs_20181212_models.DeleteRenderingInstanceConfigurationResponse:
        """
        @summary 删除云渲染实例配置参数
        
        @param request: DeleteRenderingInstanceConfigurationRequest
        @return: DeleteRenderingInstanceConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_rendering_instance_configuration_with_options(request, runtime)

    async def delete_rendering_instance_configuration_async(
        self,
        request: vs_20181212_models.DeleteRenderingInstanceConfigurationRequest,
    ) -> vs_20181212_models.DeleteRenderingInstanceConfigurationResponse:
        """
        @summary 删除云渲染实例配置参数
        
        @param request: DeleteRenderingInstanceConfigurationRequest
        @return: DeleteRenderingInstanceConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_rendering_instance_configuration_with_options_async(request, runtime)

    def delete_rendering_instance_gateway_with_options(
        self,
        request: vs_20181212_models.DeleteRenderingInstanceGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteRenderingInstanceGatewayResponse:
        """
        @summary 删除自定义网关
        
        @param request: DeleteRenderingInstanceGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRenderingInstanceGatewayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRenderingInstanceGateway',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteRenderingInstanceGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rendering_instance_gateway_with_options_async(
        self,
        request: vs_20181212_models.DeleteRenderingInstanceGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteRenderingInstanceGatewayResponse:
        """
        @summary 删除自定义网关
        
        @param request: DeleteRenderingInstanceGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRenderingInstanceGatewayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRenderingInstanceGateway',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteRenderingInstanceGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rendering_instance_gateway(
        self,
        request: vs_20181212_models.DeleteRenderingInstanceGatewayRequest,
    ) -> vs_20181212_models.DeleteRenderingInstanceGatewayResponse:
        """
        @summary 删除自定义网关
        
        @param request: DeleteRenderingInstanceGatewayRequest
        @return: DeleteRenderingInstanceGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_rendering_instance_gateway_with_options(request, runtime)

    async def delete_rendering_instance_gateway_async(
        self,
        request: vs_20181212_models.DeleteRenderingInstanceGatewayRequest,
    ) -> vs_20181212_models.DeleteRenderingInstanceGatewayResponse:
        """
        @summary 删除自定义网关
        
        @param request: DeleteRenderingInstanceGatewayRequest
        @return: DeleteRenderingInstanceGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_rendering_instance_gateway_with_options_async(request, runtime)

    def delete_rendering_instance_settings_with_options(
        self,
        tmp_req: vs_20181212_models.DeleteRenderingInstanceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteRenderingInstanceSettingsResponse:
        """
        @summary 清除实例设置
        
        @param tmp_req: DeleteRenderingInstanceSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRenderingInstanceSettingsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.DeleteRenderingInstanceSettingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attribute_names):
            request.attribute_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attribute_names, 'AttributeNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.attribute_names_shrink):
            query['AttributeNames'] = request.attribute_names_shrink
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRenderingInstanceSettings',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteRenderingInstanceSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rendering_instance_settings_with_options_async(
        self,
        tmp_req: vs_20181212_models.DeleteRenderingInstanceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteRenderingInstanceSettingsResponse:
        """
        @summary 清除实例设置
        
        @param tmp_req: DeleteRenderingInstanceSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRenderingInstanceSettingsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.DeleteRenderingInstanceSettingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attribute_names):
            request.attribute_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attribute_names, 'AttributeNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.attribute_names_shrink):
            query['AttributeNames'] = request.attribute_names_shrink
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRenderingInstanceSettings',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteRenderingInstanceSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rendering_instance_settings(
        self,
        request: vs_20181212_models.DeleteRenderingInstanceSettingsRequest,
    ) -> vs_20181212_models.DeleteRenderingInstanceSettingsResponse:
        """
        @summary 清除实例设置
        
        @param request: DeleteRenderingInstanceSettingsRequest
        @return: DeleteRenderingInstanceSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_rendering_instance_settings_with_options(request, runtime)

    async def delete_rendering_instance_settings_async(
        self,
        request: vs_20181212_models.DeleteRenderingInstanceSettingsRequest,
    ) -> vs_20181212_models.DeleteRenderingInstanceSettingsResponse:
        """
        @summary 清除实例设置
        
        @param request: DeleteRenderingInstanceSettingsRequest
        @return: DeleteRenderingInstanceSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_rendering_instance_settings_with_options_async(request, runtime)

    def delete_rendering_project_with_options(
        self,
        request: vs_20181212_models.DeleteRenderingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteRenderingProjectResponse:
        """
        @summary 删除一个云应用服务项目，有在线会话等业务调度数据的项目不允许删除。
        
        @param request: DeleteRenderingProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRenderingProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRenderingProject',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteRenderingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rendering_project_with_options_async(
        self,
        request: vs_20181212_models.DeleteRenderingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteRenderingProjectResponse:
        """
        @summary 删除一个云应用服务项目，有在线会话等业务调度数据的项目不允许删除。
        
        @param request: DeleteRenderingProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRenderingProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRenderingProject',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteRenderingProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rendering_project(
        self,
        request: vs_20181212_models.DeleteRenderingProjectRequest,
    ) -> vs_20181212_models.DeleteRenderingProjectResponse:
        """
        @summary 删除一个云应用服务项目，有在线会话等业务调度数据的项目不允许删除。
        
        @param request: DeleteRenderingProjectRequest
        @return: DeleteRenderingProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_rendering_project_with_options(request, runtime)

    async def delete_rendering_project_async(
        self,
        request: vs_20181212_models.DeleteRenderingProjectRequest,
    ) -> vs_20181212_models.DeleteRenderingProjectResponse:
        """
        @summary 删除一个云应用服务项目，有在线会话等业务调度数据的项目不允许删除。
        
        @param request: DeleteRenderingProjectRequest
        @return: DeleteRenderingProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_rendering_project_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: vs_20181212_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteTemplateResponse:
        """
        @param request: DeleteTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: vs_20181212_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteTemplateResponse:
        """
        @param request: DeleteTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        request: vs_20181212_models.DeleteTemplateRequest,
    ) -> vs_20181212_models.DeleteTemplateResponse:
        """
        @param request: DeleteTemplateRequest
        @return: DeleteTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: vs_20181212_models.DeleteTemplateRequest,
    ) -> vs_20181212_models.DeleteTemplateResponse:
        """
        @param request: DeleteTemplateRequest
        @return: DeleteTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def delete_vs_pull_stream_info_config_with_options(
        self,
        request: vs_20181212_models.DeleteVsPullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteVsPullStreamInfoConfigResponse:
        """
        @param request: DeleteVsPullStreamInfoConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVsPullStreamInfoConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVsPullStreamInfoConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteVsPullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vs_pull_stream_info_config_with_options_async(
        self,
        request: vs_20181212_models.DeleteVsPullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteVsPullStreamInfoConfigResponse:
        """
        @param request: DeleteVsPullStreamInfoConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVsPullStreamInfoConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVsPullStreamInfoConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteVsPullStreamInfoConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vs_pull_stream_info_config(
        self,
        request: vs_20181212_models.DeleteVsPullStreamInfoConfigRequest,
    ) -> vs_20181212_models.DeleteVsPullStreamInfoConfigResponse:
        """
        @param request: DeleteVsPullStreamInfoConfigRequest
        @return: DeleteVsPullStreamInfoConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vs_pull_stream_info_config_with_options(request, runtime)

    async def delete_vs_pull_stream_info_config_async(
        self,
        request: vs_20181212_models.DeleteVsPullStreamInfoConfigRequest,
    ) -> vs_20181212_models.DeleteVsPullStreamInfoConfigResponse:
        """
        @param request: DeleteVsPullStreamInfoConfigRequest
        @return: DeleteVsPullStreamInfoConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_vs_pull_stream_info_config_with_options_async(request, runtime)

    def delete_vs_streams_notify_url_config_with_options(
        self,
        request: vs_20181212_models.DeleteVsStreamsNotifyUrlConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteVsStreamsNotifyUrlConfigResponse:
        """
        @param request: DeleteVsStreamsNotifyUrlConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVsStreamsNotifyUrlConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVsStreamsNotifyUrlConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteVsStreamsNotifyUrlConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vs_streams_notify_url_config_with_options_async(
        self,
        request: vs_20181212_models.DeleteVsStreamsNotifyUrlConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DeleteVsStreamsNotifyUrlConfigResponse:
        """
        @param request: DeleteVsStreamsNotifyUrlConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVsStreamsNotifyUrlConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVsStreamsNotifyUrlConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteVsStreamsNotifyUrlConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vs_streams_notify_url_config(
        self,
        request: vs_20181212_models.DeleteVsStreamsNotifyUrlConfigRequest,
    ) -> vs_20181212_models.DeleteVsStreamsNotifyUrlConfigResponse:
        """
        @param request: DeleteVsStreamsNotifyUrlConfigRequest
        @return: DeleteVsStreamsNotifyUrlConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vs_streams_notify_url_config_with_options(request, runtime)

    async def delete_vs_streams_notify_url_config_async(
        self,
        request: vs_20181212_models.DeleteVsStreamsNotifyUrlConfigRequest,
    ) -> vs_20181212_models.DeleteVsStreamsNotifyUrlConfigResponse:
        """
        @param request: DeleteVsStreamsNotifyUrlConfigRequest
        @return: DeleteVsStreamsNotifyUrlConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_vs_streams_notify_url_config_with_options_async(request, runtime)

    def describe_account_stat_with_options(
        self,
        request: vs_20181212_models.DescribeAccountStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeAccountStatResponse:
        """
        @param request: DescribeAccountStatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountStatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountStat',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeAccountStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_stat_with_options_async(
        self,
        request: vs_20181212_models.DescribeAccountStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeAccountStatResponse:
        """
        @param request: DescribeAccountStatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountStatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountStat',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeAccountStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_stat(
        self,
        request: vs_20181212_models.DescribeAccountStatRequest,
    ) -> vs_20181212_models.DescribeAccountStatResponse:
        """
        @param request: DescribeAccountStatRequest
        @return: DescribeAccountStatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_account_stat_with_options(request, runtime)

    async def describe_account_stat_async(
        self,
        request: vs_20181212_models.DescribeAccountStatRequest,
    ) -> vs_20181212_models.DescribeAccountStatResponse:
        """
        @param request: DescribeAccountStatRequest
        @return: DescribeAccountStatResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_stat_with_options_async(request, runtime)

    def describe_device_with_options(
        self,
        request: vs_20181212_models.DescribeDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeDeviceResponse:
        """
        @param request: DescribeDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.include_directory):
            query['IncludeDirectory'] = request.include_directory
        if not UtilClient.is_unset(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_device_with_options_async(
        self,
        request: vs_20181212_models.DescribeDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeDeviceResponse:
        """
        @param request: DescribeDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.include_directory):
            query['IncludeDirectory'] = request.include_directory
        if not UtilClient.is_unset(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_device(
        self,
        request: vs_20181212_models.DescribeDeviceRequest,
    ) -> vs_20181212_models.DescribeDeviceResponse:
        """
        @param request: DescribeDeviceRequest
        @return: DescribeDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_device_with_options(request, runtime)

    async def describe_device_async(
        self,
        request: vs_20181212_models.DescribeDeviceRequest,
    ) -> vs_20181212_models.DescribeDeviceResponse:
        """
        @param request: DescribeDeviceRequest
        @return: DescribeDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_with_options_async(request, runtime)

    def describe_device_channels_with_options(
        self,
        request: vs_20181212_models.DescribeDeviceChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeDeviceChannelsResponse:
        """
        @param request: DescribeDeviceChannelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeviceChannelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeviceChannels',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDeviceChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_device_channels_with_options_async(
        self,
        request: vs_20181212_models.DescribeDeviceChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeDeviceChannelsResponse:
        """
        @param request: DescribeDeviceChannelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeviceChannelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeviceChannels',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDeviceChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_device_channels(
        self,
        request: vs_20181212_models.DescribeDeviceChannelsRequest,
    ) -> vs_20181212_models.DescribeDeviceChannelsResponse:
        """
        @param request: DescribeDeviceChannelsRequest
        @return: DescribeDeviceChannelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_device_channels_with_options(request, runtime)

    async def describe_device_channels_async(
        self,
        request: vs_20181212_models.DescribeDeviceChannelsRequest,
    ) -> vs_20181212_models.DescribeDeviceChannelsResponse:
        """
        @param request: DescribeDeviceChannelsRequest
        @return: DescribeDeviceChannelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_channels_with_options_async(request, runtime)

    def describe_device_gateway_with_options(
        self,
        request: vs_20181212_models.DescribeDeviceGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeDeviceGatewayResponse:
        """
        @param request: DescribeDeviceGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeviceGatewayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.expire):
            query['Expire'] = request.expire
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeviceGateway',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDeviceGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_device_gateway_with_options_async(
        self,
        request: vs_20181212_models.DescribeDeviceGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeDeviceGatewayResponse:
        """
        @param request: DescribeDeviceGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeviceGatewayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.expire):
            query['Expire'] = request.expire
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeviceGateway',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDeviceGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_device_gateway(
        self,
        request: vs_20181212_models.DescribeDeviceGatewayRequest,
    ) -> vs_20181212_models.DescribeDeviceGatewayResponse:
        """
        @param request: DescribeDeviceGatewayRequest
        @return: DescribeDeviceGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_device_gateway_with_options(request, runtime)

    async def describe_device_gateway_async(
        self,
        request: vs_20181212_models.DescribeDeviceGatewayRequest,
    ) -> vs_20181212_models.DescribeDeviceGatewayResponse:
        """
        @param request: DescribeDeviceGatewayRequest
        @return: DescribeDeviceGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_gateway_with_options_async(request, runtime)

    def describe_device_urlwith_options(
        self,
        request: vs_20181212_models.DescribeDeviceURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeDeviceURLResponse:
        """
        @param request: DescribeDeviceURLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeviceURLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth):
            query['Auth'] = request.auth
        if not UtilClient.is_unset(request.expire):
            query['Expire'] = request.expire
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeviceURL',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDeviceURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_device_urlwith_options_async(
        self,
        request: vs_20181212_models.DescribeDeviceURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeDeviceURLResponse:
        """
        @param request: DescribeDeviceURLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeviceURLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth):
            query['Auth'] = request.auth
        if not UtilClient.is_unset(request.expire):
            query['Expire'] = request.expire
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeviceURL',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDeviceURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_device_url(
        self,
        request: vs_20181212_models.DescribeDeviceURLRequest,
    ) -> vs_20181212_models.DescribeDeviceURLResponse:
        """
        @param request: DescribeDeviceURLRequest
        @return: DescribeDeviceURLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_device_urlwith_options(request, runtime)

    async def describe_device_url_async(
        self,
        request: vs_20181212_models.DescribeDeviceURLRequest,
    ) -> vs_20181212_models.DescribeDeviceURLResponse:
        """
        @param request: DescribeDeviceURLRequest
        @return: DescribeDeviceURLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_urlwith_options_async(request, runtime)

    def describe_devices_with_options(
        self,
        request: vs_20181212_models.DescribeDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeDevicesResponse:
        """
        @param request: DescribeDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.dsn):
            query['Dsn'] = request.dsn
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.include_directory):
            query['IncludeDirectory'] = request.include_directory
        if not UtilClient.is_unset(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_devices_with_options_async(
        self,
        request: vs_20181212_models.DescribeDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeDevicesResponse:
        """
        @param request: DescribeDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.dsn):
            query['Dsn'] = request.dsn
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.include_directory):
            query['IncludeDirectory'] = request.include_directory
        if not UtilClient.is_unset(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_devices(
        self,
        request: vs_20181212_models.DescribeDevicesRequest,
    ) -> vs_20181212_models.DescribeDevicesResponse:
        """
        @param request: DescribeDevicesRequest
        @return: DescribeDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_devices_with_options(request, runtime)

    async def describe_devices_async(
        self,
        request: vs_20181212_models.DescribeDevicesRequest,
    ) -> vs_20181212_models.DescribeDevicesResponse:
        """
        @param request: DescribeDevicesRequest
        @return: DescribeDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_devices_with_options_async(request, runtime)

    def describe_directories_with_options(
        self,
        request: vs_20181212_models.DescribeDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeDirectoriesResponse:
        """
        @param request: DescribeDirectoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.no_pagination):
            query['NoPagination'] = request.no_pagination
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDirectories',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_directories_with_options_async(
        self,
        request: vs_20181212_models.DescribeDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeDirectoriesResponse:
        """
        @param request: DescribeDirectoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.no_pagination):
            query['NoPagination'] = request.no_pagination
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDirectories',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_directories(
        self,
        request: vs_20181212_models.DescribeDirectoriesRequest,
    ) -> vs_20181212_models.DescribeDirectoriesResponse:
        """
        @param request: DescribeDirectoriesRequest
        @return: DescribeDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_directories_with_options(request, runtime)

    async def describe_directories_async(
        self,
        request: vs_20181212_models.DescribeDirectoriesRequest,
    ) -> vs_20181212_models.DescribeDirectoriesResponse:
        """
        @param request: DescribeDirectoriesRequest
        @return: DescribeDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_directories_with_options_async(request, runtime)

    def describe_directory_with_options(
        self,
        request: vs_20181212_models.DescribeDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeDirectoryResponse:
        """
        @param request: DescribeDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_directory_with_options_async(
        self,
        request: vs_20181212_models.DescribeDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeDirectoryResponse:
        """
        @param request: DescribeDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_directory(
        self,
        request: vs_20181212_models.DescribeDirectoryRequest,
    ) -> vs_20181212_models.DescribeDirectoryResponse:
        """
        @param request: DescribeDirectoryRequest
        @return: DescribeDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_directory_with_options(request, runtime)

    async def describe_directory_async(
        self,
        request: vs_20181212_models.DescribeDirectoryRequest,
    ) -> vs_20181212_models.DescribeDirectoryResponse:
        """
        @param request: DescribeDirectoryRequest
        @return: DescribeDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_directory_with_options_async(request, runtime)

    def describe_group_with_options(
        self,
        request: vs_20181212_models.DescribeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeGroupResponse:
        """
        @param request: DescribeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroup',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_with_options_async(
        self,
        request: vs_20181212_models.DescribeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeGroupResponse:
        """
        @param request: DescribeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroup',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group(
        self,
        request: vs_20181212_models.DescribeGroupRequest,
    ) -> vs_20181212_models.DescribeGroupResponse:
        """
        @param request: DescribeGroupRequest
        @return: DescribeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_group_with_options(request, runtime)

    async def describe_group_async(
        self,
        request: vs_20181212_models.DescribeGroupRequest,
    ) -> vs_20181212_models.DescribeGroupResponse:
        """
        @param request: DescribeGroupRequest
        @return: DescribeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_group_with_options_async(request, runtime)

    def describe_groups_with_options(
        self,
        request: vs_20181212_models.DescribeGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeGroupsResponse:
        """
        @param request: DescribeGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.in_protocol):
            query['InProtocol'] = request.in_protocol
        if not UtilClient.is_unset(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroups',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_groups_with_options_async(
        self,
        request: vs_20181212_models.DescribeGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeGroupsResponse:
        """
        @param request: DescribeGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.in_protocol):
            query['InProtocol'] = request.in_protocol
        if not UtilClient.is_unset(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroups',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_groups(
        self,
        request: vs_20181212_models.DescribeGroupsRequest,
    ) -> vs_20181212_models.DescribeGroupsResponse:
        """
        @param request: DescribeGroupsRequest
        @return: DescribeGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_groups_with_options(request, runtime)

    async def describe_groups_async(
        self,
        request: vs_20181212_models.DescribeGroupsRequest,
    ) -> vs_20181212_models.DescribeGroupsResponse:
        """
        @param request: DescribeGroupsRequest
        @return: DescribeGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_groups_with_options_async(request, runtime)

    def describe_parent_platform_with_options(
        self,
        request: vs_20181212_models.DescribeParentPlatformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeParentPlatformResponse:
        """
        @param request: DescribeParentPlatformRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParentPlatformResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParentPlatform',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeParentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parent_platform_with_options_async(
        self,
        request: vs_20181212_models.DescribeParentPlatformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeParentPlatformResponse:
        """
        @param request: DescribeParentPlatformRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParentPlatformResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParentPlatform',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeParentPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parent_platform(
        self,
        request: vs_20181212_models.DescribeParentPlatformRequest,
    ) -> vs_20181212_models.DescribeParentPlatformResponse:
        """
        @param request: DescribeParentPlatformRequest
        @return: DescribeParentPlatformResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parent_platform_with_options(request, runtime)

    async def describe_parent_platform_async(
        self,
        request: vs_20181212_models.DescribeParentPlatformRequest,
    ) -> vs_20181212_models.DescribeParentPlatformResponse:
        """
        @param request: DescribeParentPlatformRequest
        @return: DescribeParentPlatformResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parent_platform_with_options_async(request, runtime)

    def describe_parent_platform_devices_with_options(
        self,
        request: vs_20181212_models.DescribeParentPlatformDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeParentPlatformDevicesResponse:
        """
        @param request: DescribeParentPlatformDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParentPlatformDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParentPlatformDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeParentPlatformDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parent_platform_devices_with_options_async(
        self,
        request: vs_20181212_models.DescribeParentPlatformDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeParentPlatformDevicesResponse:
        """
        @param request: DescribeParentPlatformDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParentPlatformDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParentPlatformDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeParentPlatformDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parent_platform_devices(
        self,
        request: vs_20181212_models.DescribeParentPlatformDevicesRequest,
    ) -> vs_20181212_models.DescribeParentPlatformDevicesResponse:
        """
        @param request: DescribeParentPlatformDevicesRequest
        @return: DescribeParentPlatformDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parent_platform_devices_with_options(request, runtime)

    async def describe_parent_platform_devices_async(
        self,
        request: vs_20181212_models.DescribeParentPlatformDevicesRequest,
    ) -> vs_20181212_models.DescribeParentPlatformDevicesResponse:
        """
        @param request: DescribeParentPlatformDevicesRequest
        @return: DescribeParentPlatformDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parent_platform_devices_with_options_async(request, runtime)

    def describe_parent_platforms_with_options(
        self,
        request: vs_20181212_models.DescribeParentPlatformsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeParentPlatformsResponse:
        """
        @param request: DescribeParentPlatformsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParentPlatformsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParentPlatforms',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeParentPlatformsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parent_platforms_with_options_async(
        self,
        request: vs_20181212_models.DescribeParentPlatformsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeParentPlatformsResponse:
        """
        @param request: DescribeParentPlatformsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeParentPlatformsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParentPlatforms',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeParentPlatformsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parent_platforms(
        self,
        request: vs_20181212_models.DescribeParentPlatformsRequest,
    ) -> vs_20181212_models.DescribeParentPlatformsResponse:
        """
        @param request: DescribeParentPlatformsRequest
        @return: DescribeParentPlatformsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_parent_platforms_with_options(request, runtime)

    async def describe_parent_platforms_async(
        self,
        request: vs_20181212_models.DescribeParentPlatformsRequest,
    ) -> vs_20181212_models.DescribeParentPlatformsResponse:
        """
        @param request: DescribeParentPlatformsRequest
        @return: DescribeParentPlatformsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_parent_platforms_with_options_async(request, runtime)

    def describe_presets_with_options(
        self,
        request: vs_20181212_models.DescribePresetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribePresetsResponse:
        """
        @param request: DescribePresetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePresetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePresets',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribePresetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_presets_with_options_async(
        self,
        request: vs_20181212_models.DescribePresetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribePresetsResponse:
        """
        @param request: DescribePresetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePresetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePresets',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribePresetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_presets(
        self,
        request: vs_20181212_models.DescribePresetsRequest,
    ) -> vs_20181212_models.DescribePresetsResponse:
        """
        @param request: DescribePresetsRequest
        @return: DescribePresetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_presets_with_options(request, runtime)

    async def describe_presets_async(
        self,
        request: vs_20181212_models.DescribePresetsRequest,
    ) -> vs_20181212_models.DescribePresetsResponse:
        """
        @param request: DescribePresetsRequest
        @return: DescribePresetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_presets_with_options_async(request, runtime)

    def describe_publish_stream_status_with_options(
        self,
        request: vs_20181212_models.DescribePublishStreamStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribePublishStreamStatusResponse:
        """
        @param request: DescribePublishStreamStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePublishStreamStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePublishStreamStatus',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribePublishStreamStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_publish_stream_status_with_options_async(
        self,
        request: vs_20181212_models.DescribePublishStreamStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribePublishStreamStatusResponse:
        """
        @param request: DescribePublishStreamStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePublishStreamStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePublishStreamStatus',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribePublishStreamStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_publish_stream_status(
        self,
        request: vs_20181212_models.DescribePublishStreamStatusRequest,
    ) -> vs_20181212_models.DescribePublishStreamStatusResponse:
        """
        @param request: DescribePublishStreamStatusRequest
        @return: DescribePublishStreamStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_publish_stream_status_with_options(request, runtime)

    async def describe_publish_stream_status_async(
        self,
        request: vs_20181212_models.DescribePublishStreamStatusRequest,
    ) -> vs_20181212_models.DescribePublishStreamStatusResponse:
        """
        @param request: DescribePublishStreamStatusRequest
        @return: DescribePublishStreamStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_publish_stream_status_with_options_async(request, runtime)

    def describe_purchased_device_with_options(
        self,
        request: vs_20181212_models.DescribePurchasedDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribePurchasedDeviceResponse:
        """
        @param request: DescribePurchasedDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePurchasedDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribePurchasedDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_device_with_options_async(
        self,
        request: vs_20181212_models.DescribePurchasedDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribePurchasedDeviceResponse:
        """
        @param request: DescribePurchasedDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePurchasedDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribePurchasedDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_device(
        self,
        request: vs_20181212_models.DescribePurchasedDeviceRequest,
    ) -> vs_20181212_models.DescribePurchasedDeviceResponse:
        """
        @param request: DescribePurchasedDeviceRequest
        @return: DescribePurchasedDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_device_with_options(request, runtime)

    async def describe_purchased_device_async(
        self,
        request: vs_20181212_models.DescribePurchasedDeviceRequest,
    ) -> vs_20181212_models.DescribePurchasedDeviceResponse:
        """
        @param request: DescribePurchasedDeviceRequest
        @return: DescribePurchasedDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_purchased_device_with_options_async(request, runtime)

    def describe_purchased_devices_with_options(
        self,
        request: vs_20181212_models.DescribePurchasedDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribePurchasedDevicesResponse:
        """
        @param request: DescribePurchasedDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePurchasedDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribePurchasedDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purchased_devices_with_options_async(
        self,
        request: vs_20181212_models.DescribePurchasedDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribePurchasedDevicesResponse:
        """
        @param request: DescribePurchasedDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePurchasedDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribePurchasedDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purchased_devices(
        self,
        request: vs_20181212_models.DescribePurchasedDevicesRequest,
    ) -> vs_20181212_models.DescribePurchasedDevicesResponse:
        """
        @param request: DescribePurchasedDevicesRequest
        @return: DescribePurchasedDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_devices_with_options(request, runtime)

    async def describe_purchased_devices_async(
        self,
        request: vs_20181212_models.DescribePurchasedDevicesRequest,
    ) -> vs_20181212_models.DescribePurchasedDevicesResponse:
        """
        @param request: DescribePurchasedDevicesRequest
        @return: DescribePurchasedDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_purchased_devices_with_options_async(request, runtime)

    def describe_records_with_options(
        self,
        request: vs_20181212_models.DescribeRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeRecordsResponse:
        """
        @param request: DescribeRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.private_bucket):
            query['PrivateBucket'] = request.private_bucket
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_id):
            query['StreamId'] = request.stream_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecords',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_records_with_options_async(
        self,
        request: vs_20181212_models.DescribeRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeRecordsResponse:
        """
        @param request: DescribeRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.private_bucket):
            query['PrivateBucket'] = request.private_bucket
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_id):
            query['StreamId'] = request.stream_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecords',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_records(
        self,
        request: vs_20181212_models.DescribeRecordsRequest,
    ) -> vs_20181212_models.DescribeRecordsResponse:
        """
        @param request: DescribeRecordsRequest
        @return: DescribeRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_records_with_options(request, runtime)

    async def describe_records_async(
        self,
        request: vs_20181212_models.DescribeRecordsRequest,
    ) -> vs_20181212_models.DescribeRecordsResponse:
        """
        @param request: DescribeRecordsRequest
        @return: DescribeRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_records_with_options_async(request, runtime)

    def describe_rendering_instance_with_options(
        self,
        request: vs_20181212_models.DescribeRenderingInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeRenderingInstanceResponse:
        """
        @summary 查询云渲染实例详细信息。
        
        @param request: DescribeRenderingInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRenderingInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRenderingInstance',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeRenderingInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rendering_instance_with_options_async(
        self,
        request: vs_20181212_models.DescribeRenderingInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeRenderingInstanceResponse:
        """
        @summary 查询云渲染实例详细信息。
        
        @param request: DescribeRenderingInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRenderingInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRenderingInstance',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeRenderingInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rendering_instance(
        self,
        request: vs_20181212_models.DescribeRenderingInstanceRequest,
    ) -> vs_20181212_models.DescribeRenderingInstanceResponse:
        """
        @summary 查询云渲染实例详细信息。
        
        @param request: DescribeRenderingInstanceRequest
        @return: DescribeRenderingInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rendering_instance_with_options(request, runtime)

    async def describe_rendering_instance_async(
        self,
        request: vs_20181212_models.DescribeRenderingInstanceRequest,
    ) -> vs_20181212_models.DescribeRenderingInstanceResponse:
        """
        @summary 查询云渲染实例详细信息。
        
        @param request: DescribeRenderingInstanceRequest
        @return: DescribeRenderingInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rendering_instance_with_options_async(request, runtime)

    def describe_rendering_instance_configuration_with_options(
        self,
        tmp_req: vs_20181212_models.DescribeRenderingInstanceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeRenderingInstanceConfigurationResponse:
        """
        @summary 查询云渲染实例模块配置参数
        
        @param tmp_req: DescribeRenderingInstanceConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRenderingInstanceConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.DescribeRenderingInstanceConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configuration):
            request.configuration_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRenderingInstanceConfiguration',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeRenderingInstanceConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rendering_instance_configuration_with_options_async(
        self,
        tmp_req: vs_20181212_models.DescribeRenderingInstanceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeRenderingInstanceConfigurationResponse:
        """
        @summary 查询云渲染实例模块配置参数
        
        @param tmp_req: DescribeRenderingInstanceConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRenderingInstanceConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.DescribeRenderingInstanceConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configuration):
            request.configuration_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRenderingInstanceConfiguration',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeRenderingInstanceConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rendering_instance_configuration(
        self,
        request: vs_20181212_models.DescribeRenderingInstanceConfigurationRequest,
    ) -> vs_20181212_models.DescribeRenderingInstanceConfigurationResponse:
        """
        @summary 查询云渲染实例模块配置参数
        
        @param request: DescribeRenderingInstanceConfigurationRequest
        @return: DescribeRenderingInstanceConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rendering_instance_configuration_with_options(request, runtime)

    async def describe_rendering_instance_configuration_async(
        self,
        request: vs_20181212_models.DescribeRenderingInstanceConfigurationRequest,
    ) -> vs_20181212_models.DescribeRenderingInstanceConfigurationResponse:
        """
        @summary 查询云渲染实例模块配置参数
        
        @param request: DescribeRenderingInstanceConfigurationRequest
        @return: DescribeRenderingInstanceConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rendering_instance_configuration_with_options_async(request, runtime)

    def describe_rendering_instance_settings_with_options(
        self,
        tmp_req: vs_20181212_models.DescribeRenderingInstanceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeRenderingInstanceSettingsResponse:
        """
        @summary 查询实例配置
        
        @param tmp_req: DescribeRenderingInstanceSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRenderingInstanceSettingsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.DescribeRenderingInstanceSettingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attribute_names):
            request.attribute_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attribute_names, 'AttributeNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.attribute_names_shrink):
            query['AttributeNames'] = request.attribute_names_shrink
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRenderingInstanceSettings',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeRenderingInstanceSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rendering_instance_settings_with_options_async(
        self,
        tmp_req: vs_20181212_models.DescribeRenderingInstanceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeRenderingInstanceSettingsResponse:
        """
        @summary 查询实例配置
        
        @param tmp_req: DescribeRenderingInstanceSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRenderingInstanceSettingsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.DescribeRenderingInstanceSettingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.attribute_names):
            request.attribute_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.attribute_names, 'AttributeNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.attribute_names_shrink):
            query['AttributeNames'] = request.attribute_names_shrink
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRenderingInstanceSettings',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeRenderingInstanceSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rendering_instance_settings(
        self,
        request: vs_20181212_models.DescribeRenderingInstanceSettingsRequest,
    ) -> vs_20181212_models.DescribeRenderingInstanceSettingsResponse:
        """
        @summary 查询实例配置
        
        @param request: DescribeRenderingInstanceSettingsRequest
        @return: DescribeRenderingInstanceSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rendering_instance_settings_with_options(request, runtime)

    async def describe_rendering_instance_settings_async(
        self,
        request: vs_20181212_models.DescribeRenderingInstanceSettingsRequest,
    ) -> vs_20181212_models.DescribeRenderingInstanceSettingsResponse:
        """
        @summary 查询实例配置
        
        @param request: DescribeRenderingInstanceSettingsRequest
        @return: DescribeRenderingInstanceSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rendering_instance_settings_with_options_async(request, runtime)

    def describe_rendering_session_with_options(
        self,
        request: vs_20181212_models.DescribeRenderingSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeRenderingSessionResponse:
        """
        @summary 输出会话的详情信息，包含关联的实例、网络出口等信息。
        
        @param request: DescribeRenderingSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRenderingSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRenderingSession',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeRenderingSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rendering_session_with_options_async(
        self,
        request: vs_20181212_models.DescribeRenderingSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeRenderingSessionResponse:
        """
        @summary 输出会话的详情信息，包含关联的实例、网络出口等信息。
        
        @param request: DescribeRenderingSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRenderingSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRenderingSession',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeRenderingSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rendering_session(
        self,
        request: vs_20181212_models.DescribeRenderingSessionRequest,
    ) -> vs_20181212_models.DescribeRenderingSessionResponse:
        """
        @summary 输出会话的详情信息，包含关联的实例、网络出口等信息。
        
        @param request: DescribeRenderingSessionRequest
        @return: DescribeRenderingSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rendering_session_with_options(request, runtime)

    async def describe_rendering_session_async(
        self,
        request: vs_20181212_models.DescribeRenderingSessionRequest,
    ) -> vs_20181212_models.DescribeRenderingSessionResponse:
        """
        @summary 输出会话的详情信息，包含关联的实例、网络出口等信息。
        
        @param request: DescribeRenderingSessionRequest
        @return: DescribeRenderingSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rendering_session_with_options_async(request, runtime)

    def describe_stream_with_options(
        self,
        request: vs_20181212_models.DescribeStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeStreamResponse:
        """
        @param request: DescribeStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_stream_with_options_async(
        self,
        request: vs_20181212_models.DescribeStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeStreamResponse:
        """
        @param request: DescribeStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_stream(
        self,
        request: vs_20181212_models.DescribeStreamRequest,
    ) -> vs_20181212_models.DescribeStreamResponse:
        """
        @param request: DescribeStreamRequest
        @return: DescribeStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_stream_with_options(request, runtime)

    async def describe_stream_async(
        self,
        request: vs_20181212_models.DescribeStreamRequest,
    ) -> vs_20181212_models.DescribeStreamResponse:
        """
        @param request: DescribeStreamRequest
        @return: DescribeStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_stream_with_options_async(request, runtime)

    def describe_stream_urlwith_options(
        self,
        request: vs_20181212_models.DescribeStreamURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeStreamURLResponse:
        """
        @param request: DescribeStreamURLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStreamURLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth):
            query['Auth'] = request.auth
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.expire):
            query['Expire'] = request.expire
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.transcode):
            query['Transcode'] = request.transcode
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStreamURL',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeStreamURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_stream_urlwith_options_async(
        self,
        request: vs_20181212_models.DescribeStreamURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeStreamURLResponse:
        """
        @param request: DescribeStreamURLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStreamURLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth):
            query['Auth'] = request.auth
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.expire):
            query['Expire'] = request.expire
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.transcode):
            query['Transcode'] = request.transcode
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStreamURL',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeStreamURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_stream_url(
        self,
        request: vs_20181212_models.DescribeStreamURLRequest,
    ) -> vs_20181212_models.DescribeStreamURLResponse:
        """
        @param request: DescribeStreamURLRequest
        @return: DescribeStreamURLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_stream_urlwith_options(request, runtime)

    async def describe_stream_url_async(
        self,
        request: vs_20181212_models.DescribeStreamURLRequest,
    ) -> vs_20181212_models.DescribeStreamURLResponse:
        """
        @param request: DescribeStreamURLRequest
        @return: DescribeStreamURLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_stream_urlwith_options_async(request, runtime)

    def describe_stream_vod_list_with_options(
        self,
        request: vs_20181212_models.DescribeStreamVodListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeStreamVodListResponse:
        """
        @param request: DescribeStreamVodListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStreamVodListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStreamVodList',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeStreamVodListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_stream_vod_list_with_options_async(
        self,
        request: vs_20181212_models.DescribeStreamVodListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeStreamVodListResponse:
        """
        @param request: DescribeStreamVodListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStreamVodListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStreamVodList',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeStreamVodListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_stream_vod_list(
        self,
        request: vs_20181212_models.DescribeStreamVodListRequest,
    ) -> vs_20181212_models.DescribeStreamVodListResponse:
        """
        @param request: DescribeStreamVodListRequest
        @return: DescribeStreamVodListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_stream_vod_list_with_options(request, runtime)

    async def describe_stream_vod_list_async(
        self,
        request: vs_20181212_models.DescribeStreamVodListRequest,
    ) -> vs_20181212_models.DescribeStreamVodListResponse:
        """
        @param request: DescribeStreamVodListRequest
        @return: DescribeStreamVodListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_stream_vod_list_with_options_async(request, runtime)

    def describe_streams_with_options(
        self,
        request: vs_20181212_models.DescribeStreamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeStreamsResponse:
        """
        @param request: DescribeStreamsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStreamsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStreams',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeStreamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_streams_with_options_async(
        self,
        request: vs_20181212_models.DescribeStreamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeStreamsResponse:
        """
        @param request: DescribeStreamsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStreamsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStreams',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeStreamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_streams(
        self,
        request: vs_20181212_models.DescribeStreamsRequest,
    ) -> vs_20181212_models.DescribeStreamsResponse:
        """
        @param request: DescribeStreamsRequest
        @return: DescribeStreamsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_streams_with_options(request, runtime)

    async def describe_streams_async(
        self,
        request: vs_20181212_models.DescribeStreamsRequest,
    ) -> vs_20181212_models.DescribeStreamsResponse:
        """
        @param request: DescribeStreamsRequest
        @return: DescribeStreamsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_streams_with_options_async(request, runtime)

    def describe_template_with_options(
        self,
        request: vs_20181212_models.DescribeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeTemplateResponse:
        """
        @param request: DescribeTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_template_with_options_async(
        self,
        request: vs_20181212_models.DescribeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeTemplateResponse:
        """
        @param request: DescribeTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_template(
        self,
        request: vs_20181212_models.DescribeTemplateRequest,
    ) -> vs_20181212_models.DescribeTemplateResponse:
        """
        @param request: DescribeTemplateRequest
        @return: DescribeTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_template_with_options(request, runtime)

    async def describe_template_async(
        self,
        request: vs_20181212_models.DescribeTemplateRequest,
    ) -> vs_20181212_models.DescribeTemplateResponse:
        """
        @param request: DescribeTemplateRequest
        @return: DescribeTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_template_with_options_async(request, runtime)

    def describe_templates_with_options(
        self,
        request: vs_20181212_models.DescribeTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeTemplatesResponse:
        """
        @param request: DescribeTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplates',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_templates_with_options_async(
        self,
        request: vs_20181212_models.DescribeTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeTemplatesResponse:
        """
        @param request: DescribeTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplates',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_templates(
        self,
        request: vs_20181212_models.DescribeTemplatesRequest,
    ) -> vs_20181212_models.DescribeTemplatesResponse:
        """
        @param request: DescribeTemplatesRequest
        @return: DescribeTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_templates_with_options(request, runtime)

    async def describe_templates_async(
        self,
        request: vs_20181212_models.DescribeTemplatesRequest,
    ) -> vs_20181212_models.DescribeTemplatesResponse:
        """
        @param request: DescribeTemplatesRequest
        @return: DescribeTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_templates_with_options_async(request, runtime)

    def describe_vod_stream_urlwith_options(
        self,
        request: vs_20181212_models.DescribeVodStreamURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVodStreamURLResponse:
        """
        @param request: DescribeVodStreamURLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVodStreamURLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVodStreamURL',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVodStreamURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vod_stream_urlwith_options_async(
        self,
        request: vs_20181212_models.DescribeVodStreamURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVodStreamURLResponse:
        """
        @param request: DescribeVodStreamURLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVodStreamURLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVodStreamURL',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVodStreamURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vod_stream_url(
        self,
        request: vs_20181212_models.DescribeVodStreamURLRequest,
    ) -> vs_20181212_models.DescribeVodStreamURLResponse:
        """
        @param request: DescribeVodStreamURLRequest
        @return: DescribeVodStreamURLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_stream_urlwith_options(request, runtime)

    async def describe_vod_stream_url_async(
        self,
        request: vs_20181212_models.DescribeVodStreamURLRequest,
    ) -> vs_20181212_models.DescribeVodStreamURLResponse:
        """
        @param request: DescribeVodStreamURLRequest
        @return: DescribeVodStreamURLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_stream_urlwith_options_async(request, runtime)

    def describe_vs_certificate_detail_with_options(
        self,
        request: vs_20181212_models.DescribeVsCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsCertificateDetailResponse:
        """
        @param request: DescribeVsCertificateDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsCertificateDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsCertificateDetail',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_certificate_detail_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsCertificateDetailResponse:
        """
        @param request: DescribeVsCertificateDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsCertificateDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsCertificateDetail',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsCertificateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_certificate_detail(
        self,
        request: vs_20181212_models.DescribeVsCertificateDetailRequest,
    ) -> vs_20181212_models.DescribeVsCertificateDetailResponse:
        """
        @param request: DescribeVsCertificateDetailRequest
        @return: DescribeVsCertificateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_certificate_detail_with_options(request, runtime)

    async def describe_vs_certificate_detail_async(
        self,
        request: vs_20181212_models.DescribeVsCertificateDetailRequest,
    ) -> vs_20181212_models.DescribeVsCertificateDetailResponse:
        """
        @param request: DescribeVsCertificateDetailRequest
        @return: DescribeVsCertificateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_certificate_detail_with_options_async(request, runtime)

    def describe_vs_certificate_list_with_options(
        self,
        request: vs_20181212_models.DescribeVsCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsCertificateListResponse:
        """
        @param request: DescribeVsCertificateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsCertificateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsCertificateList',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_certificate_list_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsCertificateListResponse:
        """
        @param request: DescribeVsCertificateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsCertificateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsCertificateList',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_certificate_list(
        self,
        request: vs_20181212_models.DescribeVsCertificateListRequest,
    ) -> vs_20181212_models.DescribeVsCertificateListResponse:
        """
        @param request: DescribeVsCertificateListRequest
        @return: DescribeVsCertificateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_certificate_list_with_options(request, runtime)

    async def describe_vs_certificate_list_async(
        self,
        request: vs_20181212_models.DescribeVsCertificateListRequest,
    ) -> vs_20181212_models.DescribeVsCertificateListResponse:
        """
        @param request: DescribeVsCertificateListRequest
        @return: DescribeVsCertificateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_certificate_list_with_options_async(request, runtime)

    def describe_vs_devices_data_with_options(
        self,
        request: vs_20181212_models.DescribeVsDevicesDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDevicesDataResponse:
        """
        @param request: DescribeVsDevicesDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDevicesDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDevicesData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDevicesDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_devices_data_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsDevicesDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDevicesDataResponse:
        """
        @param request: DescribeVsDevicesDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDevicesDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDevicesData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDevicesDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_devices_data(
        self,
        request: vs_20181212_models.DescribeVsDevicesDataRequest,
    ) -> vs_20181212_models.DescribeVsDevicesDataResponse:
        """
        @param request: DescribeVsDevicesDataRequest
        @return: DescribeVsDevicesDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_devices_data_with_options(request, runtime)

    async def describe_vs_devices_data_async(
        self,
        request: vs_20181212_models.DescribeVsDevicesDataRequest,
    ) -> vs_20181212_models.DescribeVsDevicesDataResponse:
        """
        @param request: DescribeVsDevicesDataRequest
        @return: DescribeVsDevicesDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_devices_data_with_options_async(request, runtime)

    def describe_vs_domain_bps_data_with_options(
        self,
        request: vs_20181212_models.DescribeVsDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainBpsDataResponse:
        """
        @param request: DescribeVsDomainBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainBpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainBpsData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_bps_data_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainBpsDataResponse:
        """
        @param request: DescribeVsDomainBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainBpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainBpsData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_bps_data(
        self,
        request: vs_20181212_models.DescribeVsDomainBpsDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainBpsDataResponse:
        """
        @param request: DescribeVsDomainBpsDataRequest
        @return: DescribeVsDomainBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_bps_data_with_options(request, runtime)

    async def describe_vs_domain_bps_data_async(
        self,
        request: vs_20181212_models.DescribeVsDomainBpsDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainBpsDataResponse:
        """
        @param request: DescribeVsDomainBpsDataRequest
        @return: DescribeVsDomainBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_domain_bps_data_with_options_async(request, runtime)

    def describe_vs_domain_certificate_info_with_options(
        self,
        request: vs_20181212_models.DescribeVsDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainCertificateInfoResponse:
        """
        @param request: DescribeVsDomainCertificateInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainCertificateInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainCertificateInfo',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainCertificateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_certificate_info_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainCertificateInfoResponse:
        """
        @param request: DescribeVsDomainCertificateInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainCertificateInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainCertificateInfo',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainCertificateInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_certificate_info(
        self,
        request: vs_20181212_models.DescribeVsDomainCertificateInfoRequest,
    ) -> vs_20181212_models.DescribeVsDomainCertificateInfoResponse:
        """
        @param request: DescribeVsDomainCertificateInfoRequest
        @return: DescribeVsDomainCertificateInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_certificate_info_with_options(request, runtime)

    async def describe_vs_domain_certificate_info_async(
        self,
        request: vs_20181212_models.DescribeVsDomainCertificateInfoRequest,
    ) -> vs_20181212_models.DescribeVsDomainCertificateInfoResponse:
        """
        @param request: DescribeVsDomainCertificateInfoRequest
        @return: DescribeVsDomainCertificateInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_domain_certificate_info_with_options_async(request, runtime)

    def describe_vs_domain_configs_with_options(
        self,
        request: vs_20181212_models.DescribeVsDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainConfigsResponse:
        """
        @param request: DescribeVsDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainConfigs',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_configs_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainConfigsResponse:
        """
        @param request: DescribeVsDomainConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainConfigs',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_configs(
        self,
        request: vs_20181212_models.DescribeVsDomainConfigsRequest,
    ) -> vs_20181212_models.DescribeVsDomainConfigsResponse:
        """
        @param request: DescribeVsDomainConfigsRequest
        @return: DescribeVsDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_configs_with_options(request, runtime)

    async def describe_vs_domain_configs_async(
        self,
        request: vs_20181212_models.DescribeVsDomainConfigsRequest,
    ) -> vs_20181212_models.DescribeVsDomainConfigsResponse:
        """
        @param request: DescribeVsDomainConfigsRequest
        @return: DescribeVsDomainConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_domain_configs_with_options_async(request, runtime)

    def describe_vs_domain_detail_with_options(
        self,
        request: vs_20181212_models.DescribeVsDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainDetailResponse:
        """
        @param request: DescribeVsDomainDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainDetail',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_detail_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainDetailResponse:
        """
        @param request: DescribeVsDomainDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainDetail',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_detail(
        self,
        request: vs_20181212_models.DescribeVsDomainDetailRequest,
    ) -> vs_20181212_models.DescribeVsDomainDetailResponse:
        """
        @param request: DescribeVsDomainDetailRequest
        @return: DescribeVsDomainDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_detail_with_options(request, runtime)

    async def describe_vs_domain_detail_async(
        self,
        request: vs_20181212_models.DescribeVsDomainDetailRequest,
    ) -> vs_20181212_models.DescribeVsDomainDetailResponse:
        """
        @param request: DescribeVsDomainDetailRequest
        @return: DescribeVsDomainDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_domain_detail_with_options_async(request, runtime)

    def describe_vs_domain_pv_data_with_options(
        self,
        request: vs_20181212_models.DescribeVsDomainPvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainPvDataResponse:
        """
        @param request: DescribeVsDomainPvDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainPvDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainPvData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainPvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_pv_data_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsDomainPvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainPvDataResponse:
        """
        @param request: DescribeVsDomainPvDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainPvDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainPvData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainPvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_pv_data(
        self,
        request: vs_20181212_models.DescribeVsDomainPvDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainPvDataResponse:
        """
        @param request: DescribeVsDomainPvDataRequest
        @return: DescribeVsDomainPvDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_pv_data_with_options(request, runtime)

    async def describe_vs_domain_pv_data_async(
        self,
        request: vs_20181212_models.DescribeVsDomainPvDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainPvDataResponse:
        """
        @param request: DescribeVsDomainPvDataRequest
        @return: DescribeVsDomainPvDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_domain_pv_data_with_options_async(request, runtime)

    def describe_vs_domain_pv_uv_data_with_options(
        self,
        request: vs_20181212_models.DescribeVsDomainPvUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainPvUvDataResponse:
        """
        @param request: DescribeVsDomainPvUvDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainPvUvDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainPvUvData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainPvUvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_pv_uv_data_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsDomainPvUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainPvUvDataResponse:
        """
        @param request: DescribeVsDomainPvUvDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainPvUvDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainPvUvData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainPvUvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_pv_uv_data(
        self,
        request: vs_20181212_models.DescribeVsDomainPvUvDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainPvUvDataResponse:
        """
        @param request: DescribeVsDomainPvUvDataRequest
        @return: DescribeVsDomainPvUvDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_pv_uv_data_with_options(request, runtime)

    async def describe_vs_domain_pv_uv_data_async(
        self,
        request: vs_20181212_models.DescribeVsDomainPvUvDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainPvUvDataResponse:
        """
        @param request: DescribeVsDomainPvUvDataRequest
        @return: DescribeVsDomainPvUvDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_domain_pv_uv_data_with_options_async(request, runtime)

    def describe_vs_domain_record_data_with_options(
        self,
        request: vs_20181212_models.DescribeVsDomainRecordDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainRecordDataResponse:
        """
        @param request: DescribeVsDomainRecordDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainRecordDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainRecordData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainRecordDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_record_data_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsDomainRecordDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainRecordDataResponse:
        """
        @param request: DescribeVsDomainRecordDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainRecordDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainRecordData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainRecordDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_record_data(
        self,
        request: vs_20181212_models.DescribeVsDomainRecordDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainRecordDataResponse:
        """
        @param request: DescribeVsDomainRecordDataRequest
        @return: DescribeVsDomainRecordDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_record_data_with_options(request, runtime)

    async def describe_vs_domain_record_data_async(
        self,
        request: vs_20181212_models.DescribeVsDomainRecordDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainRecordDataResponse:
        """
        @param request: DescribeVsDomainRecordDataRequest
        @return: DescribeVsDomainRecordDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_domain_record_data_with_options_async(request, runtime)

    def describe_vs_domain_region_data_with_options(
        self,
        request: vs_20181212_models.DescribeVsDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainRegionDataResponse:
        """
        @param request: DescribeVsDomainRegionDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainRegionDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainRegionData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainRegionDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_region_data_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsDomainRegionDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainRegionDataResponse:
        """
        @param request: DescribeVsDomainRegionDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainRegionDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainRegionData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainRegionDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_region_data(
        self,
        request: vs_20181212_models.DescribeVsDomainRegionDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainRegionDataResponse:
        """
        @param request: DescribeVsDomainRegionDataRequest
        @return: DescribeVsDomainRegionDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_region_data_with_options(request, runtime)

    async def describe_vs_domain_region_data_async(
        self,
        request: vs_20181212_models.DescribeVsDomainRegionDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainRegionDataResponse:
        """
        @param request: DescribeVsDomainRegionDataRequest
        @return: DescribeVsDomainRegionDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_domain_region_data_with_options_async(request, runtime)

    def describe_vs_domain_req_bps_data_with_options(
        self,
        request: vs_20181212_models.DescribeVsDomainReqBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainReqBpsDataResponse:
        """
        @param request: DescribeVsDomainReqBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainReqBpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainReqBpsData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainReqBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_req_bps_data_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsDomainReqBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainReqBpsDataResponse:
        """
        @param request: DescribeVsDomainReqBpsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainReqBpsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainReqBpsData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainReqBpsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_req_bps_data(
        self,
        request: vs_20181212_models.DescribeVsDomainReqBpsDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainReqBpsDataResponse:
        """
        @param request: DescribeVsDomainReqBpsDataRequest
        @return: DescribeVsDomainReqBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_req_bps_data_with_options(request, runtime)

    async def describe_vs_domain_req_bps_data_async(
        self,
        request: vs_20181212_models.DescribeVsDomainReqBpsDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainReqBpsDataResponse:
        """
        @param request: DescribeVsDomainReqBpsDataRequest
        @return: DescribeVsDomainReqBpsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_domain_req_bps_data_with_options_async(request, runtime)

    def describe_vs_domain_req_traffic_data_with_options(
        self,
        request: vs_20181212_models.DescribeVsDomainReqTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainReqTrafficDataResponse:
        """
        @param request: DescribeVsDomainReqTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainReqTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainReqTrafficData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainReqTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_req_traffic_data_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsDomainReqTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainReqTrafficDataResponse:
        """
        @param request: DescribeVsDomainReqTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainReqTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainReqTrafficData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainReqTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_req_traffic_data(
        self,
        request: vs_20181212_models.DescribeVsDomainReqTrafficDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainReqTrafficDataResponse:
        """
        @param request: DescribeVsDomainReqTrafficDataRequest
        @return: DescribeVsDomainReqTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_req_traffic_data_with_options(request, runtime)

    async def describe_vs_domain_req_traffic_data_async(
        self,
        request: vs_20181212_models.DescribeVsDomainReqTrafficDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainReqTrafficDataResponse:
        """
        @param request: DescribeVsDomainReqTrafficDataRequest
        @return: DescribeVsDomainReqTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_domain_req_traffic_data_with_options_async(request, runtime)

    def describe_vs_domain_snapshot_data_with_options(
        self,
        request: vs_20181212_models.DescribeVsDomainSnapshotDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainSnapshotDataResponse:
        """
        @param request: DescribeVsDomainSnapshotDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainSnapshotDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainSnapshotData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainSnapshotDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_snapshot_data_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsDomainSnapshotDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainSnapshotDataResponse:
        """
        @param request: DescribeVsDomainSnapshotDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainSnapshotDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainSnapshotData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainSnapshotDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_snapshot_data(
        self,
        request: vs_20181212_models.DescribeVsDomainSnapshotDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainSnapshotDataResponse:
        """
        @param request: DescribeVsDomainSnapshotDataRequest
        @return: DescribeVsDomainSnapshotDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_snapshot_data_with_options(request, runtime)

    async def describe_vs_domain_snapshot_data_async(
        self,
        request: vs_20181212_models.DescribeVsDomainSnapshotDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainSnapshotDataResponse:
        """
        @param request: DescribeVsDomainSnapshotDataRequest
        @return: DescribeVsDomainSnapshotDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_domain_snapshot_data_with_options_async(request, runtime)

    def describe_vs_domain_traffic_data_with_options(
        self,
        request: vs_20181212_models.DescribeVsDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainTrafficDataResponse:
        """
        @param request: DescribeVsDomainTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainTrafficData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_traffic_data_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainTrafficDataResponse:
        """
        @param request: DescribeVsDomainTrafficDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainTrafficDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainTrafficData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainTrafficDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_traffic_data(
        self,
        request: vs_20181212_models.DescribeVsDomainTrafficDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainTrafficDataResponse:
        """
        @param request: DescribeVsDomainTrafficDataRequest
        @return: DescribeVsDomainTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_traffic_data_with_options(request, runtime)

    async def describe_vs_domain_traffic_data_async(
        self,
        request: vs_20181212_models.DescribeVsDomainTrafficDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainTrafficDataResponse:
        """
        @param request: DescribeVsDomainTrafficDataRequest
        @return: DescribeVsDomainTrafficDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_domain_traffic_data_with_options_async(request, runtime)

    def describe_vs_domain_uv_data_with_options(
        self,
        request: vs_20181212_models.DescribeVsDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainUvDataResponse:
        """
        @param request: DescribeVsDomainUvDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainUvDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainUvData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainUvDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_domain_uv_data_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsDomainUvDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsDomainUvDataResponse:
        """
        @param request: DescribeVsDomainUvDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsDomainUvDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainUvData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainUvDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_domain_uv_data(
        self,
        request: vs_20181212_models.DescribeVsDomainUvDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainUvDataResponse:
        """
        @param request: DescribeVsDomainUvDataRequest
        @return: DescribeVsDomainUvDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_uv_data_with_options(request, runtime)

    async def describe_vs_domain_uv_data_async(
        self,
        request: vs_20181212_models.DescribeVsDomainUvDataRequest,
    ) -> vs_20181212_models.DescribeVsDomainUvDataResponse:
        """
        @param request: DescribeVsDomainUvDataRequest
        @return: DescribeVsDomainUvDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_domain_uv_data_with_options_async(request, runtime)

    def describe_vs_pull_stream_info_config_with_options(
        self,
        request: vs_20181212_models.DescribeVsPullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsPullStreamInfoConfigResponse:
        """
        @param request: DescribeVsPullStreamInfoConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsPullStreamInfoConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsPullStreamInfoConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsPullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_pull_stream_info_config_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsPullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsPullStreamInfoConfigResponse:
        """
        @param request: DescribeVsPullStreamInfoConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsPullStreamInfoConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsPullStreamInfoConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsPullStreamInfoConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_pull_stream_info_config(
        self,
        request: vs_20181212_models.DescribeVsPullStreamInfoConfigRequest,
    ) -> vs_20181212_models.DescribeVsPullStreamInfoConfigResponse:
        """
        @param request: DescribeVsPullStreamInfoConfigRequest
        @return: DescribeVsPullStreamInfoConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_pull_stream_info_config_with_options(request, runtime)

    async def describe_vs_pull_stream_info_config_async(
        self,
        request: vs_20181212_models.DescribeVsPullStreamInfoConfigRequest,
    ) -> vs_20181212_models.DescribeVsPullStreamInfoConfigResponse:
        """
        @param request: DescribeVsPullStreamInfoConfigRequest
        @return: DescribeVsPullStreamInfoConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_pull_stream_info_config_with_options_async(request, runtime)

    def describe_vs_streams_notify_url_config_with_options(
        self,
        request: vs_20181212_models.DescribeVsStreamsNotifyUrlConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsStreamsNotifyUrlConfigResponse:
        """
        @param request: DescribeVsStreamsNotifyUrlConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsStreamsNotifyUrlConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsStreamsNotifyUrlConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsStreamsNotifyUrlConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_streams_notify_url_config_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsStreamsNotifyUrlConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsStreamsNotifyUrlConfigResponse:
        """
        @param request: DescribeVsStreamsNotifyUrlConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsStreamsNotifyUrlConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsStreamsNotifyUrlConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsStreamsNotifyUrlConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_streams_notify_url_config(
        self,
        request: vs_20181212_models.DescribeVsStreamsNotifyUrlConfigRequest,
    ) -> vs_20181212_models.DescribeVsStreamsNotifyUrlConfigResponse:
        """
        @param request: DescribeVsStreamsNotifyUrlConfigRequest
        @return: DescribeVsStreamsNotifyUrlConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_streams_notify_url_config_with_options(request, runtime)

    async def describe_vs_streams_notify_url_config_async(
        self,
        request: vs_20181212_models.DescribeVsStreamsNotifyUrlConfigRequest,
    ) -> vs_20181212_models.DescribeVsStreamsNotifyUrlConfigResponse:
        """
        @param request: DescribeVsStreamsNotifyUrlConfigRequest
        @return: DescribeVsStreamsNotifyUrlConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_streams_notify_url_config_with_options_async(request, runtime)

    def describe_vs_streams_online_list_with_options(
        self,
        request: vs_20181212_models.DescribeVsStreamsOnlineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsStreamsOnlineListResponse:
        """
        @param request: DescribeVsStreamsOnlineListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsStreamsOnlineListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsStreamsOnlineList',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsStreamsOnlineListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_streams_online_list_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsStreamsOnlineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsStreamsOnlineListResponse:
        """
        @param request: DescribeVsStreamsOnlineListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsStreamsOnlineListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsStreamsOnlineList',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsStreamsOnlineListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_streams_online_list(
        self,
        request: vs_20181212_models.DescribeVsStreamsOnlineListRequest,
    ) -> vs_20181212_models.DescribeVsStreamsOnlineListResponse:
        """
        @param request: DescribeVsStreamsOnlineListRequest
        @return: DescribeVsStreamsOnlineListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_streams_online_list_with_options(request, runtime)

    async def describe_vs_streams_online_list_async(
        self,
        request: vs_20181212_models.DescribeVsStreamsOnlineListRequest,
    ) -> vs_20181212_models.DescribeVsStreamsOnlineListResponse:
        """
        @param request: DescribeVsStreamsOnlineListRequest
        @return: DescribeVsStreamsOnlineListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_streams_online_list_with_options_async(request, runtime)

    def describe_vs_streams_publish_list_with_options(
        self,
        request: vs_20181212_models.DescribeVsStreamsPublishListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsStreamsPublishListResponse:
        """
        @param request: DescribeVsStreamsPublishListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsStreamsPublishListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsStreamsPublishList',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsStreamsPublishListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_streams_publish_list_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsStreamsPublishListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsStreamsPublishListResponse:
        """
        @param request: DescribeVsStreamsPublishListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsStreamsPublishListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsStreamsPublishList',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsStreamsPublishListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_streams_publish_list(
        self,
        request: vs_20181212_models.DescribeVsStreamsPublishListRequest,
    ) -> vs_20181212_models.DescribeVsStreamsPublishListResponse:
        """
        @param request: DescribeVsStreamsPublishListRequest
        @return: DescribeVsStreamsPublishListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_streams_publish_list_with_options(request, runtime)

    async def describe_vs_streams_publish_list_async(
        self,
        request: vs_20181212_models.DescribeVsStreamsPublishListRequest,
    ) -> vs_20181212_models.DescribeVsStreamsPublishListResponse:
        """
        @param request: DescribeVsStreamsPublishListRequest
        @return: DescribeVsStreamsPublishListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_streams_publish_list_with_options_async(request, runtime)

    def describe_vs_top_domains_by_flow_with_options(
        self,
        request: vs_20181212_models.DescribeVsTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsTopDomainsByFlowResponse:
        """
        @param request: DescribeVsTopDomainsByFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsTopDomainsByFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsTopDomainsByFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsTopDomainsByFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_top_domains_by_flow_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsTopDomainsByFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsTopDomainsByFlowResponse:
        """
        @param request: DescribeVsTopDomainsByFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsTopDomainsByFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsTopDomainsByFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsTopDomainsByFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_top_domains_by_flow(
        self,
        request: vs_20181212_models.DescribeVsTopDomainsByFlowRequest,
    ) -> vs_20181212_models.DescribeVsTopDomainsByFlowResponse:
        """
        @param request: DescribeVsTopDomainsByFlowRequest
        @return: DescribeVsTopDomainsByFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_top_domains_by_flow_with_options(request, runtime)

    async def describe_vs_top_domains_by_flow_async(
        self,
        request: vs_20181212_models.DescribeVsTopDomainsByFlowRequest,
    ) -> vs_20181212_models.DescribeVsTopDomainsByFlowResponse:
        """
        @param request: DescribeVsTopDomainsByFlowRequest
        @return: DescribeVsTopDomainsByFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_top_domains_by_flow_with_options_async(request, runtime)

    def describe_vs_up_peak_publish_stream_data_with_options(
        self,
        request: vs_20181212_models.DescribeVsUpPeakPublishStreamDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsUpPeakPublishStreamDataResponse:
        """
        @param request: DescribeVsUpPeakPublishStreamDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsUpPeakPublishStreamDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_switch):
            query['DomainSwitch'] = request.domain_switch
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsUpPeakPublishStreamData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsUpPeakPublishStreamDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_up_peak_publish_stream_data_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsUpPeakPublishStreamDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsUpPeakPublishStreamDataResponse:
        """
        @param request: DescribeVsUpPeakPublishStreamDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsUpPeakPublishStreamDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_switch):
            query['DomainSwitch'] = request.domain_switch
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsUpPeakPublishStreamData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsUpPeakPublishStreamDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_up_peak_publish_stream_data(
        self,
        request: vs_20181212_models.DescribeVsUpPeakPublishStreamDataRequest,
    ) -> vs_20181212_models.DescribeVsUpPeakPublishStreamDataResponse:
        """
        @param request: DescribeVsUpPeakPublishStreamDataRequest
        @return: DescribeVsUpPeakPublishStreamDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_up_peak_publish_stream_data_with_options(request, runtime)

    async def describe_vs_up_peak_publish_stream_data_async(
        self,
        request: vs_20181212_models.DescribeVsUpPeakPublishStreamDataRequest,
    ) -> vs_20181212_models.DescribeVsUpPeakPublishStreamDataResponse:
        """
        @param request: DescribeVsUpPeakPublishStreamDataRequest
        @return: DescribeVsUpPeakPublishStreamDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_up_peak_publish_stream_data_with_options_async(request, runtime)

    def describe_vs_user_resource_package_with_options(
        self,
        request: vs_20181212_models.DescribeVsUserResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsUserResourcePackageResponse:
        """
        @param request: DescribeVsUserResourcePackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsUserResourcePackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsUserResourcePackage',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsUserResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_user_resource_package_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsUserResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsUserResourcePackageResponse:
        """
        @param request: DescribeVsUserResourcePackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsUserResourcePackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsUserResourcePackage',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsUserResourcePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_user_resource_package(
        self,
        request: vs_20181212_models.DescribeVsUserResourcePackageRequest,
    ) -> vs_20181212_models.DescribeVsUserResourcePackageResponse:
        """
        @param request: DescribeVsUserResourcePackageRequest
        @return: DescribeVsUserResourcePackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_user_resource_package_with_options(request, runtime)

    async def describe_vs_user_resource_package_async(
        self,
        request: vs_20181212_models.DescribeVsUserResourcePackageRequest,
    ) -> vs_20181212_models.DescribeVsUserResourcePackageResponse:
        """
        @param request: DescribeVsUserResourcePackageRequest
        @return: DescribeVsUserResourcePackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_user_resource_package_with_options_async(request, runtime)

    def describe_vs_verify_content_with_options(
        self,
        request: vs_20181212_models.DescribeVsVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsVerifyContentResponse:
        """
        @param request: DescribeVsVerifyContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsVerifyContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsVerifyContent',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsVerifyContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vs_verify_content_with_options_async(
        self,
        request: vs_20181212_models.DescribeVsVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DescribeVsVerifyContentResponse:
        """
        @param request: DescribeVsVerifyContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVsVerifyContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsVerifyContent',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsVerifyContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vs_verify_content(
        self,
        request: vs_20181212_models.DescribeVsVerifyContentRequest,
    ) -> vs_20181212_models.DescribeVsVerifyContentResponse:
        """
        @param request: DescribeVsVerifyContentRequest
        @return: DescribeVsVerifyContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_verify_content_with_options(request, runtime)

    async def describe_vs_verify_content_async(
        self,
        request: vs_20181212_models.DescribeVsVerifyContentRequest,
    ) -> vs_20181212_models.DescribeVsVerifyContentResponse:
        """
        @param request: DescribeVsVerifyContentRequest
        @return: DescribeVsVerifyContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vs_verify_content_with_options_async(request, runtime)

    def disassociate_rendering_project_instances_with_options(
        self,
        tmp_req: vs_20181212_models.DisassociateRenderingProjectInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DisassociateRenderingProjectInstancesResponse:
        """
        @summary 云应用服务实例与项目解除关联
        
        @param tmp_req: DisassociateRenderingProjectInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisassociateRenderingProjectInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.DisassociateRenderingProjectInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateRenderingProjectInstances',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DisassociateRenderingProjectInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_rendering_project_instances_with_options_async(
        self,
        tmp_req: vs_20181212_models.DisassociateRenderingProjectInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.DisassociateRenderingProjectInstancesResponse:
        """
        @summary 云应用服务实例与项目解除关联
        
        @param tmp_req: DisassociateRenderingProjectInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisassociateRenderingProjectInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.DisassociateRenderingProjectInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateRenderingProjectInstances',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DisassociateRenderingProjectInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_rendering_project_instances(
        self,
        request: vs_20181212_models.DisassociateRenderingProjectInstancesRequest,
    ) -> vs_20181212_models.DisassociateRenderingProjectInstancesResponse:
        """
        @summary 云应用服务实例与项目解除关联
        
        @param request: DisassociateRenderingProjectInstancesRequest
        @return: DisassociateRenderingProjectInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disassociate_rendering_project_instances_with_options(request, runtime)

    async def disassociate_rendering_project_instances_async(
        self,
        request: vs_20181212_models.DisassociateRenderingProjectInstancesRequest,
    ) -> vs_20181212_models.DisassociateRenderingProjectInstancesResponse:
        """
        @summary 云应用服务实例与项目解除关联
        
        @param request: DisassociateRenderingProjectInstancesRequest
        @return: DisassociateRenderingProjectInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disassociate_rendering_project_instances_with_options_async(request, runtime)

    def forbid_vs_stream_with_options(
        self,
        request: vs_20181212_models.ForbidVsStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ForbidVsStreamResponse:
        """
        @param request: ForbidVsStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ForbidVsStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not UtilClient.is_unset(request.oneshot):
            query['Oneshot'] = request.oneshot
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resume_time):
            query['ResumeTime'] = request.resume_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ForbidVsStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ForbidVsStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def forbid_vs_stream_with_options_async(
        self,
        request: vs_20181212_models.ForbidVsStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ForbidVsStreamResponse:
        """
        @param request: ForbidVsStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ForbidVsStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not UtilClient.is_unset(request.oneshot):
            query['Oneshot'] = request.oneshot
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resume_time):
            query['ResumeTime'] = request.resume_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ForbidVsStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ForbidVsStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def forbid_vs_stream(
        self,
        request: vs_20181212_models.ForbidVsStreamRequest,
    ) -> vs_20181212_models.ForbidVsStreamResponse:
        """
        @param request: ForbidVsStreamRequest
        @return: ForbidVsStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.forbid_vs_stream_with_options(request, runtime)

    async def forbid_vs_stream_async(
        self,
        request: vs_20181212_models.ForbidVsStreamRequest,
    ) -> vs_20181212_models.ForbidVsStreamResponse:
        """
        @param request: ForbidVsStreamRequest
        @return: ForbidVsStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.forbid_vs_stream_with_options_async(request, runtime)

    def get_rendering_instance_commands_status_with_options(
        self,
        request: vs_20181212_models.GetRenderingInstanceCommandsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.GetRenderingInstanceCommandsStatusResponse:
        """
        @summary 查询命令的执行状态与结果。
        
        @param request: GetRenderingInstanceCommandsStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRenderingInstanceCommandsStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cmd_id):
            query['CmdId'] = request.cmd_id
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRenderingInstanceCommandsStatus',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.GetRenderingInstanceCommandsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rendering_instance_commands_status_with_options_async(
        self,
        request: vs_20181212_models.GetRenderingInstanceCommandsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.GetRenderingInstanceCommandsStatusResponse:
        """
        @summary 查询命令的执行状态与结果。
        
        @param request: GetRenderingInstanceCommandsStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRenderingInstanceCommandsStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cmd_id):
            query['CmdId'] = request.cmd_id
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRenderingInstanceCommandsStatus',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.GetRenderingInstanceCommandsStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rendering_instance_commands_status(
        self,
        request: vs_20181212_models.GetRenderingInstanceCommandsStatusRequest,
    ) -> vs_20181212_models.GetRenderingInstanceCommandsStatusResponse:
        """
        @summary 查询命令的执行状态与结果。
        
        @param request: GetRenderingInstanceCommandsStatusRequest
        @return: GetRenderingInstanceCommandsStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_rendering_instance_commands_status_with_options(request, runtime)

    async def get_rendering_instance_commands_status_async(
        self,
        request: vs_20181212_models.GetRenderingInstanceCommandsStatusRequest,
    ) -> vs_20181212_models.GetRenderingInstanceCommandsStatusResponse:
        """
        @summary 查询命令的执行状态与结果。
        
        @param request: GetRenderingInstanceCommandsStatusRequest
        @return: GetRenderingInstanceCommandsStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_rendering_instance_commands_status_with_options_async(request, runtime)

    def get_rendering_instance_streaming_info_with_options(
        self,
        request: vs_20181212_models.GetRenderingInstanceStreamingInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.GetRenderingInstanceStreamingInfoResponse:
        """
        @summary 获取云渲染实例流连接信息，每次流化建联前都需要调用此接口获取最新连接信息
        
        @param request: GetRenderingInstanceStreamingInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRenderingInstanceStreamingInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRenderingInstanceStreamingInfo',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.GetRenderingInstanceStreamingInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rendering_instance_streaming_info_with_options_async(
        self,
        request: vs_20181212_models.GetRenderingInstanceStreamingInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.GetRenderingInstanceStreamingInfoResponse:
        """
        @summary 获取云渲染实例流连接信息，每次流化建联前都需要调用此接口获取最新连接信息
        
        @param request: GetRenderingInstanceStreamingInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRenderingInstanceStreamingInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRenderingInstanceStreamingInfo',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.GetRenderingInstanceStreamingInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rendering_instance_streaming_info(
        self,
        request: vs_20181212_models.GetRenderingInstanceStreamingInfoRequest,
    ) -> vs_20181212_models.GetRenderingInstanceStreamingInfoResponse:
        """
        @summary 获取云渲染实例流连接信息，每次流化建联前都需要调用此接口获取最新连接信息
        
        @param request: GetRenderingInstanceStreamingInfoRequest
        @return: GetRenderingInstanceStreamingInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_rendering_instance_streaming_info_with_options(request, runtime)

    async def get_rendering_instance_streaming_info_async(
        self,
        request: vs_20181212_models.GetRenderingInstanceStreamingInfoRequest,
    ) -> vs_20181212_models.GetRenderingInstanceStreamingInfoResponse:
        """
        @summary 获取云渲染实例流连接信息，每次流化建联前都需要调用此接口获取最新连接信息
        
        @param request: GetRenderingInstanceStreamingInfoRequest
        @return: GetRenderingInstanceStreamingInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_rendering_instance_streaming_info_with_options_async(request, runtime)

    def get_rendering_project_instance_state_metrics_with_options(
        self,
        request: vs_20181212_models.GetRenderingProjectInstanceStateMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.GetRenderingProjectInstanceStateMetricsResponse:
        """
        @summary 输出满足特定条件的资源各状态数据量统计值。
        
        @param request: GetRenderingProjectInstanceStateMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRenderingProjectInstanceStateMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRenderingProjectInstanceStateMetrics',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.GetRenderingProjectInstanceStateMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rendering_project_instance_state_metrics_with_options_async(
        self,
        request: vs_20181212_models.GetRenderingProjectInstanceStateMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.GetRenderingProjectInstanceStateMetricsResponse:
        """
        @summary 输出满足特定条件的资源各状态数据量统计值。
        
        @param request: GetRenderingProjectInstanceStateMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRenderingProjectInstanceStateMetricsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRenderingProjectInstanceStateMetrics',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.GetRenderingProjectInstanceStateMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rendering_project_instance_state_metrics(
        self,
        request: vs_20181212_models.GetRenderingProjectInstanceStateMetricsRequest,
    ) -> vs_20181212_models.GetRenderingProjectInstanceStateMetricsResponse:
        """
        @summary 输出满足特定条件的资源各状态数据量统计值。
        
        @param request: GetRenderingProjectInstanceStateMetricsRequest
        @return: GetRenderingProjectInstanceStateMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_rendering_project_instance_state_metrics_with_options(request, runtime)

    async def get_rendering_project_instance_state_metrics_async(
        self,
        request: vs_20181212_models.GetRenderingProjectInstanceStateMetricsRequest,
    ) -> vs_20181212_models.GetRenderingProjectInstanceStateMetricsResponse:
        """
        @summary 输出满足特定条件的资源各状态数据量统计值。
        
        @param request: GetRenderingProjectInstanceStateMetricsRequest
        @return: GetRenderingProjectInstanceStateMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_rendering_project_instance_state_metrics_with_options_async(request, runtime)

    def goto_preset_with_options(
        self,
        request: vs_20181212_models.GotoPresetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.GotoPresetResponse:
        """
        @param request: GotoPresetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GotoPresetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preset_id):
            query['PresetId'] = request.preset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GotoPreset',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.GotoPresetResponse(),
            self.call_api(params, req, runtime)
        )

    async def goto_preset_with_options_async(
        self,
        request: vs_20181212_models.GotoPresetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.GotoPresetResponse:
        """
        @param request: GotoPresetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GotoPresetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preset_id):
            query['PresetId'] = request.preset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GotoPreset',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.GotoPresetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def goto_preset(
        self,
        request: vs_20181212_models.GotoPresetRequest,
    ) -> vs_20181212_models.GotoPresetResponse:
        """
        @param request: GotoPresetRequest
        @return: GotoPresetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.goto_preset_with_options(request, runtime)

    async def goto_preset_async(
        self,
        request: vs_20181212_models.GotoPresetRequest,
    ) -> vs_20181212_models.GotoPresetResponse:
        """
        @param request: GotoPresetRequest
        @return: GotoPresetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.goto_preset_with_options_async(request, runtime)

    def install_cloud_app_with_options(
        self,
        tmp_req: vs_20181212_models.InstallCloudAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.InstallCloudAppResponse:
        """
        @summary 安装云应用
        
        @param tmp_req: InstallCloudAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallCloudAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.InstallCloudAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not UtilClient.is_unset(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallCloudApp',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.InstallCloudAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_cloud_app_with_options_async(
        self,
        tmp_req: vs_20181212_models.InstallCloudAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.InstallCloudAppResponse:
        """
        @summary 安装云应用
        
        @param tmp_req: InstallCloudAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallCloudAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.InstallCloudAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not UtilClient.is_unset(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallCloudApp',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.InstallCloudAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_cloud_app(
        self,
        request: vs_20181212_models.InstallCloudAppRequest,
    ) -> vs_20181212_models.InstallCloudAppResponse:
        """
        @summary 安装云应用
        
        @param request: InstallCloudAppRequest
        @return: InstallCloudAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.install_cloud_app_with_options(request, runtime)

    async def install_cloud_app_async(
        self,
        request: vs_20181212_models.InstallCloudAppRequest,
    ) -> vs_20181212_models.InstallCloudAppResponse:
        """
        @summary 安装云应用
        
        @param request: InstallCloudAppRequest
        @return: InstallCloudAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.install_cloud_app_with_options_async(request, runtime)

    def list_cloud_app_installations_with_options(
        self,
        request: vs_20181212_models.ListCloudAppInstallationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListCloudAppInstallationsResponse:
        """
        @summary 查询云应用安装信息列表
        
        @param request: ListCloudAppInstallationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudAppInstallationsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudAppInstallations',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListCloudAppInstallationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_app_installations_with_options_async(
        self,
        request: vs_20181212_models.ListCloudAppInstallationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListCloudAppInstallationsResponse:
        """
        @summary 查询云应用安装信息列表
        
        @param request: ListCloudAppInstallationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudAppInstallationsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudAppInstallations',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListCloudAppInstallationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_app_installations(
        self,
        request: vs_20181212_models.ListCloudAppInstallationsRequest,
    ) -> vs_20181212_models.ListCloudAppInstallationsResponse:
        """
        @summary 查询云应用安装信息列表
        
        @param request: ListCloudAppInstallationsRequest
        @return: ListCloudAppInstallationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_app_installations_with_options(request, runtime)

    async def list_cloud_app_installations_async(
        self,
        request: vs_20181212_models.ListCloudAppInstallationsRequest,
    ) -> vs_20181212_models.ListCloudAppInstallationsResponse:
        """
        @summary 查询云应用安装信息列表
        
        @param request: ListCloudAppInstallationsRequest
        @return: ListCloudAppInstallationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_app_installations_with_options_async(request, runtime)

    def list_cloud_apps_with_options(
        self,
        request: vs_20181212_models.ListCloudAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListCloudAppsResponse:
        """
        @summary 查询云应用列表
        
        @param request: ListCloudAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudAppsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudApps',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListCloudAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_apps_with_options_async(
        self,
        request: vs_20181212_models.ListCloudAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListCloudAppsResponse:
        """
        @summary 查询云应用列表
        
        @param request: ListCloudAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudAppsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudApps',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListCloudAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_apps(
        self,
        request: vs_20181212_models.ListCloudAppsRequest,
    ) -> vs_20181212_models.ListCloudAppsResponse:
        """
        @summary 查询云应用列表
        
        @param request: ListCloudAppsRequest
        @return: ListCloudAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_apps_with_options(request, runtime)

    async def list_cloud_apps_async(
        self,
        request: vs_20181212_models.ListCloudAppsRequest,
    ) -> vs_20181212_models.ListCloudAppsResponse:
        """
        @summary 查询云应用列表
        
        @param request: ListCloudAppsRequest
        @return: ListCloudAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_apps_with_options_async(request, runtime)

    def list_file_push_statuses_with_options(
        self,
        request: vs_20181212_models.ListFilePushStatusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListFilePushStatusesResponse:
        """
        @summary 查询文件的实例推送状态信息列表。
        
        @param request: ListFilePushStatusesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFilePushStatusesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFilePushStatuses',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListFilePushStatusesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_file_push_statuses_with_options_async(
        self,
        request: vs_20181212_models.ListFilePushStatusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListFilePushStatusesResponse:
        """
        @summary 查询文件的实例推送状态信息列表。
        
        @param request: ListFilePushStatusesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFilePushStatusesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFilePushStatuses',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListFilePushStatusesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_file_push_statuses(
        self,
        request: vs_20181212_models.ListFilePushStatusesRequest,
    ) -> vs_20181212_models.ListFilePushStatusesResponse:
        """
        @summary 查询文件的实例推送状态信息列表。
        
        @param request: ListFilePushStatusesRequest
        @return: ListFilePushStatusesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_file_push_statuses_with_options(request, runtime)

    async def list_file_push_statuses_async(
        self,
        request: vs_20181212_models.ListFilePushStatusesRequest,
    ) -> vs_20181212_models.ListFilePushStatusesResponse:
        """
        @summary 查询文件的实例推送状态信息列表。
        
        @param request: ListFilePushStatusesRequest
        @return: ListFilePushStatusesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_file_push_statuses_with_options_async(request, runtime)

    def list_files_with_options(
        self,
        request: vs_20181212_models.ListFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListFilesResponse:
        """
        @summary 查询可用文件列表。
        
        @param request: ListFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFilesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFiles',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_files_with_options_async(
        self,
        request: vs_20181212_models.ListFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListFilesResponse:
        """
        @summary 查询可用文件列表。
        
        @param request: ListFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFilesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFiles',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_files(
        self,
        request: vs_20181212_models.ListFilesRequest,
    ) -> vs_20181212_models.ListFilesResponse:
        """
        @summary 查询可用文件列表。
        
        @param request: ListFilesRequest
        @return: ListFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_files_with_options(request, runtime)

    async def list_files_async(
        self,
        request: vs_20181212_models.ListFilesRequest,
    ) -> vs_20181212_models.ListFilesResponse:
        """
        @summary 查询可用文件列表。
        
        @param request: ListFilesRequest
        @return: ListFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_files_with_options_async(request, runtime)

    def list_public_keys_with_options(
        self,
        request: vs_20181212_models.ListPublicKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListPublicKeysResponse:
        """
        @summary 查询公钥信息
        
        @param request: ListPublicKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicKeysResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicKeys',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListPublicKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_public_keys_with_options_async(
        self,
        request: vs_20181212_models.ListPublicKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListPublicKeysResponse:
        """
        @summary 查询公钥信息
        
        @param request: ListPublicKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublicKeysResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicKeys',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListPublicKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_public_keys(
        self,
        request: vs_20181212_models.ListPublicKeysRequest,
    ) -> vs_20181212_models.ListPublicKeysResponse:
        """
        @summary 查询公钥信息
        
        @param request: ListPublicKeysRequest
        @return: ListPublicKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_public_keys_with_options(request, runtime)

    async def list_public_keys_async(
        self,
        request: vs_20181212_models.ListPublicKeysRequest,
    ) -> vs_20181212_models.ListPublicKeysResponse:
        """
        @summary 查询公钥信息
        
        @param request: ListPublicKeysRequest
        @return: ListPublicKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_public_keys_with_options_async(request, runtime)

    def list_rendering_data_packages_with_options(
        self,
        request: vs_20181212_models.ListRenderingDataPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListRenderingDataPackagesResponse:
        """
        @summary 查询所有云应用数据包信息，支持分页查询。
        
        @param request: ListRenderingDataPackagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRenderingDataPackagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.data_package_id):
            query['DataPackageId'] = request.data_package_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRenderingDataPackages',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListRenderingDataPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rendering_data_packages_with_options_async(
        self,
        request: vs_20181212_models.ListRenderingDataPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListRenderingDataPackagesResponse:
        """
        @summary 查询所有云应用数据包信息，支持分页查询。
        
        @param request: ListRenderingDataPackagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRenderingDataPackagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.data_package_id):
            query['DataPackageId'] = request.data_package_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRenderingDataPackages',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListRenderingDataPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rendering_data_packages(
        self,
        request: vs_20181212_models.ListRenderingDataPackagesRequest,
    ) -> vs_20181212_models.ListRenderingDataPackagesResponse:
        """
        @summary 查询所有云应用数据包信息，支持分页查询。
        
        @param request: ListRenderingDataPackagesRequest
        @return: ListRenderingDataPackagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_rendering_data_packages_with_options(request, runtime)

    async def list_rendering_data_packages_async(
        self,
        request: vs_20181212_models.ListRenderingDataPackagesRequest,
    ) -> vs_20181212_models.ListRenderingDataPackagesResponse:
        """
        @summary 查询所有云应用数据包信息，支持分页查询。
        
        @param request: ListRenderingDataPackagesRequest
        @return: ListRenderingDataPackagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_rendering_data_packages_with_options_async(request, runtime)

    def list_rendering_instance_gateway_with_options(
        self,
        request: vs_20181212_models.ListRenderingInstanceGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListRenderingInstanceGatewayResponse:
        """
        @summary 查询自定义网关
        
        @param request: ListRenderingInstanceGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRenderingInstanceGatewayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.gateway_instance_id):
            query['GatewayInstanceId'] = request.gateway_instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRenderingInstanceGateway',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListRenderingInstanceGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rendering_instance_gateway_with_options_async(
        self,
        request: vs_20181212_models.ListRenderingInstanceGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListRenderingInstanceGatewayResponse:
        """
        @summary 查询自定义网关
        
        @param request: ListRenderingInstanceGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRenderingInstanceGatewayResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.gateway_instance_id):
            query['GatewayInstanceId'] = request.gateway_instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRenderingInstanceGateway',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListRenderingInstanceGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rendering_instance_gateway(
        self,
        request: vs_20181212_models.ListRenderingInstanceGatewayRequest,
    ) -> vs_20181212_models.ListRenderingInstanceGatewayResponse:
        """
        @summary 查询自定义网关
        
        @param request: ListRenderingInstanceGatewayRequest
        @return: ListRenderingInstanceGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_rendering_instance_gateway_with_options(request, runtime)

    async def list_rendering_instance_gateway_async(
        self,
        request: vs_20181212_models.ListRenderingInstanceGatewayRequest,
    ) -> vs_20181212_models.ListRenderingInstanceGatewayResponse:
        """
        @summary 查询自定义网关
        
        @param request: ListRenderingInstanceGatewayRequest
        @return: ListRenderingInstanceGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_rendering_instance_gateway_with_options_async(request, runtime)

    def list_rendering_instances_with_options(
        self,
        request: vs_20181212_models.ListRenderingInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListRenderingInstancesResponse:
        """
        @summary 查询所有云渲染实例信息，支持分页查询。
        
        @param request: ListRenderingInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRenderingInstancesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRenderingInstances',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListRenderingInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rendering_instances_with_options_async(
        self,
        request: vs_20181212_models.ListRenderingInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListRenderingInstancesResponse:
        """
        @summary 查询所有云渲染实例信息，支持分页查询。
        
        @param request: ListRenderingInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRenderingInstancesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRenderingInstances',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListRenderingInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rendering_instances(
        self,
        request: vs_20181212_models.ListRenderingInstancesRequest,
    ) -> vs_20181212_models.ListRenderingInstancesResponse:
        """
        @summary 查询所有云渲染实例信息，支持分页查询。
        
        @param request: ListRenderingInstancesRequest
        @return: ListRenderingInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_rendering_instances_with_options(request, runtime)

    async def list_rendering_instances_async(
        self,
        request: vs_20181212_models.ListRenderingInstancesRequest,
    ) -> vs_20181212_models.ListRenderingInstancesResponse:
        """
        @summary 查询所有云渲染实例信息，支持分页查询。
        
        @param request: ListRenderingInstancesRequest
        @return: ListRenderingInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_rendering_instances_with_options_async(request, runtime)

    def list_rendering_project_instances_with_options(
        self,
        request: vs_20181212_models.ListRenderingProjectInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListRenderingProjectInstancesResponse:
        """
        @summary 分页查询项目关联的云应用服务实例列表。
        
        @description ## 请求说明
        - 该接口支持通过多种筛选条件（如状态、实例ID等）来查询指定项目下的云应用服务实例。
        
        @param request: ListRenderingProjectInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRenderingProjectInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRenderingProjectInstances',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListRenderingProjectInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rendering_project_instances_with_options_async(
        self,
        request: vs_20181212_models.ListRenderingProjectInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListRenderingProjectInstancesResponse:
        """
        @summary 分页查询项目关联的云应用服务实例列表。
        
        @description ## 请求说明
        - 该接口支持通过多种筛选条件（如状态、实例ID等）来查询指定项目下的云应用服务实例。
        
        @param request: ListRenderingProjectInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRenderingProjectInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRenderingProjectInstances',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListRenderingProjectInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rendering_project_instances(
        self,
        request: vs_20181212_models.ListRenderingProjectInstancesRequest,
    ) -> vs_20181212_models.ListRenderingProjectInstancesResponse:
        """
        @summary 分页查询项目关联的云应用服务实例列表。
        
        @description ## 请求说明
        - 该接口支持通过多种筛选条件（如状态、实例ID等）来查询指定项目下的云应用服务实例。
        
        @param request: ListRenderingProjectInstancesRequest
        @return: ListRenderingProjectInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_rendering_project_instances_with_options(request, runtime)

    async def list_rendering_project_instances_async(
        self,
        request: vs_20181212_models.ListRenderingProjectInstancesRequest,
    ) -> vs_20181212_models.ListRenderingProjectInstancesResponse:
        """
        @summary 分页查询项目关联的云应用服务实例列表。
        
        @description ## 请求说明
        - 该接口支持通过多种筛选条件（如状态、实例ID等）来查询指定项目下的云应用服务实例。
        
        @param request: ListRenderingProjectInstancesRequest
        @return: ListRenderingProjectInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_rendering_project_instances_with_options_async(request, runtime)

    def list_rendering_projects_with_options(
        self,
        request: vs_20181212_models.ListRenderingProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListRenderingProjectsResponse:
        """
        @summary 分页查询用户下的云应用服务项目基本信息列表。
        
        @description ## 请求说明
        - 该接口用于分页查询指定用户下的渲染项目基本信息列表。
        - 可通过 `ProjectId` 和 `ProjectName` 进行过滤查询。
        
        @param request: ListRenderingProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRenderingProjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRenderingProjects',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListRenderingProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rendering_projects_with_options_async(
        self,
        request: vs_20181212_models.ListRenderingProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListRenderingProjectsResponse:
        """
        @summary 分页查询用户下的云应用服务项目基本信息列表。
        
        @description ## 请求说明
        - 该接口用于分页查询指定用户下的渲染项目基本信息列表。
        - 可通过 `ProjectId` 和 `ProjectName` 进行过滤查询。
        
        @param request: ListRenderingProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRenderingProjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRenderingProjects',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListRenderingProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rendering_projects(
        self,
        request: vs_20181212_models.ListRenderingProjectsRequest,
    ) -> vs_20181212_models.ListRenderingProjectsResponse:
        """
        @summary 分页查询用户下的云应用服务项目基本信息列表。
        
        @description ## 请求说明
        - 该接口用于分页查询指定用户下的渲染项目基本信息列表。
        - 可通过 `ProjectId` 和 `ProjectName` 进行过滤查询。
        
        @param request: ListRenderingProjectsRequest
        @return: ListRenderingProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_rendering_projects_with_options(request, runtime)

    async def list_rendering_projects_async(
        self,
        request: vs_20181212_models.ListRenderingProjectsRequest,
    ) -> vs_20181212_models.ListRenderingProjectsResponse:
        """
        @summary 分页查询用户下的云应用服务项目基本信息列表。
        
        @description ## 请求说明
        - 该接口用于分页查询指定用户下的渲染项目基本信息列表。
        - 可通过 `ProjectId` 和 `ProjectName` 进行过滤查询。
        
        @param request: ListRenderingProjectsRequest
        @return: ListRenderingProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_rendering_projects_with_options_async(request, runtime)

    def list_rendering_sessions_with_options(
        self,
        request: vs_20181212_models.ListRenderingSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListRenderingSessionsResponse:
        """
        @summary 分页查询指定条件下的渲染会话列表。
        
        @description ## 请求说明
        - 该接口支持通过多种参数组合来过滤和分页查询用户的渲染会话列表。
        - `SessionId` 和 `ClientId` 参数至少需要提供一个，但两者都不是必选的。如果同时提供了两个参数，则将根据这两个参数进行更精确的匹配。
        
        @param request: ListRenderingSessionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRenderingSessionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRenderingSessions',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListRenderingSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rendering_sessions_with_options_async(
        self,
        request: vs_20181212_models.ListRenderingSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ListRenderingSessionsResponse:
        """
        @summary 分页查询指定条件下的渲染会话列表。
        
        @description ## 请求说明
        - 该接口支持通过多种参数组合来过滤和分页查询用户的渲染会话列表。
        - `SessionId` 和 `ClientId` 参数至少需要提供一个，但两者都不是必选的。如果同时提供了两个参数，则将根据这两个参数进行更精确的匹配。
        
        @param request: ListRenderingSessionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRenderingSessionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRenderingSessions',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListRenderingSessionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rendering_sessions(
        self,
        request: vs_20181212_models.ListRenderingSessionsRequest,
    ) -> vs_20181212_models.ListRenderingSessionsResponse:
        """
        @summary 分页查询指定条件下的渲染会话列表。
        
        @description ## 请求说明
        - 该接口支持通过多种参数组合来过滤和分页查询用户的渲染会话列表。
        - `SessionId` 和 `ClientId` 参数至少需要提供一个，但两者都不是必选的。如果同时提供了两个参数，则将根据这两个参数进行更精确的匹配。
        
        @param request: ListRenderingSessionsRequest
        @return: ListRenderingSessionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_rendering_sessions_with_options(request, runtime)

    async def list_rendering_sessions_async(
        self,
        request: vs_20181212_models.ListRenderingSessionsRequest,
    ) -> vs_20181212_models.ListRenderingSessionsResponse:
        """
        @summary 分页查询指定条件下的渲染会话列表。
        
        @description ## 请求说明
        - 该接口支持通过多种参数组合来过滤和分页查询用户的渲染会话列表。
        - `SessionId` 和 `ClientId` 参数至少需要提供一个，但两者都不是必选的。如果同时提供了两个参数，则将根据这两个参数进行更精确的匹配。
        
        @param request: ListRenderingSessionsRequest
        @return: ListRenderingSessionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_rendering_sessions_with_options_async(request, runtime)

    def manage_login_with_options(
        self,
        request: vs_20181212_models.ManageLoginRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ManageLoginResponse:
        """
        @summary 安全登陆管理
        
        @param request: ManageLoginRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ManageLoginResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.key_group):
            query['KeyGroup'] = request.key_group
        if not UtilClient.is_unset(request.key_name):
            query['KeyName'] = request.key_name
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ManageLogin',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ManageLoginResponse(),
            self.call_api(params, req, runtime)
        )

    async def manage_login_with_options_async(
        self,
        request: vs_20181212_models.ManageLoginRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ManageLoginResponse:
        """
        @summary 安全登陆管理
        
        @param request: ManageLoginRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ManageLoginResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.key_group):
            query['KeyGroup'] = request.key_group
        if not UtilClient.is_unset(request.key_name):
            query['KeyName'] = request.key_name
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ManageLogin',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ManageLoginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manage_login(
        self,
        request: vs_20181212_models.ManageLoginRequest,
    ) -> vs_20181212_models.ManageLoginResponse:
        """
        @summary 安全登陆管理
        
        @param request: ManageLoginRequest
        @return: ManageLoginResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.manage_login_with_options(request, runtime)

    async def manage_login_async(
        self,
        request: vs_20181212_models.ManageLoginRequest,
    ) -> vs_20181212_models.ManageLoginResponse:
        """
        @summary 安全登陆管理
        
        @param request: ManageLoginRequest
        @return: ManageLoginResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.manage_login_with_options_async(request, runtime)

    def modify_device_with_options(
        self,
        request: vs_20181212_models.ModifyDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyDeviceResponse:
        """
        @param request: ModifyDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_method):
            query['AlarmMethod'] = request.alarm_method
        if not UtilClient.is_unset(request.auto_directory):
            query['AutoDirectory'] = request.auto_directory
        if not UtilClient.is_unset(request.auto_pos):
            query['AutoPos'] = request.auto_pos
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.latitude):
            query['Latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            query['Longitude'] = request.longitude
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.pos_interval):
            query['PosInterval'] = request.pos_interval
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_device_with_options_async(
        self,
        request: vs_20181212_models.ModifyDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyDeviceResponse:
        """
        @param request: ModifyDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_method):
            query['AlarmMethod'] = request.alarm_method
        if not UtilClient.is_unset(request.auto_directory):
            query['AutoDirectory'] = request.auto_directory
        if not UtilClient.is_unset(request.auto_pos):
            query['AutoPos'] = request.auto_pos
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.latitude):
            query['Latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            query['Longitude'] = request.longitude
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.pos_interval):
            query['PosInterval'] = request.pos_interval
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_device(
        self,
        request: vs_20181212_models.ModifyDeviceRequest,
    ) -> vs_20181212_models.ModifyDeviceResponse:
        """
        @param request: ModifyDeviceRequest
        @return: ModifyDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_device_with_options(request, runtime)

    async def modify_device_async(
        self,
        request: vs_20181212_models.ModifyDeviceRequest,
    ) -> vs_20181212_models.ModifyDeviceResponse:
        """
        @param request: ModifyDeviceRequest
        @return: ModifyDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_device_with_options_async(request, runtime)

    def modify_device_alarm_with_options(
        self,
        request: vs_20181212_models.ModifyDeviceAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyDeviceAlarmResponse:
        """
        @param request: ModifyDeviceAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDeviceAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDeviceAlarm',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDeviceAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_device_alarm_with_options_async(
        self,
        request: vs_20181212_models.ModifyDeviceAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyDeviceAlarmResponse:
        """
        @param request: ModifyDeviceAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDeviceAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDeviceAlarm',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDeviceAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_device_alarm(
        self,
        request: vs_20181212_models.ModifyDeviceAlarmRequest,
    ) -> vs_20181212_models.ModifyDeviceAlarmResponse:
        """
        @param request: ModifyDeviceAlarmRequest
        @return: ModifyDeviceAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_device_alarm_with_options(request, runtime)

    async def modify_device_alarm_async(
        self,
        request: vs_20181212_models.ModifyDeviceAlarmRequest,
    ) -> vs_20181212_models.ModifyDeviceAlarmResponse:
        """
        @param request: ModifyDeviceAlarmRequest
        @return: ModifyDeviceAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_device_alarm_with_options_async(request, runtime)

    def modify_device_capture_with_options(
        self,
        request: vs_20181212_models.ModifyDeviceCaptureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyDeviceCaptureResponse:
        """
        @param request: ModifyDeviceCaptureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDeviceCaptureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDeviceCapture',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDeviceCaptureResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_device_capture_with_options_async(
        self,
        request: vs_20181212_models.ModifyDeviceCaptureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyDeviceCaptureResponse:
        """
        @param request: ModifyDeviceCaptureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDeviceCaptureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDeviceCapture',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDeviceCaptureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_device_capture(
        self,
        request: vs_20181212_models.ModifyDeviceCaptureRequest,
    ) -> vs_20181212_models.ModifyDeviceCaptureResponse:
        """
        @param request: ModifyDeviceCaptureRequest
        @return: ModifyDeviceCaptureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_device_capture_with_options(request, runtime)

    async def modify_device_capture_async(
        self,
        request: vs_20181212_models.ModifyDeviceCaptureRequest,
    ) -> vs_20181212_models.ModifyDeviceCaptureResponse:
        """
        @param request: ModifyDeviceCaptureRequest
        @return: ModifyDeviceCaptureResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_device_capture_with_options_async(request, runtime)

    def modify_device_channels_with_options(
        self,
        request: vs_20181212_models.ModifyDeviceChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyDeviceChannelsResponse:
        """
        @param request: ModifyDeviceChannelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDeviceChannelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channels):
            query['Channels'] = request.channels
        if not UtilClient.is_unset(request.device_status):
            query['DeviceStatus'] = request.device_status
        if not UtilClient.is_unset(request.dsn):
            query['Dsn'] = request.dsn
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDeviceChannels',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDeviceChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_device_channels_with_options_async(
        self,
        request: vs_20181212_models.ModifyDeviceChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyDeviceChannelsResponse:
        """
        @param request: ModifyDeviceChannelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDeviceChannelsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channels):
            query['Channels'] = request.channels
        if not UtilClient.is_unset(request.device_status):
            query['DeviceStatus'] = request.device_status
        if not UtilClient.is_unset(request.dsn):
            query['Dsn'] = request.dsn
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDeviceChannels',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDeviceChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_device_channels(
        self,
        request: vs_20181212_models.ModifyDeviceChannelsRequest,
    ) -> vs_20181212_models.ModifyDeviceChannelsResponse:
        """
        @param request: ModifyDeviceChannelsRequest
        @return: ModifyDeviceChannelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_device_channels_with_options(request, runtime)

    async def modify_device_channels_async(
        self,
        request: vs_20181212_models.ModifyDeviceChannelsRequest,
    ) -> vs_20181212_models.ModifyDeviceChannelsResponse:
        """
        @param request: ModifyDeviceChannelsRequest
        @return: ModifyDeviceChannelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_device_channels_with_options_async(request, runtime)

    def modify_directory_with_options(
        self,
        request: vs_20181212_models.ModifyDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyDirectoryResponse:
        """
        @param request: ModifyDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_directory_with_options_async(
        self,
        request: vs_20181212_models.ModifyDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyDirectoryResponse:
        """
        @param request: ModifyDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_directory(
        self,
        request: vs_20181212_models.ModifyDirectoryRequest,
    ) -> vs_20181212_models.ModifyDirectoryResponse:
        """
        @param request: ModifyDirectoryRequest
        @return: ModifyDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_directory_with_options(request, runtime)

    async def modify_directory_async(
        self,
        request: vs_20181212_models.ModifyDirectoryRequest,
    ) -> vs_20181212_models.ModifyDirectoryResponse:
        """
        @param request: ModifyDirectoryRequest
        @return: ModifyDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_directory_with_options_async(request, runtime)

    def modify_group_with_options(
        self,
        request: vs_20181212_models.ModifyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyGroupResponse:
        """
        @param request: ModifyGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.in_protocol):
            query['InProtocol'] = request.in_protocol
        if not UtilClient.is_unset(request.lazy_pull):
            query['LazyPull'] = request.lazy_pull
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.push_domain):
            query['PushDomain'] = request.push_domain
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGroup',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_group_with_options_async(
        self,
        request: vs_20181212_models.ModifyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyGroupResponse:
        """
        @param request: ModifyGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.in_protocol):
            query['InProtocol'] = request.in_protocol
        if not UtilClient.is_unset(request.lazy_pull):
            query['LazyPull'] = request.lazy_pull
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.push_domain):
            query['PushDomain'] = request.push_domain
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGroup',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_group(
        self,
        request: vs_20181212_models.ModifyGroupRequest,
    ) -> vs_20181212_models.ModifyGroupResponse:
        """
        @param request: ModifyGroupRequest
        @return: ModifyGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_group_with_options(request, runtime)

    async def modify_group_async(
        self,
        request: vs_20181212_models.ModifyGroupRequest,
    ) -> vs_20181212_models.ModifyGroupResponse:
        """
        @param request: ModifyGroupRequest
        @return: ModifyGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_group_with_options_async(request, runtime)

    def modify_parent_platform_with_options(
        self,
        request: vs_20181212_models.ModifyParentPlatformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyParentPlatformResponse:
        """
        @param request: ModifyParentPlatformRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyParentPlatformResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.client_auth):
            query['ClientAuth'] = request.client_auth
        if not UtilClient.is_unset(request.client_password):
            query['ClientPassword'] = request.client_password
        if not UtilClient.is_unset(request.client_username):
            query['ClientUsername'] = request.client_username
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyParentPlatform',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyParentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_parent_platform_with_options_async(
        self,
        request: vs_20181212_models.ModifyParentPlatformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyParentPlatformResponse:
        """
        @param request: ModifyParentPlatformRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyParentPlatformResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.client_auth):
            query['ClientAuth'] = request.client_auth
        if not UtilClient.is_unset(request.client_password):
            query['ClientPassword'] = request.client_password
        if not UtilClient.is_unset(request.client_username):
            query['ClientUsername'] = request.client_username
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyParentPlatform',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyParentPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_parent_platform(
        self,
        request: vs_20181212_models.ModifyParentPlatformRequest,
    ) -> vs_20181212_models.ModifyParentPlatformResponse:
        """
        @param request: ModifyParentPlatformRequest
        @return: ModifyParentPlatformResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_parent_platform_with_options(request, runtime)

    async def modify_parent_platform_async(
        self,
        request: vs_20181212_models.ModifyParentPlatformRequest,
    ) -> vs_20181212_models.ModifyParentPlatformResponse:
        """
        @param request: ModifyParentPlatformRequest
        @return: ModifyParentPlatformResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_parent_platform_with_options_async(request, runtime)

    def modify_rendering_instance_with_options(
        self,
        request: vs_20181212_models.ModifyRenderingInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyRenderingInstanceResponse:
        """
        @summary 变配云渲染资源实例
        
        @param request: ModifyRenderingInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRenderingInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not UtilClient.is_unset(request.rendering_spec):
            query['RenderingSpec'] = request.rendering_spec
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRenderingInstance',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyRenderingInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rendering_instance_with_options_async(
        self,
        request: vs_20181212_models.ModifyRenderingInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyRenderingInstanceResponse:
        """
        @summary 变配云渲染资源实例
        
        @param request: ModifyRenderingInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRenderingInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not UtilClient.is_unset(request.rendering_spec):
            query['RenderingSpec'] = request.rendering_spec
        if not UtilClient.is_unset(request.storage_size):
            query['StorageSize'] = request.storage_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRenderingInstance',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyRenderingInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rendering_instance(
        self,
        request: vs_20181212_models.ModifyRenderingInstanceRequest,
    ) -> vs_20181212_models.ModifyRenderingInstanceResponse:
        """
        @summary 变配云渲染资源实例
        
        @param request: ModifyRenderingInstanceRequest
        @return: ModifyRenderingInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_rendering_instance_with_options(request, runtime)

    async def modify_rendering_instance_async(
        self,
        request: vs_20181212_models.ModifyRenderingInstanceRequest,
    ) -> vs_20181212_models.ModifyRenderingInstanceResponse:
        """
        @summary 变配云渲染资源实例
        
        @param request: ModifyRenderingInstanceRequest
        @return: ModifyRenderingInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_rendering_instance_with_options_async(request, runtime)

    def modify_rendering_instance_bandwidth_with_options(
        self,
        request: vs_20181212_models.ModifyRenderingInstanceBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyRenderingInstanceBandwidthResponse:
        """
        @summary 修改云渲染实例限速带宽
        
        @param request: ModifyRenderingInstanceBandwidthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRenderingInstanceBandwidthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_egress_bandwidth):
            query['MaxEgressBandwidth'] = request.max_egress_bandwidth
        if not UtilClient.is_unset(request.max_ingress_bandwidth):
            query['MaxIngressBandwidth'] = request.max_ingress_bandwidth
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRenderingInstanceBandwidth',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyRenderingInstanceBandwidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rendering_instance_bandwidth_with_options_async(
        self,
        request: vs_20181212_models.ModifyRenderingInstanceBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyRenderingInstanceBandwidthResponse:
        """
        @summary 修改云渲染实例限速带宽
        
        @param request: ModifyRenderingInstanceBandwidthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyRenderingInstanceBandwidthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_egress_bandwidth):
            query['MaxEgressBandwidth'] = request.max_egress_bandwidth
        if not UtilClient.is_unset(request.max_ingress_bandwidth):
            query['MaxIngressBandwidth'] = request.max_ingress_bandwidth
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyRenderingInstanceBandwidth',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyRenderingInstanceBandwidthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rendering_instance_bandwidth(
        self,
        request: vs_20181212_models.ModifyRenderingInstanceBandwidthRequest,
    ) -> vs_20181212_models.ModifyRenderingInstanceBandwidthResponse:
        """
        @summary 修改云渲染实例限速带宽
        
        @param request: ModifyRenderingInstanceBandwidthRequest
        @return: ModifyRenderingInstanceBandwidthResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_rendering_instance_bandwidth_with_options(request, runtime)

    async def modify_rendering_instance_bandwidth_async(
        self,
        request: vs_20181212_models.ModifyRenderingInstanceBandwidthRequest,
    ) -> vs_20181212_models.ModifyRenderingInstanceBandwidthResponse:
        """
        @summary 修改云渲染实例限速带宽
        
        @param request: ModifyRenderingInstanceBandwidthRequest
        @return: ModifyRenderingInstanceBandwidthResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_rendering_instance_bandwidth_with_options_async(request, runtime)

    def modify_template_with_options(
        self,
        request: vs_20181212_models.ModifyTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyTemplateResponse:
        """
        @param request: ModifyTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_format):
            query['FileFormat'] = request.file_format
        if not UtilClient.is_unset(request.flv):
            query['Flv'] = request.flv
        if not UtilClient.is_unset(request.hls_m3u_8):
            query['HlsM3u8'] = request.hls_m3u_8
        if not UtilClient.is_unset(request.hls_ts):
            query['HlsTs'] = request.hls_ts
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.jpg_on_demand):
            query['JpgOnDemand'] = request.jpg_on_demand
        if not UtilClient.is_unset(request.jpg_overwrite):
            query['JpgOverwrite'] = request.jpg_overwrite
        if not UtilClient.is_unset(request.jpg_sequence):
            query['JpgSequence'] = request.jpg_sequence
        if not UtilClient.is_unset(request.mp_4):
            query['Mp4'] = request.mp_4
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.trans_configs_json):
            query['TransConfigsJSON'] = request.trans_configs_json
        if not UtilClient.is_unset(request.trigger):
            query['Trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_template_with_options_async(
        self,
        request: vs_20181212_models.ModifyTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ModifyTemplateResponse:
        """
        @param request: ModifyTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_format):
            query['FileFormat'] = request.file_format
        if not UtilClient.is_unset(request.flv):
            query['Flv'] = request.flv
        if not UtilClient.is_unset(request.hls_m3u_8):
            query['HlsM3u8'] = request.hls_m3u_8
        if not UtilClient.is_unset(request.hls_ts):
            query['HlsTs'] = request.hls_ts
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.jpg_on_demand):
            query['JpgOnDemand'] = request.jpg_on_demand
        if not UtilClient.is_unset(request.jpg_overwrite):
            query['JpgOverwrite'] = request.jpg_overwrite
        if not UtilClient.is_unset(request.jpg_sequence):
            query['JpgSequence'] = request.jpg_sequence
        if not UtilClient.is_unset(request.mp_4):
            query['Mp4'] = request.mp_4
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.trans_configs_json):
            query['TransConfigsJSON'] = request.trans_configs_json
        if not UtilClient.is_unset(request.trigger):
            query['Trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_template(
        self,
        request: vs_20181212_models.ModifyTemplateRequest,
    ) -> vs_20181212_models.ModifyTemplateResponse:
        """
        @param request: ModifyTemplateRequest
        @return: ModifyTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_template_with_options(request, runtime)

    async def modify_template_async(
        self,
        request: vs_20181212_models.ModifyTemplateRequest,
    ) -> vs_20181212_models.ModifyTemplateResponse:
        """
        @param request: ModifyTemplateRequest
        @return: ModifyTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_template_with_options_async(request, runtime)

    def open_vs_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.OpenVsServiceResponse:
        """
        @param request: OpenVsServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenVsServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenVsService',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.OpenVsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_vs_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.OpenVsServiceResponse:
        """
        @param request: OpenVsServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenVsServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenVsService',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.OpenVsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_vs_service(self) -> vs_20181212_models.OpenVsServiceResponse:
        """
        @return: OpenVsServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_vs_service_with_options(runtime)

    async def open_vs_service_async(self) -> vs_20181212_models.OpenVsServiceResponse:
        """
        @return: OpenVsServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_vs_service_with_options_async(runtime)

    def push_file_with_options(
        self,
        request: vs_20181212_models.PushFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.PushFileResponse:
        """
        @summary 预推文件到云渲染实例。
        
        @param request: PushFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushFile',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.PushFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_file_with_options_async(
        self,
        request: vs_20181212_models.PushFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.PushFileResponse:
        """
        @summary 预推文件到云渲染实例。
        
        @param request: PushFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushFile',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.PushFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_file(
        self,
        request: vs_20181212_models.PushFileRequest,
    ) -> vs_20181212_models.PushFileResponse:
        """
        @summary 预推文件到云渲染实例。
        
        @param request: PushFileRequest
        @return: PushFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.push_file_with_options(request, runtime)

    async def push_file_async(
        self,
        request: vs_20181212_models.PushFileRequest,
    ) -> vs_20181212_models.PushFileResponse:
        """
        @summary 预推文件到云渲染实例。
        
        @param request: PushFileRequest
        @return: PushFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.push_file_with_options_async(request, runtime)

    def reboot_rendering_instance_with_options(
        self,
        request: vs_20181212_models.RebootRenderingInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.RebootRenderingInstanceResponse:
        """
        @summary 重启云渲染实例
        
        @param request: RebootRenderingInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebootRenderingInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootRenderingInstance',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.RebootRenderingInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_rendering_instance_with_options_async(
        self,
        request: vs_20181212_models.RebootRenderingInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.RebootRenderingInstanceResponse:
        """
        @summary 重启云渲染实例
        
        @param request: RebootRenderingInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebootRenderingInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootRenderingInstance',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.RebootRenderingInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_rendering_instance(
        self,
        request: vs_20181212_models.RebootRenderingInstanceRequest,
    ) -> vs_20181212_models.RebootRenderingInstanceResponse:
        """
        @summary 重启云渲染实例
        
        @param request: RebootRenderingInstanceRequest
        @return: RebootRenderingInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reboot_rendering_instance_with_options(request, runtime)

    async def reboot_rendering_instance_async(
        self,
        request: vs_20181212_models.RebootRenderingInstanceRequest,
    ) -> vs_20181212_models.RebootRenderingInstanceResponse:
        """
        @summary 重启云渲染实例
        
        @param request: RebootRenderingInstanceRequest
        @return: RebootRenderingInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reboot_rendering_instance_with_options_async(request, runtime)

    def recover_rendering_data_package_with_options(
        self,
        request: vs_20181212_models.RecoverRenderingDataPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.RecoverRenderingDataPackageResponse:
        """
        @summary 恢复数据到云渲染实例
        
        @param request: RecoverRenderingDataPackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecoverRenderingDataPackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_package_id):
            query['DataPackageId'] = request.data_package_id
        if not UtilClient.is_unset(request.load_mode):
            query['LoadMode'] = request.load_mode
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoverRenderingDataPackage',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.RecoverRenderingDataPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def recover_rendering_data_package_with_options_async(
        self,
        request: vs_20181212_models.RecoverRenderingDataPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.RecoverRenderingDataPackageResponse:
        """
        @summary 恢复数据到云渲染实例
        
        @param request: RecoverRenderingDataPackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecoverRenderingDataPackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_package_id):
            query['DataPackageId'] = request.data_package_id
        if not UtilClient.is_unset(request.load_mode):
            query['LoadMode'] = request.load_mode
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecoverRenderingDataPackage',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.RecoverRenderingDataPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recover_rendering_data_package(
        self,
        request: vs_20181212_models.RecoverRenderingDataPackageRequest,
    ) -> vs_20181212_models.RecoverRenderingDataPackageResponse:
        """
        @summary 恢复数据到云渲染实例
        
        @param request: RecoverRenderingDataPackageRequest
        @return: RecoverRenderingDataPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.recover_rendering_data_package_with_options(request, runtime)

    async def recover_rendering_data_package_async(
        self,
        request: vs_20181212_models.RecoverRenderingDataPackageRequest,
    ) -> vs_20181212_models.RecoverRenderingDataPackageResponse:
        """
        @summary 恢复数据到云渲染实例
        
        @param request: RecoverRenderingDataPackageRequest
        @return: RecoverRenderingDataPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.recover_rendering_data_package_with_options_async(request, runtime)

    def refresh_rendering_instance_streaming_with_options(
        self,
        tmp_req: vs_20181212_models.RefreshRenderingInstanceStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.RefreshRenderingInstanceStreamingResponse:
        """
        @summary 更新实例流连接信息
        
        @param tmp_req: RefreshRenderingInstanceStreamingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshRenderingInstanceStreamingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.RefreshRenderingInstanceStreamingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_info):
            request.client_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_info, 'ClientInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_info_shrink):
            query['ClientInfo'] = request.client_info_shrink
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshRenderingInstanceStreaming',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.RefreshRenderingInstanceStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_rendering_instance_streaming_with_options_async(
        self,
        tmp_req: vs_20181212_models.RefreshRenderingInstanceStreamingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.RefreshRenderingInstanceStreamingResponse:
        """
        @summary 更新实例流连接信息
        
        @param tmp_req: RefreshRenderingInstanceStreamingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshRenderingInstanceStreamingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.RefreshRenderingInstanceStreamingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_info):
            request.client_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_info, 'ClientInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_info_shrink):
            query['ClientInfo'] = request.client_info_shrink
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshRenderingInstanceStreaming',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.RefreshRenderingInstanceStreamingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_rendering_instance_streaming(
        self,
        request: vs_20181212_models.RefreshRenderingInstanceStreamingRequest,
    ) -> vs_20181212_models.RefreshRenderingInstanceStreamingResponse:
        """
        @summary 更新实例流连接信息
        
        @param request: RefreshRenderingInstanceStreamingRequest
        @return: RefreshRenderingInstanceStreamingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_rendering_instance_streaming_with_options(request, runtime)

    async def refresh_rendering_instance_streaming_async(
        self,
        request: vs_20181212_models.RefreshRenderingInstanceStreamingRequest,
    ) -> vs_20181212_models.RefreshRenderingInstanceStreamingResponse:
        """
        @summary 更新实例流连接信息
        
        @param request: RefreshRenderingInstanceStreamingRequest
        @return: RefreshRenderingInstanceStreamingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.refresh_rendering_instance_streaming_with_options_async(request, runtime)

    def release_rendering_data_package_with_options(
        self,
        request: vs_20181212_models.ReleaseRenderingDataPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ReleaseRenderingDataPackageResponse:
        """
        @summary 释放云渲染数据包
        
        @param request: ReleaseRenderingDataPackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseRenderingDataPackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_package_id):
            query['DataPackageId'] = request.data_package_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseRenderingDataPackage',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ReleaseRenderingDataPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_rendering_data_package_with_options_async(
        self,
        request: vs_20181212_models.ReleaseRenderingDataPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ReleaseRenderingDataPackageResponse:
        """
        @summary 释放云渲染数据包
        
        @param request: ReleaseRenderingDataPackageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseRenderingDataPackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_package_id):
            query['DataPackageId'] = request.data_package_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseRenderingDataPackage',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ReleaseRenderingDataPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_rendering_data_package(
        self,
        request: vs_20181212_models.ReleaseRenderingDataPackageRequest,
    ) -> vs_20181212_models.ReleaseRenderingDataPackageResponse:
        """
        @summary 释放云渲染数据包
        
        @param request: ReleaseRenderingDataPackageRequest
        @return: ReleaseRenderingDataPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_rendering_data_package_with_options(request, runtime)

    async def release_rendering_data_package_async(
        self,
        request: vs_20181212_models.ReleaseRenderingDataPackageRequest,
    ) -> vs_20181212_models.ReleaseRenderingDataPackageResponse:
        """
        @summary 释放云渲染数据包
        
        @param request: ReleaseRenderingDataPackageRequest
        @return: ReleaseRenderingDataPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_rendering_data_package_with_options_async(request, runtime)

    def release_rendering_instance_with_options(
        self,
        request: vs_20181212_models.ReleaseRenderingInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ReleaseRenderingInstanceResponse:
        """
        @summary 释放云渲染实例
        
        @param request: ReleaseRenderingInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseRenderingInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseRenderingInstance',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ReleaseRenderingInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_rendering_instance_with_options_async(
        self,
        request: vs_20181212_models.ReleaseRenderingInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ReleaseRenderingInstanceResponse:
        """
        @summary 释放云渲染实例
        
        @param request: ReleaseRenderingInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseRenderingInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseRenderingInstance',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ReleaseRenderingInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_rendering_instance(
        self,
        request: vs_20181212_models.ReleaseRenderingInstanceRequest,
    ) -> vs_20181212_models.ReleaseRenderingInstanceResponse:
        """
        @summary 释放云渲染实例
        
        @param request: ReleaseRenderingInstanceRequest
        @return: ReleaseRenderingInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_rendering_instance_with_options(request, runtime)

    async def release_rendering_instance_async(
        self,
        request: vs_20181212_models.ReleaseRenderingInstanceRequest,
    ) -> vs_20181212_models.ReleaseRenderingInstanceResponse:
        """
        @summary 释放云渲染实例
        
        @param request: ReleaseRenderingInstanceRequest
        @return: ReleaseRenderingInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_rendering_instance_with_options_async(request, runtime)

    def renew_rendering_instance_with_options(
        self,
        request: vs_20181212_models.RenewRenderingInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.RenewRenderingInstanceResponse:
        """
        @summary 续费云渲染资源实例
        
        @param request: RenewRenderingInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewRenderingInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewRenderingInstance',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.RenewRenderingInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_rendering_instance_with_options_async(
        self,
        request: vs_20181212_models.RenewRenderingInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.RenewRenderingInstanceResponse:
        """
        @summary 续费云渲染资源实例
        
        @param request: RenewRenderingInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewRenderingInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewRenderingInstance',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.RenewRenderingInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_rendering_instance(
        self,
        request: vs_20181212_models.RenewRenderingInstanceRequest,
    ) -> vs_20181212_models.RenewRenderingInstanceResponse:
        """
        @summary 续费云渲染资源实例
        
        @param request: RenewRenderingInstanceRequest
        @return: RenewRenderingInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_rendering_instance_with_options(request, runtime)

    async def renew_rendering_instance_async(
        self,
        request: vs_20181212_models.RenewRenderingInstanceRequest,
    ) -> vs_20181212_models.RenewRenderingInstanceResponse:
        """
        @summary 续费云渲染资源实例
        
        @param request: RenewRenderingInstanceRequest
        @return: RenewRenderingInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_rendering_instance_with_options_async(request, runtime)

    def reset_rendering_instance_with_options(
        self,
        request: vs_20181212_models.ResetRenderingInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ResetRenderingInstanceResponse:
        """
        @summary 重置云渲染实例
        
        @param request: ResetRenderingInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetRenderingInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.data_package_id):
            query['DataPackageId'] = request.data_package_id
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetRenderingInstance',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ResetRenderingInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_rendering_instance_with_options_async(
        self,
        request: vs_20181212_models.ResetRenderingInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ResetRenderingInstanceResponse:
        """
        @summary 重置云渲染实例
        
        @param request: ResetRenderingInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetRenderingInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.data_package_id):
            query['DataPackageId'] = request.data_package_id
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetRenderingInstance',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ResetRenderingInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_rendering_instance(
        self,
        request: vs_20181212_models.ResetRenderingInstanceRequest,
    ) -> vs_20181212_models.ResetRenderingInstanceResponse:
        """
        @summary 重置云渲染实例
        
        @param request: ResetRenderingInstanceRequest
        @return: ResetRenderingInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_rendering_instance_with_options(request, runtime)

    async def reset_rendering_instance_async(
        self,
        request: vs_20181212_models.ResetRenderingInstanceRequest,
    ) -> vs_20181212_models.ResetRenderingInstanceResponse:
        """
        @summary 重置云渲染实例
        
        @param request: ResetRenderingInstanceRequest
        @return: ResetRenderingInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_rendering_instance_with_options_async(request, runtime)

    def resume_vs_stream_with_options(
        self,
        request: vs_20181212_models.ResumeVsStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ResumeVsStreamResponse:
        """
        @param request: ResumeVsStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeVsStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeVsStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ResumeVsStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_vs_stream_with_options_async(
        self,
        request: vs_20181212_models.ResumeVsStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.ResumeVsStreamResponse:
        """
        @param request: ResumeVsStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeVsStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeVsStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ResumeVsStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_vs_stream(
        self,
        request: vs_20181212_models.ResumeVsStreamRequest,
    ) -> vs_20181212_models.ResumeVsStreamResponse:
        """
        @param request: ResumeVsStreamRequest
        @return: ResumeVsStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_vs_stream_with_options(request, runtime)

    async def resume_vs_stream_async(
        self,
        request: vs_20181212_models.ResumeVsStreamRequest,
    ) -> vs_20181212_models.ResumeVsStreamResponse:
        """
        @param request: ResumeVsStreamRequest
        @return: ResumeVsStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resume_vs_stream_with_options_async(request, runtime)

    def send_rendering_instance_commands_with_options(
        self,
        request: vs_20181212_models.SendRenderingInstanceCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.SendRenderingInstanceCommandsResponse:
        """
        @summary 下发shell命令，支持同步/异步响应命令。
        
        @param request: SendRenderingInstanceCommandsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendRenderingInstanceCommandsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        body = {}
        if not UtilClient.is_unset(request.commands):
            body['Commands'] = request.commands
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendRenderingInstanceCommands',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.SendRenderingInstanceCommandsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_rendering_instance_commands_with_options_async(
        self,
        request: vs_20181212_models.SendRenderingInstanceCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.SendRenderingInstanceCommandsResponse:
        """
        @summary 下发shell命令，支持同步/异步响应命令。
        
        @param request: SendRenderingInstanceCommandsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendRenderingInstanceCommandsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        body = {}
        if not UtilClient.is_unset(request.commands):
            body['Commands'] = request.commands
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendRenderingInstanceCommands',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.SendRenderingInstanceCommandsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_rendering_instance_commands(
        self,
        request: vs_20181212_models.SendRenderingInstanceCommandsRequest,
    ) -> vs_20181212_models.SendRenderingInstanceCommandsResponse:
        """
        @summary 下发shell命令，支持同步/异步响应命令。
        
        @param request: SendRenderingInstanceCommandsRequest
        @return: SendRenderingInstanceCommandsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_rendering_instance_commands_with_options(request, runtime)

    async def send_rendering_instance_commands_async(
        self,
        request: vs_20181212_models.SendRenderingInstanceCommandsRequest,
    ) -> vs_20181212_models.SendRenderingInstanceCommandsResponse:
        """
        @summary 下发shell命令，支持同步/异步响应命令。
        
        @param request: SendRenderingInstanceCommandsRequest
        @return: SendRenderingInstanceCommandsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_rendering_instance_commands_with_options_async(request, runtime)

    def set_preset_with_options(
        self,
        request: vs_20181212_models.SetPresetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.SetPresetResponse:
        """
        @param request: SetPresetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPresetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preset_id):
            query['PresetId'] = request.preset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPreset',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.SetPresetResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_preset_with_options_async(
        self,
        request: vs_20181212_models.SetPresetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.SetPresetResponse:
        """
        @param request: SetPresetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPresetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preset_id):
            query['PresetId'] = request.preset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPreset',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.SetPresetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_preset(
        self,
        request: vs_20181212_models.SetPresetRequest,
    ) -> vs_20181212_models.SetPresetResponse:
        """
        @param request: SetPresetRequest
        @return: SetPresetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_preset_with_options(request, runtime)

    async def set_preset_async(
        self,
        request: vs_20181212_models.SetPresetRequest,
    ) -> vs_20181212_models.SetPresetResponse:
        """
        @param request: SetPresetRequest
        @return: SetPresetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_preset_with_options_async(request, runtime)

    def set_vs_domain_certificate_with_options(
        self,
        request: vs_20181212_models.SetVsDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.SetVsDomainCertificateResponse:
        """
        @param request: SetVsDomainCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetVsDomainCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.force_set):
            query['ForceSet'] = request.force_set
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not UtilClient.is_unset(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetVsDomainCertificate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.SetVsDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_vs_domain_certificate_with_options_async(
        self,
        request: vs_20181212_models.SetVsDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.SetVsDomainCertificateResponse:
        """
        @param request: SetVsDomainCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetVsDomainCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.force_set):
            query['ForceSet'] = request.force_set
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not UtilClient.is_unset(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetVsDomainCertificate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.SetVsDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_vs_domain_certificate(
        self,
        request: vs_20181212_models.SetVsDomainCertificateRequest,
    ) -> vs_20181212_models.SetVsDomainCertificateResponse:
        """
        @param request: SetVsDomainCertificateRequest
        @return: SetVsDomainCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_vs_domain_certificate_with_options(request, runtime)

    async def set_vs_domain_certificate_async(
        self,
        request: vs_20181212_models.SetVsDomainCertificateRequest,
    ) -> vs_20181212_models.SetVsDomainCertificateResponse:
        """
        @param request: SetVsDomainCertificateRequest
        @return: SetVsDomainCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_vs_domain_certificate_with_options_async(request, runtime)

    def set_vs_streams_notify_url_config_with_options(
        self,
        request: vs_20181212_models.SetVsStreamsNotifyUrlConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.SetVsStreamsNotifyUrlConfigResponse:
        """
        @param request: SetVsStreamsNotifyUrlConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetVsStreamsNotifyUrlConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetVsStreamsNotifyUrlConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.SetVsStreamsNotifyUrlConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_vs_streams_notify_url_config_with_options_async(
        self,
        request: vs_20181212_models.SetVsStreamsNotifyUrlConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.SetVsStreamsNotifyUrlConfigResponse:
        """
        @param request: SetVsStreamsNotifyUrlConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetVsStreamsNotifyUrlConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetVsStreamsNotifyUrlConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.SetVsStreamsNotifyUrlConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_vs_streams_notify_url_config(
        self,
        request: vs_20181212_models.SetVsStreamsNotifyUrlConfigRequest,
    ) -> vs_20181212_models.SetVsStreamsNotifyUrlConfigResponse:
        """
        @param request: SetVsStreamsNotifyUrlConfigRequest
        @return: SetVsStreamsNotifyUrlConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_vs_streams_notify_url_config_with_options(request, runtime)

    async def set_vs_streams_notify_url_config_async(
        self,
        request: vs_20181212_models.SetVsStreamsNotifyUrlConfigRequest,
    ) -> vs_20181212_models.SetVsStreamsNotifyUrlConfigResponse:
        """
        @param request: SetVsStreamsNotifyUrlConfigRequest
        @return: SetVsStreamsNotifyUrlConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_vs_streams_notify_url_config_with_options_async(request, runtime)

    def start_device_with_options(
        self,
        request: vs_20181212_models.StartDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StartDeviceResponse:
        """
        @param request: StartDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_device_with_options_async(
        self,
        request: vs_20181212_models.StartDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StartDeviceResponse:
        """
        @param request: StartDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_device(
        self,
        request: vs_20181212_models.StartDeviceRequest,
    ) -> vs_20181212_models.StartDeviceResponse:
        """
        @param request: StartDeviceRequest
        @return: StartDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_device_with_options(request, runtime)

    async def start_device_async(
        self,
        request: vs_20181212_models.StartDeviceRequest,
    ) -> vs_20181212_models.StartDeviceResponse:
        """
        @param request: StartDeviceRequest
        @return: StartDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_device_with_options_async(request, runtime)

    def start_parent_platform_with_options(
        self,
        request: vs_20181212_models.StartParentPlatformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StartParentPlatformResponse:
        """
        @param request: StartParentPlatformRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartParentPlatformResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartParentPlatform',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartParentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_parent_platform_with_options_async(
        self,
        request: vs_20181212_models.StartParentPlatformRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StartParentPlatformResponse:
        """
        @param request: StartParentPlatformRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartParentPlatformResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartParentPlatform',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartParentPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_parent_platform(
        self,
        request: vs_20181212_models.StartParentPlatformRequest,
    ) -> vs_20181212_models.StartParentPlatformResponse:
        """
        @param request: StartParentPlatformRequest
        @return: StartParentPlatformResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_parent_platform_with_options(request, runtime)

    async def start_parent_platform_async(
        self,
        request: vs_20181212_models.StartParentPlatformRequest,
    ) -> vs_20181212_models.StartParentPlatformResponse:
        """
        @param request: StartParentPlatformRequest
        @return: StartParentPlatformResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_parent_platform_with_options_async(request, runtime)

    def start_publish_stream_with_options(
        self,
        request: vs_20181212_models.StartPublishStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StartPublishStreamResponse:
        """
        @param request: StartPublishStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartPublishStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.publish_url):
            query['PublishUrl'] = request.publish_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartPublishStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartPublishStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_publish_stream_with_options_async(
        self,
        request: vs_20181212_models.StartPublishStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StartPublishStreamResponse:
        """
        @param request: StartPublishStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartPublishStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.publish_url):
            query['PublishUrl'] = request.publish_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartPublishStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartPublishStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_publish_stream(
        self,
        request: vs_20181212_models.StartPublishStreamRequest,
    ) -> vs_20181212_models.StartPublishStreamResponse:
        """
        @param request: StartPublishStreamRequest
        @return: StartPublishStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_publish_stream_with_options(request, runtime)

    async def start_publish_stream_async(
        self,
        request: vs_20181212_models.StartPublishStreamRequest,
    ) -> vs_20181212_models.StartPublishStreamResponse:
        """
        @param request: StartPublishStreamRequest
        @return: StartPublishStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_publish_stream_with_options_async(request, runtime)

    def start_record_stream_with_options(
        self,
        request: vs_20181212_models.StartRecordStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StartRecordStreamResponse:
        """
        @param request: StartRecordStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartRecordStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRecordStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartRecordStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_record_stream_with_options_async(
        self,
        request: vs_20181212_models.StartRecordStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StartRecordStreamResponse:
        """
        @param request: StartRecordStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartRecordStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRecordStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartRecordStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_record_stream(
        self,
        request: vs_20181212_models.StartRecordStreamRequest,
    ) -> vs_20181212_models.StartRecordStreamResponse:
        """
        @param request: StartRecordStreamRequest
        @return: StartRecordStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_record_stream_with_options(request, runtime)

    async def start_record_stream_async(
        self,
        request: vs_20181212_models.StartRecordStreamRequest,
    ) -> vs_20181212_models.StartRecordStreamResponse:
        """
        @param request: StartRecordStreamRequest
        @return: StartRecordStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_record_stream_with_options_async(request, runtime)

    def start_rendering_session_with_options(
        self,
        tmp_req: vs_20181212_models.StartRenderingSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StartRenderingSessionResponse:
        """
        @summary 调度一个空闲云应用服务实例，并完成服务启动。
        
        @param tmp_req: StartRenderingSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartRenderingSessionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.StartRenderingSessionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_params):
            request.client_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_params, 'ClientParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_params_shrink):
            query['ClientParams'] = request.client_params_shrink
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRenderingSession',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartRenderingSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_rendering_session_with_options_async(
        self,
        tmp_req: vs_20181212_models.StartRenderingSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StartRenderingSessionResponse:
        """
        @summary 调度一个空闲云应用服务实例，并完成服务启动。
        
        @param tmp_req: StartRenderingSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartRenderingSessionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.StartRenderingSessionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.client_params):
            request.client_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.client_params, 'ClientParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_params_shrink):
            query['ClientParams'] = request.client_params_shrink
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRenderingSession',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartRenderingSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_rendering_session(
        self,
        request: vs_20181212_models.StartRenderingSessionRequest,
    ) -> vs_20181212_models.StartRenderingSessionResponse:
        """
        @summary 调度一个空闲云应用服务实例，并完成服务启动。
        
        @param request: StartRenderingSessionRequest
        @return: StartRenderingSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_rendering_session_with_options(request, runtime)

    async def start_rendering_session_async(
        self,
        request: vs_20181212_models.StartRenderingSessionRequest,
    ) -> vs_20181212_models.StartRenderingSessionResponse:
        """
        @summary 调度一个空闲云应用服务实例，并完成服务启动。
        
        @param request: StartRenderingSessionRequest
        @return: StartRenderingSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_rendering_session_with_options_async(request, runtime)

    def start_stream_with_options(
        self,
        request: vs_20181212_models.StartStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StartStreamResponse:
        """
        @param request: StartStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_stream_with_options_async(
        self,
        request: vs_20181212_models.StartStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StartStreamResponse:
        """
        @param request: StartStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_stream(
        self,
        request: vs_20181212_models.StartStreamRequest,
    ) -> vs_20181212_models.StartStreamResponse:
        """
        @param request: StartStreamRequest
        @return: StartStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_stream_with_options(request, runtime)

    async def start_stream_async(
        self,
        request: vs_20181212_models.StartStreamRequest,
    ) -> vs_20181212_models.StartStreamResponse:
        """
        @param request: StartStreamRequest
        @return: StartStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_stream_with_options_async(request, runtime)

    def start_transfer_stream_with_options(
        self,
        request: vs_20181212_models.StartTransferStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StartTransferStreamResponse:
        """
        @param request: StartTransferStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartTransferStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.transcode):
            query['Transcode'] = request.transcode
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartTransferStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartTransferStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_transfer_stream_with_options_async(
        self,
        request: vs_20181212_models.StartTransferStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StartTransferStreamResponse:
        """
        @param request: StartTransferStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartTransferStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.transcode):
            query['Transcode'] = request.transcode
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartTransferStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartTransferStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_transfer_stream(
        self,
        request: vs_20181212_models.StartTransferStreamRequest,
    ) -> vs_20181212_models.StartTransferStreamResponse:
        """
        @param request: StartTransferStreamRequest
        @return: StartTransferStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_transfer_stream_with_options(request, runtime)

    async def start_transfer_stream_async(
        self,
        request: vs_20181212_models.StartTransferStreamRequest,
    ) -> vs_20181212_models.StartTransferStreamResponse:
        """
        @param request: StartTransferStreamRequest
        @return: StartTransferStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_transfer_stream_with_options_async(request, runtime)

    def stop_adjust_with_options(
        self,
        request: vs_20181212_models.StopAdjustRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StopAdjustResponse:
        """
        @param request: StopAdjustRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAdjustResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.focus):
            query['Focus'] = request.focus
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.iris):
            query['Iris'] = request.iris
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAdjust',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopAdjustResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_adjust_with_options_async(
        self,
        request: vs_20181212_models.StopAdjustRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StopAdjustResponse:
        """
        @param request: StopAdjustRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAdjustResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.focus):
            query['Focus'] = request.focus
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.iris):
            query['Iris'] = request.iris
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAdjust',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopAdjustResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_adjust(
        self,
        request: vs_20181212_models.StopAdjustRequest,
    ) -> vs_20181212_models.StopAdjustResponse:
        """
        @param request: StopAdjustRequest
        @return: StopAdjustResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_adjust_with_options(request, runtime)

    async def stop_adjust_async(
        self,
        request: vs_20181212_models.StopAdjustRequest,
    ) -> vs_20181212_models.StopAdjustResponse:
        """
        @param request: StopAdjustRequest
        @return: StopAdjustResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_adjust_with_options_async(request, runtime)

    def stop_device_with_options(
        self,
        request: vs_20181212_models.StopDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StopDeviceResponse:
        """
        @param request: StopDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_device_with_options_async(
        self,
        request: vs_20181212_models.StopDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StopDeviceResponse:
        """
        @param request: StopDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_device(
        self,
        request: vs_20181212_models.StopDeviceRequest,
    ) -> vs_20181212_models.StopDeviceResponse:
        """
        @param request: StopDeviceRequest
        @return: StopDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_device_with_options(request, runtime)

    async def stop_device_async(
        self,
        request: vs_20181212_models.StopDeviceRequest,
    ) -> vs_20181212_models.StopDeviceResponse:
        """
        @param request: StopDeviceRequest
        @return: StopDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_device_with_options_async(request, runtime)

    def stop_move_with_options(
        self,
        request: vs_20181212_models.StopMoveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StopMoveResponse:
        """
        @param request: StopMoveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopMoveResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pan):
            query['Pan'] = request.pan
        if not UtilClient.is_unset(request.tilt):
            query['Tilt'] = request.tilt
        if not UtilClient.is_unset(request.zoom):
            query['Zoom'] = request.zoom
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMove',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopMoveResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_move_with_options_async(
        self,
        request: vs_20181212_models.StopMoveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StopMoveResponse:
        """
        @param request: StopMoveRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopMoveResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pan):
            query['Pan'] = request.pan
        if not UtilClient.is_unset(request.tilt):
            query['Tilt'] = request.tilt
        if not UtilClient.is_unset(request.zoom):
            query['Zoom'] = request.zoom
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMove',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopMoveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_move(
        self,
        request: vs_20181212_models.StopMoveRequest,
    ) -> vs_20181212_models.StopMoveResponse:
        """
        @param request: StopMoveRequest
        @return: StopMoveResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_move_with_options(request, runtime)

    async def stop_move_async(
        self,
        request: vs_20181212_models.StopMoveRequest,
    ) -> vs_20181212_models.StopMoveResponse:
        """
        @param request: StopMoveRequest
        @return: StopMoveResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_move_with_options_async(request, runtime)

    def stop_publish_stream_with_options(
        self,
        request: vs_20181212_models.StopPublishStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StopPublishStreamResponse:
        """
        @param request: StopPublishStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopPublishStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopPublishStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopPublishStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_publish_stream_with_options_async(
        self,
        request: vs_20181212_models.StopPublishStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StopPublishStreamResponse:
        """
        @param request: StopPublishStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopPublishStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopPublishStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopPublishStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_publish_stream(
        self,
        request: vs_20181212_models.StopPublishStreamRequest,
    ) -> vs_20181212_models.StopPublishStreamResponse:
        """
        @param request: StopPublishStreamRequest
        @return: StopPublishStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_publish_stream_with_options(request, runtime)

    async def stop_publish_stream_async(
        self,
        request: vs_20181212_models.StopPublishStreamRequest,
    ) -> vs_20181212_models.StopPublishStreamResponse:
        """
        @param request: StopPublishStreamRequest
        @return: StopPublishStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_publish_stream_with_options_async(request, runtime)

    def stop_record_stream_with_options(
        self,
        request: vs_20181212_models.StopRecordStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StopRecordStreamResponse:
        """
        @param request: StopRecordStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopRecordStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopRecordStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopRecordStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_record_stream_with_options_async(
        self,
        request: vs_20181212_models.StopRecordStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StopRecordStreamResponse:
        """
        @param request: StopRecordStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopRecordStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopRecordStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopRecordStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_record_stream(
        self,
        request: vs_20181212_models.StopRecordStreamRequest,
    ) -> vs_20181212_models.StopRecordStreamResponse:
        """
        @param request: StopRecordStreamRequest
        @return: StopRecordStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_record_stream_with_options(request, runtime)

    async def stop_record_stream_async(
        self,
        request: vs_20181212_models.StopRecordStreamRequest,
    ) -> vs_20181212_models.StopRecordStreamResponse:
        """
        @param request: StopRecordStreamRequest
        @return: StopRecordStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_record_stream_with_options_async(request, runtime)

    def stop_rendering_session_with_options(
        self,
        request: vs_20181212_models.StopRenderingSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StopRenderingSessionResponse:
        """
        @summary 关闭指定的云应用服务会话并回收相关实例资源。
        
        @description ## 请求说明
        
        @param request: StopRenderingSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopRenderingSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopRenderingSession',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopRenderingSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_rendering_session_with_options_async(
        self,
        request: vs_20181212_models.StopRenderingSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StopRenderingSessionResponse:
        """
        @summary 关闭指定的云应用服务会话并回收相关实例资源。
        
        @description ## 请求说明
        
        @param request: StopRenderingSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopRenderingSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopRenderingSession',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopRenderingSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_rendering_session(
        self,
        request: vs_20181212_models.StopRenderingSessionRequest,
    ) -> vs_20181212_models.StopRenderingSessionResponse:
        """
        @summary 关闭指定的云应用服务会话并回收相关实例资源。
        
        @description ## 请求说明
        
        @param request: StopRenderingSessionRequest
        @return: StopRenderingSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_rendering_session_with_options(request, runtime)

    async def stop_rendering_session_async(
        self,
        request: vs_20181212_models.StopRenderingSessionRequest,
    ) -> vs_20181212_models.StopRenderingSessionResponse:
        """
        @summary 关闭指定的云应用服务会话并回收相关实例资源。
        
        @description ## 请求说明
        
        @param request: StopRenderingSessionRequest
        @return: StopRenderingSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_rendering_session_with_options_async(request, runtime)

    def stop_stream_with_options(
        self,
        request: vs_20181212_models.StopStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StopStreamResponse:
        """
        @param request: StopStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_stream_with_options_async(
        self,
        request: vs_20181212_models.StopStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StopStreamResponse:
        """
        @param request: StopStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_stream(
        self,
        request: vs_20181212_models.StopStreamRequest,
    ) -> vs_20181212_models.StopStreamResponse:
        """
        @param request: StopStreamRequest
        @return: StopStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_stream_with_options(request, runtime)

    async def stop_stream_async(
        self,
        request: vs_20181212_models.StopStreamRequest,
    ) -> vs_20181212_models.StopStreamResponse:
        """
        @param request: StopStreamRequest
        @return: StopStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_stream_with_options_async(request, runtime)

    def stop_transfer_stream_with_options(
        self,
        request: vs_20181212_models.StopTransferStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StopTransferStreamResponse:
        """
        @param request: StopTransferStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopTransferStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.transcode):
            query['Transcode'] = request.transcode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopTransferStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopTransferStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_transfer_stream_with_options_async(
        self,
        request: vs_20181212_models.StopTransferStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.StopTransferStreamResponse:
        """
        @param request: StopTransferStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopTransferStreamResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.transcode):
            query['Transcode'] = request.transcode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopTransferStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopTransferStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_transfer_stream(
        self,
        request: vs_20181212_models.StopTransferStreamRequest,
    ) -> vs_20181212_models.StopTransferStreamResponse:
        """
        @param request: StopTransferStreamRequest
        @return: StopTransferStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_transfer_stream_with_options(request, runtime)

    async def stop_transfer_stream_async(
        self,
        request: vs_20181212_models.StopTransferStreamRequest,
    ) -> vs_20181212_models.StopTransferStreamResponse:
        """
        @param request: StopTransferStreamRequest
        @return: StopTransferStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_transfer_stream_with_options_async(request, runtime)

    def sync_catalogs_with_options(
        self,
        request: vs_20181212_models.SyncCatalogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.SyncCatalogsResponse:
        """
        @param request: SyncCatalogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncCatalogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncCatalogs',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.SyncCatalogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_catalogs_with_options_async(
        self,
        request: vs_20181212_models.SyncCatalogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.SyncCatalogsResponse:
        """
        @param request: SyncCatalogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncCatalogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncCatalogs',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.SyncCatalogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_catalogs(
        self,
        request: vs_20181212_models.SyncCatalogsRequest,
    ) -> vs_20181212_models.SyncCatalogsResponse:
        """
        @param request: SyncCatalogsRequest
        @return: SyncCatalogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sync_catalogs_with_options(request, runtime)

    async def sync_catalogs_async(
        self,
        request: vs_20181212_models.SyncCatalogsRequest,
    ) -> vs_20181212_models.SyncCatalogsResponse:
        """
        @param request: SyncCatalogsRequest
        @return: SyncCatalogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sync_catalogs_with_options_async(request, runtime)

    def unbind_directory_with_options(
        self,
        request: vs_20181212_models.UnbindDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UnbindDirectoryResponse:
        """
        @param request: UnbindDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UnbindDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_directory_with_options_async(
        self,
        request: vs_20181212_models.UnbindDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UnbindDirectoryResponse:
        """
        @param request: UnbindDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UnbindDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_directory(
        self,
        request: vs_20181212_models.UnbindDirectoryRequest,
    ) -> vs_20181212_models.UnbindDirectoryResponse:
        """
        @param request: UnbindDirectoryRequest
        @return: UnbindDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_directory_with_options(request, runtime)

    async def unbind_directory_async(
        self,
        request: vs_20181212_models.UnbindDirectoryRequest,
    ) -> vs_20181212_models.UnbindDirectoryResponse:
        """
        @param request: UnbindDirectoryRequest
        @return: UnbindDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_directory_with_options_async(request, runtime)

    def unbind_parent_platform_device_with_options(
        self,
        request: vs_20181212_models.UnbindParentPlatformDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UnbindParentPlatformDeviceResponse:
        """
        @param request: UnbindParentPlatformDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindParentPlatformDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindParentPlatformDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UnbindParentPlatformDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_parent_platform_device_with_options_async(
        self,
        request: vs_20181212_models.UnbindParentPlatformDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UnbindParentPlatformDeviceResponse:
        """
        @param request: UnbindParentPlatformDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindParentPlatformDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindParentPlatformDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UnbindParentPlatformDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_parent_platform_device(
        self,
        request: vs_20181212_models.UnbindParentPlatformDeviceRequest,
    ) -> vs_20181212_models.UnbindParentPlatformDeviceResponse:
        """
        @param request: UnbindParentPlatformDeviceRequest
        @return: UnbindParentPlatformDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_parent_platform_device_with_options(request, runtime)

    async def unbind_parent_platform_device_async(
        self,
        request: vs_20181212_models.UnbindParentPlatformDeviceRequest,
    ) -> vs_20181212_models.UnbindParentPlatformDeviceResponse:
        """
        @param request: UnbindParentPlatformDeviceRequest
        @return: UnbindParentPlatformDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_parent_platform_device_with_options_async(request, runtime)

    def unbind_purchased_device_with_options(
        self,
        request: vs_20181212_models.UnbindPurchasedDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UnbindPurchasedDeviceResponse:
        """
        @param request: UnbindPurchasedDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindPurchasedDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindPurchasedDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UnbindPurchasedDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_purchased_device_with_options_async(
        self,
        request: vs_20181212_models.UnbindPurchasedDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UnbindPurchasedDeviceResponse:
        """
        @param request: UnbindPurchasedDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindPurchasedDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindPurchasedDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UnbindPurchasedDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_purchased_device(
        self,
        request: vs_20181212_models.UnbindPurchasedDeviceRequest,
    ) -> vs_20181212_models.UnbindPurchasedDeviceResponse:
        """
        @param request: UnbindPurchasedDeviceRequest
        @return: UnbindPurchasedDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_purchased_device_with_options(request, runtime)

    async def unbind_purchased_device_async(
        self,
        request: vs_20181212_models.UnbindPurchasedDeviceRequest,
    ) -> vs_20181212_models.UnbindPurchasedDeviceResponse:
        """
        @param request: UnbindPurchasedDeviceRequest
        @return: UnbindPurchasedDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_purchased_device_with_options_async(request, runtime)

    def unbind_template_with_options(
        self,
        request: vs_20181212_models.UnbindTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UnbindTemplateResponse:
        """
        @param request: UnbindTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UnbindTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_template_with_options_async(
        self,
        request: vs_20181212_models.UnbindTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UnbindTemplateResponse:
        """
        @param request: UnbindTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UnbindTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_template(
        self,
        request: vs_20181212_models.UnbindTemplateRequest,
    ) -> vs_20181212_models.UnbindTemplateResponse:
        """
        @param request: UnbindTemplateRequest
        @return: UnbindTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_template_with_options(request, runtime)

    async def unbind_template_async(
        self,
        request: vs_20181212_models.UnbindTemplateRequest,
    ) -> vs_20181212_models.UnbindTemplateResponse:
        """
        @param request: UnbindTemplateRequest
        @return: UnbindTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_template_with_options_async(request, runtime)

    def uninstall_cloud_app_with_options(
        self,
        tmp_req: vs_20181212_models.UninstallCloudAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UninstallCloudAppResponse:
        """
        @summary 卸载云应用
        
        @param tmp_req: UninstallCloudAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallCloudAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.UninstallCloudAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not UtilClient.is_unset(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallCloudApp',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UninstallCloudAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_cloud_app_with_options_async(
        self,
        tmp_req: vs_20181212_models.UninstallCloudAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UninstallCloudAppResponse:
        """
        @summary 卸载云应用
        
        @param tmp_req: UninstallCloudAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallCloudAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.UninstallCloudAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rendering_instance_ids):
            request.rendering_instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rendering_instance_ids, 'RenderingInstanceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not UtilClient.is_unset(request.rendering_instance_ids_shrink):
            query['RenderingInstanceIds'] = request.rendering_instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallCloudApp',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UninstallCloudAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_cloud_app(
        self,
        request: vs_20181212_models.UninstallCloudAppRequest,
    ) -> vs_20181212_models.UninstallCloudAppResponse:
        """
        @summary 卸载云应用
        
        @param request: UninstallCloudAppRequest
        @return: UninstallCloudAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.uninstall_cloud_app_with_options(request, runtime)

    async def uninstall_cloud_app_async(
        self,
        request: vs_20181212_models.UninstallCloudAppRequest,
    ) -> vs_20181212_models.UninstallCloudAppResponse:
        """
        @summary 卸载云应用
        
        @param request: UninstallCloudAppRequest
        @return: UninstallCloudAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.uninstall_cloud_app_with_options_async(request, runtime)

    def unlock_device_with_options(
        self,
        request: vs_20181212_models.UnlockDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UnlockDeviceResponse:
        """
        @param request: UnlockDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlockDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UnlockDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_device_with_options_async(
        self,
        request: vs_20181212_models.UnlockDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UnlockDeviceResponse:
        """
        @param request: UnlockDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlockDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UnlockDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_device(
        self,
        request: vs_20181212_models.UnlockDeviceRequest,
    ) -> vs_20181212_models.UnlockDeviceResponse:
        """
        @param request: UnlockDeviceRequest
        @return: UnlockDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unlock_device_with_options(request, runtime)

    async def unlock_device_async(
        self,
        request: vs_20181212_models.UnlockDeviceRequest,
    ) -> vs_20181212_models.UnlockDeviceResponse:
        """
        @param request: UnlockDeviceRequest
        @return: UnlockDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unlock_device_with_options_async(request, runtime)

    def update_cloud_app_info_with_options(
        self,
        request: vs_20181212_models.UpdateCloudAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UpdateCloudAppInfoResponse:
        """
        @summary 更新云应用信息
        
        @param request: UpdateCloudAppInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudAppInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudAppInfo',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateCloudAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_app_info_with_options_async(
        self,
        request: vs_20181212_models.UpdateCloudAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UpdateCloudAppInfoResponse:
        """
        @summary 更新云应用信息
        
        @param request: UpdateCloudAppInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCloudAppInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCloudAppInfo',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateCloudAppInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_app_info(
        self,
        request: vs_20181212_models.UpdateCloudAppInfoRequest,
    ) -> vs_20181212_models.UpdateCloudAppInfoResponse:
        """
        @summary 更新云应用信息
        
        @param request: UpdateCloudAppInfoRequest
        @return: UpdateCloudAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cloud_app_info_with_options(request, runtime)

    async def update_cloud_app_info_async(
        self,
        request: vs_20181212_models.UpdateCloudAppInfoRequest,
    ) -> vs_20181212_models.UpdateCloudAppInfoResponse:
        """
        @summary 更新云应用信息
        
        @param request: UpdateCloudAppInfoRequest
        @return: UpdateCloudAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cloud_app_info_with_options_async(request, runtime)

    def update_file_info_with_options(
        self,
        request: vs_20181212_models.UpdateFileInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UpdateFileInfoResponse:
        """
        @summary 更新文件信息。
        
        @param request: UpdateFileInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFileInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFileInfo',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateFileInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_file_info_with_options_async(
        self,
        request: vs_20181212_models.UpdateFileInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UpdateFileInfoResponse:
        """
        @summary 更新文件信息。
        
        @param request: UpdateFileInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFileInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFileInfo',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateFileInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_file_info(
        self,
        request: vs_20181212_models.UpdateFileInfoRequest,
    ) -> vs_20181212_models.UpdateFileInfoResponse:
        """
        @summary 更新文件信息。
        
        @param request: UpdateFileInfoRequest
        @return: UpdateFileInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_file_info_with_options(request, runtime)

    async def update_file_info_async(
        self,
        request: vs_20181212_models.UpdateFileInfoRequest,
    ) -> vs_20181212_models.UpdateFileInfoResponse:
        """
        @summary 更新文件信息。
        
        @param request: UpdateFileInfoRequest
        @return: UpdateFileInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_file_info_with_options_async(request, runtime)

    def update_rendering_instance_configuration_with_options(
        self,
        tmp_req: vs_20181212_models.UpdateRenderingInstanceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UpdateRenderingInstanceConfigurationResponse:
        """
        @summary 更新云渲染实例配置参数
        
        @param tmp_req: UpdateRenderingInstanceConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRenderingInstanceConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.UpdateRenderingInstanceConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configuration):
            request.configuration_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        body = {}
        if not UtilClient.is_unset(request.configuration_shrink):
            body['Configuration'] = request.configuration_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRenderingInstanceConfiguration',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateRenderingInstanceConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rendering_instance_configuration_with_options_async(
        self,
        tmp_req: vs_20181212_models.UpdateRenderingInstanceConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UpdateRenderingInstanceConfigurationResponse:
        """
        @summary 更新云渲染实例配置参数
        
        @param tmp_req: UpdateRenderingInstanceConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRenderingInstanceConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.UpdateRenderingInstanceConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configuration):
            request.configuration_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configuration, 'Configuration', 'json')
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        body = {}
        if not UtilClient.is_unset(request.configuration_shrink):
            body['Configuration'] = request.configuration_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRenderingInstanceConfiguration',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateRenderingInstanceConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rendering_instance_configuration(
        self,
        request: vs_20181212_models.UpdateRenderingInstanceConfigurationRequest,
    ) -> vs_20181212_models.UpdateRenderingInstanceConfigurationResponse:
        """
        @summary 更新云渲染实例配置参数
        
        @param request: UpdateRenderingInstanceConfigurationRequest
        @return: UpdateRenderingInstanceConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_rendering_instance_configuration_with_options(request, runtime)

    async def update_rendering_instance_configuration_async(
        self,
        request: vs_20181212_models.UpdateRenderingInstanceConfigurationRequest,
    ) -> vs_20181212_models.UpdateRenderingInstanceConfigurationResponse:
        """
        @summary 更新云渲染实例配置参数
        
        @param request: UpdateRenderingInstanceConfigurationRequest
        @return: UpdateRenderingInstanceConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_rendering_instance_configuration_with_options_async(request, runtime)

    def update_rendering_instance_settings_with_options(
        self,
        tmp_req: vs_20181212_models.UpdateRenderingInstanceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UpdateRenderingInstanceSettingsResponse:
        """
        @summary 更新实例设置
        
        @param tmp_req: UpdateRenderingInstanceSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRenderingInstanceSettingsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.UpdateRenderingInstanceSettingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.settings):
            request.settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.settings, 'Settings', 'json')
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not UtilClient.is_unset(request.settings_shrink):
            query['Settings'] = request.settings_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRenderingInstanceSettings',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateRenderingInstanceSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rendering_instance_settings_with_options_async(
        self,
        tmp_req: vs_20181212_models.UpdateRenderingInstanceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UpdateRenderingInstanceSettingsResponse:
        """
        @summary 更新实例设置
        
        @param tmp_req: UpdateRenderingInstanceSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRenderingInstanceSettingsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.UpdateRenderingInstanceSettingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.settings):
            request.settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.settings, 'Settings', 'json')
        query = {}
        if not UtilClient.is_unset(request.rendering_instance_id):
            query['RenderingInstanceId'] = request.rendering_instance_id
        if not UtilClient.is_unset(request.settings_shrink):
            query['Settings'] = request.settings_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRenderingInstanceSettings',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateRenderingInstanceSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rendering_instance_settings(
        self,
        request: vs_20181212_models.UpdateRenderingInstanceSettingsRequest,
    ) -> vs_20181212_models.UpdateRenderingInstanceSettingsResponse:
        """
        @summary 更新实例设置
        
        @param request: UpdateRenderingInstanceSettingsRequest
        @return: UpdateRenderingInstanceSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_rendering_instance_settings_with_options(request, runtime)

    async def update_rendering_instance_settings_async(
        self,
        request: vs_20181212_models.UpdateRenderingInstanceSettingsRequest,
    ) -> vs_20181212_models.UpdateRenderingInstanceSettingsResponse:
        """
        @summary 更新实例设置
        
        @param request: UpdateRenderingInstanceSettingsRequest
        @return: UpdateRenderingInstanceSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_rendering_instance_settings_with_options_async(request, runtime)

    def update_rendering_project_with_options(
        self,
        tmp_req: vs_20181212_models.UpdateRenderingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UpdateRenderingProjectResponse:
        """
        @summary 更新一个项目的属性信息
        
        @param tmp_req: UpdateRenderingProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRenderingProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.UpdateRenderingProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.session_attribs):
            request.session_attribs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.session_attribs, 'SessionAttribs', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.session_attribs_shrink):
            query['SessionAttribs'] = request.session_attribs_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRenderingProject',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateRenderingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rendering_project_with_options_async(
        self,
        tmp_req: vs_20181212_models.UpdateRenderingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UpdateRenderingProjectResponse:
        """
        @summary 更新一个项目的属性信息
        
        @param tmp_req: UpdateRenderingProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRenderingProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = vs_20181212_models.UpdateRenderingProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.session_attribs):
            request.session_attribs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.session_attribs, 'SessionAttribs', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.session_attribs_shrink):
            query['SessionAttribs'] = request.session_attribs_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRenderingProject',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateRenderingProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rendering_project(
        self,
        request: vs_20181212_models.UpdateRenderingProjectRequest,
    ) -> vs_20181212_models.UpdateRenderingProjectResponse:
        """
        @summary 更新一个项目的属性信息
        
        @param request: UpdateRenderingProjectRequest
        @return: UpdateRenderingProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_rendering_project_with_options(request, runtime)

    async def update_rendering_project_async(
        self,
        request: vs_20181212_models.UpdateRenderingProjectRequest,
    ) -> vs_20181212_models.UpdateRenderingProjectResponse:
        """
        @summary 更新一个项目的属性信息
        
        @param request: UpdateRenderingProjectRequest
        @return: UpdateRenderingProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_rendering_project_with_options_async(request, runtime)

    def update_vs_pull_stream_info_config_with_options(
        self,
        request: vs_20181212_models.UpdateVsPullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UpdateVsPullStreamInfoConfigResponse:
        """
        @param request: UpdateVsPullStreamInfoConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVsPullStreamInfoConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.always):
            query['Always'] = request.always
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_url):
            query['SourceUrl'] = request.source_url
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVsPullStreamInfoConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateVsPullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vs_pull_stream_info_config_with_options_async(
        self,
        request: vs_20181212_models.UpdateVsPullStreamInfoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UpdateVsPullStreamInfoConfigResponse:
        """
        @param request: UpdateVsPullStreamInfoConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVsPullStreamInfoConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.always):
            query['Always'] = request.always
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_url):
            query['SourceUrl'] = request.source_url
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateVsPullStreamInfoConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateVsPullStreamInfoConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vs_pull_stream_info_config(
        self,
        request: vs_20181212_models.UpdateVsPullStreamInfoConfigRequest,
    ) -> vs_20181212_models.UpdateVsPullStreamInfoConfigResponse:
        """
        @param request: UpdateVsPullStreamInfoConfigRequest
        @return: UpdateVsPullStreamInfoConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_vs_pull_stream_info_config_with_options(request, runtime)

    async def update_vs_pull_stream_info_config_async(
        self,
        request: vs_20181212_models.UpdateVsPullStreamInfoConfigRequest,
    ) -> vs_20181212_models.UpdateVsPullStreamInfoConfigResponse:
        """
        @param request: UpdateVsPullStreamInfoConfigRequest
        @return: UpdateVsPullStreamInfoConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_vs_pull_stream_info_config_with_options_async(request, runtime)

    def upload_cloud_app_with_options(
        self,
        request: vs_20181212_models.UploadCloudAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UploadCloudAppResponse:
        """
        @summary 应用上架
        
        @param request: UploadCloudAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadCloudAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.download_url):
            query['DownloadUrl'] = request.download_url
        if not UtilClient.is_unset(request.md_5):
            query['Md5'] = request.md_5
        if not UtilClient.is_unset(request.pkg_format):
            query['PkgFormat'] = request.pkg_format
        if not UtilClient.is_unset(request.pkg_type):
            query['PkgType'] = request.pkg_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCloudApp',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UploadCloudAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_cloud_app_with_options_async(
        self,
        request: vs_20181212_models.UploadCloudAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UploadCloudAppResponse:
        """
        @summary 应用上架
        
        @param request: UploadCloudAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadCloudAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.download_url):
            query['DownloadUrl'] = request.download_url
        if not UtilClient.is_unset(request.md_5):
            query['Md5'] = request.md_5
        if not UtilClient.is_unset(request.pkg_format):
            query['PkgFormat'] = request.pkg_format
        if not UtilClient.is_unset(request.pkg_type):
            query['PkgType'] = request.pkg_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCloudApp',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UploadCloudAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_cloud_app(
        self,
        request: vs_20181212_models.UploadCloudAppRequest,
    ) -> vs_20181212_models.UploadCloudAppResponse:
        """
        @summary 应用上架
        
        @param request: UploadCloudAppRequest
        @return: UploadCloudAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_cloud_app_with_options(request, runtime)

    async def upload_cloud_app_async(
        self,
        request: vs_20181212_models.UploadCloudAppRequest,
    ) -> vs_20181212_models.UploadCloudAppResponse:
        """
        @summary 应用上架
        
        @param request: UploadCloudAppRequest
        @return: UploadCloudAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_cloud_app_with_options_async(request, runtime)

    def upload_file_with_options(
        self,
        request: vs_20181212_models.UploadFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UploadFileResponse:
        """
        @summary 文件上传
        
        @param request: UploadFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.md_5):
            query['Md5'] = request.md_5
        if not UtilClient.is_unset(request.origin_url):
            query['OriginUrl'] = request.origin_url
        if not UtilClient.is_unset(request.target_path):
            query['TargetPath'] = request.target_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadFile',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UploadFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_file_with_options_async(
        self,
        request: vs_20181212_models.UploadFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UploadFileResponse:
        """
        @summary 文件上传
        
        @param request: UploadFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.md_5):
            query['Md5'] = request.md_5
        if not UtilClient.is_unset(request.origin_url):
            query['OriginUrl'] = request.origin_url
        if not UtilClient.is_unset(request.target_path):
            query['TargetPath'] = request.target_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadFile',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UploadFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_file(
        self,
        request: vs_20181212_models.UploadFileRequest,
    ) -> vs_20181212_models.UploadFileResponse:
        """
        @summary 文件上传
        
        @param request: UploadFileRequest
        @return: UploadFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_file_with_options(request, runtime)

    async def upload_file_async(
        self,
        request: vs_20181212_models.UploadFileRequest,
    ) -> vs_20181212_models.UploadFileResponse:
        """
        @summary 文件上传
        
        @param request: UploadFileRequest
        @return: UploadFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_file_with_options_async(request, runtime)

    def upload_public_key_with_options(
        self,
        request: vs_20181212_models.UploadPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UploadPublicKeyResponse:
        """
        @summary 上传公钥，用于安全登陆鉴权。
        
        @param request: UploadPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadPublicKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.key_group):
            query['KeyGroup'] = request.key_group
        if not UtilClient.is_unset(request.key_name):
            query['KeyName'] = request.key_name
        if not UtilClient.is_unset(request.key_type):
            query['KeyType'] = request.key_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadPublicKey',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UploadPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_public_key_with_options_async(
        self,
        request: vs_20181212_models.UploadPublicKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.UploadPublicKeyResponse:
        """
        @summary 上传公钥，用于安全登陆鉴权。
        
        @param request: UploadPublicKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadPublicKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.key_group):
            query['KeyGroup'] = request.key_group
        if not UtilClient.is_unset(request.key_name):
            query['KeyName'] = request.key_name
        if not UtilClient.is_unset(request.key_type):
            query['KeyType'] = request.key_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadPublicKey',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UploadPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_public_key(
        self,
        request: vs_20181212_models.UploadPublicKeyRequest,
    ) -> vs_20181212_models.UploadPublicKeyResponse:
        """
        @summary 上传公钥，用于安全登陆鉴权。
        
        @param request: UploadPublicKeyRequest
        @return: UploadPublicKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_public_key_with_options(request, runtime)

    async def upload_public_key_async(
        self,
        request: vs_20181212_models.UploadPublicKeyRequest,
    ) -> vs_20181212_models.UploadPublicKeyResponse:
        """
        @summary 上传公钥，用于安全登陆鉴权。
        
        @param request: UploadPublicKeyRequest
        @return: UploadPublicKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_public_key_with_options_async(request, runtime)

    def verify_vs_domain_owner_with_options(
        self,
        request: vs_20181212_models.VerifyVsDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.VerifyVsDomainOwnerResponse:
        """
        @param request: VerifyVsDomainOwnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyVsDomainOwnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyVsDomainOwner',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.VerifyVsDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_vs_domain_owner_with_options_async(
        self,
        request: vs_20181212_models.VerifyVsDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vs_20181212_models.VerifyVsDomainOwnerResponse:
        """
        @param request: VerifyVsDomainOwnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyVsDomainOwnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyVsDomainOwner',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.VerifyVsDomainOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_vs_domain_owner(
        self,
        request: vs_20181212_models.VerifyVsDomainOwnerRequest,
    ) -> vs_20181212_models.VerifyVsDomainOwnerResponse:
        """
        @param request: VerifyVsDomainOwnerRequest
        @return: VerifyVsDomainOwnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_vs_domain_owner_with_options(request, runtime)

    async def verify_vs_domain_owner_async(
        self,
        request: vs_20181212_models.VerifyVsDomainOwnerRequest,
    ) -> vs_20181212_models.VerifyVsDomainOwnerResponse:
        """
        @param request: VerifyVsDomainOwnerRequest
        @return: VerifyVsDomainOwnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_vs_domain_owner_with_options_async(request, runtime)
