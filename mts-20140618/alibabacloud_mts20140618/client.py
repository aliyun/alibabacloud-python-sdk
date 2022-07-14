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
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def add_media_with_options(
        self,
        request: mts_20140618_models.AddMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_url):
            query['FileURL'] = request.file_url
        if not UtilClient.is_unset(request.input_unbind):
            query['InputUnbind'] = request.input_unbind
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.media_workflow_user_data):
            query['MediaWorkflowUserData'] = request.media_workflow_user_data
        if not UtilClient.is_unset(request.override_params):
            query['OverrideParams'] = request.override_params
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_url):
            query['FileURL'] = request.file_url
        if not UtilClient.is_unset(request.input_unbind):
            query['InputUnbind'] = request.input_unbind
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.media_workflow_user_data):
            query['MediaWorkflowUserData'] = request.media_workflow_user_data
        if not UtilClient.is_unset(request.override_params):
            query['OverrideParams'] = request.override_params
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMediaTag',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMediaTag',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.topology):
            query['Topology'] = request.topology
        if not UtilClient.is_unset(request.trigger_mode):
            query['TriggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.topology):
            query['Topology'] = request.topology
        if not UtilClient.is_unset(request.trigger_mode):
            query['TriggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.notify_config):
            query['NotifyConfig'] = request.notify_config
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.speed_level):
            query['SpeedLevel'] = request.speed_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.notify_config):
            query['NotifyConfig'] = request.notify_config
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        if not UtilClient.is_unset(request.speed_level):
            query['SpeedLevel'] = request.speed_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def add_smarttag_template_with_options(
        self,
        request: mts_20140618_models.AddSmarttagTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddSmarttagTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analyse_types):
            query['AnalyseTypes'] = request.analyse_types
        if not UtilClient.is_unset(request.face_category_ids):
            query['FaceCategoryIds'] = request.face_category_ids
        if not UtilClient.is_unset(request.face_custom_params_config):
            query['FaceCustomParamsConfig'] = request.face_custom_params_config
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.is_default):
            query['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.keyword_config):
            query['KeywordConfig'] = request.keyword_config
        if not UtilClient.is_unset(request.knowledge_config):
            query['KnowledgeConfig'] = request.knowledge_config
        if not UtilClient.is_unset(request.label_type):
            query['LabelType'] = request.label_type
        if not UtilClient.is_unset(request.label_version):
            query['LabelVersion'] = request.label_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.analyse_types):
            query['AnalyseTypes'] = request.analyse_types
        if not UtilClient.is_unset(request.face_category_ids):
            query['FaceCategoryIds'] = request.face_category_ids
        if not UtilClient.is_unset(request.face_custom_params_config):
            query['FaceCustomParamsConfig'] = request.face_custom_params_config
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.is_default):
            query['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.keyword_config):
            query['KeywordConfig'] = request.keyword_config
        if not UtilClient.is_unset(request.knowledge_config):
            query['KnowledgeConfig'] = request.knowledge_config
        if not UtilClient.is_unset(request.label_type):
            query['LabelType'] = request.label_type
        if not UtilClient.is_unset(request.label_version):
            query['LabelVersion'] = request.label_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.audio):
            query['Audio'] = request.audio
        if not UtilClient.is_unset(request.container):
            query['Container'] = request.container
        if not UtilClient.is_unset(request.mux_config):
            query['MuxConfig'] = request.mux_config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.trans_config):
            query['TransConfig'] = request.trans_config
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.audio):
            query['Audio'] = request.audio
        if not UtilClient.is_unset(request.container):
            query['Container'] = request.container
        if not UtilClient.is_unset(request.mux_config):
            query['MuxConfig'] = request.mux_config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.trans_config):
            query['TransConfig'] = request.trans_config
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def add_water_mark_template_with_options(
        self,
        request: mts_20140618_models.AddWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.AddWaterMarkTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.referer):
            query['Referer'] = request.referer
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindInputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.referer):
            query['Referer'] = request.referer
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindInputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindOutputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindOutputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def create_fp_shot_dbwith_options(
        self,
        request: mts_20140618_models.CreateFpShotDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.CreateFpShotDBResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFpShotDB',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFpShotDB',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def deactivate_media_workflow_with_options(
        self,
        request: mts_20140618_models.DeactivateMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeactivateMediaWorkflowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactivateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactivateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def delete_media_with_options(
        self,
        request: mts_20140618_models.DeleteMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.DeleteMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMediaTag',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMediaTag',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.water_mark_template_id):
            query['WaterMarkTemplateId'] = request.water_mark_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.water_mark_template_id):
            query['WaterMarkTemplateId'] = request.water_mark_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def im_audit_with_options(
        self,
        request: mts_20140618_models.ImAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ImAuditResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.contents):
            query['Contents'] = request.contents
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scenes):
            query['Scenes'] = request.scenes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImAudit',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.contents):
            query['Contents'] = request.contents
        if not UtilClient.is_unset(request.images):
            query['Images'] = request.images
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scenes):
            query['Scenes'] = request.scenes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImAudit',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not UtilClient.is_unset(request.fp_import_config):
            query['FpImportConfig'] = request.fp_import_config
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportFpShotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not UtilClient.is_unset(request.fp_import_config):
            query['FpImportConfig'] = request.fp_import_config
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportFpShotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def list_all_media_bucket_with_options(
        self,
        request: mts_20140618_models.ListAllMediaBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListAllMediaBucketResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllMediaBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllMediaBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def list_custom_persons_with_options(
        self,
        request: mts_20140618_models.ListCustomPersonsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListCustomPersonsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomPersons',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomPersons',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.fp_dbids):
            query['FpDBIds'] = request.fp_dbids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFpShotDB',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.fp_dbids):
            query['FpDBIds'] = request.fp_dbids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFpShotDB',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFpShotFiles',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFpShotFiles',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFpShotImportJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFpShotImportJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def list_job_with_options(
        self,
        request: mts_20140618_models.ListJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def list_media_workflow_executions_with_options(
        self,
        request: mts_20140618_models.ListMediaWorkflowExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ListMediaWorkflowExecutionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_file_url):
            query['InputFileURL'] = request.input_file_url
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.media_workflow_name):
            query['MediaWorkflowName'] = request.media_workflow_name
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMediaWorkflowExecutions',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.input_file_url):
            query['InputFileURL'] = request.input_file_url
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.media_workflow_name):
            query['MediaWorkflowName'] = request.media_workflow_name
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMediaWorkflowExecutions',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def query_analysis_job_list_with_options(
        self,
        request: mts_20140618_models.QueryAnalysisJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryAnalysisJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_job_ids):
            query['AnalysisJobIds'] = request.analysis_job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAnalysisJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.analysis_job_ids):
            query['AnalysisJobIds'] = request.analysis_job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAnalysisJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def query_editing_job_list_with_options(
        self,
        request: mts_20140618_models.QueryEditingJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryEditingJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEditingJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEditingJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def query_fp_dbdelete_job_list_with_options(
        self,
        request: mts_20140618_models.QueryFpDBDeleteJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpDBDeleteJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFpDBDeleteJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFpDBDeleteJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFpFileDeleteJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFpFileDeleteJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def query_fp_shot_job_list_with_options(
        self,
        request: mts_20140618_models.QueryFpShotJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryFpShotJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFpShotJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFpShotJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIProductionJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIProductionJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def query_job_list_with_options(
        self,
        request: mts_20140618_models.QueryJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def query_media_censor_job_detail_with_options(
        self,
        request: mts_20140618_models.QueryMediaCensorJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaCensorJobDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaCensorJobDetail',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaCensorJobDetail',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaCensorJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaCensorJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def query_media_info_job_list_with_options(
        self,
        request: mts_20140618_models.QueryMediaInfoJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryMediaInfoJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_info_job_ids):
            query['MediaInfoJobIds'] = request.media_info_job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaInfoJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_info_job_ids):
            query['MediaInfoJobIds'] = request.media_info_job_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaInfoJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.include_media_info):
            query['IncludeMediaInfo'] = request.include_media_info
        if not UtilClient.is_unset(request.include_play_list):
            query['IncludePlayList'] = request.include_play_list
        if not UtilClient.is_unset(request.include_snapshot_list):
            query['IncludeSnapshotList'] = request.include_snapshot_list
        if not UtilClient.is_unset(request.include_summary_list):
            query['IncludeSummaryList'] = request.include_summary_list
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.include_media_info):
            query['IncludeMediaInfo'] = request.include_media_info
        if not UtilClient.is_unset(request.include_play_list):
            query['IncludePlayList'] = request.include_play_list
        if not UtilClient.is_unset(request.include_snapshot_list):
            query['IncludeSnapshotList'] = request.include_snapshot_list
        if not UtilClient.is_unset(request.include_summary_list):
            query['IncludeSummaryList'] = request.include_summary_list
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.file_urls):
            query['FileURLs'] = request.file_urls
        if not UtilClient.is_unset(request.include_media_info):
            query['IncludeMediaInfo'] = request.include_media_info
        if not UtilClient.is_unset(request.include_play_list):
            query['IncludePlayList'] = request.include_play_list
        if not UtilClient.is_unset(request.include_snapshot_list):
            query['IncludeSnapshotList'] = request.include_snapshot_list
        if not UtilClient.is_unset(request.include_summary_list):
            query['IncludeSummaryList'] = request.include_summary_list
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaListByURL',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.file_urls):
            query['FileURLs'] = request.file_urls
        if not UtilClient.is_unset(request.include_media_info):
            query['IncludeMediaInfo'] = request.include_media_info
        if not UtilClient.is_unset(request.include_play_list):
            query['IncludePlayList'] = request.include_play_list
        if not UtilClient.is_unset(request.include_snapshot_list):
            query['IncludeSnapshotList'] = request.include_snapshot_list
        if not UtilClient.is_unset(request.include_summary_list):
            query['IncludeSummaryList'] = request.include_summary_list
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaListByURL',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.run_ids):
            query['RunIds'] = request.run_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaWorkflowExecutionList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.run_ids):
            query['RunIds'] = request.run_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaWorkflowExecutionList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_workflow_ids):
            query['MediaWorkflowIds'] = request.media_workflow_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaWorkflowList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_workflow_ids):
            query['MediaWorkflowIds'] = request.media_workflow_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaWorkflowList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_ids):
            query['PipelineIds'] = request.pipeline_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPipelineList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_ids):
            query['PipelineIds'] = request.pipeline_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPipelineList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def query_smarttag_job_with_options(
        self,
        request: mts_20140618_models.QuerySmarttagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySmarttagJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmarttagJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmarttagJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def query_smarttag_template_list_with_options(
        self,
        request: mts_20140618_models.QuerySmarttagTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QuerySmarttagTemplateListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmarttagTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmarttagTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snapshot_job_ids):
            query['SnapshotJobIds'] = request.snapshot_job_ids
        if not UtilClient.is_unset(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySnapshotJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snapshot_job_ids):
            query['SnapshotJobIds'] = request.snapshot_job_ids
        if not UtilClient.is_unset(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySnapshotJobList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def query_template_list_with_options(
        self,
        request: mts_20140618_models.QueryTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryTemplateListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_ids):
            query['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_ids):
            query['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def query_video_quality_job_with_options(
        self,
        request: mts_20140618_models.QueryVideoQualityJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryVideoQualityJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryVideoQualityJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryVideoQualityJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def query_water_mark_template_list_with_options(
        self,
        request: mts_20140618_models.QueryWaterMarkTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.QueryWaterMarkTemplateListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.water_mark_template_ids):
            query['WaterMarkTemplateIds'] = request.water_mark_template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWaterMarkTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.water_mark_template_ids):
            query['WaterMarkTemplateIds'] = request.water_mark_template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWaterMarkTemplateList',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def register_custom_face_with_options(
        self,
        request: mts_20140618_models.RegisterCustomFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.RegisterCustomFaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterCustomFace',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterCustomFace',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def report_fp_shot_job_result_with_options(
        self,
        request: mts_20140618_models.ReportFpShotJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.ReportFpShotJobResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.details):
            query['Details'] = request.details
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.result):
            query['Result'] = request.result
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportFpShotJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.details):
            query['Details'] = request.details
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.result):
            query['Result'] = request.result
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportFpShotJobResult',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def search_media_workflow_with_options(
        self,
        request: mts_20140618_models.SearchMediaWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SearchMediaWorkflowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state_list):
            query['StateList'] = request.state_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state_list):
            query['StateList'] = request.state_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchPipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def submit_analysis_job_with_options(
        self,
        request: mts_20140618_models.SubmitAnalysisJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitAnalysisJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_config):
            query['AnalysisConfig'] = request.analysis_config
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAnalysisJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.analysis_config):
            query['AnalysisConfig'] = request.analysis_config
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAnalysisJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def submit_editing_jobs_with_options(
        self,
        request: mts_20140618_models.SubmitEditingJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitEditingJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.editing_inputs):
            query['EditingInputs'] = request.editing_inputs
        if not UtilClient.is_unset(request.editing_job_oss_file_role_arn):
            query['EditingJobOssFileRoleArn'] = request.editing_job_oss_file_role_arn
        if not UtilClient.is_unset(request.editing_job_oss_file_uid):
            query['EditingJobOssFileUid'] = request.editing_job_oss_file_uid
        if not UtilClient.is_unset(request.editing_job_outputs):
            query['EditingJobOutputs'] = request.editing_job_outputs
        if not UtilClient.is_unset(request.editing_job_url):
            query['EditingJobURL'] = request.editing_job_url
        if not UtilClient.is_unset(request.output_bucket):
            query['OutputBucket'] = request.output_bucket
        if not UtilClient.is_unset(request.output_location):
            query['OutputLocation'] = request.output_location
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitEditingJobs',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.editing_inputs):
            query['EditingInputs'] = request.editing_inputs
        if not UtilClient.is_unset(request.editing_job_oss_file_role_arn):
            query['EditingJobOssFileRoleArn'] = request.editing_job_oss_file_role_arn
        if not UtilClient.is_unset(request.editing_job_oss_file_uid):
            query['EditingJobOssFileUid'] = request.editing_job_oss_file_uid
        if not UtilClient.is_unset(request.editing_job_outputs):
            query['EditingJobOutputs'] = request.editing_job_outputs
        if not UtilClient.is_unset(request.editing_job_url):
            query['EditingJobURL'] = request.editing_job_url
        if not UtilClient.is_unset(request.output_bucket):
            query['OutputBucket'] = request.output_bucket
        if not UtilClient.is_unset(request.output_location):
            query['OutputLocation'] = request.output_location
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitEditingJobs',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def submit_fp_dbdelete_job_with_options(
        self,
        request: mts_20140618_models.SubmitFpDBDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitFpDBDeleteJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.del_type):
            query['DelType'] = request.del_type
        if not UtilClient.is_unset(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitFpDBDeleteJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.del_type):
            query['DelType'] = request.del_type
        if not UtilClient.is_unset(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitFpDBDeleteJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.file_ids):
            query['FileIds'] = request.file_ids
        if not UtilClient.is_unset(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitFpFileDeleteJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.file_ids):
            query['FileIds'] = request.file_ids
        if not UtilClient.is_unset(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitFpFileDeleteJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.fp_shot_config):
            query['FpShotConfig'] = request.fp_shot_config
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitFpShotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.fp_shot_config):
            query['FpShotConfig'] = request.fp_shot_config
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitFpShotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.job_params):
            query['JobParams'] = request.job_params
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.output):
            query['Output'] = request.output
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schedule_params):
            query['ScheduleParams'] = request.schedule_params
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIProductionJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.job_params):
            query['JobParams'] = request.job_params
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.output):
            query['Output'] = request.output
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.schedule_params):
            query['ScheduleParams'] = request.schedule_params
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIProductionJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def submit_jobs_with_options(
        self,
        request: mts_20140618_models.SubmitJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.output_bucket):
            query['OutputBucket'] = request.output_bucket
        if not UtilClient.is_unset(request.output_location):
            query['OutputLocation'] = request.output_location
        if not UtilClient.is_unset(request.outputs):
            query['Outputs'] = request.outputs
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitJobs',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.output_bucket):
            query['OutputBucket'] = request.output_bucket
        if not UtilClient.is_unset(request.output_location):
            query['OutputLocation'] = request.output_location
        if not UtilClient.is_unset(request.outputs):
            query['Outputs'] = request.outputs
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitJobs',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def submit_media_censor_job_with_options(
        self,
        request: mts_20140618_models.SubmitMediaCensorJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaCensorJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.barrages):
            query['Barrages'] = request.barrages
        if not UtilClient.is_unset(request.cover_images):
            query['CoverImages'] = request.cover_images
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.external_url):
            query['ExternalUrl'] = request.external_url
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.video_censor_config):
            query['VideoCensorConfig'] = request.video_censor_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMediaCensorJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.barrages):
            query['Barrages'] = request.barrages
        if not UtilClient.is_unset(request.cover_images):
            query['CoverImages'] = request.cover_images
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.external_url):
            query['ExternalUrl'] = request.external_url
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.video_censor_config):
            query['VideoCensorConfig'] = request.video_censor_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMediaCensorJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def submit_media_info_job_with_options(
        self,
        request: mts_20140618_models.SubmitMediaInfoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitMediaInfoJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMediaInfoJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMediaInfoJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def submit_smarttag_job_with_options(
        self,
        request: mts_20140618_models.SubmitSmarttagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitSmarttagJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.content_addr):
            query['ContentAddr'] = request.content_addr
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSmarttagJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.content_addr):
            query['ContentAddr'] = request.content_addr
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSmarttagJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snapshot_config):
            query['SnapshotConfig'] = request.snapshot_config
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSnapshotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.snapshot_config):
            query['SnapshotConfig'] = request.snapshot_config
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSnapshotJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def submit_video_quality_job_with_options(
        self,
        request: mts_20140618_models.SubmitVideoQualityJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.SubmitVideoQualityJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.job_params):
            query['JobParams'] = request.job_params
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.output):
            query['Output'] = request.output
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.schedule_params):
            query['ScheduleParams'] = request.schedule_params
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitVideoQualityJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.job_params):
            query['JobParams'] = request.job_params
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.output):
            query['Output'] = request.output
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.schedule_params):
            query['ScheduleParams'] = request.schedule_params
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitVideoQualityJob',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def tag_custom_person_with_options(
        self,
        request: mts_20140618_models.TagCustomPersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.TagCustomPersonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_description):
            query['CategoryDescription'] = request.category_description
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.category_name):
            query['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.person_description):
            query['PersonDescription'] = request.person_description
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.person_name):
            query['PersonName'] = request.person_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagCustomPerson',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.category_description):
            query['CategoryDescription'] = request.category_description
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.category_name):
            query['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.person_description):
            query['PersonDescription'] = request.person_description
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.person_name):
            query['PersonName'] = request.person_name
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagCustomPerson',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindInputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindInputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindOutputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindOutputBucket',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.face_id):
            query['FaceId'] = request.face_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnregisterCustomFace',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.face_id):
            query['FaceId'] = request.face_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.person_id):
            query['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnregisterCustomFace',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def update_media_with_options(
        self,
        request: mts_20140618_models.UpdateMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMedia',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaCategory',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaCategory',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaCover',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaCover',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.publish):
            query['Publish'] = request.publish
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaPublishState',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.publish):
            query['Publish'] = request.publish
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaPublishState',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.topology):
            query['Topology'] = request.topology
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.topology):
            query['Topology'] = request.topology
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaWorkflow',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.trigger_mode):
            query['TriggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaWorkflowTriggerMode',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.trigger_mode):
            query['TriggerMode'] = request.trigger_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaWorkflowTriggerMode',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.notify_config):
            query['NotifyConfig'] = request.notify_config
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.notify_config):
            query['NotifyConfig'] = request.notify_config
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipeline',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def update_smarttag_template_with_options(
        self,
        request: mts_20140618_models.UpdateSmarttagTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateSmarttagTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analyse_types):
            query['AnalyseTypes'] = request.analyse_types
        if not UtilClient.is_unset(request.face_category_ids):
            query['FaceCategoryIds'] = request.face_category_ids
        if not UtilClient.is_unset(request.face_custom_params_config):
            query['FaceCustomParamsConfig'] = request.face_custom_params_config
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.is_default):
            query['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.keyword_config):
            query['KeywordConfig'] = request.keyword_config
        if not UtilClient.is_unset(request.knowledge_config):
            query['KnowledgeConfig'] = request.knowledge_config
        if not UtilClient.is_unset(request.label_type):
            query['LabelType'] = request.label_type
        if not UtilClient.is_unset(request.label_version):
            query['LabelVersion'] = request.label_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.analyse_types):
            query['AnalyseTypes'] = request.analyse_types
        if not UtilClient.is_unset(request.face_category_ids):
            query['FaceCategoryIds'] = request.face_category_ids
        if not UtilClient.is_unset(request.face_custom_params_config):
            query['FaceCustomParamsConfig'] = request.face_custom_params_config
        if not UtilClient.is_unset(request.industry):
            query['Industry'] = request.industry
        if not UtilClient.is_unset(request.is_default):
            query['IsDefault'] = request.is_default
        if not UtilClient.is_unset(request.keyword_config):
            query['KeywordConfig'] = request.keyword_config
        if not UtilClient.is_unset(request.knowledge_config):
            query['KnowledgeConfig'] = request.knowledge_config
        if not UtilClient.is_unset(request.label_type):
            query['LabelType'] = request.label_type
        if not UtilClient.is_unset(request.label_version):
            query['LabelVersion'] = request.label_version
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmarttagTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.audio):
            query['Audio'] = request.audio
        if not UtilClient.is_unset(request.container):
            query['Container'] = request.container
        if not UtilClient.is_unset(request.mux_config):
            query['MuxConfig'] = request.mux_config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.trans_config):
            query['TransConfig'] = request.trans_config
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.audio):
            query['Audio'] = request.audio
        if not UtilClient.is_unset(request.container):
            query['Container'] = request.container
        if not UtilClient.is_unset(request.mux_config):
            query['MuxConfig'] = request.mux_config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.trans_config):
            query['TransConfig'] = request.trans_config
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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

    def update_water_mark_template_with_options(
        self,
        request: mts_20140618_models.UpdateWaterMarkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mts_20140618_models.UpdateWaterMarkTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.water_mark_template_id):
            query['WaterMarkTemplateId'] = request.water_mark_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.water_mark_template_id):
            query['WaterMarkTemplateId'] = request.water_mark_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWaterMarkTemplate',
            version='2014-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
