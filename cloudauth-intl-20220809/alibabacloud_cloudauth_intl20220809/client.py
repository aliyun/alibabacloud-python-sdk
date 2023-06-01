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

    def card_ocr_with_options(
        self,
        request: cloudauth_intl_20220809_models.CardOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.CardOcrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.doc_type):
            query['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.id_face_quality):
            query['IdFaceQuality'] = request.id_face_quality
        if not UtilClient.is_unset(request.id_ocr_picture_base_64):
            query['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        if not UtilClient.is_unset(request.id_ocr_picture_url):
            query['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.ocr):
            query['Ocr'] = request.ocr
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.spoof):
            query['Spoof'] = request.spoof
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CardOcr',
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
            cloudauth_intl_20220809_models.CardOcrResponse(),
            self.call_api(params, req, runtime)
        )

    async def card_ocr_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.CardOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.CardOcrResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.doc_type):
            query['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.id_face_quality):
            query['IdFaceQuality'] = request.id_face_quality
        if not UtilClient.is_unset(request.id_ocr_picture_base_64):
            query['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        if not UtilClient.is_unset(request.id_ocr_picture_url):
            query['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.ocr):
            query['Ocr'] = request.ocr
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.spoof):
            query['Spoof'] = request.spoof
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CardOcr',
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
            cloudauth_intl_20220809_models.CardOcrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def card_ocr(
        self,
        request: cloudauth_intl_20220809_models.CardOcrRequest,
    ) -> cloudauth_intl_20220809_models.CardOcrResponse:
        runtime = util_models.RuntimeOptions()
        return self.card_ocr_with_options(request, runtime)

    async def card_ocr_async(
        self,
        request: cloudauth_intl_20220809_models.CardOcrRequest,
    ) -> cloudauth_intl_20220809_models.CardOcrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.card_ocr_with_options_async(request, runtime)

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

    def describe_address_labels_with_options(
        self,
        request: cloudauth_intl_20220809_models.DescribeAddressLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DescribeAddressLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.coin):
            query['Coin'] = request.coin
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAddressLabels',
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
            cloudauth_intl_20220809_models.DescribeAddressLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_address_labels_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.DescribeAddressLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DescribeAddressLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.coin):
            query['Coin'] = request.coin
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAddressLabels',
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
            cloudauth_intl_20220809_models.DescribeAddressLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_address_labels(
        self,
        request: cloudauth_intl_20220809_models.DescribeAddressLabelsRequest,
    ) -> cloudauth_intl_20220809_models.DescribeAddressLabelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_address_labels_with_options(request, runtime)

    async def describe_address_labels_async(
        self,
        request: cloudauth_intl_20220809_models.DescribeAddressLabelsRequest,
    ) -> cloudauth_intl_20220809_models.DescribeAddressLabelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_address_labels_with_options_async(request, runtime)

    def describe_address_overview_with_options(
        self,
        request: cloudauth_intl_20220809_models.DescribeAddressOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DescribeAddressOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.coin):
            query['Coin'] = request.coin
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAddressOverview',
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
            cloudauth_intl_20220809_models.DescribeAddressOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_address_overview_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.DescribeAddressOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DescribeAddressOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.coin):
            query['Coin'] = request.coin
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAddressOverview',
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
            cloudauth_intl_20220809_models.DescribeAddressOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_address_overview(
        self,
        request: cloudauth_intl_20220809_models.DescribeAddressOverviewRequest,
    ) -> cloudauth_intl_20220809_models.DescribeAddressOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_address_overview_with_options(request, runtime)

    async def describe_address_overview_async(
        self,
        request: cloudauth_intl_20220809_models.DescribeAddressOverviewRequest,
    ) -> cloudauth_intl_20220809_models.DescribeAddressOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_address_overview_with_options_async(request, runtime)

    def describe_malicious_address_with_options(
        self,
        request: cloudauth_intl_20220809_models.DescribeMaliciousAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DescribeMaliciousAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coin):
            query['Coin'] = request.coin
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMaliciousAddress',
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
            cloudauth_intl_20220809_models.DescribeMaliciousAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_malicious_address_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.DescribeMaliciousAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DescribeMaliciousAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coin):
            query['Coin'] = request.coin
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMaliciousAddress',
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
            cloudauth_intl_20220809_models.DescribeMaliciousAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_malicious_address(
        self,
        request: cloudauth_intl_20220809_models.DescribeMaliciousAddressRequest,
    ) -> cloudauth_intl_20220809_models.DescribeMaliciousAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_malicious_address_with_options(request, runtime)

    async def describe_malicious_address_async(
        self,
        request: cloudauth_intl_20220809_models.DescribeMaliciousAddressRequest,
    ) -> cloudauth_intl_20220809_models.DescribeMaliciousAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_malicious_address_with_options_async(request, runtime)

    def describe_risk_score_with_options(
        self,
        request: cloudauth_intl_20220809_models.DescribeRiskScoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DescribeRiskScoreResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.coin):
            query['Coin'] = request.coin
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskScore',
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
            cloudauth_intl_20220809_models.DescribeRiskScoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_score_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.DescribeRiskScoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DescribeRiskScoreResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.coin):
            query['Coin'] = request.coin
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRiskScore',
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
            cloudauth_intl_20220809_models.DescribeRiskScoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_score(
        self,
        request: cloudauth_intl_20220809_models.DescribeRiskScoreRequest,
    ) -> cloudauth_intl_20220809_models.DescribeRiskScoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_score_with_options(request, runtime)

    async def describe_risk_score_async(
        self,
        request: cloudauth_intl_20220809_models.DescribeRiskScoreRequest,
    ) -> cloudauth_intl_20220809_models.DescribeRiskScoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_score_with_options_async(request, runtime)

    def describe_transactions_list_with_options(
        self,
        request: cloudauth_intl_20220809_models.DescribeTransactionsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DescribeTransactionsListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.coin):
            query['Coin'] = request.coin
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransactionsList',
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
            cloudauth_intl_20220809_models.DescribeTransactionsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transactions_list_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.DescribeTransactionsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DescribeTransactionsListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.coin):
            query['Coin'] = request.coin
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTransactionsList',
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
            cloudauth_intl_20220809_models.DescribeTransactionsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transactions_list(
        self,
        request: cloudauth_intl_20220809_models.DescribeTransactionsListRequest,
    ) -> cloudauth_intl_20220809_models.DescribeTransactionsListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_transactions_list_with_options(request, runtime)

    async def describe_transactions_list_async(
        self,
        request: cloudauth_intl_20220809_models.DescribeTransactionsListRequest,
    ) -> cloudauth_intl_20220809_models.DescribeTransactionsListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_transactions_list_with_options_async(request, runtime)

    def face_compare_with_options(
        self,
        request: cloudauth_intl_20220809_models.FaceCompareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.FaceCompareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.source_face_picture):
            query['SourceFacePicture'] = request.source_face_picture
        if not UtilClient.is_unset(request.source_face_picture_url):
            query['SourceFacePictureUrl'] = request.source_face_picture_url
        if not UtilClient.is_unset(request.target_face_picture):
            query['TargetFacePicture'] = request.target_face_picture
        if not UtilClient.is_unset(request.target_face_picture_url):
            query['TargetFacePictureUrl'] = request.target_face_picture_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FaceCompare',
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
            cloudauth_intl_20220809_models.FaceCompareResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_compare_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.FaceCompareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.FaceCompareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.source_face_picture):
            query['SourceFacePicture'] = request.source_face_picture
        if not UtilClient.is_unset(request.source_face_picture_url):
            query['SourceFacePictureUrl'] = request.source_face_picture_url
        if not UtilClient.is_unset(request.target_face_picture):
            query['TargetFacePicture'] = request.target_face_picture
        if not UtilClient.is_unset(request.target_face_picture_url):
            query['TargetFacePictureUrl'] = request.target_face_picture_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FaceCompare',
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
            cloudauth_intl_20220809_models.FaceCompareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_compare(
        self,
        request: cloudauth_intl_20220809_models.FaceCompareRequest,
    ) -> cloudauth_intl_20220809_models.FaceCompareResponse:
        runtime = util_models.RuntimeOptions()
        return self.face_compare_with_options(request, runtime)

    async def face_compare_async(
        self,
        request: cloudauth_intl_20220809_models.FaceCompareRequest,
    ) -> cloudauth_intl_20220809_models.FaceCompareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.face_compare_with_options_async(request, runtime)

    def face_liveness_with_options(
        self,
        request: cloudauth_intl_20220809_models.FaceLivenessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.FaceLivenessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.crop):
            query['Crop'] = request.crop
        if not UtilClient.is_unset(request.face_picture_base_64):
            query['FacePictureBase64'] = request.face_picture_base_64
        if not UtilClient.is_unset(request.face_picture_url):
            query['FacePictureUrl'] = request.face_picture_url
        if not UtilClient.is_unset(request.face_quality):
            query['FaceQuality'] = request.face_quality
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.occlusion):
            query['Occlusion'] = request.occlusion
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FaceLiveness',
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
            cloudauth_intl_20220809_models.FaceLivenessResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_liveness_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.FaceLivenessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.FaceLivenessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.crop):
            query['Crop'] = request.crop
        if not UtilClient.is_unset(request.face_picture_base_64):
            query['FacePictureBase64'] = request.face_picture_base_64
        if not UtilClient.is_unset(request.face_picture_url):
            query['FacePictureUrl'] = request.face_picture_url
        if not UtilClient.is_unset(request.face_quality):
            query['FaceQuality'] = request.face_quality
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.occlusion):
            query['Occlusion'] = request.occlusion
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FaceLiveness',
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
            cloudauth_intl_20220809_models.FaceLivenessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_liveness(
        self,
        request: cloudauth_intl_20220809_models.FaceLivenessRequest,
    ) -> cloudauth_intl_20220809_models.FaceLivenessResponse:
        runtime = util_models.RuntimeOptions()
        return self.face_liveness_with_options(request, runtime)

    async def face_liveness_async(
        self,
        request: cloudauth_intl_20220809_models.FaceLivenessRequest,
    ) -> cloudauth_intl_20220809_models.FaceLivenessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.face_liveness_with_options_async(request, runtime)

    def initialize_with_options(
        self,
        request: cloudauth_intl_20220809_models.InitializeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.InitializeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.crop):
            query['Crop'] = request.crop
        if not UtilClient.is_unset(request.doc_type):
            query['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.face_picture_base_64):
            query['FacePictureBase64'] = request.face_picture_base_64
        if not UtilClient.is_unset(request.face_picture_url):
            query['FacePictureUrl'] = request.face_picture_url
        if not UtilClient.is_unset(request.flow_type):
            query['FlowType'] = request.flow_type
        if not UtilClient.is_unset(request.id_face_quality):
            query['IdFaceQuality'] = request.id_face_quality
        if not UtilClient.is_unset(request.id_spoof):
            query['IdSpoof'] = request.id_spoof
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.meta_info):
            query['MetaInfo'] = request.meta_info
        if not UtilClient.is_unset(request.ocr):
            query['Ocr'] = request.ocr
        if not UtilClient.is_unset(request.operation_mode):
            query['OperationMode'] = request.operation_mode
        if not UtilClient.is_unset(request.pages):
            query['Pages'] = request.pages
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_config):
            query['ProductConfig'] = request.product_config
        if not UtilClient.is_unset(request.return_url):
            query['ReturnUrl'] = request.return_url
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
        if not UtilClient.is_unset(request.crop):
            query['Crop'] = request.crop
        if not UtilClient.is_unset(request.doc_type):
            query['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.face_picture_base_64):
            query['FacePictureBase64'] = request.face_picture_base_64
        if not UtilClient.is_unset(request.face_picture_url):
            query['FacePictureUrl'] = request.face_picture_url
        if not UtilClient.is_unset(request.flow_type):
            query['FlowType'] = request.flow_type
        if not UtilClient.is_unset(request.id_face_quality):
            query['IdFaceQuality'] = request.id_face_quality
        if not UtilClient.is_unset(request.id_spoof):
            query['IdSpoof'] = request.id_spoof
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.meta_info):
            query['MetaInfo'] = request.meta_info
        if not UtilClient.is_unset(request.ocr):
            query['Ocr'] = request.ocr
        if not UtilClient.is_unset(request.operation_mode):
            query['OperationMode'] = request.operation_mode
        if not UtilClient.is_unset(request.pages):
            query['Pages'] = request.pages
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_config):
            query['ProductConfig'] = request.product_config
        if not UtilClient.is_unset(request.return_url):
            query['ReturnUrl'] = request.return_url
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
