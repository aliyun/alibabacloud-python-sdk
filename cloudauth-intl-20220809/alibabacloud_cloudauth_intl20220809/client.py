# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudauth_intl20220809 import models as cloudauth_intl_20220809_models
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
        self._endpoint = self.get_endpoint('cloudauth-intl', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_result_with_options(
        self,
        request: cloudauth_intl_20220809_models.CheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.CheckResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extra_image_control_list):
            query['ExtraImageControlList'] = request.extra_image_control_list
        if not UtilClient.is_unset(request.is_return_image):
            query['IsReturnImage'] = request.is_return_image
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.return_five_category_spoof_result):
            query['ReturnFiveCategorySpoofResult'] = request.return_five_category_spoof_result
        if not UtilClient.is_unset(request.transaction_id):
            query['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckResult',
            version='2022-08-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_intl_20220809_models.CheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_result_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.CheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.CheckResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extra_image_control_list):
            query['ExtraImageControlList'] = request.extra_image_control_list
        if not UtilClient.is_unset(request.is_return_image):
            query['IsReturnImage'] = request.is_return_image
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.return_five_category_spoof_result):
            query['ReturnFiveCategorySpoofResult'] = request.return_five_category_spoof_result
        if not UtilClient.is_unset(request.transaction_id):
            query['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckResult',
            version='2022-08-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_intl_20220809_models.CheckResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_result(
        self,
        request: cloudauth_intl_20220809_models.CheckResultRequest,
    ) -> cloudauth_intl_20220809_models.CheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_result_with_options(request, runtime)

    async def check_result_async(
        self,
        request: cloudauth_intl_20220809_models.CheckResultRequest,
    ) -> cloudauth_intl_20220809_models.CheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_result_with_options_async(request, runtime)

    def initialize_with_options(
        self,
        request: cloudauth_intl_20220809_models.InitializeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.InitializeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.doc_type):
            query['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.flow_type):
            query['FlowType'] = request.flow_type
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.meta_info):
            query['MetaInfo'] = request.meta_info
        if not UtilClient.is_unset(request.operation_mode):
            query['OperationMode'] = request.operation_mode
        if not UtilClient.is_unset(request.pages):
            query['Pages'] = request.pages
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_config):
            query['ProductConfig'] = request.product_config
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.service_level):
            query['ServiceLevel'] = request.service_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Initialize',
            version='2022-08-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_intl_20220809_models.InitializeResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.InitializeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.InitializeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.doc_type):
            query['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.flow_type):
            query['FlowType'] = request.flow_type
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.meta_info):
            query['MetaInfo'] = request.meta_info
        if not UtilClient.is_unset(request.operation_mode):
            query['OperationMode'] = request.operation_mode
        if not UtilClient.is_unset(request.pages):
            query['Pages'] = request.pages
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_config):
            query['ProductConfig'] = request.product_config
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.service_level):
            query['ServiceLevel'] = request.service_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Initialize',
            version='2022-08-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_intl_20220809_models.InitializeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize(
        self,
        request: cloudauth_intl_20220809_models.InitializeRequest,
    ) -> cloudauth_intl_20220809_models.InitializeResponse:
        runtime = util_models.RuntimeOptions()
        return self.initialize_with_options(request, runtime)

    async def initialize_async(
        self,
        request: cloudauth_intl_20220809_models.InitializeRequest,
    ) -> cloudauth_intl_20220809_models.InitializeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.initialize_with_options_async(request, runtime)
