# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cd2021127 import models as cd_2021127_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('cd', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_product_image_with_options(
        self,
        tmp_req: cd_2021127_models.AddProductImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.AddProductImageResponse:
        """
        @summary 添加商品图片属性
        
        @param tmp_req: AddProductImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddProductImageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.AddProductImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.product_image_list):
            request.product_image_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.product_image_list, 'ProductImageList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_image_list_shrink):
            body['ProductImageList'] = request.product_image_list_shrink
        if not UtilClient.is_unset(request.product_name):
            body['ProductName'] = request.product_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddProductImage',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/AddProductImage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.AddProductImageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.AddProductImageResponse(),
                self.execute(params, req, runtime)
            )

    async def add_product_image_with_options_async(
        self,
        tmp_req: cd_2021127_models.AddProductImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.AddProductImageResponse:
        """
        @summary 添加商品图片属性
        
        @param tmp_req: AddProductImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddProductImageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.AddProductImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.product_image_list):
            request.product_image_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.product_image_list, 'ProductImageList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_image_list_shrink):
            body['ProductImageList'] = request.product_image_list_shrink
        if not UtilClient.is_unset(request.product_name):
            body['ProductName'] = request.product_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddProductImage',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/AddProductImage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.AddProductImageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.AddProductImageResponse(),
                await self.execute_async(params, req, runtime)
            )

    def add_product_image(
        self,
        request: cd_2021127_models.AddProductImageRequest,
    ) -> cd_2021127_models.AddProductImageResponse:
        """
        @summary 添加商品图片属性
        
        @param request: AddProductImageRequest
        @return: AddProductImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_product_image_with_options(request, headers, runtime)

    async def add_product_image_async(
        self,
        request: cd_2021127_models.AddProductImageRequest,
    ) -> cd_2021127_models.AddProductImageResponse:
        """
        @summary 添加商品图片属性
        
        @param request: AddProductImageRequest
        @return: AddProductImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_product_image_with_options_async(request, headers, runtime)

    def add_shop_to_group_with_options(
        self,
        tmp_req: cd_2021127_models.AddShopToGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.AddShopToGroupResponse:
        """
        @summary 门店组添加门店
        
        @param tmp_req: AddShopToGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddShopToGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.AddShopToGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddShopToGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/AddShopToGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.AddShopToGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.AddShopToGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def add_shop_to_group_with_options_async(
        self,
        tmp_req: cd_2021127_models.AddShopToGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.AddShopToGroupResponse:
        """
        @summary 门店组添加门店
        
        @param tmp_req: AddShopToGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddShopToGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.AddShopToGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddShopToGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/AddShopToGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.AddShopToGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.AddShopToGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def add_shop_to_group(
        self,
        request: cd_2021127_models.AddShopToGroupRequest,
    ) -> cd_2021127_models.AddShopToGroupResponse:
        """
        @summary 门店组添加门店
        
        @param request: AddShopToGroupRequest
        @return: AddShopToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_shop_to_group_with_options(request, headers, runtime)

    async def add_shop_to_group_async(
        self,
        request: cd_2021127_models.AddShopToGroupRequest,
    ) -> cd_2021127_models.AddShopToGroupResponse:
        """
        @summary 门店组添加门店
        
        @param request: AddShopToGroupRequest
        @return: AddShopToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_shop_to_group_with_options_async(request, headers, runtime)

    def add_shops_to_group_with_options(
        self,
        tmp_req: cd_2021127_models.AddShopsToGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.AddShopsToGroupResponse:
        """
        @summary 门店组添加门店
        
        @param tmp_req: AddShopsToGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddShopsToGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.AddShopsToGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddShopsToGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/AddShopsToGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.AddShopsToGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.AddShopsToGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def add_shops_to_group_with_options_async(
        self,
        tmp_req: cd_2021127_models.AddShopsToGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.AddShopsToGroupResponse:
        """
        @summary 门店组添加门店
        
        @param tmp_req: AddShopsToGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddShopsToGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.AddShopsToGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddShopsToGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/AddShopsToGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.AddShopsToGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.AddShopsToGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def add_shops_to_group(
        self,
        request: cd_2021127_models.AddShopsToGroupRequest,
    ) -> cd_2021127_models.AddShopsToGroupResponse:
        """
        @summary 门店组添加门店
        
        @param request: AddShopsToGroupRequest
        @return: AddShopsToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_shops_to_group_with_options(request, headers, runtime)

    async def add_shops_to_group_async(
        self,
        request: cd_2021127_models.AddShopsToGroupRequest,
    ) -> cd_2021127_models.AddShopsToGroupResponse:
        """
        @summary 门店组添加门店
        
        @param request: AddShopsToGroupRequest
        @return: AddShopsToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_shops_to_group_with_options_async(request, headers, runtime)

    def bai_lian_sse_chat_with_options(
        self,
        tmp_req: cd_2021127_models.BaiLianSseChatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.BaiLianSseChatResponse:
        """
        @summary 百炼vqa
        
        @param tmp_req: BaiLianSseChatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BaiLianSseChatResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.BaiLianSseChatShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BaiLianSseChat',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/llm/sse/vqa',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.BaiLianSseChatResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.BaiLianSseChatResponse(),
                self.execute(params, req, runtime)
            )

    async def bai_lian_sse_chat_with_options_async(
        self,
        tmp_req: cd_2021127_models.BaiLianSseChatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.BaiLianSseChatResponse:
        """
        @summary 百炼vqa
        
        @param tmp_req: BaiLianSseChatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BaiLianSseChatResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.BaiLianSseChatShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BaiLianSseChat',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/llm/sse/vqa',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.BaiLianSseChatResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.BaiLianSseChatResponse(),
                await self.execute_async(params, req, runtime)
            )

    def bai_lian_sse_chat(
        self,
        request: cd_2021127_models.BaiLianSseChatRequest,
    ) -> cd_2021127_models.BaiLianSseChatResponse:
        """
        @summary 百炼vqa
        
        @param request: BaiLianSseChatRequest
        @return: BaiLianSseChatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.bai_lian_sse_chat_with_options(request, headers, runtime)

    async def bai_lian_sse_chat_async(
        self,
        request: cd_2021127_models.BaiLianSseChatRequest,
    ) -> cd_2021127_models.BaiLianSseChatResponse:
        """
        @summary 百炼vqa
        
        @param request: BaiLianSseChatRequest
        @return: BaiLianSseChatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.bai_lian_sse_chat_with_options_async(request, headers, runtime)

    def batch_create_shop_with_options(
        self,
        tmp_req: cd_2021127_models.BatchCreateShopRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.BatchCreateShopResponse:
        """
        @summary 批量创建门店
        
        @param tmp_req: BatchCreateShopRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateShopResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.BatchCreateShopShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_list):
            request.shop_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_list, 'ShopList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_list_shrink):
            body['ShopList'] = request.shop_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateShop',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/BatchCreateShop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.BatchCreateShopResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.BatchCreateShopResponse(),
                self.execute(params, req, runtime)
            )

    async def batch_create_shop_with_options_async(
        self,
        tmp_req: cd_2021127_models.BatchCreateShopRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.BatchCreateShopResponse:
        """
        @summary 批量创建门店
        
        @param tmp_req: BatchCreateShopRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateShopResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.BatchCreateShopShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_list):
            request.shop_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_list, 'ShopList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_list_shrink):
            body['ShopList'] = request.shop_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateShop',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/BatchCreateShop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.BatchCreateShopResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.BatchCreateShopResponse(),
                await self.execute_async(params, req, runtime)
            )

    def batch_create_shop(
        self,
        request: cd_2021127_models.BatchCreateShopRequest,
    ) -> cd_2021127_models.BatchCreateShopResponse:
        """
        @summary 批量创建门店
        
        @param request: BatchCreateShopRequest
        @return: BatchCreateShopResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_create_shop_with_options(request, headers, runtime)

    async def batch_create_shop_async(
        self,
        request: cd_2021127_models.BatchCreateShopRequest,
    ) -> cd_2021127_models.BatchCreateShopResponse:
        """
        @summary 批量创建门店
        
        @param request: BatchCreateShopRequest
        @return: BatchCreateShopResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_create_shop_with_options_async(request, headers, runtime)

    def batch_create_shop_group_with_options(
        self,
        tmp_req: cd_2021127_models.BatchCreateShopGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.BatchCreateShopGroupResponse:
        """
        @summary 批量创建门店组
        
        @param tmp_req: BatchCreateShopGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateShopGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.BatchCreateShopGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_group_list):
            request.shop_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_group_list, 'ShopGroupList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_group_list_shrink):
            body['ShopGroupList'] = request.shop_group_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateShopGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/BatchCreateShopGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.BatchCreateShopGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.BatchCreateShopGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def batch_create_shop_group_with_options_async(
        self,
        tmp_req: cd_2021127_models.BatchCreateShopGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.BatchCreateShopGroupResponse:
        """
        @summary 批量创建门店组
        
        @param tmp_req: BatchCreateShopGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateShopGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.BatchCreateShopGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_group_list):
            request.shop_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_group_list, 'ShopGroupList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_group_list_shrink):
            body['ShopGroupList'] = request.shop_group_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateShopGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/BatchCreateShopGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.BatchCreateShopGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.BatchCreateShopGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def batch_create_shop_group(
        self,
        request: cd_2021127_models.BatchCreateShopGroupRequest,
    ) -> cd_2021127_models.BatchCreateShopGroupResponse:
        """
        @summary 批量创建门店组
        
        @param request: BatchCreateShopGroupRequest
        @return: BatchCreateShopGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_create_shop_group_with_options(request, headers, runtime)

    async def batch_create_shop_group_async(
        self,
        request: cd_2021127_models.BatchCreateShopGroupRequest,
    ) -> cd_2021127_models.BatchCreateShopGroupResponse:
        """
        @summary 批量创建门店组
        
        @param request: BatchCreateShopGroupRequest
        @return: BatchCreateShopGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_create_shop_group_with_options_async(request, headers, runtime)

    def batch_get_store_text_data_with_options(
        self,
        tmp_req: cd_2021127_models.BatchGetStoreTextDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.BatchGetStoreTextDataResponse:
        """
        @param tmp_req: BatchGetStoreTextDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetStoreTextDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.BatchGetStoreTextDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.store_ids):
            request.store_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.store_ids, 'StoreIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.store_ids_shrink):
            body['StoreIds'] = request.store_ids_shrink
        if not UtilClient.is_unset(request.country):
            body['country'] = request.country
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGetStoreTextData',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/BatchGetStoreTextData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.BatchGetStoreTextDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.BatchGetStoreTextDataResponse(),
                self.execute(params, req, runtime)
            )

    async def batch_get_store_text_data_with_options_async(
        self,
        tmp_req: cd_2021127_models.BatchGetStoreTextDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.BatchGetStoreTextDataResponse:
        """
        @param tmp_req: BatchGetStoreTextDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetStoreTextDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.BatchGetStoreTextDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.store_ids):
            request.store_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.store_ids, 'StoreIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.store_ids_shrink):
            body['StoreIds'] = request.store_ids_shrink
        if not UtilClient.is_unset(request.country):
            body['country'] = request.country
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGetStoreTextData',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/BatchGetStoreTextData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.BatchGetStoreTextDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.BatchGetStoreTextDataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def batch_get_store_text_data(
        self,
        request: cd_2021127_models.BatchGetStoreTextDataRequest,
    ) -> cd_2021127_models.BatchGetStoreTextDataResponse:
        """
        @param request: BatchGetStoreTextDataRequest
        @return: BatchGetStoreTextDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_get_store_text_data_with_options(request, headers, runtime)

    async def batch_get_store_text_data_async(
        self,
        request: cd_2021127_models.BatchGetStoreTextDataRequest,
    ) -> cd_2021127_models.BatchGetStoreTextDataResponse:
        """
        @param request: BatchGetStoreTextDataRequest
        @return: BatchGetStoreTextDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_get_store_text_data_with_options_async(request, headers, runtime)

    def batch_update_store_text_data_with_options(
        self,
        tmp_req: cd_2021127_models.BatchUpdateStoreTextDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.BatchUpdateStoreTextDataResponse:
        """
        @param tmp_req: BatchUpdateStoreTextDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUpdateStoreTextDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.BatchUpdateStoreTextDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.store_text_data):
            request.store_text_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.store_text_data, 'StoreTextData', 'json')
        body = {}
        if not UtilClient.is_unset(request.store_text_data_shrink):
            body['StoreTextData'] = request.store_text_data_shrink
        if not UtilClient.is_unset(request.country):
            body['country'] = request.country
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUpdateStoreTextData',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/BatchUpdateStoreTextData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.BatchUpdateStoreTextDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.BatchUpdateStoreTextDataResponse(),
                self.execute(params, req, runtime)
            )

    async def batch_update_store_text_data_with_options_async(
        self,
        tmp_req: cd_2021127_models.BatchUpdateStoreTextDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.BatchUpdateStoreTextDataResponse:
        """
        @param tmp_req: BatchUpdateStoreTextDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUpdateStoreTextDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.BatchUpdateStoreTextDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.store_text_data):
            request.store_text_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.store_text_data, 'StoreTextData', 'json')
        body = {}
        if not UtilClient.is_unset(request.store_text_data_shrink):
            body['StoreTextData'] = request.store_text_data_shrink
        if not UtilClient.is_unset(request.country):
            body['country'] = request.country
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUpdateStoreTextData',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/BatchUpdateStoreTextData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.BatchUpdateStoreTextDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.BatchUpdateStoreTextDataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def batch_update_store_text_data(
        self,
        request: cd_2021127_models.BatchUpdateStoreTextDataRequest,
    ) -> cd_2021127_models.BatchUpdateStoreTextDataResponse:
        """
        @param request: BatchUpdateStoreTextDataRequest
        @return: BatchUpdateStoreTextDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_update_store_text_data_with_options(request, headers, runtime)

    async def batch_update_store_text_data_async(
        self,
        request: cd_2021127_models.BatchUpdateStoreTextDataRequest,
    ) -> cd_2021127_models.BatchUpdateStoreTextDataResponse:
        """
        @param request: BatchUpdateStoreTextDataRequest
        @return: BatchUpdateStoreTextDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_update_store_text_data_with_options_async(request, headers, runtime)

    def create_label_with_options(
        self,
        request: cd_2021127_models.CreateLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.CreateLabelResponse:
        """
        @summary 创建标签
        
        @param request: CreateLabelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabel',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/CreateLabel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.CreateLabelResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.CreateLabelResponse(),
                self.execute(params, req, runtime)
            )

    async def create_label_with_options_async(
        self,
        request: cd_2021127_models.CreateLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.CreateLabelResponse:
        """
        @summary 创建标签
        
        @param request: CreateLabelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabel',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/CreateLabel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.CreateLabelResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.CreateLabelResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_label(
        self,
        request: cd_2021127_models.CreateLabelRequest,
    ) -> cd_2021127_models.CreateLabelResponse:
        """
        @summary 创建标签
        
        @param request: CreateLabelRequest
        @return: CreateLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_label_with_options(request, headers, runtime)

    async def create_label_async(
        self,
        request: cd_2021127_models.CreateLabelRequest,
    ) -> cd_2021127_models.CreateLabelResponse:
        """
        @summary 创建标签
        
        @param request: CreateLabelRequest
        @return: CreateLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_label_with_options_async(request, headers, runtime)

    def create_menu_data_with_options(
        self,
        tmp_req: cd_2021127_models.CreateMenuDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.CreateMenuDataResponse:
        """
        @summary 创建菜单数据
        
        @param tmp_req: CreateMenuDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMenuDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.CreateMenuDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.product_combine_list):
            request.product_combine_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.product_combine_list, 'ProductCombineList', 'json')
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.batch_id):
            body['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.product_combine_list_shrink):
            body['ProductCombineList'] = request.product_combine_list_shrink
        if not UtilClient.is_unset(request.product_container_id):
            body['ProductContainerId'] = request.product_container_id
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMenuData',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/CreateMenuData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.CreateMenuDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.CreateMenuDataResponse(),
                self.execute(params, req, runtime)
            )

    async def create_menu_data_with_options_async(
        self,
        tmp_req: cd_2021127_models.CreateMenuDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.CreateMenuDataResponse:
        """
        @summary 创建菜单数据
        
        @param tmp_req: CreateMenuDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMenuDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.CreateMenuDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.product_combine_list):
            request.product_combine_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.product_combine_list, 'ProductCombineList', 'json')
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.batch_id):
            body['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.product_combine_list_shrink):
            body['ProductCombineList'] = request.product_combine_list_shrink
        if not UtilClient.is_unset(request.product_container_id):
            body['ProductContainerId'] = request.product_container_id
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMenuData',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/CreateMenuData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.CreateMenuDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.CreateMenuDataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_menu_data(
        self,
        request: cd_2021127_models.CreateMenuDataRequest,
    ) -> cd_2021127_models.CreateMenuDataResponse:
        """
        @summary 创建菜单数据
        
        @param request: CreateMenuDataRequest
        @return: CreateMenuDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_menu_data_with_options(request, headers, runtime)

    async def create_menu_data_async(
        self,
        request: cd_2021127_models.CreateMenuDataRequest,
    ) -> cd_2021127_models.CreateMenuDataResponse:
        """
        @summary 创建菜单数据
        
        @param request: CreateMenuDataRequest
        @return: CreateMenuDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_menu_data_with_options_async(request, headers, runtime)

    def create_shop_with_options(
        self,
        tmp_req: cd_2021127_models.CreateShopRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.CreateShopResponse:
        """
        @summary 添加门店
        
        @param tmp_req: CreateShopRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateShopResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.CreateShopShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_list):
            request.shop_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_list, 'ShopList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_list_shrink):
            body['ShopList'] = request.shop_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateShop',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/CreateShop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.CreateShopResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.CreateShopResponse(),
                self.execute(params, req, runtime)
            )

    async def create_shop_with_options_async(
        self,
        tmp_req: cd_2021127_models.CreateShopRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.CreateShopResponse:
        """
        @summary 添加门店
        
        @param tmp_req: CreateShopRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateShopResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.CreateShopShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_list):
            request.shop_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_list, 'ShopList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_list_shrink):
            body['ShopList'] = request.shop_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateShop',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/CreateShop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.CreateShopResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.CreateShopResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_shop(
        self,
        request: cd_2021127_models.CreateShopRequest,
    ) -> cd_2021127_models.CreateShopResponse:
        """
        @summary 添加门店
        
        @param request: CreateShopRequest
        @return: CreateShopResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_shop_with_options(request, headers, runtime)

    async def create_shop_async(
        self,
        request: cd_2021127_models.CreateShopRequest,
    ) -> cd_2021127_models.CreateShopResponse:
        """
        @summary 添加门店
        
        @param request: CreateShopRequest
        @return: CreateShopResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_shop_with_options_async(request, headers, runtime)

    def create_shop_group_with_options(
        self,
        tmp_req: cd_2021127_models.CreateShopGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.CreateShopGroupResponse:
        """
        @param tmp_req: CreateShopGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateShopGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.CreateShopGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_group_list):
            request.shop_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_group_list, 'ShopGroupList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_group_list_shrink):
            body['ShopGroupList'] = request.shop_group_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateShopGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/CreateShopGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.CreateShopGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.CreateShopGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def create_shop_group_with_options_async(
        self,
        tmp_req: cd_2021127_models.CreateShopGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.CreateShopGroupResponse:
        """
        @param tmp_req: CreateShopGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateShopGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.CreateShopGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_group_list):
            request.shop_group_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_group_list, 'ShopGroupList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_group_list_shrink):
            body['ShopGroupList'] = request.shop_group_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateShopGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/CreateShopGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.CreateShopGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.CreateShopGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_shop_group(
        self,
        request: cd_2021127_models.CreateShopGroupRequest,
    ) -> cd_2021127_models.CreateShopGroupResponse:
        """
        @param request: CreateShopGroupRequest
        @return: CreateShopGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_shop_group_with_options(request, headers, runtime)

    async def create_shop_group_async(
        self,
        request: cd_2021127_models.CreateShopGroupRequest,
    ) -> cd_2021127_models.CreateShopGroupResponse:
        """
        @param request: CreateShopGroupRequest
        @return: CreateShopGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_shop_group_with_options_async(request, headers, runtime)

    def create_speech_template_with_options(
        self,
        request: cd_2021127_models.CreateSpeechTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.CreateSpeechTemplateResponse:
        """
        @param request: CreateSpeechTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSpeechTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.contents):
            body['Contents'] = request.contents
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.country):
            body['country'] = request.country
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSpeechTemplate',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/CreateSpeechTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.CreateSpeechTemplateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.CreateSpeechTemplateResponse(),
                self.execute(params, req, runtime)
            )

    async def create_speech_template_with_options_async(
        self,
        request: cd_2021127_models.CreateSpeechTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.CreateSpeechTemplateResponse:
        """
        @param request: CreateSpeechTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSpeechTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.contents):
            body['Contents'] = request.contents
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.country):
            body['country'] = request.country
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSpeechTemplate',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/CreateSpeechTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.CreateSpeechTemplateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.CreateSpeechTemplateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_speech_template(
        self,
        request: cd_2021127_models.CreateSpeechTemplateRequest,
    ) -> cd_2021127_models.CreateSpeechTemplateResponse:
        """
        @param request: CreateSpeechTemplateRequest
        @return: CreateSpeechTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_speech_template_with_options(request, headers, runtime)

    async def create_speech_template_async(
        self,
        request: cd_2021127_models.CreateSpeechTemplateRequest,
    ) -> cd_2021127_models.CreateSpeechTemplateResponse:
        """
        @param request: CreateSpeechTemplateRequest
        @return: CreateSpeechTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_speech_template_with_options_async(request, headers, runtime)

    def delete_label_with_options(
        self,
        request: cd_2021127_models.DeleteLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.DeleteLabelResponse:
        """
        @summary 删除标签
        
        @param request: DeleteLabelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLabel',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/DeleteLabel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.DeleteLabelResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.DeleteLabelResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_label_with_options_async(
        self,
        request: cd_2021127_models.DeleteLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.DeleteLabelResponse:
        """
        @summary 删除标签
        
        @param request: DeleteLabelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLabel',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/DeleteLabel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.DeleteLabelResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.DeleteLabelResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_label(
        self,
        request: cd_2021127_models.DeleteLabelRequest,
    ) -> cd_2021127_models.DeleteLabelResponse:
        """
        @summary 删除标签
        
        @param request: DeleteLabelRequest
        @return: DeleteLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_label_with_options(request, headers, runtime)

    async def delete_label_async(
        self,
        request: cd_2021127_models.DeleteLabelRequest,
    ) -> cd_2021127_models.DeleteLabelResponse:
        """
        @summary 删除标签
        
        @param request: DeleteLabelRequest
        @return: DeleteLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_label_with_options_async(request, headers, runtime)

    def delete_product_image_with_options(
        self,
        tmp_req: cd_2021127_models.DeleteProductImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.DeleteProductImageResponse:
        """
        @param tmp_req: DeleteProductImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProductImageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.DeleteProductImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.product_image_ids):
            request.product_image_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.product_image_ids, 'ProductImageIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_image_ids_shrink):
            body['ProductImageIds'] = request.product_image_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProductImage',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/DeleteProductImage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.DeleteProductImageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.DeleteProductImageResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_product_image_with_options_async(
        self,
        tmp_req: cd_2021127_models.DeleteProductImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.DeleteProductImageResponse:
        """
        @param tmp_req: DeleteProductImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProductImageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.DeleteProductImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.product_image_ids):
            request.product_image_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.product_image_ids, 'ProductImageIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_image_ids_shrink):
            body['ProductImageIds'] = request.product_image_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProductImage',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/DeleteProductImage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.DeleteProductImageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.DeleteProductImageResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_product_image(
        self,
        request: cd_2021127_models.DeleteProductImageRequest,
    ) -> cd_2021127_models.DeleteProductImageResponse:
        """
        @param request: DeleteProductImageRequest
        @return: DeleteProductImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_product_image_with_options(request, headers, runtime)

    async def delete_product_image_async(
        self,
        request: cd_2021127_models.DeleteProductImageRequest,
    ) -> cd_2021127_models.DeleteProductImageResponse:
        """
        @param request: DeleteProductImageRequest
        @return: DeleteProductImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_product_image_with_options_async(request, headers, runtime)

    def delete_shop_with_options(
        self,
        request: cd_2021127_models.DeleteShopRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.DeleteShopResponse:
        """
        @param request: DeleteShopRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteShopResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_id):
            body['ShopId'] = request.shop_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteShop',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/DeleteShop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.DeleteShopResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.DeleteShopResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_shop_with_options_async(
        self,
        request: cd_2021127_models.DeleteShopRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.DeleteShopResponse:
        """
        @param request: DeleteShopRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteShopResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_id):
            body['ShopId'] = request.shop_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteShop',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/DeleteShop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.DeleteShopResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.DeleteShopResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_shop(
        self,
        request: cd_2021127_models.DeleteShopRequest,
    ) -> cd_2021127_models.DeleteShopResponse:
        """
        @param request: DeleteShopRequest
        @return: DeleteShopResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_shop_with_options(request, headers, runtime)

    async def delete_shop_async(
        self,
        request: cd_2021127_models.DeleteShopRequest,
    ) -> cd_2021127_models.DeleteShopResponse:
        """
        @param request: DeleteShopRequest
        @return: DeleteShopResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_shop_with_options_async(request, headers, runtime)

    def delete_shop_group_with_options(
        self,
        request: cd_2021127_models.DeleteShopGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.DeleteShopGroupResponse:
        """
        @param request: DeleteShopGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteShopGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteShopGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/DeleteShopGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.DeleteShopGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.DeleteShopGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_shop_group_with_options_async(
        self,
        request: cd_2021127_models.DeleteShopGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.DeleteShopGroupResponse:
        """
        @param request: DeleteShopGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteShopGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteShopGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/DeleteShopGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.DeleteShopGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.DeleteShopGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_shop_group(
        self,
        request: cd_2021127_models.DeleteShopGroupRequest,
    ) -> cd_2021127_models.DeleteShopGroupResponse:
        """
        @param request: DeleteShopGroupRequest
        @return: DeleteShopGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_shop_group_with_options(request, headers, runtime)

    async def delete_shop_group_async(
        self,
        request: cd_2021127_models.DeleteShopGroupRequest,
    ) -> cd_2021127_models.DeleteShopGroupResponse:
        """
        @param request: DeleteShopGroupRequest
        @return: DeleteShopGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_shop_group_with_options_async(request, headers, runtime)

    def delete_speech_template_with_options(
        self,
        request: cd_2021127_models.DeleteSpeechTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.DeleteSpeechTemplateResponse:
        """
        @param request: DeleteSpeechTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSpeechTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.country):
            body['country'] = request.country
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSpeechTemplate',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/DeleteSpeechTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.DeleteSpeechTemplateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.DeleteSpeechTemplateResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_speech_template_with_options_async(
        self,
        request: cd_2021127_models.DeleteSpeechTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.DeleteSpeechTemplateResponse:
        """
        @param request: DeleteSpeechTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSpeechTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.country):
            body['country'] = request.country
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSpeechTemplate',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/DeleteSpeechTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.DeleteSpeechTemplateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.DeleteSpeechTemplateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_speech_template(
        self,
        request: cd_2021127_models.DeleteSpeechTemplateRequest,
    ) -> cd_2021127_models.DeleteSpeechTemplateResponse:
        """
        @param request: DeleteSpeechTemplateRequest
        @return: DeleteSpeechTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_speech_template_with_options(request, headers, runtime)

    async def delete_speech_template_async(
        self,
        request: cd_2021127_models.DeleteSpeechTemplateRequest,
    ) -> cd_2021127_models.DeleteSpeechTemplateResponse:
        """
        @param request: DeleteSpeechTemplateRequest
        @return: DeleteSpeechTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_speech_template_with_options_async(request, headers, runtime)

    def get_menu_data_status_with_options(
        self,
        request: cd_2021127_models.GetMenuDataStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.GetMenuDataStatusResponse:
        """
        @summary 查询菜单数据状态
        
        @param request: GetMenuDataStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMenuDataStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.batch_id):
            body['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.product_container_id):
            body['ProductContainerId'] = request.product_container_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMenuDataStatus',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/GetMenuDataStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.GetMenuDataStatusResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.GetMenuDataStatusResponse(),
                self.execute(params, req, runtime)
            )

    async def get_menu_data_status_with_options_async(
        self,
        request: cd_2021127_models.GetMenuDataStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.GetMenuDataStatusResponse:
        """
        @summary 查询菜单数据状态
        
        @param request: GetMenuDataStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMenuDataStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.batch_id):
            body['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.product_container_id):
            body['ProductContainerId'] = request.product_container_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMenuDataStatus',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/GetMenuDataStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.GetMenuDataStatusResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.GetMenuDataStatusResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_menu_data_status(
        self,
        request: cd_2021127_models.GetMenuDataStatusRequest,
    ) -> cd_2021127_models.GetMenuDataStatusResponse:
        """
        @summary 查询菜单数据状态
        
        @param request: GetMenuDataStatusRequest
        @return: GetMenuDataStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_menu_data_status_with_options(request, headers, runtime)

    async def get_menu_data_status_async(
        self,
        request: cd_2021127_models.GetMenuDataStatusRequest,
    ) -> cd_2021127_models.GetMenuDataStatusResponse:
        """
        @summary 查询菜单数据状态
        
        @param request: GetMenuDataStatusRequest
        @return: GetMenuDataStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_menu_data_status_with_options_async(request, headers, runtime)

    def get_shop_with_options(
        self,
        request: cd_2021127_models.GetShopRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.GetShopResponse:
        """
        @param request: GetShopRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetShopResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_id):
            body['ShopId'] = request.shop_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShop',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/GetShop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.GetShopResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.GetShopResponse(),
                self.execute(params, req, runtime)
            )

    async def get_shop_with_options_async(
        self,
        request: cd_2021127_models.GetShopRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.GetShopResponse:
        """
        @param request: GetShopRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetShopResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_id):
            body['ShopId'] = request.shop_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShop',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/GetShop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.GetShopResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.GetShopResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_shop(
        self,
        request: cd_2021127_models.GetShopRequest,
    ) -> cd_2021127_models.GetShopResponse:
        """
        @param request: GetShopRequest
        @return: GetShopResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_shop_with_options(request, headers, runtime)

    async def get_shop_async(
        self,
        request: cd_2021127_models.GetShopRequest,
    ) -> cd_2021127_models.GetShopResponse:
        """
        @param request: GetShopRequest
        @return: GetShopResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_shop_with_options_async(request, headers, runtime)

    def get_shop_group_with_options(
        self,
        request: cd_2021127_models.GetShopGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.GetShopGroupResponse:
        """
        @param request: GetShopGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetShopGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShopGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/GetShopGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.GetShopGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.GetShopGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def get_shop_group_with_options_async(
        self,
        request: cd_2021127_models.GetShopGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.GetShopGroupResponse:
        """
        @param request: GetShopGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetShopGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetShopGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/GetShopGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.GetShopGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.GetShopGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_shop_group(
        self,
        request: cd_2021127_models.GetShopGroupRequest,
    ) -> cd_2021127_models.GetShopGroupResponse:
        """
        @param request: GetShopGroupRequest
        @return: GetShopGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_shop_group_with_options(request, headers, runtime)

    async def get_shop_group_async(
        self,
        request: cd_2021127_models.GetShopGroupRequest,
    ) -> cd_2021127_models.GetShopGroupResponse:
        """
        @param request: GetShopGroupRequest
        @return: GetShopGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_shop_group_with_options_async(request, headers, runtime)

    def get_speech_template_with_options(
        self,
        request: cd_2021127_models.GetSpeechTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.GetSpeechTemplateResponse:
        """
        @param request: GetSpeechTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSpeechTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.country):
            body['country'] = request.country
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSpeechTemplate',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/GetSpeechTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.GetSpeechTemplateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.GetSpeechTemplateResponse(),
                self.execute(params, req, runtime)
            )

    async def get_speech_template_with_options_async(
        self,
        request: cd_2021127_models.GetSpeechTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.GetSpeechTemplateResponse:
        """
        @param request: GetSpeechTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSpeechTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.country):
            body['country'] = request.country
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSpeechTemplate',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/GetSpeechTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.GetSpeechTemplateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.GetSpeechTemplateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_speech_template(
        self,
        request: cd_2021127_models.GetSpeechTemplateRequest,
    ) -> cd_2021127_models.GetSpeechTemplateResponse:
        """
        @param request: GetSpeechTemplateRequest
        @return: GetSpeechTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_speech_template_with_options(request, headers, runtime)

    async def get_speech_template_async(
        self,
        request: cd_2021127_models.GetSpeechTemplateRequest,
    ) -> cd_2021127_models.GetSpeechTemplateResponse:
        """
        @param request: GetSpeechTemplateRequest
        @return: GetSpeechTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_speech_template_with_options_async(request, headers, runtime)

    def list_menu_data_with_options(
        self,
        request: cd_2021127_models.ListMenuDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.ListMenuDataResponse:
        """
        @summary 列举菜单数据
        
        @param request: ListMenuDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMenuDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.batch_id):
            body['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.create_request_id):
            body['CreateRequestId'] = request.create_request_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_container_id):
            body['ProductContainerId'] = request.product_container_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMenuData',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/ListMenuData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.ListMenuDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.ListMenuDataResponse(),
                self.execute(params, req, runtime)
            )

    async def list_menu_data_with_options_async(
        self,
        request: cd_2021127_models.ListMenuDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.ListMenuDataResponse:
        """
        @summary 列举菜单数据
        
        @param request: ListMenuDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMenuDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.batch_id):
            body['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.create_request_id):
            body['CreateRequestId'] = request.create_request_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_container_id):
            body['ProductContainerId'] = request.product_container_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMenuData',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/ListMenuData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.ListMenuDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.ListMenuDataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_menu_data(
        self,
        request: cd_2021127_models.ListMenuDataRequest,
    ) -> cd_2021127_models.ListMenuDataResponse:
        """
        @summary 列举菜单数据
        
        @param request: ListMenuDataRequest
        @return: ListMenuDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_menu_data_with_options(request, headers, runtime)

    async def list_menu_data_async(
        self,
        request: cd_2021127_models.ListMenuDataRequest,
    ) -> cd_2021127_models.ListMenuDataResponse:
        """
        @summary 列举菜单数据
        
        @param request: ListMenuDataRequest
        @return: ListMenuDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_menu_data_with_options_async(request, headers, runtime)

    def list_shop_with_options(
        self,
        tmp_req: cd_2021127_models.ListShopRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.ListShopResponse:
        """
        @param tmp_req: ListShopRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListShopResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.ListShopShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_group_ids):
            request.shop_group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_group_ids, 'ShopGroupIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.shop_group_ids_shrink):
            body['ShopGroupIds'] = request.shop_group_ids_shrink
        if not UtilClient.is_unset(request.shop_id):
            body['ShopId'] = request.shop_id
        if not UtilClient.is_unset(request.shop_name):
            body['ShopName'] = request.shop_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListShop',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/ListShop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.ListShopResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.ListShopResponse(),
                self.execute(params, req, runtime)
            )

    async def list_shop_with_options_async(
        self,
        tmp_req: cd_2021127_models.ListShopRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.ListShopResponse:
        """
        @param tmp_req: ListShopRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListShopResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.ListShopShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_group_ids):
            request.shop_group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_group_ids, 'ShopGroupIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.shop_group_ids_shrink):
            body['ShopGroupIds'] = request.shop_group_ids_shrink
        if not UtilClient.is_unset(request.shop_id):
            body['ShopId'] = request.shop_id
        if not UtilClient.is_unset(request.shop_name):
            body['ShopName'] = request.shop_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListShop',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/ListShop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.ListShopResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.ListShopResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_shop(
        self,
        request: cd_2021127_models.ListShopRequest,
    ) -> cd_2021127_models.ListShopResponse:
        """
        @param request: ListShopRequest
        @return: ListShopResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_shop_with_options(request, headers, runtime)

    async def list_shop_async(
        self,
        request: cd_2021127_models.ListShopRequest,
    ) -> cd_2021127_models.ListShopResponse:
        """
        @param request: ListShopRequest
        @return: ListShopResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_shop_with_options_async(request, headers, runtime)

    def list_shop_group_with_options(
        self,
        request: cd_2021127_models.ListShopGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.ListShopGroupResponse:
        """
        @param request: ListShopGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListShopGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        if not UtilClient.is_unset(request.shop_group_name):
            body['ShopGroupName'] = request.shop_group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListShopGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/ListShopGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.ListShopGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.ListShopGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def list_shop_group_with_options_async(
        self,
        request: cd_2021127_models.ListShopGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.ListShopGroupResponse:
        """
        @param request: ListShopGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListShopGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        if not UtilClient.is_unset(request.shop_group_name):
            body['ShopGroupName'] = request.shop_group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListShopGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/ListShopGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.ListShopGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.ListShopGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_shop_group(
        self,
        request: cd_2021127_models.ListShopGroupRequest,
    ) -> cd_2021127_models.ListShopGroupResponse:
        """
        @param request: ListShopGroupRequest
        @return: ListShopGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_shop_group_with_options(request, headers, runtime)

    async def list_shop_group_async(
        self,
        request: cd_2021127_models.ListShopGroupRequest,
    ) -> cd_2021127_models.ListShopGroupResponse:
        """
        @param request: ListShopGroupRequest
        @return: ListShopGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_shop_group_with_options_async(request, headers, runtime)

    def push_store_speech_data_with_options(
        self,
        tmp_req: cd_2021127_models.PushStoreSpeechDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.PushStoreSpeechDataResponse:
        """
        @param tmp_req: PushStoreSpeechDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushStoreSpeechDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.PushStoreSpeechDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.speech):
            request.speech_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.speech, 'Speech', 'json')
        body = {}
        if not UtilClient.is_unset(request.speech_shrink):
            body['Speech'] = request.speech_shrink
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.country):
            body['country'] = request.country
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushStoreSpeechData',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/PushStoreSpeechData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.PushStoreSpeechDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.PushStoreSpeechDataResponse(),
                self.execute(params, req, runtime)
            )

    async def push_store_speech_data_with_options_async(
        self,
        tmp_req: cd_2021127_models.PushStoreSpeechDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.PushStoreSpeechDataResponse:
        """
        @param tmp_req: PushStoreSpeechDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushStoreSpeechDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.PushStoreSpeechDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.speech):
            request.speech_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.speech, 'Speech', 'json')
        body = {}
        if not UtilClient.is_unset(request.speech_shrink):
            body['Speech'] = request.speech_shrink
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.country):
            body['country'] = request.country
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushStoreSpeechData',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/PushStoreSpeechData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.PushStoreSpeechDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.PushStoreSpeechDataResponse(),
                await self.execute_async(params, req, runtime)
            )

    def push_store_speech_data(
        self,
        request: cd_2021127_models.PushStoreSpeechDataRequest,
    ) -> cd_2021127_models.PushStoreSpeechDataResponse:
        """
        @param request: PushStoreSpeechDataRequest
        @return: PushStoreSpeechDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_store_speech_data_with_options(request, headers, runtime)

    async def push_store_speech_data_async(
        self,
        request: cd_2021127_models.PushStoreSpeechDataRequest,
    ) -> cd_2021127_models.PushStoreSpeechDataResponse:
        """
        @param request: PushStoreSpeechDataRequest
        @return: PushStoreSpeechDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_store_speech_data_with_options_async(request, headers, runtime)

    def query_device_data_list_with_options(
        self,
        request: cd_2021127_models.QueryDeviceDataListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.QueryDeviceDataListResponse:
        """
        @param request: QueryDeviceDataListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDeviceDataListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDeviceDataList',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/QueryDeviceDataList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.QueryDeviceDataListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.QueryDeviceDataListResponse(),
                self.execute(params, req, runtime)
            )

    async def query_device_data_list_with_options_async(
        self,
        request: cd_2021127_models.QueryDeviceDataListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.QueryDeviceDataListResponse:
        """
        @param request: QueryDeviceDataListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDeviceDataListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDeviceDataList',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/QueryDeviceDataList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.QueryDeviceDataListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.QueryDeviceDataListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_device_data_list(
        self,
        request: cd_2021127_models.QueryDeviceDataListRequest,
    ) -> cd_2021127_models.QueryDeviceDataListResponse:
        """
        @param request: QueryDeviceDataListRequest
        @return: QueryDeviceDataListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_device_data_list_with_options(request, headers, runtime)

    async def query_device_data_list_async(
        self,
        request: cd_2021127_models.QueryDeviceDataListRequest,
    ) -> cd_2021127_models.QueryDeviceDataListResponse:
        """
        @param request: QueryDeviceDataListRequest
        @return: QueryDeviceDataListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_device_data_list_with_options_async(request, headers, runtime)

    def query_fault_brief_list_with_options(
        self,
        tmp_req: cd_2021127_models.QueryFaultBriefListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.QueryFaultBriefListResponse:
        """
        @param tmp_req: QueryFaultBriefListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFaultBriefListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.QueryFaultBriefListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryFaultBriefList',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/QueryFaultBriefList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.QueryFaultBriefListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.QueryFaultBriefListResponse(),
                self.execute(params, req, runtime)
            )

    async def query_fault_brief_list_with_options_async(
        self,
        tmp_req: cd_2021127_models.QueryFaultBriefListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.QueryFaultBriefListResponse:
        """
        @param tmp_req: QueryFaultBriefListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFaultBriefListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.QueryFaultBriefListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryFaultBriefList',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/QueryFaultBriefList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.QueryFaultBriefListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.QueryFaultBriefListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_fault_brief_list(
        self,
        request: cd_2021127_models.QueryFaultBriefListRequest,
    ) -> cd_2021127_models.QueryFaultBriefListResponse:
        """
        @param request: QueryFaultBriefListRequest
        @return: QueryFaultBriefListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_fault_brief_list_with_options(request, headers, runtime)

    async def query_fault_brief_list_async(
        self,
        request: cd_2021127_models.QueryFaultBriefListRequest,
    ) -> cd_2021127_models.QueryFaultBriefListResponse:
        """
        @param request: QueryFaultBriefListRequest
        @return: QueryFaultBriefListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_fault_brief_list_with_options_async(request, headers, runtime)

    def query_fault_device_list_with_options(
        self,
        tmp_req: cd_2021127_models.QueryFaultDeviceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.QueryFaultDeviceListResponse:
        """
        @param tmp_req: QueryFaultDeviceListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFaultDeviceListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.QueryFaultDeviceListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.daily_online_time):
            body['DailyOnlineTime'] = request.daily_online_time
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.fault_type):
            body['FaultType'] = request.fault_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryFaultDeviceList',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/QueryFaultDeviceList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.QueryFaultDeviceListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.QueryFaultDeviceListResponse(),
                self.execute(params, req, runtime)
            )

    async def query_fault_device_list_with_options_async(
        self,
        tmp_req: cd_2021127_models.QueryFaultDeviceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.QueryFaultDeviceListResponse:
        """
        @param tmp_req: QueryFaultDeviceListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFaultDeviceListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.QueryFaultDeviceListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.daily_online_time):
            body['DailyOnlineTime'] = request.daily_online_time
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.fault_type):
            body['FaultType'] = request.fault_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryFaultDeviceList',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/QueryFaultDeviceList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.QueryFaultDeviceListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.QueryFaultDeviceListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_fault_device_list(
        self,
        request: cd_2021127_models.QueryFaultDeviceListRequest,
    ) -> cd_2021127_models.QueryFaultDeviceListResponse:
        """
        @param request: QueryFaultDeviceListRequest
        @return: QueryFaultDeviceListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_fault_device_list_with_options(request, headers, runtime)

    async def query_fault_device_list_async(
        self,
        request: cd_2021127_models.QueryFaultDeviceListRequest,
    ) -> cd_2021127_models.QueryFaultDeviceListResponse:
        """
        @param request: QueryFaultDeviceListRequest
        @return: QueryFaultDeviceListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_fault_device_list_with_options_async(request, headers, runtime)

    def query_label_with_options(
        self,
        request: cd_2021127_models.QueryLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.QueryLabelResponse:
        """
        @summary 查询标签
        
        @param request: QueryLabelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryLabel',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/QueryLabel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.QueryLabelResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.QueryLabelResponse(),
                self.execute(params, req, runtime)
            )

    async def query_label_with_options_async(
        self,
        request: cd_2021127_models.QueryLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.QueryLabelResponse:
        """
        @summary 查询标签
        
        @param request: QueryLabelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryLabel',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/QueryLabel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.QueryLabelResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.QueryLabelResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_label(
        self,
        request: cd_2021127_models.QueryLabelRequest,
    ) -> cd_2021127_models.QueryLabelResponse:
        """
        @summary 查询标签
        
        @param request: QueryLabelRequest
        @return: QueryLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_label_with_options(request, headers, runtime)

    async def query_label_async(
        self,
        request: cd_2021127_models.QueryLabelRequest,
    ) -> cd_2021127_models.QueryLabelResponse:
        """
        @summary 查询标签
        
        @param request: QueryLabelRequest
        @return: QueryLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_label_with_options_async(request, headers, runtime)

    def query_operation_index_with_options(
        self,
        tmp_req: cd_2021127_models.QueryOperationIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.QueryOperationIndexResponse:
        """
        @param tmp_req: QueryOperationIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOperationIndexResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.QueryOperationIndexShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOperationIndex',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/QueryOperationIndex',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.QueryOperationIndexResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.QueryOperationIndexResponse(),
                self.execute(params, req, runtime)
            )

    async def query_operation_index_with_options_async(
        self,
        tmp_req: cd_2021127_models.QueryOperationIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.QueryOperationIndexResponse:
        """
        @param tmp_req: QueryOperationIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOperationIndexResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.QueryOperationIndexShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOperationIndex',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/QueryOperationIndex',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.QueryOperationIndexResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.QueryOperationIndexResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_operation_index(
        self,
        request: cd_2021127_models.QueryOperationIndexRequest,
    ) -> cd_2021127_models.QueryOperationIndexResponse:
        """
        @param request: QueryOperationIndexRequest
        @return: QueryOperationIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_operation_index_with_options(request, headers, runtime)

    async def query_operation_index_async(
        self,
        request: cd_2021127_models.QueryOperationIndexRequest,
    ) -> cd_2021127_models.QueryOperationIndexResponse:
        """
        @param request: QueryOperationIndexRequest
        @return: QueryOperationIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_operation_index_with_options_async(request, headers, runtime)

    def query_shop_index_with_options(
        self,
        tmp_req: cd_2021127_models.QueryShopIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.QueryShopIndexResponse:
        """
        @param tmp_req: QueryShopIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryShopIndexResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.QueryShopIndexShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryShopIndex',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/QueryShopIndex',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.QueryShopIndexResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.QueryShopIndexResponse(),
                self.execute(params, req, runtime)
            )

    async def query_shop_index_with_options_async(
        self,
        tmp_req: cd_2021127_models.QueryShopIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.QueryShopIndexResponse:
        """
        @param tmp_req: QueryShopIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryShopIndexResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.QueryShopIndexShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryShopIndex',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/QueryShopIndex',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.QueryShopIndexResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.QueryShopIndexResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_shop_index(
        self,
        request: cd_2021127_models.QueryShopIndexRequest,
    ) -> cd_2021127_models.QueryShopIndexResponse:
        """
        @param request: QueryShopIndexRequest
        @return: QueryShopIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_shop_index_with_options(request, headers, runtime)

    async def query_shop_index_async(
        self,
        request: cd_2021127_models.QueryShopIndexRequest,
    ) -> cd_2021127_models.QueryShopIndexResponse:
        """
        @param request: QueryShopIndexRequest
        @return: QueryShopIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_shop_index_with_options_async(request, headers, runtime)

    def query_ticket_list_with_options(
        self,
        tmp_req: cd_2021127_models.QueryTicketListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.QueryTicketListResponse:
        """
        @param tmp_req: QueryTicketListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTicketListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.QueryTicketListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        if not UtilClient.is_unset(tmp_req.ticket_id_list):
            request.ticket_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ticket_id_list, 'TicketIdList', 'json')
        if not UtilClient.is_unset(tmp_req.ticket_type_list):
            request.ticket_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ticket_type_list, 'TicketTypeList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.ticket_id_list_shrink):
            body['TicketIdList'] = request.ticket_id_list_shrink
        if not UtilClient.is_unset(request.ticket_type_list_shrink):
            body['TicketTypeList'] = request.ticket_type_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTicketList',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/QueryTicketList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.QueryTicketListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.QueryTicketListResponse(),
                self.execute(params, req, runtime)
            )

    async def query_ticket_list_with_options_async(
        self,
        tmp_req: cd_2021127_models.QueryTicketListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.QueryTicketListResponse:
        """
        @param tmp_req: QueryTicketListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTicketListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.QueryTicketListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        if not UtilClient.is_unset(tmp_req.ticket_id_list):
            request.ticket_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ticket_id_list, 'TicketIdList', 'json')
        if not UtilClient.is_unset(tmp_req.ticket_type_list):
            request.ticket_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ticket_type_list, 'TicketTypeList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.ticket_id_list_shrink):
            body['TicketIdList'] = request.ticket_id_list_shrink
        if not UtilClient.is_unset(request.ticket_type_list_shrink):
            body['TicketTypeList'] = request.ticket_type_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTicketList',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/QueryTicketList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.QueryTicketListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.QueryTicketListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def query_ticket_list(
        self,
        request: cd_2021127_models.QueryTicketListRequest,
    ) -> cd_2021127_models.QueryTicketListResponse:
        """
        @param request: QueryTicketListRequest
        @return: QueryTicketListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_ticket_list_with_options(request, headers, runtime)

    async def query_ticket_list_async(
        self,
        request: cd_2021127_models.QueryTicketListRequest,
    ) -> cd_2021127_models.QueryTicketListResponse:
        """
        @param request: QueryTicketListRequest
        @return: QueryTicketListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_ticket_list_with_options_async(request, headers, runtime)

    def remove_shop_from_group_with_options(
        self,
        tmp_req: cd_2021127_models.RemoveShopFromGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.RemoveShopFromGroupResponse:
        """
        @summary 门店组移除门店
        
        @param tmp_req: RemoveShopFromGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveShopFromGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.RemoveShopFromGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveShopFromGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/RemoveShopFromGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.RemoveShopFromGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.RemoveShopFromGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def remove_shop_from_group_with_options_async(
        self,
        tmp_req: cd_2021127_models.RemoveShopFromGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.RemoveShopFromGroupResponse:
        """
        @summary 门店组移除门店
        
        @param tmp_req: RemoveShopFromGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveShopFromGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.RemoveShopFromGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveShopFromGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/RemoveShopFromGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.RemoveShopFromGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.RemoveShopFromGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def remove_shop_from_group(
        self,
        request: cd_2021127_models.RemoveShopFromGroupRequest,
    ) -> cd_2021127_models.RemoveShopFromGroupResponse:
        """
        @summary 门店组移除门店
        
        @param request: RemoveShopFromGroupRequest
        @return: RemoveShopFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_shop_from_group_with_options(request, headers, runtime)

    async def remove_shop_from_group_async(
        self,
        request: cd_2021127_models.RemoveShopFromGroupRequest,
    ) -> cd_2021127_models.RemoveShopFromGroupResponse:
        """
        @summary 门店组移除门店
        
        @param request: RemoveShopFromGroupRequest
        @return: RemoveShopFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_shop_from_group_with_options_async(request, headers, runtime)

    def remove_shops_from_group_with_options(
        self,
        tmp_req: cd_2021127_models.RemoveShopsFromGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.RemoveShopsFromGroupResponse:
        """
        @summary 门店组移除门店
        
        @param tmp_req: RemoveShopsFromGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveShopsFromGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.RemoveShopsFromGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveShopsFromGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/RemoveShopsFromGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.RemoveShopsFromGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.RemoveShopsFromGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def remove_shops_from_group_with_options_async(
        self,
        tmp_req: cd_2021127_models.RemoveShopsFromGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.RemoveShopsFromGroupResponse:
        """
        @summary 门店组移除门店
        
        @param tmp_req: RemoveShopsFromGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveShopsFromGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.RemoveShopsFromGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_id_list):
            request.shop_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_id_list, 'ShopIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        if not UtilClient.is_unset(request.shop_id_list_shrink):
            body['ShopIdList'] = request.shop_id_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveShopsFromGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/RemoveShopsFromGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.RemoveShopsFromGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.RemoveShopsFromGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def remove_shops_from_group(
        self,
        request: cd_2021127_models.RemoveShopsFromGroupRequest,
    ) -> cd_2021127_models.RemoveShopsFromGroupResponse:
        """
        @summary 门店组移除门店
        
        @param request: RemoveShopsFromGroupRequest
        @return: RemoveShopsFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_shops_from_group_with_options(request, headers, runtime)

    async def remove_shops_from_group_async(
        self,
        request: cd_2021127_models.RemoveShopsFromGroupRequest,
    ) -> cd_2021127_models.RemoveShopsFromGroupResponse:
        """
        @summary 门店组移除门店
        
        @param request: RemoveShopsFromGroupRequest
        @return: RemoveShopsFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_shops_from_group_with_options_async(request, headers, runtime)

    def update_label_with_options(
        self,
        request: cd_2021127_models.UpdateLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.UpdateLabelResponse:
        """
        @summary 更新标签
        
        @param request: UpdateLabelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLabel',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/UpdateLabel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.UpdateLabelResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.UpdateLabelResponse(),
                self.execute(params, req, runtime)
            )

    async def update_label_with_options_async(
        self,
        request: cd_2021127_models.UpdateLabelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.UpdateLabelResponse:
        """
        @summary 更新标签
        
        @param request: UpdateLabelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLabelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLabel',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/UpdateLabel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.UpdateLabelResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.UpdateLabelResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_label(
        self,
        request: cd_2021127_models.UpdateLabelRequest,
    ) -> cd_2021127_models.UpdateLabelResponse:
        """
        @summary 更新标签
        
        @param request: UpdateLabelRequest
        @return: UpdateLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_label_with_options(request, headers, runtime)

    async def update_label_async(
        self,
        request: cd_2021127_models.UpdateLabelRequest,
    ) -> cd_2021127_models.UpdateLabelResponse:
        """
        @summary 更新标签
        
        @param request: UpdateLabelRequest
        @return: UpdateLabelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_label_with_options_async(request, headers, runtime)

    def update_shop_with_options(
        self,
        tmp_req: cd_2021127_models.UpdateShopRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.UpdateShopResponse:
        """
        @param tmp_req: UpdateShopRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateShopResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.UpdateShopShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_group_ids):
            request.shop_group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_group_ids, 'ShopGroupIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.business_status):
            body['BusinessStatus'] = request.business_status
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.latitude):
            body['Latitude'] = request.latitude
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.longitude):
            body['Longitude'] = request.longitude
        if not UtilClient.is_unset(request.region_address):
            body['RegionAddress'] = request.region_address
        if not UtilClient.is_unset(request.region_code):
            body['RegionCode'] = request.region_code
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.shop_group_ids_shrink):
            body['ShopGroupIds'] = request.shop_group_ids_shrink
        if not UtilClient.is_unset(request.shop_id):
            body['ShopId'] = request.shop_id
        if not UtilClient.is_unset(request.shop_name):
            body['ShopName'] = request.shop_name
        if not UtilClient.is_unset(request.weekdays_end_time):
            body['WeekdaysEndTime'] = request.weekdays_end_time
        if not UtilClient.is_unset(request.weekdays_start_time):
            body['WeekdaysStartTime'] = request.weekdays_start_time
        if not UtilClient.is_unset(request.weekend_end_time):
            body['WeekendEndTime'] = request.weekend_end_time
        if not UtilClient.is_unset(request.weekend_start_time):
            body['WeekendStartTime'] = request.weekend_start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateShop',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/UpdateShop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.UpdateShopResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.UpdateShopResponse(),
                self.execute(params, req, runtime)
            )

    async def update_shop_with_options_async(
        self,
        tmp_req: cd_2021127_models.UpdateShopRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.UpdateShopResponse:
        """
        @param tmp_req: UpdateShopRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateShopResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cd_2021127_models.UpdateShopShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.shop_group_ids):
            request.shop_group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shop_group_ids, 'ShopGroupIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.business_status):
            body['BusinessStatus'] = request.business_status
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.latitude):
            body['Latitude'] = request.latitude
        if not UtilClient.is_unset(request.location):
            body['Location'] = request.location
        if not UtilClient.is_unset(request.longitude):
            body['Longitude'] = request.longitude
        if not UtilClient.is_unset(request.region_address):
            body['RegionAddress'] = request.region_address
        if not UtilClient.is_unset(request.region_code):
            body['RegionCode'] = request.region_code
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.shop_group_ids_shrink):
            body['ShopGroupIds'] = request.shop_group_ids_shrink
        if not UtilClient.is_unset(request.shop_id):
            body['ShopId'] = request.shop_id
        if not UtilClient.is_unset(request.shop_name):
            body['ShopName'] = request.shop_name
        if not UtilClient.is_unset(request.weekdays_end_time):
            body['WeekdaysEndTime'] = request.weekdays_end_time
        if not UtilClient.is_unset(request.weekdays_start_time):
            body['WeekdaysStartTime'] = request.weekdays_start_time
        if not UtilClient.is_unset(request.weekend_end_time):
            body['WeekendEndTime'] = request.weekend_end_time
        if not UtilClient.is_unset(request.weekend_start_time):
            body['WeekendStartTime'] = request.weekend_start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateShop',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/UpdateShop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.UpdateShopResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.UpdateShopResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_shop(
        self,
        request: cd_2021127_models.UpdateShopRequest,
    ) -> cd_2021127_models.UpdateShopResponse:
        """
        @param request: UpdateShopRequest
        @return: UpdateShopResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_shop_with_options(request, headers, runtime)

    async def update_shop_async(
        self,
        request: cd_2021127_models.UpdateShopRequest,
    ) -> cd_2021127_models.UpdateShopResponse:
        """
        @param request: UpdateShopRequest
        @return: UpdateShopResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_shop_with_options_async(request, headers, runtime)

    def update_shop_group_with_options(
        self,
        request: cd_2021127_models.UpdateShopGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.UpdateShopGroupResponse:
        """
        @param request: UpdateShopGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateShopGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        if not UtilClient.is_unset(request.shop_group_name):
            body['ShopGroupName'] = request.shop_group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateShopGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/UpdateShopGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.UpdateShopGroupResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.UpdateShopGroupResponse(),
                self.execute(params, req, runtime)
            )

    async def update_shop_group_with_options_async(
        self,
        request: cd_2021127_models.UpdateShopGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.UpdateShopGroupResponse:
        """
        @param request: UpdateShopGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateShopGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.country):
            body['Country'] = request.country
        if not UtilClient.is_unset(request.shop_group_id):
            body['ShopGroupId'] = request.shop_group_id
        if not UtilClient.is_unset(request.shop_group_name):
            body['ShopGroupName'] = request.shop_group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateShopGroup',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/UpdateShopGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.UpdateShopGroupResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.UpdateShopGroupResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_shop_group(
        self,
        request: cd_2021127_models.UpdateShopGroupRequest,
    ) -> cd_2021127_models.UpdateShopGroupResponse:
        """
        @param request: UpdateShopGroupRequest
        @return: UpdateShopGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_shop_group_with_options(request, headers, runtime)

    async def update_shop_group_async(
        self,
        request: cd_2021127_models.UpdateShopGroupRequest,
    ) -> cd_2021127_models.UpdateShopGroupResponse:
        """
        @param request: UpdateShopGroupRequest
        @return: UpdateShopGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_shop_group_with_options_async(request, headers, runtime)

    def update_speech_template_with_options(
        self,
        request: cd_2021127_models.UpdateSpeechTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.UpdateSpeechTemplateResponse:
        """
        @param request: UpdateSpeechTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSpeechTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.contents):
            body['Contents'] = request.contents
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.country):
            body['country'] = request.country
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSpeechTemplate',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/UpdateSpeechTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.UpdateSpeechTemplateResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.UpdateSpeechTemplateResponse(),
                self.execute(params, req, runtime)
            )

    async def update_speech_template_with_options_async(
        self,
        request: cd_2021127_models.UpdateSpeechTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cd_2021127_models.UpdateSpeechTemplateResponse:
        """
        @param request: UpdateSpeechTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSpeechTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.contents):
            body['Contents'] = request.contents
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.country):
            body['country'] = request.country
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSpeechTemplate',
            version='2021-12-7',
            protocol='HTTPS',
            pathname=f'/UpdateSpeechTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                cd_2021127_models.UpdateSpeechTemplateResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                cd_2021127_models.UpdateSpeechTemplateResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_speech_template(
        self,
        request: cd_2021127_models.UpdateSpeechTemplateRequest,
    ) -> cd_2021127_models.UpdateSpeechTemplateResponse:
        """
        @param request: UpdateSpeechTemplateRequest
        @return: UpdateSpeechTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_speech_template_with_options(request, headers, runtime)

    async def update_speech_template_async(
        self,
        request: cd_2021127_models.UpdateSpeechTemplateRequest,
    ) -> cd_2021127_models.UpdateSpeechTemplateResponse:
        """
        @param request: UpdateSpeechTemplateRequest
        @return: UpdateSpeechTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_speech_template_with_options_async(request, headers, runtime)
