# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_green20170823 import models as green_20170823_models
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
            'ap-northeast-1': 'green.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'green.ap-southeast-1.aliyuncs.com',
            'cn-chengdu': 'green.aliyuncs.com',
            'cn-hongkong': 'green.aliyuncs.com',
            'cn-huhehaote': 'green.aliyuncs.com',
            'cn-qingdao': 'green.aliyuncs.com',
            'cn-zhangjiakou': 'green.aliyuncs.com',
            'eu-central-1': 'green.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'green.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'green.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'green.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'green.aliyuncs.com',
            'cn-shenzhen-finance-1': 'green.aliyuncs.com',
            'cn-shanghai-finance-1': 'green.aliyuncs.com',
            'cn-north-2-gov-1': 'green.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('green', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def creat_custom_ocr_template_with_options(
        self,
        request: green_20170823_models.CreatCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreatCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreatCustomOcrTemplateResponse(),
            self.do_rpcrequest('CreatCustomOcrTemplate', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def creat_custom_ocr_template_with_options_async(
        self,
        request: green_20170823_models.CreatCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreatCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreatCustomOcrTemplateResponse(),
            await self.do_rpcrequest_async('CreatCustomOcrTemplate', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def creat_custom_ocr_template(
        self,
        request: green_20170823_models.CreatCustomOcrTemplateRequest,
    ) -> green_20170823_models.CreatCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.creat_custom_ocr_template_with_options(request, runtime)

    async def creat_custom_ocr_template_async(
        self,
        request: green_20170823_models.CreatCustomOcrTemplateRequest,
    ) -> green_20170823_models.CreatCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.creat_custom_ocr_template_with_options_async(request, runtime)

    def create_biz_type_with_options(
        self,
        request: green_20170823_models.CreateBizTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateBizTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreateBizTypeResponse(),
            self.do_rpcrequest('CreateBizType', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_biz_type_with_options_async(
        self,
        request: green_20170823_models.CreateBizTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateBizTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreateBizTypeResponse(),
            await self.do_rpcrequest_async('CreateBizType', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_biz_type(
        self,
        request: green_20170823_models.CreateBizTypeRequest,
    ) -> green_20170823_models.CreateBizTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_biz_type_with_options(request, runtime)

    async def create_biz_type_async(
        self,
        request: green_20170823_models.CreateBizTypeRequest,
    ) -> green_20170823_models.CreateBizTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_biz_type_with_options_async(request, runtime)

    def create_cdi_bag_with_options(
        self,
        request: green_20170823_models.CreateCdiBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateCdiBagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreateCdiBagResponse(),
            self.do_rpcrequest('CreateCdiBag', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cdi_bag_with_options_async(
        self,
        request: green_20170823_models.CreateCdiBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateCdiBagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreateCdiBagResponse(),
            await self.do_rpcrequest_async('CreateCdiBag', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cdi_bag(
        self,
        request: green_20170823_models.CreateCdiBagRequest,
    ) -> green_20170823_models.CreateCdiBagResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cdi_bag_with_options(request, runtime)

    async def create_cdi_bag_async(
        self,
        request: green_20170823_models.CreateCdiBagRequest,
    ) -> green_20170823_models.CreateCdiBagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cdi_bag_with_options_async(request, runtime)

    def create_cdi_base_bag_with_options(
        self,
        request: green_20170823_models.CreateCdiBaseBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateCdiBaseBagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreateCdiBaseBagResponse(),
            self.do_rpcrequest('CreateCdiBaseBag', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cdi_base_bag_with_options_async(
        self,
        request: green_20170823_models.CreateCdiBaseBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateCdiBaseBagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreateCdiBaseBagResponse(),
            await self.do_rpcrequest_async('CreateCdiBaseBag', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cdi_base_bag(
        self,
        request: green_20170823_models.CreateCdiBaseBagRequest,
    ) -> green_20170823_models.CreateCdiBaseBagResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cdi_base_bag_with_options(request, runtime)

    async def create_cdi_base_bag_async(
        self,
        request: green_20170823_models.CreateCdiBaseBagRequest,
    ) -> green_20170823_models.CreateCdiBaseBagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cdi_base_bag_with_options_async(request, runtime)

    def create_image_lib_with_options(
        self,
        request: green_20170823_models.CreateImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateImageLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreateImageLibResponse(),
            self.do_rpcrequest('CreateImageLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_image_lib_with_options_async(
        self,
        request: green_20170823_models.CreateImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateImageLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreateImageLibResponse(),
            await self.do_rpcrequest_async('CreateImageLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_image_lib(
        self,
        request: green_20170823_models.CreateImageLibRequest,
    ) -> green_20170823_models.CreateImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_image_lib_with_options(request, runtime)

    async def create_image_lib_async(
        self,
        request: green_20170823_models.CreateImageLibRequest,
    ) -> green_20170823_models.CreateImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_lib_with_options_async(request, runtime)

    def create_keyword_with_options(
        self,
        request: green_20170823_models.CreateKeywordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateKeywordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreateKeywordResponse(),
            self.do_rpcrequest('CreateKeyword', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_keyword_with_options_async(
        self,
        request: green_20170823_models.CreateKeywordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateKeywordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreateKeywordResponse(),
            await self.do_rpcrequest_async('CreateKeyword', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_keyword(
        self,
        request: green_20170823_models.CreateKeywordRequest,
    ) -> green_20170823_models.CreateKeywordResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_keyword_with_options(request, runtime)

    async def create_keyword_async(
        self,
        request: green_20170823_models.CreateKeywordRequest,
    ) -> green_20170823_models.CreateKeywordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_keyword_with_options_async(request, runtime)

    def create_keyword_lib_with_options(
        self,
        request: green_20170823_models.CreateKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateKeywordLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreateKeywordLibResponse(),
            self.do_rpcrequest('CreateKeywordLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_keyword_lib_with_options_async(
        self,
        request: green_20170823_models.CreateKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateKeywordLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreateKeywordLibResponse(),
            await self.do_rpcrequest_async('CreateKeywordLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_keyword_lib(
        self,
        request: green_20170823_models.CreateKeywordLibRequest,
    ) -> green_20170823_models.CreateKeywordLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_keyword_lib_with_options(request, runtime)

    async def create_keyword_lib_async(
        self,
        request: green_20170823_models.CreateKeywordLibRequest,
    ) -> green_20170823_models.CreateKeywordLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_keyword_lib_with_options_async(request, runtime)

    def create_website_index_page_baseline_with_options(
        self,
        request: green_20170823_models.CreateWebsiteIndexPageBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateWebsiteIndexPageBaselineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreateWebsiteIndexPageBaselineResponse(),
            self.do_rpcrequest('CreateWebsiteIndexPageBaseline', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_website_index_page_baseline_with_options_async(
        self,
        request: green_20170823_models.CreateWebsiteIndexPageBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateWebsiteIndexPageBaselineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreateWebsiteIndexPageBaselineResponse(),
            await self.do_rpcrequest_async('CreateWebsiteIndexPageBaseline', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_website_index_page_baseline(
        self,
        request: green_20170823_models.CreateWebsiteIndexPageBaselineRequest,
    ) -> green_20170823_models.CreateWebsiteIndexPageBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_website_index_page_baseline_with_options(request, runtime)

    async def create_website_index_page_baseline_async(
        self,
        request: green_20170823_models.CreateWebsiteIndexPageBaselineRequest,
    ) -> green_20170823_models.CreateWebsiteIndexPageBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_website_index_page_baseline_with_options_async(request, runtime)

    def create_web_site_instance_with_options(
        self,
        request: green_20170823_models.CreateWebSiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateWebSiteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreateWebSiteInstanceResponse(),
            self.do_rpcrequest('CreateWebSiteInstance', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_web_site_instance_with_options_async(
        self,
        request: green_20170823_models.CreateWebSiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.CreateWebSiteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.CreateWebSiteInstanceResponse(),
            await self.do_rpcrequest_async('CreateWebSiteInstance', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_web_site_instance(
        self,
        request: green_20170823_models.CreateWebSiteInstanceRequest,
    ) -> green_20170823_models.CreateWebSiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_web_site_instance_with_options(request, runtime)

    async def create_web_site_instance_async(
        self,
        request: green_20170823_models.CreateWebSiteInstanceRequest,
    ) -> green_20170823_models.CreateWebSiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_web_site_instance_with_options_async(request, runtime)

    def delete_biz_type_with_options(
        self,
        request: green_20170823_models.DeleteBizTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteBizTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteBizTypeResponse(),
            self.do_rpcrequest('DeleteBizType', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_biz_type_with_options_async(
        self,
        request: green_20170823_models.DeleteBizTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteBizTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteBizTypeResponse(),
            await self.do_rpcrequest_async('DeleteBizType', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_biz_type(
        self,
        request: green_20170823_models.DeleteBizTypeRequest,
    ) -> green_20170823_models.DeleteBizTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_biz_type_with_options(request, runtime)

    async def delete_biz_type_async(
        self,
        request: green_20170823_models.DeleteBizTypeRequest,
    ) -> green_20170823_models.DeleteBizTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_biz_type_with_options_async(request, runtime)

    def delete_custom_ocr_template_with_options(
        self,
        request: green_20170823_models.DeleteCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteCustomOcrTemplateResponse(),
            self.do_rpcrequest('DeleteCustomOcrTemplate', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_custom_ocr_template_with_options_async(
        self,
        request: green_20170823_models.DeleteCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteCustomOcrTemplateResponse(),
            await self.do_rpcrequest_async('DeleteCustomOcrTemplate', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_custom_ocr_template(
        self,
        request: green_20170823_models.DeleteCustomOcrTemplateRequest,
    ) -> green_20170823_models.DeleteCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_ocr_template_with_options(request, runtime)

    async def delete_custom_ocr_template_async(
        self,
        request: green_20170823_models.DeleteCustomOcrTemplateRequest,
    ) -> green_20170823_models.DeleteCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_ocr_template_with_options_async(request, runtime)

    def delete_image_from_lib_with_options(
        self,
        request: green_20170823_models.DeleteImageFromLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteImageFromLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteImageFromLibResponse(),
            self.do_rpcrequest('DeleteImageFromLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_image_from_lib_with_options_async(
        self,
        request: green_20170823_models.DeleteImageFromLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteImageFromLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteImageFromLibResponse(),
            await self.do_rpcrequest_async('DeleteImageFromLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_image_from_lib(
        self,
        request: green_20170823_models.DeleteImageFromLibRequest,
    ) -> green_20170823_models.DeleteImageFromLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_from_lib_with_options(request, runtime)

    async def delete_image_from_lib_async(
        self,
        request: green_20170823_models.DeleteImageFromLibRequest,
    ) -> green_20170823_models.DeleteImageFromLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_from_lib_with_options_async(request, runtime)

    def delete_image_lib_with_options(
        self,
        request: green_20170823_models.DeleteImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteImageLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteImageLibResponse(),
            self.do_rpcrequest('DeleteImageLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_image_lib_with_options_async(
        self,
        request: green_20170823_models.DeleteImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteImageLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteImageLibResponse(),
            await self.do_rpcrequest_async('DeleteImageLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_image_lib(
        self,
        request: green_20170823_models.DeleteImageLibRequest,
    ) -> green_20170823_models.DeleteImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_lib_with_options(request, runtime)

    async def delete_image_lib_async(
        self,
        request: green_20170823_models.DeleteImageLibRequest,
    ) -> green_20170823_models.DeleteImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_lib_with_options_async(request, runtime)

    def delete_keyword_with_options(
        self,
        request: green_20170823_models.DeleteKeywordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteKeywordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteKeywordResponse(),
            self.do_rpcrequest('DeleteKeyword', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_keyword_with_options_async(
        self,
        request: green_20170823_models.DeleteKeywordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteKeywordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteKeywordResponse(),
            await self.do_rpcrequest_async('DeleteKeyword', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_keyword(
        self,
        request: green_20170823_models.DeleteKeywordRequest,
    ) -> green_20170823_models.DeleteKeywordResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_keyword_with_options(request, runtime)

    async def delete_keyword_async(
        self,
        request: green_20170823_models.DeleteKeywordRequest,
    ) -> green_20170823_models.DeleteKeywordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_keyword_with_options_async(request, runtime)

    def delete_keyword_lib_with_options(
        self,
        request: green_20170823_models.DeleteKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteKeywordLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteKeywordLibResponse(),
            self.do_rpcrequest('DeleteKeywordLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_keyword_lib_with_options_async(
        self,
        request: green_20170823_models.DeleteKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteKeywordLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteKeywordLibResponse(),
            await self.do_rpcrequest_async('DeleteKeywordLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_keyword_lib(
        self,
        request: green_20170823_models.DeleteKeywordLibRequest,
    ) -> green_20170823_models.DeleteKeywordLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_keyword_lib_with_options(request, runtime)

    async def delete_keyword_lib_async(
        self,
        request: green_20170823_models.DeleteKeywordLibRequest,
    ) -> green_20170823_models.DeleteKeywordLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_keyword_lib_with_options_async(request, runtime)

    def delete_notification_contacts_with_options(
        self,
        request: green_20170823_models.DeleteNotificationContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteNotificationContactsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteNotificationContactsResponse(),
            self.do_rpcrequest('DeleteNotificationContacts', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_notification_contacts_with_options_async(
        self,
        request: green_20170823_models.DeleteNotificationContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DeleteNotificationContactsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DeleteNotificationContactsResponse(),
            await self.do_rpcrequest_async('DeleteNotificationContacts', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_notification_contacts(
        self,
        request: green_20170823_models.DeleteNotificationContactsRequest,
    ) -> green_20170823_models.DeleteNotificationContactsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_notification_contacts_with_options(request, runtime)

    async def delete_notification_contacts_async(
        self,
        request: green_20170823_models.DeleteNotificationContactsRequest,
    ) -> green_20170823_models.DeleteNotificationContactsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_notification_contacts_with_options_async(request, runtime)

    def describe_app_info_with_options(
        self,
        request: green_20170823_models.DescribeAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAppInfoResponse(),
            self.do_rpcrequest('DescribeAppInfo', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_app_info_with_options_async(
        self,
        request: green_20170823_models.DescribeAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAppInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAppInfoResponse(),
            await self.do_rpcrequest_async('DescribeAppInfo', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_app_info(
        self,
        request: green_20170823_models.DescribeAppInfoRequest,
    ) -> green_20170823_models.DescribeAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_info_with_options(request, runtime)

    async def describe_app_info_async(
        self,
        request: green_20170823_models.DescribeAppInfoRequest,
    ) -> green_20170823_models.DescribeAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_info_with_options_async(request, runtime)

    def describe_audit_callback_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditCallbackResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditCallbackResponse(),
            self.do_rpcrequest('DescribeAuditCallback', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_audit_callback_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditCallbackResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditCallbackResponse(),
            await self.do_rpcrequest_async('DescribeAuditCallback', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_callback(self) -> green_20170823_models.DescribeAuditCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_callback_with_options(runtime)

    async def describe_audit_callback_async(self) -> green_20170823_models.DescribeAuditCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_callback_with_options_async(runtime)

    def describe_audit_content_with_options(
        self,
        request: green_20170823_models.DescribeAuditContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditContentResponse(),
            self.do_rpcrequest('DescribeAuditContent', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_audit_content_with_options_async(
        self,
        request: green_20170823_models.DescribeAuditContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditContentResponse(),
            await self.do_rpcrequest_async('DescribeAuditContent', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_content(
        self,
        request: green_20170823_models.DescribeAuditContentRequest,
    ) -> green_20170823_models.DescribeAuditContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_content_with_options(request, runtime)

    async def describe_audit_content_async(
        self,
        request: green_20170823_models.DescribeAuditContentRequest,
    ) -> green_20170823_models.DescribeAuditContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_content_with_options_async(request, runtime)

    def describe_audit_content_item_with_options(
        self,
        request: green_20170823_models.DescribeAuditContentItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditContentItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditContentItemResponse(),
            self.do_rpcrequest('DescribeAuditContentItem', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_audit_content_item_with_options_async(
        self,
        request: green_20170823_models.DescribeAuditContentItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditContentItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditContentItemResponse(),
            await self.do_rpcrequest_async('DescribeAuditContentItem', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_content_item(
        self,
        request: green_20170823_models.DescribeAuditContentItemRequest,
    ) -> green_20170823_models.DescribeAuditContentItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_content_item_with_options(request, runtime)

    async def describe_audit_content_item_async(
        self,
        request: green_20170823_models.DescribeAuditContentItemRequest,
    ) -> green_20170823_models.DescribeAuditContentItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_content_item_with_options_async(request, runtime)

    def describe_audit_range_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditRangeResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditRangeResponse(),
            self.do_rpcrequest('DescribeAuditRange', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_audit_range_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditRangeResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditRangeResponse(),
            await self.do_rpcrequest_async('DescribeAuditRange', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_range(self) -> green_20170823_models.DescribeAuditRangeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_range_with_options(runtime)

    async def describe_audit_range_async(self) -> green_20170823_models.DescribeAuditRangeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_range_with_options_async(runtime)

    def describe_audit_setting_with_options(
        self,
        request: green_20170823_models.DescribeAuditSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditSettingResponse(),
            self.do_rpcrequest('DescribeAuditSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_audit_setting_with_options_async(
        self,
        request: green_20170823_models.DescribeAuditSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeAuditSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeAuditSettingResponse(),
            await self.do_rpcrequest_async('DescribeAuditSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_audit_setting(
        self,
        request: green_20170823_models.DescribeAuditSettingRequest,
    ) -> green_20170823_models.DescribeAuditSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_setting_with_options(request, runtime)

    async def describe_audit_setting_async(
        self,
        request: green_20170823_models.DescribeAuditSettingRequest,
    ) -> green_20170823_models.DescribeAuditSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_setting_with_options_async(request, runtime)

    def describe_biz_type_image_lib_with_options(
        self,
        request: green_20170823_models.DescribeBizTypeImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeBizTypeImageLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypeImageLibResponse(),
            self.do_rpcrequest('DescribeBizTypeImageLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_biz_type_image_lib_with_options_async(
        self,
        request: green_20170823_models.DescribeBizTypeImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeBizTypeImageLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypeImageLibResponse(),
            await self.do_rpcrequest_async('DescribeBizTypeImageLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_biz_type_image_lib(
        self,
        request: green_20170823_models.DescribeBizTypeImageLibRequest,
    ) -> green_20170823_models.DescribeBizTypeImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_biz_type_image_lib_with_options(request, runtime)

    async def describe_biz_type_image_lib_async(
        self,
        request: green_20170823_models.DescribeBizTypeImageLibRequest,
    ) -> green_20170823_models.DescribeBizTypeImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_biz_type_image_lib_with_options_async(request, runtime)

    def describe_biz_types_with_options(
        self,
        request: green_20170823_models.DescribeBizTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeBizTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypesResponse(),
            self.do_rpcrequest('DescribeBizTypes', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_biz_types_with_options_async(
        self,
        request: green_20170823_models.DescribeBizTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeBizTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypesResponse(),
            await self.do_rpcrequest_async('DescribeBizTypes', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_biz_types(
        self,
        request: green_20170823_models.DescribeBizTypesRequest,
    ) -> green_20170823_models.DescribeBizTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_biz_types_with_options(request, runtime)

    async def describe_biz_types_async(
        self,
        request: green_20170823_models.DescribeBizTypesRequest,
    ) -> green_20170823_models.DescribeBizTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_biz_types_with_options_async(request, runtime)

    def describe_biz_type_setting_with_options(
        self,
        request: green_20170823_models.DescribeBizTypeSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeBizTypeSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypeSettingResponse(),
            self.do_rpcrequest('DescribeBizTypeSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_biz_type_setting_with_options_async(
        self,
        request: green_20170823_models.DescribeBizTypeSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeBizTypeSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypeSettingResponse(),
            await self.do_rpcrequest_async('DescribeBizTypeSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_biz_type_setting(
        self,
        request: green_20170823_models.DescribeBizTypeSettingRequest,
    ) -> green_20170823_models.DescribeBizTypeSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_biz_type_setting_with_options(request, runtime)

    async def describe_biz_type_setting_async(
        self,
        request: green_20170823_models.DescribeBizTypeSettingRequest,
    ) -> green_20170823_models.DescribeBizTypeSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_biz_type_setting_with_options_async(request, runtime)

    def describe_biz_type_text_lib_with_options(
        self,
        request: green_20170823_models.DescribeBizTypeTextLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeBizTypeTextLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypeTextLibResponse(),
            self.do_rpcrequest('DescribeBizTypeTextLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_biz_type_text_lib_with_options_async(
        self,
        request: green_20170823_models.DescribeBizTypeTextLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeBizTypeTextLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeBizTypeTextLibResponse(),
            await self.do_rpcrequest_async('DescribeBizTypeTextLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_biz_type_text_lib(
        self,
        request: green_20170823_models.DescribeBizTypeTextLibRequest,
    ) -> green_20170823_models.DescribeBizTypeTextLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_biz_type_text_lib_with_options(request, runtime)

    async def describe_biz_type_text_lib_async(
        self,
        request: green_20170823_models.DescribeBizTypeTextLibRequest,
    ) -> green_20170823_models.DescribeBizTypeTextLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_biz_type_text_lib_with_options_async(request, runtime)

    def describe_cloud_monitor_services_with_options(
        self,
        request: green_20170823_models.DescribeCloudMonitorServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeCloudMonitorServicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeCloudMonitorServicesResponse(),
            self.do_rpcrequest('DescribeCloudMonitorServices', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cloud_monitor_services_with_options_async(
        self,
        request: green_20170823_models.DescribeCloudMonitorServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeCloudMonitorServicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeCloudMonitorServicesResponse(),
            await self.do_rpcrequest_async('DescribeCloudMonitorServices', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cloud_monitor_services(
        self,
        request: green_20170823_models.DescribeCloudMonitorServicesRequest,
    ) -> green_20170823_models.DescribeCloudMonitorServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_monitor_services_with_options(request, runtime)

    async def describe_cloud_monitor_services_async(
        self,
        request: green_20170823_models.DescribeCloudMonitorServicesRequest,
    ) -> green_20170823_models.DescribeCloudMonitorServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_monitor_services_with_options_async(request, runtime)

    def describe_custom_ocr_template_with_options(
        self,
        request: green_20170823_models.DescribeCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeCustomOcrTemplateResponse(),
            self.do_rpcrequest('DescribeCustomOcrTemplate', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_custom_ocr_template_with_options_async(
        self,
        request: green_20170823_models.DescribeCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeCustomOcrTemplateResponse(),
            await self.do_rpcrequest_async('DescribeCustomOcrTemplate', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_custom_ocr_template(
        self,
        request: green_20170823_models.DescribeCustomOcrTemplateRequest,
    ) -> green_20170823_models.DescribeCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_ocr_template_with_options(request, runtime)

    async def describe_custom_ocr_template_async(
        self,
        request: green_20170823_models.DescribeCustomOcrTemplateRequest,
    ) -> green_20170823_models.DescribeCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_ocr_template_with_options_async(request, runtime)

    def describe_image_from_lib_with_options(
        self,
        request: green_20170823_models.DescribeImageFromLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeImageFromLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeImageFromLibResponse(),
            self.do_rpcrequest('DescribeImageFromLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_image_from_lib_with_options_async(
        self,
        request: green_20170823_models.DescribeImageFromLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeImageFromLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeImageFromLibResponse(),
            await self.do_rpcrequest_async('DescribeImageFromLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_from_lib(
        self,
        request: green_20170823_models.DescribeImageFromLibRequest,
    ) -> green_20170823_models.DescribeImageFromLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_from_lib_with_options(request, runtime)

    async def describe_image_from_lib_async(
        self,
        request: green_20170823_models.DescribeImageFromLibRequest,
    ) -> green_20170823_models.DescribeImageFromLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_from_lib_with_options_async(request, runtime)

    def describe_image_lib_with_options(
        self,
        request: green_20170823_models.DescribeImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeImageLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeImageLibResponse(),
            self.do_rpcrequest('DescribeImageLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_image_lib_with_options_async(
        self,
        request: green_20170823_models.DescribeImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeImageLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeImageLibResponse(),
            await self.do_rpcrequest_async('DescribeImageLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_lib(
        self,
        request: green_20170823_models.DescribeImageLibRequest,
    ) -> green_20170823_models.DescribeImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_lib_with_options(request, runtime)

    async def describe_image_lib_async(
        self,
        request: green_20170823_models.DescribeImageLibRequest,
    ) -> green_20170823_models.DescribeImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_lib_with_options_async(request, runtime)

    def describe_image_upload_info_with_options(
        self,
        request: green_20170823_models.DescribeImageUploadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeImageUploadInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeImageUploadInfoResponse(),
            self.do_rpcrequest('DescribeImageUploadInfo', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_image_upload_info_with_options_async(
        self,
        request: green_20170823_models.DescribeImageUploadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeImageUploadInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeImageUploadInfoResponse(),
            await self.do_rpcrequest_async('DescribeImageUploadInfo', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_upload_info(
        self,
        request: green_20170823_models.DescribeImageUploadInfoRequest,
    ) -> green_20170823_models.DescribeImageUploadInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_upload_info_with_options(request, runtime)

    async def describe_image_upload_info_async(
        self,
        request: green_20170823_models.DescribeImageUploadInfoRequest,
    ) -> green_20170823_models.DescribeImageUploadInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_upload_info_with_options_async(request, runtime)

    def describe_keyword_with_options(
        self,
        request: green_20170823_models.DescribeKeywordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeKeywordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeKeywordResponse(),
            self.do_rpcrequest('DescribeKeyword', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_keyword_with_options_async(
        self,
        request: green_20170823_models.DescribeKeywordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeKeywordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeKeywordResponse(),
            await self.do_rpcrequest_async('DescribeKeyword', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_keyword(
        self,
        request: green_20170823_models.DescribeKeywordRequest,
    ) -> green_20170823_models.DescribeKeywordResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_keyword_with_options(request, runtime)

    async def describe_keyword_async(
        self,
        request: green_20170823_models.DescribeKeywordRequest,
    ) -> green_20170823_models.DescribeKeywordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_keyword_with_options_async(request, runtime)

    def describe_keyword_lib_with_options(
        self,
        request: green_20170823_models.DescribeKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeKeywordLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeKeywordLibResponse(),
            self.do_rpcrequest('DescribeKeywordLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_keyword_lib_with_options_async(
        self,
        request: green_20170823_models.DescribeKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeKeywordLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeKeywordLibResponse(),
            await self.do_rpcrequest_async('DescribeKeywordLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_keyword_lib(
        self,
        request: green_20170823_models.DescribeKeywordLibRequest,
    ) -> green_20170823_models.DescribeKeywordLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_keyword_lib_with_options(request, runtime)

    async def describe_keyword_lib_async(
        self,
        request: green_20170823_models.DescribeKeywordLibRequest,
    ) -> green_20170823_models.DescribeKeywordLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_keyword_lib_with_options_async(request, runtime)

    def describe_notification_setting_with_options(
        self,
        request: green_20170823_models.DescribeNotificationSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeNotificationSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeNotificationSettingResponse(),
            self.do_rpcrequest('DescribeNotificationSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_notification_setting_with_options_async(
        self,
        request: green_20170823_models.DescribeNotificationSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeNotificationSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeNotificationSettingResponse(),
            await self.do_rpcrequest_async('DescribeNotificationSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_notification_setting(
        self,
        request: green_20170823_models.DescribeNotificationSettingRequest,
    ) -> green_20170823_models.DescribeNotificationSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_notification_setting_with_options(request, runtime)

    async def describe_notification_setting_async(
        self,
        request: green_20170823_models.DescribeNotificationSettingRequest,
    ) -> green_20170823_models.DescribeNotificationSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_notification_setting_with_options_async(request, runtime)

    def describe_open_api_rcp_stats_with_options(
        self,
        request: green_20170823_models.DescribeOpenApiRcpStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOpenApiRcpStatsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOpenApiRcpStatsResponse(),
            self.do_rpcrequest('DescribeOpenApiRcpStats', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_open_api_rcp_stats_with_options_async(
        self,
        request: green_20170823_models.DescribeOpenApiRcpStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOpenApiRcpStatsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOpenApiRcpStatsResponse(),
            await self.do_rpcrequest_async('DescribeOpenApiRcpStats', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_open_api_rcp_stats(
        self,
        request: green_20170823_models.DescribeOpenApiRcpStatsRequest,
    ) -> green_20170823_models.DescribeOpenApiRcpStatsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_open_api_rcp_stats_with_options(request, runtime)

    async def describe_open_api_rcp_stats_async(
        self,
        request: green_20170823_models.DescribeOpenApiRcpStatsRequest,
    ) -> green_20170823_models.DescribeOpenApiRcpStatsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_open_api_rcp_stats_with_options_async(request, runtime)

    def describe_open_api_usage_with_options(
        self,
        request: green_20170823_models.DescribeOpenApiUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOpenApiUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOpenApiUsageResponse(),
            self.do_rpcrequest('DescribeOpenApiUsage', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_open_api_usage_with_options_async(
        self,
        request: green_20170823_models.DescribeOpenApiUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOpenApiUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOpenApiUsageResponse(),
            await self.do_rpcrequest_async('DescribeOpenApiUsage', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_open_api_usage(
        self,
        request: green_20170823_models.DescribeOpenApiUsageRequest,
    ) -> green_20170823_models.DescribeOpenApiUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_open_api_usage_with_options(request, runtime)

    async def describe_open_api_usage_async(
        self,
        request: green_20170823_models.DescribeOpenApiUsageRequest,
    ) -> green_20170823_models.DescribeOpenApiUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_open_api_usage_with_options_async(request, runtime)

    def describe_oss_callback_setting_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssCallbackSettingResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            green_20170823_models.DescribeOssCallbackSettingResponse(),
            self.do_rpcrequest('DescribeOssCallbackSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_oss_callback_setting_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssCallbackSettingResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            green_20170823_models.DescribeOssCallbackSettingResponse(),
            await self.do_rpcrequest_async('DescribeOssCallbackSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_oss_callback_setting(self) -> green_20170823_models.DescribeOssCallbackSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_callback_setting_with_options(runtime)

    async def describe_oss_callback_setting_async(self) -> green_20170823_models.DescribeOssCallbackSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_callback_setting_with_options_async(runtime)

    def describe_oss_increment_check_setting_with_options(
        self,
        request: green_20170823_models.DescribeOssIncrementCheckSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssIncrementCheckSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssIncrementCheckSettingResponse(),
            self.do_rpcrequest('DescribeOssIncrementCheckSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_oss_increment_check_setting_with_options_async(
        self,
        request: green_20170823_models.DescribeOssIncrementCheckSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssIncrementCheckSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssIncrementCheckSettingResponse(),
            await self.do_rpcrequest_async('DescribeOssIncrementCheckSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_oss_increment_check_setting(
        self,
        request: green_20170823_models.DescribeOssIncrementCheckSettingRequest,
    ) -> green_20170823_models.DescribeOssIncrementCheckSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_increment_check_setting_with_options(request, runtime)

    async def describe_oss_increment_check_setting_async(
        self,
        request: green_20170823_models.DescribeOssIncrementCheckSettingRequest,
    ) -> green_20170823_models.DescribeOssIncrementCheckSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_increment_check_setting_with_options_async(request, runtime)

    def describe_oss_increment_overview_with_options(
        self,
        request: green_20170823_models.DescribeOssIncrementOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssIncrementOverviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssIncrementOverviewResponse(),
            self.do_rpcrequest('DescribeOssIncrementOverview', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_oss_increment_overview_with_options_async(
        self,
        request: green_20170823_models.DescribeOssIncrementOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssIncrementOverviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssIncrementOverviewResponse(),
            await self.do_rpcrequest_async('DescribeOssIncrementOverview', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_oss_increment_overview(
        self,
        request: green_20170823_models.DescribeOssIncrementOverviewRequest,
    ) -> green_20170823_models.DescribeOssIncrementOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_increment_overview_with_options(request, runtime)

    async def describe_oss_increment_overview_async(
        self,
        request: green_20170823_models.DescribeOssIncrementOverviewRequest,
    ) -> green_20170823_models.DescribeOssIncrementOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_increment_overview_with_options_async(request, runtime)

    def describe_oss_increment_stats_with_options(
        self,
        request: green_20170823_models.DescribeOssIncrementStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssIncrementStatsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssIncrementStatsResponse(),
            self.do_rpcrequest('DescribeOssIncrementStats', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_oss_increment_stats_with_options_async(
        self,
        request: green_20170823_models.DescribeOssIncrementStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssIncrementStatsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssIncrementStatsResponse(),
            await self.do_rpcrequest_async('DescribeOssIncrementStats', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_oss_increment_stats(
        self,
        request: green_20170823_models.DescribeOssIncrementStatsRequest,
    ) -> green_20170823_models.DescribeOssIncrementStatsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_increment_stats_with_options(request, runtime)

    async def describe_oss_increment_stats_async(
        self,
        request: green_20170823_models.DescribeOssIncrementStatsRequest,
    ) -> green_20170823_models.DescribeOssIncrementStatsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_increment_stats_with_options_async(request, runtime)

    def describe_oss_result_items_with_options(
        self,
        request: green_20170823_models.DescribeOssResultItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssResultItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssResultItemsResponse(),
            self.do_rpcrequest('DescribeOssResultItems', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_oss_result_items_with_options_async(
        self,
        request: green_20170823_models.DescribeOssResultItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssResultItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssResultItemsResponse(),
            await self.do_rpcrequest_async('DescribeOssResultItems', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_oss_result_items(
        self,
        request: green_20170823_models.DescribeOssResultItemsRequest,
    ) -> green_20170823_models.DescribeOssResultItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_result_items_with_options(request, runtime)

    async def describe_oss_result_items_async(
        self,
        request: green_20170823_models.DescribeOssResultItemsRequest,
    ) -> green_20170823_models.DescribeOssResultItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_result_items_with_options_async(request, runtime)

    def describe_oss_stock_status_with_options(
        self,
        request: green_20170823_models.DescribeOssStockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssStockStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssStockStatusResponse(),
            self.do_rpcrequest('DescribeOssStockStatus', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_oss_stock_status_with_options_async(
        self,
        request: green_20170823_models.DescribeOssStockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeOssStockStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeOssStockStatusResponse(),
            await self.do_rpcrequest_async('DescribeOssStockStatus', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_oss_stock_status(
        self,
        request: green_20170823_models.DescribeOssStockStatusRequest,
    ) -> green_20170823_models.DescribeOssStockStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_stock_status_with_options(request, runtime)

    async def describe_oss_stock_status_async(
        self,
        request: green_20170823_models.DescribeOssStockStatusRequest,
    ) -> green_20170823_models.DescribeOssStockStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_stock_status_with_options_async(request, runtime)

    def describe_sdk_url_with_options(
        self,
        request: green_20170823_models.DescribeSdkUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeSdkUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeSdkUrlResponse(),
            self.do_rpcrequest('DescribeSdkUrl', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sdk_url_with_options_async(
        self,
        request: green_20170823_models.DescribeSdkUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeSdkUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeSdkUrlResponse(),
            await self.do_rpcrequest_async('DescribeSdkUrl', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sdk_url(
        self,
        request: green_20170823_models.DescribeSdkUrlRequest,
    ) -> green_20170823_models.DescribeSdkUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sdk_url_with_options(request, runtime)

    async def describe_sdk_url_async(
        self,
        request: green_20170823_models.DescribeSdkUrlRequest,
    ) -> green_20170823_models.DescribeSdkUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sdk_url_with_options_async(request, runtime)

    def describe_update_package_result_with_options(
        self,
        request: green_20170823_models.DescribeUpdatePackageResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUpdatePackageResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUpdatePackageResultResponse(),
            self.do_rpcrequest('DescribeUpdatePackageResult', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_update_package_result_with_options_async(
        self,
        request: green_20170823_models.DescribeUpdatePackageResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUpdatePackageResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUpdatePackageResultResponse(),
            await self.do_rpcrequest_async('DescribeUpdatePackageResult', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_update_package_result(
        self,
        request: green_20170823_models.DescribeUpdatePackageResultRequest,
    ) -> green_20170823_models.DescribeUpdatePackageResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_update_package_result_with_options(request, runtime)

    async def describe_update_package_result_async(
        self,
        request: green_20170823_models.DescribeUpdatePackageResultRequest,
    ) -> green_20170823_models.DescribeUpdatePackageResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_update_package_result_with_options_async(request, runtime)

    def describe_upload_info_with_options(
        self,
        request: green_20170823_models.DescribeUploadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUploadInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUploadInfoResponse(),
            self.do_rpcrequest('DescribeUploadInfo', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_upload_info_with_options_async(
        self,
        request: green_20170823_models.DescribeUploadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUploadInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUploadInfoResponse(),
            await self.do_rpcrequest_async('DescribeUploadInfo', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_upload_info(
        self,
        request: green_20170823_models.DescribeUploadInfoRequest,
    ) -> green_20170823_models.DescribeUploadInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_upload_info_with_options(request, runtime)

    async def describe_upload_info_async(
        self,
        request: green_20170823_models.DescribeUploadInfoRequest,
    ) -> green_20170823_models.DescribeUploadInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_upload_info_with_options_async(request, runtime)

    def describe_usage_bill_with_options(
        self,
        request: green_20170823_models.DescribeUsageBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUsageBillResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUsageBillResponse(),
            self.do_rpcrequest('DescribeUsageBill', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_usage_bill_with_options_async(
        self,
        request: green_20170823_models.DescribeUsageBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUsageBillResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUsageBillResponse(),
            await self.do_rpcrequest_async('DescribeUsageBill', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_usage_bill(
        self,
        request: green_20170823_models.DescribeUsageBillRequest,
    ) -> green_20170823_models.DescribeUsageBillResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_usage_bill_with_options(request, runtime)

    async def describe_usage_bill_async(
        self,
        request: green_20170823_models.DescribeUsageBillRequest,
    ) -> green_20170823_models.DescribeUsageBillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_usage_bill_with_options_async(request, runtime)

    def describe_user_biz_types_with_options(
        self,
        request: green_20170823_models.DescribeUserBizTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUserBizTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUserBizTypesResponse(),
            self.do_rpcrequest('DescribeUserBizTypes', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_biz_types_with_options_async(
        self,
        request: green_20170823_models.DescribeUserBizTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUserBizTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUserBizTypesResponse(),
            await self.do_rpcrequest_async('DescribeUserBizTypes', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_biz_types(
        self,
        request: green_20170823_models.DescribeUserBizTypesRequest,
    ) -> green_20170823_models.DescribeUserBizTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_biz_types_with_options(request, runtime)

    async def describe_user_biz_types_async(
        self,
        request: green_20170823_models.DescribeUserBizTypesRequest,
    ) -> green_20170823_models.DescribeUserBizTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_biz_types_with_options_async(request, runtime)

    def describe_user_status_with_options(
        self,
        request: green_20170823_models.DescribeUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUserStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUserStatusResponse(),
            self.do_rpcrequest('DescribeUserStatus', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_status_with_options_async(
        self,
        request: green_20170823_models.DescribeUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeUserStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeUserStatusResponse(),
            await self.do_rpcrequest_async('DescribeUserStatus', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_status(
        self,
        request: green_20170823_models.DescribeUserStatusRequest,
    ) -> green_20170823_models.DescribeUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_status_with_options(request, runtime)

    async def describe_user_status_async(
        self,
        request: green_20170823_models.DescribeUserStatusRequest,
    ) -> green_20170823_models.DescribeUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_status_with_options_async(request, runtime)

    def describe_view_content_with_options(
        self,
        request: green_20170823_models.DescribeViewContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeViewContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeViewContentResponse(),
            self.do_rpcrequest('DescribeViewContent', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_view_content_with_options_async(
        self,
        request: green_20170823_models.DescribeViewContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeViewContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeViewContentResponse(),
            await self.do_rpcrequest_async('DescribeViewContent', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_view_content(
        self,
        request: green_20170823_models.DescribeViewContentRequest,
    ) -> green_20170823_models.DescribeViewContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_view_content_with_options(request, runtime)

    async def describe_view_content_async(
        self,
        request: green_20170823_models.DescribeViewContentRequest,
    ) -> green_20170823_models.DescribeViewContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_view_content_with_options_async(request, runtime)

    def describe_website_index_page_baseline_with_options(
        self,
        request: green_20170823_models.DescribeWebsiteIndexPageBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteIndexPageBaselineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteIndexPageBaselineResponse(),
            self.do_rpcrequest('DescribeWebsiteIndexPageBaseline', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_website_index_page_baseline_with_options_async(
        self,
        request: green_20170823_models.DescribeWebsiteIndexPageBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteIndexPageBaselineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteIndexPageBaselineResponse(),
            await self.do_rpcrequest_async('DescribeWebsiteIndexPageBaseline', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_website_index_page_baseline(
        self,
        request: green_20170823_models.DescribeWebsiteIndexPageBaselineRequest,
    ) -> green_20170823_models.DescribeWebsiteIndexPageBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_website_index_page_baseline_with_options(request, runtime)

    async def describe_website_index_page_baseline_async(
        self,
        request: green_20170823_models.DescribeWebsiteIndexPageBaselineRequest,
    ) -> green_20170823_models.DescribeWebsiteIndexPageBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_website_index_page_baseline_with_options_async(request, runtime)

    def describe_website_instance_with_options(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteInstanceResponse(),
            self.do_rpcrequest('DescribeWebsiteInstance', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_website_instance_with_options_async(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteInstanceResponse(),
            await self.do_rpcrequest_async('DescribeWebsiteInstance', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_website_instance(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceRequest,
    ) -> green_20170823_models.DescribeWebsiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_website_instance_with_options(request, runtime)

    async def describe_website_instance_async(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceRequest,
    ) -> green_20170823_models.DescribeWebsiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_website_instance_with_options_async(request, runtime)

    def describe_website_instance_id_with_options(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteInstanceIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteInstanceIdResponse(),
            self.do_rpcrequest('DescribeWebsiteInstanceId', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_website_instance_id_with_options_async(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteInstanceIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteInstanceIdResponse(),
            await self.do_rpcrequest_async('DescribeWebsiteInstanceId', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_website_instance_id(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceIdRequest,
    ) -> green_20170823_models.DescribeWebsiteInstanceIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_website_instance_id_with_options(request, runtime)

    async def describe_website_instance_id_async(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceIdRequest,
    ) -> green_20170823_models.DescribeWebsiteInstanceIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_website_instance_id_with_options_async(request, runtime)

    def describe_website_instance_key_url_with_options(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceKeyUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteInstanceKeyUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteInstanceKeyUrlResponse(),
            self.do_rpcrequest('DescribeWebsiteInstanceKeyUrl', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_website_instance_key_url_with_options_async(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceKeyUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteInstanceKeyUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteInstanceKeyUrlResponse(),
            await self.do_rpcrequest_async('DescribeWebsiteInstanceKeyUrl', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_website_instance_key_url(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceKeyUrlRequest,
    ) -> green_20170823_models.DescribeWebsiteInstanceKeyUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_website_instance_key_url_with_options(request, runtime)

    async def describe_website_instance_key_url_async(
        self,
        request: green_20170823_models.DescribeWebsiteInstanceKeyUrlRequest,
    ) -> green_20170823_models.DescribeWebsiteInstanceKeyUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_website_instance_key_url_with_options_async(request, runtime)

    def describe_website_scan_result_with_options(
        self,
        request: green_20170823_models.DescribeWebsiteScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteScanResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteScanResultResponse(),
            self.do_rpcrequest('DescribeWebsiteScanResult', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_website_scan_result_with_options_async(
        self,
        request: green_20170823_models.DescribeWebsiteScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteScanResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteScanResultResponse(),
            await self.do_rpcrequest_async('DescribeWebsiteScanResult', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_website_scan_result(
        self,
        request: green_20170823_models.DescribeWebsiteScanResultRequest,
    ) -> green_20170823_models.DescribeWebsiteScanResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_website_scan_result_with_options(request, runtime)

    async def describe_website_scan_result_async(
        self,
        request: green_20170823_models.DescribeWebsiteScanResultRequest,
    ) -> green_20170823_models.DescribeWebsiteScanResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_website_scan_result_with_options_async(request, runtime)

    def describe_website_scan_result_detail_with_options(
        self,
        request: green_20170823_models.DescribeWebsiteScanResultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteScanResultDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteScanResultDetailResponse(),
            self.do_rpcrequest('DescribeWebsiteScanResultDetail', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_website_scan_result_detail_with_options_async(
        self,
        request: green_20170823_models.DescribeWebsiteScanResultDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteScanResultDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteScanResultDetailResponse(),
            await self.do_rpcrequest_async('DescribeWebsiteScanResultDetail', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_website_scan_result_detail(
        self,
        request: green_20170823_models.DescribeWebsiteScanResultDetailRequest,
    ) -> green_20170823_models.DescribeWebsiteScanResultDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_website_scan_result_detail_with_options(request, runtime)

    async def describe_website_scan_result_detail_async(
        self,
        request: green_20170823_models.DescribeWebsiteScanResultDetailRequest,
    ) -> green_20170823_models.DescribeWebsiteScanResultDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_website_scan_result_detail_with_options_async(request, runtime)

    def describe_website_stat_with_options(
        self,
        request: green_20170823_models.DescribeWebsiteStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteStatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteStatResponse(),
            self.do_rpcrequest('DescribeWebsiteStat', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_website_stat_with_options_async(
        self,
        request: green_20170823_models.DescribeWebsiteStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteStatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteStatResponse(),
            await self.do_rpcrequest_async('DescribeWebsiteStat', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_website_stat(
        self,
        request: green_20170823_models.DescribeWebsiteStatRequest,
    ) -> green_20170823_models.DescribeWebsiteStatResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_website_stat_with_options(request, runtime)

    async def describe_website_stat_async(
        self,
        request: green_20170823_models.DescribeWebsiteStatRequest,
    ) -> green_20170823_models.DescribeWebsiteStatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_website_stat_with_options_async(request, runtime)

    def describe_website_verify_info_with_options(
        self,
        request: green_20170823_models.DescribeWebsiteVerifyInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteVerifyInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteVerifyInfoResponse(),
            self.do_rpcrequest('DescribeWebsiteVerifyInfo', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_website_verify_info_with_options_async(
        self,
        request: green_20170823_models.DescribeWebsiteVerifyInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.DescribeWebsiteVerifyInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.DescribeWebsiteVerifyInfoResponse(),
            await self.do_rpcrequest_async('DescribeWebsiteVerifyInfo', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_website_verify_info(
        self,
        request: green_20170823_models.DescribeWebsiteVerifyInfoRequest,
    ) -> green_20170823_models.DescribeWebsiteVerifyInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_website_verify_info_with_options(request, runtime)

    async def describe_website_verify_info_async(
        self,
        request: green_20170823_models.DescribeWebsiteVerifyInfoRequest,
    ) -> green_20170823_models.DescribeWebsiteVerifyInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_website_verify_info_with_options_async(request, runtime)

    def export_keywords_with_options(
        self,
        request: green_20170823_models.ExportKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.ExportKeywordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.ExportKeywordsResponse(),
            self.do_rpcrequest('ExportKeywords', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_keywords_with_options_async(
        self,
        request: green_20170823_models.ExportKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.ExportKeywordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.ExportKeywordsResponse(),
            await self.do_rpcrequest_async('ExportKeywords', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_keywords(
        self,
        request: green_20170823_models.ExportKeywordsRequest,
    ) -> green_20170823_models.ExportKeywordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_keywords_with_options(request, runtime)

    async def export_keywords_async(
        self,
        request: green_20170823_models.ExportKeywordsRequest,
    ) -> green_20170823_models.ExportKeywordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_keywords_with_options_async(request, runtime)

    def export_open_api_rcp_stats_with_options(
        self,
        request: green_20170823_models.ExportOpenApiRcpStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.ExportOpenApiRcpStatsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.ExportOpenApiRcpStatsResponse(),
            self.do_rpcrequest('ExportOpenApiRcpStats', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_open_api_rcp_stats_with_options_async(
        self,
        request: green_20170823_models.ExportOpenApiRcpStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.ExportOpenApiRcpStatsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.ExportOpenApiRcpStatsResponse(),
            await self.do_rpcrequest_async('ExportOpenApiRcpStats', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_open_api_rcp_stats(
        self,
        request: green_20170823_models.ExportOpenApiRcpStatsRequest,
    ) -> green_20170823_models.ExportOpenApiRcpStatsResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_open_api_rcp_stats_with_options(request, runtime)

    async def export_open_api_rcp_stats_async(
        self,
        request: green_20170823_models.ExportOpenApiRcpStatsRequest,
    ) -> green_20170823_models.ExportOpenApiRcpStatsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_open_api_rcp_stats_with_options_async(request, runtime)

    def export_oss_result_with_options(
        self,
        request: green_20170823_models.ExportOssResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.ExportOssResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.ExportOssResultResponse(),
            self.do_rpcrequest('ExportOssResult', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_oss_result_with_options_async(
        self,
        request: green_20170823_models.ExportOssResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.ExportOssResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.ExportOssResultResponse(),
            await self.do_rpcrequest_async('ExportOssResult', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_oss_result(
        self,
        request: green_20170823_models.ExportOssResultRequest,
    ) -> green_20170823_models.ExportOssResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_oss_result_with_options(request, runtime)

    async def export_oss_result_async(
        self,
        request: green_20170823_models.ExportOssResultRequest,
    ) -> green_20170823_models.ExportOssResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_oss_result_with_options_async(request, runtime)

    def import_keywords_with_options(
        self,
        request: green_20170823_models.ImportKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.ImportKeywordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.ImportKeywordsResponse(),
            self.do_rpcrequest('ImportKeywords', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_keywords_with_options_async(
        self,
        request: green_20170823_models.ImportKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.ImportKeywordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.ImportKeywordsResponse(),
            await self.do_rpcrequest_async('ImportKeywords', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_keywords(
        self,
        request: green_20170823_models.ImportKeywordsRequest,
    ) -> green_20170823_models.ImportKeywordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_keywords_with_options(request, runtime)

    async def import_keywords_async(
        self,
        request: green_20170823_models.ImportKeywordsRequest,
    ) -> green_20170823_models.ImportKeywordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_keywords_with_options_async(request, runtime)

    def mark_audit_content_with_options(
        self,
        request: green_20170823_models.MarkAuditContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.MarkAuditContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.MarkAuditContentResponse(),
            self.do_rpcrequest('MarkAuditContent', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def mark_audit_content_with_options_async(
        self,
        request: green_20170823_models.MarkAuditContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.MarkAuditContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.MarkAuditContentResponse(),
            await self.do_rpcrequest_async('MarkAuditContent', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def mark_audit_content(
        self,
        request: green_20170823_models.MarkAuditContentRequest,
    ) -> green_20170823_models.MarkAuditContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.mark_audit_content_with_options(request, runtime)

    async def mark_audit_content_async(
        self,
        request: green_20170823_models.MarkAuditContentRequest,
    ) -> green_20170823_models.MarkAuditContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mark_audit_content_with_options_async(request, runtime)

    def mark_audit_content_item_with_options(
        self,
        request: green_20170823_models.MarkAuditContentItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.MarkAuditContentItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.MarkAuditContentItemResponse(),
            self.do_rpcrequest('MarkAuditContentItem', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def mark_audit_content_item_with_options_async(
        self,
        request: green_20170823_models.MarkAuditContentItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.MarkAuditContentItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.MarkAuditContentItemResponse(),
            await self.do_rpcrequest_async('MarkAuditContentItem', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def mark_audit_content_item(
        self,
        request: green_20170823_models.MarkAuditContentItemRequest,
    ) -> green_20170823_models.MarkAuditContentItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.mark_audit_content_item_with_options(request, runtime)

    async def mark_audit_content_item_async(
        self,
        request: green_20170823_models.MarkAuditContentItemRequest,
    ) -> green_20170823_models.MarkAuditContentItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mark_audit_content_item_with_options_async(request, runtime)

    def mark_oss_result_with_options(
        self,
        request: green_20170823_models.MarkOssResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.MarkOssResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.MarkOssResultResponse(),
            self.do_rpcrequest('MarkOssResult', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def mark_oss_result_with_options_async(
        self,
        request: green_20170823_models.MarkOssResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.MarkOssResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.MarkOssResultResponse(),
            await self.do_rpcrequest_async('MarkOssResult', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def mark_oss_result(
        self,
        request: green_20170823_models.MarkOssResultRequest,
    ) -> green_20170823_models.MarkOssResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.mark_oss_result_with_options(request, runtime)

    async def mark_oss_result_async(
        self,
        request: green_20170823_models.MarkOssResultRequest,
    ) -> green_20170823_models.MarkOssResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mark_oss_result_with_options_async(request, runtime)

    def mark_website_scan_result_with_options(
        self,
        request: green_20170823_models.MarkWebsiteScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.MarkWebsiteScanResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.MarkWebsiteScanResultResponse(),
            self.do_rpcrequest('MarkWebsiteScanResult', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def mark_website_scan_result_with_options_async(
        self,
        request: green_20170823_models.MarkWebsiteScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.MarkWebsiteScanResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.MarkWebsiteScanResultResponse(),
            await self.do_rpcrequest_async('MarkWebsiteScanResult', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def mark_website_scan_result(
        self,
        request: green_20170823_models.MarkWebsiteScanResultRequest,
    ) -> green_20170823_models.MarkWebsiteScanResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.mark_website_scan_result_with_options(request, runtime)

    async def mark_website_scan_result_async(
        self,
        request: green_20170823_models.MarkWebsiteScanResultRequest,
    ) -> green_20170823_models.MarkWebsiteScanResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mark_website_scan_result_with_options_async(request, runtime)

    def refund_cdi_bag_with_options(
        self,
        request: green_20170823_models.RefundCdiBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.RefundCdiBagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.RefundCdiBagResponse(),
            self.do_rpcrequest('RefundCdiBag', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refund_cdi_bag_with_options_async(
        self,
        request: green_20170823_models.RefundCdiBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.RefundCdiBagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.RefundCdiBagResponse(),
            await self.do_rpcrequest_async('RefundCdiBag', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refund_cdi_bag(
        self,
        request: green_20170823_models.RefundCdiBagRequest,
    ) -> green_20170823_models.RefundCdiBagResponse:
        runtime = util_models.RuntimeOptions()
        return self.refund_cdi_bag_with_options(request, runtime)

    async def refund_cdi_bag_async(
        self,
        request: green_20170823_models.RefundCdiBagRequest,
    ) -> green_20170823_models.RefundCdiBagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refund_cdi_bag_with_options_async(request, runtime)

    def refund_cdi_base_bag_with_options(
        self,
        request: green_20170823_models.RefundCdiBaseBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.RefundCdiBaseBagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.RefundCdiBaseBagResponse(),
            self.do_rpcrequest('RefundCdiBaseBag', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refund_cdi_base_bag_with_options_async(
        self,
        request: green_20170823_models.RefundCdiBaseBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.RefundCdiBaseBagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.RefundCdiBaseBagResponse(),
            await self.do_rpcrequest_async('RefundCdiBaseBag', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refund_cdi_base_bag(
        self,
        request: green_20170823_models.RefundCdiBaseBagRequest,
    ) -> green_20170823_models.RefundCdiBaseBagResponse:
        runtime = util_models.RuntimeOptions()
        return self.refund_cdi_base_bag_with_options(request, runtime)

    async def refund_cdi_base_bag_async(
        self,
        request: green_20170823_models.RefundCdiBaseBagRequest,
    ) -> green_20170823_models.RefundCdiBaseBagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refund_cdi_base_bag_with_options_async(request, runtime)

    def refund_web_site_instance_with_options(
        self,
        request: green_20170823_models.RefundWebSiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.RefundWebSiteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.RefundWebSiteInstanceResponse(),
            self.do_rpcrequest('RefundWebSiteInstance', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refund_web_site_instance_with_options_async(
        self,
        request: green_20170823_models.RefundWebSiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.RefundWebSiteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.RefundWebSiteInstanceResponse(),
            await self.do_rpcrequest_async('RefundWebSiteInstance', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refund_web_site_instance(
        self,
        request: green_20170823_models.RefundWebSiteInstanceRequest,
    ) -> green_20170823_models.RefundWebSiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.refund_web_site_instance_with_options(request, runtime)

    async def refund_web_site_instance_async(
        self,
        request: green_20170823_models.RefundWebSiteInstanceRequest,
    ) -> green_20170823_models.RefundWebSiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refund_web_site_instance_with_options_async(request, runtime)

    def renew_web_site_instance_with_options(
        self,
        request: green_20170823_models.RenewWebSiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.RenewWebSiteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.RenewWebSiteInstanceResponse(),
            self.do_rpcrequest('RenewWebSiteInstance', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_web_site_instance_with_options_async(
        self,
        request: green_20170823_models.RenewWebSiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.RenewWebSiteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.RenewWebSiteInstanceResponse(),
            await self.do_rpcrequest_async('RenewWebSiteInstance', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_web_site_instance(
        self,
        request: green_20170823_models.RenewWebSiteInstanceRequest,
    ) -> green_20170823_models.RenewWebSiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_web_site_instance_with_options(request, runtime)

    async def renew_web_site_instance_async(
        self,
        request: green_20170823_models.RenewWebSiteInstanceRequest,
    ) -> green_20170823_models.RenewWebSiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_web_site_instance_with_options_async(request, runtime)

    def send_verify_code_to_email_with_options(
        self,
        request: green_20170823_models.SendVerifyCodeToEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.SendVerifyCodeToEmailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.SendVerifyCodeToEmailResponse(),
            self.do_rpcrequest('SendVerifyCodeToEmail', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_verify_code_to_email_with_options_async(
        self,
        request: green_20170823_models.SendVerifyCodeToEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.SendVerifyCodeToEmailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.SendVerifyCodeToEmailResponse(),
            await self.do_rpcrequest_async('SendVerifyCodeToEmail', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_verify_code_to_email(
        self,
        request: green_20170823_models.SendVerifyCodeToEmailRequest,
    ) -> green_20170823_models.SendVerifyCodeToEmailResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_verify_code_to_email_with_options(request, runtime)

    async def send_verify_code_to_email_async(
        self,
        request: green_20170823_models.SendVerifyCodeToEmailRequest,
    ) -> green_20170823_models.SendVerifyCodeToEmailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_verify_code_to_email_with_options_async(request, runtime)

    def send_verify_code_to_phone_with_options(
        self,
        request: green_20170823_models.SendVerifyCodeToPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.SendVerifyCodeToPhoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.SendVerifyCodeToPhoneResponse(),
            self.do_rpcrequest('SendVerifyCodeToPhone', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_verify_code_to_phone_with_options_async(
        self,
        request: green_20170823_models.SendVerifyCodeToPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.SendVerifyCodeToPhoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.SendVerifyCodeToPhoneResponse(),
            await self.do_rpcrequest_async('SendVerifyCodeToPhone', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_verify_code_to_phone(
        self,
        request: green_20170823_models.SendVerifyCodeToPhoneRequest,
    ) -> green_20170823_models.SendVerifyCodeToPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_verify_code_to_phone_with_options(request, runtime)

    async def send_verify_code_to_phone_async(
        self,
        request: green_20170823_models.SendVerifyCodeToPhoneRequest,
    ) -> green_20170823_models.SendVerifyCodeToPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_verify_code_to_phone_with_options_async(request, runtime)

    def send_website_feedback_with_options(
        self,
        request: green_20170823_models.SendWebsiteFeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.SendWebsiteFeedbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.SendWebsiteFeedbackResponse(),
            self.do_rpcrequest('SendWebsiteFeedback', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_website_feedback_with_options_async(
        self,
        request: green_20170823_models.SendWebsiteFeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.SendWebsiteFeedbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.SendWebsiteFeedbackResponse(),
            await self.do_rpcrequest_async('SendWebsiteFeedback', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_website_feedback(
        self,
        request: green_20170823_models.SendWebsiteFeedbackRequest,
    ) -> green_20170823_models.SendWebsiteFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_website_feedback_with_options(request, runtime)

    async def send_website_feedback_async(
        self,
        request: green_20170823_models.SendWebsiteFeedbackRequest,
    ) -> green_20170823_models.SendWebsiteFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_website_feedback_with_options_async(request, runtime)

    def update_app_package_with_options(
        self,
        request: green_20170823_models.UpdateAppPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateAppPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAppPackageResponse(),
            self.do_rpcrequest('UpdateAppPackage', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_app_package_with_options_async(
        self,
        request: green_20170823_models.UpdateAppPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateAppPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAppPackageResponse(),
            await self.do_rpcrequest_async('UpdateAppPackage', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_package(
        self,
        request: green_20170823_models.UpdateAppPackageRequest,
    ) -> green_20170823_models.UpdateAppPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_package_with_options(request, runtime)

    async def update_app_package_async(
        self,
        request: green_20170823_models.UpdateAppPackageRequest,
    ) -> green_20170823_models.UpdateAppPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_package_with_options_async(request, runtime)

    def update_audit_callback_with_options(
        self,
        request: green_20170823_models.UpdateAuditCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateAuditCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAuditCallbackResponse(),
            self.do_rpcrequest('UpdateAuditCallback', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_audit_callback_with_options_async(
        self,
        request: green_20170823_models.UpdateAuditCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateAuditCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAuditCallbackResponse(),
            await self.do_rpcrequest_async('UpdateAuditCallback', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_audit_callback(
        self,
        request: green_20170823_models.UpdateAuditCallbackRequest,
    ) -> green_20170823_models.UpdateAuditCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_audit_callback_with_options(request, runtime)

    async def update_audit_callback_async(
        self,
        request: green_20170823_models.UpdateAuditCallbackRequest,
    ) -> green_20170823_models.UpdateAuditCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_audit_callback_with_options_async(request, runtime)

    def update_audit_range_with_options(
        self,
        request: green_20170823_models.UpdateAuditRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateAuditRangeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAuditRangeResponse(),
            self.do_rpcrequest('UpdateAuditRange', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_audit_range_with_options_async(
        self,
        request: green_20170823_models.UpdateAuditRangeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateAuditRangeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAuditRangeResponse(),
            await self.do_rpcrequest_async('UpdateAuditRange', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_audit_range(
        self,
        request: green_20170823_models.UpdateAuditRangeRequest,
    ) -> green_20170823_models.UpdateAuditRangeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_audit_range_with_options(request, runtime)

    async def update_audit_range_async(
        self,
        request: green_20170823_models.UpdateAuditRangeRequest,
    ) -> green_20170823_models.UpdateAuditRangeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_audit_range_with_options_async(request, runtime)

    def update_audit_setting_with_options(
        self,
        request: green_20170823_models.UpdateAuditSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateAuditSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAuditSettingResponse(),
            self.do_rpcrequest('UpdateAuditSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_audit_setting_with_options_async(
        self,
        request: green_20170823_models.UpdateAuditSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateAuditSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateAuditSettingResponse(),
            await self.do_rpcrequest_async('UpdateAuditSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_audit_setting(
        self,
        request: green_20170823_models.UpdateAuditSettingRequest,
    ) -> green_20170823_models.UpdateAuditSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_audit_setting_with_options(request, runtime)

    async def update_audit_setting_async(
        self,
        request: green_20170823_models.UpdateAuditSettingRequest,
    ) -> green_20170823_models.UpdateAuditSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_audit_setting_with_options_async(request, runtime)

    def update_biz_type_with_options(
        self,
        request: green_20170823_models.UpdateBizTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateBizTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeResponse(),
            self.do_rpcrequest('UpdateBizType', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_biz_type_with_options_async(
        self,
        request: green_20170823_models.UpdateBizTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateBizTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeResponse(),
            await self.do_rpcrequest_async('UpdateBizType', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_biz_type(
        self,
        request: green_20170823_models.UpdateBizTypeRequest,
    ) -> green_20170823_models.UpdateBizTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_biz_type_with_options(request, runtime)

    async def update_biz_type_async(
        self,
        request: green_20170823_models.UpdateBizTypeRequest,
    ) -> green_20170823_models.UpdateBizTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_biz_type_with_options_async(request, runtime)

    def update_biz_type_image_lib_with_options(
        self,
        request: green_20170823_models.UpdateBizTypeImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateBizTypeImageLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeImageLibResponse(),
            self.do_rpcrequest('UpdateBizTypeImageLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_biz_type_image_lib_with_options_async(
        self,
        request: green_20170823_models.UpdateBizTypeImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateBizTypeImageLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeImageLibResponse(),
            await self.do_rpcrequest_async('UpdateBizTypeImageLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_biz_type_image_lib(
        self,
        request: green_20170823_models.UpdateBizTypeImageLibRequest,
    ) -> green_20170823_models.UpdateBizTypeImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_biz_type_image_lib_with_options(request, runtime)

    async def update_biz_type_image_lib_async(
        self,
        request: green_20170823_models.UpdateBizTypeImageLibRequest,
    ) -> green_20170823_models.UpdateBizTypeImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_biz_type_image_lib_with_options_async(request, runtime)

    def update_biz_type_setting_with_options(
        self,
        request: green_20170823_models.UpdateBizTypeSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateBizTypeSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeSettingResponse(),
            self.do_rpcrequest('UpdateBizTypeSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_biz_type_setting_with_options_async(
        self,
        request: green_20170823_models.UpdateBizTypeSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateBizTypeSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeSettingResponse(),
            await self.do_rpcrequest_async('UpdateBizTypeSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_biz_type_setting(
        self,
        request: green_20170823_models.UpdateBizTypeSettingRequest,
    ) -> green_20170823_models.UpdateBizTypeSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_biz_type_setting_with_options(request, runtime)

    async def update_biz_type_setting_async(
        self,
        request: green_20170823_models.UpdateBizTypeSettingRequest,
    ) -> green_20170823_models.UpdateBizTypeSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_biz_type_setting_with_options_async(request, runtime)

    def update_biz_type_text_lib_with_options(
        self,
        request: green_20170823_models.UpdateBizTypeTextLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateBizTypeTextLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeTextLibResponse(),
            self.do_rpcrequest('UpdateBizTypeTextLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_biz_type_text_lib_with_options_async(
        self,
        request: green_20170823_models.UpdateBizTypeTextLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateBizTypeTextLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateBizTypeTextLibResponse(),
            await self.do_rpcrequest_async('UpdateBizTypeTextLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_biz_type_text_lib(
        self,
        request: green_20170823_models.UpdateBizTypeTextLibRequest,
    ) -> green_20170823_models.UpdateBizTypeTextLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_biz_type_text_lib_with_options(request, runtime)

    async def update_biz_type_text_lib_async(
        self,
        request: green_20170823_models.UpdateBizTypeTextLibRequest,
    ) -> green_20170823_models.UpdateBizTypeTextLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_biz_type_text_lib_with_options_async(request, runtime)

    def update_custom_ocr_template_with_options(
        self,
        request: green_20170823_models.UpdateCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateCustomOcrTemplateResponse(),
            self.do_rpcrequest('UpdateCustomOcrTemplate', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_custom_ocr_template_with_options_async(
        self,
        request: green_20170823_models.UpdateCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateCustomOcrTemplateResponse(),
            await self.do_rpcrequest_async('UpdateCustomOcrTemplate', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_custom_ocr_template(
        self,
        request: green_20170823_models.UpdateCustomOcrTemplateRequest,
    ) -> green_20170823_models.UpdateCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_custom_ocr_template_with_options(request, runtime)

    async def update_custom_ocr_template_async(
        self,
        request: green_20170823_models.UpdateCustomOcrTemplateRequest,
    ) -> green_20170823_models.UpdateCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_custom_ocr_template_with_options_async(request, runtime)

    def update_image_lib_with_options(
        self,
        request: green_20170823_models.UpdateImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateImageLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateImageLibResponse(),
            self.do_rpcrequest('UpdateImageLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_image_lib_with_options_async(
        self,
        request: green_20170823_models.UpdateImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateImageLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateImageLibResponse(),
            await self.do_rpcrequest_async('UpdateImageLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_image_lib(
        self,
        request: green_20170823_models.UpdateImageLibRequest,
    ) -> green_20170823_models.UpdateImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_image_lib_with_options(request, runtime)

    async def update_image_lib_async(
        self,
        request: green_20170823_models.UpdateImageLibRequest,
    ) -> green_20170823_models.UpdateImageLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_image_lib_with_options_async(request, runtime)

    def update_keyword_lib_with_options(
        self,
        request: green_20170823_models.UpdateKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateKeywordLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateKeywordLibResponse(),
            self.do_rpcrequest('UpdateKeywordLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_keyword_lib_with_options_async(
        self,
        request: green_20170823_models.UpdateKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateKeywordLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateKeywordLibResponse(),
            await self.do_rpcrequest_async('UpdateKeywordLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_keyword_lib(
        self,
        request: green_20170823_models.UpdateKeywordLibRequest,
    ) -> green_20170823_models.UpdateKeywordLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_keyword_lib_with_options(request, runtime)

    async def update_keyword_lib_async(
        self,
        request: green_20170823_models.UpdateKeywordLibRequest,
    ) -> green_20170823_models.UpdateKeywordLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_keyword_lib_with_options_async(request, runtime)

    def update_notification_setting_with_options(
        self,
        request: green_20170823_models.UpdateNotificationSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateNotificationSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateNotificationSettingResponse(),
            self.do_rpcrequest('UpdateNotificationSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_notification_setting_with_options_async(
        self,
        request: green_20170823_models.UpdateNotificationSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateNotificationSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateNotificationSettingResponse(),
            await self.do_rpcrequest_async('UpdateNotificationSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_notification_setting(
        self,
        request: green_20170823_models.UpdateNotificationSettingRequest,
    ) -> green_20170823_models.UpdateNotificationSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_notification_setting_with_options(request, runtime)

    async def update_notification_setting_async(
        self,
        request: green_20170823_models.UpdateNotificationSettingRequest,
    ) -> green_20170823_models.UpdateNotificationSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_notification_setting_with_options_async(request, runtime)

    def update_oss_callback_setting_with_options(
        self,
        request: green_20170823_models.UpdateOssCallbackSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateOssCallbackSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateOssCallbackSettingResponse(),
            self.do_rpcrequest('UpdateOssCallbackSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_oss_callback_setting_with_options_async(
        self,
        request: green_20170823_models.UpdateOssCallbackSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateOssCallbackSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateOssCallbackSettingResponse(),
            await self.do_rpcrequest_async('UpdateOssCallbackSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_oss_callback_setting(
        self,
        request: green_20170823_models.UpdateOssCallbackSettingRequest,
    ) -> green_20170823_models.UpdateOssCallbackSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_oss_callback_setting_with_options(request, runtime)

    async def update_oss_callback_setting_async(
        self,
        request: green_20170823_models.UpdateOssCallbackSettingRequest,
    ) -> green_20170823_models.UpdateOssCallbackSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_oss_callback_setting_with_options_async(request, runtime)

    def update_oss_increment_check_setting_with_options(
        self,
        request: green_20170823_models.UpdateOssIncrementCheckSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateOssIncrementCheckSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateOssIncrementCheckSettingResponse(),
            self.do_rpcrequest('UpdateOssIncrementCheckSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_oss_increment_check_setting_with_options_async(
        self,
        request: green_20170823_models.UpdateOssIncrementCheckSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateOssIncrementCheckSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateOssIncrementCheckSettingResponse(),
            await self.do_rpcrequest_async('UpdateOssIncrementCheckSetting', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_oss_increment_check_setting(
        self,
        request: green_20170823_models.UpdateOssIncrementCheckSettingRequest,
    ) -> green_20170823_models.UpdateOssIncrementCheckSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_oss_increment_check_setting_with_options(request, runtime)

    async def update_oss_increment_check_setting_async(
        self,
        request: green_20170823_models.UpdateOssIncrementCheckSettingRequest,
    ) -> green_20170823_models.UpdateOssIncrementCheckSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_oss_increment_check_setting_with_options_async(request, runtime)

    def update_oss_stock_status_with_options(
        self,
        request: green_20170823_models.UpdateOssStockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateOssStockStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateOssStockStatusResponse(),
            self.do_rpcrequest('UpdateOssStockStatus', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_oss_stock_status_with_options_async(
        self,
        request: green_20170823_models.UpdateOssStockStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateOssStockStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateOssStockStatusResponse(),
            await self.do_rpcrequest_async('UpdateOssStockStatus', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_oss_stock_status(
        self,
        request: green_20170823_models.UpdateOssStockStatusRequest,
    ) -> green_20170823_models.UpdateOssStockStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_oss_stock_status_with_options(request, runtime)

    async def update_oss_stock_status_async(
        self,
        request: green_20170823_models.UpdateOssStockStatusRequest,
    ) -> green_20170823_models.UpdateOssStockStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_oss_stock_status_with_options_async(request, runtime)

    def update_website_instance_with_options(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateWebsiteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateWebsiteInstanceResponse(),
            self.do_rpcrequest('UpdateWebsiteInstance', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_website_instance_with_options_async(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateWebsiteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateWebsiteInstanceResponse(),
            await self.do_rpcrequest_async('UpdateWebsiteInstance', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_website_instance(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceRequest,
    ) -> green_20170823_models.UpdateWebsiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_website_instance_with_options(request, runtime)

    async def update_website_instance_async(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceRequest,
    ) -> green_20170823_models.UpdateWebsiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_website_instance_with_options_async(request, runtime)

    def update_website_instance_key_url_with_options(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceKeyUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateWebsiteInstanceKeyUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateWebsiteInstanceKeyUrlResponse(),
            self.do_rpcrequest('UpdateWebsiteInstanceKeyUrl', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_website_instance_key_url_with_options_async(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceKeyUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateWebsiteInstanceKeyUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateWebsiteInstanceKeyUrlResponse(),
            await self.do_rpcrequest_async('UpdateWebsiteInstanceKeyUrl', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_website_instance_key_url(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceKeyUrlRequest,
    ) -> green_20170823_models.UpdateWebsiteInstanceKeyUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_website_instance_key_url_with_options(request, runtime)

    async def update_website_instance_key_url_async(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceKeyUrlRequest,
    ) -> green_20170823_models.UpdateWebsiteInstanceKeyUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_website_instance_key_url_with_options_async(request, runtime)

    def update_website_instance_status_with_options(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateWebsiteInstanceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateWebsiteInstanceStatusResponse(),
            self.do_rpcrequest('UpdateWebsiteInstanceStatus', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_website_instance_status_with_options_async(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpdateWebsiteInstanceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpdateWebsiteInstanceStatusResponse(),
            await self.do_rpcrequest_async('UpdateWebsiteInstanceStatus', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_website_instance_status(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceStatusRequest,
    ) -> green_20170823_models.UpdateWebsiteInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_website_instance_status_with_options(request, runtime)

    async def update_website_instance_status_async(
        self,
        request: green_20170823_models.UpdateWebsiteInstanceStatusRequest,
    ) -> green_20170823_models.UpdateWebsiteInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_website_instance_status_with_options_async(request, runtime)

    def upgrade_cdi_base_bag_with_options(
        self,
        request: green_20170823_models.UpgradeCdiBaseBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpgradeCdiBaseBagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpgradeCdiBaseBagResponse(),
            self.do_rpcrequest('UpgradeCdiBaseBag', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_cdi_base_bag_with_options_async(
        self,
        request: green_20170823_models.UpgradeCdiBaseBagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UpgradeCdiBaseBagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UpgradeCdiBaseBagResponse(),
            await self.do_rpcrequest_async('UpgradeCdiBaseBag', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_cdi_base_bag(
        self,
        request: green_20170823_models.UpgradeCdiBaseBagRequest,
    ) -> green_20170823_models.UpgradeCdiBaseBagResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_cdi_base_bag_with_options(request, runtime)

    async def upgrade_cdi_base_bag_async(
        self,
        request: green_20170823_models.UpgradeCdiBaseBagRequest,
    ) -> green_20170823_models.UpgradeCdiBaseBagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_cdi_base_bag_with_options_async(request, runtime)

    def upload_image_to_lib_with_options(
        self,
        request: green_20170823_models.UploadImageToLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UploadImageToLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UploadImageToLibResponse(),
            self.do_rpcrequest('UploadImageToLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_image_to_lib_with_options_async(
        self,
        request: green_20170823_models.UploadImageToLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.UploadImageToLibResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.UploadImageToLibResponse(),
            await self.do_rpcrequest_async('UploadImageToLib', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_image_to_lib(
        self,
        request: green_20170823_models.UploadImageToLibRequest,
    ) -> green_20170823_models.UploadImageToLibResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_image_to_lib_with_options(request, runtime)

    async def upload_image_to_lib_async(
        self,
        request: green_20170823_models.UploadImageToLibRequest,
    ) -> green_20170823_models.UploadImageToLibResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_image_to_lib_with_options_async(request, runtime)

    def verify_custom_ocr_template_with_options(
        self,
        request: green_20170823_models.VerifyCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.VerifyCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyCustomOcrTemplateResponse(),
            self.do_rpcrequest('VerifyCustomOcrTemplate', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_custom_ocr_template_with_options_async(
        self,
        request: green_20170823_models.VerifyCustomOcrTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.VerifyCustomOcrTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyCustomOcrTemplateResponse(),
            await self.do_rpcrequest_async('VerifyCustomOcrTemplate', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_custom_ocr_template(
        self,
        request: green_20170823_models.VerifyCustomOcrTemplateRequest,
    ) -> green_20170823_models.VerifyCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_custom_ocr_template_with_options(request, runtime)

    async def verify_custom_ocr_template_async(
        self,
        request: green_20170823_models.VerifyCustomOcrTemplateRequest,
    ) -> green_20170823_models.VerifyCustomOcrTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_custom_ocr_template_with_options_async(request, runtime)

    def verify_email_with_options(
        self,
        request: green_20170823_models.VerifyEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.VerifyEmailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyEmailResponse(),
            self.do_rpcrequest('VerifyEmail', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_email_with_options_async(
        self,
        request: green_20170823_models.VerifyEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.VerifyEmailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyEmailResponse(),
            await self.do_rpcrequest_async('VerifyEmail', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_email(
        self,
        request: green_20170823_models.VerifyEmailRequest,
    ) -> green_20170823_models.VerifyEmailResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_email_with_options(request, runtime)

    async def verify_email_async(
        self,
        request: green_20170823_models.VerifyEmailRequest,
    ) -> green_20170823_models.VerifyEmailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_email_with_options_async(request, runtime)

    def verify_phone_with_options(
        self,
        request: green_20170823_models.VerifyPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.VerifyPhoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyPhoneResponse(),
            self.do_rpcrequest('VerifyPhone', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_phone_with_options_async(
        self,
        request: green_20170823_models.VerifyPhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.VerifyPhoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyPhoneResponse(),
            await self.do_rpcrequest_async('VerifyPhone', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_phone(
        self,
        request: green_20170823_models.VerifyPhoneRequest,
    ) -> green_20170823_models.VerifyPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_phone_with_options(request, runtime)

    async def verify_phone_async(
        self,
        request: green_20170823_models.VerifyPhoneRequest,
    ) -> green_20170823_models.VerifyPhoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_phone_with_options_async(request, runtime)

    def verify_website_instance_with_options(
        self,
        request: green_20170823_models.VerifyWebsiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.VerifyWebsiteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyWebsiteInstanceResponse(),
            self.do_rpcrequest('VerifyWebsiteInstance', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_website_instance_with_options_async(
        self,
        request: green_20170823_models.VerifyWebsiteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20170823_models.VerifyWebsiteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            green_20170823_models.VerifyWebsiteInstanceResponse(),
            await self.do_rpcrequest_async('VerifyWebsiteInstance', '2017-08-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_website_instance(
        self,
        request: green_20170823_models.VerifyWebsiteInstanceRequest,
    ) -> green_20170823_models.VerifyWebsiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_website_instance_with_options(request, runtime)

    async def verify_website_instance_async(
        self,
        request: green_20170823_models.VerifyWebsiteInstanceRequest,
    ) -> green_20170823_models.VerifyWebsiteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_website_instance_with_options_async(request, runtime)
