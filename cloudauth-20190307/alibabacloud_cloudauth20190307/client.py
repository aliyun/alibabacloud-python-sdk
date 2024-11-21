# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudauth20190307 import models as cloudauth_20190307_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudauth', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def a_igcface_verify_with_options(
        self,
        request: cloudauth_20190307_models.AIGCFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.AIGCFaceVerifyResponse:
        """
        @summary 新增AIGC人脸检测能力
        
        @param request: AIGCFaceVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AIGCFaceVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_contrast_picture_url):
            query['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_object_name):
            query['OssObjectName'] = request.oss_object_name
        if not UtilClient.is_unset(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        body = {}
        if not UtilClient.is_unset(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AIGCFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.AIGCFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def a_igcface_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.AIGCFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.AIGCFaceVerifyResponse:
        """
        @summary 新增AIGC人脸检测能力
        
        @param request: AIGCFaceVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AIGCFaceVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_contrast_picture_url):
            query['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_object_name):
            query['OssObjectName'] = request.oss_object_name
        if not UtilClient.is_unset(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        body = {}
        if not UtilClient.is_unset(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AIGCFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.AIGCFaceVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def a_igcface_verify(
        self,
        request: cloudauth_20190307_models.AIGCFaceVerifyRequest,
    ) -> cloudauth_20190307_models.AIGCFaceVerifyResponse:
        """
        @summary 新增AIGC人脸检测能力
        
        @param request: AIGCFaceVerifyRequest
        @return: AIGCFaceVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.a_igcface_verify_with_options(request, runtime)

    async def a_igcface_verify_async(
        self,
        request: cloudauth_20190307_models.AIGCFaceVerifyRequest,
    ) -> cloudauth_20190307_models.AIGCFaceVerifyResponse:
        """
        @summary 新增AIGC人脸检测能力
        
        @param request: AIGCFaceVerifyRequest
        @return: AIGCFaceVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.a_igcface_verify_with_options_async(request, runtime)

    def bank_meta_verify_with_options(
        self,
        request: cloudauth_20190307_models.BankMetaVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.BankMetaVerifyResponse:
        """
        @summary 银行卡要素核验接口
        
        @param request: BankMetaVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BankMetaVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bank_card):
            query['BankCard'] = request.bank_card
        if not UtilClient.is_unset(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.verify_mode):
            query['VerifyMode'] = request.verify_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BankMetaVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.BankMetaVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def bank_meta_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.BankMetaVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.BankMetaVerifyResponse:
        """
        @summary 银行卡要素核验接口
        
        @param request: BankMetaVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BankMetaVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bank_card):
            query['BankCard'] = request.bank_card
        if not UtilClient.is_unset(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.identity_type):
            query['IdentityType'] = request.identity_type
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.verify_mode):
            query['VerifyMode'] = request.verify_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BankMetaVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.BankMetaVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bank_meta_verify(
        self,
        request: cloudauth_20190307_models.BankMetaVerifyRequest,
    ) -> cloudauth_20190307_models.BankMetaVerifyResponse:
        """
        @summary 银行卡要素核验接口
        
        @param request: BankMetaVerifyRequest
        @return: BankMetaVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bank_meta_verify_with_options(request, runtime)

    async def bank_meta_verify_async(
        self,
        request: cloudauth_20190307_models.BankMetaVerifyRequest,
    ) -> cloudauth_20190307_models.BankMetaVerifyResponse:
        """
        @summary 银行卡要素核验接口
        
        @param request: BankMetaVerifyRequest
        @return: BankMetaVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bank_meta_verify_with_options_async(request, runtime)

    def compare_face_verify_with_options(
        self,
        request: cloudauth_20190307_models.CompareFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CompareFaceVerifyResponse:
        """
        @param request: CompareFaceVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompareFaceVerifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.source_certify_id):
            body['SourceCertifyId'] = request.source_certify_id
        if not UtilClient.is_unset(request.source_face_contrast_picture):
            body['SourceFaceContrastPicture'] = request.source_face_contrast_picture
        if not UtilClient.is_unset(request.source_face_contrast_picture_url):
            body['SourceFaceContrastPictureUrl'] = request.source_face_contrast_picture_url
        if not UtilClient.is_unset(request.source_oss_bucket_name):
            body['SourceOssBucketName'] = request.source_oss_bucket_name
        if not UtilClient.is_unset(request.source_oss_object_name):
            body['SourceOssObjectName'] = request.source_oss_object_name
        if not UtilClient.is_unset(request.target_certify_id):
            body['TargetCertifyId'] = request.target_certify_id
        if not UtilClient.is_unset(request.target_face_contrast_picture):
            body['TargetFaceContrastPicture'] = request.target_face_contrast_picture
        if not UtilClient.is_unset(request.target_face_contrast_picture_url):
            body['TargetFaceContrastPictureUrl'] = request.target_face_contrast_picture_url
        if not UtilClient.is_unset(request.target_oss_bucket_name):
            body['TargetOssBucketName'] = request.target_oss_bucket_name
        if not UtilClient.is_unset(request.target_oss_object_name):
            body['TargetOssObjectName'] = request.target_oss_object_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompareFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_face_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.CompareFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CompareFaceVerifyResponse:
        """
        @param request: CompareFaceVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompareFaceVerifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.source_certify_id):
            body['SourceCertifyId'] = request.source_certify_id
        if not UtilClient.is_unset(request.source_face_contrast_picture):
            body['SourceFaceContrastPicture'] = request.source_face_contrast_picture
        if not UtilClient.is_unset(request.source_face_contrast_picture_url):
            body['SourceFaceContrastPictureUrl'] = request.source_face_contrast_picture_url
        if not UtilClient.is_unset(request.source_oss_bucket_name):
            body['SourceOssBucketName'] = request.source_oss_bucket_name
        if not UtilClient.is_unset(request.source_oss_object_name):
            body['SourceOssObjectName'] = request.source_oss_object_name
        if not UtilClient.is_unset(request.target_certify_id):
            body['TargetCertifyId'] = request.target_certify_id
        if not UtilClient.is_unset(request.target_face_contrast_picture):
            body['TargetFaceContrastPicture'] = request.target_face_contrast_picture
        if not UtilClient.is_unset(request.target_face_contrast_picture_url):
            body['TargetFaceContrastPictureUrl'] = request.target_face_contrast_picture_url
        if not UtilClient.is_unset(request.target_oss_bucket_name):
            body['TargetOssBucketName'] = request.target_oss_bucket_name
        if not UtilClient.is_unset(request.target_oss_object_name):
            body['TargetOssObjectName'] = request.target_oss_object_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompareFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFaceVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_face_verify(
        self,
        request: cloudauth_20190307_models.CompareFaceVerifyRequest,
    ) -> cloudauth_20190307_models.CompareFaceVerifyResponse:
        """
        @param request: CompareFaceVerifyRequest
        @return: CompareFaceVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.compare_face_verify_with_options(request, runtime)

    async def compare_face_verify_async(
        self,
        request: cloudauth_20190307_models.CompareFaceVerifyRequest,
    ) -> cloudauth_20190307_models.CompareFaceVerifyResponse:
        """
        @param request: CompareFaceVerifyRequest
        @return: CompareFaceVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.compare_face_verify_with_options_async(request, runtime)

    def compare_faces_with_options(
        self,
        request: cloudauth_20190307_models.CompareFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CompareFacesResponse:
        """
        @param request: CompareFacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompareFacesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.source_image_type):
            body['SourceImageType'] = request.source_image_type
        if not UtilClient.is_unset(request.source_image_value):
            body['SourceImageValue'] = request.source_image_value
        if not UtilClient.is_unset(request.target_image_type):
            body['TargetImageType'] = request.target_image_type
        if not UtilClient.is_unset(request.target_image_value):
            body['TargetImageValue'] = request.target_image_value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompareFaces',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_faces_with_options_async(
        self,
        request: cloudauth_20190307_models.CompareFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CompareFacesResponse:
        """
        @param request: CompareFacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompareFacesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.source_image_type):
            body['SourceImageType'] = request.source_image_type
        if not UtilClient.is_unset(request.source_image_value):
            body['SourceImageValue'] = request.source_image_value
        if not UtilClient.is_unset(request.target_image_type):
            body['TargetImageType'] = request.target_image_type
        if not UtilClient.is_unset(request.target_image_value):
            body['TargetImageValue'] = request.target_image_value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompareFaces',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CompareFacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_faces(
        self,
        request: cloudauth_20190307_models.CompareFacesRequest,
    ) -> cloudauth_20190307_models.CompareFacesResponse:
        """
        @param request: CompareFacesRequest
        @return: CompareFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.compare_faces_with_options(request, runtime)

    async def compare_faces_async(
        self,
        request: cloudauth_20190307_models.CompareFacesRequest,
    ) -> cloudauth_20190307_models.CompareFacesResponse:
        """
        @param request: CompareFacesRequest
        @return: CompareFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.compare_faces_with_options_async(request, runtime)

    def contrast_face_verify_with_options(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
        """
        @param request: ContrastFaceVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContrastFaceVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        body = {}
        if not UtilClient.is_unset(request.cert_name):
            body['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_no):
            body['CertNo'] = request.cert_no
        if not UtilClient.is_unset(request.cert_type):
            body['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.certify_id):
            body['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.device_token):
            body['DeviceToken'] = request.device_token
        if not UtilClient.is_unset(request.encrypt_type):
            body['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.face_contrast_file):
            body['FaceContrastFile'] = request.face_contrast_file
        if not UtilClient.is_unset(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        if not UtilClient.is_unset(request.face_contrast_picture_url):
            body['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.oss_bucket_name):
            body['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_object_name):
            body['OssObjectName'] = request.oss_object_name
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ContrastFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.ContrastFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def contrast_face_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
        """
        @param request: ContrastFaceVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContrastFaceVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        body = {}
        if not UtilClient.is_unset(request.cert_name):
            body['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_no):
            body['CertNo'] = request.cert_no
        if not UtilClient.is_unset(request.cert_type):
            body['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.certify_id):
            body['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.device_token):
            body['DeviceToken'] = request.device_token
        if not UtilClient.is_unset(request.encrypt_type):
            body['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.face_contrast_file):
            body['FaceContrastFile'] = request.face_contrast_file
        if not UtilClient.is_unset(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        if not UtilClient.is_unset(request.face_contrast_picture_url):
            body['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.oss_bucket_name):
            body['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_object_name):
            body['OssObjectName'] = request.oss_object_name
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ContrastFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.ContrastFaceVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def contrast_face_verify(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyRequest,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
        """
        @param request: ContrastFaceVerifyRequest
        @return: ContrastFaceVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.contrast_face_verify_with_options(request, runtime)

    async def contrast_face_verify_async(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyRequest,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
        """
        @param request: ContrastFaceVerifyRequest
        @return: ContrastFaceVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.contrast_face_verify_with_options_async(request, runtime)

    def contrast_face_verify_advance(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
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
            product='Cloudauth',
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
        contrast_face_verify_req = cloudauth_20190307_models.ContrastFaceVerifyRequest()
        OpenApiUtilClient.convert(request, contrast_face_verify_req)
        if not UtilClient.is_unset(request.face_contrast_file_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.face_contrast_file_object,
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
            contrast_face_verify_req.face_contrast_file = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        contrast_face_verify_resp = self.contrast_face_verify_with_options(contrast_face_verify_req, runtime)
        return contrast_face_verify_resp

    async def contrast_face_verify_advance_async(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
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
            product='Cloudauth',
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
        contrast_face_verify_req = cloudauth_20190307_models.ContrastFaceVerifyRequest()
        OpenApiUtilClient.convert(request, contrast_face_verify_req)
        if not UtilClient.is_unset(request.face_contrast_file_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.face_contrast_file_object,
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
            contrast_face_verify_req.face_contrast_file = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        contrast_face_verify_resp = await self.contrast_face_verify_with_options_async(contrast_face_verify_req, runtime)
        return contrast_face_verify_resp

    def create_auth_key_with_options(
        self,
        request: cloudauth_20190307_models.CreateAuthKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateAuthKeyResponse:
        """
        @param request: CreateAuthKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAuthKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_years):
            query['AuthYears'] = request.auth_years
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.test):
            query['Test'] = request.test
        if not UtilClient.is_unset(request.user_device_id):
            query['UserDeviceId'] = request.user_device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAuthKey',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateAuthKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_auth_key_with_options_async(
        self,
        request: cloudauth_20190307_models.CreateAuthKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateAuthKeyResponse:
        """
        @param request: CreateAuthKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAuthKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_years):
            query['AuthYears'] = request.auth_years
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.test):
            query['Test'] = request.test
        if not UtilClient.is_unset(request.user_device_id):
            query['UserDeviceId'] = request.user_device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAuthKey',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateAuthKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_auth_key(
        self,
        request: cloudauth_20190307_models.CreateAuthKeyRequest,
    ) -> cloudauth_20190307_models.CreateAuthKeyResponse:
        """
        @param request: CreateAuthKeyRequest
        @return: CreateAuthKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_auth_key_with_options(request, runtime)

    async def create_auth_key_async(
        self,
        request: cloudauth_20190307_models.CreateAuthKeyRequest,
    ) -> cloudauth_20190307_models.CreateAuthKeyResponse:
        """
        @param request: CreateAuthKeyRequest
        @return: CreateAuthKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_auth_key_with_options_async(request, runtime)

    def create_verify_setting_with_options(
        self,
        request: cloudauth_20190307_models.CreateVerifySettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateVerifySettingResponse:
        """
        @param request: CreateVerifySettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVerifySettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_name):
            query['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.guide_step):
            query['GuideStep'] = request.guide_step
        if not UtilClient.is_unset(request.privacy_step):
            query['PrivacyStep'] = request.privacy_step
        if not UtilClient.is_unset(request.result_step):
            query['ResultStep'] = request.result_step
        if not UtilClient.is_unset(request.solution):
            query['Solution'] = request.solution
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVerifySetting',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateVerifySettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_verify_setting_with_options_async(
        self,
        request: cloudauth_20190307_models.CreateVerifySettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateVerifySettingResponse:
        """
        @param request: CreateVerifySettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVerifySettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_name):
            query['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.guide_step):
            query['GuideStep'] = request.guide_step
        if not UtilClient.is_unset(request.privacy_step):
            query['PrivacyStep'] = request.privacy_step
        if not UtilClient.is_unset(request.result_step):
            query['ResultStep'] = request.result_step
        if not UtilClient.is_unset(request.solution):
            query['Solution'] = request.solution
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVerifySetting',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CreateVerifySettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_verify_setting(
        self,
        request: cloudauth_20190307_models.CreateVerifySettingRequest,
    ) -> cloudauth_20190307_models.CreateVerifySettingResponse:
        """
        @param request: CreateVerifySettingRequest
        @return: CreateVerifySettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_verify_setting_with_options(request, runtime)

    async def create_verify_setting_async(
        self,
        request: cloudauth_20190307_models.CreateVerifySettingRequest,
    ) -> cloudauth_20190307_models.CreateVerifySettingResponse:
        """
        @param request: CreateVerifySettingRequest
        @return: CreateVerifySettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_verify_setting_with_options_async(request, runtime)

    def credential_verify_with_options(
        self,
        tmp_req: cloudauth_20190307_models.CredentialVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CredentialVerifyResponse:
        """
        @summary 凭证核验
        
        @param tmp_req: CredentialVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CredentialVerifyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudauth_20190307_models.CredentialVerifyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.merchant_detail):
            request.merchant_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.merchant_detail, 'MerchantDetail', 'json')
        query = {}
        if not UtilClient.is_unset(request.cert_num):
            query['CertNum'] = request.cert_num
        if not UtilClient.is_unset(request.cred_name):
            query['CredName'] = request.cred_name
        if not UtilClient.is_unset(request.cred_type):
            query['CredType'] = request.cred_type
        if not UtilClient.is_unset(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.is_check):
            query['IsCheck'] = request.is_check
        if not UtilClient.is_unset(request.is_ocr):
            query['IsOCR'] = request.is_ocr
        if not UtilClient.is_unset(request.merchant_detail_shrink):
            query['MerchantDetail'] = request.merchant_detail_shrink
        if not UtilClient.is_unset(request.merchant_id):
            query['MerchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.prompt_model):
            query['PromptModel'] = request.prompt_model
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        body = {}
        if not UtilClient.is_unset(request.image_context):
            body['ImageContext'] = request.image_context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CredentialVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CredentialVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def credential_verify_with_options_async(
        self,
        tmp_req: cloudauth_20190307_models.CredentialVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CredentialVerifyResponse:
        """
        @summary 凭证核验
        
        @param tmp_req: CredentialVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CredentialVerifyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudauth_20190307_models.CredentialVerifyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.merchant_detail):
            request.merchant_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.merchant_detail, 'MerchantDetail', 'json')
        query = {}
        if not UtilClient.is_unset(request.cert_num):
            query['CertNum'] = request.cert_num
        if not UtilClient.is_unset(request.cred_name):
            query['CredName'] = request.cred_name
        if not UtilClient.is_unset(request.cred_type):
            query['CredType'] = request.cred_type
        if not UtilClient.is_unset(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.is_check):
            query['IsCheck'] = request.is_check
        if not UtilClient.is_unset(request.is_ocr):
            query['IsOCR'] = request.is_ocr
        if not UtilClient.is_unset(request.merchant_detail_shrink):
            query['MerchantDetail'] = request.merchant_detail_shrink
        if not UtilClient.is_unset(request.merchant_id):
            query['MerchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.prompt_model):
            query['PromptModel'] = request.prompt_model
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        body = {}
        if not UtilClient.is_unset(request.image_context):
            body['ImageContext'] = request.image_context
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CredentialVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.CredentialVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def credential_verify(
        self,
        request: cloudauth_20190307_models.CredentialVerifyRequest,
    ) -> cloudauth_20190307_models.CredentialVerifyResponse:
        """
        @summary 凭证核验
        
        @param request: CredentialVerifyRequest
        @return: CredentialVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.credential_verify_with_options(request, runtime)

    async def credential_verify_async(
        self,
        request: cloudauth_20190307_models.CredentialVerifyRequest,
    ) -> cloudauth_20190307_models.CredentialVerifyResponse:
        """
        @summary 凭证核验
        
        @param request: CredentialVerifyRequest
        @return: CredentialVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.credential_verify_with_options_async(request, runtime)

    def deepfake_detect_with_options(
        self,
        request: cloudauth_20190307_models.DeepfakeDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DeepfakeDetectResponse:
        """
        @summary 人脸凭证核验服务
        
        @param request: DeepfakeDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeepfakeDetectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_input_type):
            query['FaceInputType'] = request.face_input_type
        if not UtilClient.is_unset(request.face_url):
            query['FaceUrl'] = request.face_url
        if not UtilClient.is_unset(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        body = {}
        if not UtilClient.is_unset(request.face_base_64):
            body['FaceBase64'] = request.face_base_64
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeepfakeDetect',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DeepfakeDetectResponse(),
            self.call_api(params, req, runtime)
        )

    async def deepfake_detect_with_options_async(
        self,
        request: cloudauth_20190307_models.DeepfakeDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DeepfakeDetectResponse:
        """
        @summary 人脸凭证核验服务
        
        @param request: DeepfakeDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeepfakeDetectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_input_type):
            query['FaceInputType'] = request.face_input_type
        if not UtilClient.is_unset(request.face_url):
            query['FaceUrl'] = request.face_url
        if not UtilClient.is_unset(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        body = {}
        if not UtilClient.is_unset(request.face_base_64):
            body['FaceBase64'] = request.face_base_64
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeepfakeDetect',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DeepfakeDetectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deepfake_detect(
        self,
        request: cloudauth_20190307_models.DeepfakeDetectRequest,
    ) -> cloudauth_20190307_models.DeepfakeDetectResponse:
        """
        @summary 人脸凭证核验服务
        
        @param request: DeepfakeDetectRequest
        @return: DeepfakeDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deepfake_detect_with_options(request, runtime)

    async def deepfake_detect_async(
        self,
        request: cloudauth_20190307_models.DeepfakeDetectRequest,
    ) -> cloudauth_20190307_models.DeepfakeDetectResponse:
        """
        @summary 人脸凭证核验服务
        
        @param request: DeepfakeDetectRequest
        @return: DeepfakeDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deepfake_detect_with_options_async(request, runtime)

    def delete_face_verify_result_with_options(
        self,
        request: cloudauth_20190307_models.DeleteFaceVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DeleteFaceVerifyResultResponse:
        """
        @summary 金融级服务敏感数据删除接口
        
        @param request: DeleteFaceVerifyResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFaceVerifyResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.delete_after_query):
            query['DeleteAfterQuery'] = request.delete_after_query
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaceVerifyResult',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DeleteFaceVerifyResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_verify_result_with_options_async(
        self,
        request: cloudauth_20190307_models.DeleteFaceVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DeleteFaceVerifyResultResponse:
        """
        @summary 金融级服务敏感数据删除接口
        
        @param request: DeleteFaceVerifyResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFaceVerifyResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.delete_after_query):
            query['DeleteAfterQuery'] = request.delete_after_query
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaceVerifyResult',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DeleteFaceVerifyResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face_verify_result(
        self,
        request: cloudauth_20190307_models.DeleteFaceVerifyResultRequest,
    ) -> cloudauth_20190307_models.DeleteFaceVerifyResultResponse:
        """
        @summary 金融级服务敏感数据删除接口
        
        @param request: DeleteFaceVerifyResultRequest
        @return: DeleteFaceVerifyResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_face_verify_result_with_options(request, runtime)

    async def delete_face_verify_result_async(
        self,
        request: cloudauth_20190307_models.DeleteFaceVerifyResultRequest,
    ) -> cloudauth_20190307_models.DeleteFaceVerifyResultResponse:
        """
        @summary 金融级服务敏感数据删除接口
        
        @param request: DeleteFaceVerifyResultRequest
        @return: DeleteFaceVerifyResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_verify_result_with_options_async(request, runtime)

    def describe_device_info_with_options(
        self,
        request: cloudauth_20190307_models.DescribeDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeDeviceInfoResponse:
        """
        @param request: DescribeDeviceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeviceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.expired_end_day):
            query['ExpiredEndDay'] = request.expired_end_day
        if not UtilClient.is_unset(request.expired_start_day):
            query['ExpiredStartDay'] = request.expired_start_day
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_device_id):
            query['UserDeviceId'] = request.user_device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeviceInfo',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_device_info_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeDeviceInfoResponse:
        """
        @param request: DescribeDeviceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeviceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.expired_end_day):
            query['ExpiredEndDay'] = request.expired_end_day
        if not UtilClient.is_unset(request.expired_start_day):
            query['ExpiredStartDay'] = request.expired_start_day
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_device_id):
            query['UserDeviceId'] = request.user_device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeviceInfo',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_device_info(
        self,
        request: cloudauth_20190307_models.DescribeDeviceInfoRequest,
    ) -> cloudauth_20190307_models.DescribeDeviceInfoResponse:
        """
        @param request: DescribeDeviceInfoRequest
        @return: DescribeDeviceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_device_info_with_options(request, runtime)

    async def describe_device_info_async(
        self,
        request: cloudauth_20190307_models.DescribeDeviceInfoRequest,
    ) -> cloudauth_20190307_models.DescribeDeviceInfoResponse:
        """
        @param request: DescribeDeviceInfoRequest
        @return: DescribeDeviceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_device_info_with_options_async(request, runtime)

    def describe_face_guard_risk_with_options(
        self,
        request: cloudauth_20190307_models.DescribeFaceGuardRiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceGuardRiskResponse:
        """
        @summary 金融级人脸保镖服务
        
        @param request: DescribeFaceGuardRiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFaceGuardRiskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.device_token):
            query['DeviceToken'] = request.device_token
        if not UtilClient.is_unset(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaceGuardRisk',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceGuardRiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_face_guard_risk_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceGuardRiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceGuardRiskResponse:
        """
        @summary 金融级人脸保镖服务
        
        @param request: DescribeFaceGuardRiskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFaceGuardRiskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.device_token):
            query['DeviceToken'] = request.device_token
        if not UtilClient.is_unset(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaceGuardRisk',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceGuardRiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_face_guard_risk(
        self,
        request: cloudauth_20190307_models.DescribeFaceGuardRiskRequest,
    ) -> cloudauth_20190307_models.DescribeFaceGuardRiskResponse:
        """
        @summary 金融级人脸保镖服务
        
        @param request: DescribeFaceGuardRiskRequest
        @return: DescribeFaceGuardRiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_face_guard_risk_with_options(request, runtime)

    async def describe_face_guard_risk_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceGuardRiskRequest,
    ) -> cloudauth_20190307_models.DescribeFaceGuardRiskResponse:
        """
        @summary 金融级人脸保镖服务
        
        @param request: DescribeFaceGuardRiskRequest
        @return: DescribeFaceGuardRiskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_face_guard_risk_with_options_async(request, runtime)

    def describe_face_verify_with_options(
        self,
        request: cloudauth_20190307_models.DescribeFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceVerifyResponse:
        """
        @param request: DescribeFaceVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFaceVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.picture_return_type):
            query['PictureReturnType'] = request.picture_return_type
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_face_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeFaceVerifyResponse:
        """
        @param request: DescribeFaceVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFaceVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.picture_return_type):
            query['PictureReturnType'] = request.picture_return_type
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeFaceVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_face_verify(
        self,
        request: cloudauth_20190307_models.DescribeFaceVerifyRequest,
    ) -> cloudauth_20190307_models.DescribeFaceVerifyResponse:
        """
        @param request: DescribeFaceVerifyRequest
        @return: DescribeFaceVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_face_verify_with_options(request, runtime)

    async def describe_face_verify_async(
        self,
        request: cloudauth_20190307_models.DescribeFaceVerifyRequest,
    ) -> cloudauth_20190307_models.DescribeFaceVerifyResponse:
        """
        @param request: DescribeFaceVerifyRequest
        @return: DescribeFaceVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_face_verify_with_options_async(request, runtime)

    def describe_oss_upload_token_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeOssUploadTokenResponse:
        """
        @param request: DescribeOssUploadTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOssUploadTokenResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeOssUploadToken',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeOssUploadTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_upload_token_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeOssUploadTokenResponse:
        """
        @param request: DescribeOssUploadTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOssUploadTokenResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeOssUploadToken',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeOssUploadTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_upload_token(self) -> cloudauth_20190307_models.DescribeOssUploadTokenResponse:
        """
        @return: DescribeOssUploadTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_upload_token_with_options(runtime)

    async def describe_oss_upload_token_async(self) -> cloudauth_20190307_models.DescribeOssUploadTokenResponse:
        """
        @return: DescribeOssUploadTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_upload_token_with_options_async(runtime)

    def describe_page_face_verify_data_with_options(
        self,
        request: cloudauth_20190307_models.DescribePageFaceVerifyDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribePageFaceVerifyDataResponse:
        """
        @summary Open API新增金融级数据统计API
        
        @param request: DescribePageFaceVerifyDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePageFaceVerifyDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePageFaceVerifyData',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribePageFaceVerifyDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_page_face_verify_data_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribePageFaceVerifyDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribePageFaceVerifyDataResponse:
        """
        @summary Open API新增金融级数据统计API
        
        @param request: DescribePageFaceVerifyDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePageFaceVerifyDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePageFaceVerifyData',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribePageFaceVerifyDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_page_face_verify_data(
        self,
        request: cloudauth_20190307_models.DescribePageFaceVerifyDataRequest,
    ) -> cloudauth_20190307_models.DescribePageFaceVerifyDataResponse:
        """
        @summary Open API新增金融级数据统计API
        
        @param request: DescribePageFaceVerifyDataRequest
        @return: DescribePageFaceVerifyDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_page_face_verify_data_with_options(request, runtime)

    async def describe_page_face_verify_data_async(
        self,
        request: cloudauth_20190307_models.DescribePageFaceVerifyDataRequest,
    ) -> cloudauth_20190307_models.DescribePageFaceVerifyDataResponse:
        """
        @summary Open API新增金融级数据统计API
        
        @param request: DescribePageFaceVerifyDataRequest
        @return: DescribePageFaceVerifyDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_page_face_verify_data_with_options_async(request, runtime)

    def describe_smart_statistics_page_list_with_options(
        self,
        request: cloudauth_20190307_models.DescribeSmartStatisticsPageListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeSmartStatisticsPageListResponse:
        """
        @param request: DescribeSmartStatisticsPageListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSmartStatisticsPageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSmartStatisticsPageList',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeSmartStatisticsPageListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_statistics_page_list_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeSmartStatisticsPageListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeSmartStatisticsPageListResponse:
        """
        @param request: DescribeSmartStatisticsPageListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSmartStatisticsPageListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSmartStatisticsPageList',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeSmartStatisticsPageListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_smart_statistics_page_list(
        self,
        request: cloudauth_20190307_models.DescribeSmartStatisticsPageListRequest,
    ) -> cloudauth_20190307_models.DescribeSmartStatisticsPageListResponse:
        """
        @param request: DescribeSmartStatisticsPageListRequest
        @return: DescribeSmartStatisticsPageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_smart_statistics_page_list_with_options(request, runtime)

    async def describe_smart_statistics_page_list_async(
        self,
        request: cloudauth_20190307_models.DescribeSmartStatisticsPageListRequest,
    ) -> cloudauth_20190307_models.DescribeSmartStatisticsPageListResponse:
        """
        @param request: DescribeSmartStatisticsPageListRequest
        @return: DescribeSmartStatisticsPageListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_smart_statistics_page_list_with_options_async(request, runtime)

    def describe_verify_result_with_options(
        self,
        request: cloudauth_20190307_models.DescribeVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyResultResponse:
        """
        @param request: DescribeVerifyResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVerifyResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVerifyResult',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_result_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyResultResponse:
        """
        @param request: DescribeVerifyResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVerifyResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVerifyResult',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_result(
        self,
        request: cloudauth_20190307_models.DescribeVerifyResultRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyResultResponse:
        """
        @param request: DescribeVerifyResultRequest
        @return: DescribeVerifyResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_result_with_options(request, runtime)

    async def describe_verify_result_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyResultRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyResultResponse:
        """
        @param request: DescribeVerifyResultRequest
        @return: DescribeVerifyResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_result_with_options_async(request, runtime)

    def describe_verify_sdkwith_options(
        self,
        request: cloudauth_20190307_models.DescribeVerifySDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifySDKResponse:
        """
        @param request: DescribeVerifySDKRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVerifySDKResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVerifySDK',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifySDKResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_sdkwith_options_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifySDKRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifySDKResponse:
        """
        @param request: DescribeVerifySDKRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVerifySDKResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVerifySDK',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifySDKResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_sdk(
        self,
        request: cloudauth_20190307_models.DescribeVerifySDKRequest,
    ) -> cloudauth_20190307_models.DescribeVerifySDKResponse:
        """
        @param request: DescribeVerifySDKRequest
        @return: DescribeVerifySDKResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_sdkwith_options(request, runtime)

    async def describe_verify_sdk_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifySDKRequest,
    ) -> cloudauth_20190307_models.DescribeVerifySDKResponse:
        """
        @param request: DescribeVerifySDKRequest
        @return: DescribeVerifySDKResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_sdkwith_options_async(request, runtime)

    def describe_verify_token_with_options(
        self,
        request: cloudauth_20190307_models.DescribeVerifyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyTokenResponse:
        """
        @param request: DescribeVerifyTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVerifyTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.callback_seed):
            query['CallbackSeed'] = request.callback_seed
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.face_retained_image_url):
            query['FaceRetainedImageUrl'] = request.face_retained_image_url
        if not UtilClient.is_unset(request.failed_redirect_url):
            query['FailedRedirectUrl'] = request.failed_redirect_url
        if not UtilClient.is_unset(request.id_card_back_image_url):
            query['IdCardBackImageUrl'] = request.id_card_back_image_url
        if not UtilClient.is_unset(request.id_card_front_image_url):
            query['IdCardFrontImageUrl'] = request.id_card_front_image_url
        if not UtilClient.is_unset(request.id_card_number):
            query['IdCardNumber'] = request.id_card_number
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.passed_redirect_url):
            query['PassedRedirectUrl'] = request.passed_redirect_url
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_ip):
            query['UserIp'] = request.user_ip
        if not UtilClient.is_unset(request.user_phone_number):
            query['UserPhoneNumber'] = request.user_phone_number
        if not UtilClient.is_unset(request.user_regist_time):
            query['UserRegistTime'] = request.user_regist_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVerifyToken',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_verify_token_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeVerifyTokenResponse:
        """
        @param request: DescribeVerifyTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVerifyTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.callback_seed):
            query['CallbackSeed'] = request.callback_seed
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.face_retained_image_url):
            query['FaceRetainedImageUrl'] = request.face_retained_image_url
        if not UtilClient.is_unset(request.failed_redirect_url):
            query['FailedRedirectUrl'] = request.failed_redirect_url
        if not UtilClient.is_unset(request.id_card_back_image_url):
            query['IdCardBackImageUrl'] = request.id_card_back_image_url
        if not UtilClient.is_unset(request.id_card_front_image_url):
            query['IdCardFrontImageUrl'] = request.id_card_front_image_url
        if not UtilClient.is_unset(request.id_card_number):
            query['IdCardNumber'] = request.id_card_number
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.passed_redirect_url):
            query['PassedRedirectUrl'] = request.passed_redirect_url
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_ip):
            query['UserIp'] = request.user_ip
        if not UtilClient.is_unset(request.user_phone_number):
            query['UserPhoneNumber'] = request.user_phone_number
        if not UtilClient.is_unset(request.user_regist_time):
            query['UserRegistTime'] = request.user_regist_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVerifyToken',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DescribeVerifyTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_verify_token(
        self,
        request: cloudauth_20190307_models.DescribeVerifyTokenRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyTokenResponse:
        """
        @param request: DescribeVerifyTokenRequest
        @return: DescribeVerifyTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_verify_token_with_options(request, runtime)

    async def describe_verify_token_async(
        self,
        request: cloudauth_20190307_models.DescribeVerifyTokenRequest,
    ) -> cloudauth_20190307_models.DescribeVerifyTokenResponse:
        """
        @param request: DescribeVerifyTokenRequest
        @return: DescribeVerifyTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_verify_token_with_options_async(request, runtime)

    def detect_face_attributes_with_options(
        self,
        request: cloudauth_20190307_models.DetectFaceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DetectFaceAttributesResponse:
        """
        @param request: DetectFaceAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectFaceAttributesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.material_value):
            body['MaterialValue'] = request.material_value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectFaceAttributes',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DetectFaceAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_face_attributes_with_options_async(
        self,
        request: cloudauth_20190307_models.DetectFaceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DetectFaceAttributesResponse:
        """
        @param request: DetectFaceAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectFaceAttributesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.material_value):
            body['MaterialValue'] = request.material_value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectFaceAttributes',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.DetectFaceAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_face_attributes(
        self,
        request: cloudauth_20190307_models.DetectFaceAttributesRequest,
    ) -> cloudauth_20190307_models.DetectFaceAttributesResponse:
        """
        @param request: DetectFaceAttributesRequest
        @return: DetectFaceAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_face_attributes_with_options(request, runtime)

    async def detect_face_attributes_async(
        self,
        request: cloudauth_20190307_models.DetectFaceAttributesRequest,
    ) -> cloudauth_20190307_models.DetectFaceAttributesResponse:
        """
        @param request: DetectFaceAttributesRequest
        @return: DetectFaceAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_face_attributes_with_options_async(request, runtime)

    def id_2meta_standard_verify_with_options(
        self,
        request: cloudauth_20190307_models.Id2MetaStandardVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Id2MetaStandardVerifyResponse:
        """
        @summary 身份二要素标准版
        
        @param request: Id2MetaStandardVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Id2MetaStandardVerifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Id2MetaStandardVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.Id2MetaStandardVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def id_2meta_standard_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.Id2MetaStandardVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Id2MetaStandardVerifyResponse:
        """
        @summary 身份二要素标准版
        
        @param request: Id2MetaStandardVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Id2MetaStandardVerifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Id2MetaStandardVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.Id2MetaStandardVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def id_2meta_standard_verify(
        self,
        request: cloudauth_20190307_models.Id2MetaStandardVerifyRequest,
    ) -> cloudauth_20190307_models.Id2MetaStandardVerifyResponse:
        """
        @summary 身份二要素标准版
        
        @param request: Id2MetaStandardVerifyRequest
        @return: Id2MetaStandardVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.id_2meta_standard_verify_with_options(request, runtime)

    async def id_2meta_standard_verify_async(
        self,
        request: cloudauth_20190307_models.Id2MetaStandardVerifyRequest,
    ) -> cloudauth_20190307_models.Id2MetaStandardVerifyResponse:
        """
        @summary 身份二要素标准版
        
        @param request: Id2MetaStandardVerifyRequest
        @return: Id2MetaStandardVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.id_2meta_standard_verify_with_options_async(request, runtime)

    def id_2meta_verify_with_options(
        self,
        request: cloudauth_20190307_models.Id2MetaVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Id2MetaVerifyResponse:
        """
        @summary 身份二要素接口
        
        @param request: Id2MetaVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Id2MetaVerifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Id2MetaVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.Id2MetaVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def id_2meta_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.Id2MetaVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Id2MetaVerifyResponse:
        """
        @summary 身份二要素接口
        
        @param request: Id2MetaVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Id2MetaVerifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Id2MetaVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.Id2MetaVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def id_2meta_verify(
        self,
        request: cloudauth_20190307_models.Id2MetaVerifyRequest,
    ) -> cloudauth_20190307_models.Id2MetaVerifyResponse:
        """
        @summary 身份二要素接口
        
        @param request: Id2MetaVerifyRequest
        @return: Id2MetaVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.id_2meta_verify_with_options(request, runtime)

    async def id_2meta_verify_async(
        self,
        request: cloudauth_20190307_models.Id2MetaVerifyRequest,
    ) -> cloudauth_20190307_models.Id2MetaVerifyResponse:
        """
        @summary 身份二要素接口
        
        @param request: Id2MetaVerifyRequest
        @return: Id2MetaVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.id_2meta_verify_with_options_async(request, runtime)

    def init_face_verify_with_options(
        self,
        request: cloudauth_20190307_models.InitFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.InitFaceVerifyResponse:
        """
        @param request: InitFaceVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitFaceVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_quality_check):
            query['AppQualityCheck'] = request.app_quality_check
        if not UtilClient.is_unset(request.birthday):
            query['Birthday'] = request.birthday
        if not UtilClient.is_unset(request.callback_token):
            query['CallbackToken'] = request.callback_token
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_no):
            query['CertNo'] = request.cert_no
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.certify_url_style):
            query['CertifyUrlStyle'] = request.certify_url_style
        if not UtilClient.is_unset(request.certify_url_type):
            query['CertifyUrlType'] = request.certify_url_type
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.face_contrast_picture_url):
            query['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not UtilClient.is_unset(request.face_guard_output):
            query['FaceGuardOutput'] = request.face_guard_output
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.meta_info):
            query['MetaInfo'] = request.meta_info
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_object_name):
            query['OssObjectName'] = request.oss_object_name
        if not UtilClient.is_unset(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.procedure_priority):
            query['ProcedurePriority'] = request.procedure_priority
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.rarely_characters):
            query['RarelyCharacters'] = request.rarely_characters
        if not UtilClient.is_unset(request.read_img):
            query['ReadImg'] = request.read_img
        if not UtilClient.is_unset(request.return_url):
            query['ReturnUrl'] = request.return_url
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.suitable_type):
            query['SuitableType'] = request.suitable_type
        if not UtilClient.is_unset(request.ui_custom_url):
            query['UiCustomUrl'] = request.ui_custom_url
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.validity_date):
            query['ValidityDate'] = request.validity_date
        if not UtilClient.is_unset(request.video_evidence):
            query['VideoEvidence'] = request.video_evidence
        if not UtilClient.is_unset(request.voluntary_customized_content):
            query['VoluntaryCustomizedContent'] = request.voluntary_customized_content
        body = {}
        if not UtilClient.is_unset(request.auth_id):
            body['AuthId'] = request.auth_id
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.InitFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_face_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.InitFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.InitFaceVerifyResponse:
        """
        @param request: InitFaceVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitFaceVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_quality_check):
            query['AppQualityCheck'] = request.app_quality_check
        if not UtilClient.is_unset(request.birthday):
            query['Birthday'] = request.birthday
        if not UtilClient.is_unset(request.callback_token):
            query['CallbackToken'] = request.callback_token
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_no):
            query['CertNo'] = request.cert_no
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.certify_url_style):
            query['CertifyUrlStyle'] = request.certify_url_style
        if not UtilClient.is_unset(request.certify_url_type):
            query['CertifyUrlType'] = request.certify_url_type
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.face_contrast_picture_url):
            query['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not UtilClient.is_unset(request.face_guard_output):
            query['FaceGuardOutput'] = request.face_guard_output
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.meta_info):
            query['MetaInfo'] = request.meta_info
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_object_name):
            query['OssObjectName'] = request.oss_object_name
        if not UtilClient.is_unset(request.outer_order_no):
            query['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.procedure_priority):
            query['ProcedurePriority'] = request.procedure_priority
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.rarely_characters):
            query['RarelyCharacters'] = request.rarely_characters
        if not UtilClient.is_unset(request.read_img):
            query['ReadImg'] = request.read_img
        if not UtilClient.is_unset(request.return_url):
            query['ReturnUrl'] = request.return_url
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.suitable_type):
            query['SuitableType'] = request.suitable_type
        if not UtilClient.is_unset(request.ui_custom_url):
            query['UiCustomUrl'] = request.ui_custom_url
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.validity_date):
            query['ValidityDate'] = request.validity_date
        if not UtilClient.is_unset(request.video_evidence):
            query['VideoEvidence'] = request.video_evidence
        if not UtilClient.is_unset(request.voluntary_customized_content):
            query['VoluntaryCustomizedContent'] = request.voluntary_customized_content
        body = {}
        if not UtilClient.is_unset(request.auth_id):
            body['AuthId'] = request.auth_id
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.InitFaceVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_face_verify(
        self,
        request: cloudauth_20190307_models.InitFaceVerifyRequest,
    ) -> cloudauth_20190307_models.InitFaceVerifyResponse:
        """
        @param request: InitFaceVerifyRequest
        @return: InitFaceVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.init_face_verify_with_options(request, runtime)

    async def init_face_verify_async(
        self,
        request: cloudauth_20190307_models.InitFaceVerifyRequest,
    ) -> cloudauth_20190307_models.InitFaceVerifyResponse:
        """
        @param request: InitFaceVerifyRequest
        @return: InitFaceVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.init_face_verify_with_options_async(request, runtime)

    def insert_white_list_setting_with_options(
        self,
        request: cloudauth_20190307_models.InsertWhiteListSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.InsertWhiteListSettingResponse:
        """
        @summary 新增实人白名单
        
        @param request: InsertWhiteListSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertWhiteListSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_no):
            query['CertNo'] = request.cert_no
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.valid_day):
            query['ValidDay'] = request.valid_day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertWhiteListSetting',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.InsertWhiteListSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_white_list_setting_with_options_async(
        self,
        request: cloudauth_20190307_models.InsertWhiteListSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.InsertWhiteListSettingResponse:
        """
        @summary 新增实人白名单
        
        @param request: InsertWhiteListSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertWhiteListSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_no):
            query['CertNo'] = request.cert_no
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.valid_day):
            query['ValidDay'] = request.valid_day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertWhiteListSetting',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.InsertWhiteListSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_white_list_setting(
        self,
        request: cloudauth_20190307_models.InsertWhiteListSettingRequest,
    ) -> cloudauth_20190307_models.InsertWhiteListSettingResponse:
        """
        @summary 新增实人白名单
        
        @param request: InsertWhiteListSettingRequest
        @return: InsertWhiteListSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.insert_white_list_setting_with_options(request, runtime)

    async def insert_white_list_setting_async(
        self,
        request: cloudauth_20190307_models.InsertWhiteListSettingRequest,
    ) -> cloudauth_20190307_models.InsertWhiteListSettingResponse:
        """
        @summary 新增实人白名单
        
        @param request: InsertWhiteListSettingRequest
        @return: InsertWhiteListSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.insert_white_list_setting_with_options_async(request, runtime)

    def liveness_face_verify_with_options(
        self,
        request: cloudauth_20190307_models.LivenessFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.LivenessFaceVerifyResponse:
        """
        @param request: LivenessFaceVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LivenessFaceVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        body = {}
        if not UtilClient.is_unset(request.certify_id):
            body['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.device_token):
            body['DeviceToken'] = request.device_token
        if not UtilClient.is_unset(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        if not UtilClient.is_unset(request.face_contrast_picture_url):
            body['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.oss_bucket_name):
            body['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_object_name):
            body['OssObjectName'] = request.oss_object_name
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LivenessFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.LivenessFaceVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def liveness_face_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.LivenessFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.LivenessFaceVerifyResponse:
        """
        @param request: LivenessFaceVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LivenessFaceVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        body = {}
        if not UtilClient.is_unset(request.certify_id):
            body['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.device_token):
            body['DeviceToken'] = request.device_token
        if not UtilClient.is_unset(request.face_contrast_picture):
            body['FaceContrastPicture'] = request.face_contrast_picture
        if not UtilClient.is_unset(request.face_contrast_picture_url):
            body['FaceContrastPictureUrl'] = request.face_contrast_picture_url
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.oss_bucket_name):
            body['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_object_name):
            body['OssObjectName'] = request.oss_object_name
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LivenessFaceVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.LivenessFaceVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def liveness_face_verify(
        self,
        request: cloudauth_20190307_models.LivenessFaceVerifyRequest,
    ) -> cloudauth_20190307_models.LivenessFaceVerifyResponse:
        """
        @param request: LivenessFaceVerifyRequest
        @return: LivenessFaceVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.liveness_face_verify_with_options(request, runtime)

    async def liveness_face_verify_async(
        self,
        request: cloudauth_20190307_models.LivenessFaceVerifyRequest,
    ) -> cloudauth_20190307_models.LivenessFaceVerifyResponse:
        """
        @param request: LivenessFaceVerifyRequest
        @return: LivenessFaceVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.liveness_face_verify_with_options_async(request, runtime)

    def mobile_3meta_detail_verify_with_options(
        self,
        request: cloudauth_20190307_models.Mobile3MetaDetailVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Mobile3MetaDetailVerifyResponse:
        """
        @summary 手机三要素详版接口
        
        @param request: Mobile3MetaDetailVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Mobile3MetaDetailVerifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Mobile3MetaDetailVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.Mobile3MetaDetailVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_3meta_detail_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.Mobile3MetaDetailVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Mobile3MetaDetailVerifyResponse:
        """
        @summary 手机三要素详版接口
        
        @param request: Mobile3MetaDetailVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Mobile3MetaDetailVerifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Mobile3MetaDetailVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.Mobile3MetaDetailVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_3meta_detail_verify(
        self,
        request: cloudauth_20190307_models.Mobile3MetaDetailVerifyRequest,
    ) -> cloudauth_20190307_models.Mobile3MetaDetailVerifyResponse:
        """
        @summary 手机三要素详版接口
        
        @param request: Mobile3MetaDetailVerifyRequest
        @return: Mobile3MetaDetailVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.mobile_3meta_detail_verify_with_options(request, runtime)

    async def mobile_3meta_detail_verify_async(
        self,
        request: cloudauth_20190307_models.Mobile3MetaDetailVerifyRequest,
    ) -> cloudauth_20190307_models.Mobile3MetaDetailVerifyResponse:
        """
        @summary 手机三要素详版接口
        
        @param request: Mobile3MetaDetailVerifyRequest
        @return: Mobile3MetaDetailVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.mobile_3meta_detail_verify_with_options_async(request, runtime)

    def mobile_3meta_simple_verify_with_options(
        self,
        request: cloudauth_20190307_models.Mobile3MetaSimpleVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Mobile3MetaSimpleVerifyResponse:
        """
        @summary 手机号三要素简版接口
        
        @param request: Mobile3MetaSimpleVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Mobile3MetaSimpleVerifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Mobile3MetaSimpleVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.Mobile3MetaSimpleVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_3meta_simple_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.Mobile3MetaSimpleVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Mobile3MetaSimpleVerifyResponse:
        """
        @summary 手机号三要素简版接口
        
        @param request: Mobile3MetaSimpleVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Mobile3MetaSimpleVerifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Mobile3MetaSimpleVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.Mobile3MetaSimpleVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_3meta_simple_verify(
        self,
        request: cloudauth_20190307_models.Mobile3MetaSimpleVerifyRequest,
    ) -> cloudauth_20190307_models.Mobile3MetaSimpleVerifyResponse:
        """
        @summary 手机号三要素简版接口
        
        @param request: Mobile3MetaSimpleVerifyRequest
        @return: Mobile3MetaSimpleVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.mobile_3meta_simple_verify_with_options(request, runtime)

    async def mobile_3meta_simple_verify_async(
        self,
        request: cloudauth_20190307_models.Mobile3MetaSimpleVerifyRequest,
    ) -> cloudauth_20190307_models.Mobile3MetaSimpleVerifyResponse:
        """
        @summary 手机号三要素简版接口
        
        @param request: Mobile3MetaSimpleVerifyRequest
        @return: Mobile3MetaSimpleVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.mobile_3meta_simple_verify_with_options_async(request, runtime)

    def mobile_detect_with_options(
        self,
        request: cloudauth_20190307_models.MobileDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.MobileDetectResponse:
        """
        @summary 号码检测
        
        @param request: MobileDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MobileDetectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mobiles):
            body['Mobiles'] = request.mobiles
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MobileDetect',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.MobileDetectResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_detect_with_options_async(
        self,
        request: cloudauth_20190307_models.MobileDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.MobileDetectResponse:
        """
        @summary 号码检测
        
        @param request: MobileDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MobileDetectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mobiles):
            body['Mobiles'] = request.mobiles
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MobileDetect',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.MobileDetectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_detect(
        self,
        request: cloudauth_20190307_models.MobileDetectRequest,
    ) -> cloudauth_20190307_models.MobileDetectResponse:
        """
        @summary 号码检测
        
        @param request: MobileDetectRequest
        @return: MobileDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.mobile_detect_with_options(request, runtime)

    async def mobile_detect_async(
        self,
        request: cloudauth_20190307_models.MobileDetectRequest,
    ) -> cloudauth_20190307_models.MobileDetectResponse:
        """
        @summary 号码检测
        
        @param request: MobileDetectRequest
        @return: MobileDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.mobile_detect_with_options_async(request, runtime)

    def mobile_online_status_with_options(
        self,
        request: cloudauth_20190307_models.MobileOnlineStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.MobileOnlineStatusResponse:
        """
        @summary 查询手机号在网状态
        
        @param request: MobileOnlineStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MobileOnlineStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MobileOnlineStatus',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.MobileOnlineStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_online_status_with_options_async(
        self,
        request: cloudauth_20190307_models.MobileOnlineStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.MobileOnlineStatusResponse:
        """
        @summary 查询手机号在网状态
        
        @param request: MobileOnlineStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MobileOnlineStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MobileOnlineStatus',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.MobileOnlineStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_online_status(
        self,
        request: cloudauth_20190307_models.MobileOnlineStatusRequest,
    ) -> cloudauth_20190307_models.MobileOnlineStatusResponse:
        """
        @summary 查询手机号在网状态
        
        @param request: MobileOnlineStatusRequest
        @return: MobileOnlineStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.mobile_online_status_with_options(request, runtime)

    async def mobile_online_status_async(
        self,
        request: cloudauth_20190307_models.MobileOnlineStatusRequest,
    ) -> cloudauth_20190307_models.MobileOnlineStatusResponse:
        """
        @summary 查询手机号在网状态
        
        @param request: MobileOnlineStatusRequest
        @return: MobileOnlineStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.mobile_online_status_with_options_async(request, runtime)

    def mobile_online_time_with_options(
        self,
        request: cloudauth_20190307_models.MobileOnlineTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.MobileOnlineTimeResponse:
        """
        @summary 查询手机号在网时长
        
        @param request: MobileOnlineTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MobileOnlineTimeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MobileOnlineTime',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.MobileOnlineTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_online_time_with_options_async(
        self,
        request: cloudauth_20190307_models.MobileOnlineTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.MobileOnlineTimeResponse:
        """
        @summary 查询手机号在网时长
        
        @param request: MobileOnlineTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MobileOnlineTimeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MobileOnlineTime',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.MobileOnlineTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_online_time(
        self,
        request: cloudauth_20190307_models.MobileOnlineTimeRequest,
    ) -> cloudauth_20190307_models.MobileOnlineTimeResponse:
        """
        @summary 查询手机号在网时长
        
        @param request: MobileOnlineTimeRequest
        @return: MobileOnlineTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.mobile_online_time_with_options(request, runtime)

    async def mobile_online_time_async(
        self,
        request: cloudauth_20190307_models.MobileOnlineTimeRequest,
    ) -> cloudauth_20190307_models.MobileOnlineTimeResponse:
        """
        @summary 查询手机号在网时长
        
        @param request: MobileOnlineTimeRequest
        @return: MobileOnlineTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.mobile_online_time_with_options_async(request, runtime)

    def modify_device_info_with_options(
        self,
        request: cloudauth_20190307_models.ModifyDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ModifyDeviceInfoResponse:
        """
        @param request: ModifyDeviceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDeviceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.expired_day):
            query['ExpiredDay'] = request.expired_day
        if not UtilClient.is_unset(request.user_device_id):
            query['UserDeviceId'] = request.user_device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDeviceInfo',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.ModifyDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_device_info_with_options_async(
        self,
        request: cloudauth_20190307_models.ModifyDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ModifyDeviceInfoResponse:
        """
        @param request: ModifyDeviceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDeviceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.expired_day):
            query['ExpiredDay'] = request.expired_day
        if not UtilClient.is_unset(request.user_device_id):
            query['UserDeviceId'] = request.user_device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDeviceInfo',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.ModifyDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_device_info(
        self,
        request: cloudauth_20190307_models.ModifyDeviceInfoRequest,
    ) -> cloudauth_20190307_models.ModifyDeviceInfoResponse:
        """
        @param request: ModifyDeviceInfoRequest
        @return: ModifyDeviceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_device_info_with_options(request, runtime)

    async def modify_device_info_async(
        self,
        request: cloudauth_20190307_models.ModifyDeviceInfoRequest,
    ) -> cloudauth_20190307_models.ModifyDeviceInfoResponse:
        """
        @param request: ModifyDeviceInfoRequest
        @return: ModifyDeviceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_device_info_with_options_async(request, runtime)

    def page_query_white_list_setting_with_options(
        self,
        request: cloudauth_20190307_models.PageQueryWhiteListSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.PageQueryWhiteListSettingResponse:
        """
        @summary 分页查询实人白名单配置
        
        @param request: PageQueryWhiteListSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PageQueryWhiteListSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_no):
            query['CertNo'] = request.cert_no
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.valid_end_date):
            query['ValidEndDate'] = request.valid_end_date
        if not UtilClient.is_unset(request.valid_start_date):
            query['ValidStartDate'] = request.valid_start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PageQueryWhiteListSetting',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.PageQueryWhiteListSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def page_query_white_list_setting_with_options_async(
        self,
        request: cloudauth_20190307_models.PageQueryWhiteListSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.PageQueryWhiteListSettingResponse:
        """
        @summary 分页查询实人白名单配置
        
        @param request: PageQueryWhiteListSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PageQueryWhiteListSettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_no):
            query['CertNo'] = request.cert_no
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.valid_end_date):
            query['ValidEndDate'] = request.valid_end_date
        if not UtilClient.is_unset(request.valid_start_date):
            query['ValidStartDate'] = request.valid_start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PageQueryWhiteListSetting',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.PageQueryWhiteListSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def page_query_white_list_setting(
        self,
        request: cloudauth_20190307_models.PageQueryWhiteListSettingRequest,
    ) -> cloudauth_20190307_models.PageQueryWhiteListSettingResponse:
        """
        @summary 分页查询实人白名单配置
        
        @param request: PageQueryWhiteListSettingRequest
        @return: PageQueryWhiteListSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.page_query_white_list_setting_with_options(request, runtime)

    async def page_query_white_list_setting_async(
        self,
        request: cloudauth_20190307_models.PageQueryWhiteListSettingRequest,
    ) -> cloudauth_20190307_models.PageQueryWhiteListSettingResponse:
        """
        @summary 分页查询实人白名单配置
        
        @param request: PageQueryWhiteListSettingRequest
        @return: PageQueryWhiteListSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.page_query_white_list_setting_with_options_async(request, runtime)

    def remove_white_list_setting_with_options(
        self,
        tmp_req: cloudauth_20190307_models.RemoveWhiteListSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.RemoveWhiteListSettingResponse:
        """
        @summary 删除实人白名单
        
        @param tmp_req: RemoveWhiteListSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveWhiteListSettingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudauth_20190307_models.RemoveWhiteListSettingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveWhiteListSetting',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.RemoveWhiteListSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_white_list_setting_with_options_async(
        self,
        tmp_req: cloudauth_20190307_models.RemoveWhiteListSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.RemoveWhiteListSettingResponse:
        """
        @summary 删除实人白名单
        
        @param tmp_req: RemoveWhiteListSettingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveWhiteListSettingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudauth_20190307_models.RemoveWhiteListSettingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ids):
            request.ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ids, 'Ids', 'json')
        query = {}
        if not UtilClient.is_unset(request.ids_shrink):
            query['Ids'] = request.ids_shrink
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveWhiteListSetting',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.RemoveWhiteListSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_white_list_setting(
        self,
        request: cloudauth_20190307_models.RemoveWhiteListSettingRequest,
    ) -> cloudauth_20190307_models.RemoveWhiteListSettingResponse:
        """
        @summary 删除实人白名单
        
        @param request: RemoveWhiteListSettingRequest
        @return: RemoveWhiteListSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_white_list_setting_with_options(request, runtime)

    async def remove_white_list_setting_async(
        self,
        request: cloudauth_20190307_models.RemoveWhiteListSettingRequest,
    ) -> cloudauth_20190307_models.RemoveWhiteListSettingResponse:
        """
        @summary 删除实人白名单
        
        @param request: RemoveWhiteListSettingRequest
        @return: RemoveWhiteListSettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_white_list_setting_with_options_async(request, runtime)

    def vehicle_5item_query_with_options(
        self,
        request: cloudauth_20190307_models.Vehicle5ItemQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Vehicle5ItemQueryResponse:
        """
        @summary 车五项信息识别
        
        @param request: Vehicle5ItemQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Vehicle5ItemQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not UtilClient.is_unset(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Vehicle5ItemQuery',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.Vehicle5ItemQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def vehicle_5item_query_with_options_async(
        self,
        request: cloudauth_20190307_models.Vehicle5ItemQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Vehicle5ItemQueryResponse:
        """
        @summary 车五项信息识别
        
        @param request: Vehicle5ItemQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Vehicle5ItemQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not UtilClient.is_unset(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Vehicle5ItemQuery',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.Vehicle5ItemQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vehicle_5item_query(
        self,
        request: cloudauth_20190307_models.Vehicle5ItemQueryRequest,
    ) -> cloudauth_20190307_models.Vehicle5ItemQueryResponse:
        """
        @summary 车五项信息识别
        
        @param request: Vehicle5ItemQueryRequest
        @return: Vehicle5ItemQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.vehicle_5item_query_with_options(request, runtime)

    async def vehicle_5item_query_async(
        self,
        request: cloudauth_20190307_models.Vehicle5ItemQueryRequest,
    ) -> cloudauth_20190307_models.Vehicle5ItemQueryResponse:
        """
        @summary 车五项信息识别
        
        @param request: Vehicle5ItemQueryRequest
        @return: Vehicle5ItemQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.vehicle_5item_query_with_options_async(request, runtime)

    def vehicle_insure_query_with_options(
        self,
        request: cloudauth_20190307_models.VehicleInsureQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VehicleInsureQueryResponse:
        """
        @summary 车辆投保日期查询
        
        @param request: VehicleInsureQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VehicleInsureQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not UtilClient.is_unset(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        if not UtilClient.is_unset(request.vin):
            query['Vin'] = request.vin
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VehicleInsureQuery',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.VehicleInsureQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def vehicle_insure_query_with_options_async(
        self,
        request: cloudauth_20190307_models.VehicleInsureQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VehicleInsureQueryResponse:
        """
        @summary 车辆投保日期查询
        
        @param request: VehicleInsureQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VehicleInsureQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not UtilClient.is_unset(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        if not UtilClient.is_unset(request.vin):
            query['Vin'] = request.vin
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VehicleInsureQuery',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.VehicleInsureQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vehicle_insure_query(
        self,
        request: cloudauth_20190307_models.VehicleInsureQueryRequest,
    ) -> cloudauth_20190307_models.VehicleInsureQueryResponse:
        """
        @summary 车辆投保日期查询
        
        @param request: VehicleInsureQueryRequest
        @return: VehicleInsureQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.vehicle_insure_query_with_options(request, runtime)

    async def vehicle_insure_query_async(
        self,
        request: cloudauth_20190307_models.VehicleInsureQueryRequest,
    ) -> cloudauth_20190307_models.VehicleInsureQueryResponse:
        """
        @summary 车辆投保日期查询
        
        @param request: VehicleInsureQueryRequest
        @return: VehicleInsureQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.vehicle_insure_query_with_options_async(request, runtime)

    def vehicle_meta_verify_with_options(
        self,
        request: cloudauth_20190307_models.VehicleMetaVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VehicleMetaVerifyResponse:
        """
        @summary 车辆要素核验
        
        @param request: VehicleMetaVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VehicleMetaVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not UtilClient.is_unset(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        if not UtilClient.is_unset(request.verify_meta_type):
            query['VerifyMetaType'] = request.verify_meta_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VehicleMetaVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.VehicleMetaVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def vehicle_meta_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.VehicleMetaVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VehicleMetaVerifyResponse:
        """
        @summary 车辆要素核验
        
        @param request: VehicleMetaVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VehicleMetaVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not UtilClient.is_unset(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        if not UtilClient.is_unset(request.verify_meta_type):
            query['VerifyMetaType'] = request.verify_meta_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VehicleMetaVerify',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.VehicleMetaVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vehicle_meta_verify(
        self,
        request: cloudauth_20190307_models.VehicleMetaVerifyRequest,
    ) -> cloudauth_20190307_models.VehicleMetaVerifyResponse:
        """
        @summary 车辆要素核验
        
        @param request: VehicleMetaVerifyRequest
        @return: VehicleMetaVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.vehicle_meta_verify_with_options(request, runtime)

    async def vehicle_meta_verify_async(
        self,
        request: cloudauth_20190307_models.VehicleMetaVerifyRequest,
    ) -> cloudauth_20190307_models.VehicleMetaVerifyResponse:
        """
        @summary 车辆要素核验
        
        @param request: VehicleMetaVerifyRequest
        @return: VehicleMetaVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.vehicle_meta_verify_with_options_async(request, runtime)

    def vehicle_meta_verify_v2with_options(
        self,
        request: cloudauth_20190307_models.VehicleMetaVerifyV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VehicleMetaVerifyV2Response:
        """
        @summary 车辆要素核验增强版
        
        @param request: VehicleMetaVerifyV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: VehicleMetaVerifyV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not UtilClient.is_unset(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        if not UtilClient.is_unset(request.verify_meta_type):
            query['VerifyMetaType'] = request.verify_meta_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VehicleMetaVerifyV2',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.VehicleMetaVerifyV2Response(),
            self.call_api(params, req, runtime)
        )

    async def vehicle_meta_verify_v2with_options_async(
        self,
        request: cloudauth_20190307_models.VehicleMetaVerifyV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VehicleMetaVerifyV2Response:
        """
        @summary 车辆要素核验增强版
        
        @param request: VehicleMetaVerifyV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: VehicleMetaVerifyV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identify_num):
            query['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not UtilClient.is_unset(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        if not UtilClient.is_unset(request.verify_meta_type):
            query['VerifyMetaType'] = request.verify_meta_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VehicleMetaVerifyV2',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.VehicleMetaVerifyV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def vehicle_meta_verify_v2(
        self,
        request: cloudauth_20190307_models.VehicleMetaVerifyV2Request,
    ) -> cloudauth_20190307_models.VehicleMetaVerifyV2Response:
        """
        @summary 车辆要素核验增强版
        
        @param request: VehicleMetaVerifyV2Request
        @return: VehicleMetaVerifyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.vehicle_meta_verify_v2with_options(request, runtime)

    async def vehicle_meta_verify_v2_async(
        self,
        request: cloudauth_20190307_models.VehicleMetaVerifyV2Request,
    ) -> cloudauth_20190307_models.VehicleMetaVerifyV2Response:
        """
        @summary 车辆要素核验增强版
        
        @param request: VehicleMetaVerifyV2Request
        @return: VehicleMetaVerifyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.vehicle_meta_verify_v2with_options_async(request, runtime)

    def vehicle_query_with_options(
        self,
        request: cloudauth_20190307_models.VehicleQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VehicleQueryResponse:
        """
        @summary 车辆信息识别
        
        @param request: VehicleQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VehicleQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not UtilClient.is_unset(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VehicleQuery',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.VehicleQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def vehicle_query_with_options_async(
        self,
        request: cloudauth_20190307_models.VehicleQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VehicleQueryResponse:
        """
        @summary 车辆信息识别
        
        @param request: VehicleQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VehicleQueryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_type):
            query['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.vehicle_num):
            query['VehicleNum'] = request.vehicle_num
        if not UtilClient.is_unset(request.vehicle_type):
            query['VehicleType'] = request.vehicle_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VehicleQuery',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.VehicleQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vehicle_query(
        self,
        request: cloudauth_20190307_models.VehicleQueryRequest,
    ) -> cloudauth_20190307_models.VehicleQueryResponse:
        """
        @summary 车辆信息识别
        
        @param request: VehicleQueryRequest
        @return: VehicleQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.vehicle_query_with_options(request, runtime)

    async def vehicle_query_async(
        self,
        request: cloudauth_20190307_models.VehicleQueryRequest,
    ) -> cloudauth_20190307_models.VehicleQueryResponse:
        """
        @summary 车辆信息识别
        
        @param request: VehicleQueryRequest
        @return: VehicleQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.vehicle_query_with_options_async(request, runtime)

    def verify_material_with_options(
        self,
        request: cloudauth_20190307_models.VerifyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VerifyMaterialResponse:
        """
        @param request: VerifyMaterialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyMaterialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.face_image_url):
            query['FaceImageUrl'] = request.face_image_url
        if not UtilClient.is_unset(request.id_card_back_image_url):
            query['IdCardBackImageUrl'] = request.id_card_back_image_url
        if not UtilClient.is_unset(request.id_card_front_image_url):
            query['IdCardFrontImageUrl'] = request.id_card_front_image_url
        if not UtilClient.is_unset(request.id_card_number):
            query['IdCardNumber'] = request.id_card_number
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyMaterial',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.VerifyMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_material_with_options_async(
        self,
        request: cloudauth_20190307_models.VerifyMaterialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.VerifyMaterialResponse:
        """
        @param request: VerifyMaterialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyMaterialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.face_image_url):
            query['FaceImageUrl'] = request.face_image_url
        if not UtilClient.is_unset(request.id_card_back_image_url):
            query['IdCardBackImageUrl'] = request.id_card_back_image_url
        if not UtilClient.is_unset(request.id_card_front_image_url):
            query['IdCardFrontImageUrl'] = request.id_card_front_image_url
        if not UtilClient.is_unset(request.id_card_number):
            query['IdCardNumber'] = request.id_card_number
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyMaterial',
            version='2019-03-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20190307_models.VerifyMaterialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_material(
        self,
        request: cloudauth_20190307_models.VerifyMaterialRequest,
    ) -> cloudauth_20190307_models.VerifyMaterialResponse:
        """
        @param request: VerifyMaterialRequest
        @return: VerifyMaterialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_material_with_options(request, runtime)

    async def verify_material_async(
        self,
        request: cloudauth_20190307_models.VerifyMaterialRequest,
    ) -> cloudauth_20190307_models.VerifyMaterialResponse:
        """
        @param request: VerifyMaterialRequest
        @return: VerifyMaterialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_material_with_options_async(request, runtime)
