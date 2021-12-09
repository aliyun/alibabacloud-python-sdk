# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mts20140618 import models as mts_20140618_models
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
            'ap-northeast-2-pop': 'mts.aliyuncs.com',
            'ap-southeast-2': 'mts.aliyuncs.com',
            'ap-southeast-3': 'mts.aliyuncs.com',
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
            'cn-huhehaote-nebula-1': 'mts.aliyuncs.com',
            'cn-north-2-gov-1': 'mts.aliyuncs.com',
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
            'cn-wulanchabu': 'mts.aliyuncs.com',
            'cn-yushanfang': 'mts.aliyuncs.com',
            'cn-zhangbei': 'mts.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'mts.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'mts.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'mts.aliyuncs.com',
            'eu-west-1-oxs': 'mts.aliyuncs.com',
            'me-east-1': 'mts.aliyuncs.com',
            'rus-west-1-pop': 'mts.aliyuncs.com',
            'us-east-1': 'mts.aliyuncs.com'
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
        query = {}
        query['MediaWorkflowId'] = request.media_workflow_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ActivateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ActivateMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.ActivateMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ActivateMediaWorkflowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MediaWorkflowId'] = request.media_workflow_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ActivateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ActivateMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddAsrPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddAsrPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_asr_pipeline_with_options_async(
        self,
        request: mts_20140618_models.AddAsrPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddAsrPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddAsrPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddAsrPipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CateName'] = request.cate_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ParentId'] = request.parent_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddCategory',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_category_with_options_async(
        self,
        request: mts_20140618_models.AddCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CateName'] = request.cate_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ParentId'] = request.parent_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddCategory',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddCategoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddCensorPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddCensorPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_censor_pipeline_with_options_async(
        self,
        request: mts_20140618_models.AddCensorPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddCensorPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddCensorPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddCensorPipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Role'] = request.role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddCoverPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddCoverPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_cover_pipeline_with_options_async(
        self,
        request: mts_20140618_models.AddCoverPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddCoverPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Role'] = request.role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddCoverPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddCoverPipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Abuse'] = request.abuse
        query['Ad'] = request.ad
        query['Contraband'] = request.contraband
        query['Live'] = request.live
        query['Logo'] = request.logo
        query['Name'] = request.name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Politics'] = request.politics
        query['Porn'] = request.porn
        query['Qrcode'] = request.qrcode
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Terrorism'] = request.terrorism
        query['spam'] = request.spam
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddMCTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddMCTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_mctemplate_with_options_async(
        self,
        request: mts_20140618_models.AddMCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMCTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Abuse'] = request.abuse
        query['Ad'] = request.ad
        query['Contraband'] = request.contraband
        query['Live'] = request.live
        query['Logo'] = request.logo
        query['Name'] = request.name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Politics'] = request.politics
        query['Porn'] = request.porn
        query['Qrcode'] = request.qrcode
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Terrorism'] = request.terrorism
        query['spam'] = request.spam
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddMCTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddMCTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CateId'] = request.cate_id
        query['CoverURL'] = request.cover_url
        query['Description'] = request.description
        query['FileURL'] = request.file_url
        query['InputUnbind'] = request.input_unbind
        query['MediaWorkflowId'] = request.media_workflow_id
        query['MediaWorkflowUserData'] = request.media_workflow_user_data
        query['OverrideParams'] = request.override_params
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Tags'] = request.tags
        query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_media_with_options_async(
        self,
        request: mts_20140618_models.AddMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CateId'] = request.cate_id
        query['CoverURL'] = request.cover_url
        query['Description'] = request.description
        query['FileURL'] = request.file_url
        query['InputUnbind'] = request.input_unbind
        query['MediaWorkflowId'] = request.media_workflow_id
        query['MediaWorkflowUserData'] = request.media_workflow_user_data
        query['OverrideParams'] = request.override_params
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Tags'] = request.tags
        query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddMediaResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddMediaTag',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddMediaTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_media_tag_with_options_async(
        self,
        request: mts_20140618_models.AddMediaTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMediaTagResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddMediaTag',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddMediaTagResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Topology'] = request.topology
        query['TriggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.AddMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMediaWorkflowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Topology'] = request.topology
        query['TriggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Role'] = request.role
        query['Speed'] = request.speed
        query['SpeedLevel'] = request.speed_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_pipeline_with_options_async(
        self,
        request: mts_20140618_models.AddPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Role'] = request.role
        query['Speed'] = request.speed
        query['SpeedLevel'] = request.speed_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddPipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddPornPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddPornPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_porn_pipeline_with_options_async(
        self,
        request: mts_20140618_models.AddPornPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddPornPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddPornPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddPornPipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AnalyseTypes'] = request.analyse_types
        query['FaceCategoryIds'] = request.face_category_ids
        query['Industry'] = request.industry
        query['IsDefault'] = request.is_default
        query['KeywordConfig'] = request.keyword_config
        query['KnowledgeConfig'] = request.knowledge_config
        query['LabelType'] = request.label_type
        query['LabelVersion'] = request.label_version
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Scene'] = request.scene
        query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddSmarttagTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_smarttag_template_with_options_async(
        self,
        request: mts_20140618_models.AddSmarttagTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddSmarttagTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AnalyseTypes'] = request.analyse_types
        query['FaceCategoryIds'] = request.face_category_ids
        query['Industry'] = request.industry
        query['IsDefault'] = request.is_default
        query['KeywordConfig'] = request.keyword_config
        query['KnowledgeConfig'] = request.knowledge_config
        query['LabelType'] = request.label_type
        query['LabelVersion'] = request.label_version
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Scene'] = request.scene
        query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddSmarttagTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Audio'] = request.audio
        query['Container'] = request.container
        query['MuxConfig'] = request.mux_config
        query['Name'] = request.name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TransConfig'] = request.trans_config
        query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_template_with_options_async(
        self,
        request: mts_20140618_models.AddTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Audio'] = request.audio
        query['Container'] = request.container
        query['MuxConfig'] = request.mux_config
        query['Name'] = request.name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TransConfig'] = request.trans_config
        query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddTerrorismPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddTerrorismPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_terrorism_pipeline_with_options_async(
        self,
        request: mts_20140618_models.AddTerrorismPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddTerrorismPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddTerrorismPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddTerrorismPipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Config'] = request.config
        query['Name'] = request.name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddWaterMarkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_water_mark_template_with_options_async(
        self,
        request: mts_20140618_models.AddWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddWaterMarkTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Config'] = request.config
        query['Name'] = request.name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.AddWaterMarkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Bucket'] = request.bucket
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindInputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.BindInputBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_input_bucket_with_options_async(
        self,
        request: mts_20140618_models.BindInputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.BindInputBucketResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Bucket'] = request.bucket
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindInputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.BindInputBucketResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Bucket'] = request.bucket
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindOutputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.BindOutputBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_output_bucket_with_options_async(
        self,
        request: mts_20140618_models.BindOutputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.BindOutputBucketResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Bucket'] = request.bucket
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindOutputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.BindOutputBucketResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CancelJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_job_with_options_async(
        self,
        request: mts_20140618_models.CancelJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CancelJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CancelJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CategoryTree',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CategoryTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def category_tree_with_options_async(
        self,
        request: mts_20140618_models.CategoryTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CategoryTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CategoryTree',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CategoryTreeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Bid'] = request.bid
        query['Country'] = request.country
        query['GmtWakeup'] = request.gmt_wakeup
        query['Hid'] = request.hid
        query['Interrupt'] = request.interrupt
        query['Invoker'] = request.invoker
        query['Level'] = request.level
        query['Message'] = request.message
        query['Pk'] = request.pk
        query['Prompt'] = request.prompt
        query['Success'] = request.success
        query['TaskExtraData'] = request.task_extra_data
        query['TaskIdentifier'] = request.task_identifier
        query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckResource',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CheckResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_resource_with_options_async(
        self,
        request: mts_20140618_models.CheckResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CheckResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Bid'] = request.bid
        query['Country'] = request.country
        query['GmtWakeup'] = request.gmt_wakeup
        query['Hid'] = request.hid
        query['Interrupt'] = request.interrupt
        query['Invoker'] = request.invoker
        query['Level'] = request.level
        query['Message'] = request.message
        query['Pk'] = request.pk
        query['Prompt'] = request.prompt
        query['Success'] = request.success
        query['TaskExtraData'] = request.task_extra_data
        query['TaskIdentifier'] = request.task_identifier
        query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckResource',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CheckResourceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Config'] = request.config
        query['Description'] = request.description
        query['ModelId'] = request.model_id
        query['Name'] = request.name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFpShotDB',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CreateFpShotDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fp_shot_dbwith_options_async(
        self,
        request: mts_20140618_models.CreateFpShotDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateFpShotDBResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Config'] = request.config
        query['Description'] = request.description
        query['ModelId'] = request.model_id
        query['Name'] = request.name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFpShotDB',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CreateFpShotDBResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_inference_server_with_options(
        self,
        request: mts_20140618_models.CreateInferenceServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateInferenceServerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FunctionName'] = request.function_name
        query['ModelPath'] = request.model_path
        query['ModelType'] = request.model_type
        query['PipelineId'] = request.pipeline_id
        query['TestId'] = request.test_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateInferenceServer',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CreateInferenceServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_inference_server_with_options_async(
        self,
        request: mts_20140618_models.CreateInferenceServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateInferenceServerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FunctionName'] = request.function_name
        query['ModelPath'] = request.model_path
        query['ModelType'] = request.model_type
        query['PipelineId'] = request.pipeline_id
        query['TestId'] = request.test_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateInferenceServer',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CreateInferenceServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_inference_server(
        self,
        request: mts_20140618_models.CreateInferenceServerRequest,
    ) -> mts_20140618_models.CreateInferenceServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_inference_server_with_options(request, runtime)

    async def create_inference_server_async(
        self,
        request: mts_20140618_models.CreateInferenceServerRequest,
    ) -> mts_20140618_models.CreateInferenceServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_inference_server_with_options_async(request, runtime)

    def create_mcu_template_with_options(
        self,
        request: mts_20140618_models.CreateMcuTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateMcuTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMcuTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CreateMcuTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcu_template_with_options_async(
        self,
        request: mts_20140618_models.CreateMcuTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateMcuTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMcuTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CreateMcuTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['EndUserId'] = request.end_user_id
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SessionTime'] = request.session_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSession',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CreateSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_session_with_options_async(
        self,
        request: mts_20140618_models.CreateSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateSessionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndUserId'] = request.end_user_id
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SessionTime'] = request.session_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSession',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.CreateSessionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['MediaWorkflowId'] = request.media_workflow_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeactivateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeactivateMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def deactivate_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.DeactivateMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeactivateMediaWorkflowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MediaWorkflowId'] = request.media_workflow_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeactivateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeactivateMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CiphertextBlob'] = request.ciphertext_blob
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Rand'] = request.rand
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DecryptKey',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DecryptKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def decrypt_key_with_options_async(
        self,
        request: mts_20140618_models.DecryptKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DecryptKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CiphertextBlob'] = request.ciphertext_blob
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Rand'] = request.rand
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DecryptKey',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DecryptKeyResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CateId'] = request.cate_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteCategory',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_category_with_options_async(
        self,
        request: mts_20140618_models.DeleteCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CateId'] = request.cate_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteCategory',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteCategoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMCTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMCTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mctemplate_with_options_async(
        self,
        request: mts_20140618_models.DeleteMCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMCTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMCTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMCTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMcuJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMcuJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcu_job_with_options_async(
        self,
        request: mts_20140618_models.DeleteMcuJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMcuJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMcuJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMcuJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMcuTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMcuTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcu_template_with_options_async(
        self,
        request: mts_20140618_models.DeleteMcuTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMcuTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMcuTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMcuTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['MediaIds'] = request.media_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_media_with_options_async(
        self,
        request: mts_20140618_models.DeleteMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MediaIds'] = request.media_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMediaResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMediaTag',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMediaTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_media_tag_with_options_async(
        self,
        request: mts_20140618_models.DeleteMediaTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMediaTagResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMediaTag',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMediaTagResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['MediaWorkflowId'] = request.media_workflow_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.DeleteMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMediaWorkflowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MediaWorkflowId'] = request.media_workflow_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeletePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_with_options_async(
        self,
        request: mts_20140618_models.DeletePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeletePipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeletePipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteSmarttagTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_smarttag_template_with_options_async(
        self,
        request: mts_20140618_models.DeleteSmarttagTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteSmarttagTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteSmarttagTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: mts_20140618_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['WaterMarkTemplateId'] = request.water_mark_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteWaterMarkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_water_mark_template_with_options_async(
        self,
        request: mts_20140618_models.DeleteWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteWaterMarkTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['WaterMarkTemplateId'] = request.water_mark_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DeleteWaterMarkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMtsUserResourcePackage',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DescribeMtsUserResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mts_user_resource_package_with_options_async(
        self,
        request: mts_20140618_models.DescribeMtsUserResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DescribeMtsUserResourcePackageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMtsUserResourcePackage',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DescribeMtsUserResourcePackageResponse(),
            await self.call_api_async(params, req, runtime)
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

    def detect_image_sync_with_options(
        self,
        request: mts_20140618_models.DetectImageSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DetectImageSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Image'] = request.image
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectImageSync',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DetectImageSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_sync_with_options_async(
        self,
        request: mts_20140618_models.DetectImageSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DetectImageSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Image'] = request.image
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectImageSync',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.DetectImageSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_sync(
        self,
        request: mts_20140618_models.DetectImageSyncRequest,
    ) -> mts_20140618_models.DetectImageSyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_image_sync_with_options(request, runtime)

    async def detect_image_sync_async(
        self,
        request: mts_20140618_models.DetectImageSyncRequest,
    ) -> mts_20140618_models.DetectImageSyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_sync_with_options_async(request, runtime)

    def get_job_info_with_options(
        self,
        request: mts_20140618_models.GetJobInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.GetJobInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobInfo',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.GetJobInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_info_with_options_async(
        self,
        request: mts_20140618_models.GetJobInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.GetJobInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobInfo',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.GetJobInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_info(
        self,
        request: mts_20140618_models.GetJobInfoRequest,
    ) -> mts_20140618_models.GetJobInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_info_with_options(request, runtime)

    async def get_job_info_async(
        self,
        request: mts_20140618_models.GetJobInfoRequest,
    ) -> mts_20140618_models.GetJobInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_info_with_options_async(request, runtime)

    def get_license_with_options(
        self,
        request: mts_20140618_models.GetLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.GetLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Data'] = request.data
        query['Header'] = request.header
        query['LicenseUrl'] = request.license_url
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetLicense',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.GetLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_license_with_options_async(
        self,
        request: mts_20140618_models.GetLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.GetLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Data'] = request.data
        query['Header'] = request.header
        query['LicenseUrl'] = request.license_url
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetLicense',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.GetLicenseResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Data'] = request.data
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPackage',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.GetPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_package_with_options_async(
        self,
        request: mts_20140618_models.GetPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.GetPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Data'] = request.data
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetPackage',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.GetPackageResponse(),
            await self.call_api_async(params, req, runtime)
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

    def im_audit_with_options(
        self,
        request: mts_20140618_models.ImAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ImAuditResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BizType'] = request.biz_type
        query['Contents'] = request.contents
        query['Images'] = request.images
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Scenes'] = request.scenes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ImAudit',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ImAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def im_audit_with_options_async(
        self,
        request: mts_20140618_models.ImAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ImAuditResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BizType'] = request.biz_type
        query['Contents'] = request.contents
        query['Images'] = request.images
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Scenes'] = request.scenes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ImAudit',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ImAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def im_audit(
        self,
        request: mts_20140618_models.ImAuditRequest,
    ) -> mts_20140618_models.ImAuditResponse:
        runtime = util_models.RuntimeOptions()
        return self.im_audit_with_options(request, runtime)

    async def im_audit_async(
        self,
        request: mts_20140618_models.ImAuditRequest,
    ) -> mts_20140618_models.ImAuditResponse:
        runtime = util_models.RuntimeOptions()
        return await self.im_audit_with_options_async(request, runtime)

    def import_fp_shot_job_with_options(
        self,
        request: mts_20140618_models.ImportFpShotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ImportFpShotJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FpDBId'] = request.fp_dbid
        query['FpImportConfig'] = request.fp_import_config
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ImportFpShotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ImportFpShotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_fp_shot_job_with_options_async(
        self,
        request: mts_20140618_models.ImportFpShotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ImportFpShotJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FpDBId'] = request.fp_dbid
        query['FpImportConfig'] = request.fp_import_config
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ImportFpShotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ImportFpShotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_fp_shot_job(
        self,
        request: mts_20140618_models.ImportFpShotJobRequest,
    ) -> mts_20140618_models.ImportFpShotJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_fp_shot_job_with_options(request, runtime)

    async def import_fp_shot_job_async(
        self,
        request: mts_20140618_models.ImportFpShotJobRequest,
    ) -> mts_20140618_models.ImportFpShotJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_fp_shot_job_with_options_async(request, runtime)

    def list_all_category_with_options(
        self,
        request: mts_20140618_models.ListAllCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListAllCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAllCategory',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListAllCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_category_with_options_async(
        self,
        request: mts_20140618_models.ListAllCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListAllCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAllCategory',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListAllCategoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAllMediaBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListAllMediaBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_media_bucket_with_options_async(
        self,
        request: mts_20140618_models.ListAllMediaBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListAllMediaBucketResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAllMediaBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListAllMediaBucketResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAsrPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListAsrPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_asr_pipeline_with_options_async(
        self,
        request: mts_20140618_models.ListAsrPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListAsrPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAsrPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListAsrPipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListCensorPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListCensorPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_censor_pipeline_with_options_async(
        self,
        request: mts_20140618_models.ListCensorPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCensorPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListCensorPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListCensorPipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListCoverPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListCoverPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cover_pipeline_with_options_async(
        self,
        request: mts_20140618_models.ListCoverPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCoverPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListCoverPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListCoverPipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CategoryId'] = request.category_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PersonId'] = request.person_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListCustomPersons',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListCustomPersonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_persons_with_options_async(
        self,
        request: mts_20140618_models.ListCustomPersonsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCustomPersonsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CategoryId'] = request.category_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PersonId'] = request.person_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListCustomPersons',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListCustomPersonsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FpDBIds'] = request.fp_dbids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFpShotDB',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListFpShotDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fp_shot_dbwith_options_async(
        self,
        request: mts_20140618_models.ListFpShotDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotDBResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FpDBIds'] = request.fp_dbids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFpShotDB',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListFpShotDBResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FpDBId'] = request.fp_dbid
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFpShotFiles',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListFpShotFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fp_shot_files_with_options_async(
        self,
        request: mts_20140618_models.ListFpShotFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FpDBId'] = request.fp_dbid
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFpShotFiles',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListFpShotFilesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_fp_shot_import_job_with_options(
        self,
        request: mts_20140618_models.ListFpShotImportJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotImportJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFpShotImportJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListFpShotImportJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fp_shot_import_job_with_options_async(
        self,
        request: mts_20140618_models.ListFpShotImportJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotImportJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFpShotImportJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListFpShotImportJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fp_shot_import_job(
        self,
        request: mts_20140618_models.ListFpShotImportJobRequest,
    ) -> mts_20140618_models.ListFpShotImportJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_fp_shot_import_job_with_options(request, runtime)

    async def list_fp_shot_import_job_async(
        self,
        request: mts_20140618_models.ListFpShotImportJobRequest,
    ) -> mts_20140618_models.ListFpShotImportJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_fp_shot_import_job_with_options_async(request, runtime)

    def list_fp_shot_notary_with_options(
        self,
        request: mts_20140618_models.ListFpShotNotaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotNotaryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndOfCreatedTimeRange'] = request.end_of_created_time_range
        query['FpDBId'] = request.fp_dbid
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartOfCreatedTimeRange'] = request.start_of_created_time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFpShotNotary',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListFpShotNotaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fp_shot_notary_with_options_async(
        self,
        request: mts_20140618_models.ListFpShotNotaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListFpShotNotaryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndOfCreatedTimeRange'] = request.end_of_created_time_range
        query['FpDBId'] = request.fp_dbid
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartOfCreatedTimeRange'] = request.start_of_created_time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFpShotNotary',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListFpShotNotaryResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_inference_job_with_options(
        self,
        request: mts_20140618_models.ListInferenceJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListInferenceJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MaxPageSize'] = request.max_page_size
        query['PageNumber'] = request.page_number
        query['ServerName'] = request.server_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListInferenceJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListInferenceJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_inference_job_with_options_async(
        self,
        request: mts_20140618_models.ListInferenceJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListInferenceJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MaxPageSize'] = request.max_page_size
        query['PageNumber'] = request.page_number
        query['ServerName'] = request.server_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListInferenceJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListInferenceJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_inference_job(
        self,
        request: mts_20140618_models.ListInferenceJobRequest,
    ) -> mts_20140618_models.ListInferenceJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_inference_job_with_options(request, runtime)

    async def list_inference_job_async(
        self,
        request: mts_20140618_models.ListInferenceJobRequest,
    ) -> mts_20140618_models.ListInferenceJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_inference_job_with_options_async(request, runtime)

    def list_job_with_options(
        self,
        request: mts_20140618_models.ListJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_with_options_async(
        self,
        request: mts_20140618_models.ListJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['From'] = request.from_
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_media_with_options_async(
        self,
        request: mts_20140618_models.ListMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['From'] = request.from_
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListMediaResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InputFileURL'] = request.input_file_url
        query['MaximumPageSize'] = request.maximum_page_size
        query['MediaWorkflowId'] = request.media_workflow_id
        query['MediaWorkflowName'] = request.media_workflow_name
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListMediaWorkflowExecutions',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListMediaWorkflowExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_media_workflow_executions_with_options_async(
        self,
        request: mts_20140618_models.ListMediaWorkflowExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListMediaWorkflowExecutionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InputFileURL'] = request.input_file_url
        query['MaximumPageSize'] = request.maximum_page_size
        query['MediaWorkflowId'] = request.media_workflow_id
        query['MediaWorkflowName'] = request.media_workflow_name
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListMediaWorkflowExecutions',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListMediaWorkflowExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPornPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListPornPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_porn_pipeline_with_options_async(
        self,
        request: mts_20140618_models.ListPornPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListPornPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPornPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListPornPipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTerrorismPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListTerrorismPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_terrorism_pipeline_with_options_async(
        self,
        request: mts_20140618_models.ListTerrorismPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListTerrorismPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTerrorismPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ListTerrorismPipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Bid'] = request.bid
        query['Country'] = request.country
        query['GmtWakeup'] = request.gmt_wakeup
        query['Hid'] = request.hid
        query['Interrupt'] = request.interrupt
        query['Invoker'] = request.invoker
        query['Message'] = request.message
        query['Pk'] = request.pk
        query['Success'] = request.success
        query['TaskExtraData'] = request.task_extra_data
        query['TaskIdentifier'] = request.task_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='LogicalDeleteResource',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.LogicalDeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def logical_delete_resource_with_options_async(
        self,
        request: mts_20140618_models.LogicalDeleteResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.LogicalDeleteResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Bid'] = request.bid
        query['Country'] = request.country
        query['GmtWakeup'] = request.gmt_wakeup
        query['Hid'] = request.hid
        query['Interrupt'] = request.interrupt
        query['Invoker'] = request.invoker
        query['Message'] = request.message
        query['Pk'] = request.pk
        query['Success'] = request.success
        query['TaskExtraData'] = request.task_extra_data
        query['TaskIdentifier'] = request.task_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='LogicalDeleteResource',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.LogicalDeleteResourceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Bid'] = request.bid
        query['Country'] = request.country
        query['GmtWakeup'] = request.gmt_wakeup
        query['Hid'] = request.hid
        query['Interrupt'] = request.interrupt
        query['Invoker'] = request.invoker
        query['Message'] = request.message
        query['Pk'] = request.pk
        query['Success'] = request.success
        query['TaskExtraData'] = request.task_extra_data
        query['TaskIdentifier'] = request.task_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PhysicalDeleteResource',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.PhysicalDeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def physical_delete_resource_with_options_async(
        self,
        request: mts_20140618_models.PhysicalDeleteResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.PhysicalDeleteResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Bid'] = request.bid
        query['Country'] = request.country
        query['GmtWakeup'] = request.gmt_wakeup
        query['Hid'] = request.hid
        query['Interrupt'] = request.interrupt
        query['Invoker'] = request.invoker
        query['Message'] = request.message
        query['Pk'] = request.pk
        query['Success'] = request.success
        query['TaskExtraData'] = request.task_extra_data
        query['TaskIdentifier'] = request.task_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PhysicalDeleteResource',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.PhysicalDeleteResourceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def play_info_with_options(
        self,
        request: mts_20140618_models.PlayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.PlayInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AuthInfo'] = request.auth_info
        query['AuthTimeout'] = request.auth_timeout
        query['Formats'] = request.formats
        query['HlsUriToken'] = request.hls_uri_token
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PlayDomain'] = request.play_domain
        query['Rand'] = request.rand
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Terminal'] = request.terminal
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PlayInfo',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.PlayInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def play_info_with_options_async(
        self,
        request: mts_20140618_models.PlayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.PlayInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AuthInfo'] = request.auth_info
        query['AuthTimeout'] = request.auth_timeout
        query['Formats'] = request.formats
        query['HlsUriToken'] = request.hls_uri_token
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PlayDomain'] = request.play_domain
        query['Rand'] = request.rand
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Terminal'] = request.terminal
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PlayInfo',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.PlayInfoResponse(),
            await self.call_api_async(params, req, runtime)
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

    def player_auth_with_options(
        self,
        request: mts_20140618_models.PlayerAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.PlayerAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PlayerAuth',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.PlayerAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def player_auth_with_options_async(
        self,
        request: mts_20140618_models.PlayerAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.PlayerAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PlayerAuth',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.PlayerAuthResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_analysis_job_list_with_options(
        self,
        request: mts_20140618_models.QueryAnalysisJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAnalysisJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AnalysisJobIds'] = request.analysis_job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAnalysisJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryAnalysisJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_analysis_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryAnalysisJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAnalysisJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AnalysisJobIds'] = request.analysis_job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAnalysisJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryAnalysisJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AnnotationJobIds'] = request.annotation_job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAnnotationJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryAnnotationJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_annotation_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryAnnotationJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAnnotationJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AnnotationJobIds'] = request.annotation_job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAnnotationJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryAnnotationJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAsrJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryAsrJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_asr_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryAsrJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAsrJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAsrJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryAsrJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineIds'] = request.pipeline_ids
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAsrPipelineList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryAsrPipelineListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_asr_pipeline_list_with_options_async(
        self,
        request: mts_20140618_models.QueryAsrPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAsrPipelineListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineIds'] = request.pipeline_ids
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAsrPipelineList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryAsrPipelineListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAuthConfig',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryAuthConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_auth_config_with_options_async(
        self,
        request: mts_20140618_models.QueryAuthConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAuthConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryAuthConfig',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryAuthConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCensorJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryCensorJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_censor_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryCensorJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryCensorJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCensorJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryCensorJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineIds'] = request.pipeline_ids
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCensorPipelineList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryCensorPipelineListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_censor_pipeline_list_with_options_async(
        self,
        request: mts_20140618_models.QueryCensorPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryCensorPipelineListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineIds'] = request.pipeline_ids
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCensorPipelineList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryCensorPipelineListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryComplexJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryComplexJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_complex_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryComplexJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryComplexJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryComplexJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryComplexJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CoverJobIds'] = request.cover_job_ids
        query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCoverJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryCoverJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cover_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryCoverJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryCoverJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CoverJobIds'] = request.cover_job_ids
        query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCoverJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryCoverJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineIds'] = request.pipeline_ids
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCoverPipelineList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryCoverPipelineListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cover_pipeline_list_with_options_async(
        self,
        request: mts_20140618_models.QueryCoverPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryCoverPipelineListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineIds'] = request.pipeline_ids
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryCoverPipelineList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryCoverPipelineListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryEditingJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryEditingJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_editing_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryEditingJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryEditingJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryEditingJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryEditingJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FacerecogJobIds'] = request.facerecog_job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFacerecogJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFacerecogJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_facerecog_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryFacerecogJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFacerecogJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FacerecogJobIds'] = request.facerecog_job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFacerecogJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFacerecogJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFpCompareJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFpCompareJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fp_compare_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryFpCompareJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpCompareJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFpCompareJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFpCompareJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFpDBDeleteJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFpDBDeleteJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fp_dbdelete_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryFpDBDeleteJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpDBDeleteJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFpDBDeleteJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFpDBDeleteJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFpFileDeleteJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFpFileDeleteJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fp_file_delete_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryFpFileDeleteJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpFileDeleteJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFpFileDeleteJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFpFileDeleteJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['EndTime'] = request.end_time
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageIndex'] = request.page_index
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFpImportResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFpImportResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fp_import_result_with_options_async(
        self,
        request: mts_20140618_models.QueryFpImportResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpImportResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageIndex'] = request.page_index
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFpImportResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFpImportResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        query['JobIds'] = request.job_ids
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['PrimaryKeyList'] = request.primary_key_list
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        query['State'] = request.state
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFpShotJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFpShotJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fp_shot_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryFpShotJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpShotJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        query['JobIds'] = request.job_ids
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['PrimaryKeyList'] = request.primary_key_list
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        query['State'] = request.state
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryFpShotJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryFpShotJobListResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_iproduction_job_with_options(
        self,
        request: mts_20140618_models.QueryIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryIProductionJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryIProductionJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryIProductionJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_iproduction_job_with_options_async(
        self,
        request: mts_20140618_models.QueryIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryIProductionJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryIProductionJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryIProductionJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['IProductionJobIds'] = request.iproduction_job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryIProductionJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryIProductionJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_iproduction_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryIProductionJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryIProductionJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IProductionJobIds'] = request.iproduction_job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryIProductionJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryIProductionJobListResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_image_search_job_list_with_options(
        self,
        request: mts_20140618_models.QueryImageSearchJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryImageSearchJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryImageSearchJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryImageSearchJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_image_search_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryImageSearchJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryImageSearchJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryImageSearchJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryImageSearchJobListResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_inference_job_with_options(
        self,
        request: mts_20140618_models.QueryInferenceJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryInferenceJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryInferenceJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryInferenceJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_inference_job_with_options_async(
        self,
        request: mts_20140618_models.QueryInferenceJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryInferenceJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryInferenceJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryInferenceJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_inference_job(
        self,
        request: mts_20140618_models.QueryInferenceJobRequest,
    ) -> mts_20140618_models.QueryInferenceJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_inference_job_with_options(request, runtime)

    async def query_inference_job_async(
        self,
        request: mts_20140618_models.QueryInferenceJobRequest,
    ) -> mts_20140618_models.QueryInferenceJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_inference_job_with_options_async(request, runtime)

    def query_inference_server_with_options(
        self,
        request: mts_20140618_models.QueryInferenceServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryInferenceServerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CreateTime'] = request.create_time
        query['MaxPageSize'] = request.max_page_size
        query['ModelType'] = request.model_type
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryInferenceServer',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryInferenceServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_inference_server_with_options_async(
        self,
        request: mts_20140618_models.QueryInferenceServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryInferenceServerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CreateTime'] = request.create_time
        query['MaxPageSize'] = request.max_page_size
        query['ModelType'] = request.model_type
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryInferenceServer',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryInferenceServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_inference_server(
        self,
        request: mts_20140618_models.QueryInferenceServerRequest,
    ) -> mts_20140618_models.QueryInferenceServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_inference_server_with_options(request, runtime)

    async def query_inference_server_async(
        self,
        request: mts_20140618_models.QueryInferenceServerRequest,
    ) -> mts_20140618_models.QueryInferenceServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_inference_server_with_options_async(request, runtime)

    def query_inner_job_with_options(
        self,
        request: mts_20140618_models.QueryInnerJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryInnerJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryInnerJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryInnerJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_inner_job_with_options_async(
        self,
        request: mts_20140618_models.QueryInnerJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryInnerJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryInnerJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryInnerJobResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_job_list_with_options(
        self,
        request: mts_20140618_models.QueryJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        query['JobIds'] = request.job_ids
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMCJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMCJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mcjob_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMCJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMCJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        query['JobIds'] = request.job_ids
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMCJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMCJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMCTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMCTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mctemplate_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMCTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMCTemplateListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMCTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMCTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMcuJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMcuJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mcu_job_with_options_async(
        self,
        request: mts_20140618_models.QueryMcuJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMcuJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMcuJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMcuJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMcuTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMcuTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mcu_template_with_options_async(
        self,
        request: mts_20140618_models.QueryMcuTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMcuTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMcuTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMcuTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobId'] = request.job_id
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaCensorJobDetail',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaCensorJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_censor_job_detail_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaCensorJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaCensorJobDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaCensorJobDetail',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaCensorJobDetailResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        query['JobId'] = request.job_id
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaCensorJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaCensorJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_censor_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaCensorJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaCensorJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        query['JobId'] = request.job_id
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaCensorJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaCensorJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaDetailJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaDetailJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_detail_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaDetailJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaDetailJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaDetailJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaDetailJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaFpDeleteJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaFpDeleteJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_fp_delete_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaFpDeleteJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaFpDeleteJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaFpDeleteJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaFpDeleteJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['MediaInfoJobIds'] = request.media_info_job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaInfoJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaInfoJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_info_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaInfoJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaInfoJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MediaInfoJobIds'] = request.media_info_job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaInfoJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaInfoJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['IncludeMediaInfo'] = request.include_media_info
        query['IncludePlayList'] = request.include_play_list
        query['IncludeSnapshotList'] = request.include_snapshot_list
        query['IncludeSummaryList'] = request.include_summary_list
        query['MediaIds'] = request.media_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IncludeMediaInfo'] = request.include_media_info
        query['IncludePlayList'] = request.include_play_list
        query['IncludeSnapshotList'] = request.include_snapshot_list
        query['IncludeSummaryList'] = request.include_summary_list
        query['MediaIds'] = request.media_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileURLs'] = request.file_urls
        query['IncludeMediaInfo'] = request.include_media_info
        query['IncludePlayList'] = request.include_play_list
        query['IncludeSnapshotList'] = request.include_snapshot_list
        query['IncludeSummaryList'] = request.include_summary_list
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaListByURL',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaListByURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_list_by_urlwith_options_async(
        self,
        request: mts_20140618_models.QueryMediaListByURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaListByURLResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileURLs'] = request.file_urls
        query['IncludeMediaInfo'] = request.include_media_info
        query['IncludePlayList'] = request.include_play_list
        query['IncludeSnapshotList'] = request.include_snapshot_list
        query['IncludeSummaryList'] = request.include_summary_list
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaListByURL',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaListByURLResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RunIds'] = request.run_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaWorkflowExecutionList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaWorkflowExecutionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_workflow_execution_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaWorkflowExecutionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaWorkflowExecutionListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RunIds'] = request.run_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaWorkflowExecutionList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaWorkflowExecutionListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['MediaWorkflowIds'] = request.media_workflow_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaWorkflowList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaWorkflowListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_workflow_list_with_options_async(
        self,
        request: mts_20140618_models.QueryMediaWorkflowListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaWorkflowListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MediaWorkflowIds'] = request.media_workflow_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryMediaWorkflowList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryMediaWorkflowListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineIds'] = request.pipeline_ids
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPipelineList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryPipelineListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_pipeline_list_with_options_async(
        self,
        request: mts_20140618_models.QueryPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryPipelineListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineIds'] = request.pipeline_ids
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPipelineList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryPipelineListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPornJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryPornJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_porn_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryPornJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryPornJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPornJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryPornJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineIds'] = request.pipeline_ids
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPornPipelineList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryPornPipelineListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_porn_pipeline_list_with_options_async(
        self,
        request: mts_20140618_models.QueryPornPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryPornPipelineListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineIds'] = request.pipeline_ids
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryPornPipelineList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryPornPipelineListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Params'] = request.params
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QuerySmarttagJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QuerySmarttagJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_smarttag_job_with_options_async(
        self,
        request: mts_20140618_models.QuerySmarttagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySmarttagJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Params'] = request.params
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QuerySmarttagJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QuerySmarttagJobResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_smarttag_job_list_with_options(
        self,
        request: mts_20140618_models.QuerySmarttagJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySmarttagJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        query['JobIds'] = request.job_ids
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QuerySmarttagJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QuerySmarttagJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_smarttag_job_list_with_options_async(
        self,
        request: mts_20140618_models.QuerySmarttagJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySmarttagJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        query['JobIds'] = request.job_ids
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QuerySmarttagJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QuerySmarttagJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_smarttag_job_list(
        self,
        request: mts_20140618_models.QuerySmarttagJobListRequest,
    ) -> mts_20140618_models.QuerySmarttagJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_smarttag_job_list_with_options(request, runtime)

    async def query_smarttag_job_list_async(
        self,
        request: mts_20140618_models.QuerySmarttagJobListRequest,
    ) -> mts_20140618_models.QuerySmarttagJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_smarttag_job_list_with_options_async(request, runtime)

    def query_smarttag_template_list_with_options(
        self,
        request: mts_20140618_models.QuerySmarttagTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySmarttagTemplateListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QuerySmarttagTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QuerySmarttagTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_smarttag_template_list_with_options_async(
        self,
        request: mts_20140618_models.QuerySmarttagTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySmarttagTemplateListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QuerySmarttagTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QuerySmarttagTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SnapshotJobIds'] = request.snapshot_job_ids
        query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QuerySnapshotJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QuerySnapshotJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_snapshot_job_list_with_options_async(
        self,
        request: mts_20140618_models.QuerySnapshotJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySnapshotJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        query['MaximumPageSize'] = request.maximum_page_size
        query['NextPageToken'] = request.next_page_token
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SnapshotJobIds'] = request.snapshot_job_ids
        query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QuerySnapshotJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QuerySnapshotJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QuerySubtitleJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QuerySubtitleJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_subtitle_job_list_with_options_async(
        self,
        request: mts_20140618_models.QuerySubtitleJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySubtitleJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QuerySubtitleJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QuerySubtitleJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TagJobIds'] = request.tag_job_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryTagJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryTagJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tag_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryTagJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryTagJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TagJobIds'] = request.tag_job_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryTagJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryTagJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_template_list_with_options_async(
        self,
        request: mts_20140618_models.QueryTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryTemplateListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryTerrorismJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryTerrorismJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_terrorism_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryTerrorismJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryTerrorismJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryTerrorismJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryTerrorismJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineIds'] = request.pipeline_ids
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryTerrorismPipelineList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryTerrorismPipelineListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_terrorism_pipeline_list_with_options_async(
        self,
        request: mts_20140618_models.QueryTerrorismPipelineListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryTerrorismPipelineListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineIds'] = request.pipeline_ids
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryTerrorismPipelineList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryTerrorismPipelineListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryVideoGifJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryVideoGifJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_video_gif_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryVideoGifJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryVideoGifJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryVideoGifJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryVideoGifJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryVideoPoseJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryVideoPoseJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_video_pose_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryVideoPoseJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryVideoPoseJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryVideoPoseJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryVideoPoseJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryVideoQualityJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryVideoQualityJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_video_quality_job_with_options_async(
        self,
        request: mts_20140618_models.QueryVideoQualityJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryVideoQualityJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryVideoQualityJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryVideoQualityJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryVideoSplitJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryVideoSplitJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_video_split_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryVideoSplitJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryVideoSplitJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryVideoSplitJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryVideoSplitJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryVideoSummaryJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryVideoSummaryJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_video_summary_job_list_with_options_async(
        self,
        request: mts_20140618_models.QueryVideoSummaryJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryVideoSummaryJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobIds'] = request.job_ids
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryVideoSummaryJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryVideoSummaryJobListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['WaterMarkTemplateIds'] = request.water_mark_template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryWaterMarkTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryWaterMarkTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_water_mark_template_list_with_options_async(
        self,
        request: mts_20140618_models.QueryWaterMarkTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryWaterMarkTemplateListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['WaterMarkTemplateIds'] = request.water_mark_template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryWaterMarkTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.QueryWaterMarkTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Domains'] = request.domains
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RefreshCdnDomainConfigsCache',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.RefreshCdnDomainConfigsCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_cdn_domain_configs_cache_with_options_async(
        self,
        request: mts_20140618_models.RefreshCdnDomainConfigsCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.RefreshCdnDomainConfigsCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Domains'] = request.domains
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RefreshCdnDomainConfigsCache',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.RefreshCdnDomainConfigsCacheResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CategoryId'] = request.category_id
        query['ImageUrl'] = request.image_url
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PersonId'] = request.person_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RegisterCustomFace',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.RegisterCustomFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_custom_face_with_options_async(
        self,
        request: mts_20140618_models.RegisterCustomFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.RegisterCustomFaceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CategoryId'] = request.category_id
        query['ImageUrl'] = request.image_url
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PersonId'] = request.person_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RegisterCustomFace',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.RegisterCustomFaceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Category'] = request.category
        query['Images'] = request.images
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PersonLib'] = request.person_lib
        query['PersonName'] = request.person_name
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RegisterMediaDetailPerson',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.RegisterMediaDetailPersonResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_media_detail_person_with_options_async(
        self,
        request: mts_20140618_models.RegisterMediaDetailPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.RegisterMediaDetailPersonResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Category'] = request.category
        query['Images'] = request.images
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PersonLib'] = request.person_lib
        query['PersonName'] = request.person_name
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RegisterMediaDetailPerson',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.RegisterMediaDetailPersonResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Description'] = request.description
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Scenario'] = request.scenario
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RegisterMediaDetailScenario',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.RegisterMediaDetailScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_media_detail_scenario_with_options_async(
        self,
        request: mts_20140618_models.RegisterMediaDetailScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.RegisterMediaDetailScenarioResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Scenario'] = request.scenario
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RegisterMediaDetailScenario',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.RegisterMediaDetailScenarioResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Annotation'] = request.annotation
        query['Details'] = request.details
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportAnnotationJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportAnnotationJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_annotation_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportAnnotationJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportAnnotationJobResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Annotation'] = request.annotation
        query['Details'] = request.details
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportAnnotationJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportAnnotationJobResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Detail'] = request.detail
        query['JobId'] = request.job_id
        query['Label'] = request.label
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportCensorJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportCensorJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_censor_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportCensorJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportCensorJobResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Detail'] = request.detail
        query['JobId'] = request.job_id
        query['Label'] = request.label
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportCensorJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportCensorJobResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Result'] = request.result
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportCoverJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportCoverJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_cover_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportCoverJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportCoverJobResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Result'] = request.result
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportCoverJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportCoverJobResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Details'] = request.details
        query['Facerecog'] = request.facerecog
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportFacerecogJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportFacerecogJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_facerecog_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportFacerecogJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportFacerecogJobResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Details'] = request.details
        query['Facerecog'] = request.facerecog
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportFacerecogJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportFacerecogJobResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Details'] = request.details
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Result'] = request.result
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportFpShotJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportFpShotJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_fp_shot_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportFpShotJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportFpShotJobResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Details'] = request.details
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Result'] = request.result
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportFpShotJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportFpShotJobResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Results'] = request.results
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportMediaDetailJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportMediaDetailJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_media_detail_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportMediaDetailJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportMediaDetailJobResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Results'] = request.results
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportMediaDetailJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportMediaDetailJobResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Detail'] = request.detail
        query['JobId'] = request.job_id
        query['Label'] = request.label
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportPornJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportPornJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_porn_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportPornJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportPornJobResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Detail'] = request.detail
        query['JobId'] = request.job_id
        query['Label'] = request.label
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportPornJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportPornJobResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Result'] = request.result
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportTagJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportTagJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_tag_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportTagJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportTagJobResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Result'] = request.result
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportTagJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportTagJobResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Detail'] = request.detail
        query['JobId'] = request.job_id
        query['Label'] = request.label
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportTerrorismJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportTerrorismJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_terrorism_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportTerrorismJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportTerrorismJobResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Detail'] = request.detail
        query['JobId'] = request.job_id
        query['Label'] = request.label
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportTerrorismJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportTerrorismJobResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Details'] = request.details
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Result'] = request.result
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportVideoSplitJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportVideoSplitJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_video_split_job_result_with_options_async(
        self,
        request: mts_20140618_models.ReportVideoSplitJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportVideoSplitJobResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Details'] = request.details
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Result'] = request.result
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReportVideoSplitJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.ReportVideoSplitJobResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CateId'] = request.cate_id
        query['Description'] = request.description
        query['From'] = request.from_
        query['KeyWord'] = request.key_word
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SortBy'] = request.sort_by
        query['Tag'] = request.tag
        query['Title'] = request.title
        query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_media_with_options_async(
        self,
        request: mts_20140618_models.SearchMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CateId'] = request.cate_id
        query['Description'] = request.description
        query['From'] = request.from_
        query['KeyWord'] = request.key_word
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SortBy'] = request.sort_by
        query['Tag'] = request.tag
        query['Title'] = request.title
        query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchMediaResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StateList'] = request.state_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.SearchMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchMediaWorkflowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StateList'] = request.state_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_pipeline_with_options_async(
        self,
        request: mts_20140618_models.SearchPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchPipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_template_with_options_async(
        self,
        request: mts_20140618_models.SearchTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchWaterMarkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_water_mark_template_with_options_async(
        self,
        request: mts_20140618_models.SearchWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchWaterMarkTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SearchWaterMarkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Key1'] = request.key_1
        query['Key2'] = request.key_2
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetAuthConfig',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SetAuthConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_auth_config_with_options_async(
        self,
        request: mts_20140618_models.SetAuthConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SetAuthConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Key1'] = request.key_1
        query['Key2'] = request.key_2
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetAuthConfig',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SetAuthConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopIProductionJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.StopIProductionJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_iproduction_job_with_options_async(
        self,
        request: mts_20140618_models.StopIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.StopIProductionJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopIProductionJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.StopIProductionJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AnalysisConfig'] = request.analysis_config
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitAnalysisJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitAnalysisJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_analysis_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitAnalysisJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AnalysisConfig'] = request.analysis_config
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitAnalysisJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitAnalysisJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AnnotationConfig'] = request.annotation_config
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitAnnotationJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitAnnotationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_annotation_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitAnnotationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitAnnotationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AnnotationConfig'] = request.annotation_config
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitAnnotationJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitAnnotationJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AsrConfig'] = request.asr_config
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitAsrJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitAsrJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_asr_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitAsrJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitAsrJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AsrConfig'] = request.asr_config
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitAsrJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitAsrJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Async'] = request.async_
        query['BeautifyConfig'] = request.beautify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitBeautifyJobs',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitBeautifyJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_beautify_jobs_with_options_async(
        self,
        request: mts_20140618_models.SubmitBeautifyJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitBeautifyJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Async'] = request.async_
        query['BeautifyConfig'] = request.beautify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitBeautifyJobs',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitBeautifyJobsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ComplexConfigs'] = request.complex_configs
        query['Inputs'] = request.inputs
        query['OutputBucket'] = request.output_bucket
        query['OutputLocation'] = request.output_location
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TranscodeOutput'] = request.transcode_output
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitComplexJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitComplexJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_complex_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitComplexJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitComplexJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ComplexConfigs'] = request.complex_configs
        query['Inputs'] = request.inputs
        query['OutputBucket'] = request.output_bucket
        query['OutputLocation'] = request.output_location
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TranscodeOutput'] = request.transcode_output
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitComplexJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitComplexJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CoverConfig'] = request.cover_config
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitCoverJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitCoverJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_cover_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitCoverJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitCoverJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CoverConfig'] = request.cover_config
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitCoverJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitCoverJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['EditingInputs'] = request.editing_inputs
        query['EditingJobOssFileRoleArn'] = request.editing_job_oss_file_role_arn
        query['EditingJobOssFileUid'] = request.editing_job_oss_file_uid
        query['EditingJobOutputs'] = request.editing_job_outputs
        query['EditingJobURL'] = request.editing_job_url
        query['OutputBucket'] = request.output_bucket
        query['OutputLocation'] = request.output_location
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitEditingJobs',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitEditingJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_editing_jobs_with_options_async(
        self,
        request: mts_20140618_models.SubmitEditingJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitEditingJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EditingInputs'] = request.editing_inputs
        query['EditingJobOssFileRoleArn'] = request.editing_job_oss_file_role_arn
        query['EditingJobOssFileUid'] = request.editing_job_oss_file_uid
        query['EditingJobOutputs'] = request.editing_job_outputs
        query['EditingJobURL'] = request.editing_job_url
        query['OutputBucket'] = request.output_bucket
        query['OutputLocation'] = request.output_location
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitEditingJobs',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitEditingJobsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FacerecogConfig'] = request.facerecog_config
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitFacerecogJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitFacerecogJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_facerecog_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitFacerecogJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFacerecogJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FacerecogConfig'] = request.facerecog_config
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitFacerecogJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitFacerecogJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FpDBId'] = request.fp_dbid
        query['MasterMedia'] = request.master_media
        query['MatchedFrameStorage'] = request.matched_frame_storage
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['QueryMedia'] = request.query_media
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitFpCompareJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitFpCompareJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_fp_compare_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitFpCompareJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpCompareJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FpDBId'] = request.fp_dbid
        query['MasterMedia'] = request.master_media
        query['MatchedFrameStorage'] = request.matched_frame_storage
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['QueryMedia'] = request.query_media
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitFpCompareJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitFpCompareJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['DelType'] = request.del_type
        query['FpDBId'] = request.fp_dbid
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitFpDBDeleteJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitFpDBDeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_fp_dbdelete_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitFpDBDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpDBDeleteJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DelType'] = request.del_type
        query['FpDBId'] = request.fp_dbid
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitFpDBDeleteJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitFpDBDeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FileIds'] = request.file_ids
        query['FpDBId'] = request.fp_dbid
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitFpFileDeleteJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitFpFileDeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_fp_file_delete_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitFpFileDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpFileDeleteJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileIds'] = request.file_ids
        query['FpDBId'] = request.fp_dbid
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitFpFileDeleteJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitFpFileDeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FpShotConfig'] = request.fp_shot_config
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitFpShotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitFpShotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_fp_shot_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitFpShotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpShotJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FpShotConfig'] = request.fp_shot_config
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitFpShotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitFpShotJobResponse(),
            await self.call_api_async(params, req, runtime)
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

    def submit_iproduction_job_with_options(
        self,
        request: mts_20140618_models.SubmitIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitIProductionJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FunctionName'] = request.function_name
        query['Input'] = request.input
        query['JobParams'] = request.job_params
        query['ModelId'] = request.model_id
        query['NotifyUrl'] = request.notify_url
        query['Output'] = request.output
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ScheduleParams'] = request.schedule_params
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitIProductionJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitIProductionJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_iproduction_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitIProductionJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FunctionName'] = request.function_name
        query['Input'] = request.input
        query['JobParams'] = request.job_params
        query['ModelId'] = request.model_id
        query['NotifyUrl'] = request.notify_url
        query['Output'] = request.output
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ScheduleParams'] = request.schedule_params
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitIProductionJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitIProductionJobResponse(),
            await self.call_api_async(params, req, runtime)
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

    def submit_image_quality_job_with_options(
        self,
        request: mts_20140618_models.SubmitImageQualityJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitImageQualityJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitImageQualityJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitImageQualityJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_image_quality_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitImageQualityJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitImageQualityJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitImageQualityJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitImageQualityJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Config'] = request.config
        query['FpDBId'] = request.fp_dbid
        query['InputImage'] = request.input_image
        query['InputVideo'] = request.input_video
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitImageSearchJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitImageSearchJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_image_search_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitImageSearchJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitImageSearchJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Config'] = request.config
        query['FpDBId'] = request.fp_dbid
        query['InputImage'] = request.input_image
        query['InputVideo'] = request.input_video
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitImageSearchJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitImageSearchJobResponse(),
            await self.call_api_async(params, req, runtime)
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

    def submit_inference_job_with_options(
        self,
        request: mts_20140618_models.SubmitInferenceJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitInferenceJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['ModelType'] = request.model_type
        query['ServerName'] = request.server_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitInferenceJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitInferenceJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_inference_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitInferenceJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitInferenceJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['ModelType'] = request.model_type
        query['ServerName'] = request.server_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitInferenceJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitInferenceJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_inference_job(
        self,
        request: mts_20140618_models.SubmitInferenceJobRequest,
    ) -> mts_20140618_models.SubmitInferenceJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_inference_job_with_options(request, runtime)

    async def submit_inference_job_async(
        self,
        request: mts_20140618_models.SubmitInferenceJobRequest,
    ) -> mts_20140618_models.SubmitInferenceJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_inference_job_with_options_async(request, runtime)

    def submit_inner_job_with_options(
        self,
        request: mts_20140618_models.SubmitInnerJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitInnerJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Config'] = request.config
        query['Images'] = request.images
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Uid'] = request.uid
        query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitInnerJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitInnerJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_inner_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitInnerJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitInnerJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Config'] = request.config
        query['Images'] = request.images
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Uid'] = request.uid
        query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitInnerJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitInnerJobResponse(),
            await self.call_api_async(params, req, runtime)
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

    def submit_jobs_with_options(
        self,
        request: mts_20140618_models.SubmitJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['OutputBucket'] = request.output_bucket
        query['OutputLocation'] = request.output_location
        query['Outputs'] = request.outputs
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitJobs',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_jobs_with_options_async(
        self,
        request: mts_20140618_models.SubmitJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['OutputBucket'] = request.output_bucket
        query['OutputLocation'] = request.output_location
        query['Outputs'] = request.outputs
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitJobs',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitJobsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CensorConfig'] = request.censor_config
        query['Images'] = request.images
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Texts'] = request.texts
        query['UserData'] = request.user_data
        query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitMCJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitMCJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_mcjob_with_options_async(
        self,
        request: mts_20140618_models.SubmitMCJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMCJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CensorConfig'] = request.censor_config
        query['Images'] = request.images
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Texts'] = request.texts
        query['UserData'] = request.user_data
        query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitMCJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitMCJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Template'] = request.template
        query['TemplateId'] = request.template_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitMcuJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitMcuJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_mcu_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitMcuJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMcuJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Template'] = request.template
        query['TemplateId'] = request.template_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitMcuJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitMcuJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Barrages'] = request.barrages
        query['CoverImages'] = request.cover_images
        query['Description'] = request.description
        query['ExternalUrl'] = request.external_url
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Title'] = request.title
        query['UserData'] = request.user_data
        query['VideoCensorConfig'] = request.video_censor_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitMediaCensorJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitMediaCensorJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_media_censor_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitMediaCensorJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaCensorJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Barrages'] = request.barrages
        query['CoverImages'] = request.cover_images
        query['Description'] = request.description
        query['ExternalUrl'] = request.external_url
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Title'] = request.title
        query['UserData'] = request.user_data
        query['VideoCensorConfig'] = request.video_censor_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitMediaCensorJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitMediaCensorJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Input'] = request.input
        query['MediaDetailConfig'] = request.media_detail_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitMediaDetailJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitMediaDetailJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_media_detail_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitMediaDetailJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaDetailJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['MediaDetailConfig'] = request.media_detail_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitMediaDetailJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitMediaDetailJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['FpDBId'] = request.fp_dbid
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['PrimaryKey'] = request.primary_key
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitMediaFpDeleteJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitMediaFpDeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_media_fp_delete_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitMediaFpDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaFpDeleteJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FpDBId'] = request.fp_dbid
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['PrimaryKey'] = request.primary_key
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitMediaFpDeleteJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitMediaFpDeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Async'] = request.async_
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitMediaInfoJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitMediaInfoJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_media_info_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitMediaInfoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaInfoJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Async'] = request.async_
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitMediaInfoJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitMediaInfoJobResponse(),
            await self.call_api_async(params, req, runtime)
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

    def submit_oss_file_copy_job_with_options(
        self,
        tmp_req: mts_20140618_models.SubmitOssFileCopyJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitOssFileCopyJobResponse:
        UtilClient.validate_model(tmp_req)
        request = mts_20140618_models.SubmitOssFileCopyJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_storage):
            request.source_storage_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.source_storage), 'SourceStorage', 'json')
        if not UtilClient.is_unset(tmp_req.target_storage):
            request.target_storage_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.target_storage), 'TargetStorage', 'json')
        query = {}
        query['Notify'] = request.notify
        query['Region'] = request.region
        query['SourceStorage'] = request.source_storage_shrink
        query['TargetStorage'] = request.target_storage_shrink
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitOssFileCopyJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitOssFileCopyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_oss_file_copy_job_with_options_async(
        self,
        tmp_req: mts_20140618_models.SubmitOssFileCopyJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitOssFileCopyJobResponse:
        UtilClient.validate_model(tmp_req)
        request = mts_20140618_models.SubmitOssFileCopyJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_storage):
            request.source_storage_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.source_storage), 'SourceStorage', 'json')
        if not UtilClient.is_unset(tmp_req.target_storage):
            request.target_storage_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.target_storage), 'TargetStorage', 'json')
        query = {}
        query['Notify'] = request.notify
        query['Region'] = request.region
        query['SourceStorage'] = request.source_storage_shrink
        query['TargetStorage'] = request.target_storage_shrink
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitOssFileCopyJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitOssFileCopyJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_oss_file_copy_job(
        self,
        request: mts_20140618_models.SubmitOssFileCopyJobRequest,
    ) -> mts_20140618_models.SubmitOssFileCopyJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_oss_file_copy_job_with_options(request, runtime)

    async def submit_oss_file_copy_job_async(
        self,
        request: mts_20140618_models.SubmitOssFileCopyJobRequest,
    ) -> mts_20140618_models.SubmitOssFileCopyJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_oss_file_copy_job_with_options_async(request, runtime)

    def submit_porn_job_with_options(
        self,
        request: mts_20140618_models.SubmitPornJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitPornJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['PornConfig'] = request.porn_config
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitPornJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitPornJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_porn_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitPornJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitPornJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['PornConfig'] = request.porn_config
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitPornJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitPornJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Content'] = request.content
        query['ContentAddr'] = request.content_addr
        query['ContentType'] = request.content_type
        query['Input'] = request.input
        query['NotifyUrl'] = request.notify_url
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Params'] = request.params
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        query['Title'] = request.title
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitSmarttagJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitSmarttagJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_smarttag_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitSmarttagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitSmarttagJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Content'] = request.content
        query['ContentAddr'] = request.content_addr
        query['ContentType'] = request.content_type
        query['Input'] = request.input
        query['NotifyUrl'] = request.notify_url
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Params'] = request.params
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        query['Title'] = request.title
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitSmarttagJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitSmarttagJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SnapshotConfig'] = request.snapshot_config
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitSnapshotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_snapshot_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitSnapshotJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SnapshotConfig'] = request.snapshot_config
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitSnapshotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitSnapshotJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['InputConfig'] = request.input_config
        query['OutputConfig'] = request.output_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitSubtitleJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitSubtitleJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_subtitle_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitSubtitleJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitSubtitleJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InputConfig'] = request.input_config
        query['OutputConfig'] = request.output_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitSubtitleJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitSubtitleJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TagConfig'] = request.tag_config
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitTagJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitTagJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_tag_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitTagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitTagJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TagConfig'] = request.tag_config
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitTagJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitTagJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TerrorismConfig'] = request.terrorism_config
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitTerrorismJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitTerrorismJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_terrorism_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitTerrorismJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitTerrorismJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TerrorismConfig'] = request.terrorism_config
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitTerrorismJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitTerrorismJobResponse(),
            await self.call_api_async(params, req, runtime)
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

    def submit_urlupload_job_with_options(
        self,
        tmp_req: mts_20140618_models.SubmitURLUploadJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitURLUploadJobResponse:
        UtilClient.validate_model(tmp_req)
        request = mts_20140618_models.SubmitURLUploadJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.target_storage):
            request.target_storage_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.target_storage), 'TargetStorage', 'json')
        query = {}
        query['Notify'] = request.notify
        query['Region'] = request.region
        query['SourceFileURL'] = request.source_file_url
        query['TargetStorage'] = request.target_storage_shrink
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitURLUploadJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitURLUploadJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_urlupload_job_with_options_async(
        self,
        tmp_req: mts_20140618_models.SubmitURLUploadJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitURLUploadJobResponse:
        UtilClient.validate_model(tmp_req)
        request = mts_20140618_models.SubmitURLUploadJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.target_storage):
            request.target_storage_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.target_storage), 'TargetStorage', 'json')
        query = {}
        query['Notify'] = request.notify
        query['Region'] = request.region
        query['SourceFileURL'] = request.source_file_url
        query['TargetStorage'] = request.target_storage_shrink
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitURLUploadJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitURLUploadJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_urlupload_job(
        self,
        request: mts_20140618_models.SubmitURLUploadJobRequest,
    ) -> mts_20140618_models.SubmitURLUploadJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_urlupload_job_with_options(request, runtime)

    async def submit_urlupload_job_async(
        self,
        request: mts_20140618_models.SubmitURLUploadJobRequest,
    ) -> mts_20140618_models.SubmitURLUploadJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_urlupload_job_with_options_async(request, runtime)

    def submit_video_gif_job_with_options(
        self,
        request: mts_20140618_models.SubmitVideoGifJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitVideoGifJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        query['VideoGifConfig'] = request.video_gif_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitVideoGifJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitVideoGifJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_video_gif_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitVideoGifJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitVideoGifJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        query['VideoGifConfig'] = request.video_gif_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitVideoGifJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitVideoGifJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Input'] = request.input
        query['OutputConfig'] = request.output_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitVideoPoseJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitVideoPoseJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_video_pose_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitVideoPoseJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitVideoPoseJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['OutputConfig'] = request.output_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitVideoPoseJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitVideoPoseJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Input'] = request.input
        query['JobParams'] = request.job_params
        query['ModelId'] = request.model_id
        query['NotifyUrl'] = request.notify_url
        query['Output'] = request.output
        query['PipelineId'] = request.pipeline_id
        query['ScheduleParams'] = request.schedule_params
        query['SourceType'] = request.source_type
        query['UserData'] = request.user_data
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitVideoQualityJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitVideoQualityJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_video_quality_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitVideoQualityJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitVideoQualityJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['JobParams'] = request.job_params
        query['ModelId'] = request.model_id
        query['NotifyUrl'] = request.notify_url
        query['Output'] = request.output
        query['PipelineId'] = request.pipeline_id
        query['ScheduleParams'] = request.schedule_params
        query['SourceType'] = request.source_type
        query['UserData'] = request.user_data
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitVideoQualityJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitVideoQualityJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        query['VideoSplitConfig'] = request.video_split_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitVideoSplitJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitVideoSplitJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_video_split_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitVideoSplitJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitVideoSplitJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        query['VideoSplitConfig'] = request.video_split_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitVideoSplitJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitVideoSplitJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        query['VideoSummaryConfig'] = request.video_summary_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitVideoSummaryJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitVideoSummaryJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_video_summary_job_with_options_async(
        self,
        request: mts_20140618_models.SubmitVideoSummaryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitVideoSummaryJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Input'] = request.input
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserData'] = request.user_data
        query['VideoSummaryConfig'] = request.video_summary_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitVideoSummaryJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.SubmitVideoSummaryJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CategoryDescription'] = request.category_description
        query['CategoryId'] = request.category_id
        query['CategoryName'] = request.category_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PersonDescription'] = request.person_description
        query['PersonId'] = request.person_id
        query['PersonName'] = request.person_name
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagCustomPerson',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.TagCustomPersonResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_custom_person_with_options_async(
        self,
        request: mts_20140618_models.TagCustomPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.TagCustomPersonResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CategoryDescription'] = request.category_description
        query['CategoryId'] = request.category_id
        query['CategoryName'] = request.category_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PersonDescription'] = request.person_description
        query['PersonId'] = request.person_id
        query['PersonName'] = request.person_name
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagCustomPerson',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.TagCustomPersonResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Bucket'] = request.bucket
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindInputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UnbindInputBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_input_bucket_with_options_async(
        self,
        request: mts_20140618_models.UnbindInputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UnbindInputBucketResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Bucket'] = request.bucket
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindInputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UnbindInputBucketResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Bucket'] = request.bucket
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindOutputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UnbindOutputBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_output_bucket_with_options_async(
        self,
        request: mts_20140618_models.UnbindOutputBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UnbindOutputBucketResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Bucket'] = request.bucket
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindOutputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UnbindOutputBucketResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CategoryId'] = request.category_id
        query['FaceId'] = request.face_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PersonId'] = request.person_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnregisterCustomFace',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UnregisterCustomFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unregister_custom_face_with_options_async(
        self,
        request: mts_20140618_models.UnregisterCustomFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UnregisterCustomFaceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CategoryId'] = request.category_id
        query['FaceId'] = request.face_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PersonId'] = request.person_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnregisterCustomFace',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UnregisterCustomFaceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAsrPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateAsrPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_asr_pipeline_with_options_async(
        self,
        request: mts_20140618_models.UpdateAsrPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateAsrPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAsrPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateAsrPipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CateId'] = request.cate_id
        query['CateName'] = request.cate_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateCategoryName',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateCategoryNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_category_name_with_options_async(
        self,
        request: mts_20140618_models.UpdateCategoryNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateCategoryNameResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CateId'] = request.cate_id
        query['CateName'] = request.cate_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateCategoryName',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateCategoryNameResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateCensorPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateCensorPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_censor_pipeline_with_options_async(
        self,
        request: mts_20140618_models.UpdateCensorPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateCensorPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateCensorPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateCensorPipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Role'] = request.role
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateCoverPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateCoverPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cover_pipeline_with_options_async(
        self,
        request: mts_20140618_models.UpdateCoverPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateCoverPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Role'] = request.role
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateCoverPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateCoverPipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Abuse'] = request.abuse
        query['Ad'] = request.ad
        query['Contraband'] = request.contraband
        query['Live'] = request.live
        query['Logo'] = request.logo
        query['Name'] = request.name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Politics'] = request.politics
        query['Porn'] = request.porn
        query['Qrcode'] = request.qrcode
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        query['Terrorism'] = request.terrorism
        query['spam'] = request.spam
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMCTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMCTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mctemplate_with_options_async(
        self,
        request: mts_20140618_models.UpdateMCTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMCTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Abuse'] = request.abuse
        query['Ad'] = request.ad
        query['Contraband'] = request.contraband
        query['Live'] = request.live
        query['Logo'] = request.logo
        query['Name'] = request.name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Politics'] = request.politics
        query['Porn'] = request.porn
        query['Qrcode'] = request.qrcode
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        query['Terrorism'] = request.terrorism
        query['spam'] = request.spam
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMCTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMCTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Template'] = request.template
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMcuTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMcuTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mcu_template_with_options_async(
        self,
        request: mts_20140618_models.UpdateMcuTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMcuTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Template'] = request.template
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMcuTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMcuTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CateId'] = request.cate_id
        query['CoverURL'] = request.cover_url
        query['Description'] = request.description
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Tags'] = request.tags
        query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CateId'] = request.cate_id
        query['CoverURL'] = request.cover_url
        query['Description'] = request.description
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Tags'] = request.tags
        query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CateId'] = request.cate_id
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMediaCategory',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_category_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CateId'] = request.cate_id
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMediaCategory',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaCategoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CoverURL'] = request.cover_url
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMediaCover',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaCoverResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_cover_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaCoverRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaCoverResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CoverURL'] = request.cover_url
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMediaCover',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaCoverResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Publish'] = request.publish
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMediaPublishState',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaPublishStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_publish_state_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaPublishStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaPublishStateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MediaId'] = request.media_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Publish'] = request.publish
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMediaPublishState',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaPublishStateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['MediaWorkflowId'] = request.media_workflow_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Topology'] = request.topology
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_workflow_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaWorkflowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MediaWorkflowId'] = request.media_workflow_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Topology'] = request.topology
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['MediaWorkflowId'] = request.media_workflow_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TriggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMediaWorkflowTriggerMode',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaWorkflowTriggerModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_workflow_trigger_mode_with_options_async(
        self,
        request: mts_20140618_models.UpdateMediaWorkflowTriggerModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaWorkflowTriggerModeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MediaWorkflowId'] = request.media_workflow_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TriggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMediaWorkflowTriggerMode',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateMediaWorkflowTriggerModeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Role'] = request.role
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdatePipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_with_options_async(
        self,
        request: mts_20140618_models.UpdatePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdatePipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Role'] = request.role
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdatePipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdatePornPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdatePornPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_porn_pipeline_with_options_async(
        self,
        request: mts_20140618_models.UpdatePornPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdatePornPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdatePornPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdatePornPipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AnalyseTypes'] = request.analyse_types
        query['FaceCategoryIds'] = request.face_category_ids
        query['Industry'] = request.industry
        query['IsDefault'] = request.is_default
        query['KeywordConfig'] = request.keyword_config
        query['KnowledgeConfig'] = request.knowledge_config
        query['LabelType'] = request.label_type
        query['LabelVersion'] = request.label_version
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Scene'] = request.scene
        query['TemplateId'] = request.template_id
        query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateSmarttagTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smarttag_template_with_options_async(
        self,
        request: mts_20140618_models.UpdateSmarttagTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateSmarttagTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AnalyseTypes'] = request.analyse_types
        query['FaceCategoryIds'] = request.face_category_ids
        query['Industry'] = request.industry
        query['IsDefault'] = request.is_default
        query['KeywordConfig'] = request.keyword_config
        query['KnowledgeConfig'] = request.knowledge_config
        query['LabelType'] = request.label_type
        query['LabelVersion'] = request.label_version
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Scene'] = request.scene
        query['TemplateId'] = request.template_id
        query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateSmarttagTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Audio'] = request.audio
        query['Container'] = request.container
        query['MuxConfig'] = request.mux_config
        query['Name'] = request.name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        query['TransConfig'] = request.trans_config
        query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_with_options_async(
        self,
        request: mts_20140618_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Audio'] = request.audio
        query['Container'] = request.container
        query['MuxConfig'] = request.mux_config
        query['Name'] = request.name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateId'] = request.template_id
        query['TransConfig'] = request.trans_config
        query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateTerrorismPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateTerrorismPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_terrorism_pipeline_with_options_async(
        self,
        request: mts_20140618_models.UpdateTerrorismPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateTerrorismPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['NotifyConfig'] = request.notify_config
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PipelineId'] = request.pipeline_id
        query['Priority'] = request.priority
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateTerrorismPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateTerrorismPipelineResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Config'] = request.config
        query['Name'] = request.name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['WaterMarkTemplateId'] = request.water_mark_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateWaterMarkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_water_mark_template_with_options_async(
        self,
        request: mts_20140618_models.UpdateWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateWaterMarkTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Config'] = request.config
        query['Name'] = request.name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['WaterMarkTemplateId'] = request.water_mark_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mts_20140618_models.UpdateWaterMarkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
