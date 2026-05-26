# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentretailvision20260506 import models as main_models
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
        self._endpoint = self.get_endpoint('agentretailvision', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def import_products_with_options(
        self,
        tmp_req: main_models.ImportProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportProductsResponse:
        tmp_req.validate()
        request = main_models.ImportProductsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extra_images):
            request.extra_images_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra_images, 'ExtraImages', 'json')
        if not DaraCore.is_null(tmp_req.main_image):
            request.main_image_shrink = Utils.array_to_string_with_specified_style(tmp_req.main_image, 'MainImage', 'json')
        if not DaraCore.is_null(tmp_req.multi_view_images):
            request.multi_view_images_shrink = Utils.array_to_string_with_specified_style(tmp_req.multi_view_images, 'MultiViewImages', 'json')
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.extra_images_shrink):
            query['ExtraImages'] = request.extra_images_shrink
        if not DaraCore.is_null(request.image_title):
            query['ImageTitle'] = request.image_title
        if not DaraCore.is_null(request.item_unique_id):
            query['ItemUniqueId'] = request.item_unique_id
        if not DaraCore.is_null(request.main_image_shrink):
            query['MainImage'] = request.main_image_shrink
        if not DaraCore.is_null(request.multi_view_images_shrink):
            query['MultiViewImages'] = request.multi_view_images_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportProducts',
            version = '2026-05-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_products_with_options_async(
        self,
        tmp_req: main_models.ImportProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportProductsResponse:
        tmp_req.validate()
        request = main_models.ImportProductsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extra_images):
            request.extra_images_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra_images, 'ExtraImages', 'json')
        if not DaraCore.is_null(tmp_req.main_image):
            request.main_image_shrink = Utils.array_to_string_with_specified_style(tmp_req.main_image, 'MainImage', 'json')
        if not DaraCore.is_null(tmp_req.multi_view_images):
            request.multi_view_images_shrink = Utils.array_to_string_with_specified_style(tmp_req.multi_view_images, 'MultiViewImages', 'json')
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.extra_images_shrink):
            query['ExtraImages'] = request.extra_images_shrink
        if not DaraCore.is_null(request.image_title):
            query['ImageTitle'] = request.image_title
        if not DaraCore.is_null(request.item_unique_id):
            query['ItemUniqueId'] = request.item_unique_id
        if not DaraCore.is_null(request.main_image_shrink):
            query['MainImage'] = request.main_image_shrink
        if not DaraCore.is_null(request.multi_view_images_shrink):
            query['MultiViewImages'] = request.multi_view_images_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportProducts',
            version = '2026-05-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_products(
        self,
        request: main_models.ImportProductsRequest,
    ) -> main_models.ImportProductsResponse:
        runtime = RuntimeOptions()
        return self.import_products_with_options(request, runtime)

    async def import_products_async(
        self,
        request: main_models.ImportProductsRequest,
    ) -> main_models.ImportProductsResponse:
        runtime = RuntimeOptions()
        return await self.import_products_with_options_async(request, runtime)

    def query_recognition_result_with_options(
        self,
        request: main_models.QueryRecognitionResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecognitionResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_unique_id):
            query['OrderUniqueId'] = request.order_unique_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecognitionResult',
            version = '2026-05-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecognitionResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_recognition_result_with_options_async(
        self,
        request: main_models.QueryRecognitionResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRecognitionResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_unique_id):
            query['OrderUniqueId'] = request.order_unique_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRecognitionResult',
            version = '2026-05-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRecognitionResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_recognition_result(
        self,
        request: main_models.QueryRecognitionResultRequest,
    ) -> main_models.QueryRecognitionResultResponse:
        runtime = RuntimeOptions()
        return self.query_recognition_result_with_options(request, runtime)

    async def query_recognition_result_async(
        self,
        request: main_models.QueryRecognitionResultRequest,
    ) -> main_models.QueryRecognitionResultResponse:
        runtime = RuntimeOptions()
        return await self.query_recognition_result_with_options_async(request, runtime)

    def recognize_order_with_options(
        self,
        tmp_req: main_models.RecognizeOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecognizeOrderResponse:
        tmp_req.validate()
        request = main_models.RecognizeOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.candidate_items):
            request.candidate_items_shrink = Utils.array_to_string_with_specified_style(tmp_req.candidate_items, 'CandidateItems', 'json')
        if not DaraCore.is_null(tmp_req.video_urls):
            request.video_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_urls, 'VideoUrls', 'json')
        query = {}
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.candidate_items_shrink):
            query['CandidateItems'] = request.candidate_items_shrink
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.order_unique_id):
            query['OrderUniqueId'] = request.order_unique_id
        if not DaraCore.is_null(request.video_urls_shrink):
            query['VideoUrls'] = request.video_urls_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecognizeOrder',
            version = '2026-05-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecognizeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_order_with_options_async(
        self,
        tmp_req: main_models.RecognizeOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecognizeOrderResponse:
        tmp_req.validate()
        request = main_models.RecognizeOrderShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.candidate_items):
            request.candidate_items_shrink = Utils.array_to_string_with_specified_style(tmp_req.candidate_items, 'CandidateItems', 'json')
        if not DaraCore.is_null(tmp_req.video_urls):
            request.video_urls_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_urls, 'VideoUrls', 'json')
        query = {}
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.candidate_items_shrink):
            query['CandidateItems'] = request.candidate_items_shrink
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.order_unique_id):
            query['OrderUniqueId'] = request.order_unique_id
        if not DaraCore.is_null(request.video_urls_shrink):
            query['VideoUrls'] = request.video_urls_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecognizeOrder',
            version = '2026-05-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecognizeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_order(
        self,
        request: main_models.RecognizeOrderRequest,
    ) -> main_models.RecognizeOrderResponse:
        runtime = RuntimeOptions()
        return self.recognize_order_with_options(request, runtime)

    async def recognize_order_async(
        self,
        request: main_models.RecognizeOrderRequest,
    ) -> main_models.RecognizeOrderResponse:
        runtime = RuntimeOptions()
        return await self.recognize_order_with_options_async(request, runtime)

    def register_webhook_with_options(
        self,
        request: main_models.RegisterWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterWebhookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callback_secret):
            query['CallbackSecret'] = request.callback_secret
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterWebhook',
            version = '2026-05-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_webhook_with_options_async(
        self,
        request: main_models.RegisterWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterWebhookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callback_secret):
            query['CallbackSecret'] = request.callback_secret
        if not DaraCore.is_null(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterWebhook',
            version = '2026-05-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_webhook(
        self,
        request: main_models.RegisterWebhookRequest,
    ) -> main_models.RegisterWebhookResponse:
        runtime = RuntimeOptions()
        return self.register_webhook_with_options(request, runtime)

    async def register_webhook_async(
        self,
        request: main_models.RegisterWebhookRequest,
    ) -> main_models.RegisterWebhookResponse:
        runtime = RuntimeOptions()
        return await self.register_webhook_with_options_async(request, runtime)

    def update_product_with_options(
        self,
        tmp_req: main_models.UpdateProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProductResponse:
        tmp_req.validate()
        request = main_models.UpdateProductShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extra_images):
            request.extra_images_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra_images, 'ExtraImages', 'json')
        if not DaraCore.is_null(tmp_req.main_image):
            request.main_image_shrink = Utils.array_to_string_with_specified_style(tmp_req.main_image, 'MainImage', 'json')
        if not DaraCore.is_null(tmp_req.multi_view_images):
            request.multi_view_images_shrink = Utils.array_to_string_with_specified_style(tmp_req.multi_view_images, 'MultiViewImages', 'json')
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.extra_images_shrink):
            query['ExtraImages'] = request.extra_images_shrink
        if not DaraCore.is_null(request.image_title):
            query['ImageTitle'] = request.image_title
        if not DaraCore.is_null(request.item_unique_id):
            query['ItemUniqueId'] = request.item_unique_id
        if not DaraCore.is_null(request.main_image_shrink):
            query['MainImage'] = request.main_image_shrink
        if not DaraCore.is_null(request.multi_view_images_shrink):
            query['MultiViewImages'] = request.multi_view_images_shrink
        if not DaraCore.is_null(request.platform_item_id):
            query['PlatformItemId'] = request.platform_item_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProduct',
            version = '2026-05-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_product_with_options_async(
        self,
        tmp_req: main_models.UpdateProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProductResponse:
        tmp_req.validate()
        request = main_models.UpdateProductShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extra_images):
            request.extra_images_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra_images, 'ExtraImages', 'json')
        if not DaraCore.is_null(tmp_req.main_image):
            request.main_image_shrink = Utils.array_to_string_with_specified_style(tmp_req.main_image, 'MainImage', 'json')
        if not DaraCore.is_null(tmp_req.multi_view_images):
            request.multi_view_images_shrink = Utils.array_to_string_with_specified_style(tmp_req.multi_view_images, 'MultiViewImages', 'json')
        query = {}
        if not DaraCore.is_null(request.device_id):
            query['DeviceId'] = request.device_id
        if not DaraCore.is_null(request.extra_images_shrink):
            query['ExtraImages'] = request.extra_images_shrink
        if not DaraCore.is_null(request.image_title):
            query['ImageTitle'] = request.image_title
        if not DaraCore.is_null(request.item_unique_id):
            query['ItemUniqueId'] = request.item_unique_id
        if not DaraCore.is_null(request.main_image_shrink):
            query['MainImage'] = request.main_image_shrink
        if not DaraCore.is_null(request.multi_view_images_shrink):
            query['MultiViewImages'] = request.multi_view_images_shrink
        if not DaraCore.is_null(request.platform_item_id):
            query['PlatformItemId'] = request.platform_item_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProduct',
            version = '2026-05-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_product(
        self,
        request: main_models.UpdateProductRequest,
    ) -> main_models.UpdateProductResponse:
        runtime = RuntimeOptions()
        return self.update_product_with_options(request, runtime)

    async def update_product_async(
        self,
        request: main_models.UpdateProductRequest,
    ) -> main_models.UpdateProductResponse:
        runtime = RuntimeOptions()
        return await self.update_product_with_options_async(request, runtime)
