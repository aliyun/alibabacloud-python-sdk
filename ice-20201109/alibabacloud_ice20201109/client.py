# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

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

    def create_editing_project_with_options(
        self,
        request: ice20201109_models.CreateEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ice20201109_models.CreateEditingProjectResponse().from_map(
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
        return ice20201109_models.CreateEditingProjectResponse().from_map(
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

    def delete_editing_projects_with_options(
        self,
        request: ice20201109_models.DeleteEditingProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteEditingProjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ice20201109_models.DeleteEditingProjectsResponse().from_map(
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
        return ice20201109_models.DeleteEditingProjectsResponse().from_map(
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

    def delete_media_infos_with_options(
        self,
        request: ice20201109_models.DeleteMediaInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteMediaInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ice20201109_models.DeleteMediaInfosResponse().from_map(
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
        return ice20201109_models.DeleteMediaInfosResponse().from_map(
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

    def describe_ice_product_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeIceProductStatusResponse:
        req = open_api_models.OpenApiRequest()
        return ice20201109_models.DescribeIceProductStatusResponse().from_map(
            self.do_rpcrequest('DescribeIceProductStatus', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ice_product_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeIceProductStatusResponse:
        req = open_api_models.OpenApiRequest()
        return ice20201109_models.DescribeIceProductStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeIceProductStatus', '2020-11-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ice_product_status(self) -> ice20201109_models.DescribeIceProductStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ice_product_status_with_options(runtime)

    async def describe_ice_product_status_async(self) -> ice20201109_models.DescribeIceProductStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ice_product_status_with_options_async(runtime)

    def describe_related_authorization_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeRelatedAuthorizationStatusResponse:
        req = open_api_models.OpenApiRequest()
        return ice20201109_models.DescribeRelatedAuthorizationStatusResponse().from_map(
            self.do_rpcrequest('DescribeRelatedAuthorizationStatus', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_related_authorization_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeRelatedAuthorizationStatusResponse:
        req = open_api_models.OpenApiRequest()
        return ice20201109_models.DescribeRelatedAuthorizationStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeRelatedAuthorizationStatus', '2020-11-09', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_related_authorization_status(self) -> ice20201109_models.DescribeRelatedAuthorizationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_related_authorization_status_with_options(runtime)

    async def describe_related_authorization_status_async(self) -> ice20201109_models.DescribeRelatedAuthorizationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_related_authorization_status_with_options_async(runtime)

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
        return ice20201109_models.GetEditingProjectResponse().from_map(
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
        return ice20201109_models.GetEditingProjectResponse().from_map(
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

    def get_media_info_with_options(
        self,
        request: ice20201109_models.GetMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetMediaInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ice20201109_models.GetMediaInfoResponse().from_map(
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
        return ice20201109_models.GetMediaInfoResponse().from_map(
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
        return ice20201109_models.GetMediaProducingJobResponse().from_map(
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
        return ice20201109_models.GetMediaProducingJobResponse().from_map(
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

    def list_all_public_media_tags_with_options(
        self,
        request: ice20201109_models.ListAllPublicMediaTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListAllPublicMediaTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ice20201109_models.ListAllPublicMediaTagsResponse().from_map(
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
        return ice20201109_models.ListAllPublicMediaTagsResponse().from_map(
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

    def list_media_basic_infos_with_options(
        self,
        request: ice20201109_models.ListMediaBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListMediaBasicInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ice20201109_models.ListMediaBasicInfosResponse().from_map(
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
        return ice20201109_models.ListMediaBasicInfosResponse().from_map(
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

    def list_media_producing_jobs_with_options(
        self,
        request: ice20201109_models.ListMediaProducingJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListMediaProducingJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ice20201109_models.ListMediaProducingJobsResponse().from_map(
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
        return ice20201109_models.ListMediaProducingJobsResponse().from_map(
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

    def list_public_media_basic_infos_with_options(
        self,
        request: ice20201109_models.ListPublicMediaBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListPublicMediaBasicInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ice20201109_models.ListPublicMediaBasicInfosResponse().from_map(
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
        return ice20201109_models.ListPublicMediaBasicInfosResponse().from_map(
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

    def register_media_info_with_options(
        self,
        request: ice20201109_models.RegisterMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.RegisterMediaInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ice20201109_models.RegisterMediaInfoResponse().from_map(
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
        return ice20201109_models.RegisterMediaInfoResponse().from_map(
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

    def search_editing_project_with_options(
        self,
        request: ice20201109_models.SearchEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SearchEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ice20201109_models.SearchEditingProjectResponse().from_map(
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
        return ice20201109_models.SearchEditingProjectResponse().from_map(
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

    def submit_media_producing_job_with_options(
        self,
        request: ice20201109_models.SubmitMediaProducingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitMediaProducingJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ice20201109_models.SubmitMediaProducingJobResponse().from_map(
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
        return ice20201109_models.SubmitMediaProducingJobResponse().from_map(
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

    def update_editing_project_with_options(
        self,
        request: ice20201109_models.UpdateEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ice20201109_models.UpdateEditingProjectResponse().from_map(
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
        return ice20201109_models.UpdateEditingProjectResponse().from_map(
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

    def update_media_info_with_options(
        self,
        request: ice20201109_models.UpdateMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateMediaInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ice20201109_models.UpdateMediaInfoResponse().from_map(
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
        return ice20201109_models.UpdateMediaInfoResponse().from_map(
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
