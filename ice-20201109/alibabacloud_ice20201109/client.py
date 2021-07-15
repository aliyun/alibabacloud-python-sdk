# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ice20201109 import models as ice20201109_models
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
        self._endpoint_map = {
            'ap-northeast-1': 'ice.aliyuncs.com',
            'ap-northeast-2-pop': 'ice.aliyuncs.com',
            'ap-south-1': 'ice.aliyuncs.com',
            'ap-southeast-1': 'ice.aliyuncs.com',
            'ap-southeast-2': 'ice.aliyuncs.com',
            'ap-southeast-3': 'ice.aliyuncs.com',
            'ap-southeast-5': 'ice.aliyuncs.com',
            'cn-beijing': 'ice.aliyuncs.com',
            'cn-beijing-finance-1': 'ice.aliyuncs.com',
            'cn-beijing-finance-pop': 'ice.aliyuncs.com',
            'cn-beijing-gov-1': 'ice.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ice.aliyuncs.com',
            'cn-chengdu': 'ice.aliyuncs.com',
            'cn-edge-1': 'ice.aliyuncs.com',
            'cn-fujian': 'ice.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ice.aliyuncs.com',
            'cn-hangzhou': 'ice.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ice.aliyuncs.com',
            'cn-hangzhou-finance': 'ice.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ice.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ice.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ice.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ice.aliyuncs.com',
            'cn-hangzhou-test-306': 'ice.aliyuncs.com',
            'cn-hongkong': 'ice.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ice.aliyuncs.com',
            'cn-huhehaote': 'ice.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'ice.aliyuncs.com',
            'cn-north-2-gov-1': 'ice.aliyuncs.com',
            'cn-qingdao': 'ice.aliyuncs.com',
            'cn-qingdao-nebula': 'ice.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ice.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ice.aliyuncs.com',
            'cn-shanghai-finance-1': 'ice.aliyuncs.com',
            'cn-shanghai-inner': 'ice.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ice.aliyuncs.com',
            'cn-shenzhen': 'ice.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ice.aliyuncs.com',
            'cn-shenzhen-inner': 'ice.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ice.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ice.aliyuncs.com',
            'cn-wuhan': 'ice.aliyuncs.com',
            'cn-wulanchabu': 'ice.aliyuncs.com',
            'cn-yushanfang': 'ice.aliyuncs.com',
            'cn-zhangbei': 'ice.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ice.aliyuncs.com',
            'cn-zhangjiakou': 'ice.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ice.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ice.aliyuncs.com',
            'eu-central-1': 'ice.aliyuncs.com',
            'eu-west-1': 'ice.aliyuncs.com',
            'eu-west-1-oxs': 'ice.aliyuncs.com',
            'me-east-1': 'ice.aliyuncs.com',
            'rus-west-1-pop': 'ice.aliyuncs.com',
            'us-east-1': 'ice.aliyuncs.com',
            'us-west-1': 'ice.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def list_smart_jobs_with_options(
        self,
        request: ice20201109_models.ListSmartJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListSmartJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.ListSmartJobsResponse(),
            self.do_rpcrequest('ListSmartJobs', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_smart_jobs_with_options_async(
        self,
        request: ice20201109_models.ListSmartJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListSmartJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.ListSmartJobsResponse(),
            await self.do_rpcrequest_async('ListSmartJobs', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_smart_jobs(
        self,
        request: ice20201109_models.ListSmartJobsRequest,
    ) -> ice20201109_models.ListSmartJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_smart_jobs_with_options(request, runtime)

    async def list_smart_jobs_async(
        self,
        request: ice20201109_models.ListSmartJobsRequest,
    ) -> ice20201109_models.ListSmartJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_smart_jobs_with_options_async(request, runtime)

    def describe_related_authorization_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeRelatedAuthorizationStatusResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ice20201109_models.DescribeRelatedAuthorizationStatusResponse(),
            self.do_rpcrequest('DescribeRelatedAuthorizationStatus', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_related_authorization_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeRelatedAuthorizationStatusResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ice20201109_models.DescribeRelatedAuthorizationStatusResponse(),
            await self.do_rpcrequest_async('DescribeRelatedAuthorizationStatus', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_related_authorization_status(self) -> ice20201109_models.DescribeRelatedAuthorizationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_related_authorization_status_with_options(runtime)

    async def describe_related_authorization_status_async(self) -> ice20201109_models.DescribeRelatedAuthorizationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_related_authorization_status_with_options_async(runtime)

    def delete_smart_job_with_options(
        self,
        request: ice20201109_models.DeleteSmartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteSmartJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteSmartJobResponse(),
            self.do_rpcrequest('DeleteSmartJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_smart_job_with_options_async(
        self,
        request: ice20201109_models.DeleteSmartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteSmartJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteSmartJobResponse(),
            await self.do_rpcrequest_async('DeleteSmartJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_smart_job(
        self,
        request: ice20201109_models.DeleteSmartJobRequest,
    ) -> ice20201109_models.DeleteSmartJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_smart_job_with_options(request, runtime)

    async def delete_smart_job_async(
        self,
        request: ice20201109_models.DeleteSmartJobRequest,
    ) -> ice20201109_models.DeleteSmartJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_smart_job_with_options_async(request, runtime)

    def add_template_with_options(
        self,
        request: ice20201109_models.AddTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.AddTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.AddTemplateResponse(),
            self.do_rpcrequest('AddTemplate', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def add_template_with_options_async(
        self,
        request: ice20201109_models.AddTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.AddTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.AddTemplateResponse(),
            await self.do_rpcrequest_async('AddTemplate', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def add_template(
        self,
        request: ice20201109_models.AddTemplateRequest,
    ) -> ice20201109_models.AddTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_template_with_options(request, runtime)

    async def add_template_async(
        self,
        request: ice20201109_models.AddTemplateRequest,
    ) -> ice20201109_models.AddTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_template_with_options_async(request, runtime)

    def update_editing_project_with_options(
        self,
        request: ice20201109_models.UpdateEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateEditingProjectResponse(),
            self.do_rpcrequest('UpdateEditingProject', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_editing_project_with_options_async(
        self,
        request: ice20201109_models.UpdateEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateEditingProjectResponse(),
            await self.do_rpcrequest_async('UpdateEditingProject', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_editing_project(
        self,
        request: ice20201109_models.UpdateEditingProjectRequest,
    ) -> ice20201109_models.UpdateEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_editing_project_with_options(request, runtime)

    async def update_editing_project_async(
        self,
        request: ice20201109_models.UpdateEditingProjectRequest,
    ) -> ice20201109_models.UpdateEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_editing_project_with_options_async(request, runtime)

    def list_media_producing_jobs_with_options(
        self,
        request: ice20201109_models.ListMediaProducingJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListMediaProducingJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.ListMediaProducingJobsResponse(),
            self.do_rpcrequest('ListMediaProducingJobs', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_media_producing_jobs_with_options_async(
        self,
        request: ice20201109_models.ListMediaProducingJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListMediaProducingJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.ListMediaProducingJobsResponse(),
            await self.do_rpcrequest_async('ListMediaProducingJobs', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_media_producing_jobs(
        self,
        request: ice20201109_models.ListMediaProducingJobsRequest,
    ) -> ice20201109_models.ListMediaProducingJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_media_producing_jobs_with_options(request, runtime)

    async def list_media_producing_jobs_async(
        self,
        request: ice20201109_models.ListMediaProducingJobsRequest,
    ) -> ice20201109_models.ListMediaProducingJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_media_producing_jobs_with_options_async(request, runtime)

    def get_editing_project_materials_with_options(
        self,
        request: ice20201109_models.GetEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.GetEditingProjectMaterialsResponse(),
            self.do_rpcrequest('GetEditingProjectMaterials', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_editing_project_materials_with_options_async(
        self,
        request: ice20201109_models.GetEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.GetEditingProjectMaterialsResponse(),
            await self.do_rpcrequest_async('GetEditingProjectMaterials', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_editing_project_materials(
        self,
        request: ice20201109_models.GetEditingProjectMaterialsRequest,
    ) -> ice20201109_models.GetEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_editing_project_materials_with_options(request, runtime)

    async def get_editing_project_materials_async(
        self,
        request: ice20201109_models.GetEditingProjectMaterialsRequest,
    ) -> ice20201109_models.GetEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_editing_project_materials_with_options_async(request, runtime)

    def get_default_storage_location_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetDefaultStorageLocationResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ice20201109_models.GetDefaultStorageLocationResponse(),
            self.do_rpcrequest('GetDefaultStorageLocation', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_default_storage_location_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetDefaultStorageLocationResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ice20201109_models.GetDefaultStorageLocationResponse(),
            await self.do_rpcrequest_async('GetDefaultStorageLocation', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_default_storage_location(self) -> ice20201109_models.GetDefaultStorageLocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_default_storage_location_with_options(runtime)

    async def get_default_storage_location_async(self) -> ice20201109_models.GetDefaultStorageLocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_default_storage_location_with_options_async(runtime)

    def delete_media_infos_with_options(
        self,
        request: ice20201109_models.DeleteMediaInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteMediaInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteMediaInfosResponse(),
            self.do_rpcrequest('DeleteMediaInfos', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_media_infos_with_options_async(
        self,
        request: ice20201109_models.DeleteMediaInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteMediaInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteMediaInfosResponse(),
            await self.do_rpcrequest_async('DeleteMediaInfos', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_media_infos(
        self,
        request: ice20201109_models.DeleteMediaInfosRequest,
    ) -> ice20201109_models.DeleteMediaInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_media_infos_with_options(request, runtime)

    async def delete_media_infos_async(
        self,
        request: ice20201109_models.DeleteMediaInfosRequest,
    ) -> ice20201109_models.DeleteMediaInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_media_infos_with_options_async(request, runtime)

    def set_event_callback_with_options(
        self,
        request: ice20201109_models.SetEventCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SetEventCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SetEventCallbackResponse(),
            self.do_rpcrequest('SetEventCallback', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_event_callback_with_options_async(
        self,
        request: ice20201109_models.SetEventCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SetEventCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SetEventCallbackResponse(),
            await self.do_rpcrequest_async('SetEventCallback', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_event_callback(
        self,
        request: ice20201109_models.SetEventCallbackRequest,
    ) -> ice20201109_models.SetEventCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_event_callback_with_options(request, runtime)

    async def set_event_callback_async(
        self,
        request: ice20201109_models.SetEventCallbackRequest,
    ) -> ice20201109_models.SetEventCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_event_callback_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: ice20201109_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.GetTemplateResponse(),
            self.do_rpcrequest('GetTemplate', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: ice20201109_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.GetTemplateResponse(),
            await self.do_rpcrequest_async('GetTemplate', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_template(
        self,
        request: ice20201109_models.GetTemplateRequest,
    ) -> ice20201109_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: ice20201109_models.GetTemplateRequest,
    ) -> ice20201109_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def register_media_info_with_options(
        self,
        request: ice20201109_models.RegisterMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.RegisterMediaInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.RegisterMediaInfoResponse(),
            self.do_rpcrequest('RegisterMediaInfo', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_media_info_with_options_async(
        self,
        request: ice20201109_models.RegisterMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.RegisterMediaInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.RegisterMediaInfoResponse(),
            await self.do_rpcrequest_async('RegisterMediaInfo', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_media_info(
        self,
        request: ice20201109_models.RegisterMediaInfoRequest,
    ) -> ice20201109_models.RegisterMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_media_info_with_options(request, runtime)

    async def register_media_info_async(
        self,
        request: ice20201109_models.RegisterMediaInfoRequest,
    ) -> ice20201109_models.RegisterMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_media_info_with_options_async(request, runtime)

    def create_editing_project_with_options(
        self,
        request: ice20201109_models.CreateEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.CreateEditingProjectResponse(),
            self.do_rpcrequest('CreateEditingProject', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_editing_project_with_options_async(
        self,
        request: ice20201109_models.CreateEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.CreateEditingProjectResponse(),
            await self.do_rpcrequest_async('CreateEditingProject', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_editing_project(
        self,
        request: ice20201109_models.CreateEditingProjectRequest,
    ) -> ice20201109_models.CreateEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_editing_project_with_options(request, runtime)

    async def create_editing_project_async(
        self,
        request: ice20201109_models.CreateEditingProjectRequest,
    ) -> ice20201109_models.CreateEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_editing_project_with_options_async(request, runtime)

    def batch_get_media_infos_with_options(
        self,
        request: ice20201109_models.BatchGetMediaInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.BatchGetMediaInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.BatchGetMediaInfosResponse(),
            self.do_rpcrequest('BatchGetMediaInfos', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_get_media_infos_with_options_async(
        self,
        request: ice20201109_models.BatchGetMediaInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.BatchGetMediaInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.BatchGetMediaInfosResponse(),
            await self.do_rpcrequest_async('BatchGetMediaInfos', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_get_media_infos(
        self,
        request: ice20201109_models.BatchGetMediaInfosRequest,
    ) -> ice20201109_models.BatchGetMediaInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_get_media_infos_with_options(request, runtime)

    async def batch_get_media_infos_async(
        self,
        request: ice20201109_models.BatchGetMediaInfosRequest,
    ) -> ice20201109_models.BatchGetMediaInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_media_infos_with_options_async(request, runtime)

    def set_default_storage_location_with_options(
        self,
        request: ice20201109_models.SetDefaultStorageLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SetDefaultStorageLocationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SetDefaultStorageLocationResponse(),
            self.do_rpcrequest('SetDefaultStorageLocation', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_default_storage_location_with_options_async(
        self,
        request: ice20201109_models.SetDefaultStorageLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SetDefaultStorageLocationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SetDefaultStorageLocationResponse(),
            await self.do_rpcrequest_async('SetDefaultStorageLocation', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_default_storage_location(
        self,
        request: ice20201109_models.SetDefaultStorageLocationRequest,
    ) -> ice20201109_models.SetDefaultStorageLocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_default_storage_location_with_options(request, runtime)

    async def set_default_storage_location_async(
        self,
        request: ice20201109_models.SetDefaultStorageLocationRequest,
    ) -> ice20201109_models.SetDefaultStorageLocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_default_storage_location_with_options_async(request, runtime)

    def update_media_info_with_options(
        self,
        request: ice20201109_models.UpdateMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateMediaInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateMediaInfoResponse(),
            self.do_rpcrequest('UpdateMediaInfo', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_media_info_with_options_async(
        self,
        request: ice20201109_models.UpdateMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateMediaInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateMediaInfoResponse(),
            await self.do_rpcrequest_async('UpdateMediaInfo', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_media_info(
        self,
        request: ice20201109_models.UpdateMediaInfoRequest,
    ) -> ice20201109_models.UpdateMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_media_info_with_options(request, runtime)

    async def update_media_info_async(
        self,
        request: ice20201109_models.UpdateMediaInfoRequest,
    ) -> ice20201109_models.UpdateMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_media_info_with_options_async(request, runtime)

    def get_media_producing_job_with_options(
        self,
        request: ice20201109_models.GetMediaProducingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetMediaProducingJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.GetMediaProducingJobResponse(),
            self.do_rpcrequest('GetMediaProducingJob', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_media_producing_job_with_options_async(
        self,
        request: ice20201109_models.GetMediaProducingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetMediaProducingJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.GetMediaProducingJobResponse(),
            await self.do_rpcrequest_async('GetMediaProducingJob', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_media_producing_job(
        self,
        request: ice20201109_models.GetMediaProducingJobRequest,
    ) -> ice20201109_models.GetMediaProducingJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_producing_job_with_options(request, runtime)

    async def get_media_producing_job_async(
        self,
        request: ice20201109_models.GetMediaProducingJobRequest,
    ) -> ice20201109_models.GetMediaProducingJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_producing_job_with_options_async(request, runtime)

    def describe_ice_product_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeIceProductStatusResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ice20201109_models.DescribeIceProductStatusResponse(),
            self.do_rpcrequest('DescribeIceProductStatus', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ice_product_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeIceProductStatusResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ice20201109_models.DescribeIceProductStatusResponse(),
            await self.do_rpcrequest_async('DescribeIceProductStatus', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ice_product_status(self) -> ice20201109_models.DescribeIceProductStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ice_product_status_with_options(runtime)

    async def describe_ice_product_status_async(self) -> ice20201109_models.DescribeIceProductStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ice_product_status_with_options_async(runtime)

    def list_media_basic_infos_with_options(
        self,
        request: ice20201109_models.ListMediaBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListMediaBasicInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.ListMediaBasicInfosResponse(),
            self.do_rpcrequest('ListMediaBasicInfos', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_media_basic_infos_with_options_async(
        self,
        request: ice20201109_models.ListMediaBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListMediaBasicInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.ListMediaBasicInfosResponse(),
            await self.do_rpcrequest_async('ListMediaBasicInfos', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_media_basic_infos(
        self,
        request: ice20201109_models.ListMediaBasicInfosRequest,
    ) -> ice20201109_models.ListMediaBasicInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_media_basic_infos_with_options(request, runtime)

    async def list_media_basic_infos_async(
        self,
        request: ice20201109_models.ListMediaBasicInfosRequest,
    ) -> ice20201109_models.ListMediaBasicInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_media_basic_infos_with_options_async(request, runtime)

    def submit_subtitle_produce_job_with_options(
        self,
        request: ice20201109_models.SubmitSubtitleProduceJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitSubtitleProduceJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitSubtitleProduceJobResponse(),
            self.do_rpcrequest('SubmitSubtitleProduceJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_subtitle_produce_job_with_options_async(
        self,
        request: ice20201109_models.SubmitSubtitleProduceJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitSubtitleProduceJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitSubtitleProduceJobResponse(),
            await self.do_rpcrequest_async('SubmitSubtitleProduceJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_subtitle_produce_job(
        self,
        request: ice20201109_models.SubmitSubtitleProduceJobRequest,
    ) -> ice20201109_models.SubmitSubtitleProduceJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_subtitle_produce_job_with_options(request, runtime)

    async def submit_subtitle_produce_job_async(
        self,
        request: ice20201109_models.SubmitSubtitleProduceJobRequest,
    ) -> ice20201109_models.SubmitSubtitleProduceJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_subtitle_produce_job_with_options_async(request, runtime)

    def submit_key_word_cut_job_with_options(
        self,
        request: ice20201109_models.SubmitKeyWordCutJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitKeyWordCutJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitKeyWordCutJobResponse(),
            self.do_rpcrequest('SubmitKeyWordCutJob', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def submit_key_word_cut_job_with_options_async(
        self,
        request: ice20201109_models.SubmitKeyWordCutJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitKeyWordCutJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitKeyWordCutJobResponse(),
            await self.do_rpcrequest_async('SubmitKeyWordCutJob', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def submit_key_word_cut_job(
        self,
        request: ice20201109_models.SubmitKeyWordCutJobRequest,
    ) -> ice20201109_models.SubmitKeyWordCutJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_key_word_cut_job_with_options(request, runtime)

    async def submit_key_word_cut_job_async(
        self,
        request: ice20201109_models.SubmitKeyWordCutJobRequest,
    ) -> ice20201109_models.SubmitKeyWordCutJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_key_word_cut_job_with_options_async(request, runtime)

    def add_editing_project_materials_with_options(
        self,
        request: ice20201109_models.AddEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.AddEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.AddEditingProjectMaterialsResponse(),
            self.do_rpcrequest('AddEditingProjectMaterials', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_editing_project_materials_with_options_async(
        self,
        request: ice20201109_models.AddEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.AddEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.AddEditingProjectMaterialsResponse(),
            await self.do_rpcrequest_async('AddEditingProjectMaterials', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_editing_project_materials(
        self,
        request: ice20201109_models.AddEditingProjectMaterialsRequest,
    ) -> ice20201109_models.AddEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_editing_project_materials_with_options(request, runtime)

    async def add_editing_project_materials_async(
        self,
        request: ice20201109_models.AddEditingProjectMaterialsRequest,
    ) -> ice20201109_models.AddEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_editing_project_materials_with_options_async(request, runtime)

    def submit_asrjob_with_options(
        self,
        request: ice20201109_models.SubmitASRJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitASRJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitASRJobResponse(),
            self.do_rpcrequest('SubmitASRJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_asrjob_with_options_async(
        self,
        request: ice20201109_models.SubmitASRJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitASRJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitASRJobResponse(),
            await self.do_rpcrequest_async('SubmitASRJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_asrjob(
        self,
        request: ice20201109_models.SubmitASRJobRequest,
    ) -> ice20201109_models.SubmitASRJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_asrjob_with_options(request, runtime)

    async def submit_asrjob_async(
        self,
        request: ice20201109_models.SubmitASRJobRequest,
    ) -> ice20201109_models.SubmitASRJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_asrjob_with_options_async(request, runtime)

    def get_editing_project_with_options(
        self,
        request: ice20201109_models.GetEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetEditingProjectResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.GetEditingProjectResponse(),
            self.do_rpcrequest('GetEditingProject', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_editing_project_with_options_async(
        self,
        request: ice20201109_models.GetEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetEditingProjectResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.GetEditingProjectResponse(),
            await self.do_rpcrequest_async('GetEditingProject', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_editing_project(
        self,
        request: ice20201109_models.GetEditingProjectRequest,
    ) -> ice20201109_models.GetEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_editing_project_with_options(request, runtime)

    async def get_editing_project_async(
        self,
        request: ice20201109_models.GetEditingProjectRequest,
    ) -> ice20201109_models.GetEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_editing_project_with_options_async(request, runtime)

    def list_sys_templates_with_options(
        self,
        request: ice20201109_models.ListSysTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListSysTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.ListSysTemplatesResponse(),
            self.do_rpcrequest('ListSysTemplates', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_sys_templates_with_options_async(
        self,
        request: ice20201109_models.ListSysTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListSysTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.ListSysTemplatesResponse(),
            await self.do_rpcrequest_async('ListSysTemplates', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_sys_templates(
        self,
        request: ice20201109_models.ListSysTemplatesRequest,
    ) -> ice20201109_models.ListSysTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sys_templates_with_options(request, runtime)

    async def list_sys_templates_async(
        self,
        request: ice20201109_models.ListSysTemplatesRequest,
    ) -> ice20201109_models.ListSysTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sys_templates_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: ice20201109_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteTemplateResponse(),
            self.do_rpcrequest('DeleteTemplate', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: ice20201109_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteTemplateResponse(),
            await self.do_rpcrequest_async('DeleteTemplate', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_template(
        self,
        request: ice20201109_models.DeleteTemplateRequest,
    ) -> ice20201109_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: ice20201109_models.DeleteTemplateRequest,
    ) -> ice20201109_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def submit_irjob_with_options(
        self,
        request: ice20201109_models.SubmitIRJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitIRJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitIRJobResponse(),
            self.do_rpcrequest('SubmitIRJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_irjob_with_options_async(
        self,
        request: ice20201109_models.SubmitIRJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitIRJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitIRJobResponse(),
            await self.do_rpcrequest_async('SubmitIRJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_irjob(
        self,
        request: ice20201109_models.SubmitIRJobRequest,
    ) -> ice20201109_models.SubmitIRJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_irjob_with_options(request, runtime)

    async def submit_irjob_async(
        self,
        request: ice20201109_models.SubmitIRJobRequest,
    ) -> ice20201109_models.SubmitIRJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_irjob_with_options_async(request, runtime)

    def delete_editing_project_materials_with_options(
        self,
        request: ice20201109_models.DeleteEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteEditingProjectMaterialsResponse(),
            self.do_rpcrequest('DeleteEditingProjectMaterials', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_editing_project_materials_with_options_async(
        self,
        request: ice20201109_models.DeleteEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteEditingProjectMaterialsResponse(),
            await self.do_rpcrequest_async('DeleteEditingProjectMaterials', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_editing_project_materials(
        self,
        request: ice20201109_models.DeleteEditingProjectMaterialsRequest,
    ) -> ice20201109_models.DeleteEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_editing_project_materials_with_options(request, runtime)

    async def delete_editing_project_materials_async(
        self,
        request: ice20201109_models.DeleteEditingProjectMaterialsRequest,
    ) -> ice20201109_models.DeleteEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_editing_project_materials_with_options_async(request, runtime)

    def search_editing_project_with_options(
        self,
        request: ice20201109_models.SearchEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SearchEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SearchEditingProjectResponse(),
            self.do_rpcrequest('SearchEditingProject', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_editing_project_with_options_async(
        self,
        request: ice20201109_models.SearchEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SearchEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SearchEditingProjectResponse(),
            await self.do_rpcrequest_async('SearchEditingProject', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_editing_project(
        self,
        request: ice20201109_models.SearchEditingProjectRequest,
    ) -> ice20201109_models.SearchEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_editing_project_with_options(request, runtime)

    async def search_editing_project_async(
        self,
        request: ice20201109_models.SearchEditingProjectRequest,
    ) -> ice20201109_models.SearchEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_editing_project_with_options_async(request, runtime)

    def list_templates_with_options(
        self,
        request: ice20201109_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.ListTemplatesResponse(),
            self.do_rpcrequest('ListTemplates', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: ice20201109_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.ListTemplatesResponse(),
            await self.do_rpcrequest_async('ListTemplates', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_templates(
        self,
        request: ice20201109_models.ListTemplatesRequest,
    ) -> ice20201109_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    async def list_templates_async(
        self,
        request: ice20201109_models.ListTemplatesRequest,
    ) -> ice20201109_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_templates_with_options_async(request, runtime)

    def delete_editing_projects_with_options(
        self,
        request: ice20201109_models.DeleteEditingProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteEditingProjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteEditingProjectsResponse(),
            self.do_rpcrequest('DeleteEditingProjects', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_editing_projects_with_options_async(
        self,
        request: ice20201109_models.DeleteEditingProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteEditingProjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteEditingProjectsResponse(),
            await self.do_rpcrequest_async('DeleteEditingProjects', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_editing_projects(
        self,
        request: ice20201109_models.DeleteEditingProjectsRequest,
    ) -> ice20201109_models.DeleteEditingProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_editing_projects_with_options(request, runtime)

    async def delete_editing_projects_async(
        self,
        request: ice20201109_models.DeleteEditingProjectsRequest,
    ) -> ice20201109_models.DeleteEditingProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_editing_projects_with_options_async(request, runtime)

    def get_media_info_with_options(
        self,
        request: ice20201109_models.GetMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetMediaInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.GetMediaInfoResponse(),
            self.do_rpcrequest('GetMediaInfo', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_media_info_with_options_async(
        self,
        request: ice20201109_models.GetMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetMediaInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.GetMediaInfoResponse(),
            await self.do_rpcrequest_async('GetMediaInfo', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_media_info(
        self,
        request: ice20201109_models.GetMediaInfoRequest,
    ) -> ice20201109_models.GetMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_info_with_options(request, runtime)

    async def get_media_info_async(
        self,
        request: ice20201109_models.GetMediaInfoRequest,
    ) -> ice20201109_models.GetMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_info_with_options_async(request, runtime)

    def submit_smart_job_with_options(
        self,
        request: ice20201109_models.SubmitSmartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitSmartJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitSmartJobResponse(),
            self.do_rpcrequest('SubmitSmartJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_smart_job_with_options_async(
        self,
        request: ice20201109_models.SubmitSmartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitSmartJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitSmartJobResponse(),
            await self.do_rpcrequest_async('SubmitSmartJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_smart_job(
        self,
        request: ice20201109_models.SubmitSmartJobRequest,
    ) -> ice20201109_models.SubmitSmartJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_smart_job_with_options(request, runtime)

    async def submit_smart_job_async(
        self,
        request: ice20201109_models.SubmitSmartJobRequest,
    ) -> ice20201109_models.SubmitSmartJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_smart_job_with_options_async(request, runtime)

    def submit_delogo_job_with_options(
        self,
        request: ice20201109_models.SubmitDelogoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitDelogoJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitDelogoJobResponse(),
            self.do_rpcrequest('SubmitDelogoJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_delogo_job_with_options_async(
        self,
        request: ice20201109_models.SubmitDelogoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitDelogoJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitDelogoJobResponse(),
            await self.do_rpcrequest_async('SubmitDelogoJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_delogo_job(
        self,
        request: ice20201109_models.SubmitDelogoJobRequest,
    ) -> ice20201109_models.SubmitDelogoJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_delogo_job_with_options(request, runtime)

    async def submit_delogo_job_async(
        self,
        request: ice20201109_models.SubmitDelogoJobRequest,
    ) -> ice20201109_models.SubmitDelogoJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_delogo_job_with_options_async(request, runtime)

    def update_template_with_options(
        self,
        request: ice20201109_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateTemplateResponse(),
            self.do_rpcrequest('UpdateTemplate', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def update_template_with_options_async(
        self,
        request: ice20201109_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateTemplateResponse(),
            await self.do_rpcrequest_async('UpdateTemplate', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def update_template(
        self,
        request: ice20201109_models.UpdateTemplateRequest,
    ) -> ice20201109_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    async def update_template_async(
        self,
        request: ice20201109_models.UpdateTemplateRequest,
    ) -> ice20201109_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_template_with_options_async(request, runtime)

    def submit_audio_produce_job_with_options(
        self,
        request: ice20201109_models.SubmitAudioProduceJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitAudioProduceJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitAudioProduceJobResponse(),
            self.do_rpcrequest('SubmitAudioProduceJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_audio_produce_job_with_options_async(
        self,
        request: ice20201109_models.SubmitAudioProduceJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitAudioProduceJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitAudioProduceJobResponse(),
            await self.do_rpcrequest_async('SubmitAudioProduceJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_audio_produce_job(
        self,
        request: ice20201109_models.SubmitAudioProduceJobRequest,
    ) -> ice20201109_models.SubmitAudioProduceJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_audio_produce_job_with_options(request, runtime)

    async def submit_audio_produce_job_async(
        self,
        request: ice20201109_models.SubmitAudioProduceJobRequest,
    ) -> ice20201109_models.SubmitAudioProduceJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_audio_produce_job_with_options_async(request, runtime)

    def submit_media_producing_job_with_options(
        self,
        request: ice20201109_models.SubmitMediaProducingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitMediaProducingJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitMediaProducingJobResponse(),
            self.do_rpcrequest('SubmitMediaProducingJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_media_producing_job_with_options_async(
        self,
        request: ice20201109_models.SubmitMediaProducingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitMediaProducingJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitMediaProducingJobResponse(),
            await self.do_rpcrequest_async('SubmitMediaProducingJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_media_producing_job(
        self,
        request: ice20201109_models.SubmitMediaProducingJobRequest,
    ) -> ice20201109_models.SubmitMediaProducingJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_media_producing_job_with_options(request, runtime)

    async def submit_media_producing_job_async(
        self,
        request: ice20201109_models.SubmitMediaProducingJobRequest,
    ) -> ice20201109_models.SubmitMediaProducingJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_media_producing_job_with_options_async(request, runtime)

    def update_smart_job_with_options(
        self,
        request: ice20201109_models.UpdateSmartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateSmartJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateSmartJobResponse(),
            self.do_rpcrequest('UpdateSmartJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_smart_job_with_options_async(
        self,
        request: ice20201109_models.UpdateSmartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateSmartJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateSmartJobResponse(),
            await self.do_rpcrequest_async('UpdateSmartJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_smart_job(
        self,
        request: ice20201109_models.UpdateSmartJobRequest,
    ) -> ice20201109_models.UpdateSmartJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_smart_job_with_options(request, runtime)

    async def update_smart_job_async(
        self,
        request: ice20201109_models.UpdateSmartJobRequest,
    ) -> ice20201109_models.UpdateSmartJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_smart_job_with_options_async(request, runtime)

    def list_all_public_media_tags_with_options(
        self,
        request: ice20201109_models.ListAllPublicMediaTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListAllPublicMediaTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.ListAllPublicMediaTagsResponse(),
            self.do_rpcrequest('ListAllPublicMediaTags', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_all_public_media_tags_with_options_async(
        self,
        request: ice20201109_models.ListAllPublicMediaTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListAllPublicMediaTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.ListAllPublicMediaTagsResponse(),
            await self.do_rpcrequest_async('ListAllPublicMediaTags', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_all_public_media_tags(
        self,
        request: ice20201109_models.ListAllPublicMediaTagsRequest,
    ) -> ice20201109_models.ListAllPublicMediaTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_all_public_media_tags_with_options(request, runtime)

    async def list_all_public_media_tags_async(
        self,
        request: ice20201109_models.ListAllPublicMediaTagsRequest,
    ) -> ice20201109_models.ListAllPublicMediaTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_all_public_media_tags_with_options_async(request, runtime)

    def submit_matting_job_with_options(
        self,
        request: ice20201109_models.SubmitMattingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitMattingJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitMattingJobResponse(),
            self.do_rpcrequest('SubmitMattingJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_matting_job_with_options_async(
        self,
        request: ice20201109_models.SubmitMattingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitMattingJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitMattingJobResponse(),
            await self.do_rpcrequest_async('SubmitMattingJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_matting_job(
        self,
        request: ice20201109_models.SubmitMattingJobRequest,
    ) -> ice20201109_models.SubmitMattingJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_matting_job_with_options(request, runtime)

    async def submit_matting_job_async(
        self,
        request: ice20201109_models.SubmitMattingJobRequest,
    ) -> ice20201109_models.SubmitMattingJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_matting_job_with_options_async(request, runtime)

    def get_event_callback_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetEventCallbackResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ice20201109_models.GetEventCallbackResponse(),
            self.do_rpcrequest('GetEventCallback', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_event_callback_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetEventCallbackResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            ice20201109_models.GetEventCallbackResponse(),
            await self.do_rpcrequest_async('GetEventCallback', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_event_callback(self) -> ice20201109_models.GetEventCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_callback_with_options(runtime)

    async def get_event_callback_async(self) -> ice20201109_models.GetEventCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_callback_with_options_async(runtime)

    def list_public_media_basic_infos_with_options(
        self,
        request: ice20201109_models.ListPublicMediaBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListPublicMediaBasicInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.ListPublicMediaBasicInfosResponse(),
            self.do_rpcrequest('ListPublicMediaBasicInfos', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_public_media_basic_infos_with_options_async(
        self,
        request: ice20201109_models.ListPublicMediaBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListPublicMediaBasicInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.ListPublicMediaBasicInfosResponse(),
            await self.do_rpcrequest_async('ListPublicMediaBasicInfos', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_public_media_basic_infos(
        self,
        request: ice20201109_models.ListPublicMediaBasicInfosRequest,
    ) -> ice20201109_models.ListPublicMediaBasicInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_public_media_basic_infos_with_options(request, runtime)

    async def list_public_media_basic_infos_async(
        self,
        request: ice20201109_models.ListPublicMediaBasicInfosRequest,
    ) -> ice20201109_models.ListPublicMediaBasicInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_public_media_basic_infos_with_options_async(request, runtime)

    def submit_cover_job_with_options(
        self,
        request: ice20201109_models.SubmitCoverJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitCoverJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitCoverJobResponse(),
            self.do_rpcrequest('SubmitCoverJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_cover_job_with_options_async(
        self,
        request: ice20201109_models.SubmitCoverJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitCoverJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitCoverJobResponse(),
            await self.do_rpcrequest_async('SubmitCoverJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_cover_job(
        self,
        request: ice20201109_models.SubmitCoverJobRequest,
    ) -> ice20201109_models.SubmitCoverJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_cover_job_with_options(request, runtime)

    async def submit_cover_job_async(
        self,
        request: ice20201109_models.SubmitCoverJobRequest,
    ) -> ice20201109_models.SubmitCoverJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_cover_job_with_options_async(request, runtime)

    def get_smart_handle_job_with_options(
        self,
        request: ice20201109_models.GetSmartHandleJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetSmartHandleJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.GetSmartHandleJobResponse(),
            self.do_rpcrequest('GetSmartHandleJob', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_smart_handle_job_with_options_async(
        self,
        request: ice20201109_models.GetSmartHandleJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetSmartHandleJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.GetSmartHandleJobResponse(),
            await self.do_rpcrequest_async('GetSmartHandleJob', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_smart_handle_job(
        self,
        request: ice20201109_models.GetSmartHandleJobRequest,
    ) -> ice20201109_models.GetSmartHandleJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_smart_handle_job_with_options(request, runtime)

    async def get_smart_handle_job_async(
        self,
        request: ice20201109_models.GetSmartHandleJobRequest,
    ) -> ice20201109_models.GetSmartHandleJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_smart_handle_job_with_options_async(request, runtime)

    def submit_h2vjob_with_options(
        self,
        request: ice20201109_models.SubmitH2VJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitH2VJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitH2VJobResponse(),
            self.do_rpcrequest('SubmitH2VJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_h2vjob_with_options_async(
        self,
        request: ice20201109_models.SubmitH2VJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitH2VJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitH2VJobResponse(),
            await self.do_rpcrequest_async('SubmitH2VJob', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_h2vjob(
        self,
        request: ice20201109_models.SubmitH2VJobRequest,
    ) -> ice20201109_models.SubmitH2VJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_h2vjob_with_options(request, runtime)

    async def submit_h2vjob_async(
        self,
        request: ice20201109_models.SubmitH2VJobRequest,
    ) -> ice20201109_models.SubmitH2VJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_h2vjob_with_options_async(request, runtime)

    def submit_pptcut_job_with_options(
        self,
        request: ice20201109_models.SubmitPPTCutJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitPPTCutJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitPPTCutJobResponse(),
            self.do_rpcrequest('SubmitPPTCutJob', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def submit_pptcut_job_with_options_async(
        self,
        request: ice20201109_models.SubmitPPTCutJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitPPTCutJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitPPTCutJobResponse(),
            await self.do_rpcrequest_async('SubmitPPTCutJob', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def submit_pptcut_job(
        self,
        request: ice20201109_models.SubmitPPTCutJobRequest,
    ) -> ice20201109_models.SubmitPPTCutJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_pptcut_job_with_options(request, runtime)

    async def submit_pptcut_job_async(
        self,
        request: ice20201109_models.SubmitPPTCutJobRequest,
    ) -> ice20201109_models.SubmitPPTCutJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_pptcut_job_with_options_async(request, runtime)
