# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mts20140618 import models as mts_20140618_models
from alibabacloud_tea_util import models as util_models


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
            'ap-northeast-2-pop': 'mts.ap-northeast-1.aliyuncs.com',
            'ap-southeast-2': 'mts.ap-northeast-1.aliyuncs.com',
            'ap-southeast-3': 'mts.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'mts.aliyuncs.com',
            'cn-beijing-finance-pop': 'mts.aliyuncs.com',
            'cn-beijing-gov-1': 'mts.aliyuncs.com',
            'cn-beijing-nu16-b01': 'mts.aliyuncs.com',
            'cn-chengdu': 'mts.aliyuncs.com',
            'cn-edge-1': 'mts.aliyuncs.com',
            'cn-fujian': 'mts.aliyuncs.com',
            'cn-haidian-cm12-c01': 'mts.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'mts.aliyuncs.com',
            'cn-hangzhou-finance': 'mts.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'mts.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'mts.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'mts.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'mts.aliyuncs.com',
            'cn-hangzhou-test-306': 'mts.aliyuncs.com',
            'cn-hongkong-finance-pop': 'mts.aliyuncs.com',
            'cn-north-2-gov-1': 'mts.aliyuncs.com',
            'cn-qingdao': 'mts.aliyuncs.com',
            'cn-qingdao-nebula': 'mts.aliyuncs.com',
            'cn-shanghai-et15-b01': 'mts.aliyuncs.com',
            'cn-shanghai-et2-b01': 'mts.aliyuncs.com',
            'cn-shanghai-finance-1': 'mts.aliyuncs.com',
            'cn-shanghai-inner': 'mts.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'mts.aliyuncs.com',
            'cn-shenzhen-finance-1': 'mts.aliyuncs.com',
            'cn-shenzhen-inner': 'mts.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'mts.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'mts.aliyuncs.com',
            'cn-wuhan': 'mts.aliyuncs.com',
            'cn-yushanfang': 'mts.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'mts.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'mts.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'mts.aliyuncs.com',
            'eu-west-1-oxs': 'mts.ap-northeast-1.aliyuncs.com',
            'me-east-1': 'mts.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'mts.ap-northeast-1.aliyuncs.com',
            'us-east-1': 'mts.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('mts', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_media_workflow_with_options(
        self,
        request: mts_20140618_models.ActivateMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ActivateMediaWorkflowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ActivateMediaWorkflowResponse().from_map(
            self.do_rpcrequest('ActivateMediaWorkflow', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def activate_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.ActivateMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ActivateMediaWorkflowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ActivateMediaWorkflowResponse().from_map(
            await self.do_rpcrequest_async('ActivateMediaWorkflow', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def activate_media_workflow(
        self,
        request: mts_20140618_models.ActivateMediaWorkflowRequest,
    ) -> mts_20140618_models.ActivateMediaWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.activate_media_workflow_with_options(request, runtime)

    async def activate_media_workflow_async(
        self,
        request: mts_20140618_models.ActivateMediaWorkflowRequest,
    ) -> mts_20140618_models.ActivateMediaWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.activate_media_workflow_with_options_async(request, runtime)

    def add_asr_pipeline_with_options(
        self,
        request: mts_20140618_models.AddAsrPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddAsrPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddAsrPipelineResponse().from_map(
            self.do_rpcrequest('AddAsrPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_asr_pipeline_with_options_async(
        self,
        request: mts_20140618_models.AddAsrPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddAsrPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddAsrPipelineResponse().from_map(
            await self.do_rpcrequest_async('AddAsrPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_asr_pipeline(
        self,
        request: mts_20140618_models.AddAsrPipelineRequest,
    ) -> mts_20140618_models.AddAsrPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_asr_pipeline_with_options(request, runtime)

    async def add_asr_pipeline_async(
        self,
        request: mts_20140618_models.AddAsrPipelineRequest,
    ) -> mts_20140618_models.AddAsrPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_asr_pipeline_with_options_async(request, runtime)

    def add_category_with_options(
        self,
        request: mts_20140618_models.AddCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddCategoryResponse().from_map(
            self.do_rpcrequest('AddCategory', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_category_with_options_async(
        self,
        request: mts_20140618_models.AddCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddCategoryResponse().from_map(
            await self.do_rpcrequest_async('AddCategory', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_category(
        self,
        request: mts_20140618_models.AddCategoryRequest,
    ) -> mts_20140618_models.AddCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_category_with_options(request, runtime)

    async def add_category_async(
        self,
        request: mts_20140618_models.AddCategoryRequest,
    ) -> mts_20140618_models.AddCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_category_with_options_async(request, runtime)

    def add_censor_pipeline_with_options(
        self,
        request: mts_20140618_models.AddCensorPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddCensorPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddCensorPipelineResponse().from_map(
            self.do_rpcrequest('AddCensorPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_censor_pipeline_with_options_async(
        self,
        request: mts_20140618_models.AddCensorPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddCensorPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddCensorPipelineResponse().from_map(
            await self.do_rpcrequest_async('AddCensorPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_censor_pipeline(
        self,
        request: mts_20140618_models.AddCensorPipelineRequest,
    ) -> mts_20140618_models.AddCensorPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_censor_pipeline_with_options(request, runtime)

    async def add_censor_pipeline_async(
        self,
        request: mts_20140618_models.AddCensorPipelineRequest,
    ) -> mts_20140618_models.AddCensorPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_censor_pipeline_with_options_async(request, runtime)

    def add_cover_pipeline_with_options(
        self,
        request: mts_20140618_models.AddCoverPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddCoverPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddCoverPipelineResponse().from_map(
            self.do_rpcrequest('AddCoverPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_cover_pipeline_with_options_async(
        self,
        request: mts_20140618_models.AddCoverPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddCoverPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddCoverPipelineResponse().from_map(
            await self.do_rpcrequest_async('AddCoverPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_cover_pipeline(
        self,
        request: mts_20140618_models.AddCoverPipelineRequest,
    ) -> mts_20140618_models.AddCoverPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_cover_pipeline_with_options(request, runtime)

    async def add_cover_pipeline_async(
        self,
        request: mts_20140618_models.AddCoverPipelineRequest,
    ) -> mts_20140618_models.AddCoverPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_cover_pipeline_with_options_async(request, runtime)

    def add_mctemplate_with_options(
        self,
        request: mts_20140618_models.AddMCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMCTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddMCTemplateResponse().from_map(
            self.do_rpcrequest('AddMCTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_mctemplate_with_options_async(
        self,
        request: mts_20140618_models.AddMCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMCTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddMCTemplateResponse().from_map(
            await self.do_rpcrequest_async('AddMCTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_mctemplate(
        self,
        request: mts_20140618_models.AddMCTemplateRequest,
    ) -> mts_20140618_models.AddMCTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_mctemplate_with_options(request, runtime)

    async def add_mctemplate_async(
        self,
        request: mts_20140618_models.AddMCTemplateRequest,
    ) -> mts_20140618_models.AddMCTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_mctemplate_with_options_async(request, runtime)

    def add_media_with_options(
        self,
        request: mts_20140618_models.AddMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddMediaResponse().from_map(
            self.do_rpcrequest('AddMedia', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_media_with_options_async(
        self,
        request: mts_20140618_models.AddMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddMediaResponse().from_map(
            await self.do_rpcrequest_async('AddMedia', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_media(
        self,
        request: mts_20140618_models.AddMediaRequest,
    ) -> mts_20140618_models.AddMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_media_with_options(request, runtime)

    async def add_media_async(
        self,
        request: mts_20140618_models.AddMediaRequest,
    ) -> mts_20140618_models.AddMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_media_with_options_async(request, runtime)

    def add_media_tag_with_options(
        self,
        request: mts_20140618_models.AddMediaTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMediaTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddMediaTagResponse().from_map(
            self.do_rpcrequest('AddMediaTag', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_media_tag_with_options_async(
        self,
        request: mts_20140618_models.AddMediaTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMediaTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddMediaTagResponse().from_map(
            await self.do_rpcrequest_async('AddMediaTag', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_media_tag(
        self,
        request: mts_20140618_models.AddMediaTagRequest,
    ) -> mts_20140618_models.AddMediaTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_media_tag_with_options(request, runtime)

    async def add_media_tag_async(
        self,
        request: mts_20140618_models.AddMediaTagRequest,
    ) -> mts_20140618_models.AddMediaTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_media_tag_with_options_async(request, runtime)

    def add_media_workflow_with_options(
        self,
        request: mts_20140618_models.AddMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMediaWorkflowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddMediaWorkflowResponse().from_map(
            self.do_rpcrequest('AddMediaWorkflow', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.AddMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMediaWorkflowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddMediaWorkflowResponse().from_map(
            await self.do_rpcrequest_async('AddMediaWorkflow', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_media_workflow(
        self,
        request: mts_20140618_models.AddMediaWorkflowRequest,
    ) -> mts_20140618_models.AddMediaWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_media_workflow_with_options(request, runtime)

    async def add_media_workflow_async(
        self,
        request: mts_20140618_models.AddMediaWorkflowRequest,
    ) -> mts_20140618_models.AddMediaWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_media_workflow_with_options_async(request, runtime)

    def add_pipeline_with_options(
        self,
        request: mts_20140618_models.AddPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddPipelineResponse().from_map(
            self.do_rpcrequest('AddPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_pipeline_with_options_async(
        self,
        request: mts_20140618_models.AddPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddPipelineResponse().from_map(
            await self.do_rpcrequest_async('AddPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_pipeline(
        self,
        request: mts_20140618_models.AddPipelineRequest,
    ) -> mts_20140618_models.AddPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_pipeline_with_options(request, runtime)

    async def add_pipeline_async(
        self,
        request: mts_20140618_models.AddPipelineRequest,
    ) -> mts_20140618_models.AddPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_pipeline_with_options_async(request, runtime)

    def add_porn_pipeline_with_options(
        self,
        request: mts_20140618_models.AddPornPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddPornPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddPornPipelineResponse().from_map(
            self.do_rpcrequest('AddPornPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_porn_pipeline_with_options_async(
        self,
        request: mts_20140618_models.AddPornPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddPornPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddPornPipelineResponse().from_map(
            await self.do_rpcrequest_async('AddPornPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_porn_pipeline(
        self,
        request: mts_20140618_models.AddPornPipelineRequest,
    ) -> mts_20140618_models.AddPornPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_porn_pipeline_with_options(request, runtime)

    async def add_porn_pipeline_async(
        self,
        request: mts_20140618_models.AddPornPipelineRequest,
    ) -> mts_20140618_models.AddPornPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_porn_pipeline_with_options_async(request, runtime)

    def add_smarttag_template_with_options(
        self,
        request: mts_20140618_models.AddSmarttagTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddSmarttagTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddSmarttagTemplateResponse().from_map(
            self.do_rpcrequest('AddSmarttagTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_smarttag_template_with_options_async(
        self,
        request: mts_20140618_models.AddSmarttagTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddSmarttagTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddSmarttagTemplateResponse().from_map(
            await self.do_rpcrequest_async('AddSmarttagTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_smarttag_template(
        self,
        request: mts_20140618_models.AddSmarttagTemplateRequest,
    ) -> mts_20140618_models.AddSmarttagTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_smarttag_template_with_options(request, runtime)

    async def add_smarttag_template_async(
        self,
        request: mts_20140618_models.AddSmarttagTemplateRequest,
    ) -> mts_20140618_models.AddSmarttagTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_smarttag_template_with_options_async(request, runtime)

    def add_template_with_options(
        self,
        request: mts_20140618_models.AddTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddTemplateResponse().from_map(
            self.do_rpcrequest('AddTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_template_with_options_async(
        self,
        request: mts_20140618_models.AddTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddTemplateResponse().from_map(
            await self.do_rpcrequest_async('AddTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_template(
        self,
        request: mts_20140618_models.AddTemplateRequest,
    ) -> mts_20140618_models.AddTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_template_with_options(request, runtime)

    async def add_template_async(
        self,
        request: mts_20140618_models.AddTemplateRequest,
    ) -> mts_20140618_models.AddTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_template_with_options_async(request, runtime)

    def add_terrorism_pipeline_with_options(
        self,
        request: mts_20140618_models.AddTerrorismPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddTerrorismPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddTerrorismPipelineResponse().from_map(
            self.do_rpcrequest('AddTerrorismPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_terrorism_pipeline_with_options_async(
        self,
        request: mts_20140618_models.AddTerrorismPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddTerrorismPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddTerrorismPipelineResponse().from_map(
            await self.do_rpcrequest_async('AddTerrorismPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_terrorism_pipeline(
        self,
        request: mts_20140618_models.AddTerrorismPipelineRequest,
    ) -> mts_20140618_models.AddTerrorismPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_terrorism_pipeline_with_options(request, runtime)

    async def add_terrorism_pipeline_async(
        self,
        request: mts_20140618_models.AddTerrorismPipelineRequest,
    ) -> mts_20140618_models.AddTerrorismPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_terrorism_pipeline_with_options_async(request, runtime)

    def add_water_mark_template_with_options(
        self,
        request: mts_20140618_models.AddWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddWaterMarkTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddWaterMarkTemplateResponse().from_map(
            self.do_rpcrequest('AddWaterMarkTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_water_mark_template_with_options_async(
        self,
        request: mts_20140618_models.AddWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddWaterMarkTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.AddWaterMarkTemplateResponse().from_map(
            await self.do_rpcrequest_async('AddWaterMarkTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_water_mark_template(
        self,
        request: mts_20140618_models.AddWaterMarkTemplateRequest,
    ) -> mts_20140618_models.AddWaterMarkTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_water_mark_template_with_options(request, runtime)

    async def add_water_mark_template_async(
        self,
        request: mts_20140618_models.AddWaterMarkTemplateRequest,
    ) -> mts_20140618_models.AddWaterMarkTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_water_mark_template_with_options_async(request, runtime)

    def bind_input_bucket_with_options(
        self,
        request: mts_20140618_models.BindInputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.BindInputBucketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.BindInputBucketResponse().from_map(
            self.do_rpcrequest('BindInputBucket', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_input_bucket_with_options_async(
        self,
        request: mts_20140618_models.BindInputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.BindInputBucketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.BindInputBucketResponse().from_map(
            await self.do_rpcrequest_async('BindInputBucket', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_input_bucket(
        self,
        request: mts_20140618_models.BindInputBucketRequest,
    ) -> mts_20140618_models.BindInputBucketResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_input_bucket_with_options(request, runtime)

    async def bind_input_bucket_async(
        self,
        request: mts_20140618_models.BindInputBucketRequest,
    ) -> mts_20140618_models.BindInputBucketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_input_bucket_with_options_async(request, runtime)

    def bind_output_bucket_with_options(
        self,
        request: mts_20140618_models.BindOutputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.BindOutputBucketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.BindOutputBucketResponse().from_map(
            self.do_rpcrequest('BindOutputBucket', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_output_bucket_with_options_async(
        self,
        request: mts_20140618_models.BindOutputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.BindOutputBucketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.BindOutputBucketResponse().from_map(
            await self.do_rpcrequest_async('BindOutputBucket', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_output_bucket(
        self,
        request: mts_20140618_models.BindOutputBucketRequest,
    ) -> mts_20140618_models.BindOutputBucketResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_output_bucket_with_options(request, runtime)

    async def bind_output_bucket_async(
        self,
        request: mts_20140618_models.BindOutputBucketRequest,
    ) -> mts_20140618_models.BindOutputBucketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_output_bucket_with_options_async(request, runtime)

    def cancel_job_with_options(
        self,
        request: mts_20140618_models.CancelJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CancelJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.CancelJobResponse().from_map(
            self.do_rpcrequest('CancelJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_job_with_options_async(
        self,
        request: mts_20140618_models.CancelJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CancelJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.CancelJobResponse().from_map(
            await self.do_rpcrequest_async('CancelJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_job(
        self,
        request: mts_20140618_models.CancelJobRequest,
    ) -> mts_20140618_models.CancelJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_job_with_options(request, runtime)

    async def cancel_job_async(
        self,
        request: mts_20140618_models.CancelJobRequest,
    ) -> mts_20140618_models.CancelJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_job_with_options_async(request, runtime)

    def category_tree_with_options(
        self,
        request: mts_20140618_models.CategoryTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CategoryTreeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.CategoryTreeResponse().from_map(
            self.do_rpcrequest('CategoryTree', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def category_tree_with_options_async(
        self,
        request: mts_20140618_models.CategoryTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CategoryTreeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.CategoryTreeResponse().from_map(
            await self.do_rpcrequest_async('CategoryTree', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def category_tree(
        self,
        request: mts_20140618_models.CategoryTreeRequest,
    ) -> mts_20140618_models.CategoryTreeResponse:
        runtime = util_models.RuntimeOptions()
        return self.category_tree_with_options(request, runtime)

    async def category_tree_async(
        self,
        request: mts_20140618_models.CategoryTreeRequest,
    ) -> mts_20140618_models.CategoryTreeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.category_tree_with_options_async(request, runtime)

    def check_resource_with_options(
        self,
        request: mts_20140618_models.CheckResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CheckResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.CheckResourceResponse().from_map(
            self.do_rpcrequest('CheckResource', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_resource_with_options_async(
        self,
        request: mts_20140618_models.CheckResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CheckResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.CheckResourceResponse().from_map(
            await self.do_rpcrequest_async('CheckResource', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_resource(
        self,
        request: mts_20140618_models.CheckResourceRequest,
    ) -> mts_20140618_models.CheckResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_resource_with_options(request, runtime)

    async def check_resource_async(
        self,
        request: mts_20140618_models.CheckResourceRequest,
    ) -> mts_20140618_models.CheckResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_resource_with_options_async(request, runtime)

    def create_fp_shot_dbwith_options(
        self,
        request: mts_20140618_models.CreateFpShotDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateFpShotDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.CreateFpShotDBResponse().from_map(
            self.do_rpcrequest('CreateFpShotDB', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_fp_shot_dbwith_options_async(
        self,
        request: mts_20140618_models.CreateFpShotDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateFpShotDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.CreateFpShotDBResponse().from_map(
            await self.do_rpcrequest_async('CreateFpShotDB', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_fp_shot_db(
        self,
        request: mts_20140618_models.CreateFpShotDBRequest,
    ) -> mts_20140618_models.CreateFpShotDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_fp_shot_dbwith_options(request, runtime)

    async def create_fp_shot_db_async(
        self,
        request: mts_20140618_models.CreateFpShotDBRequest,
    ) -> mts_20140618_models.CreateFpShotDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_fp_shot_dbwith_options_async(request, runtime)

    def create_mcu_template_with_options(
        self,
        request: mts_20140618_models.CreateMcuTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateMcuTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.CreateMcuTemplateResponse().from_map(
            self.do_rpcrequest('CreateMcuTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_mcu_template_with_options_async(
        self,
        request: mts_20140618_models.CreateMcuTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateMcuTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.CreateMcuTemplateResponse().from_map(
            await self.do_rpcrequest_async('CreateMcuTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_mcu_template(
        self,
        request: mts_20140618_models.CreateMcuTemplateRequest,
    ) -> mts_20140618_models.CreateMcuTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_mcu_template_with_options(request, runtime)

    async def create_mcu_template_async(
        self,
        request: mts_20140618_models.CreateMcuTemplateRequest,
    ) -> mts_20140618_models.CreateMcuTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_mcu_template_with_options_async(request, runtime)

    def create_session_with_options(
        self,
        request: mts_20140618_models.CreateSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.CreateSessionResponse().from_map(
            self.do_rpcrequest('CreateSession', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_session_with_options_async(
        self,
        request: mts_20140618_models.CreateSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.CreateSessionResponse().from_map(
            await self.do_rpcrequest_async('CreateSession', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_session(
        self,
        request: mts_20140618_models.CreateSessionRequest,
    ) -> mts_20140618_models.CreateSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_session_with_options(request, runtime)

    async def create_session_async(
        self,
        request: mts_20140618_models.CreateSessionRequest,
    ) -> mts_20140618_models.CreateSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_session_with_options_async(request, runtime)

    def deactivate_media_workflow_with_options(
        self,
        request: mts_20140618_models.DeactivateMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeactivateMediaWorkflowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeactivateMediaWorkflowResponse().from_map(
            self.do_rpcrequest('DeactivateMediaWorkflow', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deactivate_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.DeactivateMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeactivateMediaWorkflowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeactivateMediaWorkflowResponse().from_map(
            await self.do_rpcrequest_async('DeactivateMediaWorkflow', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deactivate_media_workflow(
        self,
        request: mts_20140618_models.DeactivateMediaWorkflowRequest,
    ) -> mts_20140618_models.DeactivateMediaWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.deactivate_media_workflow_with_options(request, runtime)

    async def deactivate_media_workflow_async(
        self,
        request: mts_20140618_models.DeactivateMediaWorkflowRequest,
    ) -> mts_20140618_models.DeactivateMediaWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deactivate_media_workflow_with_options_async(request, runtime)

    def decrypt_key_with_options(
        self,
        request: mts_20140618_models.DecryptKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DecryptKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DecryptKeyResponse().from_map(
            self.do_rpcrequest('DecryptKey', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def decrypt_key_with_options_async(
        self,
        request: mts_20140618_models.DecryptKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DecryptKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DecryptKeyResponse().from_map(
            await self.do_rpcrequest_async('DecryptKey', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def decrypt_key(
        self,
        request: mts_20140618_models.DecryptKeyRequest,
    ) -> mts_20140618_models.DecryptKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.decrypt_key_with_options(request, runtime)

    async def decrypt_key_async(
        self,
        request: mts_20140618_models.DecryptKeyRequest,
    ) -> mts_20140618_models.DecryptKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.decrypt_key_with_options_async(request, runtime)

    def delete_category_with_options(
        self,
        request: mts_20140618_models.DeleteCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteCategoryResponse().from_map(
            self.do_rpcrequest('DeleteCategory', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_category_with_options_async(
        self,
        request: mts_20140618_models.DeleteCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteCategoryResponse().from_map(
            await self.do_rpcrequest_async('DeleteCategory', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_category(
        self,
        request: mts_20140618_models.DeleteCategoryRequest,
    ) -> mts_20140618_models.DeleteCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_category_with_options(request, runtime)

    async def delete_category_async(
        self,
        request: mts_20140618_models.DeleteCategoryRequest,
    ) -> mts_20140618_models.DeleteCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_category_with_options_async(request, runtime)

    def delete_mctemplate_with_options(
        self,
        request: mts_20140618_models.DeleteMCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMCTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteMCTemplateResponse().from_map(
            self.do_rpcrequest('DeleteMCTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_mctemplate_with_options_async(
        self,
        request: mts_20140618_models.DeleteMCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMCTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteMCTemplateResponse().from_map(
            await self.do_rpcrequest_async('DeleteMCTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_mctemplate(
        self,
        request: mts_20140618_models.DeleteMCTemplateRequest,
    ) -> mts_20140618_models.DeleteMCTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_mctemplate_with_options(request, runtime)

    async def delete_mctemplate_async(
        self,
        request: mts_20140618_models.DeleteMCTemplateRequest,
    ) -> mts_20140618_models.DeleteMCTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_mctemplate_with_options_async(request, runtime)

    def delete_mcu_job_with_options(
        self,
        request: mts_20140618_models.DeleteMcuJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMcuJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteMcuJobResponse().from_map(
            self.do_rpcrequest('DeleteMcuJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_mcu_job_with_options_async(
        self,
        request: mts_20140618_models.DeleteMcuJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMcuJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteMcuJobResponse().from_map(
            await self.do_rpcrequest_async('DeleteMcuJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_mcu_job(
        self,
        request: mts_20140618_models.DeleteMcuJobRequest,
    ) -> mts_20140618_models.DeleteMcuJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_mcu_job_with_options(request, runtime)

    async def delete_mcu_job_async(
        self,
        request: mts_20140618_models.DeleteMcuJobRequest,
    ) -> mts_20140618_models.DeleteMcuJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_mcu_job_with_options_async(request, runtime)

    def delete_mcu_template_with_options(
        self,
        request: mts_20140618_models.DeleteMcuTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMcuTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteMcuTemplateResponse().from_map(
            self.do_rpcrequest('DeleteMcuTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_mcu_template_with_options_async(
        self,
        request: mts_20140618_models.DeleteMcuTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMcuTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteMcuTemplateResponse().from_map(
            await self.do_rpcrequest_async('DeleteMcuTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_mcu_template(
        self,
        request: mts_20140618_models.DeleteMcuTemplateRequest,
    ) -> mts_20140618_models.DeleteMcuTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_mcu_template_with_options(request, runtime)

    async def delete_mcu_template_async(
        self,
        request: mts_20140618_models.DeleteMcuTemplateRequest,
    ) -> mts_20140618_models.DeleteMcuTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_mcu_template_with_options_async(request, runtime)

    def delete_media_with_options(
        self,
        request: mts_20140618_models.DeleteMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteMediaResponse().from_map(
            self.do_rpcrequest('DeleteMedia', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_media_with_options_async(
        self,
        request: mts_20140618_models.DeleteMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteMediaResponse().from_map(
            await self.do_rpcrequest_async('DeleteMedia', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_media(
        self,
        request: mts_20140618_models.DeleteMediaRequest,
    ) -> mts_20140618_models.DeleteMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_media_with_options(request, runtime)

    async def delete_media_async(
        self,
        request: mts_20140618_models.DeleteMediaRequest,
    ) -> mts_20140618_models.DeleteMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_media_with_options_async(request, runtime)

    def delete_media_tag_with_options(
        self,
        request: mts_20140618_models.DeleteMediaTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMediaTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteMediaTagResponse().from_map(
            self.do_rpcrequest('DeleteMediaTag', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_media_tag_with_options_async(
        self,
        request: mts_20140618_models.DeleteMediaTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMediaTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteMediaTagResponse().from_map(
            await self.do_rpcrequest_async('DeleteMediaTag', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_media_tag(
        self,
        request: mts_20140618_models.DeleteMediaTagRequest,
    ) -> mts_20140618_models.DeleteMediaTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_media_tag_with_options(request, runtime)

    async def delete_media_tag_async(
        self,
        request: mts_20140618_models.DeleteMediaTagRequest,
    ) -> mts_20140618_models.DeleteMediaTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_media_tag_with_options_async(request, runtime)

    def delete_media_workflow_with_options(
        self,
        request: mts_20140618_models.DeleteMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMediaWorkflowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteMediaWorkflowResponse().from_map(
            self.do_rpcrequest('DeleteMediaWorkflow', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.DeleteMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMediaWorkflowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteMediaWorkflowResponse().from_map(
            await self.do_rpcrequest_async('DeleteMediaWorkflow', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_media_workflow(
        self,
        request: mts_20140618_models.DeleteMediaWorkflowRequest,
    ) -> mts_20140618_models.DeleteMediaWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_media_workflow_with_options(request, runtime)

    async def delete_media_workflow_async(
        self,
        request: mts_20140618_models.DeleteMediaWorkflowRequest,
    ) -> mts_20140618_models.DeleteMediaWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_media_workflow_with_options_async(request, runtime)

    def delete_pipeline_with_options(
        self,
        request: mts_20140618_models.DeletePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeletePipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeletePipelineResponse().from_map(
            self.do_rpcrequest('DeletePipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_pipeline_with_options_async(
        self,
        request: mts_20140618_models.DeletePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeletePipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeletePipelineResponse().from_map(
            await self.do_rpcrequest_async('DeletePipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_pipeline(
        self,
        request: mts_20140618_models.DeletePipelineRequest,
    ) -> mts_20140618_models.DeletePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_pipeline_with_options(request, runtime)

    async def delete_pipeline_async(
        self,
        request: mts_20140618_models.DeletePipelineRequest,
    ) -> mts_20140618_models.DeletePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_pipeline_with_options_async(request, runtime)

    def delete_smarttag_template_with_options(
        self,
        request: mts_20140618_models.DeleteSmarttagTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteSmarttagTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteSmarttagTemplateResponse().from_map(
            self.do_rpcrequest('DeleteSmarttagTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_smarttag_template_with_options_async(
        self,
        request: mts_20140618_models.DeleteSmarttagTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteSmarttagTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteSmarttagTemplateResponse().from_map(
            await self.do_rpcrequest_async('DeleteSmarttagTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_smarttag_template(
        self,
        request: mts_20140618_models.DeleteSmarttagTemplateRequest,
    ) -> mts_20140618_models.DeleteSmarttagTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_smarttag_template_with_options(request, runtime)

    async def delete_smarttag_template_async(
        self,
        request: mts_20140618_models.DeleteSmarttagTemplateRequest,
    ) -> mts_20140618_models.DeleteSmarttagTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_smarttag_template_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: mts_20140618_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteTemplateResponse().from_map(
            self.do_rpcrequest('DeleteTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: mts_20140618_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteTemplateResponse().from_map(
            await self.do_rpcrequest_async('DeleteTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_template(
        self,
        request: mts_20140618_models.DeleteTemplateRequest,
    ) -> mts_20140618_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: mts_20140618_models.DeleteTemplateRequest,
    ) -> mts_20140618_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def delete_water_mark_template_with_options(
        self,
        request: mts_20140618_models.DeleteWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteWaterMarkTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteWaterMarkTemplateResponse().from_map(
            self.do_rpcrequest('DeleteWaterMarkTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_water_mark_template_with_options_async(
        self,
        request: mts_20140618_models.DeleteWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteWaterMarkTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DeleteWaterMarkTemplateResponse().from_map(
            await self.do_rpcrequest_async('DeleteWaterMarkTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_water_mark_template(
        self,
        request: mts_20140618_models.DeleteWaterMarkTemplateRequest,
    ) -> mts_20140618_models.DeleteWaterMarkTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_water_mark_template_with_options(request, runtime)

    async def delete_water_mark_template_async(
        self,
        request: mts_20140618_models.DeleteWaterMarkTemplateRequest,
    ) -> mts_20140618_models.DeleteWaterMarkTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_water_mark_template_with_options_async(request, runtime)

    def describe_mts_user_resource_package_with_options(
        self,
        request: mts_20140618_models.DescribeMtsUserResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DescribeMtsUserResourcePackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DescribeMtsUserResourcePackageResponse().from_map(
            self.do_rpcrequest('DescribeMtsUserResourcePackage', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_mts_user_resource_package_with_options_async(
        self,
        request: mts_20140618_models.DescribeMtsUserResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DescribeMtsUserResourcePackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.DescribeMtsUserResourcePackageResponse().from_map(
            await self.do_rpcrequest_async('DescribeMtsUserResourcePackage', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mts_user_resource_package(
        self,
        request: mts_20140618_models.DescribeMtsUserResourcePackageRequest,
    ) -> mts_20140618_models.DescribeMtsUserResourcePackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_mts_user_resource_package_with_options(request, runtime)

    async def describe_mts_user_resource_package_async(
        self,
        request: mts_20140618_models.DescribeMtsUserResourcePackageRequest,
    ) -> mts_20140618_models.DescribeMtsUserResourcePackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_mts_user_resource_package_with_options_async(request, runtime)

    def get_license_with_options(
        self,
        request: mts_20140618_models.GetLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.GetLicenseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.GetLicenseResponse().from_map(
            self.do_rpcrequest('GetLicense', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_license_with_options_async(
        self,
        request: mts_20140618_models.GetLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.GetLicenseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.GetLicenseResponse().from_map(
            await self.do_rpcrequest_async('GetLicense', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_license(
        self,
        request: mts_20140618_models.GetLicenseRequest,
    ) -> mts_20140618_models.GetLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_license_with_options(request, runtime)

    async def get_license_async(
        self,
        request: mts_20140618_models.GetLicenseRequest,
    ) -> mts_20140618_models.GetLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_license_with_options_async(request, runtime)

    def get_package_with_options(
        self,
        request: mts_20140618_models.GetPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.GetPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.GetPackageResponse().from_map(
            self.do_rpcrequest('GetPackage', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_package_with_options_async(
        self,
        request: mts_20140618_models.GetPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.GetPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.GetPackageResponse().from_map(
            await self.do_rpcrequest_async('GetPackage', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_package(
        self,
        request: mts_20140618_models.GetPackageRequest,
    ) -> mts_20140618_models.GetPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_package_with_options(request, runtime)

    async def get_package_async(
        self,
        request: mts_20140618_models.GetPackageRequest,
    ) -> mts_20140618_models.GetPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_package_with_options_async(request, runtime)

    def list_all_category_with_options(
        self,
        request: mts_20140618_models.ListAllCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListAllCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListAllCategoryResponse().from_map(
            self.do_rpcrequest('ListAllCategory', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_all_category_with_options_async(
        self,
        request: mts_20140618_models.ListAllCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListAllCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListAllCategoryResponse().from_map(
            await self.do_rpcrequest_async('ListAllCategory', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_all_category(
        self,
        request: mts_20140618_models.ListAllCategoryRequest,
    ) -> mts_20140618_models.ListAllCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_all_category_with_options(request, runtime)

    async def list_all_category_async(
        self,
        request: mts_20140618_models.ListAllCategoryRequest,
    ) -> mts_20140618_models.ListAllCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_all_category_with_options_async(request, runtime)

    def list_all_media_bucket_with_options(
        self,
        request: mts_20140618_models.ListAllMediaBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListAllMediaBucketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListAllMediaBucketResponse().from_map(
            self.do_rpcrequest('ListAllMediaBucket', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_all_media_bucket_with_options_async(
        self,
        request: mts_20140618_models.ListAllMediaBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListAllMediaBucketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListAllMediaBucketResponse().from_map(
            await self.do_rpcrequest_async('ListAllMediaBucket', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_all_media_bucket(
        self,
        request: mts_20140618_models.ListAllMediaBucketRequest,
    ) -> mts_20140618_models.ListAllMediaBucketResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_all_media_bucket_with_options(request, runtime)

    async def list_all_media_bucket_async(
        self,
        request: mts_20140618_models.ListAllMediaBucketRequest,
    ) -> mts_20140618_models.ListAllMediaBucketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_all_media_bucket_with_options_async(request, runtime)

    def list_asr_pipeline_with_options(
        self,
        request: mts_20140618_models.ListAsrPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListAsrPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListAsrPipelineResponse().from_map(
            self.do_rpcrequest('ListAsrPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_asr_pipeline_with_options_async(
        self,
        request: mts_20140618_models.ListAsrPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListAsrPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListAsrPipelineResponse().from_map(
            await self.do_rpcrequest_async('ListAsrPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_asr_pipeline(
        self,
        request: mts_20140618_models.ListAsrPipelineRequest,
    ) -> mts_20140618_models.ListAsrPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_asr_pipeline_with_options(request, runtime)

    async def list_asr_pipeline_async(
        self,
        request: mts_20140618_models.ListAsrPipelineRequest,
    ) -> mts_20140618_models.ListAsrPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_asr_pipeline_with_options_async(request, runtime)

    def list_censor_pipeline_with_options(
        self,
        request: mts_20140618_models.ListCensorPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCensorPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListCensorPipelineResponse().from_map(
            self.do_rpcrequest('ListCensorPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_censor_pipeline_with_options_async(
        self,
        request: mts_20140618_models.ListCensorPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCensorPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListCensorPipelineResponse().from_map(
            await self.do_rpcrequest_async('ListCensorPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_censor_pipeline(
        self,
        request: mts_20140618_models.ListCensorPipelineRequest,
    ) -> mts_20140618_models.ListCensorPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_censor_pipeline_with_options(request, runtime)

    async def list_censor_pipeline_async(
        self,
        request: mts_20140618_models.ListCensorPipelineRequest,
    ) -> mts_20140618_models.ListCensorPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_censor_pipeline_with_options_async(request, runtime)

    def list_cover_pipeline_with_options(
        self,
        request: mts_20140618_models.ListCoverPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCoverPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListCoverPipelineResponse().from_map(
            self.do_rpcrequest('ListCoverPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cover_pipeline_with_options_async(
        self,
        request: mts_20140618_models.ListCoverPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCoverPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListCoverPipelineResponse().from_map(
            await self.do_rpcrequest_async('ListCoverPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cover_pipeline(
        self,
        request: mts_20140618_models.ListCoverPipelineRequest,
    ) -> mts_20140618_models.ListCoverPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cover_pipeline_with_options(request, runtime)

    async def list_cover_pipeline_async(
        self,
        request: mts_20140618_models.ListCoverPipelineRequest,
    ) -> mts_20140618_models.ListCoverPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cover_pipeline_with_options_async(request, runtime)

    def list_custom_persons_with_options(
        self,
        request: mts_20140618_models.ListCustomPersonsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCustomPersonsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListCustomPersonsResponse().from_map(
            self.do_rpcrequest('ListCustomPersons', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_custom_persons_with_options_async(
        self,
        request: mts_20140618_models.ListCustomPersonsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCustomPersonsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListCustomPersonsResponse().from_map(
            await self.do_rpcrequest_async('ListCustomPersons', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_custom_persons(
        self,
        request: mts_20140618_models.ListCustomPersonsRequest,
    ) -> mts_20140618_models.ListCustomPersonsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_custom_persons_with_options(request, runtime)

    async def list_custom_persons_async(
        self,
        request: mts_20140618_models.ListCustomPersonsRequest,
    ) -> mts_20140618_models.ListCustomPersonsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_persons_with_options_async(request, runtime)

    def list_fp_shot_dbwith_options(
        self,
        request: mts_20140618_models.ListFpShotDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListFpShotDBResponse().from_map(
            self.do_rpcrequest('ListFpShotDB', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_fp_shot_dbwith_options_async(
        self,
        request: mts_20140618_models.ListFpShotDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListFpShotDBResponse().from_map(
            await self.do_rpcrequest_async('ListFpShotDB', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_fp_shot_db(
        self,
        request: mts_20140618_models.ListFpShotDBRequest,
    ) -> mts_20140618_models.ListFpShotDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_fp_shot_dbwith_options(request, runtime)

    async def list_fp_shot_db_async(
        self,
        request: mts_20140618_models.ListFpShotDBRequest,
    ) -> mts_20140618_models.ListFpShotDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_fp_shot_dbwith_options_async(request, runtime)

    def list_fp_shot_files_with_options(
        self,
        request: mts_20140618_models.ListFpShotFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListFpShotFilesResponse().from_map(
            self.do_rpcrequest('ListFpShotFiles', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_fp_shot_files_with_options_async(
        self,
        request: mts_20140618_models.ListFpShotFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListFpShotFilesResponse().from_map(
            await self.do_rpcrequest_async('ListFpShotFiles', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_fp_shot_files(
        self,
        request: mts_20140618_models.ListFpShotFilesRequest,
    ) -> mts_20140618_models.ListFpShotFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_fp_shot_files_with_options(request, runtime)

    async def list_fp_shot_files_async(
        self,
        request: mts_20140618_models.ListFpShotFilesRequest,
    ) -> mts_20140618_models.ListFpShotFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_fp_shot_files_with_options_async(request, runtime)

    def list_fp_shot_notary_with_options(
        self,
        request: mts_20140618_models.ListFpShotNotaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotNotaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListFpShotNotaryResponse().from_map(
            self.do_rpcrequest('ListFpShotNotary', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_fp_shot_notary_with_options_async(
        self,
        request: mts_20140618_models.ListFpShotNotaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotNotaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListFpShotNotaryResponse().from_map(
            await self.do_rpcrequest_async('ListFpShotNotary', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_fp_shot_notary(
        self,
        request: mts_20140618_models.ListFpShotNotaryRequest,
    ) -> mts_20140618_models.ListFpShotNotaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_fp_shot_notary_with_options(request, runtime)

    async def list_fp_shot_notary_async(
        self,
        request: mts_20140618_models.ListFpShotNotaryRequest,
    ) -> mts_20140618_models.ListFpShotNotaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_fp_shot_notary_with_options_async(request, runtime)

    def list_job_with_options(
        self,
        request: mts_20140618_models.ListJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListJobResponse().from_map(
            self.do_rpcrequest('ListJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_job_with_options_async(
        self,
        request: mts_20140618_models.ListJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListJobResponse().from_map(
            await self.do_rpcrequest_async('ListJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_job(
        self,
        request: mts_20140618_models.ListJobRequest,
    ) -> mts_20140618_models.ListJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_job_with_options(request, runtime)

    async def list_job_async(
        self,
        request: mts_20140618_models.ListJobRequest,
    ) -> mts_20140618_models.ListJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_job_with_options_async(request, runtime)

    def list_media_with_options(
        self,
        request: mts_20140618_models.ListMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListMediaResponse().from_map(
            self.do_rpcrequest('ListMedia', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_media_with_options_async(
        self,
        request: mts_20140618_models.ListMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListMediaResponse().from_map(
            await self.do_rpcrequest_async('ListMedia', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_media(
        self,
        request: mts_20140618_models.ListMediaRequest,
    ) -> mts_20140618_models.ListMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_media_with_options(request, runtime)

    async def list_media_async(
        self,
        request: mts_20140618_models.ListMediaRequest,
    ) -> mts_20140618_models.ListMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_media_with_options_async(request, runtime)

    def list_media_workflow_executions_with_options(
        self,
        request: mts_20140618_models.ListMediaWorkflowExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListMediaWorkflowExecutionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListMediaWorkflowExecutionsResponse().from_map(
            self.do_rpcrequest('ListMediaWorkflowExecutions', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_media_workflow_executions_with_options_async(
        self,
        request: mts_20140618_models.ListMediaWorkflowExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListMediaWorkflowExecutionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListMediaWorkflowExecutionsResponse().from_map(
            await self.do_rpcrequest_async('ListMediaWorkflowExecutions', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_media_workflow_executions(
        self,
        request: mts_20140618_models.ListMediaWorkflowExecutionsRequest,
    ) -> mts_20140618_models.ListMediaWorkflowExecutionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_media_workflow_executions_with_options(request, runtime)

    async def list_media_workflow_executions_async(
        self,
        request: mts_20140618_models.ListMediaWorkflowExecutionsRequest,
    ) -> mts_20140618_models.ListMediaWorkflowExecutionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_media_workflow_executions_with_options_async(request, runtime)

    def list_porn_pipeline_with_options(
        self,
        request: mts_20140618_models.ListPornPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListPornPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListPornPipelineResponse().from_map(
            self.do_rpcrequest('ListPornPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_porn_pipeline_with_options_async(
        self,
        request: mts_20140618_models.ListPornPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListPornPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListPornPipelineResponse().from_map(
            await self.do_rpcrequest_async('ListPornPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_porn_pipeline(
        self,
        request: mts_20140618_models.ListPornPipelineRequest,
    ) -> mts_20140618_models.ListPornPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_porn_pipeline_with_options(request, runtime)

    async def list_porn_pipeline_async(
        self,
        request: mts_20140618_models.ListPornPipelineRequest,
    ) -> mts_20140618_models.ListPornPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_porn_pipeline_with_options_async(request, runtime)

    def list_terrorism_pipeline_with_options(
        self,
        request: mts_20140618_models.ListTerrorismPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListTerrorismPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListTerrorismPipelineResponse().from_map(
            self.do_rpcrequest('ListTerrorismPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_terrorism_pipeline_with_options_async(
        self,
        request: mts_20140618_models.ListTerrorismPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListTerrorismPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ListTerrorismPipelineResponse().from_map(
            await self.do_rpcrequest_async('ListTerrorismPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_terrorism_pipeline(
        self,
        request: mts_20140618_models.ListTerrorismPipelineRequest,
    ) -> mts_20140618_models.ListTerrorismPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_terrorism_pipeline_with_options(request, runtime)

    async def list_terrorism_pipeline_async(
        self,
        request: mts_20140618_models.ListTerrorismPipelineRequest,
    ) -> mts_20140618_models.ListTerrorismPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_terrorism_pipeline_with_options_async(request, runtime)

    def logical_delete_resource_with_options(
        self,
        request: mts_20140618_models.LogicalDeleteResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.LogicalDeleteResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.LogicalDeleteResourceResponse().from_map(
            self.do_rpcrequest('LogicalDeleteResource', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def logical_delete_resource_with_options_async(
        self,
        request: mts_20140618_models.LogicalDeleteResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.LogicalDeleteResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.LogicalDeleteResourceResponse().from_map(
            await self.do_rpcrequest_async('LogicalDeleteResource', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def logical_delete_resource(
        self,
        request: mts_20140618_models.LogicalDeleteResourceRequest,
    ) -> mts_20140618_models.LogicalDeleteResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.logical_delete_resource_with_options(request, runtime)

    async def logical_delete_resource_async(
        self,
        request: mts_20140618_models.LogicalDeleteResourceRequest,
    ) -> mts_20140618_models.LogicalDeleteResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.logical_delete_resource_with_options_async(request, runtime)

    def physical_delete_resource_with_options(
        self,
        request: mts_20140618_models.PhysicalDeleteResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.PhysicalDeleteResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.PhysicalDeleteResourceResponse().from_map(
            self.do_rpcrequest('PhysicalDeleteResource', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def physical_delete_resource_with_options_async(
        self,
        request: mts_20140618_models.PhysicalDeleteResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.PhysicalDeleteResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.PhysicalDeleteResourceResponse().from_map(
            await self.do_rpcrequest_async('PhysicalDeleteResource', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def physical_delete_resource(
        self,
        request: mts_20140618_models.PhysicalDeleteResourceRequest,
    ) -> mts_20140618_models.PhysicalDeleteResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.physical_delete_resource_with_options(request, runtime)

    async def physical_delete_resource_async(
        self,
        request: mts_20140618_models.PhysicalDeleteResourceRequest,
    ) -> mts_20140618_models.PhysicalDeleteResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.physical_delete_resource_with_options_async(request, runtime)

    def player_auth_with_options(
        self,
        request: mts_20140618_models.PlayerAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.PlayerAuthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.PlayerAuthResponse().from_map(
            self.do_rpcrequest('PlayerAuth', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def player_auth_with_options_async(
        self,
        request: mts_20140618_models.PlayerAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.PlayerAuthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.PlayerAuthResponse().from_map(
            await self.do_rpcrequest_async('PlayerAuth', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def player_auth(
        self,
        request: mts_20140618_models.PlayerAuthRequest,
    ) -> mts_20140618_models.PlayerAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.player_auth_with_options(request, runtime)

    async def player_auth_async(
        self,
        request: mts_20140618_models.PlayerAuthRequest,
    ) -> mts_20140618_models.PlayerAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.player_auth_with_options_async(request, runtime)

    def play_info_with_options(
        self,
        request: mts_20140618_models.PlayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.PlayInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.PlayInfoResponse().from_map(
            self.do_rpcrequest('PlayInfo', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def play_info_with_options_async(
        self,
        request: mts_20140618_models.PlayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.PlayInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.PlayInfoResponse().from_map(
            await self.do_rpcrequest_async('PlayInfo', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def play_info(
        self,
        request: mts_20140618_models.PlayInfoRequest,
    ) -> mts_20140618_models.PlayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.play_info_with_options(request, runtime)

    async def play_info_async(
        self,
        request: mts_20140618_models.PlayInfoRequest,
    ) -> mts_20140618_models.PlayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.play_info_with_options_async(request, runtime)

    def query_analysis_job_list_with_options(
        self,
        request: mts_20140618_models.QueryAnalysisJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAnalysisJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryAnalysisJobListResponse().from_map(
            self.do_rpcrequest('QueryAnalysisJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_analysis_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryAnalysisJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAnalysisJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryAnalysisJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryAnalysisJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_analysis_job_list(
        self,
        request: mts_20140618_models.QueryAnalysisJobListRequest,
    ) -> mts_20140618_models.QueryAnalysisJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_analysis_job_list_with_options(request, runtime)

    async def query_analysis_job_list_async(
        self,
        request: mts_20140618_models.QueryAnalysisJobListRequest,
    ) -> mts_20140618_models.QueryAnalysisJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_analysis_job_list_with_options_async(request, runtime)

    def query_annotation_job_list_with_options(
        self,
        request: mts_20140618_models.QueryAnnotationJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAnnotationJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryAnnotationJobListResponse().from_map(
            self.do_rpcrequest('QueryAnnotationJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_annotation_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryAnnotationJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAnnotationJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryAnnotationJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryAnnotationJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_annotation_job_list(
        self,
        request: mts_20140618_models.QueryAnnotationJobListRequest,
    ) -> mts_20140618_models.QueryAnnotationJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_annotation_job_list_with_options(request, runtime)

    async def query_annotation_job_list_async(
        self,
        request: mts_20140618_models.QueryAnnotationJobListRequest,
    ) -> mts_20140618_models.QueryAnnotationJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_annotation_job_list_with_options_async(request, runtime)

    def query_asr_job_list_with_options(
        self,
        request: mts_20140618_models.QueryAsrJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAsrJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryAsrJobListResponse().from_map(
            self.do_rpcrequest('QueryAsrJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_asr_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryAsrJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAsrJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryAsrJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryAsrJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_asr_job_list(
        self,
        request: mts_20140618_models.QueryAsrJobListRequest,
    ) -> mts_20140618_models.QueryAsrJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_asr_job_list_with_options(request, runtime)

    async def query_asr_job_list_async(
        self,
        request: mts_20140618_models.QueryAsrJobListRequest,
    ) -> mts_20140618_models.QueryAsrJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_asr_job_list_with_options_async(request, runtime)

    def query_asr_pipeline_list_with_options(
        self,
        request: mts_20140618_models.QueryAsrPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAsrPipelineListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryAsrPipelineListResponse().from_map(
            self.do_rpcrequest('QueryAsrPipelineList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_asr_pipeline_list_with_options_async(
        self,
        request: mts_20140618_models.QueryAsrPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAsrPipelineListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryAsrPipelineListResponse().from_map(
            await self.do_rpcrequest_async('QueryAsrPipelineList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_asr_pipeline_list(
        self,
        request: mts_20140618_models.QueryAsrPipelineListRequest,
    ) -> mts_20140618_models.QueryAsrPipelineListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_asr_pipeline_list_with_options(request, runtime)

    async def query_asr_pipeline_list_async(
        self,
        request: mts_20140618_models.QueryAsrPipelineListRequest,
    ) -> mts_20140618_models.QueryAsrPipelineListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_asr_pipeline_list_with_options_async(request, runtime)

    def query_auth_config_with_options(
        self,
        request: mts_20140618_models.QueryAuthConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAuthConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryAuthConfigResponse().from_map(
            self.do_rpcrequest('QueryAuthConfig', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_auth_config_with_options_async(
        self,
        request: mts_20140618_models.QueryAuthConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAuthConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryAuthConfigResponse().from_map(
            await self.do_rpcrequest_async('QueryAuthConfig', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_auth_config(
        self,
        request: mts_20140618_models.QueryAuthConfigRequest,
    ) -> mts_20140618_models.QueryAuthConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_auth_config_with_options(request, runtime)

    async def query_auth_config_async(
        self,
        request: mts_20140618_models.QueryAuthConfigRequest,
    ) -> mts_20140618_models.QueryAuthConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_auth_config_with_options_async(request, runtime)

    def query_censor_job_list_with_options(
        self,
        request: mts_20140618_models.QueryCensorJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryCensorJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryCensorJobListResponse().from_map(
            self.do_rpcrequest('QueryCensorJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_censor_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryCensorJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryCensorJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryCensorJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryCensorJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_censor_job_list(
        self,
        request: mts_20140618_models.QueryCensorJobListRequest,
    ) -> mts_20140618_models.QueryCensorJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_censor_job_list_with_options(request, runtime)

    async def query_censor_job_list_async(
        self,
        request: mts_20140618_models.QueryCensorJobListRequest,
    ) -> mts_20140618_models.QueryCensorJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_censor_job_list_with_options_async(request, runtime)

    def query_censor_pipeline_list_with_options(
        self,
        request: mts_20140618_models.QueryCensorPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryCensorPipelineListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryCensorPipelineListResponse().from_map(
            self.do_rpcrequest('QueryCensorPipelineList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_censor_pipeline_list_with_options_async(
        self,
        request: mts_20140618_models.QueryCensorPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryCensorPipelineListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryCensorPipelineListResponse().from_map(
            await self.do_rpcrequest_async('QueryCensorPipelineList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_censor_pipeline_list(
        self,
        request: mts_20140618_models.QueryCensorPipelineListRequest,
    ) -> mts_20140618_models.QueryCensorPipelineListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_censor_pipeline_list_with_options(request, runtime)

    async def query_censor_pipeline_list_async(
        self,
        request: mts_20140618_models.QueryCensorPipelineListRequest,
    ) -> mts_20140618_models.QueryCensorPipelineListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_censor_pipeline_list_with_options_async(request, runtime)

    def query_complex_job_list_with_options(
        self,
        request: mts_20140618_models.QueryComplexJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryComplexJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryComplexJobListResponse().from_map(
            self.do_rpcrequest('QueryComplexJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_complex_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryComplexJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryComplexJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryComplexJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryComplexJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_complex_job_list(
        self,
        request: mts_20140618_models.QueryComplexJobListRequest,
    ) -> mts_20140618_models.QueryComplexJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_complex_job_list_with_options(request, runtime)

    async def query_complex_job_list_async(
        self,
        request: mts_20140618_models.QueryComplexJobListRequest,
    ) -> mts_20140618_models.QueryComplexJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_complex_job_list_with_options_async(request, runtime)

    def query_cover_job_list_with_options(
        self,
        request: mts_20140618_models.QueryCoverJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryCoverJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryCoverJobListResponse().from_map(
            self.do_rpcrequest('QueryCoverJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_cover_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryCoverJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryCoverJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryCoverJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryCoverJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_cover_job_list(
        self,
        request: mts_20140618_models.QueryCoverJobListRequest,
    ) -> mts_20140618_models.QueryCoverJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_cover_job_list_with_options(request, runtime)

    async def query_cover_job_list_async(
        self,
        request: mts_20140618_models.QueryCoverJobListRequest,
    ) -> mts_20140618_models.QueryCoverJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_cover_job_list_with_options_async(request, runtime)

    def query_cover_pipeline_list_with_options(
        self,
        request: mts_20140618_models.QueryCoverPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryCoverPipelineListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryCoverPipelineListResponse().from_map(
            self.do_rpcrequest('QueryCoverPipelineList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_cover_pipeline_list_with_options_async(
        self,
        request: mts_20140618_models.QueryCoverPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryCoverPipelineListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryCoverPipelineListResponse().from_map(
            await self.do_rpcrequest_async('QueryCoverPipelineList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_cover_pipeline_list(
        self,
        request: mts_20140618_models.QueryCoverPipelineListRequest,
    ) -> mts_20140618_models.QueryCoverPipelineListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_cover_pipeline_list_with_options(request, runtime)

    async def query_cover_pipeline_list_async(
        self,
        request: mts_20140618_models.QueryCoverPipelineListRequest,
    ) -> mts_20140618_models.QueryCoverPipelineListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_cover_pipeline_list_with_options_async(request, runtime)

    def query_editing_job_list_with_options(
        self,
        request: mts_20140618_models.QueryEditingJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryEditingJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryEditingJobListResponse().from_map(
            self.do_rpcrequest('QueryEditingJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_editing_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryEditingJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryEditingJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryEditingJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryEditingJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_editing_job_list(
        self,
        request: mts_20140618_models.QueryEditingJobListRequest,
    ) -> mts_20140618_models.QueryEditingJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_editing_job_list_with_options(request, runtime)

    async def query_editing_job_list_async(
        self,
        request: mts_20140618_models.QueryEditingJobListRequest,
    ) -> mts_20140618_models.QueryEditingJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_editing_job_list_with_options_async(request, runtime)

    def query_facerecog_job_list_with_options(
        self,
        request: mts_20140618_models.QueryFacerecogJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFacerecogJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryFacerecogJobListResponse().from_map(
            self.do_rpcrequest('QueryFacerecogJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_facerecog_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryFacerecogJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFacerecogJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryFacerecogJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryFacerecogJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_facerecog_job_list(
        self,
        request: mts_20140618_models.QueryFacerecogJobListRequest,
    ) -> mts_20140618_models.QueryFacerecogJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_facerecog_job_list_with_options(request, runtime)

    async def query_facerecog_job_list_async(
        self,
        request: mts_20140618_models.QueryFacerecogJobListRequest,
    ) -> mts_20140618_models.QueryFacerecogJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_facerecog_job_list_with_options_async(request, runtime)

    def query_fp_compare_job_list_with_options(
        self,
        request: mts_20140618_models.QueryFpCompareJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpCompareJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryFpCompareJobListResponse().from_map(
            self.do_rpcrequest('QueryFpCompareJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_fp_compare_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryFpCompareJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpCompareJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryFpCompareJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryFpCompareJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_fp_compare_job_list(
        self,
        request: mts_20140618_models.QueryFpCompareJobListRequest,
    ) -> mts_20140618_models.QueryFpCompareJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_fp_compare_job_list_with_options(request, runtime)

    async def query_fp_compare_job_list_async(
        self,
        request: mts_20140618_models.QueryFpCompareJobListRequest,
    ) -> mts_20140618_models.QueryFpCompareJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_fp_compare_job_list_with_options_async(request, runtime)

    def query_fp_dbdelete_job_list_with_options(
        self,
        request: mts_20140618_models.QueryFpDBDeleteJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpDBDeleteJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryFpDBDeleteJobListResponse().from_map(
            self.do_rpcrequest('QueryFpDBDeleteJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_fp_dbdelete_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryFpDBDeleteJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpDBDeleteJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryFpDBDeleteJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryFpDBDeleteJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_fp_dbdelete_job_list(
        self,
        request: mts_20140618_models.QueryFpDBDeleteJobListRequest,
    ) -> mts_20140618_models.QueryFpDBDeleteJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_fp_dbdelete_job_list_with_options(request, runtime)

    async def query_fp_dbdelete_job_list_async(
        self,
        request: mts_20140618_models.QueryFpDBDeleteJobListRequest,
    ) -> mts_20140618_models.QueryFpDBDeleteJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_fp_dbdelete_job_list_with_options_async(request, runtime)

    def query_fp_file_delete_job_list_with_options(
        self,
        request: mts_20140618_models.QueryFpFileDeleteJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpFileDeleteJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryFpFileDeleteJobListResponse().from_map(
            self.do_rpcrequest('QueryFpFileDeleteJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_fp_file_delete_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryFpFileDeleteJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpFileDeleteJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryFpFileDeleteJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryFpFileDeleteJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_fp_file_delete_job_list(
        self,
        request: mts_20140618_models.QueryFpFileDeleteJobListRequest,
    ) -> mts_20140618_models.QueryFpFileDeleteJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_fp_file_delete_job_list_with_options(request, runtime)

    async def query_fp_file_delete_job_list_async(
        self,
        request: mts_20140618_models.QueryFpFileDeleteJobListRequest,
    ) -> mts_20140618_models.QueryFpFileDeleteJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_fp_file_delete_job_list_with_options_async(request, runtime)

    def query_fp_import_result_with_options(
        self,
        request: mts_20140618_models.QueryFpImportResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpImportResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryFpImportResultResponse().from_map(
            self.do_rpcrequest('QueryFpImportResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_fp_import_result_with_options_async(
        self,
        request: mts_20140618_models.QueryFpImportResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpImportResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryFpImportResultResponse().from_map(
            await self.do_rpcrequest_async('QueryFpImportResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_fp_import_result(
        self,
        request: mts_20140618_models.QueryFpImportResultRequest,
    ) -> mts_20140618_models.QueryFpImportResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_fp_import_result_with_options(request, runtime)

    async def query_fp_import_result_async(
        self,
        request: mts_20140618_models.QueryFpImportResultRequest,
    ) -> mts_20140618_models.QueryFpImportResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_fp_import_result_with_options_async(request, runtime)

    def query_fp_shot_job_list_with_options(
        self,
        request: mts_20140618_models.QueryFpShotJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpShotJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryFpShotJobListResponse().from_map(
            self.do_rpcrequest('QueryFpShotJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_fp_shot_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryFpShotJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpShotJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryFpShotJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryFpShotJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_fp_shot_job_list(
        self,
        request: mts_20140618_models.QueryFpShotJobListRequest,
    ) -> mts_20140618_models.QueryFpShotJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_fp_shot_job_list_with_options(request, runtime)

    async def query_fp_shot_job_list_async(
        self,
        request: mts_20140618_models.QueryFpShotJobListRequest,
    ) -> mts_20140618_models.QueryFpShotJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_fp_shot_job_list_with_options_async(request, runtime)

    def query_image_search_job_list_with_options(
        self,
        request: mts_20140618_models.QueryImageSearchJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryImageSearchJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryImageSearchJobListResponse().from_map(
            self.do_rpcrequest('QueryImageSearchJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_image_search_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryImageSearchJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryImageSearchJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryImageSearchJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryImageSearchJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_image_search_job_list(
        self,
        request: mts_20140618_models.QueryImageSearchJobListRequest,
    ) -> mts_20140618_models.QueryImageSearchJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_image_search_job_list_with_options(request, runtime)

    async def query_image_search_job_list_async(
        self,
        request: mts_20140618_models.QueryImageSearchJobListRequest,
    ) -> mts_20140618_models.QueryImageSearchJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_image_search_job_list_with_options_async(request, runtime)

    def query_inner_job_with_options(
        self,
        request: mts_20140618_models.QueryInnerJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryInnerJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryInnerJobResponse().from_map(
            self.do_rpcrequest('QueryInnerJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_inner_job_with_options_async(
        self,
        request: mts_20140618_models.QueryInnerJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryInnerJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryInnerJobResponse().from_map(
            await self.do_rpcrequest_async('QueryInnerJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_inner_job(
        self,
        request: mts_20140618_models.QueryInnerJobRequest,
    ) -> mts_20140618_models.QueryInnerJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_inner_job_with_options(request, runtime)

    async def query_inner_job_async(
        self,
        request: mts_20140618_models.QueryInnerJobRequest,
    ) -> mts_20140618_models.QueryInnerJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_inner_job_with_options_async(request, runtime)

    def query_iproduction_job_with_options(
        self,
        request: mts_20140618_models.QueryIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryIProductionJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryIProductionJobResponse().from_map(
            self.do_rpcrequest('QueryIProductionJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_iproduction_job_with_options_async(
        self,
        request: mts_20140618_models.QueryIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryIProductionJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryIProductionJobResponse().from_map(
            await self.do_rpcrequest_async('QueryIProductionJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_iproduction_job(
        self,
        request: mts_20140618_models.QueryIProductionJobRequest,
    ) -> mts_20140618_models.QueryIProductionJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_iproduction_job_with_options(request, runtime)

    async def query_iproduction_job_async(
        self,
        request: mts_20140618_models.QueryIProductionJobRequest,
    ) -> mts_20140618_models.QueryIProductionJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_iproduction_job_with_options_async(request, runtime)

    def query_iproduction_job_list_with_options(
        self,
        request: mts_20140618_models.QueryIProductionJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryIProductionJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryIProductionJobListResponse().from_map(
            self.do_rpcrequest('QueryIProductionJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_iproduction_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryIProductionJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryIProductionJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryIProductionJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryIProductionJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_iproduction_job_list(
        self,
        request: mts_20140618_models.QueryIProductionJobListRequest,
    ) -> mts_20140618_models.QueryIProductionJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_iproduction_job_list_with_options(request, runtime)

    async def query_iproduction_job_list_async(
        self,
        request: mts_20140618_models.QueryIProductionJobListRequest,
    ) -> mts_20140618_models.QueryIProductionJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_iproduction_job_list_with_options_async(request, runtime)

    def query_job_list_with_options(
        self,
        request: mts_20140618_models.QueryJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryJobListResponse().from_map(
            self.do_rpcrequest('QueryJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_job_list(
        self,
        request: mts_20140618_models.QueryJobListRequest,
    ) -> mts_20140618_models.QueryJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_job_list_with_options(request, runtime)

    async def query_job_list_async(
        self,
        request: mts_20140618_models.QueryJobListRequest,
    ) -> mts_20140618_models.QueryJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_job_list_with_options_async(request, runtime)

    def query_mcjob_list_with_options(
        self,
        request: mts_20140618_models.QueryMCJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMCJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMCJobListResponse().from_map(
            self.do_rpcrequest('QueryMCJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_mcjob_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMCJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMCJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMCJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryMCJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_mcjob_list(
        self,
        request: mts_20140618_models.QueryMCJobListRequest,
    ) -> mts_20140618_models.QueryMCJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_mcjob_list_with_options(request, runtime)

    async def query_mcjob_list_async(
        self,
        request: mts_20140618_models.QueryMCJobListRequest,
    ) -> mts_20140618_models.QueryMCJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_mcjob_list_with_options_async(request, runtime)

    def query_mctemplate_list_with_options(
        self,
        request: mts_20140618_models.QueryMCTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMCTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMCTemplateListResponse().from_map(
            self.do_rpcrequest('QueryMCTemplateList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_mctemplate_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMCTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMCTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMCTemplateListResponse().from_map(
            await self.do_rpcrequest_async('QueryMCTemplateList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_mctemplate_list(
        self,
        request: mts_20140618_models.QueryMCTemplateListRequest,
    ) -> mts_20140618_models.QueryMCTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_mctemplate_list_with_options(request, runtime)

    async def query_mctemplate_list_async(
        self,
        request: mts_20140618_models.QueryMCTemplateListRequest,
    ) -> mts_20140618_models.QueryMCTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_mctemplate_list_with_options_async(request, runtime)

    def query_mcu_job_with_options(
        self,
        request: mts_20140618_models.QueryMcuJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMcuJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMcuJobResponse().from_map(
            self.do_rpcrequest('QueryMcuJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_mcu_job_with_options_async(
        self,
        request: mts_20140618_models.QueryMcuJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMcuJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMcuJobResponse().from_map(
            await self.do_rpcrequest_async('QueryMcuJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_mcu_job(
        self,
        request: mts_20140618_models.QueryMcuJobRequest,
    ) -> mts_20140618_models.QueryMcuJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_mcu_job_with_options(request, runtime)

    async def query_mcu_job_async(
        self,
        request: mts_20140618_models.QueryMcuJobRequest,
    ) -> mts_20140618_models.QueryMcuJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_mcu_job_with_options_async(request, runtime)

    def query_mcu_template_with_options(
        self,
        request: mts_20140618_models.QueryMcuTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMcuTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMcuTemplateResponse().from_map(
            self.do_rpcrequest('QueryMcuTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_mcu_template_with_options_async(
        self,
        request: mts_20140618_models.QueryMcuTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMcuTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMcuTemplateResponse().from_map(
            await self.do_rpcrequest_async('QueryMcuTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_mcu_template(
        self,
        request: mts_20140618_models.QueryMcuTemplateRequest,
    ) -> mts_20140618_models.QueryMcuTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_mcu_template_with_options(request, runtime)

    async def query_mcu_template_async(
        self,
        request: mts_20140618_models.QueryMcuTemplateRequest,
    ) -> mts_20140618_models.QueryMcuTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_mcu_template_with_options_async(request, runtime)

    def query_media_censor_job_detail_with_options(
        self,
        request: mts_20140618_models.QueryMediaCensorJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaCensorJobDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaCensorJobDetailResponse().from_map(
            self.do_rpcrequest('QueryMediaCensorJobDetail', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_media_censor_job_detail_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaCensorJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaCensorJobDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaCensorJobDetailResponse().from_map(
            await self.do_rpcrequest_async('QueryMediaCensorJobDetail', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_media_censor_job_detail(
        self,
        request: mts_20140618_models.QueryMediaCensorJobDetailRequest,
    ) -> mts_20140618_models.QueryMediaCensorJobDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_media_censor_job_detail_with_options(request, runtime)

    async def query_media_censor_job_detail_async(
        self,
        request: mts_20140618_models.QueryMediaCensorJobDetailRequest,
    ) -> mts_20140618_models.QueryMediaCensorJobDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_media_censor_job_detail_with_options_async(request, runtime)

    def query_media_censor_job_list_with_options(
        self,
        request: mts_20140618_models.QueryMediaCensorJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaCensorJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaCensorJobListResponse().from_map(
            self.do_rpcrequest('QueryMediaCensorJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_media_censor_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaCensorJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaCensorJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaCensorJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryMediaCensorJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_media_censor_job_list(
        self,
        request: mts_20140618_models.QueryMediaCensorJobListRequest,
    ) -> mts_20140618_models.QueryMediaCensorJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_media_censor_job_list_with_options(request, runtime)

    async def query_media_censor_job_list_async(
        self,
        request: mts_20140618_models.QueryMediaCensorJobListRequest,
    ) -> mts_20140618_models.QueryMediaCensorJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_media_censor_job_list_with_options_async(request, runtime)

    def query_media_detail_job_list_with_options(
        self,
        request: mts_20140618_models.QueryMediaDetailJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaDetailJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaDetailJobListResponse().from_map(
            self.do_rpcrequest('QueryMediaDetailJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_media_detail_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaDetailJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaDetailJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaDetailJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryMediaDetailJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_media_detail_job_list(
        self,
        request: mts_20140618_models.QueryMediaDetailJobListRequest,
    ) -> mts_20140618_models.QueryMediaDetailJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_media_detail_job_list_with_options(request, runtime)

    async def query_media_detail_job_list_async(
        self,
        request: mts_20140618_models.QueryMediaDetailJobListRequest,
    ) -> mts_20140618_models.QueryMediaDetailJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_media_detail_job_list_with_options_async(request, runtime)

    def query_media_fp_delete_job_list_with_options(
        self,
        request: mts_20140618_models.QueryMediaFpDeleteJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaFpDeleteJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaFpDeleteJobListResponse().from_map(
            self.do_rpcrequest('QueryMediaFpDeleteJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_media_fp_delete_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaFpDeleteJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaFpDeleteJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaFpDeleteJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryMediaFpDeleteJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_media_fp_delete_job_list(
        self,
        request: mts_20140618_models.QueryMediaFpDeleteJobListRequest,
    ) -> mts_20140618_models.QueryMediaFpDeleteJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_media_fp_delete_job_list_with_options(request, runtime)

    async def query_media_fp_delete_job_list_async(
        self,
        request: mts_20140618_models.QueryMediaFpDeleteJobListRequest,
    ) -> mts_20140618_models.QueryMediaFpDeleteJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_media_fp_delete_job_list_with_options_async(request, runtime)

    def query_media_info_job_list_with_options(
        self,
        request: mts_20140618_models.QueryMediaInfoJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaInfoJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaInfoJobListResponse().from_map(
            self.do_rpcrequest('QueryMediaInfoJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_media_info_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaInfoJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaInfoJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaInfoJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryMediaInfoJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_media_info_job_list(
        self,
        request: mts_20140618_models.QueryMediaInfoJobListRequest,
    ) -> mts_20140618_models.QueryMediaInfoJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_media_info_job_list_with_options(request, runtime)

    async def query_media_info_job_list_async(
        self,
        request: mts_20140618_models.QueryMediaInfoJobListRequest,
    ) -> mts_20140618_models.QueryMediaInfoJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_media_info_job_list_with_options_async(request, runtime)

    def query_media_list_with_options(
        self,
        request: mts_20140618_models.QueryMediaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaListResponse().from_map(
            self.do_rpcrequest('QueryMediaList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_media_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaListResponse().from_map(
            await self.do_rpcrequest_async('QueryMediaList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_media_list(
        self,
        request: mts_20140618_models.QueryMediaListRequest,
    ) -> mts_20140618_models.QueryMediaListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_media_list_with_options(request, runtime)

    async def query_media_list_async(
        self,
        request: mts_20140618_models.QueryMediaListRequest,
    ) -> mts_20140618_models.QueryMediaListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_media_list_with_options_async(request, runtime)

    def query_media_list_by_urlwith_options(
        self,
        request: mts_20140618_models.QueryMediaListByURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaListByURLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaListByURLResponse().from_map(
            self.do_rpcrequest('QueryMediaListByURL', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_media_list_by_urlwith_options_async(
        self,
        request: mts_20140618_models.QueryMediaListByURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaListByURLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaListByURLResponse().from_map(
            await self.do_rpcrequest_async('QueryMediaListByURL', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_media_list_by_url(
        self,
        request: mts_20140618_models.QueryMediaListByURLRequest,
    ) -> mts_20140618_models.QueryMediaListByURLResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_media_list_by_urlwith_options(request, runtime)

    async def query_media_list_by_url_async(
        self,
        request: mts_20140618_models.QueryMediaListByURLRequest,
    ) -> mts_20140618_models.QueryMediaListByURLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_media_list_by_urlwith_options_async(request, runtime)

    def query_media_workflow_execution_list_with_options(
        self,
        request: mts_20140618_models.QueryMediaWorkflowExecutionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaWorkflowExecutionListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaWorkflowExecutionListResponse().from_map(
            self.do_rpcrequest('QueryMediaWorkflowExecutionList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_media_workflow_execution_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaWorkflowExecutionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaWorkflowExecutionListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaWorkflowExecutionListResponse().from_map(
            await self.do_rpcrequest_async('QueryMediaWorkflowExecutionList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_media_workflow_execution_list(
        self,
        request: mts_20140618_models.QueryMediaWorkflowExecutionListRequest,
    ) -> mts_20140618_models.QueryMediaWorkflowExecutionListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_media_workflow_execution_list_with_options(request, runtime)

    async def query_media_workflow_execution_list_async(
        self,
        request: mts_20140618_models.QueryMediaWorkflowExecutionListRequest,
    ) -> mts_20140618_models.QueryMediaWorkflowExecutionListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_media_workflow_execution_list_with_options_async(request, runtime)

    def query_media_workflow_list_with_options(
        self,
        request: mts_20140618_models.QueryMediaWorkflowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaWorkflowListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaWorkflowListResponse().from_map(
            self.do_rpcrequest('QueryMediaWorkflowList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_media_workflow_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaWorkflowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaWorkflowListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryMediaWorkflowListResponse().from_map(
            await self.do_rpcrequest_async('QueryMediaWorkflowList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_media_workflow_list(
        self,
        request: mts_20140618_models.QueryMediaWorkflowListRequest,
    ) -> mts_20140618_models.QueryMediaWorkflowListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_media_workflow_list_with_options(request, runtime)

    async def query_media_workflow_list_async(
        self,
        request: mts_20140618_models.QueryMediaWorkflowListRequest,
    ) -> mts_20140618_models.QueryMediaWorkflowListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_media_workflow_list_with_options_async(request, runtime)

    def query_pipeline_list_with_options(
        self,
        request: mts_20140618_models.QueryPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryPipelineListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryPipelineListResponse().from_map(
            self.do_rpcrequest('QueryPipelineList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_pipeline_list_with_options_async(
        self,
        request: mts_20140618_models.QueryPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryPipelineListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryPipelineListResponse().from_map(
            await self.do_rpcrequest_async('QueryPipelineList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_pipeline_list(
        self,
        request: mts_20140618_models.QueryPipelineListRequest,
    ) -> mts_20140618_models.QueryPipelineListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_pipeline_list_with_options(request, runtime)

    async def query_pipeline_list_async(
        self,
        request: mts_20140618_models.QueryPipelineListRequest,
    ) -> mts_20140618_models.QueryPipelineListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_pipeline_list_with_options_async(request, runtime)

    def query_porn_job_list_with_options(
        self,
        request: mts_20140618_models.QueryPornJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryPornJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryPornJobListResponse().from_map(
            self.do_rpcrequest('QueryPornJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_porn_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryPornJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryPornJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryPornJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryPornJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_porn_job_list(
        self,
        request: mts_20140618_models.QueryPornJobListRequest,
    ) -> mts_20140618_models.QueryPornJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_porn_job_list_with_options(request, runtime)

    async def query_porn_job_list_async(
        self,
        request: mts_20140618_models.QueryPornJobListRequest,
    ) -> mts_20140618_models.QueryPornJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_porn_job_list_with_options_async(request, runtime)

    def query_porn_pipeline_list_with_options(
        self,
        request: mts_20140618_models.QueryPornPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryPornPipelineListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryPornPipelineListResponse().from_map(
            self.do_rpcrequest('QueryPornPipelineList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_porn_pipeline_list_with_options_async(
        self,
        request: mts_20140618_models.QueryPornPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryPornPipelineListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryPornPipelineListResponse().from_map(
            await self.do_rpcrequest_async('QueryPornPipelineList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_porn_pipeline_list(
        self,
        request: mts_20140618_models.QueryPornPipelineListRequest,
    ) -> mts_20140618_models.QueryPornPipelineListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_porn_pipeline_list_with_options(request, runtime)

    async def query_porn_pipeline_list_async(
        self,
        request: mts_20140618_models.QueryPornPipelineListRequest,
    ) -> mts_20140618_models.QueryPornPipelineListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_porn_pipeline_list_with_options_async(request, runtime)

    def query_smarttag_job_with_options(
        self,
        request: mts_20140618_models.QuerySmarttagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySmarttagJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QuerySmarttagJobResponse().from_map(
            self.do_rpcrequest('QuerySmarttagJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_smarttag_job_with_options_async(
        self,
        request: mts_20140618_models.QuerySmarttagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySmarttagJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QuerySmarttagJobResponse().from_map(
            await self.do_rpcrequest_async('QuerySmarttagJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_smarttag_job(
        self,
        request: mts_20140618_models.QuerySmarttagJobRequest,
    ) -> mts_20140618_models.QuerySmarttagJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_smarttag_job_with_options(request, runtime)

    async def query_smarttag_job_async(
        self,
        request: mts_20140618_models.QuerySmarttagJobRequest,
    ) -> mts_20140618_models.QuerySmarttagJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_smarttag_job_with_options_async(request, runtime)

    def query_smarttag_template_list_with_options(
        self,
        request: mts_20140618_models.QuerySmarttagTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySmarttagTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QuerySmarttagTemplateListResponse().from_map(
            self.do_rpcrequest('QuerySmarttagTemplateList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_smarttag_template_list_with_options_async(
        self,
        request: mts_20140618_models.QuerySmarttagTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySmarttagTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QuerySmarttagTemplateListResponse().from_map(
            await self.do_rpcrequest_async('QuerySmarttagTemplateList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_smarttag_template_list(
        self,
        request: mts_20140618_models.QuerySmarttagTemplateListRequest,
    ) -> mts_20140618_models.QuerySmarttagTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_smarttag_template_list_with_options(request, runtime)

    async def query_smarttag_template_list_async(
        self,
        request: mts_20140618_models.QuerySmarttagTemplateListRequest,
    ) -> mts_20140618_models.QuerySmarttagTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_smarttag_template_list_with_options_async(request, runtime)

    def query_snapshot_job_list_with_options(
        self,
        request: mts_20140618_models.QuerySnapshotJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySnapshotJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QuerySnapshotJobListResponse().from_map(
            self.do_rpcrequest('QuerySnapshotJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_snapshot_job_list_with_options_async(
        self,
        request: mts_20140618_models.QuerySnapshotJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySnapshotJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QuerySnapshotJobListResponse().from_map(
            await self.do_rpcrequest_async('QuerySnapshotJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_snapshot_job_list(
        self,
        request: mts_20140618_models.QuerySnapshotJobListRequest,
    ) -> mts_20140618_models.QuerySnapshotJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_snapshot_job_list_with_options(request, runtime)

    async def query_snapshot_job_list_async(
        self,
        request: mts_20140618_models.QuerySnapshotJobListRequest,
    ) -> mts_20140618_models.QuerySnapshotJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_snapshot_job_list_with_options_async(request, runtime)

    def query_subtitle_job_list_with_options(
        self,
        request: mts_20140618_models.QuerySubtitleJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySubtitleJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QuerySubtitleJobListResponse().from_map(
            self.do_rpcrequest('QuerySubtitleJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_subtitle_job_list_with_options_async(
        self,
        request: mts_20140618_models.QuerySubtitleJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySubtitleJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QuerySubtitleJobListResponse().from_map(
            await self.do_rpcrequest_async('QuerySubtitleJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_subtitle_job_list(
        self,
        request: mts_20140618_models.QuerySubtitleJobListRequest,
    ) -> mts_20140618_models.QuerySubtitleJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_subtitle_job_list_with_options(request, runtime)

    async def query_subtitle_job_list_async(
        self,
        request: mts_20140618_models.QuerySubtitleJobListRequest,
    ) -> mts_20140618_models.QuerySubtitleJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_subtitle_job_list_with_options_async(request, runtime)

    def query_tag_job_list_with_options(
        self,
        request: mts_20140618_models.QueryTagJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryTagJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryTagJobListResponse().from_map(
            self.do_rpcrequest('QueryTagJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_tag_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryTagJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryTagJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryTagJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryTagJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_tag_job_list(
        self,
        request: mts_20140618_models.QueryTagJobListRequest,
    ) -> mts_20140618_models.QueryTagJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_tag_job_list_with_options(request, runtime)

    async def query_tag_job_list_async(
        self,
        request: mts_20140618_models.QueryTagJobListRequest,
    ) -> mts_20140618_models.QueryTagJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_tag_job_list_with_options_async(request, runtime)

    def query_template_list_with_options(
        self,
        request: mts_20140618_models.QueryTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryTemplateListResponse().from_map(
            self.do_rpcrequest('QueryTemplateList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_template_list_with_options_async(
        self,
        request: mts_20140618_models.QueryTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryTemplateListResponse().from_map(
            await self.do_rpcrequest_async('QueryTemplateList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_template_list(
        self,
        request: mts_20140618_models.QueryTemplateListRequest,
    ) -> mts_20140618_models.QueryTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_template_list_with_options(request, runtime)

    async def query_template_list_async(
        self,
        request: mts_20140618_models.QueryTemplateListRequest,
    ) -> mts_20140618_models.QueryTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_template_list_with_options_async(request, runtime)

    def query_terrorism_job_list_with_options(
        self,
        request: mts_20140618_models.QueryTerrorismJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryTerrorismJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryTerrorismJobListResponse().from_map(
            self.do_rpcrequest('QueryTerrorismJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_terrorism_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryTerrorismJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryTerrorismJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryTerrorismJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryTerrorismJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_terrorism_job_list(
        self,
        request: mts_20140618_models.QueryTerrorismJobListRequest,
    ) -> mts_20140618_models.QueryTerrorismJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_terrorism_job_list_with_options(request, runtime)

    async def query_terrorism_job_list_async(
        self,
        request: mts_20140618_models.QueryTerrorismJobListRequest,
    ) -> mts_20140618_models.QueryTerrorismJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_terrorism_job_list_with_options_async(request, runtime)

    def query_terrorism_pipeline_list_with_options(
        self,
        request: mts_20140618_models.QueryTerrorismPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryTerrorismPipelineListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryTerrorismPipelineListResponse().from_map(
            self.do_rpcrequest('QueryTerrorismPipelineList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_terrorism_pipeline_list_with_options_async(
        self,
        request: mts_20140618_models.QueryTerrorismPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryTerrorismPipelineListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryTerrorismPipelineListResponse().from_map(
            await self.do_rpcrequest_async('QueryTerrorismPipelineList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_terrorism_pipeline_list(
        self,
        request: mts_20140618_models.QueryTerrorismPipelineListRequest,
    ) -> mts_20140618_models.QueryTerrorismPipelineListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_terrorism_pipeline_list_with_options(request, runtime)

    async def query_terrorism_pipeline_list_async(
        self,
        request: mts_20140618_models.QueryTerrorismPipelineListRequest,
    ) -> mts_20140618_models.QueryTerrorismPipelineListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_terrorism_pipeline_list_with_options_async(request, runtime)

    def query_video_gif_job_list_with_options(
        self,
        request: mts_20140618_models.QueryVideoGifJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryVideoGifJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryVideoGifJobListResponse().from_map(
            self.do_rpcrequest('QueryVideoGifJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_video_gif_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryVideoGifJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryVideoGifJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryVideoGifJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryVideoGifJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_video_gif_job_list(
        self,
        request: mts_20140618_models.QueryVideoGifJobListRequest,
    ) -> mts_20140618_models.QueryVideoGifJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_video_gif_job_list_with_options(request, runtime)

    async def query_video_gif_job_list_async(
        self,
        request: mts_20140618_models.QueryVideoGifJobListRequest,
    ) -> mts_20140618_models.QueryVideoGifJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_video_gif_job_list_with_options_async(request, runtime)

    def query_video_pose_job_list_with_options(
        self,
        request: mts_20140618_models.QueryVideoPoseJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryVideoPoseJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryVideoPoseJobListResponse().from_map(
            self.do_rpcrequest('QueryVideoPoseJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_video_pose_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryVideoPoseJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryVideoPoseJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryVideoPoseJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryVideoPoseJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_video_pose_job_list(
        self,
        request: mts_20140618_models.QueryVideoPoseJobListRequest,
    ) -> mts_20140618_models.QueryVideoPoseJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_video_pose_job_list_with_options(request, runtime)

    async def query_video_pose_job_list_async(
        self,
        request: mts_20140618_models.QueryVideoPoseJobListRequest,
    ) -> mts_20140618_models.QueryVideoPoseJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_video_pose_job_list_with_options_async(request, runtime)

    def query_video_quality_job_with_options(
        self,
        request: mts_20140618_models.QueryVideoQualityJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryVideoQualityJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryVideoQualityJobResponse().from_map(
            self.do_rpcrequest('QueryVideoQualityJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_video_quality_job_with_options_async(
        self,
        request: mts_20140618_models.QueryVideoQualityJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryVideoQualityJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryVideoQualityJobResponse().from_map(
            await self.do_rpcrequest_async('QueryVideoQualityJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_video_quality_job(
        self,
        request: mts_20140618_models.QueryVideoQualityJobRequest,
    ) -> mts_20140618_models.QueryVideoQualityJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_video_quality_job_with_options(request, runtime)

    async def query_video_quality_job_async(
        self,
        request: mts_20140618_models.QueryVideoQualityJobRequest,
    ) -> mts_20140618_models.QueryVideoQualityJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_video_quality_job_with_options_async(request, runtime)

    def query_video_split_job_list_with_options(
        self,
        request: mts_20140618_models.QueryVideoSplitJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryVideoSplitJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryVideoSplitJobListResponse().from_map(
            self.do_rpcrequest('QueryVideoSplitJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_video_split_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryVideoSplitJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryVideoSplitJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryVideoSplitJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryVideoSplitJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_video_split_job_list(
        self,
        request: mts_20140618_models.QueryVideoSplitJobListRequest,
    ) -> mts_20140618_models.QueryVideoSplitJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_video_split_job_list_with_options(request, runtime)

    async def query_video_split_job_list_async(
        self,
        request: mts_20140618_models.QueryVideoSplitJobListRequest,
    ) -> mts_20140618_models.QueryVideoSplitJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_video_split_job_list_with_options_async(request, runtime)

    def query_video_summary_job_list_with_options(
        self,
        request: mts_20140618_models.QueryVideoSummaryJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryVideoSummaryJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryVideoSummaryJobListResponse().from_map(
            self.do_rpcrequest('QueryVideoSummaryJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_video_summary_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryVideoSummaryJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryVideoSummaryJobListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryVideoSummaryJobListResponse().from_map(
            await self.do_rpcrequest_async('QueryVideoSummaryJobList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_video_summary_job_list(
        self,
        request: mts_20140618_models.QueryVideoSummaryJobListRequest,
    ) -> mts_20140618_models.QueryVideoSummaryJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_video_summary_job_list_with_options(request, runtime)

    async def query_video_summary_job_list_async(
        self,
        request: mts_20140618_models.QueryVideoSummaryJobListRequest,
    ) -> mts_20140618_models.QueryVideoSummaryJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_video_summary_job_list_with_options_async(request, runtime)

    def query_water_mark_template_list_with_options(
        self,
        request: mts_20140618_models.QueryWaterMarkTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryWaterMarkTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryWaterMarkTemplateListResponse().from_map(
            self.do_rpcrequest('QueryWaterMarkTemplateList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_water_mark_template_list_with_options_async(
        self,
        request: mts_20140618_models.QueryWaterMarkTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryWaterMarkTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.QueryWaterMarkTemplateListResponse().from_map(
            await self.do_rpcrequest_async('QueryWaterMarkTemplateList', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_water_mark_template_list(
        self,
        request: mts_20140618_models.QueryWaterMarkTemplateListRequest,
    ) -> mts_20140618_models.QueryWaterMarkTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_water_mark_template_list_with_options(request, runtime)

    async def query_water_mark_template_list_async(
        self,
        request: mts_20140618_models.QueryWaterMarkTemplateListRequest,
    ) -> mts_20140618_models.QueryWaterMarkTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_water_mark_template_list_with_options_async(request, runtime)

    def refresh_cdn_domain_configs_cache_with_options(
        self,
        request: mts_20140618_models.RefreshCdnDomainConfigsCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.RefreshCdnDomainConfigsCacheResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.RefreshCdnDomainConfigsCacheResponse().from_map(
            self.do_rpcrequest('RefreshCdnDomainConfigsCache', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_cdn_domain_configs_cache_with_options_async(
        self,
        request: mts_20140618_models.RefreshCdnDomainConfigsCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.RefreshCdnDomainConfigsCacheResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.RefreshCdnDomainConfigsCacheResponse().from_map(
            await self.do_rpcrequest_async('RefreshCdnDomainConfigsCache', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_cdn_domain_configs_cache(
        self,
        request: mts_20140618_models.RefreshCdnDomainConfigsCacheRequest,
    ) -> mts_20140618_models.RefreshCdnDomainConfigsCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_cdn_domain_configs_cache_with_options(request, runtime)

    async def refresh_cdn_domain_configs_cache_async(
        self,
        request: mts_20140618_models.RefreshCdnDomainConfigsCacheRequest,
    ) -> mts_20140618_models.RefreshCdnDomainConfigsCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_cdn_domain_configs_cache_with_options_async(request, runtime)

    def register_custom_face_with_options(
        self,
        request: mts_20140618_models.RegisterCustomFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.RegisterCustomFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.RegisterCustomFaceResponse().from_map(
            self.do_rpcrequest('RegisterCustomFace', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_custom_face_with_options_async(
        self,
        request: mts_20140618_models.RegisterCustomFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.RegisterCustomFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.RegisterCustomFaceResponse().from_map(
            await self.do_rpcrequest_async('RegisterCustomFace', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_custom_face(
        self,
        request: mts_20140618_models.RegisterCustomFaceRequest,
    ) -> mts_20140618_models.RegisterCustomFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_custom_face_with_options(request, runtime)

    async def register_custom_face_async(
        self,
        request: mts_20140618_models.RegisterCustomFaceRequest,
    ) -> mts_20140618_models.RegisterCustomFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_custom_face_with_options_async(request, runtime)

    def register_media_detail_person_with_options(
        self,
        request: mts_20140618_models.RegisterMediaDetailPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.RegisterMediaDetailPersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.RegisterMediaDetailPersonResponse().from_map(
            self.do_rpcrequest('RegisterMediaDetailPerson', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_media_detail_person_with_options_async(
        self,
        request: mts_20140618_models.RegisterMediaDetailPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.RegisterMediaDetailPersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.RegisterMediaDetailPersonResponse().from_map(
            await self.do_rpcrequest_async('RegisterMediaDetailPerson', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_media_detail_person(
        self,
        request: mts_20140618_models.RegisterMediaDetailPersonRequest,
    ) -> mts_20140618_models.RegisterMediaDetailPersonResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_media_detail_person_with_options(request, runtime)

    async def register_media_detail_person_async(
        self,
        request: mts_20140618_models.RegisterMediaDetailPersonRequest,
    ) -> mts_20140618_models.RegisterMediaDetailPersonResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_media_detail_person_with_options_async(request, runtime)

    def register_media_detail_scenario_with_options(
        self,
        request: mts_20140618_models.RegisterMediaDetailScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.RegisterMediaDetailScenarioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.RegisterMediaDetailScenarioResponse().from_map(
            self.do_rpcrequest('RegisterMediaDetailScenario', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_media_detail_scenario_with_options_async(
        self,
        request: mts_20140618_models.RegisterMediaDetailScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.RegisterMediaDetailScenarioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.RegisterMediaDetailScenarioResponse().from_map(
            await self.do_rpcrequest_async('RegisterMediaDetailScenario', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_media_detail_scenario(
        self,
        request: mts_20140618_models.RegisterMediaDetailScenarioRequest,
    ) -> mts_20140618_models.RegisterMediaDetailScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_media_detail_scenario_with_options(request, runtime)

    async def register_media_detail_scenario_async(
        self,
        request: mts_20140618_models.RegisterMediaDetailScenarioRequest,
    ) -> mts_20140618_models.RegisterMediaDetailScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_media_detail_scenario_with_options_async(request, runtime)

    def report_annotation_job_result_with_options(
        self,
        request: mts_20140618_models.ReportAnnotationJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportAnnotationJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportAnnotationJobResultResponse().from_map(
            self.do_rpcrequest('ReportAnnotationJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def report_annotation_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportAnnotationJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportAnnotationJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportAnnotationJobResultResponse().from_map(
            await self.do_rpcrequest_async('ReportAnnotationJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_annotation_job_result(
        self,
        request: mts_20140618_models.ReportAnnotationJobResultRequest,
    ) -> mts_20140618_models.ReportAnnotationJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_annotation_job_result_with_options(request, runtime)

    async def report_annotation_job_result_async(
        self,
        request: mts_20140618_models.ReportAnnotationJobResultRequest,
    ) -> mts_20140618_models.ReportAnnotationJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_annotation_job_result_with_options_async(request, runtime)

    def report_censor_job_result_with_options(
        self,
        request: mts_20140618_models.ReportCensorJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportCensorJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportCensorJobResultResponse().from_map(
            self.do_rpcrequest('ReportCensorJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def report_censor_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportCensorJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportCensorJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportCensorJobResultResponse().from_map(
            await self.do_rpcrequest_async('ReportCensorJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_censor_job_result(
        self,
        request: mts_20140618_models.ReportCensorJobResultRequest,
    ) -> mts_20140618_models.ReportCensorJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_censor_job_result_with_options(request, runtime)

    async def report_censor_job_result_async(
        self,
        request: mts_20140618_models.ReportCensorJobResultRequest,
    ) -> mts_20140618_models.ReportCensorJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_censor_job_result_with_options_async(request, runtime)

    def report_cover_job_result_with_options(
        self,
        request: mts_20140618_models.ReportCoverJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportCoverJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportCoverJobResultResponse().from_map(
            self.do_rpcrequest('ReportCoverJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def report_cover_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportCoverJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportCoverJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportCoverJobResultResponse().from_map(
            await self.do_rpcrequest_async('ReportCoverJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_cover_job_result(
        self,
        request: mts_20140618_models.ReportCoverJobResultRequest,
    ) -> mts_20140618_models.ReportCoverJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_cover_job_result_with_options(request, runtime)

    async def report_cover_job_result_async(
        self,
        request: mts_20140618_models.ReportCoverJobResultRequest,
    ) -> mts_20140618_models.ReportCoverJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_cover_job_result_with_options_async(request, runtime)

    def report_facerecog_job_result_with_options(
        self,
        request: mts_20140618_models.ReportFacerecogJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportFacerecogJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportFacerecogJobResultResponse().from_map(
            self.do_rpcrequest('ReportFacerecogJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def report_facerecog_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportFacerecogJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportFacerecogJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportFacerecogJobResultResponse().from_map(
            await self.do_rpcrequest_async('ReportFacerecogJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_facerecog_job_result(
        self,
        request: mts_20140618_models.ReportFacerecogJobResultRequest,
    ) -> mts_20140618_models.ReportFacerecogJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_facerecog_job_result_with_options(request, runtime)

    async def report_facerecog_job_result_async(
        self,
        request: mts_20140618_models.ReportFacerecogJobResultRequest,
    ) -> mts_20140618_models.ReportFacerecogJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_facerecog_job_result_with_options_async(request, runtime)

    def report_fp_shot_job_result_with_options(
        self,
        request: mts_20140618_models.ReportFpShotJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportFpShotJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportFpShotJobResultResponse().from_map(
            self.do_rpcrequest('ReportFpShotJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def report_fp_shot_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportFpShotJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportFpShotJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportFpShotJobResultResponse().from_map(
            await self.do_rpcrequest_async('ReportFpShotJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_fp_shot_job_result(
        self,
        request: mts_20140618_models.ReportFpShotJobResultRequest,
    ) -> mts_20140618_models.ReportFpShotJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_fp_shot_job_result_with_options(request, runtime)

    async def report_fp_shot_job_result_async(
        self,
        request: mts_20140618_models.ReportFpShotJobResultRequest,
    ) -> mts_20140618_models.ReportFpShotJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_fp_shot_job_result_with_options_async(request, runtime)

    def report_media_detail_job_result_with_options(
        self,
        request: mts_20140618_models.ReportMediaDetailJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportMediaDetailJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportMediaDetailJobResultResponse().from_map(
            self.do_rpcrequest('ReportMediaDetailJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def report_media_detail_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportMediaDetailJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportMediaDetailJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportMediaDetailJobResultResponse().from_map(
            await self.do_rpcrequest_async('ReportMediaDetailJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_media_detail_job_result(
        self,
        request: mts_20140618_models.ReportMediaDetailJobResultRequest,
    ) -> mts_20140618_models.ReportMediaDetailJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_media_detail_job_result_with_options(request, runtime)

    async def report_media_detail_job_result_async(
        self,
        request: mts_20140618_models.ReportMediaDetailJobResultRequest,
    ) -> mts_20140618_models.ReportMediaDetailJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_media_detail_job_result_with_options_async(request, runtime)

    def report_porn_job_result_with_options(
        self,
        request: mts_20140618_models.ReportPornJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportPornJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportPornJobResultResponse().from_map(
            self.do_rpcrequest('ReportPornJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def report_porn_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportPornJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportPornJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportPornJobResultResponse().from_map(
            await self.do_rpcrequest_async('ReportPornJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_porn_job_result(
        self,
        request: mts_20140618_models.ReportPornJobResultRequest,
    ) -> mts_20140618_models.ReportPornJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_porn_job_result_with_options(request, runtime)

    async def report_porn_job_result_async(
        self,
        request: mts_20140618_models.ReportPornJobResultRequest,
    ) -> mts_20140618_models.ReportPornJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_porn_job_result_with_options_async(request, runtime)

    def report_tag_job_result_with_options(
        self,
        request: mts_20140618_models.ReportTagJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportTagJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportTagJobResultResponse().from_map(
            self.do_rpcrequest('ReportTagJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def report_tag_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportTagJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportTagJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportTagJobResultResponse().from_map(
            await self.do_rpcrequest_async('ReportTagJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_tag_job_result(
        self,
        request: mts_20140618_models.ReportTagJobResultRequest,
    ) -> mts_20140618_models.ReportTagJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_tag_job_result_with_options(request, runtime)

    async def report_tag_job_result_async(
        self,
        request: mts_20140618_models.ReportTagJobResultRequest,
    ) -> mts_20140618_models.ReportTagJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_tag_job_result_with_options_async(request, runtime)

    def report_terrorism_job_result_with_options(
        self,
        request: mts_20140618_models.ReportTerrorismJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportTerrorismJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportTerrorismJobResultResponse().from_map(
            self.do_rpcrequest('ReportTerrorismJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def report_terrorism_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportTerrorismJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportTerrorismJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportTerrorismJobResultResponse().from_map(
            await self.do_rpcrequest_async('ReportTerrorismJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_terrorism_job_result(
        self,
        request: mts_20140618_models.ReportTerrorismJobResultRequest,
    ) -> mts_20140618_models.ReportTerrorismJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_terrorism_job_result_with_options(request, runtime)

    async def report_terrorism_job_result_async(
        self,
        request: mts_20140618_models.ReportTerrorismJobResultRequest,
    ) -> mts_20140618_models.ReportTerrorismJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_terrorism_job_result_with_options_async(request, runtime)

    def report_video_split_job_result_with_options(
        self,
        request: mts_20140618_models.ReportVideoSplitJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportVideoSplitJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportVideoSplitJobResultResponse().from_map(
            self.do_rpcrequest('ReportVideoSplitJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def report_video_split_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportVideoSplitJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportVideoSplitJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.ReportVideoSplitJobResultResponse().from_map(
            await self.do_rpcrequest_async('ReportVideoSplitJobResult', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_video_split_job_result(
        self,
        request: mts_20140618_models.ReportVideoSplitJobResultRequest,
    ) -> mts_20140618_models.ReportVideoSplitJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_video_split_job_result_with_options(request, runtime)

    async def report_video_split_job_result_async(
        self,
        request: mts_20140618_models.ReportVideoSplitJobResultRequest,
    ) -> mts_20140618_models.ReportVideoSplitJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_video_split_job_result_with_options_async(request, runtime)

    def search_media_with_options(
        self,
        request: mts_20140618_models.SearchMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SearchMediaResponse().from_map(
            self.do_rpcrequest('SearchMedia', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_media_with_options_async(
        self,
        request: mts_20140618_models.SearchMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SearchMediaResponse().from_map(
            await self.do_rpcrequest_async('SearchMedia', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_media(
        self,
        request: mts_20140618_models.SearchMediaRequest,
    ) -> mts_20140618_models.SearchMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_media_with_options(request, runtime)

    async def search_media_async(
        self,
        request: mts_20140618_models.SearchMediaRequest,
    ) -> mts_20140618_models.SearchMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_media_with_options_async(request, runtime)

    def search_media_workflow_with_options(
        self,
        request: mts_20140618_models.SearchMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchMediaWorkflowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SearchMediaWorkflowResponse().from_map(
            self.do_rpcrequest('SearchMediaWorkflow', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.SearchMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchMediaWorkflowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SearchMediaWorkflowResponse().from_map(
            await self.do_rpcrequest_async('SearchMediaWorkflow', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_media_workflow(
        self,
        request: mts_20140618_models.SearchMediaWorkflowRequest,
    ) -> mts_20140618_models.SearchMediaWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_media_workflow_with_options(request, runtime)

    async def search_media_workflow_async(
        self,
        request: mts_20140618_models.SearchMediaWorkflowRequest,
    ) -> mts_20140618_models.SearchMediaWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_media_workflow_with_options_async(request, runtime)

    def search_pipeline_with_options(
        self,
        request: mts_20140618_models.SearchPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SearchPipelineResponse().from_map(
            self.do_rpcrequest('SearchPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_pipeline_with_options_async(
        self,
        request: mts_20140618_models.SearchPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SearchPipelineResponse().from_map(
            await self.do_rpcrequest_async('SearchPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_pipeline(
        self,
        request: mts_20140618_models.SearchPipelineRequest,
    ) -> mts_20140618_models.SearchPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_pipeline_with_options(request, runtime)

    async def search_pipeline_async(
        self,
        request: mts_20140618_models.SearchPipelineRequest,
    ) -> mts_20140618_models.SearchPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_pipeline_with_options_async(request, runtime)

    def search_template_with_options(
        self,
        request: mts_20140618_models.SearchTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SearchTemplateResponse().from_map(
            self.do_rpcrequest('SearchTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_template_with_options_async(
        self,
        request: mts_20140618_models.SearchTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SearchTemplateResponse().from_map(
            await self.do_rpcrequest_async('SearchTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_template(
        self,
        request: mts_20140618_models.SearchTemplateRequest,
    ) -> mts_20140618_models.SearchTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_template_with_options(request, runtime)

    async def search_template_async(
        self,
        request: mts_20140618_models.SearchTemplateRequest,
    ) -> mts_20140618_models.SearchTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_template_with_options_async(request, runtime)

    def search_water_mark_template_with_options(
        self,
        request: mts_20140618_models.SearchWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchWaterMarkTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SearchWaterMarkTemplateResponse().from_map(
            self.do_rpcrequest('SearchWaterMarkTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_water_mark_template_with_options_async(
        self,
        request: mts_20140618_models.SearchWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchWaterMarkTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SearchWaterMarkTemplateResponse().from_map(
            await self.do_rpcrequest_async('SearchWaterMarkTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_water_mark_template(
        self,
        request: mts_20140618_models.SearchWaterMarkTemplateRequest,
    ) -> mts_20140618_models.SearchWaterMarkTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_water_mark_template_with_options(request, runtime)

    async def search_water_mark_template_async(
        self,
        request: mts_20140618_models.SearchWaterMarkTemplateRequest,
    ) -> mts_20140618_models.SearchWaterMarkTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_water_mark_template_with_options_async(request, runtime)

    def set_auth_config_with_options(
        self,
        request: mts_20140618_models.SetAuthConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SetAuthConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SetAuthConfigResponse().from_map(
            self.do_rpcrequest('SetAuthConfig', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_auth_config_with_options_async(
        self,
        request: mts_20140618_models.SetAuthConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SetAuthConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SetAuthConfigResponse().from_map(
            await self.do_rpcrequest_async('SetAuthConfig', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_auth_config(
        self,
        request: mts_20140618_models.SetAuthConfigRequest,
    ) -> mts_20140618_models.SetAuthConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_auth_config_with_options(request, runtime)

    async def set_auth_config_async(
        self,
        request: mts_20140618_models.SetAuthConfigRequest,
    ) -> mts_20140618_models.SetAuthConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_auth_config_with_options_async(request, runtime)

    def stop_iproduction_job_with_options(
        self,
        request: mts_20140618_models.StopIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.StopIProductionJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.StopIProductionJobResponse().from_map(
            self.do_rpcrequest('StopIProductionJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_iproduction_job_with_options_async(
        self,
        request: mts_20140618_models.StopIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.StopIProductionJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.StopIProductionJobResponse().from_map(
            await self.do_rpcrequest_async('StopIProductionJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_iproduction_job(
        self,
        request: mts_20140618_models.StopIProductionJobRequest,
    ) -> mts_20140618_models.StopIProductionJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_iproduction_job_with_options(request, runtime)

    async def stop_iproduction_job_async(
        self,
        request: mts_20140618_models.StopIProductionJobRequest,
    ) -> mts_20140618_models.StopIProductionJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_iproduction_job_with_options_async(request, runtime)

    def submit_analysis_job_with_options(
        self,
        request: mts_20140618_models.SubmitAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitAnalysisJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitAnalysisJobResponse().from_map(
            self.do_rpcrequest('SubmitAnalysisJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_analysis_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitAnalysisJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitAnalysisJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitAnalysisJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_analysis_job(
        self,
        request: mts_20140618_models.SubmitAnalysisJobRequest,
    ) -> mts_20140618_models.SubmitAnalysisJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_analysis_job_with_options(request, runtime)

    async def submit_analysis_job_async(
        self,
        request: mts_20140618_models.SubmitAnalysisJobRequest,
    ) -> mts_20140618_models.SubmitAnalysisJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_analysis_job_with_options_async(request, runtime)

    def submit_annotation_job_with_options(
        self,
        request: mts_20140618_models.SubmitAnnotationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitAnnotationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitAnnotationJobResponse().from_map(
            self.do_rpcrequest('SubmitAnnotationJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_annotation_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitAnnotationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitAnnotationJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitAnnotationJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitAnnotationJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_annotation_job(
        self,
        request: mts_20140618_models.SubmitAnnotationJobRequest,
    ) -> mts_20140618_models.SubmitAnnotationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_annotation_job_with_options(request, runtime)

    async def submit_annotation_job_async(
        self,
        request: mts_20140618_models.SubmitAnnotationJobRequest,
    ) -> mts_20140618_models.SubmitAnnotationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_annotation_job_with_options_async(request, runtime)

    def submit_asr_job_with_options(
        self,
        request: mts_20140618_models.SubmitAsrJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitAsrJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitAsrJobResponse().from_map(
            self.do_rpcrequest('SubmitAsrJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_asr_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitAsrJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitAsrJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitAsrJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitAsrJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_asr_job(
        self,
        request: mts_20140618_models.SubmitAsrJobRequest,
    ) -> mts_20140618_models.SubmitAsrJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_asr_job_with_options(request, runtime)

    async def submit_asr_job_async(
        self,
        request: mts_20140618_models.SubmitAsrJobRequest,
    ) -> mts_20140618_models.SubmitAsrJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_asr_job_with_options_async(request, runtime)

    def submit_beautify_jobs_with_options(
        self,
        request: mts_20140618_models.SubmitBeautifyJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitBeautifyJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitBeautifyJobsResponse().from_map(
            self.do_rpcrequest('SubmitBeautifyJobs', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_beautify_jobs_with_options_async(
        self,
        request: mts_20140618_models.SubmitBeautifyJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitBeautifyJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitBeautifyJobsResponse().from_map(
            await self.do_rpcrequest_async('SubmitBeautifyJobs', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_beautify_jobs(
        self,
        request: mts_20140618_models.SubmitBeautifyJobsRequest,
    ) -> mts_20140618_models.SubmitBeautifyJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_beautify_jobs_with_options(request, runtime)

    async def submit_beautify_jobs_async(
        self,
        request: mts_20140618_models.SubmitBeautifyJobsRequest,
    ) -> mts_20140618_models.SubmitBeautifyJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_beautify_jobs_with_options_async(request, runtime)

    def submit_complex_job_with_options(
        self,
        request: mts_20140618_models.SubmitComplexJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitComplexJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitComplexJobResponse().from_map(
            self.do_rpcrequest('SubmitComplexJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_complex_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitComplexJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitComplexJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitComplexJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitComplexJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_complex_job(
        self,
        request: mts_20140618_models.SubmitComplexJobRequest,
    ) -> mts_20140618_models.SubmitComplexJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_complex_job_with_options(request, runtime)

    async def submit_complex_job_async(
        self,
        request: mts_20140618_models.SubmitComplexJobRequest,
    ) -> mts_20140618_models.SubmitComplexJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_complex_job_with_options_async(request, runtime)

    def submit_cover_job_with_options(
        self,
        request: mts_20140618_models.SubmitCoverJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitCoverJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitCoverJobResponse().from_map(
            self.do_rpcrequest('SubmitCoverJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_cover_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitCoverJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitCoverJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitCoverJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitCoverJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_cover_job(
        self,
        request: mts_20140618_models.SubmitCoverJobRequest,
    ) -> mts_20140618_models.SubmitCoverJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_cover_job_with_options(request, runtime)

    async def submit_cover_job_async(
        self,
        request: mts_20140618_models.SubmitCoverJobRequest,
    ) -> mts_20140618_models.SubmitCoverJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_cover_job_with_options_async(request, runtime)

    def submit_editing_jobs_with_options(
        self,
        request: mts_20140618_models.SubmitEditingJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitEditingJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitEditingJobsResponse().from_map(
            self.do_rpcrequest('SubmitEditingJobs', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_editing_jobs_with_options_async(
        self,
        request: mts_20140618_models.SubmitEditingJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitEditingJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitEditingJobsResponse().from_map(
            await self.do_rpcrequest_async('SubmitEditingJobs', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_editing_jobs(
        self,
        request: mts_20140618_models.SubmitEditingJobsRequest,
    ) -> mts_20140618_models.SubmitEditingJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_editing_jobs_with_options(request, runtime)

    async def submit_editing_jobs_async(
        self,
        request: mts_20140618_models.SubmitEditingJobsRequest,
    ) -> mts_20140618_models.SubmitEditingJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_editing_jobs_with_options_async(request, runtime)

    def submit_facerecog_job_with_options(
        self,
        request: mts_20140618_models.SubmitFacerecogJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFacerecogJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitFacerecogJobResponse().from_map(
            self.do_rpcrequest('SubmitFacerecogJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_facerecog_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitFacerecogJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFacerecogJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitFacerecogJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitFacerecogJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_facerecog_job(
        self,
        request: mts_20140618_models.SubmitFacerecogJobRequest,
    ) -> mts_20140618_models.SubmitFacerecogJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_facerecog_job_with_options(request, runtime)

    async def submit_facerecog_job_async(
        self,
        request: mts_20140618_models.SubmitFacerecogJobRequest,
    ) -> mts_20140618_models.SubmitFacerecogJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_facerecog_job_with_options_async(request, runtime)

    def submit_fp_compare_job_with_options(
        self,
        request: mts_20140618_models.SubmitFpCompareJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpCompareJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitFpCompareJobResponse().from_map(
            self.do_rpcrequest('SubmitFpCompareJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_fp_compare_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitFpCompareJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpCompareJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitFpCompareJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitFpCompareJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_fp_compare_job(
        self,
        request: mts_20140618_models.SubmitFpCompareJobRequest,
    ) -> mts_20140618_models.SubmitFpCompareJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_fp_compare_job_with_options(request, runtime)

    async def submit_fp_compare_job_async(
        self,
        request: mts_20140618_models.SubmitFpCompareJobRequest,
    ) -> mts_20140618_models.SubmitFpCompareJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_fp_compare_job_with_options_async(request, runtime)

    def submit_fp_dbdelete_job_with_options(
        self,
        request: mts_20140618_models.SubmitFpDBDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpDBDeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitFpDBDeleteJobResponse().from_map(
            self.do_rpcrequest('SubmitFpDBDeleteJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_fp_dbdelete_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitFpDBDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpDBDeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitFpDBDeleteJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitFpDBDeleteJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_fp_dbdelete_job(
        self,
        request: mts_20140618_models.SubmitFpDBDeleteJobRequest,
    ) -> mts_20140618_models.SubmitFpDBDeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_fp_dbdelete_job_with_options(request, runtime)

    async def submit_fp_dbdelete_job_async(
        self,
        request: mts_20140618_models.SubmitFpDBDeleteJobRequest,
    ) -> mts_20140618_models.SubmitFpDBDeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_fp_dbdelete_job_with_options_async(request, runtime)

    def submit_fp_file_delete_job_with_options(
        self,
        request: mts_20140618_models.SubmitFpFileDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpFileDeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitFpFileDeleteJobResponse().from_map(
            self.do_rpcrequest('SubmitFpFileDeleteJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_fp_file_delete_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitFpFileDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpFileDeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitFpFileDeleteJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitFpFileDeleteJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_fp_file_delete_job(
        self,
        request: mts_20140618_models.SubmitFpFileDeleteJobRequest,
    ) -> mts_20140618_models.SubmitFpFileDeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_fp_file_delete_job_with_options(request, runtime)

    async def submit_fp_file_delete_job_async(
        self,
        request: mts_20140618_models.SubmitFpFileDeleteJobRequest,
    ) -> mts_20140618_models.SubmitFpFileDeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_fp_file_delete_job_with_options_async(request, runtime)

    def submit_fp_shot_job_with_options(
        self,
        request: mts_20140618_models.SubmitFpShotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpShotJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitFpShotJobResponse().from_map(
            self.do_rpcrequest('SubmitFpShotJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_fp_shot_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitFpShotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpShotJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitFpShotJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitFpShotJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_fp_shot_job(
        self,
        request: mts_20140618_models.SubmitFpShotJobRequest,
    ) -> mts_20140618_models.SubmitFpShotJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_fp_shot_job_with_options(request, runtime)

    async def submit_fp_shot_job_async(
        self,
        request: mts_20140618_models.SubmitFpShotJobRequest,
    ) -> mts_20140618_models.SubmitFpShotJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_fp_shot_job_with_options_async(request, runtime)

    def submit_image_quality_job_with_options(
        self,
        request: mts_20140618_models.SubmitImageQualityJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitImageQualityJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitImageQualityJobResponse().from_map(
            self.do_rpcrequest('SubmitImageQualityJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_image_quality_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitImageQualityJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitImageQualityJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitImageQualityJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitImageQualityJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_image_quality_job(
        self,
        request: mts_20140618_models.SubmitImageQualityJobRequest,
    ) -> mts_20140618_models.SubmitImageQualityJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_image_quality_job_with_options(request, runtime)

    async def submit_image_quality_job_async(
        self,
        request: mts_20140618_models.SubmitImageQualityJobRequest,
    ) -> mts_20140618_models.SubmitImageQualityJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_image_quality_job_with_options_async(request, runtime)

    def submit_image_search_job_with_options(
        self,
        request: mts_20140618_models.SubmitImageSearchJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitImageSearchJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitImageSearchJobResponse().from_map(
            self.do_rpcrequest('SubmitImageSearchJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_image_search_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitImageSearchJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitImageSearchJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitImageSearchJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitImageSearchJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_image_search_job(
        self,
        request: mts_20140618_models.SubmitImageSearchJobRequest,
    ) -> mts_20140618_models.SubmitImageSearchJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_image_search_job_with_options(request, runtime)

    async def submit_image_search_job_async(
        self,
        request: mts_20140618_models.SubmitImageSearchJobRequest,
    ) -> mts_20140618_models.SubmitImageSearchJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_image_search_job_with_options_async(request, runtime)

    def submit_inner_job_with_options(
        self,
        request: mts_20140618_models.SubmitInnerJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitInnerJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitInnerJobResponse().from_map(
            self.do_rpcrequest('SubmitInnerJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_inner_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitInnerJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitInnerJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitInnerJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitInnerJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_inner_job(
        self,
        request: mts_20140618_models.SubmitInnerJobRequest,
    ) -> mts_20140618_models.SubmitInnerJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_inner_job_with_options(request, runtime)

    async def submit_inner_job_async(
        self,
        request: mts_20140618_models.SubmitInnerJobRequest,
    ) -> mts_20140618_models.SubmitInnerJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_inner_job_with_options_async(request, runtime)

    def submit_iproduction_job_with_options(
        self,
        request: mts_20140618_models.SubmitIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitIProductionJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitIProductionJobResponse().from_map(
            self.do_rpcrequest('SubmitIProductionJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_iproduction_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitIProductionJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitIProductionJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitIProductionJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_iproduction_job(
        self,
        request: mts_20140618_models.SubmitIProductionJobRequest,
    ) -> mts_20140618_models.SubmitIProductionJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_iproduction_job_with_options(request, runtime)

    async def submit_iproduction_job_async(
        self,
        request: mts_20140618_models.SubmitIProductionJobRequest,
    ) -> mts_20140618_models.SubmitIProductionJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_iproduction_job_with_options_async(request, runtime)

    def submit_jobs_with_options(
        self,
        request: mts_20140618_models.SubmitJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitJobsResponse().from_map(
            self.do_rpcrequest('SubmitJobs', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_jobs_with_options_async(
        self,
        request: mts_20140618_models.SubmitJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitJobsResponse().from_map(
            await self.do_rpcrequest_async('SubmitJobs', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_jobs(
        self,
        request: mts_20140618_models.SubmitJobsRequest,
    ) -> mts_20140618_models.SubmitJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_jobs_with_options(request, runtime)

    async def submit_jobs_async(
        self,
        request: mts_20140618_models.SubmitJobsRequest,
    ) -> mts_20140618_models.SubmitJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_jobs_with_options_async(request, runtime)

    def submit_mcjob_with_options(
        self,
        request: mts_20140618_models.SubmitMCJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMCJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitMCJobResponse().from_map(
            self.do_rpcrequest('SubmitMCJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_mcjob_with_options_async(
        self,
        request: mts_20140618_models.SubmitMCJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMCJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitMCJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitMCJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_mcjob(
        self,
        request: mts_20140618_models.SubmitMCJobRequest,
    ) -> mts_20140618_models.SubmitMCJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_mcjob_with_options(request, runtime)

    async def submit_mcjob_async(
        self,
        request: mts_20140618_models.SubmitMCJobRequest,
    ) -> mts_20140618_models.SubmitMCJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_mcjob_with_options_async(request, runtime)

    def submit_mcu_job_with_options(
        self,
        request: mts_20140618_models.SubmitMcuJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMcuJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitMcuJobResponse().from_map(
            self.do_rpcrequest('SubmitMcuJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_mcu_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitMcuJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMcuJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitMcuJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitMcuJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_mcu_job(
        self,
        request: mts_20140618_models.SubmitMcuJobRequest,
    ) -> mts_20140618_models.SubmitMcuJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_mcu_job_with_options(request, runtime)

    async def submit_mcu_job_async(
        self,
        request: mts_20140618_models.SubmitMcuJobRequest,
    ) -> mts_20140618_models.SubmitMcuJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_mcu_job_with_options_async(request, runtime)

    def submit_media_censor_job_with_options(
        self,
        request: mts_20140618_models.SubmitMediaCensorJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaCensorJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitMediaCensorJobResponse().from_map(
            self.do_rpcrequest('SubmitMediaCensorJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_media_censor_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitMediaCensorJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaCensorJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitMediaCensorJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitMediaCensorJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_media_censor_job(
        self,
        request: mts_20140618_models.SubmitMediaCensorJobRequest,
    ) -> mts_20140618_models.SubmitMediaCensorJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_media_censor_job_with_options(request, runtime)

    async def submit_media_censor_job_async(
        self,
        request: mts_20140618_models.SubmitMediaCensorJobRequest,
    ) -> mts_20140618_models.SubmitMediaCensorJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_media_censor_job_with_options_async(request, runtime)

    def submit_media_detail_job_with_options(
        self,
        request: mts_20140618_models.SubmitMediaDetailJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaDetailJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitMediaDetailJobResponse().from_map(
            self.do_rpcrequest('SubmitMediaDetailJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_media_detail_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitMediaDetailJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaDetailJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitMediaDetailJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitMediaDetailJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_media_detail_job(
        self,
        request: mts_20140618_models.SubmitMediaDetailJobRequest,
    ) -> mts_20140618_models.SubmitMediaDetailJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_media_detail_job_with_options(request, runtime)

    async def submit_media_detail_job_async(
        self,
        request: mts_20140618_models.SubmitMediaDetailJobRequest,
    ) -> mts_20140618_models.SubmitMediaDetailJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_media_detail_job_with_options_async(request, runtime)

    def submit_media_fp_delete_job_with_options(
        self,
        request: mts_20140618_models.SubmitMediaFpDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaFpDeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitMediaFpDeleteJobResponse().from_map(
            self.do_rpcrequest('SubmitMediaFpDeleteJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_media_fp_delete_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitMediaFpDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaFpDeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitMediaFpDeleteJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitMediaFpDeleteJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_media_fp_delete_job(
        self,
        request: mts_20140618_models.SubmitMediaFpDeleteJobRequest,
    ) -> mts_20140618_models.SubmitMediaFpDeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_media_fp_delete_job_with_options(request, runtime)

    async def submit_media_fp_delete_job_async(
        self,
        request: mts_20140618_models.SubmitMediaFpDeleteJobRequest,
    ) -> mts_20140618_models.SubmitMediaFpDeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_media_fp_delete_job_with_options_async(request, runtime)

    def submit_media_info_job_with_options(
        self,
        request: mts_20140618_models.SubmitMediaInfoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaInfoJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitMediaInfoJobResponse().from_map(
            self.do_rpcrequest('SubmitMediaInfoJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_media_info_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitMediaInfoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaInfoJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitMediaInfoJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitMediaInfoJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_media_info_job(
        self,
        request: mts_20140618_models.SubmitMediaInfoJobRequest,
    ) -> mts_20140618_models.SubmitMediaInfoJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_media_info_job_with_options(request, runtime)

    async def submit_media_info_job_async(
        self,
        request: mts_20140618_models.SubmitMediaInfoJobRequest,
    ) -> mts_20140618_models.SubmitMediaInfoJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_media_info_job_with_options_async(request, runtime)

    def submit_porn_job_with_options(
        self,
        request: mts_20140618_models.SubmitPornJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitPornJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitPornJobResponse().from_map(
            self.do_rpcrequest('SubmitPornJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_porn_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitPornJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitPornJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitPornJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitPornJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_porn_job(
        self,
        request: mts_20140618_models.SubmitPornJobRequest,
    ) -> mts_20140618_models.SubmitPornJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_porn_job_with_options(request, runtime)

    async def submit_porn_job_async(
        self,
        request: mts_20140618_models.SubmitPornJobRequest,
    ) -> mts_20140618_models.SubmitPornJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_porn_job_with_options_async(request, runtime)

    def submit_smarttag_job_with_options(
        self,
        request: mts_20140618_models.SubmitSmarttagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitSmarttagJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitSmarttagJobResponse().from_map(
            self.do_rpcrequest('SubmitSmarttagJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_smarttag_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitSmarttagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitSmarttagJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitSmarttagJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitSmarttagJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_smarttag_job(
        self,
        request: mts_20140618_models.SubmitSmarttagJobRequest,
    ) -> mts_20140618_models.SubmitSmarttagJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_smarttag_job_with_options(request, runtime)

    async def submit_smarttag_job_async(
        self,
        request: mts_20140618_models.SubmitSmarttagJobRequest,
    ) -> mts_20140618_models.SubmitSmarttagJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_smarttag_job_with_options_async(request, runtime)

    def submit_snapshot_job_with_options(
        self,
        request: mts_20140618_models.SubmitSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitSnapshotJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitSnapshotJobResponse().from_map(
            self.do_rpcrequest('SubmitSnapshotJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_snapshot_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitSnapshotJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitSnapshotJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitSnapshotJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_snapshot_job(
        self,
        request: mts_20140618_models.SubmitSnapshotJobRequest,
    ) -> mts_20140618_models.SubmitSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_snapshot_job_with_options(request, runtime)

    async def submit_snapshot_job_async(
        self,
        request: mts_20140618_models.SubmitSnapshotJobRequest,
    ) -> mts_20140618_models.SubmitSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_snapshot_job_with_options_async(request, runtime)

    def submit_subtitle_job_with_options(
        self,
        request: mts_20140618_models.SubmitSubtitleJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitSubtitleJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitSubtitleJobResponse().from_map(
            self.do_rpcrequest('SubmitSubtitleJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_subtitle_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitSubtitleJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitSubtitleJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitSubtitleJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitSubtitleJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_subtitle_job(
        self,
        request: mts_20140618_models.SubmitSubtitleJobRequest,
    ) -> mts_20140618_models.SubmitSubtitleJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_subtitle_job_with_options(request, runtime)

    async def submit_subtitle_job_async(
        self,
        request: mts_20140618_models.SubmitSubtitleJobRequest,
    ) -> mts_20140618_models.SubmitSubtitleJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_subtitle_job_with_options_async(request, runtime)

    def submit_tag_job_with_options(
        self,
        request: mts_20140618_models.SubmitTagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitTagJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitTagJobResponse().from_map(
            self.do_rpcrequest('SubmitTagJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_tag_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitTagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitTagJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitTagJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitTagJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_tag_job(
        self,
        request: mts_20140618_models.SubmitTagJobRequest,
    ) -> mts_20140618_models.SubmitTagJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_tag_job_with_options(request, runtime)

    async def submit_tag_job_async(
        self,
        request: mts_20140618_models.SubmitTagJobRequest,
    ) -> mts_20140618_models.SubmitTagJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_tag_job_with_options_async(request, runtime)

    def submit_terrorism_job_with_options(
        self,
        request: mts_20140618_models.SubmitTerrorismJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitTerrorismJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitTerrorismJobResponse().from_map(
            self.do_rpcrequest('SubmitTerrorismJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_terrorism_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitTerrorismJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitTerrorismJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitTerrorismJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitTerrorismJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_terrorism_job(
        self,
        request: mts_20140618_models.SubmitTerrorismJobRequest,
    ) -> mts_20140618_models.SubmitTerrorismJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_terrorism_job_with_options(request, runtime)

    async def submit_terrorism_job_async(
        self,
        request: mts_20140618_models.SubmitTerrorismJobRequest,
    ) -> mts_20140618_models.SubmitTerrorismJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_terrorism_job_with_options_async(request, runtime)

    def submit_video_gif_job_with_options(
        self,
        request: mts_20140618_models.SubmitVideoGifJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitVideoGifJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitVideoGifJobResponse().from_map(
            self.do_rpcrequest('SubmitVideoGifJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_video_gif_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitVideoGifJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitVideoGifJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitVideoGifJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitVideoGifJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_video_gif_job(
        self,
        request: mts_20140618_models.SubmitVideoGifJobRequest,
    ) -> mts_20140618_models.SubmitVideoGifJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_video_gif_job_with_options(request, runtime)

    async def submit_video_gif_job_async(
        self,
        request: mts_20140618_models.SubmitVideoGifJobRequest,
    ) -> mts_20140618_models.SubmitVideoGifJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_video_gif_job_with_options_async(request, runtime)

    def submit_video_pose_job_with_options(
        self,
        request: mts_20140618_models.SubmitVideoPoseJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitVideoPoseJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitVideoPoseJobResponse().from_map(
            self.do_rpcrequest('SubmitVideoPoseJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_video_pose_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitVideoPoseJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitVideoPoseJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitVideoPoseJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitVideoPoseJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_video_pose_job(
        self,
        request: mts_20140618_models.SubmitVideoPoseJobRequest,
    ) -> mts_20140618_models.SubmitVideoPoseJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_video_pose_job_with_options(request, runtime)

    async def submit_video_pose_job_async(
        self,
        request: mts_20140618_models.SubmitVideoPoseJobRequest,
    ) -> mts_20140618_models.SubmitVideoPoseJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_video_pose_job_with_options_async(request, runtime)

    def submit_video_quality_job_with_options(
        self,
        request: mts_20140618_models.SubmitVideoQualityJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitVideoQualityJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitVideoQualityJobResponse().from_map(
            self.do_rpcrequest('SubmitVideoQualityJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_video_quality_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitVideoQualityJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitVideoQualityJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitVideoQualityJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitVideoQualityJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_video_quality_job(
        self,
        request: mts_20140618_models.SubmitVideoQualityJobRequest,
    ) -> mts_20140618_models.SubmitVideoQualityJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_video_quality_job_with_options(request, runtime)

    async def submit_video_quality_job_async(
        self,
        request: mts_20140618_models.SubmitVideoQualityJobRequest,
    ) -> mts_20140618_models.SubmitVideoQualityJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_video_quality_job_with_options_async(request, runtime)

    def submit_video_split_job_with_options(
        self,
        request: mts_20140618_models.SubmitVideoSplitJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitVideoSplitJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitVideoSplitJobResponse().from_map(
            self.do_rpcrequest('SubmitVideoSplitJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_video_split_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitVideoSplitJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitVideoSplitJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitVideoSplitJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitVideoSplitJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_video_split_job(
        self,
        request: mts_20140618_models.SubmitVideoSplitJobRequest,
    ) -> mts_20140618_models.SubmitVideoSplitJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_video_split_job_with_options(request, runtime)

    async def submit_video_split_job_async(
        self,
        request: mts_20140618_models.SubmitVideoSplitJobRequest,
    ) -> mts_20140618_models.SubmitVideoSplitJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_video_split_job_with_options_async(request, runtime)

    def submit_video_summary_job_with_options(
        self,
        request: mts_20140618_models.SubmitVideoSummaryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitVideoSummaryJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitVideoSummaryJobResponse().from_map(
            self.do_rpcrequest('SubmitVideoSummaryJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_video_summary_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitVideoSummaryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitVideoSummaryJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.SubmitVideoSummaryJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitVideoSummaryJob', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_video_summary_job(
        self,
        request: mts_20140618_models.SubmitVideoSummaryJobRequest,
    ) -> mts_20140618_models.SubmitVideoSummaryJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_video_summary_job_with_options(request, runtime)

    async def submit_video_summary_job_async(
        self,
        request: mts_20140618_models.SubmitVideoSummaryJobRequest,
    ) -> mts_20140618_models.SubmitVideoSummaryJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_video_summary_job_with_options_async(request, runtime)

    def tag_custom_person_with_options(
        self,
        request: mts_20140618_models.TagCustomPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.TagCustomPersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.TagCustomPersonResponse().from_map(
            self.do_rpcrequest('TagCustomPerson', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_custom_person_with_options_async(
        self,
        request: mts_20140618_models.TagCustomPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.TagCustomPersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.TagCustomPersonResponse().from_map(
            await self.do_rpcrequest_async('TagCustomPerson', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_custom_person(
        self,
        request: mts_20140618_models.TagCustomPersonRequest,
    ) -> mts_20140618_models.TagCustomPersonResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_custom_person_with_options(request, runtime)

    async def tag_custom_person_async(
        self,
        request: mts_20140618_models.TagCustomPersonRequest,
    ) -> mts_20140618_models.TagCustomPersonResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_custom_person_with_options_async(request, runtime)

    def unbind_input_bucket_with_options(
        self,
        request: mts_20140618_models.UnbindInputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UnbindInputBucketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UnbindInputBucketResponse().from_map(
            self.do_rpcrequest('UnbindInputBucket', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_input_bucket_with_options_async(
        self,
        request: mts_20140618_models.UnbindInputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UnbindInputBucketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UnbindInputBucketResponse().from_map(
            await self.do_rpcrequest_async('UnbindInputBucket', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_input_bucket(
        self,
        request: mts_20140618_models.UnbindInputBucketRequest,
    ) -> mts_20140618_models.UnbindInputBucketResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_input_bucket_with_options(request, runtime)

    async def unbind_input_bucket_async(
        self,
        request: mts_20140618_models.UnbindInputBucketRequest,
    ) -> mts_20140618_models.UnbindInputBucketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_input_bucket_with_options_async(request, runtime)

    def unbind_output_bucket_with_options(
        self,
        request: mts_20140618_models.UnbindOutputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UnbindOutputBucketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UnbindOutputBucketResponse().from_map(
            self.do_rpcrequest('UnbindOutputBucket', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_output_bucket_with_options_async(
        self,
        request: mts_20140618_models.UnbindOutputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UnbindOutputBucketResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UnbindOutputBucketResponse().from_map(
            await self.do_rpcrequest_async('UnbindOutputBucket', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_output_bucket(
        self,
        request: mts_20140618_models.UnbindOutputBucketRequest,
    ) -> mts_20140618_models.UnbindOutputBucketResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_output_bucket_with_options(request, runtime)

    async def unbind_output_bucket_async(
        self,
        request: mts_20140618_models.UnbindOutputBucketRequest,
    ) -> mts_20140618_models.UnbindOutputBucketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_output_bucket_with_options_async(request, runtime)

    def unregister_custom_face_with_options(
        self,
        request: mts_20140618_models.UnregisterCustomFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UnregisterCustomFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UnregisterCustomFaceResponse().from_map(
            self.do_rpcrequest('UnregisterCustomFace', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unregister_custom_face_with_options_async(
        self,
        request: mts_20140618_models.UnregisterCustomFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UnregisterCustomFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UnregisterCustomFaceResponse().from_map(
            await self.do_rpcrequest_async('UnregisterCustomFace', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unregister_custom_face(
        self,
        request: mts_20140618_models.UnregisterCustomFaceRequest,
    ) -> mts_20140618_models.UnregisterCustomFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unregister_custom_face_with_options(request, runtime)

    async def unregister_custom_face_async(
        self,
        request: mts_20140618_models.UnregisterCustomFaceRequest,
    ) -> mts_20140618_models.UnregisterCustomFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unregister_custom_face_with_options_async(request, runtime)

    def update_asr_pipeline_with_options(
        self,
        request: mts_20140618_models.UpdateAsrPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateAsrPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateAsrPipelineResponse().from_map(
            self.do_rpcrequest('UpdateAsrPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_asr_pipeline_with_options_async(
        self,
        request: mts_20140618_models.UpdateAsrPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateAsrPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateAsrPipelineResponse().from_map(
            await self.do_rpcrequest_async('UpdateAsrPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_asr_pipeline(
        self,
        request: mts_20140618_models.UpdateAsrPipelineRequest,
    ) -> mts_20140618_models.UpdateAsrPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_asr_pipeline_with_options(request, runtime)

    async def update_asr_pipeline_async(
        self,
        request: mts_20140618_models.UpdateAsrPipelineRequest,
    ) -> mts_20140618_models.UpdateAsrPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_asr_pipeline_with_options_async(request, runtime)

    def update_category_name_with_options(
        self,
        request: mts_20140618_models.UpdateCategoryNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateCategoryNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateCategoryNameResponse().from_map(
            self.do_rpcrequest('UpdateCategoryName', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_category_name_with_options_async(
        self,
        request: mts_20140618_models.UpdateCategoryNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateCategoryNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateCategoryNameResponse().from_map(
            await self.do_rpcrequest_async('UpdateCategoryName', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_category_name(
        self,
        request: mts_20140618_models.UpdateCategoryNameRequest,
    ) -> mts_20140618_models.UpdateCategoryNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_category_name_with_options(request, runtime)

    async def update_category_name_async(
        self,
        request: mts_20140618_models.UpdateCategoryNameRequest,
    ) -> mts_20140618_models.UpdateCategoryNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_category_name_with_options_async(request, runtime)

    def update_censor_pipeline_with_options(
        self,
        request: mts_20140618_models.UpdateCensorPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateCensorPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateCensorPipelineResponse().from_map(
            self.do_rpcrequest('UpdateCensorPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_censor_pipeline_with_options_async(
        self,
        request: mts_20140618_models.UpdateCensorPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateCensorPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateCensorPipelineResponse().from_map(
            await self.do_rpcrequest_async('UpdateCensorPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_censor_pipeline(
        self,
        request: mts_20140618_models.UpdateCensorPipelineRequest,
    ) -> mts_20140618_models.UpdateCensorPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_censor_pipeline_with_options(request, runtime)

    async def update_censor_pipeline_async(
        self,
        request: mts_20140618_models.UpdateCensorPipelineRequest,
    ) -> mts_20140618_models.UpdateCensorPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_censor_pipeline_with_options_async(request, runtime)

    def update_cover_pipeline_with_options(
        self,
        request: mts_20140618_models.UpdateCoverPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateCoverPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateCoverPipelineResponse().from_map(
            self.do_rpcrequest('UpdateCoverPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_cover_pipeline_with_options_async(
        self,
        request: mts_20140618_models.UpdateCoverPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateCoverPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateCoverPipelineResponse().from_map(
            await self.do_rpcrequest_async('UpdateCoverPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cover_pipeline(
        self,
        request: mts_20140618_models.UpdateCoverPipelineRequest,
    ) -> mts_20140618_models.UpdateCoverPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cover_pipeline_with_options(request, runtime)

    async def update_cover_pipeline_async(
        self,
        request: mts_20140618_models.UpdateCoverPipelineRequest,
    ) -> mts_20140618_models.UpdateCoverPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cover_pipeline_with_options_async(request, runtime)

    def update_mctemplate_with_options(
        self,
        request: mts_20140618_models.UpdateMCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMCTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateMCTemplateResponse().from_map(
            self.do_rpcrequest('UpdateMCTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_mctemplate_with_options_async(
        self,
        request: mts_20140618_models.UpdateMCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMCTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateMCTemplateResponse().from_map(
            await self.do_rpcrequest_async('UpdateMCTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_mctemplate(
        self,
        request: mts_20140618_models.UpdateMCTemplateRequest,
    ) -> mts_20140618_models.UpdateMCTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_mctemplate_with_options(request, runtime)

    async def update_mctemplate_async(
        self,
        request: mts_20140618_models.UpdateMCTemplateRequest,
    ) -> mts_20140618_models.UpdateMCTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_mctemplate_with_options_async(request, runtime)

    def update_mcu_template_with_options(
        self,
        request: mts_20140618_models.UpdateMcuTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMcuTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateMcuTemplateResponse().from_map(
            self.do_rpcrequest('UpdateMcuTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_mcu_template_with_options_async(
        self,
        request: mts_20140618_models.UpdateMcuTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMcuTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateMcuTemplateResponse().from_map(
            await self.do_rpcrequest_async('UpdateMcuTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_mcu_template(
        self,
        request: mts_20140618_models.UpdateMcuTemplateRequest,
    ) -> mts_20140618_models.UpdateMcuTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_mcu_template_with_options(request, runtime)

    async def update_mcu_template_async(
        self,
        request: mts_20140618_models.UpdateMcuTemplateRequest,
    ) -> mts_20140618_models.UpdateMcuTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_mcu_template_with_options_async(request, runtime)

    def update_media_with_options(
        self,
        request: mts_20140618_models.UpdateMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateMediaResponse().from_map(
            self.do_rpcrequest('UpdateMedia', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_media_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateMediaResponse().from_map(
            await self.do_rpcrequest_async('UpdateMedia', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_media(
        self,
        request: mts_20140618_models.UpdateMediaRequest,
    ) -> mts_20140618_models.UpdateMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_media_with_options(request, runtime)

    async def update_media_async(
        self,
        request: mts_20140618_models.UpdateMediaRequest,
    ) -> mts_20140618_models.UpdateMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_media_with_options_async(request, runtime)

    def update_media_category_with_options(
        self,
        request: mts_20140618_models.UpdateMediaCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateMediaCategoryResponse().from_map(
            self.do_rpcrequest('UpdateMediaCategory', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_media_category_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateMediaCategoryResponse().from_map(
            await self.do_rpcrequest_async('UpdateMediaCategory', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_media_category(
        self,
        request: mts_20140618_models.UpdateMediaCategoryRequest,
    ) -> mts_20140618_models.UpdateMediaCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_media_category_with_options(request, runtime)

    async def update_media_category_async(
        self,
        request: mts_20140618_models.UpdateMediaCategoryRequest,
    ) -> mts_20140618_models.UpdateMediaCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_media_category_with_options_async(request, runtime)

    def update_media_cover_with_options(
        self,
        request: mts_20140618_models.UpdateMediaCoverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaCoverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateMediaCoverResponse().from_map(
            self.do_rpcrequest('UpdateMediaCover', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_media_cover_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaCoverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaCoverResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateMediaCoverResponse().from_map(
            await self.do_rpcrequest_async('UpdateMediaCover', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_media_cover(
        self,
        request: mts_20140618_models.UpdateMediaCoverRequest,
    ) -> mts_20140618_models.UpdateMediaCoverResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_media_cover_with_options(request, runtime)

    async def update_media_cover_async(
        self,
        request: mts_20140618_models.UpdateMediaCoverRequest,
    ) -> mts_20140618_models.UpdateMediaCoverResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_media_cover_with_options_async(request, runtime)

    def update_media_publish_state_with_options(
        self,
        request: mts_20140618_models.UpdateMediaPublishStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaPublishStateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateMediaPublishStateResponse().from_map(
            self.do_rpcrequest('UpdateMediaPublishState', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_media_publish_state_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaPublishStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaPublishStateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateMediaPublishStateResponse().from_map(
            await self.do_rpcrequest_async('UpdateMediaPublishState', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_media_publish_state(
        self,
        request: mts_20140618_models.UpdateMediaPublishStateRequest,
    ) -> mts_20140618_models.UpdateMediaPublishStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_media_publish_state_with_options(request, runtime)

    async def update_media_publish_state_async(
        self,
        request: mts_20140618_models.UpdateMediaPublishStateRequest,
    ) -> mts_20140618_models.UpdateMediaPublishStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_media_publish_state_with_options_async(request, runtime)

    def update_media_workflow_with_options(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaWorkflowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateMediaWorkflowResponse().from_map(
            self.do_rpcrequest('UpdateMediaWorkflow', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaWorkflowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateMediaWorkflowResponse().from_map(
            await self.do_rpcrequest_async('UpdateMediaWorkflow', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_media_workflow(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowRequest,
    ) -> mts_20140618_models.UpdateMediaWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_media_workflow_with_options(request, runtime)

    async def update_media_workflow_async(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowRequest,
    ) -> mts_20140618_models.UpdateMediaWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_media_workflow_with_options_async(request, runtime)

    def update_media_workflow_trigger_mode_with_options(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowTriggerModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaWorkflowTriggerModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateMediaWorkflowTriggerModeResponse().from_map(
            self.do_rpcrequest('UpdateMediaWorkflowTriggerMode', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_media_workflow_trigger_mode_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowTriggerModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaWorkflowTriggerModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateMediaWorkflowTriggerModeResponse().from_map(
            await self.do_rpcrequest_async('UpdateMediaWorkflowTriggerMode', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_media_workflow_trigger_mode(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowTriggerModeRequest,
    ) -> mts_20140618_models.UpdateMediaWorkflowTriggerModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_media_workflow_trigger_mode_with_options(request, runtime)

    async def update_media_workflow_trigger_mode_async(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowTriggerModeRequest,
    ) -> mts_20140618_models.UpdateMediaWorkflowTriggerModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_media_workflow_trigger_mode_with_options_async(request, runtime)

    def update_pipeline_with_options(
        self,
        request: mts_20140618_models.UpdatePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdatePipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdatePipelineResponse().from_map(
            self.do_rpcrequest('UpdatePipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_pipeline_with_options_async(
        self,
        request: mts_20140618_models.UpdatePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdatePipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdatePipelineResponse().from_map(
            await self.do_rpcrequest_async('UpdatePipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_pipeline(
        self,
        request: mts_20140618_models.UpdatePipelineRequest,
    ) -> mts_20140618_models.UpdatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_pipeline_with_options(request, runtime)

    async def update_pipeline_async(
        self,
        request: mts_20140618_models.UpdatePipelineRequest,
    ) -> mts_20140618_models.UpdatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_pipeline_with_options_async(request, runtime)

    def update_porn_pipeline_with_options(
        self,
        request: mts_20140618_models.UpdatePornPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdatePornPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdatePornPipelineResponse().from_map(
            self.do_rpcrequest('UpdatePornPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_porn_pipeline_with_options_async(
        self,
        request: mts_20140618_models.UpdatePornPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdatePornPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdatePornPipelineResponse().from_map(
            await self.do_rpcrequest_async('UpdatePornPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_porn_pipeline(
        self,
        request: mts_20140618_models.UpdatePornPipelineRequest,
    ) -> mts_20140618_models.UpdatePornPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_porn_pipeline_with_options(request, runtime)

    async def update_porn_pipeline_async(
        self,
        request: mts_20140618_models.UpdatePornPipelineRequest,
    ) -> mts_20140618_models.UpdatePornPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_porn_pipeline_with_options_async(request, runtime)

    def update_smarttag_template_with_options(
        self,
        request: mts_20140618_models.UpdateSmarttagTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateSmarttagTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateSmarttagTemplateResponse().from_map(
            self.do_rpcrequest('UpdateSmarttagTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_smarttag_template_with_options_async(
        self,
        request: mts_20140618_models.UpdateSmarttagTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateSmarttagTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateSmarttagTemplateResponse().from_map(
            await self.do_rpcrequest_async('UpdateSmarttagTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_smarttag_template(
        self,
        request: mts_20140618_models.UpdateSmarttagTemplateRequest,
    ) -> mts_20140618_models.UpdateSmarttagTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_smarttag_template_with_options(request, runtime)

    async def update_smarttag_template_async(
        self,
        request: mts_20140618_models.UpdateSmarttagTemplateRequest,
    ) -> mts_20140618_models.UpdateSmarttagTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_smarttag_template_with_options_async(request, runtime)

    def update_template_with_options(
        self,
        request: mts_20140618_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateTemplateResponse().from_map(
            self.do_rpcrequest('UpdateTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_template_with_options_async(
        self,
        request: mts_20140618_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateTemplateResponse().from_map(
            await self.do_rpcrequest_async('UpdateTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_template(
        self,
        request: mts_20140618_models.UpdateTemplateRequest,
    ) -> mts_20140618_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    async def update_template_async(
        self,
        request: mts_20140618_models.UpdateTemplateRequest,
    ) -> mts_20140618_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_template_with_options_async(request, runtime)

    def update_terrorism_pipeline_with_options(
        self,
        request: mts_20140618_models.UpdateTerrorismPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateTerrorismPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateTerrorismPipelineResponse().from_map(
            self.do_rpcrequest('UpdateTerrorismPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_terrorism_pipeline_with_options_async(
        self,
        request: mts_20140618_models.UpdateTerrorismPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateTerrorismPipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateTerrorismPipelineResponse().from_map(
            await self.do_rpcrequest_async('UpdateTerrorismPipeline', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_terrorism_pipeline(
        self,
        request: mts_20140618_models.UpdateTerrorismPipelineRequest,
    ) -> mts_20140618_models.UpdateTerrorismPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_terrorism_pipeline_with_options(request, runtime)

    async def update_terrorism_pipeline_async(
        self,
        request: mts_20140618_models.UpdateTerrorismPipelineRequest,
    ) -> mts_20140618_models.UpdateTerrorismPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_terrorism_pipeline_with_options_async(request, runtime)

    def update_water_mark_template_with_options(
        self,
        request: mts_20140618_models.UpdateWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateWaterMarkTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateWaterMarkTemplateResponse().from_map(
            self.do_rpcrequest('UpdateWaterMarkTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_water_mark_template_with_options_async(
        self,
        request: mts_20140618_models.UpdateWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateWaterMarkTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return mts_20140618_models.UpdateWaterMarkTemplateResponse().from_map(
            await self.do_rpcrequest_async('UpdateWaterMarkTemplate', '2014-06-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_water_mark_template(
        self,
        request: mts_20140618_models.UpdateWaterMarkTemplateRequest,
    ) -> mts_20140618_models.UpdateWaterMarkTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_water_mark_template_with_options(request, runtime)

    async def update_water_mark_template_async(
        self,
        request: mts_20140618_models.UpdateWaterMarkTemplateRequest,
    ) -> mts_20140618_models.UpdateWaterMarkTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_water_mark_template_with_options_async(request, runtime)
