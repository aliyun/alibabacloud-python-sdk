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
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_oss_sdk.client import Client as OSSClient
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models


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
        @deprecated OpenAPI CardOcr is deprecated, please use Cloudauth-intl::2022-08-09::DocOcr instead.
        
        @summary 证件OCR识别纯服务端接口
        
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
        @deprecated OpenAPI CardOcr is deprecated, please use Cloudauth-intl::2022-08-09::DocOcr instead.
        
        @summary 证件OCR识别纯服务端接口
        
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
        @deprecated OpenAPI CardOcr is deprecated, please use Cloudauth-intl::2022-08-09::DocOcr instead.
        
        @summary 证件OCR识别纯服务端接口
        
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
        @deprecated OpenAPI CardOcr is deprecated, please use Cloudauth-intl::2022-08-09::DocOcr instead.
        
        @summary 证件OCR识别纯服务端接口
        
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
        """
        @summary 结果查询
        
        @param request: CheckResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckResultResponse
        """
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
        """
        @summary 结果查询
        
        @param request: CheckResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckResultResponse
        """
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
        """
        @summary 结果查询
        
        @param request: CheckResultRequest
        @return: CheckResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_result_with_options(request, runtime)

    async def check_result_async(
        self,
        request: cloudauth_intl_20220809_models.CheckResultRequest,
    ) -> cloudauth_intl_20220809_models.CheckResultResponse:
        """
        @summary 结果查询
        
        @param request: CheckResultRequest
        @return: CheckResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_result_with_options_async(request, runtime)

    def check_verify_log_with_options(
        self,
        request: cloudauth_intl_20220809_models.CheckVerifyLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.CheckVerifyLogResponse:
        """
        @summary 认证日志查询接口
        
        @param request: CheckVerifyLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckVerifyLogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.merchant_biz_id):
            body['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckVerifyLog',
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
            cloudauth_intl_20220809_models.CheckVerifyLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_verify_log_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.CheckVerifyLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.CheckVerifyLogResponse:
        """
        @summary 认证日志查询接口
        
        @param request: CheckVerifyLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckVerifyLogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.merchant_biz_id):
            body['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.transaction_id):
            body['TransactionId'] = request.transaction_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckVerifyLog',
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
            cloudauth_intl_20220809_models.CheckVerifyLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_verify_log(
        self,
        request: cloudauth_intl_20220809_models.CheckVerifyLogRequest,
    ) -> cloudauth_intl_20220809_models.CheckVerifyLogResponse:
        """
        @summary 认证日志查询接口
        
        @param request: CheckVerifyLogRequest
        @return: CheckVerifyLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_verify_log_with_options(request, runtime)

    async def check_verify_log_async(
        self,
        request: cloudauth_intl_20220809_models.CheckVerifyLogRequest,
    ) -> cloudauth_intl_20220809_models.CheckVerifyLogResponse:
        """
        @summary 认证日志查询接口
        
        @param request: CheckVerifyLogRequest
        @return: CheckVerifyLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_verify_log_with_options_async(request, runtime)

    def credential_verify_intl_with_options(
        self,
        request: cloudauth_intl_20220809_models.CredentialVerifyIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.CredentialVerifyIntlResponse:
        """
        @summary 凭证核验
        
        @param request: CredentialVerifyIntlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CredentialVerifyIntlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cred_name):
            query['CredName'] = request.cred_name
        if not UtilClient.is_unset(request.cred_type):
            query['CredType'] = request.cred_type
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        body = {}
        if not UtilClient.is_unset(request.image_file):
            body['ImageFile'] = request.image_file
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CredentialVerifyIntl',
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
            cloudauth_intl_20220809_models.CredentialVerifyIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def credential_verify_intl_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.CredentialVerifyIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.CredentialVerifyIntlResponse:
        """
        @summary 凭证核验
        
        @param request: CredentialVerifyIntlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CredentialVerifyIntlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cred_name):
            query['CredName'] = request.cred_name
        if not UtilClient.is_unset(request.cred_type):
            query['CredType'] = request.cred_type
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        body = {}
        if not UtilClient.is_unset(request.image_file):
            body['ImageFile'] = request.image_file
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CredentialVerifyIntl',
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
            cloudauth_intl_20220809_models.CredentialVerifyIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def credential_verify_intl(
        self,
        request: cloudauth_intl_20220809_models.CredentialVerifyIntlRequest,
    ) -> cloudauth_intl_20220809_models.CredentialVerifyIntlResponse:
        """
        @summary 凭证核验
        
        @param request: CredentialVerifyIntlRequest
        @return: CredentialVerifyIntlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.credential_verify_intl_with_options(request, runtime)

    async def credential_verify_intl_async(
        self,
        request: cloudauth_intl_20220809_models.CredentialVerifyIntlRequest,
    ) -> cloudauth_intl_20220809_models.CredentialVerifyIntlResponse:
        """
        @summary 凭证核验
        
        @param request: CredentialVerifyIntlRequest
        @return: CredentialVerifyIntlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.credential_verify_intl_with_options_async(request, runtime)

    def credential_verify_intl_advance(
        self,
        request: cloudauth_intl_20220809_models.CredentialVerifyIntlAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.CredentialVerifyIntlResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='Cloudauth-intl',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        credential_verify_intl_req = cloudauth_intl_20220809_models.CredentialVerifyIntlRequest()
        OpenApiUtilClient.convert(request, credential_verify_intl_req)
        if not UtilClient.is_unset(request.image_file_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_file_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            credential_verify_intl_req.image_file = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        credential_verify_intl_resp = self.credential_verify_intl_with_options(credential_verify_intl_req, runtime)
        return credential_verify_intl_resp

    async def credential_verify_intl_advance_async(
        self,
        request: cloudauth_intl_20220809_models.CredentialVerifyIntlAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.CredentialVerifyIntlResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='Cloudauth-intl',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        credential_verify_intl_req = cloudauth_intl_20220809_models.CredentialVerifyIntlRequest()
        OpenApiUtilClient.convert(request, credential_verify_intl_req)
        if not UtilClient.is_unset(request.image_file_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_file_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            credential_verify_intl_req.image_file = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        credential_verify_intl_resp = await self.credential_verify_intl_with_options_async(credential_verify_intl_req, runtime)
        return credential_verify_intl_resp

    def deepfake_detect_intl_with_options(
        self,
        request: cloudauth_intl_20220809_models.DeepfakeDetectIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DeepfakeDetectIntlResponse:
        """
        @summary 人脸凭证核验
        
        @param request: DeepfakeDetectIntlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeepfakeDetectIntlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_input_type):
            query['FaceInputType'] = request.face_input_type
        if not UtilClient.is_unset(request.face_url):
            query['FaceUrl'] = request.face_url
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        body = {}
        if not UtilClient.is_unset(request.face_base_64):
            body['FaceBase64'] = request.face_base_64
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeepfakeDetectIntl',
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
            cloudauth_intl_20220809_models.DeepfakeDetectIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def deepfake_detect_intl_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.DeepfakeDetectIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DeepfakeDetectIntlResponse:
        """
        @summary 人脸凭证核验
        
        @param request: DeepfakeDetectIntlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeepfakeDetectIntlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_input_type):
            query['FaceInputType'] = request.face_input_type
        if not UtilClient.is_unset(request.face_url):
            query['FaceUrl'] = request.face_url
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        body = {}
        if not UtilClient.is_unset(request.face_base_64):
            body['FaceBase64'] = request.face_base_64
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeepfakeDetectIntl',
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
            cloudauth_intl_20220809_models.DeepfakeDetectIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deepfake_detect_intl(
        self,
        request: cloudauth_intl_20220809_models.DeepfakeDetectIntlRequest,
    ) -> cloudauth_intl_20220809_models.DeepfakeDetectIntlResponse:
        """
        @summary 人脸凭证核验
        
        @param request: DeepfakeDetectIntlRequest
        @return: DeepfakeDetectIntlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deepfake_detect_intl_with_options(request, runtime)

    async def deepfake_detect_intl_async(
        self,
        request: cloudauth_intl_20220809_models.DeepfakeDetectIntlRequest,
    ) -> cloudauth_intl_20220809_models.DeepfakeDetectIntlResponse:
        """
        @summary 人脸凭证核验
        
        @param request: DeepfakeDetectIntlRequest
        @return: DeepfakeDetectIntlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deepfake_detect_intl_with_options_async(request, runtime)

    def delete_verify_result_with_options(
        self,
        request: cloudauth_intl_20220809_models.DeleteVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DeleteVerifyResultResponse:
        """
        @summary 删除用户认证记录结果
        
        @param request: DeleteVerifyResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVerifyResultResponse
        """
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
        """
        @summary 删除用户认证记录结果
        
        @param request: DeleteVerifyResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVerifyResultResponse
        """
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
        """
        @summary 删除用户认证记录结果
        
        @param request: DeleteVerifyResultRequest
        @return: DeleteVerifyResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_verify_result_with_options(request, runtime)

    async def delete_verify_result_async(
        self,
        request: cloudauth_intl_20220809_models.DeleteVerifyResultRequest,
    ) -> cloudauth_intl_20220809_models.DeleteVerifyResultResponse:
        """
        @summary 删除用户认证记录结果
        
        @param request: DeleteVerifyResultRequest
        @return: DeleteVerifyResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_verify_result_with_options_async(request, runtime)

    def doc_ocr_with_options(
        self,
        request: cloudauth_intl_20220809_models.DocOcrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DocOcrResponse:
        """
        @summary 卡证ocr纯服务端
        
        @param request: DocOcrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DocOcrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.card_side):
            query['CardSide'] = request.card_side
        if not UtilClient.is_unset(request.doc_type):
            query['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.id_face_quality):
            query['IdFaceQuality'] = request.id_face_quality
        if not UtilClient.is_unset(request.id_ocr_picture_url):
            query['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not UtilClient.is_unset(request.id_threshold):
            query['IdThreshold'] = request.id_threshold
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
        """
        @summary 卡证ocr纯服务端
        
        @param request: DocOcrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DocOcrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.card_side):
            query['CardSide'] = request.card_side
        if not UtilClient.is_unset(request.doc_type):
            query['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.id_face_quality):
            query['IdFaceQuality'] = request.id_face_quality
        if not UtilClient.is_unset(request.id_ocr_picture_url):
            query['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not UtilClient.is_unset(request.id_threshold):
            query['IdThreshold'] = request.id_threshold
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
        """
        @summary 卡证ocr纯服务端
        
        @param request: DocOcrRequest
        @return: DocOcrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.doc_ocr_with_options(request, runtime)

    async def doc_ocr_async(
        self,
        request: cloudauth_intl_20220809_models.DocOcrRequest,
    ) -> cloudauth_intl_20220809_models.DocOcrResponse:
        """
        @summary 卡证ocr纯服务端
        
        @param request: DocOcrRequest
        @return: DocOcrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.doc_ocr_with_options_async(request, runtime)

    def doc_ocr_max_with_options(
        self,
        request: cloudauth_intl_20220809_models.DocOcrMaxRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DocOcrMaxResponse:
        """
        @summary 全球证件ocr识别接口
        
        @param request: DocOcrMaxRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DocOcrMaxResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.id_ocr_picture_base_64):
            body['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        if not UtilClient.is_unset(request.id_ocr_picture_url):
            body['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not UtilClient.is_unset(request.id_threshold):
            body['IdThreshold'] = request.id_threshold
        if not UtilClient.is_unset(request.merchant_biz_id):
            body['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            body['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.ocr_model):
            body['OcrModel'] = request.ocr_model
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.scene_code):
            body['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.spoof):
            body['Spoof'] = request.spoof
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DocOcrMax',
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
            cloudauth_intl_20220809_models.DocOcrMaxResponse(),
            self.call_api(params, req, runtime)
        )

    async def doc_ocr_max_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.DocOcrMaxRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.DocOcrMaxResponse:
        """
        @summary 全球证件ocr识别接口
        
        @param request: DocOcrMaxRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DocOcrMaxResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.id_ocr_picture_base_64):
            body['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        if not UtilClient.is_unset(request.id_ocr_picture_url):
            body['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not UtilClient.is_unset(request.id_threshold):
            body['IdThreshold'] = request.id_threshold
        if not UtilClient.is_unset(request.merchant_biz_id):
            body['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            body['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.ocr_model):
            body['OcrModel'] = request.ocr_model
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.prompt):
            body['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.scene_code):
            body['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.spoof):
            body['Spoof'] = request.spoof
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DocOcrMax',
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
            cloudauth_intl_20220809_models.DocOcrMaxResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def doc_ocr_max(
        self,
        request: cloudauth_intl_20220809_models.DocOcrMaxRequest,
    ) -> cloudauth_intl_20220809_models.DocOcrMaxResponse:
        """
        @summary 全球证件ocr识别接口
        
        @param request: DocOcrMaxRequest
        @return: DocOcrMaxResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.doc_ocr_max_with_options(request, runtime)

    async def doc_ocr_max_async(
        self,
        request: cloudauth_intl_20220809_models.DocOcrMaxRequest,
    ) -> cloudauth_intl_20220809_models.DocOcrMaxResponse:
        """
        @summary 全球证件ocr识别接口
        
        @param request: DocOcrMaxRequest
        @return: DocOcrMaxResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.doc_ocr_max_with_options_async(request, runtime)

    def ekyc_verify_with_options(
        self,
        request: cloudauth_intl_20220809_models.EkycVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.EkycVerifyResponse:
        """
        @summary ekyc纯服务端接口
        
        @param request: EkycVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EkycVerifyResponse
        """
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
        if not UtilClient.is_unset(request.face_picture_url):
            query['FacePictureUrl'] = request.face_picture_url
        if not UtilClient.is_unset(request.id_ocr_picture_url):
            query['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not UtilClient.is_unset(request.id_threshold):
            query['IdThreshold'] = request.id_threshold
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        body = {}
        if not UtilClient.is_unset(request.face_picture_base_64):
            body['FacePictureBase64'] = request.face_picture_base_64
        if not UtilClient.is_unset(request.id_ocr_picture_base_64):
            body['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        """
        @summary ekyc纯服务端接口
        
        @param request: EkycVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EkycVerifyResponse
        """
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
        if not UtilClient.is_unset(request.face_picture_url):
            query['FacePictureUrl'] = request.face_picture_url
        if not UtilClient.is_unset(request.id_ocr_picture_url):
            query['IdOcrPictureUrl'] = request.id_ocr_picture_url
        if not UtilClient.is_unset(request.id_threshold):
            query['IdThreshold'] = request.id_threshold
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        body = {}
        if not UtilClient.is_unset(request.face_picture_base_64):
            body['FacePictureBase64'] = request.face_picture_base_64
        if not UtilClient.is_unset(request.id_ocr_picture_base_64):
            body['IdOcrPictureBase64'] = request.id_ocr_picture_base_64
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        """
        @summary ekyc纯服务端接口
        
        @param request: EkycVerifyRequest
        @return: EkycVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.ekyc_verify_with_options(request, runtime)

    async def ekyc_verify_async(
        self,
        request: cloudauth_intl_20220809_models.EkycVerifyRequest,
    ) -> cloudauth_intl_20220809_models.EkycVerifyResponse:
        """
        @summary ekyc纯服务端接口
        
        @param request: EkycVerifyRequest
        @return: EkycVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.ekyc_verify_with_options_async(request, runtime)

    def face_compare_with_options(
        self,
        request: cloudauth_intl_20220809_models.FaceCompareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.FaceCompareResponse:
        """
        @summary 人脸比对
        
        @param request: FaceCompareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FaceCompareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.source_face_picture_url):
            query['SourceFacePictureUrl'] = request.source_face_picture_url
        if not UtilClient.is_unset(request.target_face_picture_url):
            query['TargetFacePictureUrl'] = request.target_face_picture_url
        body = {}
        if not UtilClient.is_unset(request.source_face_picture):
            body['SourceFacePicture'] = request.source_face_picture
        if not UtilClient.is_unset(request.target_face_picture):
            body['TargetFacePicture'] = request.target_face_picture
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        """
        @summary 人脸比对
        
        @param request: FaceCompareRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FaceCompareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.source_face_picture_url):
            query['SourceFacePictureUrl'] = request.source_face_picture_url
        if not UtilClient.is_unset(request.target_face_picture_url):
            query['TargetFacePictureUrl'] = request.target_face_picture_url
        body = {}
        if not UtilClient.is_unset(request.source_face_picture):
            body['SourceFacePicture'] = request.source_face_picture
        if not UtilClient.is_unset(request.target_face_picture):
            body['TargetFacePicture'] = request.target_face_picture
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        """
        @summary 人脸比对
        
        @param request: FaceCompareRequest
        @return: FaceCompareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.face_compare_with_options(request, runtime)

    async def face_compare_async(
        self,
        request: cloudauth_intl_20220809_models.FaceCompareRequest,
    ) -> cloudauth_intl_20220809_models.FaceCompareResponse:
        """
        @summary 人脸比对
        
        @param request: FaceCompareRequest
        @return: FaceCompareResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.face_compare_with_options_async(request, runtime)

    def face_guard_risk_with_options(
        self,
        request: cloudauth_intl_20220809_models.FaceGuardRiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.FaceGuardRiskResponse:
        """
        @summary 国际人脸保镖纯服务端接口
        
        @param request: FaceGuardRiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FaceGuardRiskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.device_token):
            query['DeviceToken'] = request.device_token
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FaceGuardRisk',
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
            cloudauth_intl_20220809_models.FaceGuardRiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_guard_risk_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.FaceGuardRiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.FaceGuardRiskResponse:
        """
        @summary 国际人脸保镖纯服务端接口
        
        @param request: FaceGuardRiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FaceGuardRiskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.device_token):
            query['DeviceToken'] = request.device_token
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FaceGuardRisk',
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
            cloudauth_intl_20220809_models.FaceGuardRiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_guard_risk(
        self,
        request: cloudauth_intl_20220809_models.FaceGuardRiskRequest,
    ) -> cloudauth_intl_20220809_models.FaceGuardRiskResponse:
        """
        @summary 国际人脸保镖纯服务端接口
        
        @param request: FaceGuardRiskRequest
        @return: FaceGuardRiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.face_guard_risk_with_options(request, runtime)

    async def face_guard_risk_async(
        self,
        request: cloudauth_intl_20220809_models.FaceGuardRiskRequest,
    ) -> cloudauth_intl_20220809_models.FaceGuardRiskResponse:
        """
        @summary 国际人脸保镖纯服务端接口
        
        @param request: FaceGuardRiskRequest
        @return: FaceGuardRiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.face_guard_risk_with_options_async(request, runtime)

    def face_liveness_with_options(
        self,
        request: cloudauth_intl_20220809_models.FaceLivenessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.FaceLivenessResponse:
        """
        @summary 静默活体API 纯服务端
        
        @param request: FaceLivenessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FaceLivenessResponse
        """
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
        """
        @summary 静默活体API 纯服务端
        
        @param request: FaceLivenessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FaceLivenessResponse
        """
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
        """
        @summary 静默活体API 纯服务端
        
        @param request: FaceLivenessRequest
        @return: FaceLivenessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.face_liveness_with_options(request, runtime)

    async def face_liveness_async(
        self,
        request: cloudauth_intl_20220809_models.FaceLivenessRequest,
    ) -> cloudauth_intl_20220809_models.FaceLivenessResponse:
        """
        @summary 静默活体API 纯服务端
        
        @param request: FaceLivenessRequest
        @return: FaceLivenessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.face_liveness_with_options_async(request, runtime)

    def fraud_result_call_back_with_options(
        self,
        request: cloudauth_intl_20220809_models.FraudResultCallBackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.FraudResultCallBackResponse:
        """
        @summary 防伪回调接口
        
        @param request: FraudResultCallBackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FraudResultCallBackResponse
        """
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
        """
        @summary 防伪回调接口
        
        @param request: FraudResultCallBackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FraudResultCallBackResponse
        """
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
        """
        @summary 防伪回调接口
        
        @param request: FraudResultCallBackRequest
        @return: FraudResultCallBackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.fraud_result_call_back_with_options(request, runtime)

    async def fraud_result_call_back_async(
        self,
        request: cloudauth_intl_20220809_models.FraudResultCallBackRequest,
    ) -> cloudauth_intl_20220809_models.FraudResultCallBackResponse:
        """
        @summary 防伪回调接口
        
        @param request: FraudResultCallBackRequest
        @return: FraudResultCallBackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.fraud_result_call_back_with_options_async(request, runtime)

    def id_2meta_period_verify_intl_with_options(
        self,
        request: cloudauth_intl_20220809_models.Id2MetaPeriodVerifyIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.Id2MetaPeriodVerifyIntlResponse:
        """
        @summary 身份二要素有效期核验
        
        @param request: Id2MetaPeriodVerifyIntlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Id2MetaPeriodVerifyIntlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_name):
            body['DocName'] = request.doc_name
        if not UtilClient.is_unset(request.doc_no):
            body['DocNo'] = request.doc_no
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.merchant_biz_id):
            body['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            body['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.scene_code):
            body['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.validity_end_date):
            body['ValidityEndDate'] = request.validity_end_date
        if not UtilClient.is_unset(request.validity_start_date):
            body['ValidityStartDate'] = request.validity_start_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Id2MetaPeriodVerifyIntl',
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
            cloudauth_intl_20220809_models.Id2MetaPeriodVerifyIntlResponse(),
            self.call_api(params, req, runtime)
        )

    async def id_2meta_period_verify_intl_with_options_async(
        self,
        request: cloudauth_intl_20220809_models.Id2MetaPeriodVerifyIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.Id2MetaPeriodVerifyIntlResponse:
        """
        @summary 身份二要素有效期核验
        
        @param request: Id2MetaPeriodVerifyIntlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Id2MetaPeriodVerifyIntlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.doc_name):
            body['DocName'] = request.doc_name
        if not UtilClient.is_unset(request.doc_no):
            body['DocNo'] = request.doc_no
        if not UtilClient.is_unset(request.doc_type):
            body['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.merchant_biz_id):
            body['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            body['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.scene_code):
            body['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.validity_end_date):
            body['ValidityEndDate'] = request.validity_end_date
        if not UtilClient.is_unset(request.validity_start_date):
            body['ValidityStartDate'] = request.validity_start_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Id2MetaPeriodVerifyIntl',
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
            cloudauth_intl_20220809_models.Id2MetaPeriodVerifyIntlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def id_2meta_period_verify_intl(
        self,
        request: cloudauth_intl_20220809_models.Id2MetaPeriodVerifyIntlRequest,
    ) -> cloudauth_intl_20220809_models.Id2MetaPeriodVerifyIntlResponse:
        """
        @summary 身份二要素有效期核验
        
        @param request: Id2MetaPeriodVerifyIntlRequest
        @return: Id2MetaPeriodVerifyIntlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.id_2meta_period_verify_intl_with_options(request, runtime)

    async def id_2meta_period_verify_intl_async(
        self,
        request: cloudauth_intl_20220809_models.Id2MetaPeriodVerifyIntlRequest,
    ) -> cloudauth_intl_20220809_models.Id2MetaPeriodVerifyIntlResponse:
        """
        @summary 身份二要素有效期核验
        
        @param request: Id2MetaPeriodVerifyIntlRequest
        @return: Id2MetaPeriodVerifyIntlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.id_2meta_period_verify_intl_with_options_async(request, runtime)

    def id_2meta_verify_intl_with_options(
        self,
        request: cloudauth_intl_20220809_models.Id2MetaVerifyIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.Id2MetaVerifyIntlResponse:
        """
        @summary 身份二要素国际版接口
        
        @param request: Id2MetaVerifyIntlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Id2MetaVerifyIntlResponse
        """
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
        """
        @summary 身份二要素国际版接口
        
        @param request: Id2MetaVerifyIntlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Id2MetaVerifyIntlResponse
        """
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
        """
        @summary 身份二要素国际版接口
        
        @param request: Id2MetaVerifyIntlRequest
        @return: Id2MetaVerifyIntlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.id_2meta_verify_intl_with_options(request, runtime)

    async def id_2meta_verify_intl_async(
        self,
        request: cloudauth_intl_20220809_models.Id2MetaVerifyIntlRequest,
    ) -> cloudauth_intl_20220809_models.Id2MetaVerifyIntlResponse:
        """
        @summary 身份二要素国际版接口
        
        @param request: Id2MetaVerifyIntlRequest
        @return: Id2MetaVerifyIntlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.id_2meta_verify_intl_with_options_async(request, runtime)

    def initialize_with_options(
        self,
        tmp_req: cloudauth_intl_20220809_models.InitializeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.InitializeResponse:
        """
        @summary 认证初始化
        
        @param tmp_req: InitializeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitializeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudauth_intl_20220809_models.InitializeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_page_config):
            request.doc_page_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_page_config, 'DocPageConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_quality_check):
            query['AppQualityCheck'] = request.app_quality_check
        if not UtilClient.is_unset(request.authorize):
            query['Authorize'] = request.authorize
        if not UtilClient.is_unset(request.callback_token):
            query['CallbackToken'] = request.callback_token
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.crop):
            query['Crop'] = request.crop
        if not UtilClient.is_unset(request.date_of_birth):
            query['DateOfBirth'] = request.date_of_birth
        if not UtilClient.is_unset(request.date_of_expiry):
            query['DateOfExpiry'] = request.date_of_expiry
        if not UtilClient.is_unset(request.doc_page_config_shrink):
            query['DocPageConfig'] = request.doc_page_config_shrink
        if not UtilClient.is_unset(request.doc_scan_mode):
            query['DocScanMode'] = request.doc_scan_mode
        if not UtilClient.is_unset(request.doc_type):
            query['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.doc_video):
            query['DocVideo'] = request.doc_video
        if not UtilClient.is_unset(request.document_number):
            query['DocumentNumber'] = request.document_number
        if not UtilClient.is_unset(request.experience_code):
            query['ExperienceCode'] = request.experience_code
        if not UtilClient.is_unset(request.face_picture_url):
            query['FacePictureUrl'] = request.face_picture_url
        if not UtilClient.is_unset(request.id_face_quality):
            query['IdFaceQuality'] = request.id_face_quality
        if not UtilClient.is_unset(request.id_spoof):
            query['IdSpoof'] = request.id_spoof
        if not UtilClient.is_unset(request.id_threshold):
            query['IdThreshold'] = request.id_threshold
        if not UtilClient.is_unset(request.language_config):
            query['LanguageConfig'] = request.language_config
        if not UtilClient.is_unset(request.mrtdinput):
            query['MRTDInput'] = request.mrtdinput
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.meta_info):
            query['MetaInfo'] = request.meta_info
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.ocr):
            query['Ocr'] = request.ocr
        if not UtilClient.is_unset(request.procedure_priority):
            query['ProcedurePriority'] = request.procedure_priority
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_flow):
            query['ProductFlow'] = request.product_flow
        if not UtilClient.is_unset(request.return_url):
            query['ReturnUrl'] = request.return_url
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.security_level):
            query['SecurityLevel'] = request.security_level
        if not UtilClient.is_unset(request.show_album_icon):
            query['ShowAlbumIcon'] = request.show_album_icon
        if not UtilClient.is_unset(request.show_guide_page):
            query['ShowGuidePage'] = request.show_guide_page
        if not UtilClient.is_unset(request.show_ocr_result):
            query['ShowOcrResult'] = request.show_ocr_result
        if not UtilClient.is_unset(request.style_config):
            query['StyleConfig'] = request.style_config
        if not UtilClient.is_unset(request.use_nfc):
            query['UseNFC'] = request.use_nfc
        body = {}
        if not UtilClient.is_unset(request.face_picture_base_64):
            body['FacePictureBase64'] = request.face_picture_base_64
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        tmp_req: cloudauth_intl_20220809_models.InitializeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.InitializeResponse:
        """
        @summary 认证初始化
        
        @param tmp_req: InitializeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitializeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudauth_intl_20220809_models.InitializeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.doc_page_config):
            request.doc_page_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.doc_page_config, 'DocPageConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_quality_check):
            query['AppQualityCheck'] = request.app_quality_check
        if not UtilClient.is_unset(request.authorize):
            query['Authorize'] = request.authorize
        if not UtilClient.is_unset(request.callback_token):
            query['CallbackToken'] = request.callback_token
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.crop):
            query['Crop'] = request.crop
        if not UtilClient.is_unset(request.date_of_birth):
            query['DateOfBirth'] = request.date_of_birth
        if not UtilClient.is_unset(request.date_of_expiry):
            query['DateOfExpiry'] = request.date_of_expiry
        if not UtilClient.is_unset(request.doc_page_config_shrink):
            query['DocPageConfig'] = request.doc_page_config_shrink
        if not UtilClient.is_unset(request.doc_scan_mode):
            query['DocScanMode'] = request.doc_scan_mode
        if not UtilClient.is_unset(request.doc_type):
            query['DocType'] = request.doc_type
        if not UtilClient.is_unset(request.doc_video):
            query['DocVideo'] = request.doc_video
        if not UtilClient.is_unset(request.document_number):
            query['DocumentNumber'] = request.document_number
        if not UtilClient.is_unset(request.experience_code):
            query['ExperienceCode'] = request.experience_code
        if not UtilClient.is_unset(request.face_picture_url):
            query['FacePictureUrl'] = request.face_picture_url
        if not UtilClient.is_unset(request.id_face_quality):
            query['IdFaceQuality'] = request.id_face_quality
        if not UtilClient.is_unset(request.id_spoof):
            query['IdSpoof'] = request.id_spoof
        if not UtilClient.is_unset(request.id_threshold):
            query['IdThreshold'] = request.id_threshold
        if not UtilClient.is_unset(request.language_config):
            query['LanguageConfig'] = request.language_config
        if not UtilClient.is_unset(request.mrtdinput):
            query['MRTDInput'] = request.mrtdinput
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.merchant_user_id):
            query['MerchantUserId'] = request.merchant_user_id
        if not UtilClient.is_unset(request.meta_info):
            query['MetaInfo'] = request.meta_info
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.ocr):
            query['Ocr'] = request.ocr
        if not UtilClient.is_unset(request.procedure_priority):
            query['ProcedurePriority'] = request.procedure_priority
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_flow):
            query['ProductFlow'] = request.product_flow
        if not UtilClient.is_unset(request.return_url):
            query['ReturnUrl'] = request.return_url
        if not UtilClient.is_unset(request.scene_code):
            query['SceneCode'] = request.scene_code
        if not UtilClient.is_unset(request.security_level):
            query['SecurityLevel'] = request.security_level
        if not UtilClient.is_unset(request.show_album_icon):
            query['ShowAlbumIcon'] = request.show_album_icon
        if not UtilClient.is_unset(request.show_guide_page):
            query['ShowGuidePage'] = request.show_guide_page
        if not UtilClient.is_unset(request.show_ocr_result):
            query['ShowOcrResult'] = request.show_ocr_result
        if not UtilClient.is_unset(request.style_config):
            query['StyleConfig'] = request.style_config
        if not UtilClient.is_unset(request.use_nfc):
            query['UseNFC'] = request.use_nfc
        body = {}
        if not UtilClient.is_unset(request.face_picture_base_64):
            body['FacePictureBase64'] = request.face_picture_base_64
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        """
        @summary 认证初始化
        
        @param request: InitializeRequest
        @return: InitializeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.initialize_with_options(request, runtime)

    async def initialize_async(
        self,
        request: cloudauth_intl_20220809_models.InitializeRequest,
    ) -> cloudauth_intl_20220809_models.InitializeResponse:
        """
        @summary 认证初始化
        
        @param request: InitializeRequest
        @return: InitializeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.initialize_with_options_async(request, runtime)

    def mobile_3meta_verify_intl_with_options(
        self,
        request: cloudauth_intl_20220809_models.Mobile3MetaVerifyIntlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_intl_20220809_models.Mobile3MetaVerifyIntlResponse:
        """
        @summary 手机号三要素国际版接口
        
        @param request: Mobile3MetaVerifyIntlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Mobile3MetaVerifyIntlResponse
        """
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
        """
        @summary 手机号三要素国际版接口
        
        @param request: Mobile3MetaVerifyIntlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Mobile3MetaVerifyIntlResponse
        """
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
        """
        @summary 手机号三要素国际版接口
        
        @param request: Mobile3MetaVerifyIntlRequest
        @return: Mobile3MetaVerifyIntlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.mobile_3meta_verify_intl_with_options(request, runtime)

    async def mobile_3meta_verify_intl_async(
        self,
        request: cloudauth_intl_20220809_models.Mobile3MetaVerifyIntlRequest,
    ) -> cloudauth_intl_20220809_models.Mobile3MetaVerifyIntlResponse:
        """
        @summary 手机号三要素国际版接口
        
        @param request: Mobile3MetaVerifyIntlRequest
        @return: Mobile3MetaVerifyIntlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.mobile_3meta_verify_intl_with_options_async(request, runtime)
