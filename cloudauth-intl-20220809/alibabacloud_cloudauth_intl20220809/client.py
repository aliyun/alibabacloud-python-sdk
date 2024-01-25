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
        """
        @deprecated : CardOcr is deprecated, please use Cloudauth-intl::2022-08-09::DocOcr instead.
        
        @param request: CardOcrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CardOcrResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.doc_type):
            query['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.id_face_quality):
            query['IdFaceQuality'] = request.id_face_quality
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
        body = {}
        if not UtilClient.is_unset(request.id_ocr_picture_base_64):
            body['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        """
        @deprecated : CardOcr is deprecated, please use Cloudauth-intl::2022-08-09::DocOcr instead.
        
        @param request: CardOcrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CardOcrResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.doc_type):
            query['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.id_face_quality):
            query['IdFaceQuality'] = request.id_face_quality
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
        body = {}
        if not UtilClient.is_unset(request.id_ocr_picture_base_64):
            body['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        """
        @deprecated : CardOcr is deprecated, please use Cloudauth-intl::2022-08-09::DocOcr instead.
        
        @param request: CardOcrRequest
        @return: CardOcrResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.card_ocr_with_options(request, runtime)

    async def card_ocr_async(
        self,
        request: cloudauth_intl_20220809_models.CardOcrRequest,
    ) -> cloudauth_intl_20220809_models.CardOcrResponse:
        """
        @deprecated : CardOcr is deprecated, please use Cloudauth-intl::2022-08-09::DocOcr instead.
        
        @param request: CardOcrRequest
        @return: CardOcrResponse
        Deprecated
        """
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

    def delete_picture_with_options(
        self,
        request: cloudauth_intl_20220809_models.DeletePictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DeletePictureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_pic_after_query):
            query['DeletePicAfterQuery'] = request.delete_pic_after_query
        if not UtilClient.is_unset(request.transaction_id):
            query['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePicture',
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
            cloudauth_intl_20220809_models.DeletePictureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_picture_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.DeletePictureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DeletePictureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_pic_after_query):
            query['DeletePicAfterQuery'] = request.delete_pic_after_query
        if not UtilClient.is_unset(request.transaction_id):
            query['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePicture',
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
            cloudauth_intl_20220809_models.DeletePictureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_picture(
        self,
        request: cloudauth_intl_20220809_models.DeletePictureRequest,
    ) -> cloudauth_intl_20220809_models.DeletePictureResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_picture_with_options(request, runtime)

    async def delete_picture_async(
        self,
        request: cloudauth_intl_20220809_models.DeletePictureRequest,
    ) -> cloudauth_intl_20220809_models.DeletePictureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_picture_with_options_async(request, runtime)

    def delete_verify_result_with_options(
        self,
        request: cloudauth_intl_20220809_models.DeleteVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DeleteVerifyResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_after_query):
            query['DeleteAfterQuery'] = request.delete_after_query
        if not UtilClient.is_unset(request.delete_type):
            query['DeleteType'] = request.delete_type
        if not UtilClient.is_unset(request.transaction_id):
            query['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVerifyResult',
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
            cloudauth_intl_20220809_models.DeleteVerifyResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_verify_result_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.DeleteVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DeleteVerifyResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_after_query):
            query['DeleteAfterQuery'] = request.delete_after_query
        if not UtilClient.is_unset(request.delete_type):
            query['DeleteType'] = request.delete_type
        if not UtilClient.is_unset(request.transaction_id):
            query['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVerifyResult',
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
            cloudauth_intl_20220809_models.DeleteVerifyResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_verify_result(
        self,
        request: cloudauth_intl_20220809_models.DeleteVerifyResultRequest,
    ) -> cloudauth_intl_20220809_models.DeleteVerifyResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_verify_result_with_options(request, runtime)

    async def delete_verify_result_async(
        self,
        request: cloudauth_intl_20220809_models.DeleteVerifyResultRequest,
    ) -> cloudauth_intl_20220809_models.DeleteVerifyResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_verify_result_with_options_async(request, runtime)

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

    def describe_web_3address_labels_with_options(
        self,
        request: cloudauth_intl_20220809_models.DescribeWeb3AddressLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DescribeWeb3AddressLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.chain_short_name):
            query['ChainShortName'] = request.chain_short_name
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWeb3AddressLabels',
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
            cloudauth_intl_20220809_models.DescribeWeb3AddressLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_3address_labels_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.DescribeWeb3AddressLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DescribeWeb3AddressLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.chain_short_name):
            query['ChainShortName'] = request.chain_short_name
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWeb3AddressLabels',
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
            cloudauth_intl_20220809_models.DescribeWeb3AddressLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_3address_labels(
        self,
        request: cloudauth_intl_20220809_models.DescribeWeb3AddressLabelsRequest,
    ) -> cloudauth_intl_20220809_models.DescribeWeb3AddressLabelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_3address_labels_with_options(request, runtime)

    async def describe_web_3address_labels_async(
        self,
        request: cloudauth_intl_20220809_models.DescribeWeb3AddressLabelsRequest,
    ) -> cloudauth_intl_20220809_models.DescribeWeb3AddressLabelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_3address_labels_with_options_async(request, runtime)

    def describe_web_3risk_score_with_options(
        self,
        request: cloudauth_intl_20220809_models.DescribeWeb3RiskScoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DescribeWeb3RiskScoreResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chain_short_name):
            query['ChainShortName'] = request.chain_short_name
        if not UtilClient.is_unset(request.depth):
            query['Depth'] = request.depth
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWeb3RiskScore',
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
            cloudauth_intl_20220809_models.DescribeWeb3RiskScoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_3risk_score_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.DescribeWeb3RiskScoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DescribeWeb3RiskScoreResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chain_short_name):
            query['ChainShortName'] = request.chain_short_name
        if not UtilClient.is_unset(request.depth):
            query['Depth'] = request.depth
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWeb3RiskScore',
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
            cloudauth_intl_20220809_models.DescribeWeb3RiskScoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_3risk_score(
        self,
        request: cloudauth_intl_20220809_models.DescribeWeb3RiskScoreRequest,
    ) -> cloudauth_intl_20220809_models.DescribeWeb3RiskScoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_3risk_score_with_options(request, runtime)

    async def describe_web_3risk_score_async(
        self,
        request: cloudauth_intl_20220809_models.DescribeWeb3RiskScoreRequest,
    ) -> cloudauth_intl_20220809_models.DescribeWeb3RiskScoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_3risk_score_with_options_async(request, runtime)

    def describe_web_3transaction_labels_with_options(
        self,
        request: cloudauth_intl_20220809_models.DescribeWeb3TransactionLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DescribeWeb3TransactionLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chain_short_name):
            query['ChainShortName'] = request.chain_short_name
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.transaction):
            query['Transaction'] = request.transaction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWeb3TransactionLabels',
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
            cloudauth_intl_20220809_models.DescribeWeb3TransactionLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_web_3transaction_labels_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.DescribeWeb3TransactionLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DescribeWeb3TransactionLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chain_short_name):
            query['ChainShortName'] = request.chain_short_name
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.transaction):
            query['Transaction'] = request.transaction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWeb3TransactionLabels',
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
            cloudauth_intl_20220809_models.DescribeWeb3TransactionLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_web_3transaction_labels(
        self,
        request: cloudauth_intl_20220809_models.DescribeWeb3TransactionLabelsRequest,
    ) -> cloudauth_intl_20220809_models.DescribeWeb3TransactionLabelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_web_3transaction_labels_with_options(request, runtime)

    async def describe_web_3transaction_labels_async(
        self,
        request: cloudauth_intl_20220809_models.DescribeWeb3TransactionLabelsRequest,
    ) -> cloudauth_intl_20220809_models.DescribeWeb3TransactionLabelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_web_3transaction_labels_with_options_async(request, runtime)

    def doc_ocr_with_options(
        self,
        request: cloudauth_intl_20220809_models.DocOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DocOcrResponse:
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
            action='DocOcr',
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
            cloudauth_intl_20220809_models.DocOcrResponse(),
            self.call_api(params, req, runtime)
        )

    async def doc_ocr_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.DocOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DocOcrResponse:
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
            action='DocOcr',
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
            cloudauth_intl_20220809_models.DocOcrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def doc_ocr(
        self,
        request: cloudauth_intl_20220809_models.DocOcrRequest,
    ) -> cloudauth_intl_20220809_models.DocOcrResponse:
        runtime = util_models.RuntimeOptions()
        return self.doc_ocr_with_options(request, runtime)

    async def doc_ocr_async(
        self,
        request: cloudauth_intl_20220809_models.DocOcrRequest,
    ) -> cloudauth_intl_20220809_models.DocOcrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.doc_ocr_with_options_async(request, runtime)

    def ekyc_verify_with_options(
        self,
        request: cloudauth_intl_20220809_models.EkycVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.EkycVerifyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorize):
            query['Authorize'] = request.authorize
        if not UtilClient.is_unset(request.crop):
            query['Crop'] = request.crop
        if not UtilClient.is_unset(request.doc_name):
            query['DocName'] = request.doc_name
        if not UtilClient.is_unset(request.doc_no):
            query['DocNo'] = request.doc_no
        if not UtilClient.is_unset(request.doc_type):
            query['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.face_picture_base_64):
            query['FacePictureBase64'] = request.face_picture_base_64
        if not UtilClient.is_unset(request.face_picture_url):
            query['FacePictureUrl'] = request.face_picture_url
        if not UtilClient.is_unset(request.id_ocr_picture_base_64):
            query['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        if not UtilClient.is_unset(request.id_ocr_picture_url):
            query['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EkycVerify',
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
            cloudauth_intl_20220809_models.EkycVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def ekyc_verify_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.EkycVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.EkycVerifyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorize):
            query['Authorize'] = request.authorize
        if not UtilClient.is_unset(request.crop):
            query['Crop'] = request.crop
        if not UtilClient.is_unset(request.doc_name):
            query['DocName'] = request.doc_name
        if not UtilClient.is_unset(request.doc_no):
            query['DocNo'] = request.doc_no
        if not UtilClient.is_unset(request.doc_type):
            query['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.face_picture_base_64):
            query['FacePictureBase64'] = request.face_picture_base_64
        if not UtilClient.is_unset(request.face_picture_url):
            query['FacePictureUrl'] = request.face_picture_url
        if not UtilClient.is_unset(request.id_ocr_picture_base_64):
            query['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        if not UtilClient.is_unset(request.id_ocr_picture_url):
            query['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EkycVerify',
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
            cloudauth_intl_20220809_models.EkycVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ekyc_verify(
        self,
        request: cloudauth_intl_20220809_models.EkycVerifyRequest,
    ) -> cloudauth_intl_20220809_models.EkycVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.ekyc_verify_with_options(request, runtime)

    async def ekyc_verify_async(
        self,
        request: cloudauth_intl_20220809_models.EkycVerifyRequest,
    ) -> cloudauth_intl_20220809_models.EkycVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ekyc_verify_with_options_async(request, runtime)

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
        body = {}
        if not UtilClient.is_unset(request.face_picture_base_64):
            body['FacePictureBase64'] = request.face_picture_base_64
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        body = {}
        if not UtilClient.is_unset(request.face_picture_base_64):
            body['FacePictureBase64'] = request.face_picture_base_64
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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

    def fraud_result_call_back_with_options(
        self,
        request: cloudauth_intl_20220809_models.FraudResultCallBackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.FraudResultCallBackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.ext_params):
            query['ExtParams'] = request.ext_params
        if not UtilClient.is_unset(request.result_code):
            query['ResultCode'] = request.result_code
        if not UtilClient.is_unset(request.verify_deploy_env):
            query['VerifyDeployEnv'] = request.verify_deploy_env
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FraudResultCallBack',
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
            cloudauth_intl_20220809_models.FraudResultCallBackResponse(),
            self.call_api(params, req, runtime)
        )

    async def fraud_result_call_back_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.FraudResultCallBackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.FraudResultCallBackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.ext_params):
            query['ExtParams'] = request.ext_params
        if not UtilClient.is_unset(request.result_code):
            query['ResultCode'] = request.result_code
        if not UtilClient.is_unset(request.verify_deploy_env):
            query['VerifyDeployEnv'] = request.verify_deploy_env
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FraudResultCallBack',
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
            cloudauth_intl_20220809_models.FraudResultCallBackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fraud_result_call_back(
        self,
        request: cloudauth_intl_20220809_models.FraudResultCallBackRequest,
    ) -> cloudauth_intl_20220809_models.FraudResultCallBackResponse:
        runtime = util_models.RuntimeOptions()
        return self.fraud_result_call_back_with_options(request, runtime)

    async def fraud_result_call_back_async(
        self,
        request: cloudauth_intl_20220809_models.FraudResultCallBackRequest,
    ) -> cloudauth_intl_20220809_models.FraudResultCallBackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.fraud_result_call_back_with_options_async(request, runtime)

    def id_2meta_verify_intl_with_options(
        self,
        request: cloudauth_intl_20220809_models.Id2MetaVerifyIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.Id2MetaVerifyIntlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Id2MetaVerifyIntl',
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
            cloudauth_intl_20220809_models.Id2MetaVerifyIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def id_2meta_verify_intl_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.Id2MetaVerifyIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.Id2MetaVerifyIntlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Id2MetaVerifyIntl',
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
            cloudauth_intl_20220809_models.Id2MetaVerifyIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def id_2meta_verify_intl(
        self,
        request: cloudauth_intl_20220809_models.Id2MetaVerifyIntlRequest,
    ) -> cloudauth_intl_20220809_models.Id2MetaVerifyIntlResponse:
        runtime = util_models.RuntimeOptions()
        return self.id_2meta_verify_intl_with_options(request, runtime)

    async def id_2meta_verify_intl_async(
        self,
        request: cloudauth_intl_20220809_models.Id2MetaVerifyIntlRequest,
    ) -> cloudauth_intl_20220809_models.Id2MetaVerifyIntlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.id_2meta_verify_intl_with_options_async(request, runtime)

    def initialize_with_options(
        self,
        request: cloudauth_intl_20220809_models.InitializeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.InitializeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorize):
            query['Authorize'] = request.authorize
        if not UtilClient.is_unset(request.callback_token):
            query['CallbackToken'] = request.callback_token
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.crop):
            query['Crop'] = request.crop
        if not UtilClient.is_unset(request.doc_scan_mode):
            query['DocScanMode'] = request.doc_scan_mode
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
        if not UtilClient.is_unset(request.language_config):
            query['LanguageConfig'] = request.language_config
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
        if not UtilClient.is_unset(request.product_flow):
            query['ProductFlow'] = request.product_flow
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
        if not UtilClient.is_unset(request.authorize):
            query['Authorize'] = request.authorize
        if not UtilClient.is_unset(request.callback_token):
            query['CallbackToken'] = request.callback_token
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.crop):
            query['Crop'] = request.crop
        if not UtilClient.is_unset(request.doc_scan_mode):
            query['DocScanMode'] = request.doc_scan_mode
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
        if not UtilClient.is_unset(request.language_config):
            query['LanguageConfig'] = request.language_config
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
        if not UtilClient.is_unset(request.product_flow):
            query['ProductFlow'] = request.product_flow
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

    def mobile_3meta_verify_intl_with_options(
        self,
        request: cloudauth_intl_20220809_models.Mobile3MetaVerifyIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.Mobile3MetaVerifyIntlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Mobile3MetaVerifyIntl',
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
            cloudauth_intl_20220809_models.Mobile3MetaVerifyIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_3meta_verify_intl_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.Mobile3MetaVerifyIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.Mobile3MetaVerifyIntlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Mobile3MetaVerifyIntl',
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
            cloudauth_intl_20220809_models.Mobile3MetaVerifyIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_3meta_verify_intl(
        self,
        request: cloudauth_intl_20220809_models.Mobile3MetaVerifyIntlRequest,
    ) -> cloudauth_intl_20220809_models.Mobile3MetaVerifyIntlResponse:
        runtime = util_models.RuntimeOptions()
        return self.mobile_3meta_verify_intl_with_options(request, runtime)

    async def mobile_3meta_verify_intl_async(
        self,
        request: cloudauth_intl_20220809_models.Mobile3MetaVerifyIntlRequest,
    ) -> cloudauth_intl_20220809_models.Mobile3MetaVerifyIntlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.mobile_3meta_verify_intl_with_options_async(request, runtime)
