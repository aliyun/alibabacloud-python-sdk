# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aidge20260428 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('aidge', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def asset_optimize_lite_with_options(
        self,
        request: main_models.AssetOptimizeLiteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssetOptimizeLiteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.glossary):
            query['Glossary'] = request.glossary
        if not DaraCore.is_null(request.including_product_area):
            query['IncludingProductArea'] = request.including_product_area
        if not DaraCore.is_null(request.need_trans):
            query['NeedTrans'] = request.need_trans
        if not DaraCore.is_null(request.product_url):
            query['ProductUrl'] = request.product_url
        if not DaraCore.is_null(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.source_platform):
            query['SourcePlatform'] = request.source_platform
        if not DaraCore.is_null(request.target_language):
            query['TargetLanguage'] = request.target_language
        if not DaraCore.is_null(request.target_platform):
            query['TargetPlatform'] = request.target_platform
        if not DaraCore.is_null(request.translating_brand_in_the_product):
            query['TranslatingBrandInTheProduct'] = request.translating_brand_in_the_product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssetOptimizeLite',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssetOptimizeLiteResponse(),
            self.call_api(params, req, runtime)
        )

    async def asset_optimize_lite_with_options_async(
        self,
        request: main_models.AssetOptimizeLiteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssetOptimizeLiteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.glossary):
            query['Glossary'] = request.glossary
        if not DaraCore.is_null(request.including_product_area):
            query['IncludingProductArea'] = request.including_product_area
        if not DaraCore.is_null(request.need_trans):
            query['NeedTrans'] = request.need_trans
        if not DaraCore.is_null(request.product_url):
            query['ProductUrl'] = request.product_url
        if not DaraCore.is_null(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.source_platform):
            query['SourcePlatform'] = request.source_platform
        if not DaraCore.is_null(request.target_language):
            query['TargetLanguage'] = request.target_language
        if not DaraCore.is_null(request.target_platform):
            query['TargetPlatform'] = request.target_platform
        if not DaraCore.is_null(request.translating_brand_in_the_product):
            query['TranslatingBrandInTheProduct'] = request.translating_brand_in_the_product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssetOptimizeLite',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssetOptimizeLiteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def asset_optimize_lite(
        self,
        request: main_models.AssetOptimizeLiteRequest,
    ) -> main_models.AssetOptimizeLiteResponse:
        runtime = RuntimeOptions()
        return self.asset_optimize_lite_with_options(request, runtime)

    async def asset_optimize_lite_async(
        self,
        request: main_models.AssetOptimizeLiteRequest,
    ) -> main_models.AssetOptimizeLiteResponse:
        runtime = RuntimeOptions()
        return await self.asset_optimize_lite_with_options_async(request, runtime)

    def asset_optimize_pro_with_options(
        self,
        tmp_req: main_models.AssetOptimizeProRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssetOptimizeProResponse:
        tmp_req.validate()
        request = main_models.AssetOptimizeProShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.column_name_list):
            request.column_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.column_name_list, 'ColumnNameList', 'json')
        query = {}
        if not DaraCore.is_null(request.column_name_list_shrink):
            query['ColumnNameList'] = request.column_name_list_shrink
        if not DaraCore.is_null(request.glossary):
            query['Glossary'] = request.glossary
        if not DaraCore.is_null(request.including_product_area):
            query['IncludingProductArea'] = request.including_product_area
        if not DaraCore.is_null(request.language_model):
            query['LanguageModel'] = request.language_model
        if not DaraCore.is_null(request.need_trans):
            query['NeedTrans'] = request.need_trans
        if not DaraCore.is_null(request.product_url):
            query['ProductUrl'] = request.product_url
        if not DaraCore.is_null(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.source_platform):
            query['SourcePlatform'] = request.source_platform
        if not DaraCore.is_null(request.target_language):
            query['TargetLanguage'] = request.target_language
        if not DaraCore.is_null(request.target_platform):
            query['TargetPlatform'] = request.target_platform
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        if not DaraCore.is_null(request.translating_brand_in_the_product):
            query['TranslatingBrandInTheProduct'] = request.translating_brand_in_the_product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssetOptimizePro',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssetOptimizeProResponse(),
            self.call_api(params, req, runtime)
        )

    async def asset_optimize_pro_with_options_async(
        self,
        tmp_req: main_models.AssetOptimizeProRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssetOptimizeProResponse:
        tmp_req.validate()
        request = main_models.AssetOptimizeProShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.column_name_list):
            request.column_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.column_name_list, 'ColumnNameList', 'json')
        query = {}
        if not DaraCore.is_null(request.column_name_list_shrink):
            query['ColumnNameList'] = request.column_name_list_shrink
        if not DaraCore.is_null(request.glossary):
            query['Glossary'] = request.glossary
        if not DaraCore.is_null(request.including_product_area):
            query['IncludingProductArea'] = request.including_product_area
        if not DaraCore.is_null(request.language_model):
            query['LanguageModel'] = request.language_model
        if not DaraCore.is_null(request.need_trans):
            query['NeedTrans'] = request.need_trans
        if not DaraCore.is_null(request.product_url):
            query['ProductUrl'] = request.product_url
        if not DaraCore.is_null(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.source_platform):
            query['SourcePlatform'] = request.source_platform
        if not DaraCore.is_null(request.target_language):
            query['TargetLanguage'] = request.target_language
        if not DaraCore.is_null(request.target_platform):
            query['TargetPlatform'] = request.target_platform
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        if not DaraCore.is_null(request.translating_brand_in_the_product):
            query['TranslatingBrandInTheProduct'] = request.translating_brand_in_the_product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssetOptimizePro',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssetOptimizeProResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def asset_optimize_pro(
        self,
        request: main_models.AssetOptimizeProRequest,
    ) -> main_models.AssetOptimizeProResponse:
        runtime = RuntimeOptions()
        return self.asset_optimize_pro_with_options(request, runtime)

    async def asset_optimize_pro_async(
        self,
        request: main_models.AssetOptimizeProRequest,
    ) -> main_models.AssetOptimizeProResponse:
        runtime = RuntimeOptions()
        return await self.asset_optimize_pro_with_options_async(request, runtime)

    def category_attribute_match_with_options(
        self,
        tmp_req: main_models.CategoryAttributeMatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CategoryAttributeMatchResponse:
        tmp_req.validate()
        request = main_models.CategoryAttributeMatchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_url):
            request.image_url_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_url, 'ImageUrl', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.image_url_shrink):
            body['ImageUrl'] = request.image_url_shrink
        if not DaraCore.is_null(request.item_spec):
            body['ItemSpec'] = request.item_spec
        if not DaraCore.is_null(request.sku):
            body['Sku'] = request.sku
        if not DaraCore.is_null(request.source_category):
            body['SourceCategory'] = request.source_category
        if not DaraCore.is_null(request.source_platform):
            body['SourcePlatform'] = request.source_platform
        if not DaraCore.is_null(request.target_platform):
            body['TargetPlatform'] = request.target_platform
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CategoryAttributeMatch',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CategoryAttributeMatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def category_attribute_match_with_options_async(
        self,
        tmp_req: main_models.CategoryAttributeMatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CategoryAttributeMatchResponse:
        tmp_req.validate()
        request = main_models.CategoryAttributeMatchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_url):
            request.image_url_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_url, 'ImageUrl', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.image_url_shrink):
            body['ImageUrl'] = request.image_url_shrink
        if not DaraCore.is_null(request.item_spec):
            body['ItemSpec'] = request.item_spec
        if not DaraCore.is_null(request.sku):
            body['Sku'] = request.sku
        if not DaraCore.is_null(request.source_category):
            body['SourceCategory'] = request.source_category
        if not DaraCore.is_null(request.source_platform):
            body['SourcePlatform'] = request.source_platform
        if not DaraCore.is_null(request.target_platform):
            body['TargetPlatform'] = request.target_platform
        if not DaraCore.is_null(request.title):
            body['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CategoryAttributeMatch',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CategoryAttributeMatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def category_attribute_match(
        self,
        request: main_models.CategoryAttributeMatchRequest,
    ) -> main_models.CategoryAttributeMatchResponse:
        runtime = RuntimeOptions()
        return self.category_attribute_match_with_options(request, runtime)

    async def category_attribute_match_async(
        self,
        request: main_models.CategoryAttributeMatchRequest,
    ) -> main_models.CategoryAttributeMatchResponse:
        runtime = RuntimeOptions()
        return await self.category_attribute_match_with_options_async(request, runtime)

    def category_match_with_options(
        self,
        request: main_models.CategoryMatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CategoryMatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.item_spec):
            query['ItemSpec'] = request.item_spec
        if not DaraCore.is_null(request.sku):
            query['Sku'] = request.sku
        if not DaraCore.is_null(request.source_category):
            query['SourceCategory'] = request.source_category
        if not DaraCore.is_null(request.source_platform):
            query['SourcePlatform'] = request.source_platform
        if not DaraCore.is_null(request.target_platform):
            query['TargetPlatform'] = request.target_platform
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CategoryMatch',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CategoryMatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def category_match_with_options_async(
        self,
        request: main_models.CategoryMatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CategoryMatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.item_spec):
            query['ItemSpec'] = request.item_spec
        if not DaraCore.is_null(request.sku):
            query['Sku'] = request.sku
        if not DaraCore.is_null(request.source_category):
            query['SourceCategory'] = request.source_category
        if not DaraCore.is_null(request.source_platform):
            query['SourcePlatform'] = request.source_platform
        if not DaraCore.is_null(request.target_platform):
            query['TargetPlatform'] = request.target_platform
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CategoryMatch',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CategoryMatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def category_match(
        self,
        request: main_models.CategoryMatchRequest,
    ) -> main_models.CategoryMatchResponse:
        runtime = RuntimeOptions()
        return self.category_match_with_options(request, runtime)

    async def category_match_async(
        self,
        request: main_models.CategoryMatchRequest,
    ) -> main_models.CategoryMatchResponse:
        runtime = RuntimeOptions()
        return await self.category_match_with_options_async(request, runtime)

    def document_translate_with_options(
        self,
        request: main_models.DocumentTranslateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DocumentTranslateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.glossary):
            query['Glossary'] = request.glossary
        if not DaraCore.is_null(request.target_language):
            query['TargetLanguage'] = request.target_language
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DocumentTranslate',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DocumentTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def document_translate_with_options_async(
        self,
        request: main_models.DocumentTranslateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DocumentTranslateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.glossary):
            query['Glossary'] = request.glossary
        if not DaraCore.is_null(request.target_language):
            query['TargetLanguage'] = request.target_language
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DocumentTranslate',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DocumentTranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def document_translate(
        self,
        request: main_models.DocumentTranslateRequest,
    ) -> main_models.DocumentTranslateResponse:
        runtime = RuntimeOptions()
        return self.document_translate_with_options(request, runtime)

    async def document_translate_async(
        self,
        request: main_models.DocumentTranslateRequest,
    ) -> main_models.DocumentTranslateResponse:
        runtime = RuntimeOptions()
        return await self.document_translate_with_options_async(request, runtime)

    def image_cropping_with_options(
        self,
        request: main_models.ImageCroppingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageCroppingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.target_height):
            query['TargetHeight'] = request.target_height
        if not DaraCore.is_null(request.target_width):
            query['TargetWidth'] = request.target_width
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImageCropping',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageCroppingResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_cropping_with_options_async(
        self,
        request: main_models.ImageCroppingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageCroppingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.target_height):
            query['TargetHeight'] = request.target_height
        if not DaraCore.is_null(request.target_width):
            query['TargetWidth'] = request.target_width
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImageCropping',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageCroppingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_cropping(
        self,
        request: main_models.ImageCroppingRequest,
    ) -> main_models.ImageCroppingResponse:
        runtime = RuntimeOptions()
        return self.image_cropping_with_options(request, runtime)

    async def image_cropping_async(
        self,
        request: main_models.ImageCroppingRequest,
    ) -> main_models.ImageCroppingResponse:
        runtime = RuntimeOptions()
        return await self.image_cropping_with_options_async(request, runtime)

    def image_matting_with_options(
        self,
        request: main_models.ImageMattingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageMattingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.back_ground_type):
            query['BackGroundType'] = request.back_ground_type
        if not DaraCore.is_null(request.bg_color):
            query['BgColor'] = request.bg_color
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.target_height):
            query['TargetHeight'] = request.target_height
        if not DaraCore.is_null(request.target_width):
            query['TargetWidth'] = request.target_width
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImageMatting',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageMattingResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_matting_with_options_async(
        self,
        request: main_models.ImageMattingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageMattingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.back_ground_type):
            query['BackGroundType'] = request.back_ground_type
        if not DaraCore.is_null(request.bg_color):
            query['BgColor'] = request.bg_color
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.target_height):
            query['TargetHeight'] = request.target_height
        if not DaraCore.is_null(request.target_width):
            query['TargetWidth'] = request.target_width
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImageMatting',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageMattingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_matting(
        self,
        request: main_models.ImageMattingRequest,
    ) -> main_models.ImageMattingResponse:
        runtime = RuntimeOptions()
        return self.image_matting_with_options(request, runtime)

    async def image_matting_async(
        self,
        request: main_models.ImageMattingRequest,
    ) -> main_models.ImageMattingResponse:
        runtime = RuntimeOptions()
        return await self.image_matting_with_options_async(request, runtime)

    def image_recognition_with_options(
        self,
        tmp_req: main_models.ImageRecognitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageRecognitionResponse:
        tmp_req.validate()
        request = main_models.ImageRecognitionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.non_object_detect_elements):
            request.non_object_detect_elements_shrink = Utils.array_to_string_with_specified_style(tmp_req.non_object_detect_elements, 'NonObjectDetectElements', 'json')
        if not DaraCore.is_null(tmp_req.object_detect_elements):
            request.object_detect_elements_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_detect_elements, 'ObjectDetectElements', 'json')
        query = {}
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.non_object_detect_elements_shrink):
            query['NonObjectDetectElements'] = request.non_object_detect_elements_shrink
        if not DaraCore.is_null(request.object_detect_elements_shrink):
            query['ObjectDetectElements'] = request.object_detect_elements_shrink
        if not DaraCore.is_null(request.return_border_pixel):
            query['ReturnBorderPixel'] = request.return_border_pixel
        if not DaraCore.is_null(request.return_character):
            query['ReturnCharacter'] = request.return_character
        if not DaraCore.is_null(request.return_character_prop):
            query['ReturnCharacterProp'] = request.return_character_prop
        if not DaraCore.is_null(request.return_product_num):
            query['ReturnProductNum'] = request.return_product_num
        if not DaraCore.is_null(request.return_product_prop):
            query['ReturnProductProp'] = request.return_product_prop
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImageRecognition',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageRecognitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_recognition_with_options_async(
        self,
        tmp_req: main_models.ImageRecognitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageRecognitionResponse:
        tmp_req.validate()
        request = main_models.ImageRecognitionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.non_object_detect_elements):
            request.non_object_detect_elements_shrink = Utils.array_to_string_with_specified_style(tmp_req.non_object_detect_elements, 'NonObjectDetectElements', 'json')
        if not DaraCore.is_null(tmp_req.object_detect_elements):
            request.object_detect_elements_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_detect_elements, 'ObjectDetectElements', 'json')
        query = {}
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.non_object_detect_elements_shrink):
            query['NonObjectDetectElements'] = request.non_object_detect_elements_shrink
        if not DaraCore.is_null(request.object_detect_elements_shrink):
            query['ObjectDetectElements'] = request.object_detect_elements_shrink
        if not DaraCore.is_null(request.return_border_pixel):
            query['ReturnBorderPixel'] = request.return_border_pixel
        if not DaraCore.is_null(request.return_character):
            query['ReturnCharacter'] = request.return_character
        if not DaraCore.is_null(request.return_character_prop):
            query['ReturnCharacterProp'] = request.return_character_prop
        if not DaraCore.is_null(request.return_product_num):
            query['ReturnProductNum'] = request.return_product_num
        if not DaraCore.is_null(request.return_product_prop):
            query['ReturnProductProp'] = request.return_product_prop
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImageRecognition',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageRecognitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_recognition(
        self,
        request: main_models.ImageRecognitionRequest,
    ) -> main_models.ImageRecognitionResponse:
        runtime = RuntimeOptions()
        return self.image_recognition_with_options(request, runtime)

    async def image_recognition_async(
        self,
        request: main_models.ImageRecognitionRequest,
    ) -> main_models.ImageRecognitionResponse:
        runtime = RuntimeOptions()
        return await self.image_recognition_with_options_async(request, runtime)

    def image_remove_with_options(
        self,
        tmp_req: main_models.ImageRemoveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageRemoveResponse:
        tmp_req.validate()
        request = main_models.ImageRemoveShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.non_object_remove_elements):
            request.non_object_remove_elements_shrink = Utils.array_to_string_with_specified_style(tmp_req.non_object_remove_elements, 'NonObjectRemoveElements', 'json')
        if not DaraCore.is_null(tmp_req.object_remove_elements):
            request.object_remove_elements_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_remove_elements, 'ObjectRemoveElements', 'json')
        query = {}
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.non_object_remove_elements_shrink):
            query['NonObjectRemoveElements'] = request.non_object_remove_elements_shrink
        if not DaraCore.is_null(request.object_remove_elements_shrink):
            query['ObjectRemoveElements'] = request.object_remove_elements_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImageRemove',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageRemoveResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_remove_with_options_async(
        self,
        tmp_req: main_models.ImageRemoveRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageRemoveResponse:
        tmp_req.validate()
        request = main_models.ImageRemoveShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.non_object_remove_elements):
            request.non_object_remove_elements_shrink = Utils.array_to_string_with_specified_style(tmp_req.non_object_remove_elements, 'NonObjectRemoveElements', 'json')
        if not DaraCore.is_null(tmp_req.object_remove_elements):
            request.object_remove_elements_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_remove_elements, 'ObjectRemoveElements', 'json')
        query = {}
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.non_object_remove_elements_shrink):
            query['NonObjectRemoveElements'] = request.non_object_remove_elements_shrink
        if not DaraCore.is_null(request.object_remove_elements_shrink):
            query['ObjectRemoveElements'] = request.object_remove_elements_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImageRemove',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageRemoveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_remove(
        self,
        request: main_models.ImageRemoveRequest,
    ) -> main_models.ImageRemoveResponse:
        runtime = RuntimeOptions()
        return self.image_remove_with_options(request, runtime)

    async def image_remove_async(
        self,
        request: main_models.ImageRemoveRequest,
    ) -> main_models.ImageRemoveResponse:
        runtime = RuntimeOptions()
        return await self.image_remove_with_options_async(request, runtime)

    def image_translation_pro_with_options(
        self,
        request: main_models.ImageTranslationProRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageTranslationProResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.glossary):
            body['Glossary'] = request.glossary
        if not DaraCore.is_null(request.image_url):
            body['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.including_product_area):
            body['IncludingProductArea'] = request.including_product_area
        if not DaraCore.is_null(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['TargetLanguage'] = request.target_language
        if not DaraCore.is_null(request.translating_brand_in_the_product):
            body['TranslatingBrandInTheProduct'] = request.translating_brand_in_the_product
        if not DaraCore.is_null(request.use_image_editor):
            body['UseImageEditor'] = request.use_image_editor
        if not DaraCore.is_null(request.call_type):
            body['callType'] = request.call_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImageTranslationPro',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageTranslationProResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_translation_pro_with_options_async(
        self,
        request: main_models.ImageTranslationProRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageTranslationProResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.glossary):
            body['Glossary'] = request.glossary
        if not DaraCore.is_null(request.image_url):
            body['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.including_product_area):
            body['IncludingProductArea'] = request.including_product_area
        if not DaraCore.is_null(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            body['TargetLanguage'] = request.target_language
        if not DaraCore.is_null(request.translating_brand_in_the_product):
            body['TranslatingBrandInTheProduct'] = request.translating_brand_in_the_product
        if not DaraCore.is_null(request.use_image_editor):
            body['UseImageEditor'] = request.use_image_editor
        if not DaraCore.is_null(request.call_type):
            body['callType'] = request.call_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImageTranslationPro',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageTranslationProResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_translation_pro(
        self,
        request: main_models.ImageTranslationProRequest,
    ) -> main_models.ImageTranslationProResponse:
        runtime = RuntimeOptions()
        return self.image_translation_pro_with_options(request, runtime)

    async def image_translation_pro_async(
        self,
        request: main_models.ImageTranslationProRequest,
    ) -> main_models.ImageTranslationProResponse:
        runtime = RuntimeOptions()
        return await self.image_translation_pro_with_options_async(request, runtime)

    def image_translation_standard_with_options(
        self,
        request: main_models.ImageTranslationStandardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageTranslationStandardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.glossary):
            query['Glossary'] = request.glossary
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.including_product_area):
            query['IncludingProductArea'] = request.including_product_area
        if not DaraCore.is_null(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            query['TargetLanguage'] = request.target_language
        if not DaraCore.is_null(request.translating_brand_in_the_product):
            query['TranslatingBrandInTheProduct'] = request.translating_brand_in_the_product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImageTranslationStandard',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageTranslationStandardResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_translation_standard_with_options_async(
        self,
        request: main_models.ImageTranslationStandardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImageTranslationStandardResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.glossary):
            query['Glossary'] = request.glossary
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.including_product_area):
            query['IncludingProductArea'] = request.including_product_area
        if not DaraCore.is_null(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_language):
            query['TargetLanguage'] = request.target_language
        if not DaraCore.is_null(request.translating_brand_in_the_product):
            query['TranslatingBrandInTheProduct'] = request.translating_brand_in_the_product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImageTranslationStandard',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImageTranslationStandardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_translation_standard(
        self,
        request: main_models.ImageTranslationStandardRequest,
    ) -> main_models.ImageTranslationStandardResponse:
        runtime = RuntimeOptions()
        return self.image_translation_standard_with_options(request, runtime)

    async def image_translation_standard_async(
        self,
        request: main_models.ImageTranslationStandardRequest,
    ) -> main_models.ImageTranslationStandardResponse:
        runtime = RuntimeOptions()
        return await self.image_translation_standard_with_options_async(request, runtime)

    def language_detect_with_options(
        self,
        request: main_models.LanguageDetectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LanguageDetectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.source_text):
            query['SourceText'] = request.source_text
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LanguageDetect',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LanguageDetectResponse(),
            self.call_api(params, req, runtime)
        )

    async def language_detect_with_options_async(
        self,
        request: main_models.LanguageDetectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LanguageDetectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.source_text):
            query['SourceText'] = request.source_text
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LanguageDetect',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LanguageDetectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def language_detect(
        self,
        request: main_models.LanguageDetectRequest,
    ) -> main_models.LanguageDetectResponse:
        runtime = RuntimeOptions()
        return self.language_detect_with_options(request, runtime)

    async def language_detect_async(
        self,
        request: main_models.LanguageDetectRequest,
    ) -> main_models.LanguageDetectResponse:
        runtime = RuntimeOptions()
        return await self.language_detect_with_options_async(request, runtime)

    def package_weight_size_check_with_options(
        self,
        request: main_models.PackageWeightSizeCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PackageWeightSizeCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotated_image_url):
            query['AnnotatedImageUrl'] = request.annotated_image_url
        if not DaraCore.is_null(request.raw_image_url):
            query['RawImageUrl'] = request.raw_image_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PackageWeightSizeCheck',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PackageWeightSizeCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def package_weight_size_check_with_options_async(
        self,
        request: main_models.PackageWeightSizeCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PackageWeightSizeCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotated_image_url):
            query['AnnotatedImageUrl'] = request.annotated_image_url
        if not DaraCore.is_null(request.raw_image_url):
            query['RawImageUrl'] = request.raw_image_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PackageWeightSizeCheck',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PackageWeightSizeCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def package_weight_size_check(
        self,
        request: main_models.PackageWeightSizeCheckRequest,
    ) -> main_models.PackageWeightSizeCheckResponse:
        runtime = RuntimeOptions()
        return self.package_weight_size_check_with_options(request, runtime)

    async def package_weight_size_check_async(
        self,
        request: main_models.PackageWeightSizeCheckRequest,
    ) -> main_models.PackageWeightSizeCheckResponse:
        runtime = RuntimeOptions()
        return await self.package_weight_size_check_with_options_async(request, runtime)

    def query_async_task_result_with_options(
        self,
        request: main_models.QueryAsyncTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAsyncTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAsyncTaskResult',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAsyncTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_async_task_result_with_options_async(
        self,
        request: main_models.QueryAsyncTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAsyncTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAsyncTaskResult',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAsyncTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_async_task_result(
        self,
        request: main_models.QueryAsyncTaskResultRequest,
    ) -> main_models.QueryAsyncTaskResultResponse:
        runtime = RuntimeOptions()
        return self.query_async_task_result_with_options(request, runtime)

    async def query_async_task_result_async(
        self,
        request: main_models.QueryAsyncTaskResultRequest,
    ) -> main_models.QueryAsyncTaskResultResponse:
        runtime = RuntimeOptions()
        return await self.query_async_task_result_with_options_async(request, runtime)

    def size_chart_detect_with_options(
        self,
        request: main_models.SizeChartDetectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SizeChartDetectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SizeChartDetect',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SizeChartDetectResponse(),
            self.call_api(params, req, runtime)
        )

    async def size_chart_detect_with_options_async(
        self,
        request: main_models.SizeChartDetectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SizeChartDetectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SizeChartDetect',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SizeChartDetectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def size_chart_detect(
        self,
        request: main_models.SizeChartDetectRequest,
    ) -> main_models.SizeChartDetectResponse:
        runtime = RuntimeOptions()
        return self.size_chart_detect_with_options(request, runtime)

    async def size_chart_detect_async(
        self,
        request: main_models.SizeChartDetectRequest,
    ) -> main_models.SizeChartDetectResponse:
        runtime = RuntimeOptions()
        return await self.size_chart_detect_with_options_async(request, runtime)

    def size_chart_extract_with_options(
        self,
        tmp_req: main_models.SizeChartExtractRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SizeChartExtractResponse:
        tmp_req.validate()
        request = main_models.SizeChartExtractShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.column_name_list):
            request.column_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.column_name_list, 'ColumnNameList', 'json')
        query = {}
        if not DaraCore.is_null(request.column_name_list_shrink):
            query['ColumnNameList'] = request.column_name_list_shrink
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.language_model):
            query['LanguageModel'] = request.language_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SizeChartExtract',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SizeChartExtractResponse(),
            self.call_api(params, req, runtime)
        )

    async def size_chart_extract_with_options_async(
        self,
        tmp_req: main_models.SizeChartExtractRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SizeChartExtractResponse:
        tmp_req.validate()
        request = main_models.SizeChartExtractShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.column_name_list):
            request.column_name_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.column_name_list, 'ColumnNameList', 'json')
        query = {}
        if not DaraCore.is_null(request.column_name_list_shrink):
            query['ColumnNameList'] = request.column_name_list_shrink
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.language_model):
            query['LanguageModel'] = request.language_model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SizeChartExtract',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SizeChartExtractResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def size_chart_extract(
        self,
        request: main_models.SizeChartExtractRequest,
    ) -> main_models.SizeChartExtractResponse:
        runtime = RuntimeOptions()
        return self.size_chart_extract_with_options(request, runtime)

    async def size_chart_extract_async(
        self,
        request: main_models.SizeChartExtractRequest,
    ) -> main_models.SizeChartExtractResponse:
        runtime = RuntimeOptions()
        return await self.size_chart_extract_with_options_async(request, runtime)

    def text_correct_with_options(
        self,
        request: main_models.TextCorrectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TextCorrectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.source_text):
            query['SourceText'] = request.source_text
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TextCorrect',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TextCorrectResponse(),
            self.call_api(params, req, runtime)
        )

    async def text_correct_with_options_async(
        self,
        request: main_models.TextCorrectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TextCorrectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.source_text):
            query['SourceText'] = request.source_text
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TextCorrect',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TextCorrectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def text_correct(
        self,
        request: main_models.TextCorrectRequest,
    ) -> main_models.TextCorrectResponse:
        runtime = RuntimeOptions()
        return self.text_correct_with_options(request, runtime)

    async def text_correct_async(
        self,
        request: main_models.TextCorrectRequest,
    ) -> main_models.TextCorrectResponse:
        runtime = RuntimeOptions()
        return await self.text_correct_with_options_async(request, runtime)

    def text_translate_with_options(
        self,
        tmp_req: main_models.TextTranslateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TextTranslateResponse:
        tmp_req.validate()
        request = main_models.TextTranslateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.source_text_list):
            request.source_text_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_text_list, 'SourceTextList', 'json')
        body = {}
        if not DaraCore.is_null(request.format_type):
            body['FormatType'] = request.format_type
        if not DaraCore.is_null(request.glossary):
            body['Glossary'] = request.glossary
        if not DaraCore.is_null(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.source_text_list_shrink):
            body['SourceTextList'] = request.source_text_list_shrink
        if not DaraCore.is_null(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TextTranslate',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TextTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def text_translate_with_options_async(
        self,
        tmp_req: main_models.TextTranslateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TextTranslateResponse:
        tmp_req.validate()
        request = main_models.TextTranslateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.source_text_list):
            request.source_text_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_text_list, 'SourceTextList', 'json')
        body = {}
        if not DaraCore.is_null(request.format_type):
            body['FormatType'] = request.format_type
        if not DaraCore.is_null(request.glossary):
            body['Glossary'] = request.glossary
        if not DaraCore.is_null(request.source_language):
            body['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.source_text_list_shrink):
            body['SourceTextList'] = request.source_text_list_shrink
        if not DaraCore.is_null(request.target_language):
            body['TargetLanguage'] = request.target_language
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TextTranslate',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TextTranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def text_translate(
        self,
        request: main_models.TextTranslateRequest,
    ) -> main_models.TextTranslateResponse:
        runtime = RuntimeOptions()
        return self.text_translate_with_options(request, runtime)

    async def text_translate_async(
        self,
        request: main_models.TextTranslateRequest,
    ) -> main_models.TextTranslateResponse:
        runtime = RuntimeOptions()
        return await self.text_translate_with_options_async(request, runtime)

    def vision_flow_with_options(
        self,
        tmp_req: main_models.VisionFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VisionFlowResponse:
        tmp_req.validate()
        request = main_models.VisionFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ability):
            request.ability_shrink = Utils.array_to_string_with_specified_style(tmp_req.ability, 'Ability', 'json')
        if not DaraCore.is_null(tmp_req.nonobject_detect_elements):
            request.nonobject_detect_elements_shrink = Utils.array_to_string_with_specified_style(tmp_req.nonobject_detect_elements, 'NonobjectDetectElements', 'json')
        if not DaraCore.is_null(tmp_req.nonobject_remove_elements):
            request.nonobject_remove_elements_shrink = Utils.array_to_string_with_specified_style(tmp_req.nonobject_remove_elements, 'NonobjectRemoveElements', 'json')
        if not DaraCore.is_null(tmp_req.object_detect_elements):
            request.object_detect_elements_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_detect_elements, 'ObjectDetectElements', 'json')
        if not DaraCore.is_null(tmp_req.object_remove_elements):
            request.object_remove_elements_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_remove_elements, 'ObjectRemoveElements', 'json')
        query = {}
        if not DaraCore.is_null(request.ability_shrink):
            query['Ability'] = request.ability_shrink
        if not DaraCore.is_null(request.back_ground_type):
            query['BackGroundType'] = request.back_ground_type
        if not DaraCore.is_null(request.glossary):
            query['Glossary'] = request.glossary
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.including_product_area):
            query['IncludingProductArea'] = request.including_product_area
        if not DaraCore.is_null(request.is_filter):
            query['IsFilter'] = request.is_filter
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.nonobject_detect_elements_shrink):
            query['NonobjectDetectElements'] = request.nonobject_detect_elements_shrink
        if not DaraCore.is_null(request.nonobject_remove_elements_shrink):
            query['NonobjectRemoveElements'] = request.nonobject_remove_elements_shrink
        if not DaraCore.is_null(request.object_detect_elements_shrink):
            query['ObjectDetectElements'] = request.object_detect_elements_shrink
        if not DaraCore.is_null(request.object_remove_elements_shrink):
            query['ObjectRemoveElements'] = request.object_remove_elements_shrink
        if not DaraCore.is_null(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_height):
            query['TargetHeight'] = request.target_height
        if not DaraCore.is_null(request.target_language):
            query['TargetLanguage'] = request.target_language
        if not DaraCore.is_null(request.target_width):
            query['TargetWidth'] = request.target_width
        if not DaraCore.is_null(request.translating_brand_in_the_product):
            query['TranslatingBrandInTheProduct'] = request.translating_brand_in_the_product
        if not DaraCore.is_null(request.upscale_factor):
            query['UpscaleFactor'] = request.upscale_factor
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VisionFlow',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VisionFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def vision_flow_with_options_async(
        self,
        tmp_req: main_models.VisionFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VisionFlowResponse:
        tmp_req.validate()
        request = main_models.VisionFlowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ability):
            request.ability_shrink = Utils.array_to_string_with_specified_style(tmp_req.ability, 'Ability', 'json')
        if not DaraCore.is_null(tmp_req.nonobject_detect_elements):
            request.nonobject_detect_elements_shrink = Utils.array_to_string_with_specified_style(tmp_req.nonobject_detect_elements, 'NonobjectDetectElements', 'json')
        if not DaraCore.is_null(tmp_req.nonobject_remove_elements):
            request.nonobject_remove_elements_shrink = Utils.array_to_string_with_specified_style(tmp_req.nonobject_remove_elements, 'NonobjectRemoveElements', 'json')
        if not DaraCore.is_null(tmp_req.object_detect_elements):
            request.object_detect_elements_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_detect_elements, 'ObjectDetectElements', 'json')
        if not DaraCore.is_null(tmp_req.object_remove_elements):
            request.object_remove_elements_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_remove_elements, 'ObjectRemoveElements', 'json')
        query = {}
        if not DaraCore.is_null(request.ability_shrink):
            query['Ability'] = request.ability_shrink
        if not DaraCore.is_null(request.back_ground_type):
            query['BackGroundType'] = request.back_ground_type
        if not DaraCore.is_null(request.glossary):
            query['Glossary'] = request.glossary
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.including_product_area):
            query['IncludingProductArea'] = request.including_product_area
        if not DaraCore.is_null(request.is_filter):
            query['IsFilter'] = request.is_filter
        if not DaraCore.is_null(request.mask):
            query['Mask'] = request.mask
        if not DaraCore.is_null(request.nonobject_detect_elements_shrink):
            query['NonobjectDetectElements'] = request.nonobject_detect_elements_shrink
        if not DaraCore.is_null(request.nonobject_remove_elements_shrink):
            query['NonobjectRemoveElements'] = request.nonobject_remove_elements_shrink
        if not DaraCore.is_null(request.object_detect_elements_shrink):
            query['ObjectDetectElements'] = request.object_detect_elements_shrink
        if not DaraCore.is_null(request.object_remove_elements_shrink):
            query['ObjectRemoveElements'] = request.object_remove_elements_shrink
        if not DaraCore.is_null(request.source_language):
            query['SourceLanguage'] = request.source_language
        if not DaraCore.is_null(request.target_height):
            query['TargetHeight'] = request.target_height
        if not DaraCore.is_null(request.target_language):
            query['TargetLanguage'] = request.target_language
        if not DaraCore.is_null(request.target_width):
            query['TargetWidth'] = request.target_width
        if not DaraCore.is_null(request.translating_brand_in_the_product):
            query['TranslatingBrandInTheProduct'] = request.translating_brand_in_the_product
        if not DaraCore.is_null(request.upscale_factor):
            query['UpscaleFactor'] = request.upscale_factor
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VisionFlow',
            version = '2026-04-28',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VisionFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vision_flow(
        self,
        request: main_models.VisionFlowRequest,
    ) -> main_models.VisionFlowResponse:
        runtime = RuntimeOptions()
        return self.vision_flow_with_options(request, runtime)

    async def vision_flow_async(
        self,
        request: main_models.VisionFlowRequest,
    ) -> main_models.VisionFlowResponse:
        runtime = RuntimeOptions()
        return await self.vision_flow_with_options_async(request, runtime)
