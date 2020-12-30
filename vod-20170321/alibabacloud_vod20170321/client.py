# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_vod20170321 import models as vod_20170321_models
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
            'cn-hangzhou': 'vod.cn-shanghai.aliyuncs.com',
            'ap-northeast-2-pop': 'vod.aliyuncs.com',
            'ap-southeast-2': 'vod.aliyuncs.com',
            'ap-southeast-3': 'vod.aliyuncs.com',
            'cn-beijing-finance-1': 'vod.aliyuncs.com',
            'cn-beijing-finance-pop': 'vod.aliyuncs.com',
            'cn-beijing-gov-1': 'vod.aliyuncs.com',
            'cn-beijing-nu16-b01': 'vod.aliyuncs.com',
            'cn-chengdu': 'vod.aliyuncs.com',
            'cn-edge-1': 'vod.aliyuncs.com',
            'cn-fujian': 'vod.aliyuncs.com',
            'cn-haidian-cm12-c01': 'vod.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'vod.aliyuncs.com',
            'cn-hangzhou-finance': 'vod.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'vod.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'vod.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'vod.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'vod.aliyuncs.com',
            'cn-hangzhou-test-306': 'vod.aliyuncs.com',
            'cn-hongkong-finance-pop': 'vod.aliyuncs.com',
            'cn-huhehaote': 'vod.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'vod.aliyuncs.com',
            'cn-qingdao': 'vod.aliyuncs.com',
            'cn-qingdao-nebula': 'vod.aliyuncs.com',
            'cn-shanghai-et15-b01': 'vod.aliyuncs.com',
            'cn-shanghai-et2-b01': 'vod.aliyuncs.com',
            'cn-shanghai-finance-1': 'vod.aliyuncs.com',
            'cn-shanghai-inner': 'vod.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'vod.aliyuncs.com',
            'cn-shenzhen-finance-1': 'vod.aliyuncs.com',
            'cn-shenzhen-inner': 'vod.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'vod.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'vod.aliyuncs.com',
            'cn-wuhan': 'vod.aliyuncs.com',
            'cn-wulanchabu': 'vod.aliyuncs.com',
            'cn-yushanfang': 'vod.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'vod.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'vod.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'vod.aliyuncs.com',
            'eu-west-1-oxs': 'vod.aliyuncs.com',
            'me-east-1': 'vod.aliyuncs.com',
            'rus-west-1-pop': 'vod.aliyuncs.com',
            'us-east-1': 'vod.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('vod', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_aitemplate_with_options(
        self,
        request: vod_20170321_models.AddAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.AddAITemplateResponse().from_map(
            self.do_rpcrequest('AddAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_aitemplate_with_options_async(
        self,
        request: vod_20170321_models.AddAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.AddAITemplateResponse().from_map(
            await self.do_rpcrequest_async('AddAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_aitemplate(
        self,
        request: vod_20170321_models.AddAITemplateRequest,
    ) -> vod_20170321_models.AddAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_aitemplate_with_options(request, runtime)

    async def add_aitemplate_async(
        self,
        request: vod_20170321_models.AddAITemplateRequest,
    ) -> vod_20170321_models.AddAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_aitemplate_with_options_async(request, runtime)

    def add_category_with_options(
        self,
        request: vod_20170321_models.AddCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.AddCategoryResponse().from_map(
            self.do_rpcrequest('AddCategory', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_category_with_options_async(
        self,
        request: vod_20170321_models.AddCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.AddCategoryResponse().from_map(
            await self.do_rpcrequest_async('AddCategory', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_category(
        self,
        request: vod_20170321_models.AddCategoryRequest,
    ) -> vod_20170321_models.AddCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_category_with_options(request, runtime)

    async def add_category_async(
        self,
        request: vod_20170321_models.AddCategoryRequest,
    ) -> vod_20170321_models.AddCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_category_with_options_async(request, runtime)

    def add_editing_project_with_options(
        self,
        request: vod_20170321_models.AddEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.AddEditingProjectResponse().from_map(
            self.do_rpcrequest('AddEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_editing_project_with_options_async(
        self,
        request: vod_20170321_models.AddEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.AddEditingProjectResponse().from_map(
            await self.do_rpcrequest_async('AddEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_editing_project(
        self,
        request: vod_20170321_models.AddEditingProjectRequest,
    ) -> vod_20170321_models.AddEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_editing_project_with_options(request, runtime)

    async def add_editing_project_async(
        self,
        request: vod_20170321_models.AddEditingProjectRequest,
    ) -> vod_20170321_models.AddEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_editing_project_with_options_async(request, runtime)

    def add_transcode_template_group_with_options(
        self,
        request: vod_20170321_models.AddTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.AddTranscodeTemplateGroupResponse().from_map(
            self.do_rpcrequest('AddTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_transcode_template_group_with_options_async(
        self,
        request: vod_20170321_models.AddTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.AddTranscodeTemplateGroupResponse().from_map(
            await self.do_rpcrequest_async('AddTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_transcode_template_group(
        self,
        request: vod_20170321_models.AddTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.AddTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_transcode_template_group_with_options(request, runtime)

    async def add_transcode_template_group_async(
        self,
        request: vod_20170321_models.AddTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.AddTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_transcode_template_group_with_options_async(request, runtime)

    def add_vod_domain_with_options(
        self,
        request: vod_20170321_models.AddVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.AddVodDomainResponse().from_map(
            self.do_rpcrequest('AddVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_vod_domain_with_options_async(
        self,
        request: vod_20170321_models.AddVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.AddVodDomainResponse().from_map(
            await self.do_rpcrequest_async('AddVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_vod_domain(
        self,
        request: vod_20170321_models.AddVodDomainRequest,
    ) -> vod_20170321_models.AddVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_vod_domain_with_options(request, runtime)

    async def add_vod_domain_async(
        self,
        request: vod_20170321_models.AddVodDomainRequest,
    ) -> vod_20170321_models.AddVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_vod_domain_with_options_async(request, runtime)

    def add_vod_template_with_options(
        self,
        request: vod_20170321_models.AddVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.AddVodTemplateResponse().from_map(
            self.do_rpcrequest('AddVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_vod_template_with_options_async(
        self,
        request: vod_20170321_models.AddVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.AddVodTemplateResponse().from_map(
            await self.do_rpcrequest_async('AddVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_vod_template(
        self,
        request: vod_20170321_models.AddVodTemplateRequest,
    ) -> vod_20170321_models.AddVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_vod_template_with_options(request, runtime)

    async def add_vod_template_async(
        self,
        request: vod_20170321_models.AddVodTemplateRequest,
    ) -> vod_20170321_models.AddVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_vod_template_with_options_async(request, runtime)

    def add_watermark_with_options(
        self,
        request: vod_20170321_models.AddWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.AddWatermarkResponse().from_map(
            self.do_rpcrequest('AddWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_watermark_with_options_async(
        self,
        request: vod_20170321_models.AddWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AddWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.AddWatermarkResponse().from_map(
            await self.do_rpcrequest_async('AddWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_watermark(
        self,
        request: vod_20170321_models.AddWatermarkRequest,
    ) -> vod_20170321_models.AddWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_watermark_with_options(request, runtime)

    async def add_watermark_async(
        self,
        request: vod_20170321_models.AddWatermarkRequest,
    ) -> vod_20170321_models.AddWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_watermark_with_options_async(request, runtime)

    def attach_app_policy_to_identity_with_options(
        self,
        request: vod_20170321_models.AttachAppPolicyToIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AttachAppPolicyToIdentityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.AttachAppPolicyToIdentityResponse().from_map(
            self.do_rpcrequest('AttachAppPolicyToIdentity', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_app_policy_to_identity_with_options_async(
        self,
        request: vod_20170321_models.AttachAppPolicyToIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.AttachAppPolicyToIdentityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.AttachAppPolicyToIdentityResponse().from_map(
            await self.do_rpcrequest_async('AttachAppPolicyToIdentity', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_app_policy_to_identity(
        self,
        request: vod_20170321_models.AttachAppPolicyToIdentityRequest,
    ) -> vod_20170321_models.AttachAppPolicyToIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_app_policy_to_identity_with_options(request, runtime)

    async def attach_app_policy_to_identity_async(
        self,
        request: vod_20170321_models.AttachAppPolicyToIdentityRequest,
    ) -> vod_20170321_models.AttachAppPolicyToIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_app_policy_to_identity_with_options_async(request, runtime)

    def batch_set_vod_domain_configs_with_options(
        self,
        request: vod_20170321_models.BatchSetVodDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.BatchSetVodDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.BatchSetVodDomainConfigsResponse().from_map(
            self.do_rpcrequest('BatchSetVodDomainConfigs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_set_vod_domain_configs_with_options_async(
        self,
        request: vod_20170321_models.BatchSetVodDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.BatchSetVodDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.BatchSetVodDomainConfigsResponse().from_map(
            await self.do_rpcrequest_async('BatchSetVodDomainConfigs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_set_vod_domain_configs(
        self,
        request: vod_20170321_models.BatchSetVodDomainConfigsRequest,
    ) -> vod_20170321_models.BatchSetVodDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_set_vod_domain_configs_with_options(request, runtime)

    async def batch_set_vod_domain_configs_async(
        self,
        request: vod_20170321_models.BatchSetVodDomainConfigsRequest,
    ) -> vod_20170321_models.BatchSetVodDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_vod_domain_configs_with_options_async(request, runtime)

    def batch_start_vod_domain_with_options(
        self,
        request: vod_20170321_models.BatchStartVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.BatchStartVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.BatchStartVodDomainResponse().from_map(
            self.do_rpcrequest('BatchStartVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_start_vod_domain_with_options_async(
        self,
        request: vod_20170321_models.BatchStartVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.BatchStartVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.BatchStartVodDomainResponse().from_map(
            await self.do_rpcrequest_async('BatchStartVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_start_vod_domain(
        self,
        request: vod_20170321_models.BatchStartVodDomainRequest,
    ) -> vod_20170321_models.BatchStartVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_start_vod_domain_with_options(request, runtime)

    async def batch_start_vod_domain_async(
        self,
        request: vod_20170321_models.BatchStartVodDomainRequest,
    ) -> vod_20170321_models.BatchStartVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_start_vod_domain_with_options_async(request, runtime)

    def batch_stop_vod_domain_with_options(
        self,
        request: vod_20170321_models.BatchStopVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.BatchStopVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.BatchStopVodDomainResponse().from_map(
            self.do_rpcrequest('BatchStopVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_stop_vod_domain_with_options_async(
        self,
        request: vod_20170321_models.BatchStopVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.BatchStopVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.BatchStopVodDomainResponse().from_map(
            await self.do_rpcrequest_async('BatchStopVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_stop_vod_domain(
        self,
        request: vod_20170321_models.BatchStopVodDomainRequest,
    ) -> vod_20170321_models.BatchStopVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_vod_domain_with_options(request, runtime)

    async def batch_stop_vod_domain_async(
        self,
        request: vod_20170321_models.BatchStopVodDomainRequest,
    ) -> vod_20170321_models.BatchStopVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_stop_vod_domain_with_options_async(request, runtime)

    def create_app_info_with_options(
        self,
        request: vod_20170321_models.CreateAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.CreateAppInfoResponse().from_map(
            self.do_rpcrequest('CreateAppInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_app_info_with_options_async(
        self,
        request: vod_20170321_models.CreateAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.CreateAppInfoResponse().from_map(
            await self.do_rpcrequest_async('CreateAppInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_app_info(
        self,
        request: vod_20170321_models.CreateAppInfoRequest,
    ) -> vod_20170321_models.CreateAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_info_with_options(request, runtime)

    async def create_app_info_async(
        self,
        request: vod_20170321_models.CreateAppInfoRequest,
    ) -> vod_20170321_models.CreateAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_info_with_options_async(request, runtime)

    def create_audit_with_options(
        self,
        request: vod_20170321_models.CreateAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateAuditResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.CreateAuditResponse().from_map(
            self.do_rpcrequest('CreateAudit', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_audit_with_options_async(
        self,
        request: vod_20170321_models.CreateAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateAuditResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.CreateAuditResponse().from_map(
            await self.do_rpcrequest_async('CreateAudit', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_audit(
        self,
        request: vod_20170321_models.CreateAuditRequest,
    ) -> vod_20170321_models.CreateAuditResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_audit_with_options(request, runtime)

    async def create_audit_async(
        self,
        request: vod_20170321_models.CreateAuditRequest,
    ) -> vod_20170321_models.CreateAuditResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_audit_with_options_async(request, runtime)

    def create_upload_attached_media_with_options(
        self,
        request: vod_20170321_models.CreateUploadAttachedMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateUploadAttachedMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.CreateUploadAttachedMediaResponse().from_map(
            self.do_rpcrequest('CreateUploadAttachedMedia', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_upload_attached_media_with_options_async(
        self,
        request: vod_20170321_models.CreateUploadAttachedMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateUploadAttachedMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.CreateUploadAttachedMediaResponse().from_map(
            await self.do_rpcrequest_async('CreateUploadAttachedMedia', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_upload_attached_media(
        self,
        request: vod_20170321_models.CreateUploadAttachedMediaRequest,
    ) -> vod_20170321_models.CreateUploadAttachedMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_upload_attached_media_with_options(request, runtime)

    async def create_upload_attached_media_async(
        self,
        request: vod_20170321_models.CreateUploadAttachedMediaRequest,
    ) -> vod_20170321_models.CreateUploadAttachedMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_upload_attached_media_with_options_async(request, runtime)

    def create_upload_image_with_options(
        self,
        request: vod_20170321_models.CreateUploadImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateUploadImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.CreateUploadImageResponse().from_map(
            self.do_rpcrequest('CreateUploadImage', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_upload_image_with_options_async(
        self,
        request: vod_20170321_models.CreateUploadImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateUploadImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.CreateUploadImageResponse().from_map(
            await self.do_rpcrequest_async('CreateUploadImage', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_upload_image(
        self,
        request: vod_20170321_models.CreateUploadImageRequest,
    ) -> vod_20170321_models.CreateUploadImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_upload_image_with_options(request, runtime)

    async def create_upload_image_async(
        self,
        request: vod_20170321_models.CreateUploadImageRequest,
    ) -> vod_20170321_models.CreateUploadImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_upload_image_with_options_async(request, runtime)

    def create_upload_video_with_options(
        self,
        request: vod_20170321_models.CreateUploadVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateUploadVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.CreateUploadVideoResponse().from_map(
            self.do_rpcrequest('CreateUploadVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_upload_video_with_options_async(
        self,
        request: vod_20170321_models.CreateUploadVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.CreateUploadVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.CreateUploadVideoResponse().from_map(
            await self.do_rpcrequest_async('CreateUploadVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_upload_video(
        self,
        request: vod_20170321_models.CreateUploadVideoRequest,
    ) -> vod_20170321_models.CreateUploadVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_upload_video_with_options(request, runtime)

    async def create_upload_video_async(
        self,
        request: vod_20170321_models.CreateUploadVideoRequest,
    ) -> vod_20170321_models.CreateUploadVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_upload_video_with_options_async(request, runtime)

    def delete_aiimage_infos_with_options(
        self,
        request: vod_20170321_models.DeleteAIImageInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteAIImageInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteAIImageInfosResponse().from_map(
            self.do_rpcrequest('DeleteAIImageInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_aiimage_infos_with_options_async(
        self,
        request: vod_20170321_models.DeleteAIImageInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteAIImageInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteAIImageInfosResponse().from_map(
            await self.do_rpcrequest_async('DeleteAIImageInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_aiimage_infos(
        self,
        request: vod_20170321_models.DeleteAIImageInfosRequest,
    ) -> vod_20170321_models.DeleteAIImageInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_aiimage_infos_with_options(request, runtime)

    async def delete_aiimage_infos_async(
        self,
        request: vod_20170321_models.DeleteAIImageInfosRequest,
    ) -> vod_20170321_models.DeleteAIImageInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_aiimage_infos_with_options_async(request, runtime)

    def delete_aitemplate_with_options(
        self,
        request: vod_20170321_models.DeleteAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteAITemplateResponse().from_map(
            self.do_rpcrequest('DeleteAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_aitemplate_with_options_async(
        self,
        request: vod_20170321_models.DeleteAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteAITemplateResponse().from_map(
            await self.do_rpcrequest_async('DeleteAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_aitemplate(
        self,
        request: vod_20170321_models.DeleteAITemplateRequest,
    ) -> vod_20170321_models.DeleteAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_aitemplate_with_options(request, runtime)

    async def delete_aitemplate_async(
        self,
        request: vod_20170321_models.DeleteAITemplateRequest,
    ) -> vod_20170321_models.DeleteAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_aitemplate_with_options_async(request, runtime)

    def delete_app_info_with_options(
        self,
        request: vod_20170321_models.DeleteAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteAppInfoResponse().from_map(
            self.do_rpcrequest('DeleteAppInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_app_info_with_options_async(
        self,
        request: vod_20170321_models.DeleteAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteAppInfoResponse().from_map(
            await self.do_rpcrequest_async('DeleteAppInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_app_info(
        self,
        request: vod_20170321_models.DeleteAppInfoRequest,
    ) -> vod_20170321_models.DeleteAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_info_with_options(request, runtime)

    async def delete_app_info_async(
        self,
        request: vod_20170321_models.DeleteAppInfoRequest,
    ) -> vod_20170321_models.DeleteAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_info_with_options_async(request, runtime)

    def delete_attached_media_with_options(
        self,
        request: vod_20170321_models.DeleteAttachedMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteAttachedMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteAttachedMediaResponse().from_map(
            self.do_rpcrequest('DeleteAttachedMedia', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_attached_media_with_options_async(
        self,
        request: vod_20170321_models.DeleteAttachedMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteAttachedMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteAttachedMediaResponse().from_map(
            await self.do_rpcrequest_async('DeleteAttachedMedia', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_attached_media(
        self,
        request: vod_20170321_models.DeleteAttachedMediaRequest,
    ) -> vod_20170321_models.DeleteAttachedMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_attached_media_with_options(request, runtime)

    async def delete_attached_media_async(
        self,
        request: vod_20170321_models.DeleteAttachedMediaRequest,
    ) -> vod_20170321_models.DeleteAttachedMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_attached_media_with_options_async(request, runtime)

    def delete_category_with_options(
        self,
        request: vod_20170321_models.DeleteCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteCategoryResponse().from_map(
            self.do_rpcrequest('DeleteCategory', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_category_with_options_async(
        self,
        request: vod_20170321_models.DeleteCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteCategoryResponse().from_map(
            await self.do_rpcrequest_async('DeleteCategory', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_category(
        self,
        request: vod_20170321_models.DeleteCategoryRequest,
    ) -> vod_20170321_models.DeleteCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_category_with_options(request, runtime)

    async def delete_category_async(
        self,
        request: vod_20170321_models.DeleteCategoryRequest,
    ) -> vod_20170321_models.DeleteCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_category_with_options_async(request, runtime)

    def delete_dynamic_image_with_options(
        self,
        request: vod_20170321_models.DeleteDynamicImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteDynamicImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteDynamicImageResponse().from_map(
            self.do_rpcrequest('DeleteDynamicImage', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dynamic_image_with_options_async(
        self,
        request: vod_20170321_models.DeleteDynamicImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteDynamicImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteDynamicImageResponse().from_map(
            await self.do_rpcrequest_async('DeleteDynamicImage', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dynamic_image(
        self,
        request: vod_20170321_models.DeleteDynamicImageRequest,
    ) -> vod_20170321_models.DeleteDynamicImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dynamic_image_with_options(request, runtime)

    async def delete_dynamic_image_async(
        self,
        request: vod_20170321_models.DeleteDynamicImageRequest,
    ) -> vod_20170321_models.DeleteDynamicImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dynamic_image_with_options_async(request, runtime)

    def delete_editing_project_with_options(
        self,
        request: vod_20170321_models.DeleteEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteEditingProjectResponse().from_map(
            self.do_rpcrequest('DeleteEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_editing_project_with_options_async(
        self,
        request: vod_20170321_models.DeleteEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteEditingProjectResponse().from_map(
            await self.do_rpcrequest_async('DeleteEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_editing_project(
        self,
        request: vod_20170321_models.DeleteEditingProjectRequest,
    ) -> vod_20170321_models.DeleteEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_editing_project_with_options(request, runtime)

    async def delete_editing_project_async(
        self,
        request: vod_20170321_models.DeleteEditingProjectRequest,
    ) -> vod_20170321_models.DeleteEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_editing_project_with_options_async(request, runtime)

    def delete_image_with_options(
        self,
        request: vod_20170321_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteImageResponse().from_map(
            self.do_rpcrequest('DeleteImage', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_image_with_options_async(
        self,
        request: vod_20170321_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteImageResponse().from_map(
            await self.do_rpcrequest_async('DeleteImage', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_image(
        self,
        request: vod_20170321_models.DeleteImageRequest,
    ) -> vod_20170321_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    async def delete_image_async(
        self,
        request: vod_20170321_models.DeleteImageRequest,
    ) -> vod_20170321_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_with_options_async(request, runtime)

    def delete_message_callback_with_options(
        self,
        request: vod_20170321_models.DeleteMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteMessageCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteMessageCallbackResponse().from_map(
            self.do_rpcrequest('DeleteMessageCallback', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_message_callback_with_options_async(
        self,
        request: vod_20170321_models.DeleteMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteMessageCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteMessageCallbackResponse().from_map(
            await self.do_rpcrequest_async('DeleteMessageCallback', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_message_callback(
        self,
        request: vod_20170321_models.DeleteMessageCallbackRequest,
    ) -> vod_20170321_models.DeleteMessageCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_message_callback_with_options(request, runtime)

    async def delete_message_callback_async(
        self,
        request: vod_20170321_models.DeleteMessageCallbackRequest,
    ) -> vod_20170321_models.DeleteMessageCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_message_callback_with_options_async(request, runtime)

    def delete_mezzanines_with_options(
        self,
        request: vod_20170321_models.DeleteMezzaninesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteMezzaninesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteMezzaninesResponse().from_map(
            self.do_rpcrequest('DeleteMezzanines', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_mezzanines_with_options_async(
        self,
        request: vod_20170321_models.DeleteMezzaninesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteMezzaninesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteMezzaninesResponse().from_map(
            await self.do_rpcrequest_async('DeleteMezzanines', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_mezzanines(
        self,
        request: vod_20170321_models.DeleteMezzaninesRequest,
    ) -> vod_20170321_models.DeleteMezzaninesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_mezzanines_with_options(request, runtime)

    async def delete_mezzanines_async(
        self,
        request: vod_20170321_models.DeleteMezzaninesRequest,
    ) -> vod_20170321_models.DeleteMezzaninesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_mezzanines_with_options_async(request, runtime)

    def delete_multipart_upload_with_options(
        self,
        request: vod_20170321_models.DeleteMultipartUploadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteMultipartUploadResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteMultipartUploadResponse().from_map(
            self.do_rpcrequest('DeleteMultipartUpload', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_multipart_upload_with_options_async(
        self,
        request: vod_20170321_models.DeleteMultipartUploadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteMultipartUploadResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteMultipartUploadResponse().from_map(
            await self.do_rpcrequest_async('DeleteMultipartUpload', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_multipart_upload(
        self,
        request: vod_20170321_models.DeleteMultipartUploadRequest,
    ) -> vod_20170321_models.DeleteMultipartUploadResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_multipart_upload_with_options(request, runtime)

    async def delete_multipart_upload_async(
        self,
        request: vod_20170321_models.DeleteMultipartUploadRequest,
    ) -> vod_20170321_models.DeleteMultipartUploadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_multipart_upload_with_options_async(request, runtime)

    def delete_stream_with_options(
        self,
        request: vod_20170321_models.DeleteStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteStreamResponse().from_map(
            self.do_rpcrequest('DeleteStream', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_stream_with_options_async(
        self,
        request: vod_20170321_models.DeleteStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteStreamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteStreamResponse().from_map(
            await self.do_rpcrequest_async('DeleteStream', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_stream(
        self,
        request: vod_20170321_models.DeleteStreamRequest,
    ) -> vod_20170321_models.DeleteStreamResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_stream_with_options(request, runtime)

    async def delete_stream_async(
        self,
        request: vod_20170321_models.DeleteStreamRequest,
    ) -> vod_20170321_models.DeleteStreamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_stream_with_options_async(request, runtime)

    def delete_transcode_template_group_with_options(
        self,
        request: vod_20170321_models.DeleteTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteTranscodeTemplateGroupResponse().from_map(
            self.do_rpcrequest('DeleteTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_transcode_template_group_with_options_async(
        self,
        request: vod_20170321_models.DeleteTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteTranscodeTemplateGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_transcode_template_group(
        self,
        request: vod_20170321_models.DeleteTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.DeleteTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_transcode_template_group_with_options(request, runtime)

    async def delete_transcode_template_group_async(
        self,
        request: vod_20170321_models.DeleteTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.DeleteTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_transcode_template_group_with_options_async(request, runtime)

    def delete_video_with_options(
        self,
        request: vod_20170321_models.DeleteVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteVideoResponse().from_map(
            self.do_rpcrequest('DeleteVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_video_with_options_async(
        self,
        request: vod_20170321_models.DeleteVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteVideoResponse().from_map(
            await self.do_rpcrequest_async('DeleteVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_video(
        self,
        request: vod_20170321_models.DeleteVideoRequest,
    ) -> vod_20170321_models.DeleteVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_video_with_options(request, runtime)

    async def delete_video_async(
        self,
        request: vod_20170321_models.DeleteVideoRequest,
    ) -> vod_20170321_models.DeleteVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_video_with_options_async(request, runtime)

    def delete_vod_domain_with_options(
        self,
        request: vod_20170321_models.DeleteVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteVodDomainResponse().from_map(
            self.do_rpcrequest('DeleteVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vod_domain_with_options_async(
        self,
        request: vod_20170321_models.DeleteVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteVodDomainResponse().from_map(
            await self.do_rpcrequest_async('DeleteVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vod_domain(
        self,
        request: vod_20170321_models.DeleteVodDomainRequest,
    ) -> vod_20170321_models.DeleteVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vod_domain_with_options(request, runtime)

    async def delete_vod_domain_async(
        self,
        request: vod_20170321_models.DeleteVodDomainRequest,
    ) -> vod_20170321_models.DeleteVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vod_domain_with_options_async(request, runtime)

    def delete_vod_specific_config_with_options(
        self,
        request: vod_20170321_models.DeleteVodSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVodSpecificConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteVodSpecificConfigResponse().from_map(
            self.do_rpcrequest('DeleteVodSpecificConfig', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vod_specific_config_with_options_async(
        self,
        request: vod_20170321_models.DeleteVodSpecificConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVodSpecificConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteVodSpecificConfigResponse().from_map(
            await self.do_rpcrequest_async('DeleteVodSpecificConfig', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vod_specific_config(
        self,
        request: vod_20170321_models.DeleteVodSpecificConfigRequest,
    ) -> vod_20170321_models.DeleteVodSpecificConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vod_specific_config_with_options(request, runtime)

    async def delete_vod_specific_config_async(
        self,
        request: vod_20170321_models.DeleteVodSpecificConfigRequest,
    ) -> vod_20170321_models.DeleteVodSpecificConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vod_specific_config_with_options_async(request, runtime)

    def delete_vod_template_with_options(
        self,
        request: vod_20170321_models.DeleteVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteVodTemplateResponse().from_map(
            self.do_rpcrequest('DeleteVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vod_template_with_options_async(
        self,
        request: vod_20170321_models.DeleteVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteVodTemplateResponse().from_map(
            await self.do_rpcrequest_async('DeleteVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vod_template(
        self,
        request: vod_20170321_models.DeleteVodTemplateRequest,
    ) -> vod_20170321_models.DeleteVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vod_template_with_options(request, runtime)

    async def delete_vod_template_async(
        self,
        request: vod_20170321_models.DeleteVodTemplateRequest,
    ) -> vod_20170321_models.DeleteVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vod_template_with_options_async(request, runtime)

    def delete_watermark_with_options(
        self,
        request: vod_20170321_models.DeleteWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteWatermarkResponse().from_map(
            self.do_rpcrequest('DeleteWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_watermark_with_options_async(
        self,
        request: vod_20170321_models.DeleteWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DeleteWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DeleteWatermarkResponse().from_map(
            await self.do_rpcrequest_async('DeleteWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_watermark(
        self,
        request: vod_20170321_models.DeleteWatermarkRequest,
    ) -> vod_20170321_models.DeleteWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_watermark_with_options(request, runtime)

    async def delete_watermark_async(
        self,
        request: vod_20170321_models.DeleteWatermarkRequest,
    ) -> vod_20170321_models.DeleteWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_watermark_with_options_async(request, runtime)

    def describe_play_top_videos_with_options(
        self,
        request: vod_20170321_models.DescribePlayTopVideosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribePlayTopVideosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribePlayTopVideosResponse().from_map(
            self.do_rpcrequest('DescribePlayTopVideos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_play_top_videos_with_options_async(
        self,
        request: vod_20170321_models.DescribePlayTopVideosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribePlayTopVideosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribePlayTopVideosResponse().from_map(
            await self.do_rpcrequest_async('DescribePlayTopVideos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_play_top_videos(
        self,
        request: vod_20170321_models.DescribePlayTopVideosRequest,
    ) -> vod_20170321_models.DescribePlayTopVideosResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_play_top_videos_with_options(request, runtime)

    async def describe_play_top_videos_async(
        self,
        request: vod_20170321_models.DescribePlayTopVideosRequest,
    ) -> vod_20170321_models.DescribePlayTopVideosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_play_top_videos_with_options_async(request, runtime)

    def describe_play_user_avg_with_options(
        self,
        request: vod_20170321_models.DescribePlayUserAvgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribePlayUserAvgResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribePlayUserAvgResponse().from_map(
            self.do_rpcrequest('DescribePlayUserAvg', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_play_user_avg_with_options_async(
        self,
        request: vod_20170321_models.DescribePlayUserAvgRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribePlayUserAvgResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribePlayUserAvgResponse().from_map(
            await self.do_rpcrequest_async('DescribePlayUserAvg', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_play_user_avg(
        self,
        request: vod_20170321_models.DescribePlayUserAvgRequest,
    ) -> vod_20170321_models.DescribePlayUserAvgResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_play_user_avg_with_options(request, runtime)

    async def describe_play_user_avg_async(
        self,
        request: vod_20170321_models.DescribePlayUserAvgRequest,
    ) -> vod_20170321_models.DescribePlayUserAvgResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_play_user_avg_with_options_async(request, runtime)

    def describe_play_user_total_with_options(
        self,
        request: vod_20170321_models.DescribePlayUserTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribePlayUserTotalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribePlayUserTotalResponse().from_map(
            self.do_rpcrequest('DescribePlayUserTotal', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_play_user_total_with_options_async(
        self,
        request: vod_20170321_models.DescribePlayUserTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribePlayUserTotalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribePlayUserTotalResponse().from_map(
            await self.do_rpcrequest_async('DescribePlayUserTotal', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_play_user_total(
        self,
        request: vod_20170321_models.DescribePlayUserTotalRequest,
    ) -> vod_20170321_models.DescribePlayUserTotalResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_play_user_total_with_options(request, runtime)

    async def describe_play_user_total_async(
        self,
        request: vod_20170321_models.DescribePlayUserTotalRequest,
    ) -> vod_20170321_models.DescribePlayUserTotalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_play_user_total_with_options_async(request, runtime)

    def describe_play_video_statis_with_options(
        self,
        request: vod_20170321_models.DescribePlayVideoStatisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribePlayVideoStatisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribePlayVideoStatisResponse().from_map(
            self.do_rpcrequest('DescribePlayVideoStatis', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_play_video_statis_with_options_async(
        self,
        request: vod_20170321_models.DescribePlayVideoStatisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribePlayVideoStatisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribePlayVideoStatisResponse().from_map(
            await self.do_rpcrequest_async('DescribePlayVideoStatis', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_play_video_statis(
        self,
        request: vod_20170321_models.DescribePlayVideoStatisRequest,
    ) -> vod_20170321_models.DescribePlayVideoStatisResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_play_video_statis_with_options(request, runtime)

    async def describe_play_video_statis_async(
        self,
        request: vod_20170321_models.DescribePlayVideoStatisRequest,
    ) -> vod_20170321_models.DescribePlayVideoStatisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_play_video_statis_with_options_async(request, runtime)

    def describe_vod_aidata_with_options(
        self,
        request: vod_20170321_models.DescribeVodAIDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodAIDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodAIDataResponse().from_map(
            self.do_rpcrequest('DescribeVodAIData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_aidata_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodAIDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodAIDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodAIDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeVodAIData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_aidata(
        self,
        request: vod_20170321_models.DescribeVodAIDataRequest,
    ) -> vod_20170321_models.DescribeVodAIDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_aidata_with_options(request, runtime)

    async def describe_vod_aidata_async(
        self,
        request: vod_20170321_models.DescribeVodAIDataRequest,
    ) -> vod_20170321_models.DescribeVodAIDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_aidata_with_options_async(request, runtime)

    def describe_vod_certificate_list_with_options(
        self,
        request: vod_20170321_models.DescribeVodCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodCertificateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodCertificateListResponse().from_map(
            self.do_rpcrequest('DescribeVodCertificateList', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_certificate_list_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodCertificateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodCertificateListResponse().from_map(
            await self.do_rpcrequest_async('DescribeVodCertificateList', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_certificate_list(
        self,
        request: vod_20170321_models.DescribeVodCertificateListRequest,
    ) -> vod_20170321_models.DescribeVodCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_certificate_list_with_options(request, runtime)

    async def describe_vod_certificate_list_async(
        self,
        request: vod_20170321_models.DescribeVodCertificateListRequest,
    ) -> vod_20170321_models.DescribeVodCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_certificate_list_with_options_async(request, runtime)

    def describe_vod_domain_bps_data_with_options(
        self,
        request: vod_20170321_models.DescribeVodDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodDomainBpsDataResponse().from_map(
            self.do_rpcrequest('DescribeVodDomainBpsData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_domain_bps_data_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodDomainBpsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainBpsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodDomainBpsDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeVodDomainBpsData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_domain_bps_data(
        self,
        request: vod_20170321_models.DescribeVodDomainBpsDataRequest,
    ) -> vod_20170321_models.DescribeVodDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_bps_data_with_options(request, runtime)

    async def describe_vod_domain_bps_data_async(
        self,
        request: vod_20170321_models.DescribeVodDomainBpsDataRequest,
    ) -> vod_20170321_models.DescribeVodDomainBpsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_domain_bps_data_with_options_async(request, runtime)

    def describe_vod_domain_certificate_info_with_options(
        self,
        request: vod_20170321_models.DescribeVodDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainCertificateInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodDomainCertificateInfoResponse().from_map(
            self.do_rpcrequest('DescribeVodDomainCertificateInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_domain_certificate_info_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodDomainCertificateInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainCertificateInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodDomainCertificateInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeVodDomainCertificateInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_domain_certificate_info(
        self,
        request: vod_20170321_models.DescribeVodDomainCertificateInfoRequest,
    ) -> vod_20170321_models.DescribeVodDomainCertificateInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_certificate_info_with_options(request, runtime)

    async def describe_vod_domain_certificate_info_async(
        self,
        request: vod_20170321_models.DescribeVodDomainCertificateInfoRequest,
    ) -> vod_20170321_models.DescribeVodDomainCertificateInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_domain_certificate_info_with_options_async(request, runtime)

    def describe_vod_domain_configs_with_options(
        self,
        request: vod_20170321_models.DescribeVodDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodDomainConfigsResponse().from_map(
            self.do_rpcrequest('DescribeVodDomainConfigs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_domain_configs_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodDomainConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodDomainConfigsResponse().from_map(
            await self.do_rpcrequest_async('DescribeVodDomainConfigs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_domain_configs(
        self,
        request: vod_20170321_models.DescribeVodDomainConfigsRequest,
    ) -> vod_20170321_models.DescribeVodDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_configs_with_options(request, runtime)

    async def describe_vod_domain_configs_async(
        self,
        request: vod_20170321_models.DescribeVodDomainConfigsRequest,
    ) -> vod_20170321_models.DescribeVodDomainConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_domain_configs_with_options_async(request, runtime)

    def describe_vod_domain_detail_with_options(
        self,
        request: vod_20170321_models.DescribeVodDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodDomainDetailResponse().from_map(
            self.do_rpcrequest('DescribeVodDomainDetail', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_domain_detail_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodDomainDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodDomainDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeVodDomainDetail', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_domain_detail(
        self,
        request: vod_20170321_models.DescribeVodDomainDetailRequest,
    ) -> vod_20170321_models.DescribeVodDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_detail_with_options(request, runtime)

    async def describe_vod_domain_detail_async(
        self,
        request: vod_20170321_models.DescribeVodDomainDetailRequest,
    ) -> vod_20170321_models.DescribeVodDomainDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_domain_detail_with_options_async(request, runtime)

    def describe_vod_domain_log_with_options(
        self,
        request: vod_20170321_models.DescribeVodDomainLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodDomainLogResponse().from_map(
            self.do_rpcrequest('DescribeVodDomainLog', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_domain_log_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodDomainLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodDomainLogResponse().from_map(
            await self.do_rpcrequest_async('DescribeVodDomainLog', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_domain_log(
        self,
        request: vod_20170321_models.DescribeVodDomainLogRequest,
    ) -> vod_20170321_models.DescribeVodDomainLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_log_with_options(request, runtime)

    async def describe_vod_domain_log_async(
        self,
        request: vod_20170321_models.DescribeVodDomainLogRequest,
    ) -> vod_20170321_models.DescribeVodDomainLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_domain_log_with_options_async(request, runtime)

    def describe_vod_domain_traffic_data_with_options(
        self,
        request: vod_20170321_models.DescribeVodDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodDomainTrafficDataResponse().from_map(
            self.do_rpcrequest('DescribeVodDomainTrafficData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_domain_traffic_data_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodDomainTrafficDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainTrafficDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodDomainTrafficDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeVodDomainTrafficData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_domain_traffic_data(
        self,
        request: vod_20170321_models.DescribeVodDomainTrafficDataRequest,
    ) -> vod_20170321_models.DescribeVodDomainTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_traffic_data_with_options(request, runtime)

    async def describe_vod_domain_traffic_data_async(
        self,
        request: vod_20170321_models.DescribeVodDomainTrafficDataRequest,
    ) -> vod_20170321_models.DescribeVodDomainTrafficDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_domain_traffic_data_with_options_async(request, runtime)

    def describe_vod_domain_usage_data_with_options(
        self,
        request: vod_20170321_models.DescribeVodDomainUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainUsageDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodDomainUsageDataResponse().from_map(
            self.do_rpcrequest('DescribeVodDomainUsageData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_domain_usage_data_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodDomainUsageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodDomainUsageDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodDomainUsageDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeVodDomainUsageData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_domain_usage_data(
        self,
        request: vod_20170321_models.DescribeVodDomainUsageDataRequest,
    ) -> vod_20170321_models.DescribeVodDomainUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_domain_usage_data_with_options(request, runtime)

    async def describe_vod_domain_usage_data_async(
        self,
        request: vod_20170321_models.DescribeVodDomainUsageDataRequest,
    ) -> vod_20170321_models.DescribeVodDomainUsageDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_domain_usage_data_with_options_async(request, runtime)

    def describe_vod_refresh_quota_with_options(
        self,
        request: vod_20170321_models.DescribeVodRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodRefreshQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodRefreshQuotaResponse().from_map(
            self.do_rpcrequest('DescribeVodRefreshQuota', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_refresh_quota_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodRefreshQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodRefreshQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodRefreshQuotaResponse().from_map(
            await self.do_rpcrequest_async('DescribeVodRefreshQuota', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_refresh_quota(
        self,
        request: vod_20170321_models.DescribeVodRefreshQuotaRequest,
    ) -> vod_20170321_models.DescribeVodRefreshQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_refresh_quota_with_options(request, runtime)

    async def describe_vod_refresh_quota_async(
        self,
        request: vod_20170321_models.DescribeVodRefreshQuotaRequest,
    ) -> vod_20170321_models.DescribeVodRefreshQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_refresh_quota_with_options_async(request, runtime)

    def describe_vod_refresh_tasks_with_options(
        self,
        request: vod_20170321_models.DescribeVodRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodRefreshTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodRefreshTasksResponse().from_map(
            self.do_rpcrequest('DescribeVodRefreshTasks', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_refresh_tasks_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodRefreshTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodRefreshTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodRefreshTasksResponse().from_map(
            await self.do_rpcrequest_async('DescribeVodRefreshTasks', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_refresh_tasks(
        self,
        request: vod_20170321_models.DescribeVodRefreshTasksRequest,
    ) -> vod_20170321_models.DescribeVodRefreshTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_refresh_tasks_with_options(request, runtime)

    async def describe_vod_refresh_tasks_async(
        self,
        request: vod_20170321_models.DescribeVodRefreshTasksRequest,
    ) -> vod_20170321_models.DescribeVodRefreshTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_refresh_tasks_with_options_async(request, runtime)

    def describe_vod_storage_data_with_options(
        self,
        request: vod_20170321_models.DescribeVodStorageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodStorageDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodStorageDataResponse().from_map(
            self.do_rpcrequest('DescribeVodStorageData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_storage_data_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodStorageDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodStorageDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodStorageDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeVodStorageData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_storage_data(
        self,
        request: vod_20170321_models.DescribeVodStorageDataRequest,
    ) -> vod_20170321_models.DescribeVodStorageDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_storage_data_with_options(request, runtime)

    async def describe_vod_storage_data_async(
        self,
        request: vod_20170321_models.DescribeVodStorageDataRequest,
    ) -> vod_20170321_models.DescribeVodStorageDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_storage_data_with_options_async(request, runtime)

    def describe_vod_tag_resources_with_options(
        self,
        request: vod_20170321_models.DescribeVodTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodTagResourcesResponse().from_map(
            self.do_rpcrequest('DescribeVodTagResources', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_tag_resources_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('DescribeVodTagResources', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_tag_resources(
        self,
        request: vod_20170321_models.DescribeVodTagResourcesRequest,
    ) -> vod_20170321_models.DescribeVodTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_tag_resources_with_options(request, runtime)

    async def describe_vod_tag_resources_async(
        self,
        request: vod_20170321_models.DescribeVodTagResourcesRequest,
    ) -> vod_20170321_models.DescribeVodTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_tag_resources_with_options_async(request, runtime)

    def describe_vod_transcode_data_with_options(
        self,
        request: vod_20170321_models.DescribeVodTranscodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodTranscodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodTranscodeDataResponse().from_map(
            self.do_rpcrequest('DescribeVodTranscodeData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_transcode_data_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodTranscodeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodTranscodeDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodTranscodeDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeVodTranscodeData', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_transcode_data(
        self,
        request: vod_20170321_models.DescribeVodTranscodeDataRequest,
    ) -> vod_20170321_models.DescribeVodTranscodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_transcode_data_with_options(request, runtime)

    async def describe_vod_transcode_data_async(
        self,
        request: vod_20170321_models.DescribeVodTranscodeDataRequest,
    ) -> vod_20170321_models.DescribeVodTranscodeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_transcode_data_with_options_async(request, runtime)

    def describe_vod_user_domains_with_options(
        self,
        request: vod_20170321_models.DescribeVodUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodUserDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodUserDomainsResponse().from_map(
            self.do_rpcrequest('DescribeVodUserDomains', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_user_domains_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodUserDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodUserDomainsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodUserDomainsResponse().from_map(
            await self.do_rpcrequest_async('DescribeVodUserDomains', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_user_domains(
        self,
        request: vod_20170321_models.DescribeVodUserDomainsRequest,
    ) -> vod_20170321_models.DescribeVodUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_user_domains_with_options(request, runtime)

    async def describe_vod_user_domains_async(
        self,
        request: vod_20170321_models.DescribeVodUserDomainsRequest,
    ) -> vod_20170321_models.DescribeVodUserDomainsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_user_domains_with_options_async(request, runtime)

    def describe_vod_user_tags_with_options(
        self,
        request: vod_20170321_models.DescribeVodUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodUserTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodUserTagsResponse().from_map(
            self.do_rpcrequest('DescribeVodUserTags', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_user_tags_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodUserTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodUserTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodUserTagsResponse().from_map(
            await self.do_rpcrequest_async('DescribeVodUserTags', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_user_tags(
        self,
        request: vod_20170321_models.DescribeVodUserTagsRequest,
    ) -> vod_20170321_models.DescribeVodUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_user_tags_with_options(request, runtime)

    async def describe_vod_user_tags_async(
        self,
        request: vod_20170321_models.DescribeVodUserTagsRequest,
    ) -> vod_20170321_models.DescribeVodUserTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_user_tags_with_options_async(request, runtime)

    def describe_vod_verify_content_with_options(
        self,
        request: vod_20170321_models.DescribeVodVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodVerifyContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodVerifyContentResponse().from_map(
            self.do_rpcrequest('DescribeVodVerifyContent', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vod_verify_content_with_options_async(
        self,
        request: vod_20170321_models.DescribeVodVerifyContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DescribeVodVerifyContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DescribeVodVerifyContentResponse().from_map(
            await self.do_rpcrequest_async('DescribeVodVerifyContent', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_verify_content(
        self,
        request: vod_20170321_models.DescribeVodVerifyContentRequest,
    ) -> vod_20170321_models.DescribeVodVerifyContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_verify_content_with_options(request, runtime)

    async def describe_vod_verify_content_async(
        self,
        request: vod_20170321_models.DescribeVodVerifyContentRequest,
    ) -> vod_20170321_models.DescribeVodVerifyContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vod_verify_content_with_options_async(request, runtime)

    def detach_app_policy_from_identity_with_options(
        self,
        request: vod_20170321_models.DetachAppPolicyFromIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DetachAppPolicyFromIdentityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DetachAppPolicyFromIdentityResponse().from_map(
            self.do_rpcrequest('DetachAppPolicyFromIdentity', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_app_policy_from_identity_with_options_async(
        self,
        request: vod_20170321_models.DetachAppPolicyFromIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.DetachAppPolicyFromIdentityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.DetachAppPolicyFromIdentityResponse().from_map(
            await self.do_rpcrequest_async('DetachAppPolicyFromIdentity', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_app_policy_from_identity(
        self,
        request: vod_20170321_models.DetachAppPolicyFromIdentityRequest,
    ) -> vod_20170321_models.DetachAppPolicyFromIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_app_policy_from_identity_with_options(request, runtime)

    async def detach_app_policy_from_identity_async(
        self,
        request: vod_20170321_models.DetachAppPolicyFromIdentityRequest,
    ) -> vod_20170321_models.DetachAppPolicyFromIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_app_policy_from_identity_with_options_async(request, runtime)

    def get_aiimage_jobs_with_options(
        self,
        request: vod_20170321_models.GetAIImageJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAIImageJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetAIImageJobsResponse().from_map(
            self.do_rpcrequest('GetAIImageJobs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_aiimage_jobs_with_options_async(
        self,
        request: vod_20170321_models.GetAIImageJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAIImageJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetAIImageJobsResponse().from_map(
            await self.do_rpcrequest_async('GetAIImageJobs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_aiimage_jobs(
        self,
        request: vod_20170321_models.GetAIImageJobsRequest,
    ) -> vod_20170321_models.GetAIImageJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aiimage_jobs_with_options(request, runtime)

    async def get_aiimage_jobs_async(
        self,
        request: vod_20170321_models.GetAIImageJobsRequest,
    ) -> vod_20170321_models.GetAIImageJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aiimage_jobs_with_options_async(request, runtime)

    def get_aimedia_audit_job_with_options(
        self,
        request: vod_20170321_models.GetAIMediaAuditJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAIMediaAuditJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetAIMediaAuditJobResponse().from_map(
            self.do_rpcrequest('GetAIMediaAuditJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_aimedia_audit_job_with_options_async(
        self,
        request: vod_20170321_models.GetAIMediaAuditJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAIMediaAuditJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetAIMediaAuditJobResponse().from_map(
            await self.do_rpcrequest_async('GetAIMediaAuditJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_aimedia_audit_job(
        self,
        request: vod_20170321_models.GetAIMediaAuditJobRequest,
    ) -> vod_20170321_models.GetAIMediaAuditJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aimedia_audit_job_with_options(request, runtime)

    async def get_aimedia_audit_job_async(
        self,
        request: vod_20170321_models.GetAIMediaAuditJobRequest,
    ) -> vod_20170321_models.GetAIMediaAuditJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aimedia_audit_job_with_options_async(request, runtime)

    def get_aitemplate_with_options(
        self,
        request: vod_20170321_models.GetAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetAITemplateResponse().from_map(
            self.do_rpcrequest('GetAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_aitemplate_with_options_async(
        self,
        request: vod_20170321_models.GetAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetAITemplateResponse().from_map(
            await self.do_rpcrequest_async('GetAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_aitemplate(
        self,
        request: vod_20170321_models.GetAITemplateRequest,
    ) -> vod_20170321_models.GetAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aitemplate_with_options(request, runtime)

    async def get_aitemplate_async(
        self,
        request: vod_20170321_models.GetAITemplateRequest,
    ) -> vod_20170321_models.GetAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aitemplate_with_options_async(request, runtime)

    def get_aivideo_tag_result_with_options(
        self,
        request: vod_20170321_models.GetAIVideoTagResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAIVideoTagResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetAIVideoTagResultResponse().from_map(
            self.do_rpcrequest('GetAIVideoTagResult', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_aivideo_tag_result_with_options_async(
        self,
        request: vod_20170321_models.GetAIVideoTagResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAIVideoTagResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetAIVideoTagResultResponse().from_map(
            await self.do_rpcrequest_async('GetAIVideoTagResult', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_aivideo_tag_result(
        self,
        request: vod_20170321_models.GetAIVideoTagResultRequest,
    ) -> vod_20170321_models.GetAIVideoTagResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aivideo_tag_result_with_options(request, runtime)

    async def get_aivideo_tag_result_async(
        self,
        request: vod_20170321_models.GetAIVideoTagResultRequest,
    ) -> vod_20170321_models.GetAIVideoTagResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aivideo_tag_result_with_options_async(request, runtime)

    def get_app_infos_with_options(
        self,
        request: vod_20170321_models.GetAppInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAppInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetAppInfosResponse().from_map(
            self.do_rpcrequest('GetAppInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_app_infos_with_options_async(
        self,
        request: vod_20170321_models.GetAppInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAppInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetAppInfosResponse().from_map(
            await self.do_rpcrequest_async('GetAppInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_app_infos(
        self,
        request: vod_20170321_models.GetAppInfosRequest,
    ) -> vod_20170321_models.GetAppInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_infos_with_options(request, runtime)

    async def get_app_infos_async(
        self,
        request: vod_20170321_models.GetAppInfosRequest,
    ) -> vod_20170321_models.GetAppInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_infos_with_options_async(request, runtime)

    def get_attached_media_info_with_options(
        self,
        request: vod_20170321_models.GetAttachedMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAttachedMediaInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetAttachedMediaInfoResponse().from_map(
            self.do_rpcrequest('GetAttachedMediaInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_attached_media_info_with_options_async(
        self,
        request: vod_20170321_models.GetAttachedMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAttachedMediaInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetAttachedMediaInfoResponse().from_map(
            await self.do_rpcrequest_async('GetAttachedMediaInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_attached_media_info(
        self,
        request: vod_20170321_models.GetAttachedMediaInfoRequest,
    ) -> vod_20170321_models.GetAttachedMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_attached_media_info_with_options(request, runtime)

    async def get_attached_media_info_async(
        self,
        request: vod_20170321_models.GetAttachedMediaInfoRequest,
    ) -> vod_20170321_models.GetAttachedMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_attached_media_info_with_options_async(request, runtime)

    def get_audit_history_with_options(
        self,
        request: vod_20170321_models.GetAuditHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAuditHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetAuditHistoryResponse().from_map(
            self.do_rpcrequest('GetAuditHistory', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_audit_history_with_options_async(
        self,
        request: vod_20170321_models.GetAuditHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetAuditHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetAuditHistoryResponse().from_map(
            await self.do_rpcrequest_async('GetAuditHistory', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_audit_history(
        self,
        request: vod_20170321_models.GetAuditHistoryRequest,
    ) -> vod_20170321_models.GetAuditHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_audit_history_with_options(request, runtime)

    async def get_audit_history_async(
        self,
        request: vod_20170321_models.GetAuditHistoryRequest,
    ) -> vod_20170321_models.GetAuditHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_audit_history_with_options_async(request, runtime)

    def get_categories_with_options(
        self,
        request: vod_20170321_models.GetCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetCategoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetCategoriesResponse().from_map(
            self.do_rpcrequest('GetCategories', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_categories_with_options_async(
        self,
        request: vod_20170321_models.GetCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetCategoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetCategoriesResponse().from_map(
            await self.do_rpcrequest_async('GetCategories', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_categories(
        self,
        request: vod_20170321_models.GetCategoriesRequest,
    ) -> vod_20170321_models.GetCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_categories_with_options(request, runtime)

    async def get_categories_async(
        self,
        request: vod_20170321_models.GetCategoriesRequest,
    ) -> vod_20170321_models.GetCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_categories_with_options_async(request, runtime)

    def get_default_aitemplate_with_options(
        self,
        request: vod_20170321_models.GetDefaultAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetDefaultAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetDefaultAITemplateResponse().from_map(
            self.do_rpcrequest('GetDefaultAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_default_aitemplate_with_options_async(
        self,
        request: vod_20170321_models.GetDefaultAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetDefaultAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetDefaultAITemplateResponse().from_map(
            await self.do_rpcrequest_async('GetDefaultAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_default_aitemplate(
        self,
        request: vod_20170321_models.GetDefaultAITemplateRequest,
    ) -> vod_20170321_models.GetDefaultAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_default_aitemplate_with_options(request, runtime)

    async def get_default_aitemplate_async(
        self,
        request: vod_20170321_models.GetDefaultAITemplateRequest,
    ) -> vod_20170321_models.GetDefaultAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_default_aitemplate_with_options_async(request, runtime)

    def get_editing_project_with_options(
        self,
        request: vod_20170321_models.GetEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetEditingProjectResponse().from_map(
            self.do_rpcrequest('GetEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_editing_project_with_options_async(
        self,
        request: vod_20170321_models.GetEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetEditingProjectResponse().from_map(
            await self.do_rpcrequest_async('GetEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_editing_project(
        self,
        request: vod_20170321_models.GetEditingProjectRequest,
    ) -> vod_20170321_models.GetEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_editing_project_with_options(request, runtime)

    async def get_editing_project_async(
        self,
        request: vod_20170321_models.GetEditingProjectRequest,
    ) -> vod_20170321_models.GetEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_editing_project_with_options_async(request, runtime)

    def get_editing_project_materials_with_options(
        self,
        request: vod_20170321_models.GetEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetEditingProjectMaterialsResponse().from_map(
            self.do_rpcrequest('GetEditingProjectMaterials', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_editing_project_materials_with_options_async(
        self,
        request: vod_20170321_models.GetEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetEditingProjectMaterialsResponse().from_map(
            await self.do_rpcrequest_async('GetEditingProjectMaterials', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_editing_project_materials(
        self,
        request: vod_20170321_models.GetEditingProjectMaterialsRequest,
    ) -> vod_20170321_models.GetEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_editing_project_materials_with_options(request, runtime)

    async def get_editing_project_materials_async(
        self,
        request: vod_20170321_models.GetEditingProjectMaterialsRequest,
    ) -> vod_20170321_models.GetEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_editing_project_materials_with_options_async(request, runtime)

    def get_image_info_with_options(
        self,
        request: vod_20170321_models.GetImageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetImageInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetImageInfoResponse().from_map(
            self.do_rpcrequest('GetImageInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_image_info_with_options_async(
        self,
        request: vod_20170321_models.GetImageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetImageInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetImageInfoResponse().from_map(
            await self.do_rpcrequest_async('GetImageInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_image_info(
        self,
        request: vod_20170321_models.GetImageInfoRequest,
    ) -> vod_20170321_models.GetImageInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_image_info_with_options(request, runtime)

    async def get_image_info_async(
        self,
        request: vod_20170321_models.GetImageInfoRequest,
    ) -> vod_20170321_models.GetImageInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_image_info_with_options_async(request, runtime)

    def get_media_audit_audio_result_detail_with_options(
        self,
        request: vod_20170321_models.GetMediaAuditAudioResultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaAuditAudioResultDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetMediaAuditAudioResultDetailResponse().from_map(
            self.do_rpcrequest('GetMediaAuditAudioResultDetail', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_media_audit_audio_result_detail_with_options_async(
        self,
        request: vod_20170321_models.GetMediaAuditAudioResultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaAuditAudioResultDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetMediaAuditAudioResultDetailResponse().from_map(
            await self.do_rpcrequest_async('GetMediaAuditAudioResultDetail', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_media_audit_audio_result_detail(
        self,
        request: vod_20170321_models.GetMediaAuditAudioResultDetailRequest,
    ) -> vod_20170321_models.GetMediaAuditAudioResultDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_audit_audio_result_detail_with_options(request, runtime)

    async def get_media_audit_audio_result_detail_async(
        self,
        request: vod_20170321_models.GetMediaAuditAudioResultDetailRequest,
    ) -> vod_20170321_models.GetMediaAuditAudioResultDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_audit_audio_result_detail_with_options_async(request, runtime)

    def get_media_audit_result_with_options(
        self,
        request: vod_20170321_models.GetMediaAuditResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaAuditResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetMediaAuditResultResponse().from_map(
            self.do_rpcrequest('GetMediaAuditResult', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_media_audit_result_with_options_async(
        self,
        request: vod_20170321_models.GetMediaAuditResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaAuditResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetMediaAuditResultResponse().from_map(
            await self.do_rpcrequest_async('GetMediaAuditResult', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_media_audit_result(
        self,
        request: vod_20170321_models.GetMediaAuditResultRequest,
    ) -> vod_20170321_models.GetMediaAuditResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_audit_result_with_options(request, runtime)

    async def get_media_audit_result_async(
        self,
        request: vod_20170321_models.GetMediaAuditResultRequest,
    ) -> vod_20170321_models.GetMediaAuditResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_audit_result_with_options_async(request, runtime)

    def get_media_audit_result_detail_with_options(
        self,
        request: vod_20170321_models.GetMediaAuditResultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaAuditResultDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetMediaAuditResultDetailResponse().from_map(
            self.do_rpcrequest('GetMediaAuditResultDetail', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_media_audit_result_detail_with_options_async(
        self,
        request: vod_20170321_models.GetMediaAuditResultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaAuditResultDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetMediaAuditResultDetailResponse().from_map(
            await self.do_rpcrequest_async('GetMediaAuditResultDetail', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_media_audit_result_detail(
        self,
        request: vod_20170321_models.GetMediaAuditResultDetailRequest,
    ) -> vod_20170321_models.GetMediaAuditResultDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_audit_result_detail_with_options(request, runtime)

    async def get_media_audit_result_detail_async(
        self,
        request: vod_20170321_models.GetMediaAuditResultDetailRequest,
    ) -> vod_20170321_models.GetMediaAuditResultDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_audit_result_detail_with_options_async(request, runtime)

    def get_media_audit_result_timeline_with_options(
        self,
        request: vod_20170321_models.GetMediaAuditResultTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaAuditResultTimelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetMediaAuditResultTimelineResponse().from_map(
            self.do_rpcrequest('GetMediaAuditResultTimeline', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_media_audit_result_timeline_with_options_async(
        self,
        request: vod_20170321_models.GetMediaAuditResultTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaAuditResultTimelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetMediaAuditResultTimelineResponse().from_map(
            await self.do_rpcrequest_async('GetMediaAuditResultTimeline', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_media_audit_result_timeline(
        self,
        request: vod_20170321_models.GetMediaAuditResultTimelineRequest,
    ) -> vod_20170321_models.GetMediaAuditResultTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_audit_result_timeline_with_options(request, runtime)

    async def get_media_audit_result_timeline_async(
        self,
        request: vod_20170321_models.GetMediaAuditResultTimelineRequest,
    ) -> vod_20170321_models.GetMediaAuditResultTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_audit_result_timeline_with_options_async(request, runtime)

    def get_media_dnaresult_with_options(
        self,
        request: vod_20170321_models.GetMediaDNAResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaDNAResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetMediaDNAResultResponse().from_map(
            self.do_rpcrequest('GetMediaDNAResult', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_media_dnaresult_with_options_async(
        self,
        request: vod_20170321_models.GetMediaDNAResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMediaDNAResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetMediaDNAResultResponse().from_map(
            await self.do_rpcrequest_async('GetMediaDNAResult', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_media_dnaresult(
        self,
        request: vod_20170321_models.GetMediaDNAResultRequest,
    ) -> vod_20170321_models.GetMediaDNAResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_dnaresult_with_options(request, runtime)

    async def get_media_dnaresult_async(
        self,
        request: vod_20170321_models.GetMediaDNAResultRequest,
    ) -> vod_20170321_models.GetMediaDNAResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_dnaresult_with_options_async(request, runtime)

    def get_message_callback_with_options(
        self,
        request: vod_20170321_models.GetMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMessageCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetMessageCallbackResponse().from_map(
            self.do_rpcrequest('GetMessageCallback', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_message_callback_with_options_async(
        self,
        request: vod_20170321_models.GetMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMessageCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetMessageCallbackResponse().from_map(
            await self.do_rpcrequest_async('GetMessageCallback', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_message_callback(
        self,
        request: vod_20170321_models.GetMessageCallbackRequest,
    ) -> vod_20170321_models.GetMessageCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_message_callback_with_options(request, runtime)

    async def get_message_callback_async(
        self,
        request: vod_20170321_models.GetMessageCallbackRequest,
    ) -> vod_20170321_models.GetMessageCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_message_callback_with_options_async(request, runtime)

    def get_mezzanine_info_with_options(
        self,
        request: vod_20170321_models.GetMezzanineInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMezzanineInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetMezzanineInfoResponse().from_map(
            self.do_rpcrequest('GetMezzanineInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_mezzanine_info_with_options_async(
        self,
        request: vod_20170321_models.GetMezzanineInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetMezzanineInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetMezzanineInfoResponse().from_map(
            await self.do_rpcrequest_async('GetMezzanineInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_mezzanine_info(
        self,
        request: vod_20170321_models.GetMezzanineInfoRequest,
    ) -> vod_20170321_models.GetMezzanineInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_mezzanine_info_with_options(request, runtime)

    async def get_mezzanine_info_async(
        self,
        request: vod_20170321_models.GetMezzanineInfoRequest,
    ) -> vod_20170321_models.GetMezzanineInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_mezzanine_info_with_options_async(request, runtime)

    def get_play_info_with_options(
        self,
        request: vod_20170321_models.GetPlayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetPlayInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetPlayInfoResponse().from_map(
            self.do_rpcrequest('GetPlayInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_play_info_with_options_async(
        self,
        request: vod_20170321_models.GetPlayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetPlayInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetPlayInfoResponse().from_map(
            await self.do_rpcrequest_async('GetPlayInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_play_info(
        self,
        request: vod_20170321_models.GetPlayInfoRequest,
    ) -> vod_20170321_models.GetPlayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_play_info_with_options(request, runtime)

    async def get_play_info_async(
        self,
        request: vod_20170321_models.GetPlayInfoRequest,
    ) -> vod_20170321_models.GetPlayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_play_info_with_options_async(request, runtime)

    def get_transcode_summary_with_options(
        self,
        request: vod_20170321_models.GetTranscodeSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetTranscodeSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetTranscodeSummaryResponse().from_map(
            self.do_rpcrequest('GetTranscodeSummary', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_transcode_summary_with_options_async(
        self,
        request: vod_20170321_models.GetTranscodeSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetTranscodeSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetTranscodeSummaryResponse().from_map(
            await self.do_rpcrequest_async('GetTranscodeSummary', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_transcode_summary(
        self,
        request: vod_20170321_models.GetTranscodeSummaryRequest,
    ) -> vod_20170321_models.GetTranscodeSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_transcode_summary_with_options(request, runtime)

    async def get_transcode_summary_async(
        self,
        request: vod_20170321_models.GetTranscodeSummaryRequest,
    ) -> vod_20170321_models.GetTranscodeSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_transcode_summary_with_options_async(request, runtime)

    def get_transcode_task_with_options(
        self,
        request: vod_20170321_models.GetTranscodeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetTranscodeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetTranscodeTaskResponse().from_map(
            self.do_rpcrequest('GetTranscodeTask', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_transcode_task_with_options_async(
        self,
        request: vod_20170321_models.GetTranscodeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetTranscodeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetTranscodeTaskResponse().from_map(
            await self.do_rpcrequest_async('GetTranscodeTask', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_transcode_task(
        self,
        request: vod_20170321_models.GetTranscodeTaskRequest,
    ) -> vod_20170321_models.GetTranscodeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_transcode_task_with_options(request, runtime)

    async def get_transcode_task_async(
        self,
        request: vod_20170321_models.GetTranscodeTaskRequest,
    ) -> vod_20170321_models.GetTranscodeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_transcode_task_with_options_async(request, runtime)

    def get_transcode_template_group_with_options(
        self,
        request: vod_20170321_models.GetTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetTranscodeTemplateGroupResponse().from_map(
            self.do_rpcrequest('GetTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_transcode_template_group_with_options_async(
        self,
        request: vod_20170321_models.GetTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetTranscodeTemplateGroupResponse().from_map(
            await self.do_rpcrequest_async('GetTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_transcode_template_group(
        self,
        request: vod_20170321_models.GetTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.GetTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_transcode_template_group_with_options(request, runtime)

    async def get_transcode_template_group_async(
        self,
        request: vod_20170321_models.GetTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.GetTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_transcode_template_group_with_options_async(request, runtime)

    def get_upload_details_with_options(
        self,
        request: vod_20170321_models.GetUploadDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetUploadDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetUploadDetailsResponse().from_map(
            self.do_rpcrequest('GetUploadDetails', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_upload_details_with_options_async(
        self,
        request: vod_20170321_models.GetUploadDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetUploadDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetUploadDetailsResponse().from_map(
            await self.do_rpcrequest_async('GetUploadDetails', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_upload_details(
        self,
        request: vod_20170321_models.GetUploadDetailsRequest,
    ) -> vod_20170321_models.GetUploadDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_upload_details_with_options(request, runtime)

    async def get_upload_details_async(
        self,
        request: vod_20170321_models.GetUploadDetailsRequest,
    ) -> vod_20170321_models.GetUploadDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_upload_details_with_options_async(request, runtime)

    def get_urlupload_infos_with_options(
        self,
        request: vod_20170321_models.GetURLUploadInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetURLUploadInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetURLUploadInfosResponse().from_map(
            self.do_rpcrequest('GetURLUploadInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_urlupload_infos_with_options_async(
        self,
        request: vod_20170321_models.GetURLUploadInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetURLUploadInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetURLUploadInfosResponse().from_map(
            await self.do_rpcrequest_async('GetURLUploadInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_urlupload_infos(
        self,
        request: vod_20170321_models.GetURLUploadInfosRequest,
    ) -> vod_20170321_models.GetURLUploadInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_urlupload_infos_with_options(request, runtime)

    async def get_urlupload_infos_async(
        self,
        request: vod_20170321_models.GetURLUploadInfosRequest,
    ) -> vod_20170321_models.GetURLUploadInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_urlupload_infos_with_options_async(request, runtime)

    def get_video_info_with_options(
        self,
        request: vod_20170321_models.GetVideoInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVideoInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetVideoInfoResponse().from_map(
            self.do_rpcrequest('GetVideoInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_video_info_with_options_async(
        self,
        request: vod_20170321_models.GetVideoInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVideoInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetVideoInfoResponse().from_map(
            await self.do_rpcrequest_async('GetVideoInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_info(
        self,
        request: vod_20170321_models.GetVideoInfoRequest,
    ) -> vod_20170321_models.GetVideoInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_info_with_options(request, runtime)

    async def get_video_info_async(
        self,
        request: vod_20170321_models.GetVideoInfoRequest,
    ) -> vod_20170321_models.GetVideoInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_info_with_options_async(request, runtime)

    def get_video_infos_with_options(
        self,
        request: vod_20170321_models.GetVideoInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVideoInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetVideoInfosResponse().from_map(
            self.do_rpcrequest('GetVideoInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_video_infos_with_options_async(
        self,
        request: vod_20170321_models.GetVideoInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVideoInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetVideoInfosResponse().from_map(
            await self.do_rpcrequest_async('GetVideoInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_infos(
        self,
        request: vod_20170321_models.GetVideoInfosRequest,
    ) -> vod_20170321_models.GetVideoInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_infos_with_options(request, runtime)

    async def get_video_infos_async(
        self,
        request: vod_20170321_models.GetVideoInfosRequest,
    ) -> vod_20170321_models.GetVideoInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_infos_with_options_async(request, runtime)

    def get_video_list_with_options(
        self,
        request: vod_20170321_models.GetVideoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVideoListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetVideoListResponse().from_map(
            self.do_rpcrequest('GetVideoList', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_video_list_with_options_async(
        self,
        request: vod_20170321_models.GetVideoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVideoListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetVideoListResponse().from_map(
            await self.do_rpcrequest_async('GetVideoList', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_list(
        self,
        request: vod_20170321_models.GetVideoListRequest,
    ) -> vod_20170321_models.GetVideoListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_list_with_options(request, runtime)

    async def get_video_list_async(
        self,
        request: vod_20170321_models.GetVideoListRequest,
    ) -> vod_20170321_models.GetVideoListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_list_with_options_async(request, runtime)

    def get_video_play_auth_with_options(
        self,
        request: vod_20170321_models.GetVideoPlayAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVideoPlayAuthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetVideoPlayAuthResponse().from_map(
            self.do_rpcrequest('GetVideoPlayAuth', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_video_play_auth_with_options_async(
        self,
        request: vod_20170321_models.GetVideoPlayAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVideoPlayAuthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetVideoPlayAuthResponse().from_map(
            await self.do_rpcrequest_async('GetVideoPlayAuth', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_video_play_auth(
        self,
        request: vod_20170321_models.GetVideoPlayAuthRequest,
    ) -> vod_20170321_models.GetVideoPlayAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_play_auth_with_options(request, runtime)

    async def get_video_play_auth_async(
        self,
        request: vod_20170321_models.GetVideoPlayAuthRequest,
    ) -> vod_20170321_models.GetVideoPlayAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_play_auth_with_options_async(request, runtime)

    def get_vod_template_with_options(
        self,
        request: vod_20170321_models.GetVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetVodTemplateResponse().from_map(
            self.do_rpcrequest('GetVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_vod_template_with_options_async(
        self,
        request: vod_20170321_models.GetVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetVodTemplateResponse().from_map(
            await self.do_rpcrequest_async('GetVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_vod_template(
        self,
        request: vod_20170321_models.GetVodTemplateRequest,
    ) -> vod_20170321_models.GetVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vod_template_with_options(request, runtime)

    async def get_vod_template_async(
        self,
        request: vod_20170321_models.GetVodTemplateRequest,
    ) -> vod_20170321_models.GetVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vod_template_with_options_async(request, runtime)

    def get_watermark_with_options(
        self,
        request: vod_20170321_models.GetWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetWatermarkResponse().from_map(
            self.do_rpcrequest('GetWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_watermark_with_options_async(
        self,
        request: vod_20170321_models.GetWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.GetWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.GetWatermarkResponse().from_map(
            await self.do_rpcrequest_async('GetWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_watermark(
        self,
        request: vod_20170321_models.GetWatermarkRequest,
    ) -> vod_20170321_models.GetWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_watermark_with_options(request, runtime)

    async def get_watermark_async(
        self,
        request: vod_20170321_models.GetWatermarkRequest,
    ) -> vod_20170321_models.GetWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_watermark_with_options_async(request, runtime)

    def list_aiimage_info_with_options(
        self,
        request: vod_20170321_models.ListAIImageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAIImageInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListAIImageInfoResponse().from_map(
            self.do_rpcrequest('ListAIImageInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_aiimage_info_with_options_async(
        self,
        request: vod_20170321_models.ListAIImageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAIImageInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListAIImageInfoResponse().from_map(
            await self.do_rpcrequest_async('ListAIImageInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_aiimage_info(
        self,
        request: vod_20170321_models.ListAIImageInfoRequest,
    ) -> vod_20170321_models.ListAIImageInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_aiimage_info_with_options(request, runtime)

    async def list_aiimage_info_async(
        self,
        request: vod_20170321_models.ListAIImageInfoRequest,
    ) -> vod_20170321_models.ListAIImageInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aiimage_info_with_options_async(request, runtime)

    def list_aijob_with_options(
        self,
        request: vod_20170321_models.ListAIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAIJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListAIJobResponse().from_map(
            self.do_rpcrequest('ListAIJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_aijob_with_options_async(
        self,
        request: vod_20170321_models.ListAIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAIJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListAIJobResponse().from_map(
            await self.do_rpcrequest_async('ListAIJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_aijob(
        self,
        request: vod_20170321_models.ListAIJobRequest,
    ) -> vod_20170321_models.ListAIJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_aijob_with_options(request, runtime)

    async def list_aijob_async(
        self,
        request: vod_20170321_models.ListAIJobRequest,
    ) -> vod_20170321_models.ListAIJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aijob_with_options_async(request, runtime)

    def list_aitemplate_with_options(
        self,
        request: vod_20170321_models.ListAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListAITemplateResponse().from_map(
            self.do_rpcrequest('ListAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_aitemplate_with_options_async(
        self,
        request: vod_20170321_models.ListAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListAITemplateResponse().from_map(
            await self.do_rpcrequest_async('ListAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_aitemplate(
        self,
        request: vod_20170321_models.ListAITemplateRequest,
    ) -> vod_20170321_models.ListAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_aitemplate_with_options(request, runtime)

    async def list_aitemplate_async(
        self,
        request: vod_20170321_models.ListAITemplateRequest,
    ) -> vod_20170321_models.ListAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aitemplate_with_options_async(request, runtime)

    def list_app_info_with_options(
        self,
        request: vod_20170321_models.ListAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListAppInfoResponse().from_map(
            self.do_rpcrequest('ListAppInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_app_info_with_options_async(
        self,
        request: vod_20170321_models.ListAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListAppInfoResponse().from_map(
            await self.do_rpcrequest_async('ListAppInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_app_info(
        self,
        request: vod_20170321_models.ListAppInfoRequest,
    ) -> vod_20170321_models.ListAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_info_with_options(request, runtime)

    async def list_app_info_async(
        self,
        request: vod_20170321_models.ListAppInfoRequest,
    ) -> vod_20170321_models.ListAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_info_with_options_async(request, runtime)

    def list_app_policies_for_identity_with_options(
        self,
        request: vod_20170321_models.ListAppPoliciesForIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAppPoliciesForIdentityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListAppPoliciesForIdentityResponse().from_map(
            self.do_rpcrequest('ListAppPoliciesForIdentity', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_app_policies_for_identity_with_options_async(
        self,
        request: vod_20170321_models.ListAppPoliciesForIdentityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAppPoliciesForIdentityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListAppPoliciesForIdentityResponse().from_map(
            await self.do_rpcrequest_async('ListAppPoliciesForIdentity', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_app_policies_for_identity(
        self,
        request: vod_20170321_models.ListAppPoliciesForIdentityRequest,
    ) -> vod_20170321_models.ListAppPoliciesForIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_policies_for_identity_with_options(request, runtime)

    async def list_app_policies_for_identity_async(
        self,
        request: vod_20170321_models.ListAppPoliciesForIdentityRequest,
    ) -> vod_20170321_models.ListAppPoliciesForIdentityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_policies_for_identity_with_options_async(request, runtime)

    def list_audit_security_ip_with_options(
        self,
        request: vod_20170321_models.ListAuditSecurityIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAuditSecurityIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListAuditSecurityIpResponse().from_map(
            self.do_rpcrequest('ListAuditSecurityIp', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_audit_security_ip_with_options_async(
        self,
        request: vod_20170321_models.ListAuditSecurityIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListAuditSecurityIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListAuditSecurityIpResponse().from_map(
            await self.do_rpcrequest_async('ListAuditSecurityIp', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_audit_security_ip(
        self,
        request: vod_20170321_models.ListAuditSecurityIpRequest,
    ) -> vod_20170321_models.ListAuditSecurityIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_audit_security_ip_with_options(request, runtime)

    async def list_audit_security_ip_async(
        self,
        request: vod_20170321_models.ListAuditSecurityIpRequest,
    ) -> vod_20170321_models.ListAuditSecurityIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_audit_security_ip_with_options_async(request, runtime)

    def list_dynamic_image_with_options(
        self,
        request: vod_20170321_models.ListDynamicImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListDynamicImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListDynamicImageResponse().from_map(
            self.do_rpcrequest('ListDynamicImage', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_dynamic_image_with_options_async(
        self,
        request: vod_20170321_models.ListDynamicImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListDynamicImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListDynamicImageResponse().from_map(
            await self.do_rpcrequest_async('ListDynamicImage', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_dynamic_image(
        self,
        request: vod_20170321_models.ListDynamicImageRequest,
    ) -> vod_20170321_models.ListDynamicImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dynamic_image_with_options(request, runtime)

    async def list_dynamic_image_async(
        self,
        request: vod_20170321_models.ListDynamicImageRequest,
    ) -> vod_20170321_models.ListDynamicImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dynamic_image_with_options_async(request, runtime)

    def list_live_record_video_with_options(
        self,
        request: vod_20170321_models.ListLiveRecordVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListLiveRecordVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListLiveRecordVideoResponse().from_map(
            self.do_rpcrequest('ListLiveRecordVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_live_record_video_with_options_async(
        self,
        request: vod_20170321_models.ListLiveRecordVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListLiveRecordVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListLiveRecordVideoResponse().from_map(
            await self.do_rpcrequest_async('ListLiveRecordVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_live_record_video(
        self,
        request: vod_20170321_models.ListLiveRecordVideoRequest,
    ) -> vod_20170321_models.ListLiveRecordVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_record_video_with_options(request, runtime)

    async def list_live_record_video_async(
        self,
        request: vod_20170321_models.ListLiveRecordVideoRequest,
    ) -> vod_20170321_models.ListLiveRecordVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_record_video_with_options_async(request, runtime)

    def list_media_dnadelete_job_with_options(
        self,
        request: vod_20170321_models.ListMediaDNADeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListMediaDNADeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListMediaDNADeleteJobResponse().from_map(
            self.do_rpcrequest('ListMediaDNADeleteJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_media_dnadelete_job_with_options_async(
        self,
        request: vod_20170321_models.ListMediaDNADeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListMediaDNADeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListMediaDNADeleteJobResponse().from_map(
            await self.do_rpcrequest_async('ListMediaDNADeleteJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_media_dnadelete_job(
        self,
        request: vod_20170321_models.ListMediaDNADeleteJobRequest,
    ) -> vod_20170321_models.ListMediaDNADeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_media_dnadelete_job_with_options(request, runtime)

    async def list_media_dnadelete_job_async(
        self,
        request: vod_20170321_models.ListMediaDNADeleteJobRequest,
    ) -> vod_20170321_models.ListMediaDNADeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_media_dnadelete_job_with_options_async(request, runtime)

    def list_snapshots_with_options(
        self,
        request: vod_20170321_models.ListSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListSnapshotsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListSnapshotsResponse().from_map(
            self.do_rpcrequest('ListSnapshots', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_snapshots_with_options_async(
        self,
        request: vod_20170321_models.ListSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListSnapshotsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListSnapshotsResponse().from_map(
            await self.do_rpcrequest_async('ListSnapshots', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_snapshots(
        self,
        request: vod_20170321_models.ListSnapshotsRequest,
    ) -> vod_20170321_models.ListSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_snapshots_with_options(request, runtime)

    async def list_snapshots_async(
        self,
        request: vod_20170321_models.ListSnapshotsRequest,
    ) -> vod_20170321_models.ListSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_snapshots_with_options_async(request, runtime)

    def list_transcode_task_with_options(
        self,
        request: vod_20170321_models.ListTranscodeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListTranscodeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListTranscodeTaskResponse().from_map(
            self.do_rpcrequest('ListTranscodeTask', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_transcode_task_with_options_async(
        self,
        request: vod_20170321_models.ListTranscodeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListTranscodeTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListTranscodeTaskResponse().from_map(
            await self.do_rpcrequest_async('ListTranscodeTask', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_transcode_task(
        self,
        request: vod_20170321_models.ListTranscodeTaskRequest,
    ) -> vod_20170321_models.ListTranscodeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transcode_task_with_options(request, runtime)

    async def list_transcode_task_async(
        self,
        request: vod_20170321_models.ListTranscodeTaskRequest,
    ) -> vod_20170321_models.ListTranscodeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transcode_task_with_options_async(request, runtime)

    def list_transcode_template_group_with_options(
        self,
        request: vod_20170321_models.ListTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListTranscodeTemplateGroupResponse().from_map(
            self.do_rpcrequest('ListTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_transcode_template_group_with_options_async(
        self,
        request: vod_20170321_models.ListTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListTranscodeTemplateGroupResponse().from_map(
            await self.do_rpcrequest_async('ListTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_transcode_template_group(
        self,
        request: vod_20170321_models.ListTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.ListTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transcode_template_group_with_options(request, runtime)

    async def list_transcode_template_group_async(
        self,
        request: vod_20170321_models.ListTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.ListTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transcode_template_group_with_options_async(request, runtime)

    def list_vod_template_with_options(
        self,
        request: vod_20170321_models.ListVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListVodTemplateResponse().from_map(
            self.do_rpcrequest('ListVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_vod_template_with_options_async(
        self,
        request: vod_20170321_models.ListVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListVodTemplateResponse().from_map(
            await self.do_rpcrequest_async('ListVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vod_template(
        self,
        request: vod_20170321_models.ListVodTemplateRequest,
    ) -> vod_20170321_models.ListVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vod_template_with_options(request, runtime)

    async def list_vod_template_async(
        self,
        request: vod_20170321_models.ListVodTemplateRequest,
    ) -> vod_20170321_models.ListVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vod_template_with_options_async(request, runtime)

    def list_watermark_with_options(
        self,
        request: vod_20170321_models.ListWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListWatermarkResponse().from_map(
            self.do_rpcrequest('ListWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_watermark_with_options_async(
        self,
        request: vod_20170321_models.ListWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ListWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ListWatermarkResponse().from_map(
            await self.do_rpcrequest_async('ListWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_watermark(
        self,
        request: vod_20170321_models.ListWatermarkRequest,
    ) -> vod_20170321_models.ListWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_watermark_with_options(request, runtime)

    async def list_watermark_async(
        self,
        request: vod_20170321_models.ListWatermarkRequest,
    ) -> vod_20170321_models.ListWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_watermark_with_options_async(request, runtime)

    def move_app_resource_with_options(
        self,
        request: vod_20170321_models.MoveAppResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.MoveAppResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.MoveAppResourceResponse().from_map(
            self.do_rpcrequest('MoveAppResource', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_app_resource_with_options_async(
        self,
        request: vod_20170321_models.MoveAppResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.MoveAppResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.MoveAppResourceResponse().from_map(
            await self.do_rpcrequest_async('MoveAppResource', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_app_resource(
        self,
        request: vod_20170321_models.MoveAppResourceRequest,
    ) -> vod_20170321_models.MoveAppResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_app_resource_with_options(request, runtime)

    async def move_app_resource_async(
        self,
        request: vod_20170321_models.MoveAppResourceRequest,
    ) -> vod_20170321_models.MoveAppResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_app_resource_with_options_async(request, runtime)

    def preload_vod_object_caches_with_options(
        self,
        request: vod_20170321_models.PreloadVodObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.PreloadVodObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.PreloadVodObjectCachesResponse().from_map(
            self.do_rpcrequest('PreloadVodObjectCaches', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def preload_vod_object_caches_with_options_async(
        self,
        request: vod_20170321_models.PreloadVodObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.PreloadVodObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.PreloadVodObjectCachesResponse().from_map(
            await self.do_rpcrequest_async('PreloadVodObjectCaches', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def preload_vod_object_caches(
        self,
        request: vod_20170321_models.PreloadVodObjectCachesRequest,
    ) -> vod_20170321_models.PreloadVodObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.preload_vod_object_caches_with_options(request, runtime)

    async def preload_vod_object_caches_async(
        self,
        request: vod_20170321_models.PreloadVodObjectCachesRequest,
    ) -> vod_20170321_models.PreloadVodObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.preload_vod_object_caches_with_options_async(request, runtime)

    def produce_editing_project_video_with_options(
        self,
        request: vod_20170321_models.ProduceEditingProjectVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ProduceEditingProjectVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ProduceEditingProjectVideoResponse().from_map(
            self.do_rpcrequest('ProduceEditingProjectVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def produce_editing_project_video_with_options_async(
        self,
        request: vod_20170321_models.ProduceEditingProjectVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.ProduceEditingProjectVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.ProduceEditingProjectVideoResponse().from_map(
            await self.do_rpcrequest_async('ProduceEditingProjectVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def produce_editing_project_video(
        self,
        request: vod_20170321_models.ProduceEditingProjectVideoRequest,
    ) -> vod_20170321_models.ProduceEditingProjectVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.produce_editing_project_video_with_options(request, runtime)

    async def produce_editing_project_video_async(
        self,
        request: vod_20170321_models.ProduceEditingProjectVideoRequest,
    ) -> vod_20170321_models.ProduceEditingProjectVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.produce_editing_project_video_with_options_async(request, runtime)

    def refresh_upload_video_with_options(
        self,
        request: vod_20170321_models.RefreshUploadVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.RefreshUploadVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.RefreshUploadVideoResponse().from_map(
            self.do_rpcrequest('RefreshUploadVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_upload_video_with_options_async(
        self,
        request: vod_20170321_models.RefreshUploadVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.RefreshUploadVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.RefreshUploadVideoResponse().from_map(
            await self.do_rpcrequest_async('RefreshUploadVideo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_upload_video(
        self,
        request: vod_20170321_models.RefreshUploadVideoRequest,
    ) -> vod_20170321_models.RefreshUploadVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_upload_video_with_options(request, runtime)

    async def refresh_upload_video_async(
        self,
        request: vod_20170321_models.RefreshUploadVideoRequest,
    ) -> vod_20170321_models.RefreshUploadVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_upload_video_with_options_async(request, runtime)

    def refresh_vod_object_caches_with_options(
        self,
        request: vod_20170321_models.RefreshVodObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.RefreshVodObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.RefreshVodObjectCachesResponse().from_map(
            self.do_rpcrequest('RefreshVodObjectCaches', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_vod_object_caches_with_options_async(
        self,
        request: vod_20170321_models.RefreshVodObjectCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.RefreshVodObjectCachesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.RefreshVodObjectCachesResponse().from_map(
            await self.do_rpcrequest_async('RefreshVodObjectCaches', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_vod_object_caches(
        self,
        request: vod_20170321_models.RefreshVodObjectCachesRequest,
    ) -> vod_20170321_models.RefreshVodObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_vod_object_caches_with_options(request, runtime)

    async def refresh_vod_object_caches_async(
        self,
        request: vod_20170321_models.RefreshVodObjectCachesRequest,
    ) -> vod_20170321_models.RefreshVodObjectCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_vod_object_caches_with_options_async(request, runtime)

    def register_media_with_options(
        self,
        request: vod_20170321_models.RegisterMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.RegisterMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.RegisterMediaResponse().from_map(
            self.do_rpcrequest('RegisterMedia', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_media_with_options_async(
        self,
        request: vod_20170321_models.RegisterMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.RegisterMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.RegisterMediaResponse().from_map(
            await self.do_rpcrequest_async('RegisterMedia', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_media(
        self,
        request: vod_20170321_models.RegisterMediaRequest,
    ) -> vod_20170321_models.RegisterMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_media_with_options(request, runtime)

    async def register_media_async(
        self,
        request: vod_20170321_models.RegisterMediaRequest,
    ) -> vod_20170321_models.RegisterMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_media_with_options_async(request, runtime)

    def search_editing_project_with_options(
        self,
        request: vod_20170321_models.SearchEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SearchEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SearchEditingProjectResponse().from_map(
            self.do_rpcrequest('SearchEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_editing_project_with_options_async(
        self,
        request: vod_20170321_models.SearchEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SearchEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SearchEditingProjectResponse().from_map(
            await self.do_rpcrequest_async('SearchEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_editing_project(
        self,
        request: vod_20170321_models.SearchEditingProjectRequest,
    ) -> vod_20170321_models.SearchEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_editing_project_with_options(request, runtime)

    async def search_editing_project_async(
        self,
        request: vod_20170321_models.SearchEditingProjectRequest,
    ) -> vod_20170321_models.SearchEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_editing_project_with_options_async(request, runtime)

    def search_media_with_options(
        self,
        request: vod_20170321_models.SearchMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SearchMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SearchMediaResponse().from_map(
            self.do_rpcrequest('SearchMedia', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_media_with_options_async(
        self,
        request: vod_20170321_models.SearchMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SearchMediaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SearchMediaResponse().from_map(
            await self.do_rpcrequest_async('SearchMedia', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_media(
        self,
        request: vod_20170321_models.SearchMediaRequest,
    ) -> vod_20170321_models.SearchMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_media_with_options(request, runtime)

    async def search_media_async(
        self,
        request: vod_20170321_models.SearchMediaRequest,
    ) -> vod_20170321_models.SearchMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_media_with_options_async(request, runtime)

    def set_audit_security_ip_with_options(
        self,
        request: vod_20170321_models.SetAuditSecurityIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetAuditSecurityIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SetAuditSecurityIpResponse().from_map(
            self.do_rpcrequest('SetAuditSecurityIp', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_audit_security_ip_with_options_async(
        self,
        request: vod_20170321_models.SetAuditSecurityIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetAuditSecurityIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SetAuditSecurityIpResponse().from_map(
            await self.do_rpcrequest_async('SetAuditSecurityIp', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_audit_security_ip(
        self,
        request: vod_20170321_models.SetAuditSecurityIpRequest,
    ) -> vod_20170321_models.SetAuditSecurityIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_audit_security_ip_with_options(request, runtime)

    async def set_audit_security_ip_async(
        self,
        request: vod_20170321_models.SetAuditSecurityIpRequest,
    ) -> vod_20170321_models.SetAuditSecurityIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_audit_security_ip_with_options_async(request, runtime)

    def set_default_aitemplate_with_options(
        self,
        request: vod_20170321_models.SetDefaultAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetDefaultAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SetDefaultAITemplateResponse().from_map(
            self.do_rpcrequest('SetDefaultAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_default_aitemplate_with_options_async(
        self,
        request: vod_20170321_models.SetDefaultAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetDefaultAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SetDefaultAITemplateResponse().from_map(
            await self.do_rpcrequest_async('SetDefaultAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_default_aitemplate(
        self,
        request: vod_20170321_models.SetDefaultAITemplateRequest,
    ) -> vod_20170321_models.SetDefaultAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_default_aitemplate_with_options(request, runtime)

    async def set_default_aitemplate_async(
        self,
        request: vod_20170321_models.SetDefaultAITemplateRequest,
    ) -> vod_20170321_models.SetDefaultAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_default_aitemplate_with_options_async(request, runtime)

    def set_default_transcode_template_group_with_options(
        self,
        request: vod_20170321_models.SetDefaultTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetDefaultTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SetDefaultTranscodeTemplateGroupResponse().from_map(
            self.do_rpcrequest('SetDefaultTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_default_transcode_template_group_with_options_async(
        self,
        request: vod_20170321_models.SetDefaultTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetDefaultTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SetDefaultTranscodeTemplateGroupResponse().from_map(
            await self.do_rpcrequest_async('SetDefaultTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_default_transcode_template_group(
        self,
        request: vod_20170321_models.SetDefaultTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.SetDefaultTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_default_transcode_template_group_with_options(request, runtime)

    async def set_default_transcode_template_group_async(
        self,
        request: vod_20170321_models.SetDefaultTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.SetDefaultTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_default_transcode_template_group_with_options_async(request, runtime)

    def set_default_watermark_with_options(
        self,
        request: vod_20170321_models.SetDefaultWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetDefaultWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SetDefaultWatermarkResponse().from_map(
            self.do_rpcrequest('SetDefaultWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_default_watermark_with_options_async(
        self,
        request: vod_20170321_models.SetDefaultWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetDefaultWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SetDefaultWatermarkResponse().from_map(
            await self.do_rpcrequest_async('SetDefaultWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_default_watermark(
        self,
        request: vod_20170321_models.SetDefaultWatermarkRequest,
    ) -> vod_20170321_models.SetDefaultWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_default_watermark_with_options(request, runtime)

    async def set_default_watermark_async(
        self,
        request: vod_20170321_models.SetDefaultWatermarkRequest,
    ) -> vod_20170321_models.SetDefaultWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_default_watermark_with_options_async(request, runtime)

    def set_editing_project_materials_with_options(
        self,
        request: vod_20170321_models.SetEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SetEditingProjectMaterialsResponse().from_map(
            self.do_rpcrequest('SetEditingProjectMaterials', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_editing_project_materials_with_options_async(
        self,
        request: vod_20170321_models.SetEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SetEditingProjectMaterialsResponse().from_map(
            await self.do_rpcrequest_async('SetEditingProjectMaterials', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_editing_project_materials(
        self,
        request: vod_20170321_models.SetEditingProjectMaterialsRequest,
    ) -> vod_20170321_models.SetEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_editing_project_materials_with_options(request, runtime)

    async def set_editing_project_materials_async(
        self,
        request: vod_20170321_models.SetEditingProjectMaterialsRequest,
    ) -> vod_20170321_models.SetEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_editing_project_materials_with_options_async(request, runtime)

    def set_message_callback_with_options(
        self,
        request: vod_20170321_models.SetMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetMessageCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SetMessageCallbackResponse().from_map(
            self.do_rpcrequest('SetMessageCallback', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_message_callback_with_options_async(
        self,
        request: vod_20170321_models.SetMessageCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetMessageCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SetMessageCallbackResponse().from_map(
            await self.do_rpcrequest_async('SetMessageCallback', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_message_callback(
        self,
        request: vod_20170321_models.SetMessageCallbackRequest,
    ) -> vod_20170321_models.SetMessageCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_message_callback_with_options(request, runtime)

    async def set_message_callback_async(
        self,
        request: vod_20170321_models.SetMessageCallbackRequest,
    ) -> vod_20170321_models.SetMessageCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_message_callback_with_options_async(request, runtime)

    def set_vod_domain_certificate_with_options(
        self,
        request: vod_20170321_models.SetVodDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetVodDomainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SetVodDomainCertificateResponse().from_map(
            self.do_rpcrequest('SetVodDomainCertificate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_vod_domain_certificate_with_options_async(
        self,
        request: vod_20170321_models.SetVodDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SetVodDomainCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SetVodDomainCertificateResponse().from_map(
            await self.do_rpcrequest_async('SetVodDomainCertificate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_vod_domain_certificate(
        self,
        request: vod_20170321_models.SetVodDomainCertificateRequest,
    ) -> vod_20170321_models.SetVodDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_vod_domain_certificate_with_options(request, runtime)

    async def set_vod_domain_certificate_async(
        self,
        request: vod_20170321_models.SetVodDomainCertificateRequest,
    ) -> vod_20170321_models.SetVodDomainCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_vod_domain_certificate_with_options_async(request, runtime)

    def submit_aiimage_audit_job_with_options(
        self,
        request: vod_20170321_models.SubmitAIImageAuditJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAIImageAuditJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitAIImageAuditJobResponse().from_map(
            self.do_rpcrequest('SubmitAIImageAuditJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_aiimage_audit_job_with_options_async(
        self,
        request: vod_20170321_models.SubmitAIImageAuditJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAIImageAuditJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitAIImageAuditJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitAIImageAuditJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_aiimage_audit_job(
        self,
        request: vod_20170321_models.SubmitAIImageAuditJobRequest,
    ) -> vod_20170321_models.SubmitAIImageAuditJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_aiimage_audit_job_with_options(request, runtime)

    async def submit_aiimage_audit_job_async(
        self,
        request: vod_20170321_models.SubmitAIImageAuditJobRequest,
    ) -> vod_20170321_models.SubmitAIImageAuditJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_aiimage_audit_job_with_options_async(request, runtime)

    def submit_aiimage_job_with_options(
        self,
        request: vod_20170321_models.SubmitAIImageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAIImageJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitAIImageJobResponse().from_map(
            self.do_rpcrequest('SubmitAIImageJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_aiimage_job_with_options_async(
        self,
        request: vod_20170321_models.SubmitAIImageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAIImageJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitAIImageJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitAIImageJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_aiimage_job(
        self,
        request: vod_20170321_models.SubmitAIImageJobRequest,
    ) -> vod_20170321_models.SubmitAIImageJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_aiimage_job_with_options(request, runtime)

    async def submit_aiimage_job_async(
        self,
        request: vod_20170321_models.SubmitAIImageJobRequest,
    ) -> vod_20170321_models.SubmitAIImageJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_aiimage_job_with_options_async(request, runtime)

    def submit_aijob_with_options(
        self,
        request: vod_20170321_models.SubmitAIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAIJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitAIJobResponse().from_map(
            self.do_rpcrequest('SubmitAIJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_aijob_with_options_async(
        self,
        request: vod_20170321_models.SubmitAIJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAIJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitAIJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitAIJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_aijob(
        self,
        request: vod_20170321_models.SubmitAIJobRequest,
    ) -> vod_20170321_models.SubmitAIJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_aijob_with_options(request, runtime)

    async def submit_aijob_async(
        self,
        request: vod_20170321_models.SubmitAIJobRequest,
    ) -> vod_20170321_models.SubmitAIJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_aijob_with_options_async(request, runtime)

    def submit_aimedia_audit_job_with_options(
        self,
        request: vod_20170321_models.SubmitAIMediaAuditJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAIMediaAuditJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitAIMediaAuditJobResponse().from_map(
            self.do_rpcrequest('SubmitAIMediaAuditJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_aimedia_audit_job_with_options_async(
        self,
        request: vod_20170321_models.SubmitAIMediaAuditJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitAIMediaAuditJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitAIMediaAuditJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitAIMediaAuditJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_aimedia_audit_job(
        self,
        request: vod_20170321_models.SubmitAIMediaAuditJobRequest,
    ) -> vod_20170321_models.SubmitAIMediaAuditJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_aimedia_audit_job_with_options(request, runtime)

    async def submit_aimedia_audit_job_async(
        self,
        request: vod_20170321_models.SubmitAIMediaAuditJobRequest,
    ) -> vod_20170321_models.SubmitAIMediaAuditJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_aimedia_audit_job_with_options_async(request, runtime)

    def submit_dynamic_image_job_with_options(
        self,
        request: vod_20170321_models.SubmitDynamicImageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitDynamicImageJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitDynamicImageJobResponse().from_map(
            self.do_rpcrequest('SubmitDynamicImageJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_dynamic_image_job_with_options_async(
        self,
        request: vod_20170321_models.SubmitDynamicImageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitDynamicImageJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitDynamicImageJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitDynamicImageJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_dynamic_image_job(
        self,
        request: vod_20170321_models.SubmitDynamicImageJobRequest,
    ) -> vod_20170321_models.SubmitDynamicImageJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_dynamic_image_job_with_options(request, runtime)

    async def submit_dynamic_image_job_async(
        self,
        request: vod_20170321_models.SubmitDynamicImageJobRequest,
    ) -> vod_20170321_models.SubmitDynamicImageJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_dynamic_image_job_with_options_async(request, runtime)

    def submit_media_dnadelete_job_with_options(
        self,
        request: vod_20170321_models.SubmitMediaDNADeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitMediaDNADeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitMediaDNADeleteJobResponse().from_map(
            self.do_rpcrequest('SubmitMediaDNADeleteJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_media_dnadelete_job_with_options_async(
        self,
        request: vod_20170321_models.SubmitMediaDNADeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitMediaDNADeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitMediaDNADeleteJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitMediaDNADeleteJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_media_dnadelete_job(
        self,
        request: vod_20170321_models.SubmitMediaDNADeleteJobRequest,
    ) -> vod_20170321_models.SubmitMediaDNADeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_media_dnadelete_job_with_options(request, runtime)

    async def submit_media_dnadelete_job_async(
        self,
        request: vod_20170321_models.SubmitMediaDNADeleteJobRequest,
    ) -> vod_20170321_models.SubmitMediaDNADeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_media_dnadelete_job_with_options_async(request, runtime)

    def submit_preprocess_jobs_with_options(
        self,
        request: vod_20170321_models.SubmitPreprocessJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitPreprocessJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitPreprocessJobsResponse().from_map(
            self.do_rpcrequest('SubmitPreprocessJobs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_preprocess_jobs_with_options_async(
        self,
        request: vod_20170321_models.SubmitPreprocessJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitPreprocessJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitPreprocessJobsResponse().from_map(
            await self.do_rpcrequest_async('SubmitPreprocessJobs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_preprocess_jobs(
        self,
        request: vod_20170321_models.SubmitPreprocessJobsRequest,
    ) -> vod_20170321_models.SubmitPreprocessJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_preprocess_jobs_with_options(request, runtime)

    async def submit_preprocess_jobs_async(
        self,
        request: vod_20170321_models.SubmitPreprocessJobsRequest,
    ) -> vod_20170321_models.SubmitPreprocessJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_preprocess_jobs_with_options_async(request, runtime)

    def submit_snapshot_job_with_options(
        self,
        request: vod_20170321_models.SubmitSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitSnapshotJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitSnapshotJobResponse().from_map(
            self.do_rpcrequest('SubmitSnapshotJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_snapshot_job_with_options_async(
        self,
        request: vod_20170321_models.SubmitSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitSnapshotJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitSnapshotJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitSnapshotJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_snapshot_job(
        self,
        request: vod_20170321_models.SubmitSnapshotJobRequest,
    ) -> vod_20170321_models.SubmitSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_snapshot_job_with_options(request, runtime)

    async def submit_snapshot_job_async(
        self,
        request: vod_20170321_models.SubmitSnapshotJobRequest,
    ) -> vod_20170321_models.SubmitSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_snapshot_job_with_options_async(request, runtime)

    def submit_transcode_jobs_with_options(
        self,
        request: vod_20170321_models.SubmitTranscodeJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitTranscodeJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitTranscodeJobsResponse().from_map(
            self.do_rpcrequest('SubmitTranscodeJobs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_transcode_jobs_with_options_async(
        self,
        request: vod_20170321_models.SubmitTranscodeJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitTranscodeJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitTranscodeJobsResponse().from_map(
            await self.do_rpcrequest_async('SubmitTranscodeJobs', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_transcode_jobs(
        self,
        request: vod_20170321_models.SubmitTranscodeJobsRequest,
    ) -> vod_20170321_models.SubmitTranscodeJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_transcode_jobs_with_options(request, runtime)

    async def submit_transcode_jobs_async(
        self,
        request: vod_20170321_models.SubmitTranscodeJobsRequest,
    ) -> vod_20170321_models.SubmitTranscodeJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_transcode_jobs_with_options_async(request, runtime)

    def submit_workflow_job_with_options(
        self,
        request: vod_20170321_models.SubmitWorkflowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitWorkflowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitWorkflowJobResponse().from_map(
            self.do_rpcrequest('SubmitWorkflowJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_workflow_job_with_options_async(
        self,
        request: vod_20170321_models.SubmitWorkflowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.SubmitWorkflowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.SubmitWorkflowJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitWorkflowJob', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_workflow_job(
        self,
        request: vod_20170321_models.SubmitWorkflowJobRequest,
    ) -> vod_20170321_models.SubmitWorkflowJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_workflow_job_with_options(request, runtime)

    async def submit_workflow_job_async(
        self,
        request: vod_20170321_models.SubmitWorkflowJobRequest,
    ) -> vod_20170321_models.SubmitWorkflowJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_workflow_job_with_options_async(request, runtime)

    def tag_vod_resources_with_options(
        self,
        request: vod_20170321_models.TagVodResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.TagVodResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.TagVodResourcesResponse().from_map(
            self.do_rpcrequest('TagVodResources', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_vod_resources_with_options_async(
        self,
        request: vod_20170321_models.TagVodResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.TagVodResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.TagVodResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagVodResources', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_vod_resources(
        self,
        request: vod_20170321_models.TagVodResourcesRequest,
    ) -> vod_20170321_models.TagVodResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_vod_resources_with_options(request, runtime)

    async def tag_vod_resources_async(
        self,
        request: vod_20170321_models.TagVodResourcesRequest,
    ) -> vod_20170321_models.TagVodResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_vod_resources_with_options_async(request, runtime)

    def un_tag_vod_resources_with_options(
        self,
        request: vod_20170321_models.UnTagVodResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UnTagVodResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UnTagVodResourcesResponse().from_map(
            self.do_rpcrequest('UnTagVodResources', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def un_tag_vod_resources_with_options_async(
        self,
        request: vod_20170321_models.UnTagVodResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UnTagVodResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UnTagVodResourcesResponse().from_map(
            await self.do_rpcrequest_async('UnTagVodResources', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def un_tag_vod_resources(
        self,
        request: vod_20170321_models.UnTagVodResourcesRequest,
    ) -> vod_20170321_models.UnTagVodResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.un_tag_vod_resources_with_options(request, runtime)

    async def un_tag_vod_resources_async(
        self,
        request: vod_20170321_models.UnTagVodResourcesRequest,
    ) -> vod_20170321_models.UnTagVodResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.un_tag_vod_resources_with_options_async(request, runtime)

    def update_aitemplate_with_options(
        self,
        request: vod_20170321_models.UpdateAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateAITemplateResponse().from_map(
            self.do_rpcrequest('UpdateAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_aitemplate_with_options_async(
        self,
        request: vod_20170321_models.UpdateAITemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateAITemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateAITemplateResponse().from_map(
            await self.do_rpcrequest_async('UpdateAITemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_aitemplate(
        self,
        request: vod_20170321_models.UpdateAITemplateRequest,
    ) -> vod_20170321_models.UpdateAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_aitemplate_with_options(request, runtime)

    async def update_aitemplate_async(
        self,
        request: vod_20170321_models.UpdateAITemplateRequest,
    ) -> vod_20170321_models.UpdateAITemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_aitemplate_with_options_async(request, runtime)

    def update_app_info_with_options(
        self,
        request: vod_20170321_models.UpdateAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateAppInfoResponse().from_map(
            self.do_rpcrequest('UpdateAppInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_app_info_with_options_async(
        self,
        request: vod_20170321_models.UpdateAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateAppInfoResponse().from_map(
            await self.do_rpcrequest_async('UpdateAppInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_info(
        self,
        request: vod_20170321_models.UpdateAppInfoRequest,
    ) -> vod_20170321_models.UpdateAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_info_with_options(request, runtime)

    async def update_app_info_async(
        self,
        request: vod_20170321_models.UpdateAppInfoRequest,
    ) -> vod_20170321_models.UpdateAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_info_with_options_async(request, runtime)

    def update_attached_media_infos_with_options(
        self,
        request: vod_20170321_models.UpdateAttachedMediaInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateAttachedMediaInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateAttachedMediaInfosResponse().from_map(
            self.do_rpcrequest('UpdateAttachedMediaInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_attached_media_infos_with_options_async(
        self,
        request: vod_20170321_models.UpdateAttachedMediaInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateAttachedMediaInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateAttachedMediaInfosResponse().from_map(
            await self.do_rpcrequest_async('UpdateAttachedMediaInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_attached_media_infos(
        self,
        request: vod_20170321_models.UpdateAttachedMediaInfosRequest,
    ) -> vod_20170321_models.UpdateAttachedMediaInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_attached_media_infos_with_options(request, runtime)

    async def update_attached_media_infos_async(
        self,
        request: vod_20170321_models.UpdateAttachedMediaInfosRequest,
    ) -> vod_20170321_models.UpdateAttachedMediaInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_attached_media_infos_with_options_async(request, runtime)

    def update_category_with_options(
        self,
        request: vod_20170321_models.UpdateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateCategoryResponse().from_map(
            self.do_rpcrequest('UpdateCategory', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_category_with_options_async(
        self,
        request: vod_20170321_models.UpdateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateCategoryResponse().from_map(
            await self.do_rpcrequest_async('UpdateCategory', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_category(
        self,
        request: vod_20170321_models.UpdateCategoryRequest,
    ) -> vod_20170321_models.UpdateCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_category_with_options(request, runtime)

    async def update_category_async(
        self,
        request: vod_20170321_models.UpdateCategoryRequest,
    ) -> vod_20170321_models.UpdateCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_category_with_options_async(request, runtime)

    def update_editing_project_with_options(
        self,
        request: vod_20170321_models.UpdateEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateEditingProjectResponse().from_map(
            self.do_rpcrequest('UpdateEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_editing_project_with_options_async(
        self,
        request: vod_20170321_models.UpdateEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateEditingProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateEditingProjectResponse().from_map(
            await self.do_rpcrequest_async('UpdateEditingProject', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_editing_project(
        self,
        request: vod_20170321_models.UpdateEditingProjectRequest,
    ) -> vod_20170321_models.UpdateEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_editing_project_with_options(request, runtime)

    async def update_editing_project_async(
        self,
        request: vod_20170321_models.UpdateEditingProjectRequest,
    ) -> vod_20170321_models.UpdateEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_editing_project_with_options_async(request, runtime)

    def update_image_infos_with_options(
        self,
        request: vod_20170321_models.UpdateImageInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateImageInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateImageInfosResponse().from_map(
            self.do_rpcrequest('UpdateImageInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_image_infos_with_options_async(
        self,
        request: vod_20170321_models.UpdateImageInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateImageInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateImageInfosResponse().from_map(
            await self.do_rpcrequest_async('UpdateImageInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_image_infos(
        self,
        request: vod_20170321_models.UpdateImageInfosRequest,
    ) -> vod_20170321_models.UpdateImageInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_image_infos_with_options(request, runtime)

    async def update_image_infos_async(
        self,
        request: vod_20170321_models.UpdateImageInfosRequest,
    ) -> vod_20170321_models.UpdateImageInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_image_infos_with_options_async(request, runtime)

    def update_transcode_template_group_with_options(
        self,
        request: vod_20170321_models.UpdateTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateTranscodeTemplateGroupResponse().from_map(
            self.do_rpcrequest('UpdateTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_transcode_template_group_with_options_async(
        self,
        request: vod_20170321_models.UpdateTranscodeTemplateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateTranscodeTemplateGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateTranscodeTemplateGroupResponse().from_map(
            await self.do_rpcrequest_async('UpdateTranscodeTemplateGroup', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_transcode_template_group(
        self,
        request: vod_20170321_models.UpdateTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.UpdateTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_transcode_template_group_with_options(request, runtime)

    async def update_transcode_template_group_async(
        self,
        request: vod_20170321_models.UpdateTranscodeTemplateGroupRequest,
    ) -> vod_20170321_models.UpdateTranscodeTemplateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_transcode_template_group_with_options_async(request, runtime)

    def update_video_info_with_options(
        self,
        request: vod_20170321_models.UpdateVideoInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateVideoInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateVideoInfoResponse().from_map(
            self.do_rpcrequest('UpdateVideoInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_video_info_with_options_async(
        self,
        request: vod_20170321_models.UpdateVideoInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateVideoInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateVideoInfoResponse().from_map(
            await self.do_rpcrequest_async('UpdateVideoInfo', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_video_info(
        self,
        request: vod_20170321_models.UpdateVideoInfoRequest,
    ) -> vod_20170321_models.UpdateVideoInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_video_info_with_options(request, runtime)

    async def update_video_info_async(
        self,
        request: vod_20170321_models.UpdateVideoInfoRequest,
    ) -> vod_20170321_models.UpdateVideoInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_video_info_with_options_async(request, runtime)

    def update_video_infos_with_options(
        self,
        request: vod_20170321_models.UpdateVideoInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateVideoInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateVideoInfosResponse().from_map(
            self.do_rpcrequest('UpdateVideoInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_video_infos_with_options_async(
        self,
        request: vod_20170321_models.UpdateVideoInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateVideoInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateVideoInfosResponse().from_map(
            await self.do_rpcrequest_async('UpdateVideoInfos', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_video_infos(
        self,
        request: vod_20170321_models.UpdateVideoInfosRequest,
    ) -> vod_20170321_models.UpdateVideoInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_video_infos_with_options(request, runtime)

    async def update_video_infos_async(
        self,
        request: vod_20170321_models.UpdateVideoInfosRequest,
    ) -> vod_20170321_models.UpdateVideoInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_video_infos_with_options_async(request, runtime)

    def update_vod_domain_with_options(
        self,
        request: vod_20170321_models.UpdateVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateVodDomainResponse().from_map(
            self.do_rpcrequest('UpdateVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_vod_domain_with_options_async(
        self,
        request: vod_20170321_models.UpdateVodDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateVodDomainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateVodDomainResponse().from_map(
            await self.do_rpcrequest_async('UpdateVodDomain', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_vod_domain(
        self,
        request: vod_20170321_models.UpdateVodDomainRequest,
    ) -> vod_20170321_models.UpdateVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_vod_domain_with_options(request, runtime)

    async def update_vod_domain_async(
        self,
        request: vod_20170321_models.UpdateVodDomainRequest,
    ) -> vod_20170321_models.UpdateVodDomainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_vod_domain_with_options_async(request, runtime)

    def update_vod_template_with_options(
        self,
        request: vod_20170321_models.UpdateVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateVodTemplateResponse().from_map(
            self.do_rpcrequest('UpdateVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_vod_template_with_options_async(
        self,
        request: vod_20170321_models.UpdateVodTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateVodTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateVodTemplateResponse().from_map(
            await self.do_rpcrequest_async('UpdateVodTemplate', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_vod_template(
        self,
        request: vod_20170321_models.UpdateVodTemplateRequest,
    ) -> vod_20170321_models.UpdateVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_vod_template_with_options(request, runtime)

    async def update_vod_template_async(
        self,
        request: vod_20170321_models.UpdateVodTemplateRequest,
    ) -> vod_20170321_models.UpdateVodTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_vod_template_with_options_async(request, runtime)

    def update_watermark_with_options(
        self,
        request: vod_20170321_models.UpdateWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateWatermarkResponse().from_map(
            self.do_rpcrequest('UpdateWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_watermark_with_options_async(
        self,
        request: vod_20170321_models.UpdateWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UpdateWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UpdateWatermarkResponse().from_map(
            await self.do_rpcrequest_async('UpdateWatermark', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_watermark(
        self,
        request: vod_20170321_models.UpdateWatermarkRequest,
    ) -> vod_20170321_models.UpdateWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_watermark_with_options(request, runtime)

    async def update_watermark_async(
        self,
        request: vod_20170321_models.UpdateWatermarkRequest,
    ) -> vod_20170321_models.UpdateWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_watermark_with_options_async(request, runtime)

    def upload_media_by_urlwith_options(
        self,
        request: vod_20170321_models.UploadMediaByURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UploadMediaByURLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UploadMediaByURLResponse().from_map(
            self.do_rpcrequest('UploadMediaByURL', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_media_by_urlwith_options_async(
        self,
        request: vod_20170321_models.UploadMediaByURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.UploadMediaByURLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.UploadMediaByURLResponse().from_map(
            await self.do_rpcrequest_async('UploadMediaByURL', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_media_by_url(
        self,
        request: vod_20170321_models.UploadMediaByURLRequest,
    ) -> vod_20170321_models.UploadMediaByURLResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_media_by_urlwith_options(request, runtime)

    async def upload_media_by_url_async(
        self,
        request: vod_20170321_models.UploadMediaByURLRequest,
    ) -> vod_20170321_models.UploadMediaByURLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_media_by_urlwith_options_async(request, runtime)

    def verify_vod_domain_owner_with_options(
        self,
        request: vod_20170321_models.VerifyVodDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.VerifyVodDomainOwnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.VerifyVodDomainOwnerResponse().from_map(
            self.do_rpcrequest('VerifyVodDomainOwner', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_vod_domain_owner_with_options_async(
        self,
        request: vod_20170321_models.VerifyVodDomainOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vod_20170321_models.VerifyVodDomainOwnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vod_20170321_models.VerifyVodDomainOwnerResponse().from_map(
            await self.do_rpcrequest_async('VerifyVodDomainOwner', '2017-03-21', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_vod_domain_owner(
        self,
        request: vod_20170321_models.VerifyVodDomainOwnerRequest,
    ) -> vod_20170321_models.VerifyVodDomainOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_vod_domain_owner_with_options(request, runtime)

    async def verify_vod_domain_owner_async(
        self,
        request: vod_20170321_models.VerifyVodDomainOwnerRequest,
    ) -> vod_20170321_models.VerifyVodDomainOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_vod_domain_owner_with_options_async(request, runtime)
