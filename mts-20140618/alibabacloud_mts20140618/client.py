# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_mts20140618 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def activate_media_workflow_with_options(
        self,
        request: main_models.ActivateMediaWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActivateMediaWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActivateMediaWorkflow',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActivateMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_media_workflow_with_options_async(
        self,
        request: main_models.ActivateMediaWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActivateMediaWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActivateMediaWorkflow',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActivateMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_media_workflow(
        self,
        request: main_models.ActivateMediaWorkflowRequest,
    ) -> main_models.ActivateMediaWorkflowResponse:
        runtime = RuntimeOptions()
        return self.activate_media_workflow_with_options(request, runtime)

    async def activate_media_workflow_async(
        self,
        request: main_models.ActivateMediaWorkflowRequest,
    ) -> main_models.ActivateMediaWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.activate_media_workflow_with_options_async(request, runtime)

    def add_media_with_options(
        self,
        request: main_models.AddMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_url):
            query['FileURL'] = request.file_url
        if not DaraCore.is_null(request.input_unbind):
            query['InputUnbind'] = request.input_unbind
        if not DaraCore.is_null(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not DaraCore.is_null(request.media_workflow_user_data):
            query['MediaWorkflowUserData'] = request.media_workflow_user_data
        if not DaraCore.is_null(request.override_params):
            query['OverrideParams'] = request.override_params
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddMedia',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_media_with_options_async(
        self,
        request: main_models.AddMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_url):
            query['FileURL'] = request.file_url
        if not DaraCore.is_null(request.input_unbind):
            query['InputUnbind'] = request.input_unbind
        if not DaraCore.is_null(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not DaraCore.is_null(request.media_workflow_user_data):
            query['MediaWorkflowUserData'] = request.media_workflow_user_data
        if not DaraCore.is_null(request.override_params):
            query['OverrideParams'] = request.override_params
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddMedia',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_media(
        self,
        request: main_models.AddMediaRequest,
    ) -> main_models.AddMediaResponse:
        runtime = RuntimeOptions()
        return self.add_media_with_options(request, runtime)

    async def add_media_async(
        self,
        request: main_models.AddMediaRequest,
    ) -> main_models.AddMediaResponse:
        runtime = RuntimeOptions()
        return await self.add_media_with_options_async(request, runtime)

    def add_media_tag_with_options(
        self,
        request: main_models.AddMediaTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMediaTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddMediaTag',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMediaTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_media_tag_with_options_async(
        self,
        request: main_models.AddMediaTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMediaTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddMediaTag',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMediaTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_media_tag(
        self,
        request: main_models.AddMediaTagRequest,
    ) -> main_models.AddMediaTagResponse:
        runtime = RuntimeOptions()
        return self.add_media_tag_with_options(request, runtime)

    async def add_media_tag_async(
        self,
        request: main_models.AddMediaTagRequest,
    ) -> main_models.AddMediaTagResponse:
        runtime = RuntimeOptions()
        return await self.add_media_tag_with_options_async(request, runtime)

    def add_media_workflow_with_options(
        self,
        request: main_models.AddMediaWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMediaWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.topology):
            query['Topology'] = request.topology
        if not DaraCore.is_null(request.trigger_mode):
            query['TriggerMode'] = request.trigger_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddMediaWorkflow',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_media_workflow_with_options_async(
        self,
        request: main_models.AddMediaWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddMediaWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.topology):
            query['Topology'] = request.topology
        if not DaraCore.is_null(request.trigger_mode):
            query['TriggerMode'] = request.trigger_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddMediaWorkflow',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_media_workflow(
        self,
        request: main_models.AddMediaWorkflowRequest,
    ) -> main_models.AddMediaWorkflowResponse:
        runtime = RuntimeOptions()
        return self.add_media_workflow_with_options(request, runtime)

    async def add_media_workflow_async(
        self,
        request: main_models.AddMediaWorkflowRequest,
    ) -> main_models.AddMediaWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.add_media_workflow_with_options_async(request, runtime)

    def add_pipeline_with_options(
        self,
        request: main_models.AddPipelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.notify_config):
            query['NotifyConfig'] = request.notify_config
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.speed):
            query['Speed'] = request.speed
        if not DaraCore.is_null(request.speed_level):
            query['SpeedLevel'] = request.speed_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPipeline',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_pipeline_with_options_async(
        self,
        request: main_models.AddPipelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.notify_config):
            query['NotifyConfig'] = request.notify_config
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.speed):
            query['Speed'] = request.speed
        if not DaraCore.is_null(request.speed_level):
            query['SpeedLevel'] = request.speed_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPipeline',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_pipeline(
        self,
        request: main_models.AddPipelineRequest,
    ) -> main_models.AddPipelineResponse:
        runtime = RuntimeOptions()
        return self.add_pipeline_with_options(request, runtime)

    async def add_pipeline_async(
        self,
        request: main_models.AddPipelineRequest,
    ) -> main_models.AddPipelineResponse:
        runtime = RuntimeOptions()
        return await self.add_pipeline_with_options_async(request, runtime)

    def add_smarttag_template_with_options(
        self,
        request: main_models.AddSmarttagTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSmarttagTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analyse_types):
            query['AnalyseTypes'] = request.analyse_types
        if not DaraCore.is_null(request.face_category_ids):
            query['FaceCategoryIds'] = request.face_category_ids
        if not DaraCore.is_null(request.face_custom_params_config):
            query['FaceCustomParamsConfig'] = request.face_custom_params_config
        if not DaraCore.is_null(request.industry):
            query['Industry'] = request.industry
        if not DaraCore.is_null(request.is_default):
            query['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.keyword_config):
            query['KeywordConfig'] = request.keyword_config
        if not DaraCore.is_null(request.knowledge_config):
            query['KnowledgeConfig'] = request.knowledge_config
        if not DaraCore.is_null(request.label_custom_category_ids):
            query['LabelCustomCategoryIds'] = request.label_custom_category_ids
        if not DaraCore.is_null(request.label_custom_params_config):
            query['LabelCustomParamsConfig'] = request.label_custom_params_config
        if not DaraCore.is_null(request.label_type):
            query['LabelType'] = request.label_type
        if not DaraCore.is_null(request.label_version):
            query['LabelVersion'] = request.label_version
        if not DaraCore.is_null(request.landmark_group_ids):
            query['LandmarkGroupIds'] = request.landmark_group_ids
        if not DaraCore.is_null(request.object_group_ids):
            query['ObjectGroupIds'] = request.object_group_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSmarttagTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSmarttagTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_smarttag_template_with_options_async(
        self,
        request: main_models.AddSmarttagTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddSmarttagTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analyse_types):
            query['AnalyseTypes'] = request.analyse_types
        if not DaraCore.is_null(request.face_category_ids):
            query['FaceCategoryIds'] = request.face_category_ids
        if not DaraCore.is_null(request.face_custom_params_config):
            query['FaceCustomParamsConfig'] = request.face_custom_params_config
        if not DaraCore.is_null(request.industry):
            query['Industry'] = request.industry
        if not DaraCore.is_null(request.is_default):
            query['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.keyword_config):
            query['KeywordConfig'] = request.keyword_config
        if not DaraCore.is_null(request.knowledge_config):
            query['KnowledgeConfig'] = request.knowledge_config
        if not DaraCore.is_null(request.label_custom_category_ids):
            query['LabelCustomCategoryIds'] = request.label_custom_category_ids
        if not DaraCore.is_null(request.label_custom_params_config):
            query['LabelCustomParamsConfig'] = request.label_custom_params_config
        if not DaraCore.is_null(request.label_type):
            query['LabelType'] = request.label_type
        if not DaraCore.is_null(request.label_version):
            query['LabelVersion'] = request.label_version
        if not DaraCore.is_null(request.landmark_group_ids):
            query['LandmarkGroupIds'] = request.landmark_group_ids
        if not DaraCore.is_null(request.object_group_ids):
            query['ObjectGroupIds'] = request.object_group_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddSmarttagTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSmarttagTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_smarttag_template(
        self,
        request: main_models.AddSmarttagTemplateRequest,
    ) -> main_models.AddSmarttagTemplateResponse:
        runtime = RuntimeOptions()
        return self.add_smarttag_template_with_options(request, runtime)

    async def add_smarttag_template_async(
        self,
        request: main_models.AddSmarttagTemplateRequest,
    ) -> main_models.AddSmarttagTemplateResponse:
        runtime = RuntimeOptions()
        return await self.add_smarttag_template_with_options_async(request, runtime)

    def add_template_with_options(
        self,
        request: main_models.AddTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio):
            query['Audio'] = request.audio
        if not DaraCore.is_null(request.container):
            query['Container'] = request.container
        if not DaraCore.is_null(request.mux_config):
            query['MuxConfig'] = request.mux_config
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.trans_config):
            query['TransConfig'] = request.trans_config
        if not DaraCore.is_null(request.video):
            query['Video'] = request.video
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_template_with_options_async(
        self,
        request: main_models.AddTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio):
            query['Audio'] = request.audio
        if not DaraCore.is_null(request.container):
            query['Container'] = request.container
        if not DaraCore.is_null(request.mux_config):
            query['MuxConfig'] = request.mux_config
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.trans_config):
            query['TransConfig'] = request.trans_config
        if not DaraCore.is_null(request.video):
            query['Video'] = request.video
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_template(
        self,
        request: main_models.AddTemplateRequest,
    ) -> main_models.AddTemplateResponse:
        runtime = RuntimeOptions()
        return self.add_template_with_options(request, runtime)

    async def add_template_async(
        self,
        request: main_models.AddTemplateRequest,
    ) -> main_models.AddTemplateResponse:
        runtime = RuntimeOptions()
        return await self.add_template_with_options_async(request, runtime)

    def add_water_mark_template_with_options(
        self,
        request: main_models.AddWaterMarkTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddWaterMarkTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddWaterMarkTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddWaterMarkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_water_mark_template_with_options_async(
        self,
        request: main_models.AddWaterMarkTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddWaterMarkTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddWaterMarkTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddWaterMarkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_water_mark_template(
        self,
        request: main_models.AddWaterMarkTemplateRequest,
    ) -> main_models.AddWaterMarkTemplateResponse:
        runtime = RuntimeOptions()
        return self.add_water_mark_template_with_options(request, runtime)

    async def add_water_mark_template_async(
        self,
        request: main_models.AddWaterMarkTemplateRequest,
    ) -> main_models.AddWaterMarkTemplateResponse:
        runtime = RuntimeOptions()
        return await self.add_water_mark_template_with_options_async(request, runtime)

    def bind_input_bucket_with_options(
        self,
        request: main_models.BindInputBucketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindInputBucketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket):
            query['Bucket'] = request.bucket
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.referer):
            query['Referer'] = request.referer
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindInputBucket',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindInputBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_input_bucket_with_options_async(
        self,
        request: main_models.BindInputBucketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindInputBucketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket):
            query['Bucket'] = request.bucket
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.referer):
            query['Referer'] = request.referer
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindInputBucket',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindInputBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_input_bucket(
        self,
        request: main_models.BindInputBucketRequest,
    ) -> main_models.BindInputBucketResponse:
        runtime = RuntimeOptions()
        return self.bind_input_bucket_with_options(request, runtime)

    async def bind_input_bucket_async(
        self,
        request: main_models.BindInputBucketRequest,
    ) -> main_models.BindInputBucketResponse:
        runtime = RuntimeOptions()
        return await self.bind_input_bucket_with_options_async(request, runtime)

    def bind_output_bucket_with_options(
        self,
        request: main_models.BindOutputBucketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindOutputBucketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket):
            query['Bucket'] = request.bucket
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindOutputBucket',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindOutputBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_output_bucket_with_options_async(
        self,
        request: main_models.BindOutputBucketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindOutputBucketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket):
            query['Bucket'] = request.bucket
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindOutputBucket',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindOutputBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_output_bucket(
        self,
        request: main_models.BindOutputBucketRequest,
    ) -> main_models.BindOutputBucketResponse:
        runtime = RuntimeOptions()
        return self.bind_output_bucket_with_options(request, runtime)

    async def bind_output_bucket_async(
        self,
        request: main_models.BindOutputBucketRequest,
    ) -> main_models.BindOutputBucketResponse:
        runtime = RuntimeOptions()
        return await self.bind_output_bucket_with_options_async(request, runtime)

    def cancel_job_with_options(
        self,
        request: main_models.CancelJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_job_with_options_async(
        self,
        request: main_models.CancelJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_job(
        self,
        request: main_models.CancelJobRequest,
    ) -> main_models.CancelJobResponse:
        runtime = RuntimeOptions()
        return self.cancel_job_with_options(request, runtime)

    async def cancel_job_async(
        self,
        request: main_models.CancelJobRequest,
    ) -> main_models.CancelJobResponse:
        runtime = RuntimeOptions()
        return await self.cancel_job_with_options_async(request, runtime)

    def create_custom_entity_with_options(
        self,
        request: main_models.CreateCustomEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomEntityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.custom_entity_info):
            query['CustomEntityInfo'] = request.custom_entity_info
        if not DaraCore.is_null(request.custom_entity_name):
            query['CustomEntityName'] = request.custom_entity_name
        if not DaraCore.is_null(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomEntity',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_entity_with_options_async(
        self,
        request: main_models.CreateCustomEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomEntityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.custom_entity_info):
            query['CustomEntityInfo'] = request.custom_entity_info
        if not DaraCore.is_null(request.custom_entity_name):
            query['CustomEntityName'] = request.custom_entity_name
        if not DaraCore.is_null(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomEntity',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_entity(
        self,
        request: main_models.CreateCustomEntityRequest,
    ) -> main_models.CreateCustomEntityResponse:
        runtime = RuntimeOptions()
        return self.create_custom_entity_with_options(request, runtime)

    async def create_custom_entity_async(
        self,
        request: main_models.CreateCustomEntityRequest,
    ) -> main_models.CreateCustomEntityResponse:
        runtime = RuntimeOptions()
        return await self.create_custom_entity_with_options_async(request, runtime)

    def create_custom_group_with_options(
        self,
        request: main_models.CreateCustomGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.custom_group_description):
            query['CustomGroupDescription'] = request.custom_group_description
        if not DaraCore.is_null(request.custom_group_name):
            query['CustomGroupName'] = request.custom_group_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomGroup',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_group_with_options_async(
        self,
        request: main_models.CreateCustomGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.custom_group_description):
            query['CustomGroupDescription'] = request.custom_group_description
        if not DaraCore.is_null(request.custom_group_name):
            query['CustomGroupName'] = request.custom_group_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomGroup',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_group(
        self,
        request: main_models.CreateCustomGroupRequest,
    ) -> main_models.CreateCustomGroupResponse:
        runtime = RuntimeOptions()
        return self.create_custom_group_with_options(request, runtime)

    async def create_custom_group_async(
        self,
        request: main_models.CreateCustomGroupRequest,
    ) -> main_models.CreateCustomGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_custom_group_with_options_async(request, runtime)

    def create_fp_shot_dbwith_options(
        self,
        request: main_models.CreateFpShotDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFpShotDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.model_id):
            query['ModelId'] = request.model_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFpShotDB',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFpShotDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fp_shot_dbwith_options_async(
        self,
        request: main_models.CreateFpShotDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFpShotDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.model_id):
            query['ModelId'] = request.model_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFpShotDB',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFpShotDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fp_shot_db(
        self,
        request: main_models.CreateFpShotDBRequest,
    ) -> main_models.CreateFpShotDBResponse:
        runtime = RuntimeOptions()
        return self.create_fp_shot_dbwith_options(request, runtime)

    async def create_fp_shot_db_async(
        self,
        request: main_models.CreateFpShotDBRequest,
    ) -> main_models.CreateFpShotDBResponse:
        runtime = RuntimeOptions()
        return await self.create_fp_shot_dbwith_options_async(request, runtime)

    def deactivate_media_workflow_with_options(
        self,
        request: main_models.DeactivateMediaWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeactivateMediaWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeactivateMediaWorkflow',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeactivateMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def deactivate_media_workflow_with_options_async(
        self,
        request: main_models.DeactivateMediaWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeactivateMediaWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeactivateMediaWorkflow',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeactivateMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deactivate_media_workflow(
        self,
        request: main_models.DeactivateMediaWorkflowRequest,
    ) -> main_models.DeactivateMediaWorkflowResponse:
        runtime = RuntimeOptions()
        return self.deactivate_media_workflow_with_options(request, runtime)

    async def deactivate_media_workflow_async(
        self,
        request: main_models.DeactivateMediaWorkflowRequest,
    ) -> main_models.DeactivateMediaWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.deactivate_media_workflow_with_options_async(request, runtime)

    def delete_custom_entity_with_options(
        self,
        request: main_models.DeleteCustomEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomEntityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.custom_entity_id):
            query['CustomEntityId'] = request.custom_entity_id
        if not DaraCore.is_null(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomEntity',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_entity_with_options_async(
        self,
        request: main_models.DeleteCustomEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomEntityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.custom_entity_id):
            query['CustomEntityId'] = request.custom_entity_id
        if not DaraCore.is_null(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomEntity',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_entity(
        self,
        request: main_models.DeleteCustomEntityRequest,
    ) -> main_models.DeleteCustomEntityResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_entity_with_options(request, runtime)

    async def delete_custom_entity_async(
        self,
        request: main_models.DeleteCustomEntityRequest,
    ) -> main_models.DeleteCustomEntityResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_entity_with_options_async(request, runtime)

    def delete_custom_group_with_options(
        self,
        request: main_models.DeleteCustomGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomGroup',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_group_with_options_async(
        self,
        request: main_models.DeleteCustomGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomGroup',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_group(
        self,
        request: main_models.DeleteCustomGroupRequest,
    ) -> main_models.DeleteCustomGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_group_with_options(request, runtime)

    async def delete_custom_group_async(
        self,
        request: main_models.DeleteCustomGroupRequest,
    ) -> main_models.DeleteCustomGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_group_with_options_async(request, runtime)

    def delete_custom_view_with_options(
        self,
        request: main_models.DeleteCustomViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.custom_entity_id):
            query['CustomEntityId'] = request.custom_entity_id
        if not DaraCore.is_null(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not DaraCore.is_null(request.custom_view_id):
            query['CustomViewId'] = request.custom_view_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomView',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_view_with_options_async(
        self,
        request: main_models.DeleteCustomViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.custom_entity_id):
            query['CustomEntityId'] = request.custom_entity_id
        if not DaraCore.is_null(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not DaraCore.is_null(request.custom_view_id):
            query['CustomViewId'] = request.custom_view_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomView',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_view(
        self,
        request: main_models.DeleteCustomViewRequest,
    ) -> main_models.DeleteCustomViewResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_view_with_options(request, runtime)

    async def delete_custom_view_async(
        self,
        request: main_models.DeleteCustomViewRequest,
    ) -> main_models.DeleteCustomViewResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_view_with_options_async(request, runtime)

    def delete_media_with_options(
        self,
        request: main_models.DeleteMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMedia',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_media_with_options_async(
        self,
        request: main_models.DeleteMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMedia',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_media(
        self,
        request: main_models.DeleteMediaRequest,
    ) -> main_models.DeleteMediaResponse:
        runtime = RuntimeOptions()
        return self.delete_media_with_options(request, runtime)

    async def delete_media_async(
        self,
        request: main_models.DeleteMediaRequest,
    ) -> main_models.DeleteMediaResponse:
        runtime = RuntimeOptions()
        return await self.delete_media_with_options_async(request, runtime)

    def delete_media_tag_with_options(
        self,
        request: main_models.DeleteMediaTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMediaTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMediaTag',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMediaTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_media_tag_with_options_async(
        self,
        request: main_models.DeleteMediaTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMediaTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMediaTag',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMediaTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_media_tag(
        self,
        request: main_models.DeleteMediaTagRequest,
    ) -> main_models.DeleteMediaTagResponse:
        runtime = RuntimeOptions()
        return self.delete_media_tag_with_options(request, runtime)

    async def delete_media_tag_async(
        self,
        request: main_models.DeleteMediaTagRequest,
    ) -> main_models.DeleteMediaTagResponse:
        runtime = RuntimeOptions()
        return await self.delete_media_tag_with_options_async(request, runtime)

    def delete_media_workflow_with_options(
        self,
        request: main_models.DeleteMediaWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMediaWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMediaWorkflow',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_media_workflow_with_options_async(
        self,
        request: main_models.DeleteMediaWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMediaWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMediaWorkflow',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_media_workflow(
        self,
        request: main_models.DeleteMediaWorkflowRequest,
    ) -> main_models.DeleteMediaWorkflowResponse:
        runtime = RuntimeOptions()
        return self.delete_media_workflow_with_options(request, runtime)

    async def delete_media_workflow_async(
        self,
        request: main_models.DeleteMediaWorkflowRequest,
    ) -> main_models.DeleteMediaWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.delete_media_workflow_with_options_async(request, runtime)

    def delete_pipeline_with_options(
        self,
        request: main_models.DeletePipelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePipeline',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_with_options_async(
        self,
        request: main_models.DeletePipelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePipeline',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipeline(
        self,
        request: main_models.DeletePipelineRequest,
    ) -> main_models.DeletePipelineResponse:
        runtime = RuntimeOptions()
        return self.delete_pipeline_with_options(request, runtime)

    async def delete_pipeline_async(
        self,
        request: main_models.DeletePipelineRequest,
    ) -> main_models.DeletePipelineResponse:
        runtime = RuntimeOptions()
        return await self.delete_pipeline_with_options_async(request, runtime)

    def delete_smarttag_template_with_options(
        self,
        request: main_models.DeleteSmarttagTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSmarttagTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSmarttagTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSmarttagTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_smarttag_template_with_options_async(
        self,
        request: main_models.DeleteSmarttagTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSmarttagTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSmarttagTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSmarttagTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_smarttag_template(
        self,
        request: main_models.DeleteSmarttagTemplateRequest,
    ) -> main_models.DeleteSmarttagTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_smarttag_template_with_options(request, runtime)

    async def delete_smarttag_template_async(
        self,
        request: main_models.DeleteSmarttagTemplateRequest,
    ) -> main_models.DeleteSmarttagTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_smarttag_template_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: main_models.DeleteTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2014-06-18',
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
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2014-06-18',
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

    def delete_water_mark_template_with_options(
        self,
        request: main_models.DeleteWaterMarkTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWaterMarkTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.water_mark_template_id):
            query['WaterMarkTemplateId'] = request.water_mark_template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWaterMarkTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWaterMarkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_water_mark_template_with_options_async(
        self,
        request: main_models.DeleteWaterMarkTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWaterMarkTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.water_mark_template_id):
            query['WaterMarkTemplateId'] = request.water_mark_template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWaterMarkTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWaterMarkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_water_mark_template(
        self,
        request: main_models.DeleteWaterMarkTemplateRequest,
    ) -> main_models.DeleteWaterMarkTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_water_mark_template_with_options(request, runtime)

    async def delete_water_mark_template_async(
        self,
        request: main_models.DeleteWaterMarkTemplateRequest,
    ) -> main_models.DeleteWaterMarkTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_water_mark_template_with_options_async(request, runtime)

    def im_audit_with_options(
        self,
        request: main_models.ImAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImAuditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.contents):
            query['Contents'] = request.contents
        if not DaraCore.is_null(request.images):
            query['Images'] = request.images
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scenes):
            query['Scenes'] = request.scenes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImAudit',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def im_audit_with_options_async(
        self,
        request: main_models.ImAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImAuditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.contents):
            query['Contents'] = request.contents
        if not DaraCore.is_null(request.images):
            query['Images'] = request.images
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scenes):
            query['Scenes'] = request.scenes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImAudit',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def im_audit(
        self,
        request: main_models.ImAuditRequest,
    ) -> main_models.ImAuditResponse:
        runtime = RuntimeOptions()
        return self.im_audit_with_options(request, runtime)

    async def im_audit_async(
        self,
        request: main_models.ImAuditRequest,
    ) -> main_models.ImAuditResponse:
        runtime = RuntimeOptions()
        return await self.im_audit_with_options_async(request, runtime)

    def import_fp_shot_job_with_options(
        self,
        request: main_models.ImportFpShotJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportFpShotJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not DaraCore.is_null(request.fp_import_config):
            query['FpImportConfig'] = request.fp_import_config
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportFpShotJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportFpShotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_fp_shot_job_with_options_async(
        self,
        request: main_models.ImportFpShotJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportFpShotJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not DaraCore.is_null(request.fp_import_config):
            query['FpImportConfig'] = request.fp_import_config
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportFpShotJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportFpShotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_fp_shot_job(
        self,
        request: main_models.ImportFpShotJobRequest,
    ) -> main_models.ImportFpShotJobResponse:
        runtime = RuntimeOptions()
        return self.import_fp_shot_job_with_options(request, runtime)

    async def import_fp_shot_job_async(
        self,
        request: main_models.ImportFpShotJobRequest,
    ) -> main_models.ImportFpShotJobResponse:
        runtime = RuntimeOptions()
        return await self.import_fp_shot_job_with_options_async(request, runtime)

    def list_all_media_bucket_with_options(
        self,
        request: main_models.ListAllMediaBucketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAllMediaBucketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAllMediaBucket',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllMediaBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_media_bucket_with_options_async(
        self,
        request: main_models.ListAllMediaBucketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAllMediaBucketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAllMediaBucket',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllMediaBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_media_bucket(
        self,
        request: main_models.ListAllMediaBucketRequest,
    ) -> main_models.ListAllMediaBucketResponse:
        runtime = RuntimeOptions()
        return self.list_all_media_bucket_with_options(request, runtime)

    async def list_all_media_bucket_async(
        self,
        request: main_models.ListAllMediaBucketRequest,
    ) -> main_models.ListAllMediaBucketResponse:
        runtime = RuntimeOptions()
        return await self.list_all_media_bucket_with_options_async(request, runtime)

    def list_custom_entities_with_options(
        self,
        request: main_models.ListCustomEntitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomEntitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomEntities',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_entities_with_options_async(
        self,
        request: main_models.ListCustomEntitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomEntitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomEntities',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_entities(
        self,
        request: main_models.ListCustomEntitiesRequest,
    ) -> main_models.ListCustomEntitiesResponse:
        runtime = RuntimeOptions()
        return self.list_custom_entities_with_options(request, runtime)

    async def list_custom_entities_async(
        self,
        request: main_models.ListCustomEntitiesRequest,
    ) -> main_models.ListCustomEntitiesResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_entities_with_options_async(request, runtime)

    def list_custom_groups_with_options(
        self,
        request: main_models.ListCustomGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomGroups',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_groups_with_options_async(
        self,
        request: main_models.ListCustomGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomGroups',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_groups(
        self,
        request: main_models.ListCustomGroupsRequest,
    ) -> main_models.ListCustomGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_custom_groups_with_options(request, runtime)

    async def list_custom_groups_async(
        self,
        request: main_models.ListCustomGroupsRequest,
    ) -> main_models.ListCustomGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_groups_with_options_async(request, runtime)

    def list_custom_persons_with_options(
        self,
        request: main_models.ListCustomPersonsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomPersonsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.person_id):
            query['PersonId'] = request.person_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomPersons',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomPersonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_persons_with_options_async(
        self,
        request: main_models.ListCustomPersonsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomPersonsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.person_id):
            query['PersonId'] = request.person_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomPersons',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomPersonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_persons(
        self,
        request: main_models.ListCustomPersonsRequest,
    ) -> main_models.ListCustomPersonsResponse:
        runtime = RuntimeOptions()
        return self.list_custom_persons_with_options(request, runtime)

    async def list_custom_persons_async(
        self,
        request: main_models.ListCustomPersonsRequest,
    ) -> main_models.ListCustomPersonsResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_persons_with_options_async(request, runtime)

    def list_custom_views_with_options(
        self,
        request: main_models.ListCustomViewsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomViewsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.custom_entity_id):
            query['CustomEntityId'] = request.custom_entity_id
        if not DaraCore.is_null(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomViews',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomViewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_views_with_options_async(
        self,
        request: main_models.ListCustomViewsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomViewsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.custom_entity_id):
            query['CustomEntityId'] = request.custom_entity_id
        if not DaraCore.is_null(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomViews',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomViewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_views(
        self,
        request: main_models.ListCustomViewsRequest,
    ) -> main_models.ListCustomViewsResponse:
        runtime = RuntimeOptions()
        return self.list_custom_views_with_options(request, runtime)

    async def list_custom_views_async(
        self,
        request: main_models.ListCustomViewsRequest,
    ) -> main_models.ListCustomViewsResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_views_with_options_async(request, runtime)

    def list_fp_shot_dbwith_options(
        self,
        request: main_models.ListFpShotDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFpShotDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fp_dbids):
            query['FpDBIds'] = request.fp_dbids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFpShotDB',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFpShotDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fp_shot_dbwith_options_async(
        self,
        request: main_models.ListFpShotDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFpShotDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fp_dbids):
            query['FpDBIds'] = request.fp_dbids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFpShotDB',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFpShotDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fp_shot_db(
        self,
        request: main_models.ListFpShotDBRequest,
    ) -> main_models.ListFpShotDBResponse:
        runtime = RuntimeOptions()
        return self.list_fp_shot_dbwith_options(request, runtime)

    async def list_fp_shot_db_async(
        self,
        request: main_models.ListFpShotDBRequest,
    ) -> main_models.ListFpShotDBResponse:
        runtime = RuntimeOptions()
        return await self.list_fp_shot_dbwith_options_async(request, runtime)

    def list_fp_shot_files_with_options(
        self,
        request: main_models.ListFpShotFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFpShotFilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFpShotFiles',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFpShotFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fp_shot_files_with_options_async(
        self,
        request: main_models.ListFpShotFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFpShotFilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFpShotFiles',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFpShotFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fp_shot_files(
        self,
        request: main_models.ListFpShotFilesRequest,
    ) -> main_models.ListFpShotFilesResponse:
        runtime = RuntimeOptions()
        return self.list_fp_shot_files_with_options(request, runtime)

    async def list_fp_shot_files_async(
        self,
        request: main_models.ListFpShotFilesRequest,
    ) -> main_models.ListFpShotFilesResponse:
        runtime = RuntimeOptions()
        return await self.list_fp_shot_files_with_options_async(request, runtime)

    def list_fp_shot_import_job_with_options(
        self,
        request: main_models.ListFpShotImportJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFpShotImportJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFpShotImportJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFpShotImportJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fp_shot_import_job_with_options_async(
        self,
        request: main_models.ListFpShotImportJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFpShotImportJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFpShotImportJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFpShotImportJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fp_shot_import_job(
        self,
        request: main_models.ListFpShotImportJobRequest,
    ) -> main_models.ListFpShotImportJobResponse:
        runtime = RuntimeOptions()
        return self.list_fp_shot_import_job_with_options(request, runtime)

    async def list_fp_shot_import_job_async(
        self,
        request: main_models.ListFpShotImportJobRequest,
    ) -> main_models.ListFpShotImportJobResponse:
        runtime = RuntimeOptions()
        return await self.list_fp_shot_import_job_with_options_async(request, runtime)

    def list_job_with_options(
        self,
        request: main_models.ListJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not DaraCore.is_null(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_with_options_async(
        self,
        request: main_models.ListJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not DaraCore.is_null(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job(
        self,
        request: main_models.ListJobRequest,
    ) -> main_models.ListJobResponse:
        runtime = RuntimeOptions()
        return self.list_job_with_options(request, runtime)

    async def list_job_async(
        self,
        request: main_models.ListJobRequest,
    ) -> main_models.ListJobResponse:
        runtime = RuntimeOptions()
        return await self.list_job_with_options_async(request, runtime)

    def list_media_workflow_executions_with_options(
        self,
        request: main_models.ListMediaWorkflowExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMediaWorkflowExecutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.input_file_url):
            query['InputFileURL'] = request.input_file_url
        if not DaraCore.is_null(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not DaraCore.is_null(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not DaraCore.is_null(request.media_workflow_name):
            query['MediaWorkflowName'] = request.media_workflow_name
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMediaWorkflowExecutions',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMediaWorkflowExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_media_workflow_executions_with_options_async(
        self,
        request: main_models.ListMediaWorkflowExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMediaWorkflowExecutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.input_file_url):
            query['InputFileURL'] = request.input_file_url
        if not DaraCore.is_null(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not DaraCore.is_null(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not DaraCore.is_null(request.media_workflow_name):
            query['MediaWorkflowName'] = request.media_workflow_name
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMediaWorkflowExecutions',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMediaWorkflowExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_media_workflow_executions(
        self,
        request: main_models.ListMediaWorkflowExecutionsRequest,
    ) -> main_models.ListMediaWorkflowExecutionsResponse:
        runtime = RuntimeOptions()
        return self.list_media_workflow_executions_with_options(request, runtime)

    async def list_media_workflow_executions_async(
        self,
        request: main_models.ListMediaWorkflowExecutionsRequest,
    ) -> main_models.ListMediaWorkflowExecutionsResponse:
        runtime = RuntimeOptions()
        return await self.list_media_workflow_executions_with_options_async(request, runtime)

    def query_analysis_job_list_with_options(
        self,
        request: main_models.QueryAnalysisJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAnalysisJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analysis_job_ids):
            query['AnalysisJobIds'] = request.analysis_job_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAnalysisJobList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAnalysisJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_analysis_job_list_with_options_async(
        self,
        request: main_models.QueryAnalysisJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAnalysisJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analysis_job_ids):
            query['AnalysisJobIds'] = request.analysis_job_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAnalysisJobList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAnalysisJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_analysis_job_list(
        self,
        request: main_models.QueryAnalysisJobListRequest,
    ) -> main_models.QueryAnalysisJobListResponse:
        runtime = RuntimeOptions()
        return self.query_analysis_job_list_with_options(request, runtime)

    async def query_analysis_job_list_async(
        self,
        request: main_models.QueryAnalysisJobListRequest,
    ) -> main_models.QueryAnalysisJobListResponse:
        runtime = RuntimeOptions()
        return await self.query_analysis_job_list_with_options_async(request, runtime)

    def query_copyright_extract_job_with_options(
        self,
        request: main_models.QueryCopyrightExtractJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCopyrightExtractJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCopyrightExtractJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCopyrightExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_copyright_extract_job_with_options_async(
        self,
        request: main_models.QueryCopyrightExtractJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCopyrightExtractJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCopyrightExtractJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCopyrightExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_copyright_extract_job(
        self,
        request: main_models.QueryCopyrightExtractJobRequest,
    ) -> main_models.QueryCopyrightExtractJobResponse:
        runtime = RuntimeOptions()
        return self.query_copyright_extract_job_with_options(request, runtime)

    async def query_copyright_extract_job_async(
        self,
        request: main_models.QueryCopyrightExtractJobRequest,
    ) -> main_models.QueryCopyrightExtractJobResponse:
        runtime = RuntimeOptions()
        return await self.query_copyright_extract_job_with_options_async(request, runtime)

    def query_copyright_job_with_options(
        self,
        request: main_models.QueryCopyrightJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCopyrightJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCopyrightJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCopyrightJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_copyright_job_with_options_async(
        self,
        request: main_models.QueryCopyrightJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCopyrightJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCopyrightJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCopyrightJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_copyright_job(
        self,
        request: main_models.QueryCopyrightJobRequest,
    ) -> main_models.QueryCopyrightJobResponse:
        runtime = RuntimeOptions()
        return self.query_copyright_job_with_options(request, runtime)

    async def query_copyright_job_async(
        self,
        request: main_models.QueryCopyrightJobRequest,
    ) -> main_models.QueryCopyrightJobResponse:
        runtime = RuntimeOptions()
        return await self.query_copyright_job_with_options_async(request, runtime)

    def query_fp_dbdelete_job_list_with_options(
        self,
        request: main_models.QueryFpDBDeleteJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFpDBDeleteJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFpDBDeleteJobList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFpDBDeleteJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fp_dbdelete_job_list_with_options_async(
        self,
        request: main_models.QueryFpDBDeleteJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFpDBDeleteJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFpDBDeleteJobList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFpDBDeleteJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_fp_dbdelete_job_list(
        self,
        request: main_models.QueryFpDBDeleteJobListRequest,
    ) -> main_models.QueryFpDBDeleteJobListResponse:
        runtime = RuntimeOptions()
        return self.query_fp_dbdelete_job_list_with_options(request, runtime)

    async def query_fp_dbdelete_job_list_async(
        self,
        request: main_models.QueryFpDBDeleteJobListRequest,
    ) -> main_models.QueryFpDBDeleteJobListResponse:
        runtime = RuntimeOptions()
        return await self.query_fp_dbdelete_job_list_with_options_async(request, runtime)

    def query_fp_file_delete_job_list_with_options(
        self,
        request: main_models.QueryFpFileDeleteJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFpFileDeleteJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFpFileDeleteJobList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFpFileDeleteJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fp_file_delete_job_list_with_options_async(
        self,
        request: main_models.QueryFpFileDeleteJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFpFileDeleteJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFpFileDeleteJobList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFpFileDeleteJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_fp_file_delete_job_list(
        self,
        request: main_models.QueryFpFileDeleteJobListRequest,
    ) -> main_models.QueryFpFileDeleteJobListResponse:
        runtime = RuntimeOptions()
        return self.query_fp_file_delete_job_list_with_options(request, runtime)

    async def query_fp_file_delete_job_list_async(
        self,
        request: main_models.QueryFpFileDeleteJobListRequest,
    ) -> main_models.QueryFpFileDeleteJobListResponse:
        runtime = RuntimeOptions()
        return await self.query_fp_file_delete_job_list_with_options_async(request, runtime)

    def query_fp_shot_job_list_with_options(
        self,
        request: main_models.QueryFpShotJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFpShotJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFpShotJobList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFpShotJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fp_shot_job_list_with_options_async(
        self,
        request: main_models.QueryFpShotJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFpShotJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFpShotJobList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFpShotJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_fp_shot_job_list(
        self,
        request: main_models.QueryFpShotJobListRequest,
    ) -> main_models.QueryFpShotJobListResponse:
        runtime = RuntimeOptions()
        return self.query_fp_shot_job_list_with_options(request, runtime)

    async def query_fp_shot_job_list_async(
        self,
        request: main_models.QueryFpShotJobListRequest,
    ) -> main_models.QueryFpShotJobListResponse:
        runtime = RuntimeOptions()
        return await self.query_fp_shot_job_list_with_options_async(request, runtime)

    def query_iproduction_job_with_options(
        self,
        request: main_models.QueryIProductionJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryIProductionJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryIProductionJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryIProductionJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_iproduction_job_with_options_async(
        self,
        request: main_models.QueryIProductionJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryIProductionJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryIProductionJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryIProductionJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_iproduction_job(
        self,
        request: main_models.QueryIProductionJobRequest,
    ) -> main_models.QueryIProductionJobResponse:
        runtime = RuntimeOptions()
        return self.query_iproduction_job_with_options(request, runtime)

    async def query_iproduction_job_async(
        self,
        request: main_models.QueryIProductionJobRequest,
    ) -> main_models.QueryIProductionJobResponse:
        runtime = RuntimeOptions()
        return await self.query_iproduction_job_with_options_async(request, runtime)

    def query_job_list_with_options(
        self,
        request: main_models.QueryJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryJobList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_job_list_with_options_async(
        self,
        request: main_models.QueryJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryJobList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_job_list(
        self,
        request: main_models.QueryJobListRequest,
    ) -> main_models.QueryJobListResponse:
        runtime = RuntimeOptions()
        return self.query_job_list_with_options(request, runtime)

    async def query_job_list_async(
        self,
        request: main_models.QueryJobListRequest,
    ) -> main_models.QueryJobListResponse:
        runtime = RuntimeOptions()
        return await self.query_job_list_with_options_async(request, runtime)

    def query_media_censor_job_detail_with_options(
        self,
        request: main_models.QueryMediaCensorJobDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMediaCensorJobDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMediaCensorJobDetail',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMediaCensorJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_censor_job_detail_with_options_async(
        self,
        request: main_models.QueryMediaCensorJobDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMediaCensorJobDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMediaCensorJobDetail',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMediaCensorJobDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_media_censor_job_detail(
        self,
        request: main_models.QueryMediaCensorJobDetailRequest,
    ) -> main_models.QueryMediaCensorJobDetailResponse:
        runtime = RuntimeOptions()
        return self.query_media_censor_job_detail_with_options(request, runtime)

    async def query_media_censor_job_detail_async(
        self,
        request: main_models.QueryMediaCensorJobDetailRequest,
    ) -> main_models.QueryMediaCensorJobDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_media_censor_job_detail_with_options_async(request, runtime)

    def query_media_censor_job_list_with_options(
        self,
        request: main_models.QueryMediaCensorJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMediaCensorJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMediaCensorJobList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMediaCensorJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_censor_job_list_with_options_async(
        self,
        request: main_models.QueryMediaCensorJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMediaCensorJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not DaraCore.is_null(request.job_ids):
            query['JobIds'] = request.job_ids
        if not DaraCore.is_null(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMediaCensorJobList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMediaCensorJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_media_censor_job_list(
        self,
        request: main_models.QueryMediaCensorJobListRequest,
    ) -> main_models.QueryMediaCensorJobListResponse:
        runtime = RuntimeOptions()
        return self.query_media_censor_job_list_with_options(request, runtime)

    async def query_media_censor_job_list_async(
        self,
        request: main_models.QueryMediaCensorJobListRequest,
    ) -> main_models.QueryMediaCensorJobListResponse:
        runtime = RuntimeOptions()
        return await self.query_media_censor_job_list_with_options_async(request, runtime)

    def query_media_info_job_list_with_options(
        self,
        request: main_models.QueryMediaInfoJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMediaInfoJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_info_job_ids):
            query['MediaInfoJobIds'] = request.media_info_job_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMediaInfoJobList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMediaInfoJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_info_job_list_with_options_async(
        self,
        request: main_models.QueryMediaInfoJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMediaInfoJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_info_job_ids):
            query['MediaInfoJobIds'] = request.media_info_job_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMediaInfoJobList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMediaInfoJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_media_info_job_list(
        self,
        request: main_models.QueryMediaInfoJobListRequest,
    ) -> main_models.QueryMediaInfoJobListResponse:
        runtime = RuntimeOptions()
        return self.query_media_info_job_list_with_options(request, runtime)

    async def query_media_info_job_list_async(
        self,
        request: main_models.QueryMediaInfoJobListRequest,
    ) -> main_models.QueryMediaInfoJobListResponse:
        runtime = RuntimeOptions()
        return await self.query_media_info_job_list_with_options_async(request, runtime)

    def query_media_list_with_options(
        self,
        request: main_models.QueryMediaListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMediaListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_media_info):
            query['IncludeMediaInfo'] = request.include_media_info
        if not DaraCore.is_null(request.include_play_list):
            query['IncludePlayList'] = request.include_play_list
        if not DaraCore.is_null(request.include_snapshot_list):
            query['IncludeSnapshotList'] = request.include_snapshot_list
        if not DaraCore.is_null(request.include_summary_list):
            query['IncludeSummaryList'] = request.include_summary_list
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMediaList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMediaListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_list_with_options_async(
        self,
        request: main_models.QueryMediaListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMediaListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_media_info):
            query['IncludeMediaInfo'] = request.include_media_info
        if not DaraCore.is_null(request.include_play_list):
            query['IncludePlayList'] = request.include_play_list
        if not DaraCore.is_null(request.include_snapshot_list):
            query['IncludeSnapshotList'] = request.include_snapshot_list
        if not DaraCore.is_null(request.include_summary_list):
            query['IncludeSummaryList'] = request.include_summary_list
        if not DaraCore.is_null(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMediaList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMediaListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_media_list(
        self,
        request: main_models.QueryMediaListRequest,
    ) -> main_models.QueryMediaListResponse:
        runtime = RuntimeOptions()
        return self.query_media_list_with_options(request, runtime)

    async def query_media_list_async(
        self,
        request: main_models.QueryMediaListRequest,
    ) -> main_models.QueryMediaListResponse:
        runtime = RuntimeOptions()
        return await self.query_media_list_with_options_async(request, runtime)

    def query_media_list_by_urlwith_options(
        self,
        request: main_models.QueryMediaListByURLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMediaListByURLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_urls):
            query['FileURLs'] = request.file_urls
        if not DaraCore.is_null(request.include_media_info):
            query['IncludeMediaInfo'] = request.include_media_info
        if not DaraCore.is_null(request.include_play_list):
            query['IncludePlayList'] = request.include_play_list
        if not DaraCore.is_null(request.include_snapshot_list):
            query['IncludeSnapshotList'] = request.include_snapshot_list
        if not DaraCore.is_null(request.include_summary_list):
            query['IncludeSummaryList'] = request.include_summary_list
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMediaListByURL',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMediaListByURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_list_by_urlwith_options_async(
        self,
        request: main_models.QueryMediaListByURLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMediaListByURLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_urls):
            query['FileURLs'] = request.file_urls
        if not DaraCore.is_null(request.include_media_info):
            query['IncludeMediaInfo'] = request.include_media_info
        if not DaraCore.is_null(request.include_play_list):
            query['IncludePlayList'] = request.include_play_list
        if not DaraCore.is_null(request.include_snapshot_list):
            query['IncludeSnapshotList'] = request.include_snapshot_list
        if not DaraCore.is_null(request.include_summary_list):
            query['IncludeSummaryList'] = request.include_summary_list
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMediaListByURL',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMediaListByURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_media_list_by_url(
        self,
        request: main_models.QueryMediaListByURLRequest,
    ) -> main_models.QueryMediaListByURLResponse:
        runtime = RuntimeOptions()
        return self.query_media_list_by_urlwith_options(request, runtime)

    async def query_media_list_by_url_async(
        self,
        request: main_models.QueryMediaListByURLRequest,
    ) -> main_models.QueryMediaListByURLResponse:
        runtime = RuntimeOptions()
        return await self.query_media_list_by_urlwith_options_async(request, runtime)

    def query_media_workflow_execution_list_with_options(
        self,
        request: main_models.QueryMediaWorkflowExecutionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMediaWorkflowExecutionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.run_ids):
            query['RunIds'] = request.run_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMediaWorkflowExecutionList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMediaWorkflowExecutionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_workflow_execution_list_with_options_async(
        self,
        request: main_models.QueryMediaWorkflowExecutionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMediaWorkflowExecutionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.run_ids):
            query['RunIds'] = request.run_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMediaWorkflowExecutionList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMediaWorkflowExecutionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_media_workflow_execution_list(
        self,
        request: main_models.QueryMediaWorkflowExecutionListRequest,
    ) -> main_models.QueryMediaWorkflowExecutionListResponse:
        runtime = RuntimeOptions()
        return self.query_media_workflow_execution_list_with_options(request, runtime)

    async def query_media_workflow_execution_list_async(
        self,
        request: main_models.QueryMediaWorkflowExecutionListRequest,
    ) -> main_models.QueryMediaWorkflowExecutionListResponse:
        runtime = RuntimeOptions()
        return await self.query_media_workflow_execution_list_with_options_async(request, runtime)

    def query_media_workflow_list_with_options(
        self,
        request: main_models.QueryMediaWorkflowListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMediaWorkflowListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_workflow_ids):
            query['MediaWorkflowIds'] = request.media_workflow_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMediaWorkflowList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMediaWorkflowListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_workflow_list_with_options_async(
        self,
        request: main_models.QueryMediaWorkflowListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMediaWorkflowListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_workflow_ids):
            query['MediaWorkflowIds'] = request.media_workflow_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMediaWorkflowList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMediaWorkflowListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_media_workflow_list(
        self,
        request: main_models.QueryMediaWorkflowListRequest,
    ) -> main_models.QueryMediaWorkflowListResponse:
        runtime = RuntimeOptions()
        return self.query_media_workflow_list_with_options(request, runtime)

    async def query_media_workflow_list_async(
        self,
        request: main_models.QueryMediaWorkflowListRequest,
    ) -> main_models.QueryMediaWorkflowListResponse:
        runtime = RuntimeOptions()
        return await self.query_media_workflow_list_with_options_async(request, runtime)

    def query_pipeline_list_with_options(
        self,
        request: main_models.QueryPipelineListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPipelineListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_ids):
            query['PipelineIds'] = request.pipeline_ids
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPipelineList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPipelineListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_pipeline_list_with_options_async(
        self,
        request: main_models.QueryPipelineListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPipelineListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_ids):
            query['PipelineIds'] = request.pipeline_ids
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPipelineList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPipelineListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_pipeline_list(
        self,
        request: main_models.QueryPipelineListRequest,
    ) -> main_models.QueryPipelineListResponse:
        runtime = RuntimeOptions()
        return self.query_pipeline_list_with_options(request, runtime)

    async def query_pipeline_list_async(
        self,
        request: main_models.QueryPipelineListRequest,
    ) -> main_models.QueryPipelineListResponse:
        runtime = RuntimeOptions()
        return await self.query_pipeline_list_with_options_async(request, runtime)

    def query_smarttag_job_with_options(
        self,
        request: main_models.QuerySmarttagJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmarttagJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmarttagJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmarttagJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_smarttag_job_with_options_async(
        self,
        request: main_models.QuerySmarttagJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmarttagJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmarttagJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmarttagJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_smarttag_job(
        self,
        request: main_models.QuerySmarttagJobRequest,
    ) -> main_models.QuerySmarttagJobResponse:
        runtime = RuntimeOptions()
        return self.query_smarttag_job_with_options(request, runtime)

    async def query_smarttag_job_async(
        self,
        request: main_models.QuerySmarttagJobRequest,
    ) -> main_models.QuerySmarttagJobResponse:
        runtime = RuntimeOptions()
        return await self.query_smarttag_job_with_options_async(request, runtime)

    def query_smarttag_template_list_with_options(
        self,
        request: main_models.QuerySmarttagTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmarttagTemplateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmarttagTemplateList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmarttagTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_smarttag_template_list_with_options_async(
        self,
        request: main_models.QuerySmarttagTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySmarttagTemplateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySmarttagTemplateList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySmarttagTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_smarttag_template_list(
        self,
        request: main_models.QuerySmarttagTemplateListRequest,
    ) -> main_models.QuerySmarttagTemplateListResponse:
        runtime = RuntimeOptions()
        return self.query_smarttag_template_list_with_options(request, runtime)

    async def query_smarttag_template_list_async(
        self,
        request: main_models.QuerySmarttagTemplateListRequest,
    ) -> main_models.QuerySmarttagTemplateListResponse:
        runtime = RuntimeOptions()
        return await self.query_smarttag_template_list_with_options_async(request, runtime)

    def query_snapshot_job_list_with_options(
        self,
        request: main_models.QuerySnapshotJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySnapshotJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not DaraCore.is_null(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.snapshot_job_ids):
            query['SnapshotJobIds'] = request.snapshot_job_ids
        if not DaraCore.is_null(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySnapshotJobList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySnapshotJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_snapshot_job_list_with_options_async(
        self,
        request: main_models.QuerySnapshotJobListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySnapshotJobListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not DaraCore.is_null(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not DaraCore.is_null(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.snapshot_job_ids):
            query['SnapshotJobIds'] = request.snapshot_job_ids
        if not DaraCore.is_null(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySnapshotJobList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySnapshotJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_snapshot_job_list(
        self,
        request: main_models.QuerySnapshotJobListRequest,
    ) -> main_models.QuerySnapshotJobListResponse:
        runtime = RuntimeOptions()
        return self.query_snapshot_job_list_with_options(request, runtime)

    async def query_snapshot_job_list_async(
        self,
        request: main_models.QuerySnapshotJobListRequest,
    ) -> main_models.QuerySnapshotJobListResponse:
        runtime = RuntimeOptions()
        return await self.query_snapshot_job_list_with_options_async(request, runtime)

    def query_template_list_with_options(
        self,
        request: main_models.QueryTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTemplateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTemplateList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_template_list_with_options_async(
        self,
        request: main_models.QueryTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTemplateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTemplateList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_template_list(
        self,
        request: main_models.QueryTemplateListRequest,
    ) -> main_models.QueryTemplateListResponse:
        runtime = RuntimeOptions()
        return self.query_template_list_with_options(request, runtime)

    async def query_template_list_async(
        self,
        request: main_models.QueryTemplateListRequest,
    ) -> main_models.QueryTemplateListResponse:
        runtime = RuntimeOptions()
        return await self.query_template_list_with_options_async(request, runtime)

    def query_trace_ab_job_with_options(
        self,
        request: main_models.QueryTraceAbJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTraceAbJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTraceAbJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTraceAbJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_trace_ab_job_with_options_async(
        self,
        request: main_models.QueryTraceAbJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTraceAbJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTraceAbJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTraceAbJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_trace_ab_job(
        self,
        request: main_models.QueryTraceAbJobRequest,
    ) -> main_models.QueryTraceAbJobResponse:
        runtime = RuntimeOptions()
        return self.query_trace_ab_job_with_options(request, runtime)

    async def query_trace_ab_job_async(
        self,
        request: main_models.QueryTraceAbJobRequest,
    ) -> main_models.QueryTraceAbJobResponse:
        runtime = RuntimeOptions()
        return await self.query_trace_ab_job_with_options_async(request, runtime)

    def query_trace_extract_job_with_options(
        self,
        request: main_models.QueryTraceExtractJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTraceExtractJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTraceExtractJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTraceExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_trace_extract_job_with_options_async(
        self,
        request: main_models.QueryTraceExtractJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTraceExtractJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTraceExtractJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTraceExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_trace_extract_job(
        self,
        request: main_models.QueryTraceExtractJobRequest,
    ) -> main_models.QueryTraceExtractJobResponse:
        runtime = RuntimeOptions()
        return self.query_trace_extract_job_with_options(request, runtime)

    async def query_trace_extract_job_async(
        self,
        request: main_models.QueryTraceExtractJobRequest,
    ) -> main_models.QueryTraceExtractJobResponse:
        runtime = RuntimeOptions()
        return await self.query_trace_extract_job_with_options_async(request, runtime)

    def query_trace_m3u_8job_with_options(
        self,
        request: main_models.QueryTraceM3u8JobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTraceM3u8JobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTraceM3u8Job',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTraceM3u8JobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_trace_m3u_8job_with_options_async(
        self,
        request: main_models.QueryTraceM3u8JobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTraceM3u8JobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTraceM3u8Job',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTraceM3u8JobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_trace_m3u_8job(
        self,
        request: main_models.QueryTraceM3u8JobRequest,
    ) -> main_models.QueryTraceM3u8JobResponse:
        runtime = RuntimeOptions()
        return self.query_trace_m3u_8job_with_options(request, runtime)

    async def query_trace_m3u_8job_async(
        self,
        request: main_models.QueryTraceM3u8JobRequest,
    ) -> main_models.QueryTraceM3u8JobResponse:
        runtime = RuntimeOptions()
        return await self.query_trace_m3u_8job_with_options_async(request, runtime)

    def query_water_mark_template_list_with_options(
        self,
        request: main_models.QueryWaterMarkTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWaterMarkTemplateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.water_mark_template_ids):
            query['WaterMarkTemplateIds'] = request.water_mark_template_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWaterMarkTemplateList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWaterMarkTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_water_mark_template_list_with_options_async(
        self,
        request: main_models.QueryWaterMarkTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWaterMarkTemplateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.water_mark_template_ids):
            query['WaterMarkTemplateIds'] = request.water_mark_template_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWaterMarkTemplateList',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWaterMarkTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_water_mark_template_list(
        self,
        request: main_models.QueryWaterMarkTemplateListRequest,
    ) -> main_models.QueryWaterMarkTemplateListResponse:
        runtime = RuntimeOptions()
        return self.query_water_mark_template_list_with_options(request, runtime)

    async def query_water_mark_template_list_async(
        self,
        request: main_models.QueryWaterMarkTemplateListRequest,
    ) -> main_models.QueryWaterMarkTemplateListResponse:
        runtime = RuntimeOptions()
        return await self.query_water_mark_template_list_with_options_async(request, runtime)

    def register_custom_face_with_options(
        self,
        request: main_models.RegisterCustomFaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterCustomFaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.person_id):
            query['PersonId'] = request.person_id
        if not DaraCore.is_null(request.person_name):
            query['PersonName'] = request.person_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterCustomFace',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterCustomFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_custom_face_with_options_async(
        self,
        request: main_models.RegisterCustomFaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterCustomFaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.person_id):
            query['PersonId'] = request.person_id
        if not DaraCore.is_null(request.person_name):
            query['PersonName'] = request.person_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterCustomFace',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterCustomFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_custom_face(
        self,
        request: main_models.RegisterCustomFaceRequest,
    ) -> main_models.RegisterCustomFaceResponse:
        runtime = RuntimeOptions()
        return self.register_custom_face_with_options(request, runtime)

    async def register_custom_face_async(
        self,
        request: main_models.RegisterCustomFaceRequest,
    ) -> main_models.RegisterCustomFaceResponse:
        runtime = RuntimeOptions()
        return await self.register_custom_face_with_options_async(request, runtime)

    def register_custom_view_with_options(
        self,
        request: main_models.RegisterCustomViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterCustomViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.custom_entity_id):
            query['CustomEntityId'] = request.custom_entity_id
        if not DaraCore.is_null(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.label_prompt):
            query['LabelPrompt'] = request.label_prompt
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterCustomView',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterCustomViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_custom_view_with_options_async(
        self,
        request: main_models.RegisterCustomViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterCustomViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.custom_entity_id):
            query['CustomEntityId'] = request.custom_entity_id
        if not DaraCore.is_null(request.custom_group_id):
            query['CustomGroupId'] = request.custom_group_id
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.label_prompt):
            query['LabelPrompt'] = request.label_prompt
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterCustomView',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterCustomViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_custom_view(
        self,
        request: main_models.RegisterCustomViewRequest,
    ) -> main_models.RegisterCustomViewResponse:
        runtime = RuntimeOptions()
        return self.register_custom_view_with_options(request, runtime)

    async def register_custom_view_async(
        self,
        request: main_models.RegisterCustomViewRequest,
    ) -> main_models.RegisterCustomViewResponse:
        runtime = RuntimeOptions()
        return await self.register_custom_view_with_options_async(request, runtime)

    def search_media_workflow_with_options(
        self,
        request: main_models.SearchMediaWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchMediaWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.state_list):
            query['StateList'] = request.state_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchMediaWorkflow',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_media_workflow_with_options_async(
        self,
        request: main_models.SearchMediaWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchMediaWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.state_list):
            query['StateList'] = request.state_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchMediaWorkflow',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_media_workflow(
        self,
        request: main_models.SearchMediaWorkflowRequest,
    ) -> main_models.SearchMediaWorkflowResponse:
        runtime = RuntimeOptions()
        return self.search_media_workflow_with_options(request, runtime)

    async def search_media_workflow_async(
        self,
        request: main_models.SearchMediaWorkflowRequest,
    ) -> main_models.SearchMediaWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.search_media_workflow_with_options_async(request, runtime)

    def search_pipeline_with_options(
        self,
        request: main_models.SearchPipelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchPipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchPipeline',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_pipeline_with_options_async(
        self,
        request: main_models.SearchPipelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchPipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchPipeline',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_pipeline(
        self,
        request: main_models.SearchPipelineRequest,
    ) -> main_models.SearchPipelineResponse:
        runtime = RuntimeOptions()
        return self.search_pipeline_with_options(request, runtime)

    async def search_pipeline_async(
        self,
        request: main_models.SearchPipelineRequest,
    ) -> main_models.SearchPipelineResponse:
        runtime = RuntimeOptions()
        return await self.search_pipeline_with_options_async(request, runtime)

    def search_template_with_options(
        self,
        request: main_models.SearchTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_template_with_options_async(
        self,
        request: main_models.SearchTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_template(
        self,
        request: main_models.SearchTemplateRequest,
    ) -> main_models.SearchTemplateResponse:
        runtime = RuntimeOptions()
        return self.search_template_with_options(request, runtime)

    async def search_template_async(
        self,
        request: main_models.SearchTemplateRequest,
    ) -> main_models.SearchTemplateResponse:
        runtime = RuntimeOptions()
        return await self.search_template_with_options_async(request, runtime)

    def search_water_mark_template_with_options(
        self,
        request: main_models.SearchWaterMarkTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchWaterMarkTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchWaterMarkTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchWaterMarkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_water_mark_template_with_options_async(
        self,
        request: main_models.SearchWaterMarkTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchWaterMarkTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchWaterMarkTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchWaterMarkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_water_mark_template(
        self,
        request: main_models.SearchWaterMarkTemplateRequest,
    ) -> main_models.SearchWaterMarkTemplateResponse:
        runtime = RuntimeOptions()
        return self.search_water_mark_template_with_options(request, runtime)

    async def search_water_mark_template_async(
        self,
        request: main_models.SearchWaterMarkTemplateRequest,
    ) -> main_models.SearchWaterMarkTemplateResponse:
        runtime = RuntimeOptions()
        return await self.search_water_mark_template_with_options_async(request, runtime)

    def submit_analysis_job_with_options(
        self,
        request: main_models.SubmitAnalysisJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAnalysisJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analysis_config):
            query['AnalysisConfig'] = request.analysis_config
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAnalysisJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAnalysisJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_analysis_job_with_options_async(
        self,
        request: main_models.SubmitAnalysisJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitAnalysisJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analysis_config):
            query['AnalysisConfig'] = request.analysis_config
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitAnalysisJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitAnalysisJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_analysis_job(
        self,
        request: main_models.SubmitAnalysisJobRequest,
    ) -> main_models.SubmitAnalysisJobResponse:
        runtime = RuntimeOptions()
        return self.submit_analysis_job_with_options(request, runtime)

    async def submit_analysis_job_async(
        self,
        request: main_models.SubmitAnalysisJobRequest,
    ) -> main_models.SubmitAnalysisJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_analysis_job_with_options_async(request, runtime)

    def submit_copyright_extract_job_with_options(
        self,
        request: main_models.SubmitCopyrightExtractJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitCopyrightExtractJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_back):
            query['CallBack'] = request.call_back
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitCopyrightExtractJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitCopyrightExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_copyright_extract_job_with_options_async(
        self,
        request: main_models.SubmitCopyrightExtractJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitCopyrightExtractJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_back):
            query['CallBack'] = request.call_back
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitCopyrightExtractJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitCopyrightExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_copyright_extract_job(
        self,
        request: main_models.SubmitCopyrightExtractJobRequest,
    ) -> main_models.SubmitCopyrightExtractJobResponse:
        runtime = RuntimeOptions()
        return self.submit_copyright_extract_job_with_options(request, runtime)

    async def submit_copyright_extract_job_async(
        self,
        request: main_models.SubmitCopyrightExtractJobRequest,
    ) -> main_models.SubmitCopyrightExtractJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_copyright_extract_job_with_options_async(request, runtime)

    def submit_copyright_job_with_options(
        self,
        request: main_models.SubmitCopyrightJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitCopyrightJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_back):
            query['CallBack'] = request.call_back
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.output):
            query['Output'] = request.output
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.total_time):
            query['TotalTime'] = request.total_time
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitCopyrightJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitCopyrightJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_copyright_job_with_options_async(
        self,
        request: main_models.SubmitCopyrightJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitCopyrightJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_back):
            query['CallBack'] = request.call_back
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.output):
            query['Output'] = request.output
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.total_time):
            query['TotalTime'] = request.total_time
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitCopyrightJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitCopyrightJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_copyright_job(
        self,
        request: main_models.SubmitCopyrightJobRequest,
    ) -> main_models.SubmitCopyrightJobResponse:
        runtime = RuntimeOptions()
        return self.submit_copyright_job_with_options(request, runtime)

    async def submit_copyright_job_async(
        self,
        request: main_models.SubmitCopyrightJobRequest,
    ) -> main_models.SubmitCopyrightJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_copyright_job_with_options_async(request, runtime)

    def submit_fp_dbdelete_job_with_options(
        self,
        request: main_models.SubmitFpDBDeleteJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitFpDBDeleteJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.del_type):
            query['DelType'] = request.del_type
        if not DaraCore.is_null(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitFpDBDeleteJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitFpDBDeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_fp_dbdelete_job_with_options_async(
        self,
        request: main_models.SubmitFpDBDeleteJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitFpDBDeleteJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.del_type):
            query['DelType'] = request.del_type
        if not DaraCore.is_null(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitFpDBDeleteJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitFpDBDeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_fp_dbdelete_job(
        self,
        request: main_models.SubmitFpDBDeleteJobRequest,
    ) -> main_models.SubmitFpDBDeleteJobResponse:
        runtime = RuntimeOptions()
        return self.submit_fp_dbdelete_job_with_options(request, runtime)

    async def submit_fp_dbdelete_job_async(
        self,
        request: main_models.SubmitFpDBDeleteJobRequest,
    ) -> main_models.SubmitFpDBDeleteJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_fp_dbdelete_job_with_options_async(request, runtime)

    def submit_fp_file_delete_job_with_options(
        self,
        request: main_models.SubmitFpFileDeleteJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitFpFileDeleteJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_ids):
            query['FileIds'] = request.file_ids
        if not DaraCore.is_null(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.primary_keys):
            query['PrimaryKeys'] = request.primary_keys
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitFpFileDeleteJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitFpFileDeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_fp_file_delete_job_with_options_async(
        self,
        request: main_models.SubmitFpFileDeleteJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitFpFileDeleteJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_ids):
            query['FileIds'] = request.file_ids
        if not DaraCore.is_null(request.fp_dbid):
            query['FpDBId'] = request.fp_dbid
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.primary_keys):
            query['PrimaryKeys'] = request.primary_keys
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitFpFileDeleteJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitFpFileDeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_fp_file_delete_job(
        self,
        request: main_models.SubmitFpFileDeleteJobRequest,
    ) -> main_models.SubmitFpFileDeleteJobResponse:
        runtime = RuntimeOptions()
        return self.submit_fp_file_delete_job_with_options(request, runtime)

    async def submit_fp_file_delete_job_async(
        self,
        request: main_models.SubmitFpFileDeleteJobRequest,
    ) -> main_models.SubmitFpFileDeleteJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_fp_file_delete_job_with_options_async(request, runtime)

    def submit_fp_shot_job_with_options(
        self,
        request: main_models.SubmitFpShotJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitFpShotJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fp_shot_config):
            query['FpShotConfig'] = request.fp_shot_config
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitFpShotJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitFpShotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_fp_shot_job_with_options_async(
        self,
        request: main_models.SubmitFpShotJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitFpShotJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fp_shot_config):
            query['FpShotConfig'] = request.fp_shot_config
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitFpShotJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitFpShotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_fp_shot_job(
        self,
        request: main_models.SubmitFpShotJobRequest,
    ) -> main_models.SubmitFpShotJobResponse:
        runtime = RuntimeOptions()
        return self.submit_fp_shot_job_with_options(request, runtime)

    async def submit_fp_shot_job_async(
        self,
        request: main_models.SubmitFpShotJobRequest,
    ) -> main_models.SubmitFpShotJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_fp_shot_job_with_options_async(request, runtime)

    def submit_iproduction_job_with_options(
        self,
        request: main_models.SubmitIProductionJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitIProductionJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.job_params):
            query['JobParams'] = request.job_params
        if not DaraCore.is_null(request.model_id):
            query['ModelId'] = request.model_id
        if not DaraCore.is_null(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not DaraCore.is_null(request.output):
            query['Output'] = request.output
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schedule_params):
            query['ScheduleParams'] = request.schedule_params
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitIProductionJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitIProductionJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_iproduction_job_with_options_async(
        self,
        request: main_models.SubmitIProductionJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitIProductionJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.job_params):
            query['JobParams'] = request.job_params
        if not DaraCore.is_null(request.model_id):
            query['ModelId'] = request.model_id
        if not DaraCore.is_null(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not DaraCore.is_null(request.output):
            query['Output'] = request.output
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schedule_params):
            query['ScheduleParams'] = request.schedule_params
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitIProductionJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitIProductionJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_iproduction_job(
        self,
        request: main_models.SubmitIProductionJobRequest,
    ) -> main_models.SubmitIProductionJobResponse:
        runtime = RuntimeOptions()
        return self.submit_iproduction_job_with_options(request, runtime)

    async def submit_iproduction_job_async(
        self,
        request: main_models.SubmitIProductionJobRequest,
    ) -> main_models.SubmitIProductionJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_iproduction_job_with_options_async(request, runtime)

    def submit_image_copyright_with_options(
        self,
        request: main_models.SubmitImageCopyrightRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitImageCopyrightResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.output):
            query['Output'] = request.output
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitImageCopyright',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitImageCopyrightResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_image_copyright_with_options_async(
        self,
        request: main_models.SubmitImageCopyrightRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitImageCopyrightResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.output):
            query['Output'] = request.output
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitImageCopyright',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitImageCopyrightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_image_copyright(
        self,
        request: main_models.SubmitImageCopyrightRequest,
    ) -> main_models.SubmitImageCopyrightResponse:
        runtime = RuntimeOptions()
        return self.submit_image_copyright_with_options(request, runtime)

    async def submit_image_copyright_async(
        self,
        request: main_models.SubmitImageCopyrightRequest,
    ) -> main_models.SubmitImageCopyrightResponse:
        runtime = RuntimeOptions()
        return await self.submit_image_copyright_with_options_async(request, runtime)

    def submit_jobs_with_options(
        self,
        request: main_models.SubmitJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.output_bucket):
            query['OutputBucket'] = request.output_bucket
        if not DaraCore.is_null(request.output_location):
            query['OutputLocation'] = request.output_location
        if not DaraCore.is_null(request.outputs):
            query['Outputs'] = request.outputs
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitJobs',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_jobs_with_options_async(
        self,
        request: main_models.SubmitJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.output_bucket):
            query['OutputBucket'] = request.output_bucket
        if not DaraCore.is_null(request.output_location):
            query['OutputLocation'] = request.output_location
        if not DaraCore.is_null(request.outputs):
            query['Outputs'] = request.outputs
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitJobs',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_jobs(
        self,
        request: main_models.SubmitJobsRequest,
    ) -> main_models.SubmitJobsResponse:
        runtime = RuntimeOptions()
        return self.submit_jobs_with_options(request, runtime)

    async def submit_jobs_async(
        self,
        request: main_models.SubmitJobsRequest,
    ) -> main_models.SubmitJobsResponse:
        runtime = RuntimeOptions()
        return await self.submit_jobs_with_options_async(request, runtime)

    def submit_media_censor_job_with_options(
        self,
        request: main_models.SubmitMediaCensorJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitMediaCensorJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.barrages):
            query['Barrages'] = request.barrages
        if not DaraCore.is_null(request.cover_images):
            query['CoverImages'] = request.cover_images
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.external_url):
            query['ExternalUrl'] = request.external_url
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.video_censor_config):
            query['VideoCensorConfig'] = request.video_censor_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitMediaCensorJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitMediaCensorJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_media_censor_job_with_options_async(
        self,
        request: main_models.SubmitMediaCensorJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitMediaCensorJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.barrages):
            query['Barrages'] = request.barrages
        if not DaraCore.is_null(request.cover_images):
            query['CoverImages'] = request.cover_images
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.external_url):
            query['ExternalUrl'] = request.external_url
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.video_censor_config):
            query['VideoCensorConfig'] = request.video_censor_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitMediaCensorJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitMediaCensorJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_media_censor_job(
        self,
        request: main_models.SubmitMediaCensorJobRequest,
    ) -> main_models.SubmitMediaCensorJobResponse:
        runtime = RuntimeOptions()
        return self.submit_media_censor_job_with_options(request, runtime)

    async def submit_media_censor_job_async(
        self,
        request: main_models.SubmitMediaCensorJobRequest,
    ) -> main_models.SubmitMediaCensorJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_media_censor_job_with_options_async(request, runtime)

    def submit_media_info_job_with_options(
        self,
        request: main_models.SubmitMediaInfoJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitMediaInfoJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.async_):
            query['Async'] = request.async_
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitMediaInfoJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitMediaInfoJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_media_info_job_with_options_async(
        self,
        request: main_models.SubmitMediaInfoJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitMediaInfoJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.async_):
            query['Async'] = request.async_
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitMediaInfoJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitMediaInfoJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_media_info_job(
        self,
        request: main_models.SubmitMediaInfoJobRequest,
    ) -> main_models.SubmitMediaInfoJobResponse:
        runtime = RuntimeOptions()
        return self.submit_media_info_job_with_options(request, runtime)

    async def submit_media_info_job_async(
        self,
        request: main_models.SubmitMediaInfoJobRequest,
    ) -> main_models.SubmitMediaInfoJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_media_info_job_with_options_async(request, runtime)

    def submit_smarttag_job_with_options(
        self,
        request: main_models.SubmitSmarttagJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSmarttagJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.content_addr):
            query['ContentAddr'] = request.content_addr
        if not DaraCore.is_null(request.content_type):
            query['ContentType'] = request.content_type
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSmarttagJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSmarttagJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_smarttag_job_with_options_async(
        self,
        request: main_models.SubmitSmarttagJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSmarttagJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.content_addr):
            query['ContentAddr'] = request.content_addr
        if not DaraCore.is_null(request.content_type):
            query['ContentType'] = request.content_type
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSmarttagJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSmarttagJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_smarttag_job(
        self,
        request: main_models.SubmitSmarttagJobRequest,
    ) -> main_models.SubmitSmarttagJobResponse:
        runtime = RuntimeOptions()
        return self.submit_smarttag_job_with_options(request, runtime)

    async def submit_smarttag_job_async(
        self,
        request: main_models.SubmitSmarttagJobRequest,
    ) -> main_models.SubmitSmarttagJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_smarttag_job_with_options_async(request, runtime)

    def submit_snapshot_job_with_options(
        self,
        request: main_models.SubmitSnapshotJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSnapshotJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.snapshot_config):
            query['SnapshotConfig'] = request.snapshot_config
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSnapshotJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_snapshot_job_with_options_async(
        self,
        request: main_models.SubmitSnapshotJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSnapshotJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.snapshot_config):
            query['SnapshotConfig'] = request.snapshot_config
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSnapshotJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSnapshotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_snapshot_job(
        self,
        request: main_models.SubmitSnapshotJobRequest,
    ) -> main_models.SubmitSnapshotJobResponse:
        runtime = RuntimeOptions()
        return self.submit_snapshot_job_with_options(request, runtime)

    async def submit_snapshot_job_async(
        self,
        request: main_models.SubmitSnapshotJobRequest,
    ) -> main_models.SubmitSnapshotJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_snapshot_job_with_options_async(request, runtime)

    def submit_trace_ab_job_with_options(
        self,
        request: main_models.SubmitTraceAbJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTraceAbJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_back):
            query['CallBack'] = request.call_back
        if not DaraCore.is_null(request.cipher_base_64ed):
            query['CipherBase64ed'] = request.cipher_base_64ed
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.output):
            query['Output'] = request.output
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.total_time):
            query['TotalTime'] = request.total_time
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTraceAbJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTraceAbJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_trace_ab_job_with_options_async(
        self,
        request: main_models.SubmitTraceAbJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTraceAbJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_back):
            query['CallBack'] = request.call_back
        if not DaraCore.is_null(request.cipher_base_64ed):
            query['CipherBase64ed'] = request.cipher_base_64ed
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.output):
            query['Output'] = request.output
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.total_time):
            query['TotalTime'] = request.total_time
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTraceAbJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTraceAbJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_trace_ab_job(
        self,
        request: main_models.SubmitTraceAbJobRequest,
    ) -> main_models.SubmitTraceAbJobResponse:
        runtime = RuntimeOptions()
        return self.submit_trace_ab_job_with_options(request, runtime)

    async def submit_trace_ab_job_async(
        self,
        request: main_models.SubmitTraceAbJobRequest,
    ) -> main_models.SubmitTraceAbJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_trace_ab_job_with_options_async(request, runtime)

    def submit_trace_extract_job_with_options(
        self,
        request: main_models.SubmitTraceExtractJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTraceExtractJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_back):
            query['CallBack'] = request.call_back
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTraceExtractJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTraceExtractJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_trace_extract_job_with_options_async(
        self,
        request: main_models.SubmitTraceExtractJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTraceExtractJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_back):
            query['CallBack'] = request.call_back
        if not DaraCore.is_null(request.input):
            query['Input'] = request.input
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTraceExtractJob',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTraceExtractJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_trace_extract_job(
        self,
        request: main_models.SubmitTraceExtractJobRequest,
    ) -> main_models.SubmitTraceExtractJobResponse:
        runtime = RuntimeOptions()
        return self.submit_trace_extract_job_with_options(request, runtime)

    async def submit_trace_extract_job_async(
        self,
        request: main_models.SubmitTraceExtractJobRequest,
    ) -> main_models.SubmitTraceExtractJobResponse:
        runtime = RuntimeOptions()
        return await self.submit_trace_extract_job_with_options_async(request, runtime)

    def submit_trace_m3u_8job_with_options(
        self,
        request: main_models.SubmitTraceM3u8JobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTraceM3u8JobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_uri):
            query['KeyUri'] = request.key_uri
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.output):
            query['Output'] = request.output
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.trace):
            query['Trace'] = request.trace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTraceM3u8Job',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTraceM3u8JobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_trace_m3u_8job_with_options_async(
        self,
        request: main_models.SubmitTraceM3u8JobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitTraceM3u8JobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_uri):
            query['KeyUri'] = request.key_uri
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.output):
            query['Output'] = request.output
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.trace):
            query['Trace'] = request.trace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitTraceM3u8Job',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitTraceM3u8JobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_trace_m3u_8job(
        self,
        request: main_models.SubmitTraceM3u8JobRequest,
    ) -> main_models.SubmitTraceM3u8JobResponse:
        runtime = RuntimeOptions()
        return self.submit_trace_m3u_8job_with_options(request, runtime)

    async def submit_trace_m3u_8job_async(
        self,
        request: main_models.SubmitTraceM3u8JobRequest,
    ) -> main_models.SubmitTraceM3u8JobResponse:
        runtime = RuntimeOptions()
        return await self.submit_trace_m3u_8job_with_options_async(request, runtime)

    def tag_custom_person_with_options(
        self,
        request: main_models.TagCustomPersonRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagCustomPersonResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_description):
            query['CategoryDescription'] = request.category_description
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.category_name):
            query['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.person_description):
            query['PersonDescription'] = request.person_description
        if not DaraCore.is_null(request.person_id):
            query['PersonId'] = request.person_id
        if not DaraCore.is_null(request.person_name):
            query['PersonName'] = request.person_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagCustomPerson',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagCustomPersonResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_custom_person_with_options_async(
        self,
        request: main_models.TagCustomPersonRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagCustomPersonResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_description):
            query['CategoryDescription'] = request.category_description
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.category_name):
            query['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.person_description):
            query['PersonDescription'] = request.person_description
        if not DaraCore.is_null(request.person_id):
            query['PersonId'] = request.person_id
        if not DaraCore.is_null(request.person_name):
            query['PersonName'] = request.person_name
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagCustomPerson',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagCustomPersonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_custom_person(
        self,
        request: main_models.TagCustomPersonRequest,
    ) -> main_models.TagCustomPersonResponse:
        runtime = RuntimeOptions()
        return self.tag_custom_person_with_options(request, runtime)

    async def tag_custom_person_async(
        self,
        request: main_models.TagCustomPersonRequest,
    ) -> main_models.TagCustomPersonResponse:
        runtime = RuntimeOptions()
        return await self.tag_custom_person_with_options_async(request, runtime)

    def unbind_input_bucket_with_options(
        self,
        request: main_models.UnbindInputBucketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindInputBucketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket):
            query['Bucket'] = request.bucket
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_arn):
            query['RoleArn'] = request.role_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindInputBucket',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindInputBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_input_bucket_with_options_async(
        self,
        request: main_models.UnbindInputBucketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindInputBucketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket):
            query['Bucket'] = request.bucket
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_arn):
            query['RoleArn'] = request.role_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindInputBucket',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindInputBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_input_bucket(
        self,
        request: main_models.UnbindInputBucketRequest,
    ) -> main_models.UnbindInputBucketResponse:
        runtime = RuntimeOptions()
        return self.unbind_input_bucket_with_options(request, runtime)

    async def unbind_input_bucket_async(
        self,
        request: main_models.UnbindInputBucketRequest,
    ) -> main_models.UnbindInputBucketResponse:
        runtime = RuntimeOptions()
        return await self.unbind_input_bucket_with_options_async(request, runtime)

    def unbind_output_bucket_with_options(
        self,
        request: main_models.UnbindOutputBucketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindOutputBucketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket):
            query['Bucket'] = request.bucket
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindOutputBucket',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindOutputBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_output_bucket_with_options_async(
        self,
        request: main_models.UnbindOutputBucketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindOutputBucketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket):
            query['Bucket'] = request.bucket
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindOutputBucket',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindOutputBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_output_bucket(
        self,
        request: main_models.UnbindOutputBucketRequest,
    ) -> main_models.UnbindOutputBucketResponse:
        runtime = RuntimeOptions()
        return self.unbind_output_bucket_with_options(request, runtime)

    async def unbind_output_bucket_async(
        self,
        request: main_models.UnbindOutputBucketRequest,
    ) -> main_models.UnbindOutputBucketResponse:
        runtime = RuntimeOptions()
        return await self.unbind_output_bucket_with_options_async(request, runtime)

    def unregister_custom_face_with_options(
        self,
        request: main_models.UnregisterCustomFaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnregisterCustomFaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.face_id):
            query['FaceId'] = request.face_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.person_id):
            query['PersonId'] = request.person_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnregisterCustomFace',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnregisterCustomFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unregister_custom_face_with_options_async(
        self,
        request: main_models.UnregisterCustomFaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnregisterCustomFaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.face_id):
            query['FaceId'] = request.face_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.person_id):
            query['PersonId'] = request.person_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnregisterCustomFace',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnregisterCustomFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unregister_custom_face(
        self,
        request: main_models.UnregisterCustomFaceRequest,
    ) -> main_models.UnregisterCustomFaceResponse:
        runtime = RuntimeOptions()
        return self.unregister_custom_face_with_options(request, runtime)

    async def unregister_custom_face_async(
        self,
        request: main_models.UnregisterCustomFaceRequest,
    ) -> main_models.UnregisterCustomFaceResponse:
        runtime = RuntimeOptions()
        return await self.unregister_custom_face_with_options_async(request, runtime)

    def update_media_with_options(
        self,
        request: main_models.UpdateMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMedia',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_with_options_async(
        self,
        request: main_models.UpdateMediaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMedia',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_media(
        self,
        request: main_models.UpdateMediaRequest,
    ) -> main_models.UpdateMediaResponse:
        runtime = RuntimeOptions()
        return self.update_media_with_options(request, runtime)

    async def update_media_async(
        self,
        request: main_models.UpdateMediaRequest,
    ) -> main_models.UpdateMediaResponse:
        runtime = RuntimeOptions()
        return await self.update_media_with_options_async(request, runtime)

    def update_media_category_with_options(
        self,
        request: main_models.UpdateMediaCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMediaCategory',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMediaCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_category_with_options_async(
        self,
        request: main_models.UpdateMediaCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cate_id):
            query['CateId'] = request.cate_id
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMediaCategory',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMediaCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_media_category(
        self,
        request: main_models.UpdateMediaCategoryRequest,
    ) -> main_models.UpdateMediaCategoryResponse:
        runtime = RuntimeOptions()
        return self.update_media_category_with_options(request, runtime)

    async def update_media_category_async(
        self,
        request: main_models.UpdateMediaCategoryRequest,
    ) -> main_models.UpdateMediaCategoryResponse:
        runtime = RuntimeOptions()
        return await self.update_media_category_with_options_async(request, runtime)

    def update_media_cover_with_options(
        self,
        request: main_models.UpdateMediaCoverRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaCoverResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMediaCover',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMediaCoverResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_cover_with_options_async(
        self,
        request: main_models.UpdateMediaCoverRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaCoverResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMediaCover',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMediaCoverResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_media_cover(
        self,
        request: main_models.UpdateMediaCoverRequest,
    ) -> main_models.UpdateMediaCoverResponse:
        runtime = RuntimeOptions()
        return self.update_media_cover_with_options(request, runtime)

    async def update_media_cover_async(
        self,
        request: main_models.UpdateMediaCoverRequest,
    ) -> main_models.UpdateMediaCoverResponse:
        runtime = RuntimeOptions()
        return await self.update_media_cover_with_options_async(request, runtime)

    def update_media_publish_state_with_options(
        self,
        request: main_models.UpdateMediaPublishStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaPublishStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.publish):
            query['Publish'] = request.publish
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMediaPublishState',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMediaPublishStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_publish_state_with_options_async(
        self,
        request: main_models.UpdateMediaPublishStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaPublishStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_id):
            query['MediaId'] = request.media_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.publish):
            query['Publish'] = request.publish
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMediaPublishState',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMediaPublishStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_media_publish_state(
        self,
        request: main_models.UpdateMediaPublishStateRequest,
    ) -> main_models.UpdateMediaPublishStateResponse:
        runtime = RuntimeOptions()
        return self.update_media_publish_state_with_options(request, runtime)

    async def update_media_publish_state_async(
        self,
        request: main_models.UpdateMediaPublishStateRequest,
    ) -> main_models.UpdateMediaPublishStateResponse:
        runtime = RuntimeOptions()
        return await self.update_media_publish_state_with_options_async(request, runtime)

    def update_media_workflow_with_options(
        self,
        request: main_models.UpdateMediaWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.topology):
            query['Topology'] = request.topology
        if not DaraCore.is_null(request.trigger_mode):
            query['TriggerMode'] = request.trigger_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMediaWorkflow',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMediaWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_workflow_with_options_async(
        self,
        request: main_models.UpdateMediaWorkflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaWorkflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.topology):
            query['Topology'] = request.topology
        if not DaraCore.is_null(request.trigger_mode):
            query['TriggerMode'] = request.trigger_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMediaWorkflow',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMediaWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_media_workflow(
        self,
        request: main_models.UpdateMediaWorkflowRequest,
    ) -> main_models.UpdateMediaWorkflowResponse:
        runtime = RuntimeOptions()
        return self.update_media_workflow_with_options(request, runtime)

    async def update_media_workflow_async(
        self,
        request: main_models.UpdateMediaWorkflowRequest,
    ) -> main_models.UpdateMediaWorkflowResponse:
        runtime = RuntimeOptions()
        return await self.update_media_workflow_with_options_async(request, runtime)

    def update_media_workflow_trigger_mode_with_options(
        self,
        request: main_models.UpdateMediaWorkflowTriggerModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaWorkflowTriggerModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.trigger_mode):
            query['TriggerMode'] = request.trigger_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMediaWorkflowTriggerMode',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMediaWorkflowTriggerModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_workflow_trigger_mode_with_options_async(
        self,
        request: main_models.UpdateMediaWorkflowTriggerModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMediaWorkflowTriggerModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.media_workflow_id):
            query['MediaWorkflowId'] = request.media_workflow_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.trigger_mode):
            query['TriggerMode'] = request.trigger_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMediaWorkflowTriggerMode',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMediaWorkflowTriggerModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_media_workflow_trigger_mode(
        self,
        request: main_models.UpdateMediaWorkflowTriggerModeRequest,
    ) -> main_models.UpdateMediaWorkflowTriggerModeResponse:
        runtime = RuntimeOptions()
        return self.update_media_workflow_trigger_mode_with_options(request, runtime)

    async def update_media_workflow_trigger_mode_async(
        self,
        request: main_models.UpdateMediaWorkflowTriggerModeRequest,
    ) -> main_models.UpdateMediaWorkflowTriggerModeResponse:
        runtime = RuntimeOptions()
        return await self.update_media_workflow_trigger_mode_with_options_async(request, runtime)

    def update_pipeline_with_options(
        self,
        request: main_models.UpdatePipelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extend_config):
            query['ExtendConfig'] = request.extend_config
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.notify_config):
            query['NotifyConfig'] = request.notify_config
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePipeline',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_with_options_async(
        self,
        request: main_models.UpdatePipelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extend_config):
            query['ExtendConfig'] = request.extend_config
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.notify_config):
            query['NotifyConfig'] = request.notify_config
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePipeline',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline(
        self,
        request: main_models.UpdatePipelineRequest,
    ) -> main_models.UpdatePipelineResponse:
        runtime = RuntimeOptions()
        return self.update_pipeline_with_options(request, runtime)

    async def update_pipeline_async(
        self,
        request: main_models.UpdatePipelineRequest,
    ) -> main_models.UpdatePipelineResponse:
        runtime = RuntimeOptions()
        return await self.update_pipeline_with_options_async(request, runtime)

    def update_smarttag_template_with_options(
        self,
        request: main_models.UpdateSmarttagTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmarttagTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analyse_types):
            query['AnalyseTypes'] = request.analyse_types
        if not DaraCore.is_null(request.face_category_ids):
            query['FaceCategoryIds'] = request.face_category_ids
        if not DaraCore.is_null(request.face_custom_params_config):
            query['FaceCustomParamsConfig'] = request.face_custom_params_config
        if not DaraCore.is_null(request.industry):
            query['Industry'] = request.industry
        if not DaraCore.is_null(request.is_default):
            query['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.keyword_config):
            query['KeywordConfig'] = request.keyword_config
        if not DaraCore.is_null(request.knowledge_config):
            query['KnowledgeConfig'] = request.knowledge_config
        if not DaraCore.is_null(request.label_type):
            query['LabelType'] = request.label_type
        if not DaraCore.is_null(request.label_version):
            query['LabelVersion'] = request.label_version
        if not DaraCore.is_null(request.landmark_group_ids):
            query['LandmarkGroupIds'] = request.landmark_group_ids
        if not DaraCore.is_null(request.object_group_ids):
            query['ObjectGroupIds'] = request.object_group_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmarttagTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmarttagTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smarttag_template_with_options_async(
        self,
        request: main_models.UpdateSmarttagTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSmarttagTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.analyse_types):
            query['AnalyseTypes'] = request.analyse_types
        if not DaraCore.is_null(request.face_category_ids):
            query['FaceCategoryIds'] = request.face_category_ids
        if not DaraCore.is_null(request.face_custom_params_config):
            query['FaceCustomParamsConfig'] = request.face_custom_params_config
        if not DaraCore.is_null(request.industry):
            query['Industry'] = request.industry
        if not DaraCore.is_null(request.is_default):
            query['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.keyword_config):
            query['KeywordConfig'] = request.keyword_config
        if not DaraCore.is_null(request.knowledge_config):
            query['KnowledgeConfig'] = request.knowledge_config
        if not DaraCore.is_null(request.label_type):
            query['LabelType'] = request.label_type
        if not DaraCore.is_null(request.label_version):
            query['LabelVersion'] = request.label_version
        if not DaraCore.is_null(request.landmark_group_ids):
            query['LandmarkGroupIds'] = request.landmark_group_ids
        if not DaraCore.is_null(request.object_group_ids):
            query['ObjectGroupIds'] = request.object_group_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        if not DaraCore.is_null(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSmarttagTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSmarttagTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smarttag_template(
        self,
        request: main_models.UpdateSmarttagTemplateRequest,
    ) -> main_models.UpdateSmarttagTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_smarttag_template_with_options(request, runtime)

    async def update_smarttag_template_async(
        self,
        request: main_models.UpdateSmarttagTemplateRequest,
    ) -> main_models.UpdateSmarttagTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_smarttag_template_with_options_async(request, runtime)

    def update_template_with_options(
        self,
        request: main_models.UpdateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio):
            query['Audio'] = request.audio
        if not DaraCore.is_null(request.container):
            query['Container'] = request.container
        if not DaraCore.is_null(request.mux_config):
            query['MuxConfig'] = request.mux_config
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.trans_config):
            query['TransConfig'] = request.trans_config
        if not DaraCore.is_null(request.video):
            query['Video'] = request.video
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_with_options_async(
        self,
        request: main_models.UpdateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audio):
            query['Audio'] = request.audio
        if not DaraCore.is_null(request.container):
            query['Container'] = request.container
        if not DaraCore.is_null(request.mux_config):
            query['MuxConfig'] = request.mux_config
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.trans_config):
            query['TransConfig'] = request.trans_config
        if not DaraCore.is_null(request.video):
            query['Video'] = request.video
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template(
        self,
        request: main_models.UpdateTemplateRequest,
    ) -> main_models.UpdateTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    async def update_template_async(
        self,
        request: main_models.UpdateTemplateRequest,
    ) -> main_models.UpdateTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_template_with_options_async(request, runtime)

    def update_water_mark_template_with_options(
        self,
        request: main_models.UpdateWaterMarkTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWaterMarkTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.water_mark_template_id):
            query['WaterMarkTemplateId'] = request.water_mark_template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWaterMarkTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWaterMarkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_water_mark_template_with_options_async(
        self,
        request: main_models.UpdateWaterMarkTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWaterMarkTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.water_mark_template_id):
            query['WaterMarkTemplateId'] = request.water_mark_template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWaterMarkTemplate',
            version = '2014-06-18',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWaterMarkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_water_mark_template(
        self,
        request: main_models.UpdateWaterMarkTemplateRequest,
    ) -> main_models.UpdateWaterMarkTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_water_mark_template_with_options(request, runtime)

    async def update_water_mark_template_async(
        self,
        request: main_models.UpdateWaterMarkTemplateRequest,
    ) -> main_models.UpdateWaterMarkTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_water_mark_template_with_options_async(request, runtime)
