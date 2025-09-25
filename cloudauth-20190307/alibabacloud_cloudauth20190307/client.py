# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.request import TeaRequest
from Tea.exceptions import TeaException
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_fileform.client import Client as FileFormClient
from alibabacloud_tea_xml.client import Client as XMLClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudauth20190307 import models as cloudauth_20190307_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_tea_fileform import models as file_form_models


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

    def _post_ossobject(
        self,
        bucket_name: str,
        data: dict,
    ) -> dict:
        _request = TeaRequest()
        form = UtilClient.assert_as_map(data)
        boundary = FileFormClient.get_boundary()
        host = UtilClient.assert_as_string(form.get('host'))
        _request.protocol = 'HTTPS'
        _request.method = 'POST'
        _request.pathname = f'/'
        _request.headers = {
            'host': host,
            'date': UtilClient.get_date_utcstring(),
            'user-agent': UtilClient.get_user_agent('')
        }
        _request.headers['content-type'] = f'multipart/form-data; boundary={boundary}'
        _request.body = FileFormClient.to_file_form(form, boundary)
        _last_request = _request
        _response = TeaCore.do_action(_request)
        resp_map = None
        body_str = UtilClient.read_as_string(_response.body)
        if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
            resp_map = XMLClient.parse_xml(body_str, None)
            err = UtilClient.assert_as_map(resp_map.get('Error'))
            raise TeaException({
                'code': err.get('Code'),
                'message': err.get('Message'),
                'data': {
                    'httpCode': _response.status_code,
                    'requestId': err.get('RequestId'),
                    'hostId': err.get('HostId')
                }
            })
        resp_map = XMLClient.parse_xml(body_str, None)
        return TeaCore.merge(resp_map)

    async def _post_ossobject_async(
        self,
        bucket_name: str,
        data: dict,
    ) -> dict:
        _request = TeaRequest()
        form = UtilClient.assert_as_map(data)
        boundary = FileFormClient.get_boundary()
        host = UtilClient.assert_as_string(form.get('host'))
        _request.protocol = 'HTTPS'
        _request.method = 'POST'
        _request.pathname = f'/'
        _request.headers = {
            'host': host,
            'date': UtilClient.get_date_utcstring(),
            'user-agent': UtilClient.get_user_agent('')
        }
        _request.headers['content-type'] = f'multipart/form-data; boundary={boundary}'
        _request.body = FileFormClient.to_file_form(form, boundary)
        _last_request = _request
        _response = await TeaCore.async_do_action(_request)
        resp_map = None
        body_str = await UtilClient.read_as_string_async(_response.body)
        if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(_response.status_code):
            resp_map = XMLClient.parse_xml(body_str, None)
            err = UtilClient.assert_as_map(resp_map.get('Error'))
            raise TeaException({
                'code': err.get('Code'),
                'message': err.get('Message'),
                'data': {
                    'httpCode': _response.status_code,
                    'requestId': err.get('RequestId'),
                    'hostId': err.get('HostId')
                }
            })
        resp_map = XMLClient.parse_xml(body_str, None)
        return TeaCore.merge(resp_map)

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
        @summary Add AIGC Face Detection Capability
        
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
        @summary Add AIGC Face Detection Capability
        
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
        @summary Add AIGC Face Detection Capability
        
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
        @summary Add AIGC Face Detection Capability
        
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
        @summary Bank Card Element Verification Interface
        
        @description Bank card verification, including: two elements (name + bank card number), three elements (name + ID number + bank card number), and four elements (name + ID number + mobile phone number + bank card number) consistency verification.
        - Service address:
        - Beijing region: cloudauth.cn-beijing.aliyuncs.com (IPv4) or cloudauth-dualstack.cn-beijing.aliyuncs.com (IPv6).
        - Shanghai region: cloudauth.cn-shanghai.aliyuncs.com (IPv4) or cloudauth-dualstack.cn-shanghai.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Bank Card Element Verification Interface
        
        @description Bank card verification, including: two elements (name + bank card number), three elements (name + ID number + bank card number), and four elements (name + ID number + mobile phone number + bank card number) consistency verification.
        - Service address:
        - Beijing region: cloudauth.cn-beijing.aliyuncs.com (IPv4) or cloudauth-dualstack.cn-beijing.aliyuncs.com (IPv6).
        - Shanghai region: cloudauth.cn-shanghai.aliyuncs.com (IPv4) or cloudauth-dualstack.cn-shanghai.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Bank Card Element Verification Interface
        
        @description Bank card verification, including: two elements (name + bank card number), three elements (name + ID number + bank card number), and four elements (name + ID number + mobile phone number + bank card number) consistency verification.
        - Service address:
        - Beijing region: cloudauth.cn-beijing.aliyuncs.com (IPv4) or cloudauth-dualstack.cn-beijing.aliyuncs.com (IPv6).
        - Shanghai region: cloudauth.cn-shanghai.aliyuncs.com (IPv4) or cloudauth-dualstack.cn-shanghai.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Bank Card Element Verification Interface
        
        @description Bank card verification, including: two elements (name + bank card number), three elements (name + ID number + bank card number), and four elements (name + ID number + mobile phone number + bank card number) consistency verification.
        - Service address:
        - Beijing region: cloudauth.cn-beijing.aliyuncs.com (IPv4) or cloudauth-dualstack.cn-beijing.aliyuncs.com (IPv6).
        - Shanghai region: cloudauth.cn-shanghai.aliyuncs.com (IPv4) or cloudauth-dualstack.cn-shanghai.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Financial-grade Pure Server-Side API for Face Comparison.
        
        @description - API Name: CompareFaceVerify.
        - Service Address: cloudauth.aliyuncs.com.
        - Request Method: HTTPS POST and GET.
        - API Description: An interface to achieve real-person authentication through server-side integration.
        #### Photo Format Requirements
        When performing face comparison, please upload 2 facial photos that meet all the following conditions:
        - Recent photo/recent database photo, with a complete, clear, unobstructed face, natural expression, and facing the camera directly.
        - Clear photo with normal exposure, no overly dark, overly bright, or halo effects on the face, and no significant angle deviation.
        - Resolution not exceeding 19201080, at least 640*480, recommended to scale the shorter side to 720 pixels, with a compression ratio greater than 0.9.
        - Photo size: <1MB.
        - Supports 90, 180, and 270-degree photos; in cases of multiple faces, the largest face will be selected.
        
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
        @summary Financial-grade Pure Server-Side API for Face Comparison.
        
        @description - API Name: CompareFaceVerify.
        - Service Address: cloudauth.aliyuncs.com.
        - Request Method: HTTPS POST and GET.
        - API Description: An interface to achieve real-person authentication through server-side integration.
        #### Photo Format Requirements
        When performing face comparison, please upload 2 facial photos that meet all the following conditions:
        - Recent photo/recent database photo, with a complete, clear, unobstructed face, natural expression, and facing the camera directly.
        - Clear photo with normal exposure, no overly dark, overly bright, or halo effects on the face, and no significant angle deviation.
        - Resolution not exceeding 19201080, at least 640*480, recommended to scale the shorter side to 720 pixels, with a compression ratio greater than 0.9.
        - Photo size: <1MB.
        - Supports 90, 180, and 270-degree photos; in cases of multiple faces, the largest face will be selected.
        
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
        @summary Financial-grade Pure Server-Side API for Face Comparison.
        
        @description - API Name: CompareFaceVerify.
        - Service Address: cloudauth.aliyuncs.com.
        - Request Method: HTTPS POST and GET.
        - API Description: An interface to achieve real-person authentication through server-side integration.
        #### Photo Format Requirements
        When performing face comparison, please upload 2 facial photos that meet all the following conditions:
        - Recent photo/recent database photo, with a complete, clear, unobstructed face, natural expression, and facing the camera directly.
        - Clear photo with normal exposure, no overly dark, overly bright, or halo effects on the face, and no significant angle deviation.
        - Resolution not exceeding 19201080, at least 640*480, recommended to scale the shorter side to 720 pixels, with a compression ratio greater than 0.9.
        - Photo size: <1MB.
        - Supports 90, 180, and 270-degree photos; in cases of multiple faces, the largest face will be selected.
        
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
        @summary Financial-grade Pure Server-Side API for Face Comparison.
        
        @description - API Name: CompareFaceVerify.
        - Service Address: cloudauth.aliyuncs.com.
        - Request Method: HTTPS POST and GET.
        - API Description: An interface to achieve real-person authentication through server-side integration.
        #### Photo Format Requirements
        When performing face comparison, please upload 2 facial photos that meet all the following conditions:
        - Recent photo/recent database photo, with a complete, clear, unobstructed face, natural expression, and facing the camera directly.
        - Clear photo with normal exposure, no overly dark, overly bright, or halo effects on the face, and no significant angle deviation.
        - Resolution not exceeding 19201080, at least 640*480, recommended to scale the shorter side to 720 pixels, with a compression ratio greater than 0.9.
        - Photo size: <1MB.
        - Supports 90, 180, and 270-degree photos; in cases of multiple faces, the largest face will be selected.
        
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
        @summary Invoke CompareFaces for face comparison.
        
        @description Request Method: Only supports sending requests via HTTPS POST.
        Interface Description: Compares two face images and outputs the similarity score of the faces in the two images as the result.
        - At least one of the specified comparison images should be a face photo (FacePic).
        - If an image contains multiple faces, the algorithm will automatically select the largest face in the image.
        - If one of the two comparison images does not detect a face, the system will return an error message stating \\"No face detected\\".
        When uploading images, you need to provide the HTTP address or base64 encoding of the image.
        - HTTP Address: A publicly accessible HTTP address. For example, `http://image-demo.img-cn-hangzhou.aliyuncs.com/example.jpg`.
        - Base64 Encoding: An image encoded in base64, formatted as `base64://<base64 string of the image>`.
        Image Restrictions
        - Does not support relative or absolute paths for local images.
        - Please keep the size of a single image within 2MB to avoid timeout during retrieval by the algorithm.
        - The body of a single request has a size limit of 8MB; please calculate the total size of all images and other information in the request to ensure it does not exceed this limit.
        - When using base64 to transmit images, the request method must be changed to POST; the header description such as `data:image/png;base64,` should be removed from the base64 string of the image.
        
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
        @summary Invoke CompareFaces for face comparison.
        
        @description Request Method: Only supports sending requests via HTTPS POST.
        Interface Description: Compares two face images and outputs the similarity score of the faces in the two images as the result.
        - At least one of the specified comparison images should be a face photo (FacePic).
        - If an image contains multiple faces, the algorithm will automatically select the largest face in the image.
        - If one of the two comparison images does not detect a face, the system will return an error message stating \\"No face detected\\".
        When uploading images, you need to provide the HTTP address or base64 encoding of the image.
        - HTTP Address: A publicly accessible HTTP address. For example, `http://image-demo.img-cn-hangzhou.aliyuncs.com/example.jpg`.
        - Base64 Encoding: An image encoded in base64, formatted as `base64://<base64 string of the image>`.
        Image Restrictions
        - Does not support relative or absolute paths for local images.
        - Please keep the size of a single image within 2MB to avoid timeout during retrieval by the algorithm.
        - The body of a single request has a size limit of 8MB; please calculate the total size of all images and other information in the request to ensure it does not exceed this limit.
        - When using base64 to transmit images, the request method must be changed to POST; the header description such as `data:image/png;base64,` should be removed from the base64 string of the image.
        
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
        @summary Invoke CompareFaces for face comparison.
        
        @description Request Method: Only supports sending requests via HTTPS POST.
        Interface Description: Compares two face images and outputs the similarity score of the faces in the two images as the result.
        - At least one of the specified comparison images should be a face photo (FacePic).
        - If an image contains multiple faces, the algorithm will automatically select the largest face in the image.
        - If one of the two comparison images does not detect a face, the system will return an error message stating \\"No face detected\\".
        When uploading images, you need to provide the HTTP address or base64 encoding of the image.
        - HTTP Address: A publicly accessible HTTP address. For example, `http://image-demo.img-cn-hangzhou.aliyuncs.com/example.jpg`.
        - Base64 Encoding: An image encoded in base64, formatted as `base64://<base64 string of the image>`.
        Image Restrictions
        - Does not support relative or absolute paths for local images.
        - Please keep the size of a single image within 2MB to avoid timeout during retrieval by the algorithm.
        - The body of a single request has a size limit of 8MB; please calculate the total size of all images and other information in the request to ensure it does not exceed this limit.
        - When using base64 to transmit images, the request method must be changed to POST; the header description such as `data:image/png;base64,` should be removed from the base64 string of the image.
        
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
        @summary Invoke CompareFaces for face comparison.
        
        @description Request Method: Only supports sending requests via HTTPS POST.
        Interface Description: Compares two face images and outputs the similarity score of the faces in the two images as the result.
        - At least one of the specified comparison images should be a face photo (FacePic).
        - If an image contains multiple faces, the algorithm will automatically select the largest face in the image.
        - If one of the two comparison images does not detect a face, the system will return an error message stating \\"No face detected\\".
        When uploading images, you need to provide the HTTP address or base64 encoding of the image.
        - HTTP Address: A publicly accessible HTTP address. For example, `http://image-demo.img-cn-hangzhou.aliyuncs.com/example.jpg`.
        - Base64 Encoding: An image encoded in base64, formatted as `base64://<base64 string of the image>`.
        Image Restrictions
        - Does not support relative or absolute paths for local images.
        - Please keep the size of a single image within 2MB to avoid timeout during retrieval by the algorithm.
        - The body of a single request has a size limit of 8MB; please calculate the total size of all images and other information in the request to ensure it does not exceed this limit.
        - When using base64 to transmit images, the request method must be changed to POST; the header description such as `data:image/png;base64,` should be removed from the base64 string of the image.
        
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
        @summary This interface is used to submit authentication materials for verification and comparison, and it synchronously returns the authentication result.
        
        @description - Interface Name: ContrastFaceVerify.
        - Service Address: cloudauth.aliyuncs.com.
        - Request Method: HTTPS POST and GET.
        - Interface Description: An interface for real person authentication through server-side integration.
        #### Image Format Requirements
        When performing real person authentication, please ensure that the images you upload meet all of the following conditions:
        - Recent photo with a clear, unobstructed, and natural expression, facing the camera directly.
        - Clear and properly exposed photo, without overly dark, bright, or haloed faces, and with minimal angle deviation.
        - Resolution not exceeding 19201080, at least 640*480, with the shorter side recommended to be resized to 720 pixels, and a compression ratio greater than 0.9.
        - Photo size: <1MB.
        - Supports 90, 180, and 270-degree photos; in cases of multiple faces, the largest face will be selected.
        
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
        @summary This interface is used to submit authentication materials for verification and comparison, and it synchronously returns the authentication result.
        
        @description - Interface Name: ContrastFaceVerify.
        - Service Address: cloudauth.aliyuncs.com.
        - Request Method: HTTPS POST and GET.
        - Interface Description: An interface for real person authentication through server-side integration.
        #### Image Format Requirements
        When performing real person authentication, please ensure that the images you upload meet all of the following conditions:
        - Recent photo with a clear, unobstructed, and natural expression, facing the camera directly.
        - Clear and properly exposed photo, without overly dark, bright, or haloed faces, and with minimal angle deviation.
        - Resolution not exceeding 19201080, at least 640*480, with the shorter side recommended to be resized to 720 pixels, and a compression ratio greater than 0.9.
        - Photo size: <1MB.
        - Supports 90, 180, and 270-degree photos; in cases of multiple faces, the largest face will be selected.
        
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
        @summary This interface is used to submit authentication materials for verification and comparison, and it synchronously returns the authentication result.
        
        @description - Interface Name: ContrastFaceVerify.
        - Service Address: cloudauth.aliyuncs.com.
        - Request Method: HTTPS POST and GET.
        - Interface Description: An interface for real person authentication through server-side integration.
        #### Image Format Requirements
        When performing real person authentication, please ensure that the images you upload meet all of the following conditions:
        - Recent photo with a clear, unobstructed, and natural expression, facing the camera directly.
        - Clear and properly exposed photo, without overly dark, bright, or haloed faces, and with minimal angle deviation.
        - Resolution not exceeding 19201080, at least 640*480, with the shorter side recommended to be resized to 720 pixels, and a compression ratio greater than 0.9.
        - Photo size: <1MB.
        - Supports 90, 180, and 270-degree photos; in cases of multiple faces, the largest face will be selected.
        
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
        @summary This interface is used to submit authentication materials for verification and comparison, and it synchronously returns the authentication result.
        
        @description - Interface Name: ContrastFaceVerify.
        - Service Address: cloudauth.aliyuncs.com.
        - Request Method: HTTPS POST and GET.
        - Interface Description: An interface for real person authentication through server-side integration.
        #### Image Format Requirements
        When performing real person authentication, please ensure that the images you upload meet all of the following conditions:
        - Recent photo with a clear, unobstructed, and natural expression, facing the camera directly.
        - Clear and properly exposed photo, without overly dark, bright, or haloed faces, and with minimal angle deviation.
        - Resolution not exceeding 19201080, at least 640*480, with the shorter side recommended to be resized to 720 pixels, and a compression ratio greater than 0.9.
        - Photo size: <1MB.
        - Supports 90, 180, and 270-degree photos; in cases of multiple faces, the largest face will be selected.
        
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
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
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
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Cloudauth',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        contrast_face_verify_req = cloudauth_20190307_models.ContrastFaceVerifyRequest()
        OpenApiUtilClient.convert(request, contrast_face_verify_req)
        if not UtilClient.is_unset(request.face_contrast_file_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.face_contrast_file_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            contrast_face_verify_req.face_contrast_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        contrast_face_verify_resp = self.contrast_face_verify_with_options(contrast_face_verify_req, runtime)
        return contrast_face_verify_resp

    async def contrast_face_verify_advance_async(
        self,
        request: cloudauth_20190307_models.ContrastFaceVerifyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.ContrastFaceVerifyResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
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
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Cloudauth',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        contrast_face_verify_req = cloudauth_20190307_models.ContrastFaceVerifyRequest()
        OpenApiUtilClient.convert(request, contrast_face_verify_req)
        if not UtilClient.is_unset(request.face_contrast_file_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.face_contrast_file_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            contrast_face_verify_req.face_contrast_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        contrast_face_verify_resp = await self.contrast_face_verify_with_options_async(contrast_face_verify_req, runtime)
        return contrast_face_verify_resp

    def create_auth_key_with_options(
        self,
        request: cloudauth_20190307_models.CreateAuthKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CreateAuthKeyResponse:
        """
        @summary Call CreateAuthKey to get the authorization key, which is used for offline face recognition SDK activation.
        
        @description Request Method: Supports sending requests via HTTPS POST and GET methods.
        > The authorization key is valid for 30 minutes and cannot be reused. It is recommended to re-obtain it before each activation.
        
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
        @summary Call CreateAuthKey to get the authorization key, which is used for offline face recognition SDK activation.
        
        @description Request Method: Supports sending requests via HTTPS POST and GET methods.
        > The authorization key is valid for 30 minutes and cannot be reused. It is recommended to re-obtain it before each activation.
        
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
        @summary Call CreateAuthKey to get the authorization key, which is used for offline face recognition SDK activation.
        
        @description Request Method: Supports sending requests via HTTPS POST and GET methods.
        > The authorization key is valid for 30 minutes and cannot be reused. It is recommended to re-obtain it before each activation.
        
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
        @summary Call CreateAuthKey to get the authorization key, which is used for offline face recognition SDK activation.
        
        @description Request Method: Supports sending requests via HTTPS POST and GET methods.
        > The authorization key is valid for 30 minutes and cannot be reused. It is recommended to re-obtain it before each activation.
        
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
        @summary Call CreateVerifySetting to create a verification scenario configuration. This operation is equivalent to creating a new verification scenario on the console.
        
        @description Request Method: Only supports sending requests via HTTPS POST.
        
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
        @summary Call CreateVerifySetting to create a verification scenario configuration. This operation is equivalent to creating a new verification scenario on the console.
        
        @description Request Method: Only supports sending requests via HTTPS POST.
        
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
        @summary Call CreateVerifySetting to create a verification scenario configuration. This operation is equivalent to creating a new verification scenario on the console.
        
        @description Request Method: Only supports sending requests via HTTPS POST.
        
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
        @summary Call CreateVerifySetting to create a verification scenario configuration. This operation is equivalent to creating a new verification scenario on the console.
        
        @description Request Method: Only supports sending requests via HTTPS POST.
        
        @param request: CreateVerifySettingRequest
        @return: CreateVerifySettingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_verify_setting_with_options_async(request, runtime)

    def credential_product_verify_v2with_options(
        self,
        request: cloudauth_20190307_models.CredentialProductVerifyV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CredentialProductVerifyV2Response:
        """
        @summary Product Credential Verification
        
        @description Upload e-commerce product images to perform tampering, quality (clarity), and similar image detection, returning risk labels and scores.
        
        @param request: CredentialProductVerifyV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: CredentialProductVerifyV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cred_name):
            query['CredName'] = request.cred_name
        if not UtilClient.is_unset(request.cred_type):
            query['CredType'] = request.cred_type
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.merchant_id):
            query['MerchantId'] = request.merchant_id
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
            action='CredentialProductVerifyV2',
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
            cloudauth_20190307_models.CredentialProductVerifyV2Response(),
            self.call_api(params, req, runtime)
        )

    async def credential_product_verify_v2with_options_async(
        self,
        request: cloudauth_20190307_models.CredentialProductVerifyV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CredentialProductVerifyV2Response:
        """
        @summary Product Credential Verification
        
        @description Upload e-commerce product images to perform tampering, quality (clarity), and similar image detection, returning risk labels and scores.
        
        @param request: CredentialProductVerifyV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: CredentialProductVerifyV2Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cred_name):
            query['CredName'] = request.cred_name
        if not UtilClient.is_unset(request.cred_type):
            query['CredType'] = request.cred_type
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.merchant_id):
            query['MerchantId'] = request.merchant_id
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
            action='CredentialProductVerifyV2',
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
            cloudauth_20190307_models.CredentialProductVerifyV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def credential_product_verify_v2(
        self,
        request: cloudauth_20190307_models.CredentialProductVerifyV2Request,
    ) -> cloudauth_20190307_models.CredentialProductVerifyV2Response:
        """
        @summary Product Credential Verification
        
        @description Upload e-commerce product images to perform tampering, quality (clarity), and similar image detection, returning risk labels and scores.
        
        @param request: CredentialProductVerifyV2Request
        @return: CredentialProductVerifyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.credential_product_verify_v2with_options(request, runtime)

    async def credential_product_verify_v2_async(
        self,
        request: cloudauth_20190307_models.CredentialProductVerifyV2Request,
    ) -> cloudauth_20190307_models.CredentialProductVerifyV2Response:
        """
        @summary Product Credential Verification
        
        @description Upload e-commerce product images to perform tampering, quality (clarity), and similar image detection, returning risk labels and scores.
        
        @param request: CredentialProductVerifyV2Request
        @return: CredentialProductVerifyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.credential_product_verify_v2with_options_async(request, runtime)

    def credential_product_verify_v2advance(
        self,
        request: cloudauth_20190307_models.CredentialProductVerifyV2AdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CredentialProductVerifyV2Response:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
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
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Cloudauth',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        credential_product_verify_v2req = cloudauth_20190307_models.CredentialProductVerifyV2Request()
        OpenApiUtilClient.convert(request, credential_product_verify_v2req)
        if not UtilClient.is_unset(request.image_file_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_file_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            credential_product_verify_v2req.image_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        credential_product_verify_v2resp = self.credential_product_verify_v2with_options(credential_product_verify_v2req, runtime)
        return credential_product_verify_v2resp

    async def credential_product_verify_v2advance_async(
        self,
        request: cloudauth_20190307_models.CredentialProductVerifyV2AdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CredentialProductVerifyV2Response:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
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
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Cloudauth',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        credential_product_verify_v2req = cloudauth_20190307_models.CredentialProductVerifyV2Request()
        OpenApiUtilClient.convert(request, credential_product_verify_v2req)
        if not UtilClient.is_unset(request.image_file_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_file_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            credential_product_verify_v2req.image_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        credential_product_verify_v2resp = await self.credential_product_verify_v2with_options_async(credential_product_verify_v2req, runtime)
        return credential_product_verify_v2resp

    def credential_verify_with_options(
        self,
        tmp_req: cloudauth_20190307_models.CredentialVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CredentialVerifyResponse:
        """
        @summary Credential verification
        
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
        @summary Credential verification
        
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
        @summary Credential verification
        
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
        @summary Credential verification
        
        @param request: CredentialVerifyRequest
        @return: CredentialVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.credential_verify_with_options_async(request, runtime)

    def credential_verify_v2with_options(
        self,
        tmp_req: cloudauth_20190307_models.CredentialVerifyV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CredentialVerifyV2Response:
        """
        @summary Credential Verification
        
        @description Input credential image information, perform image tampering and forgery detection, and image semantic understanding. Return the risk detection results.
        
        @param tmp_req: CredentialVerifyV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: CredentialVerifyV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = cloudauth_20190307_models.CredentialVerifyV2ShrinkRequest()
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
            query['IsOcr'] = request.is_ocr
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
        if not UtilClient.is_unset(request.image_file):
            body['ImageFile'] = request.image_file
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CredentialVerifyV2',
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
            cloudauth_20190307_models.CredentialVerifyV2Response(),
            self.call_api(params, req, runtime)
        )

    async def credential_verify_v2with_options_async(
        self,
        tmp_req: cloudauth_20190307_models.CredentialVerifyV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CredentialVerifyV2Response:
        """
        @summary Credential Verification
        
        @description Input credential image information, perform image tampering and forgery detection, and image semantic understanding. Return the risk detection results.
        
        @param tmp_req: CredentialVerifyV2Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: CredentialVerifyV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = cloudauth_20190307_models.CredentialVerifyV2ShrinkRequest()
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
            query['IsOcr'] = request.is_ocr
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
        if not UtilClient.is_unset(request.image_file):
            body['ImageFile'] = request.image_file
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CredentialVerifyV2',
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
            cloudauth_20190307_models.CredentialVerifyV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def credential_verify_v2(
        self,
        request: cloudauth_20190307_models.CredentialVerifyV2Request,
    ) -> cloudauth_20190307_models.CredentialVerifyV2Response:
        """
        @summary Credential Verification
        
        @description Input credential image information, perform image tampering and forgery detection, and image semantic understanding. Return the risk detection results.
        
        @param request: CredentialVerifyV2Request
        @return: CredentialVerifyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return self.credential_verify_v2with_options(request, runtime)

    async def credential_verify_v2_async(
        self,
        request: cloudauth_20190307_models.CredentialVerifyV2Request,
    ) -> cloudauth_20190307_models.CredentialVerifyV2Response:
        """
        @summary Credential Verification
        
        @description Input credential image information, perform image tampering and forgery detection, and image semantic understanding. Return the risk detection results.
        
        @param request: CredentialVerifyV2Request
        @return: CredentialVerifyV2Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.credential_verify_v2with_options_async(request, runtime)

    def credential_verify_v2advance(
        self,
        request: cloudauth_20190307_models.CredentialVerifyV2AdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CredentialVerifyV2Response:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
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
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Cloudauth',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        credential_verify_v2req = cloudauth_20190307_models.CredentialVerifyV2Request()
        OpenApiUtilClient.convert(request, credential_verify_v2req)
        if not UtilClient.is_unset(request.image_file_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_file_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            credential_verify_v2req.image_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        credential_verify_v2resp = self.credential_verify_v2with_options(credential_verify_v2req, runtime)
        return credential_verify_v2resp

    async def credential_verify_v2advance_async(
        self,
        request: cloudauth_20190307_models.CredentialVerifyV2AdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.CredentialVerifyV2Response:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
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
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Cloudauth',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        credential_verify_v2req = cloudauth_20190307_models.CredentialVerifyV2Request()
        OpenApiUtilClient.convert(request, credential_verify_v2req)
        if not UtilClient.is_unset(request.image_file_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.image_file_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            credential_verify_v2req.image_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        credential_verify_v2resp = await self.credential_verify_v2with_options_async(credential_verify_v2req, runtime)
        return credential_verify_v2resp

    def deepfake_detect_with_options(
        self,
        request: cloudauth_20190307_models.DeepfakeDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DeepfakeDetectResponse:
        """
        @summary Face Credential Verification Service
        
        @description > The Face Deepfake Detection API is currently in the free public beta stage, which will end on August 30, 2024, at 23:59:59. During the public beta, the QPS (Queries Per Second) cannot exceed 3 times/second.
        - Service address: cloudauth.aliyuncs.com (IPv4) or cloudauth-dualstack.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Face Credential Verification Service
        
        @description > The Face Deepfake Detection API is currently in the free public beta stage, which will end on August 30, 2024, at 23:59:59. During the public beta, the QPS (Queries Per Second) cannot exceed 3 times/second.
        - Service address: cloudauth.aliyuncs.com (IPv4) or cloudauth-dualstack.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Face Credential Verification Service
        
        @description > The Face Deepfake Detection API is currently in the free public beta stage, which will end on August 30, 2024, at 23:59:59. During the public beta, the QPS (Queries Per Second) cannot exceed 3 times/second.
        - Service address: cloudauth.aliyuncs.com (IPv4) or cloudauth-dualstack.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Face Credential Verification Service
        
        @description > The Face Deepfake Detection API is currently in the free public beta stage, which will end on August 30, 2024, at 23:59:59. During the public beta, the QPS (Queries Per Second) cannot exceed 3 times/second.
        - Service address: cloudauth.aliyuncs.com (IPv4) or cloudauth-dualstack.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Financial Level Sensitive Data Deletion Interface
        
        @description Deletes all personal information fields in the request, including name, ID number, phone number, IP, images, videos, and device information, etc.
        
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
        @summary Financial Level Sensitive Data Deletion Interface
        
        @description Deletes all personal information fields in the request, including name, ID number, phone number, IP, images, videos, and device information, etc.
        
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
        @summary Financial Level Sensitive Data Deletion Interface
        
        @description Deletes all personal information fields in the request, including name, ID number, phone number, IP, images, videos, and device information, etc.
        
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
        @summary Financial Level Sensitive Data Deletion Interface
        
        @description Deletes all personal information fields in the request, including name, ID number, phone number, IP, images, videos, and device information, etc.
        
        @param request: DeleteFaceVerifyResultRequest
        @return: DeleteFaceVerifyResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_verify_result_with_options_async(request, runtime)

    def describe_card_verify_with_options(
        self,
        request: cloudauth_20190307_models.DescribeCardVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeCardVerifyResponse:
        """
        @summary Obtain Authentication Results from Image Element Verification
        
        @description After receiving the callback notification, you can use this interface on the server side to obtain the corresponding authentication status and information.
        
        @param request: DescribeCardVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCardVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCardVerify',
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
            cloudauth_20190307_models.DescribeCardVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_card_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.DescribeCardVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeCardVerifyResponse:
        """
        @summary Obtain Authentication Results from Image Element Verification
        
        @description After receiving the callback notification, you can use this interface on the server side to obtain the corresponding authentication status and information.
        
        @param request: DescribeCardVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCardVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certify_id):
            query['CertifyId'] = request.certify_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCardVerify',
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
            cloudauth_20190307_models.DescribeCardVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_card_verify(
        self,
        request: cloudauth_20190307_models.DescribeCardVerifyRequest,
    ) -> cloudauth_20190307_models.DescribeCardVerifyResponse:
        """
        @summary Obtain Authentication Results from Image Element Verification
        
        @description After receiving the callback notification, you can use this interface on the server side to obtain the corresponding authentication status and information.
        
        @param request: DescribeCardVerifyRequest
        @return: DescribeCardVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_card_verify_with_options(request, runtime)

    async def describe_card_verify_async(
        self,
        request: cloudauth_20190307_models.DescribeCardVerifyRequest,
    ) -> cloudauth_20190307_models.DescribeCardVerifyResponse:
        """
        @summary Obtain Authentication Results from Image Element Verification
        
        @description After receiving the callback notification, you can use this interface on the server side to obtain the corresponding authentication status and information.
        
        @param request: DescribeCardVerifyRequest
        @return: DescribeCardVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_card_verify_with_options_async(request, runtime)

    def describe_device_info_with_options(
        self,
        request: cloudauth_20190307_models.DescribeDeviceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.DescribeDeviceInfoResponse:
        """
        @summary Call DescribeDeviceInfo to query device-related information, such as the validity period of authorization, business identifiers customized by the access party, and device ID, etc.
        
        @description Request Method: Supports sending requests using HTTPS POST and GET methods.
        
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
        @summary Call DescribeDeviceInfo to query device-related information, such as the validity period of authorization, business identifiers customized by the access party, and device ID, etc.
        
        @description Request Method: Supports sending requests using HTTPS POST and GET methods.
        
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
        @summary Call DescribeDeviceInfo to query device-related information, such as the validity period of authorization, business identifiers customized by the access party, and device ID, etc.
        
        @description Request Method: Supports sending requests using HTTPS POST and GET methods.
        
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
        @summary Call DescribeDeviceInfo to query device-related information, such as the validity period of authorization, business identifiers customized by the access party, and device ID, etc.
        
        @description Request Method: Supports sending requests using HTTPS POST and GET methods.
        
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
        @summary Financial-Grade Face Guard Service
        
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
        @summary Financial-Grade Face Guard Service
        
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
        @summary Financial-Grade Face Guard Service
        
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
        @summary Financial-Grade Face Guard Service
        
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
        @summary After the mobile end of the integrator receives the callback, its server can call this interface to obtain the corresponding authentication status and authentication information.
        
        @description - Service Address: cloudauth.aliyuncs.com.
        - Request Method: HTTPS POST and GET.
        
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
        @summary After the mobile end of the integrator receives the callback, its server can call this interface to obtain the corresponding authentication status and authentication information.
        
        @description - Service Address: cloudauth.aliyuncs.com.
        - Request Method: HTTPS POST and GET.
        
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
        @summary After the mobile end of the integrator receives the callback, its server can call this interface to obtain the corresponding authentication status and authentication information.
        
        @description - Service Address: cloudauth.aliyuncs.com.
        - Request Method: HTTPS POST and GET.
        
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
        @summary After the mobile end of the integrator receives the callback, its server can call this interface to obtain the corresponding authentication status and authentication information.
        
        @description - Service Address: cloudauth.aliyuncs.com.
        - Request Method: HTTPS POST and GET.
        
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
        @summary Call DescribeOssUploadToken to get the Token required for uploading photos to OSS.
        
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
        @summary Call DescribeOssUploadToken to get the Token required for uploading photos to OSS.
        
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
        @summary Call DescribeOssUploadToken to get the Token required for uploading photos to OSS.
        
        @return: DescribeOssUploadTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_upload_token_with_options(runtime)

    async def describe_oss_upload_token_async(self) -> cloudauth_20190307_models.DescribeOssUploadTokenResponse:
        """
        @summary Call DescribeOssUploadToken to get the Token required for uploading photos to OSS.
        
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
        @summary Open API adds financial-grade data statistics API
        
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
        @summary Open API adds financial-grade data statistics API
        
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
        @summary Open API adds financial-grade data statistics API
        
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
        @summary Open API adds financial-grade data statistics API
        
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
        @summary Enhanced Real Person Authentication Call Statistics Pagination Query Interface
        
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
        @summary Enhanced Real Person Authentication Call Statistics Pagination Query Interface
        
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
        @summary Enhanced Real Person Authentication Call Statistics Pagination Query Interface
        
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
        @summary Enhanced Real Person Authentication Call Statistics Pagination Query Interface
        
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
        @summary Query the result of real-person authentication.
        
        @description Prerequisites: Before accessing this API, please ensure that you have completed the necessary preparations. For more details, see [Real Person Authentication Server-side Preparation](https://help.aliyun.com/document_detail/127471.html) and [Liveness Face Verification Server-side Preparation](https://help.aliyun.com/document_detail/127717.html).
        > Alibaba Cloud Real Person Authentication only stores authentication data for the last 180 days. For any subsequent business use, please call this interface in a timely manner to retrieve and store the data yourself to avoid any impact on usage.
        Request Method: HTTPS POST and GET.
        Interface Description: After the mobile end of the access party receives the callback, its server can call this interface to obtain the corresponding authentication status and authentication information.
        Applicable Scope: This interface is applicable to the authentication solution with SDK + server-side integration.
        
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
        @summary Query the result of real-person authentication.
        
        @description Prerequisites: Before accessing this API, please ensure that you have completed the necessary preparations. For more details, see [Real Person Authentication Server-side Preparation](https://help.aliyun.com/document_detail/127471.html) and [Liveness Face Verification Server-side Preparation](https://help.aliyun.com/document_detail/127717.html).
        > Alibaba Cloud Real Person Authentication only stores authentication data for the last 180 days. For any subsequent business use, please call this interface in a timely manner to retrieve and store the data yourself to avoid any impact on usage.
        Request Method: HTTPS POST and GET.
        Interface Description: After the mobile end of the access party receives the callback, its server can call this interface to obtain the corresponding authentication status and authentication information.
        Applicable Scope: This interface is applicable to the authentication solution with SDK + server-side integration.
        
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
        @summary Query the result of real-person authentication.
        
        @description Prerequisites: Before accessing this API, please ensure that you have completed the necessary preparations. For more details, see [Real Person Authentication Server-side Preparation](https://help.aliyun.com/document_detail/127471.html) and [Liveness Face Verification Server-side Preparation](https://help.aliyun.com/document_detail/127717.html).
        > Alibaba Cloud Real Person Authentication only stores authentication data for the last 180 days. For any subsequent business use, please call this interface in a timely manner to retrieve and store the data yourself to avoid any impact on usage.
        Request Method: HTTPS POST and GET.
        Interface Description: After the mobile end of the access party receives the callback, its server can call this interface to obtain the corresponding authentication status and authentication information.
        Applicable Scope: This interface is applicable to the authentication solution with SDK + server-side integration.
        
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
        @summary Query the result of real-person authentication.
        
        @description Prerequisites: Before accessing this API, please ensure that you have completed the necessary preparations. For more details, see [Real Person Authentication Server-side Preparation](https://help.aliyun.com/document_detail/127471.html) and [Liveness Face Verification Server-side Preparation](https://help.aliyun.com/document_detail/127717.html).
        > Alibaba Cloud Real Person Authentication only stores authentication data for the last 180 days. For any subsequent business use, please call this interface in a timely manner to retrieve and store the data yourself to avoid any impact on usage.
        Request Method: HTTPS POST and GET.
        Interface Description: After the mobile end of the access party receives the callback, its server can call this interface to obtain the corresponding authentication status and authentication information.
        Applicable Scope: This interface is applicable to the authentication solution with SDK + server-side integration.
        
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
        @summary Call DescribeVerifySDK to get the offline SDK download address.
        
        @description Request Method: Supports sending requests via HTTPS POST and GET methods.
        Interface Description: Obtain the SDK generation result based on the task ID for generating an offline facial recognition SDK.
        
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
        @summary Call DescribeVerifySDK to get the offline SDK download address.
        
        @description Request Method: Supports sending requests via HTTPS POST and GET methods.
        Interface Description: Obtain the SDK generation result based on the task ID for generating an offline facial recognition SDK.
        
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
        @summary Call DescribeVerifySDK to get the offline SDK download address.
        
        @description Request Method: Supports sending requests via HTTPS POST and GET methods.
        Interface Description: Obtain the SDK generation result based on the task ID for generating an offline facial recognition SDK.
        
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
        @summary Call DescribeVerifySDK to get the offline SDK download address.
        
        @description Request Method: Supports sending requests via HTTPS POST and GET methods.
        Interface Description: Obtain the SDK generation result based on the task ID for generating an offline facial recognition SDK.
        
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
        @summary Call DescribeVerifyToken to initiate an authentication request and obtain an authentication Token. This interface is suitable for authentication solutions using SDK + server-side integration.
        
        @description Preparation for Access: When integrating this API, please ensure that the corresponding preparations have been completed. For details, see [Overview of Real Person Authentication Solution Integration Process](https://help.aliyun.com/document_detail/127536.html) and [Overview of Live Face Verification Solution (Liveness Detection Solution) Integration Process](https://help.aliyun.com/document_detail/127687.html).
        Request Method: HTTPS POST and GET
        API Description: Before each authentication, use this interface to obtain an authentication Token (VerifyToken), which is used to link various interfaces in the authentication request.
        Applicable Scope: This interface is suitable for wireless SDK integration.
        Image Address: Use HTTP or HTTPS addresses that are publicly accessible over the Internet. For example, `http://image-demo.img-cn-hangzhou.aliyuncs.com/example.jpg`.
        Image Restrictions:
        - Relative or absolute paths of local images are not supported.
        - The size of a single image should be controlled within 2 MB to avoid algorithm retrieval timeout.
        - The face area in the image must be at least 6464 pixels (px).
        - There is an 8 MB size limit for the Body of a single request. Please calculate the total size of all images and other information in the request to ensure it does not exceed the limit.
        
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
        @summary Call DescribeVerifyToken to initiate an authentication request and obtain an authentication Token. This interface is suitable for authentication solutions using SDK + server-side integration.
        
        @description Preparation for Access: When integrating this API, please ensure that the corresponding preparations have been completed. For details, see [Overview of Real Person Authentication Solution Integration Process](https://help.aliyun.com/document_detail/127536.html) and [Overview of Live Face Verification Solution (Liveness Detection Solution) Integration Process](https://help.aliyun.com/document_detail/127687.html).
        Request Method: HTTPS POST and GET
        API Description: Before each authentication, use this interface to obtain an authentication Token (VerifyToken), which is used to link various interfaces in the authentication request.
        Applicable Scope: This interface is suitable for wireless SDK integration.
        Image Address: Use HTTP or HTTPS addresses that are publicly accessible over the Internet. For example, `http://image-demo.img-cn-hangzhou.aliyuncs.com/example.jpg`.
        Image Restrictions:
        - Relative or absolute paths of local images are not supported.
        - The size of a single image should be controlled within 2 MB to avoid algorithm retrieval timeout.
        - The face area in the image must be at least 6464 pixels (px).
        - There is an 8 MB size limit for the Body of a single request. Please calculate the total size of all images and other information in the request to ensure it does not exceed the limit.
        
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
        @summary Call DescribeVerifyToken to initiate an authentication request and obtain an authentication Token. This interface is suitable for authentication solutions using SDK + server-side integration.
        
        @description Preparation for Access: When integrating this API, please ensure that the corresponding preparations have been completed. For details, see [Overview of Real Person Authentication Solution Integration Process](https://help.aliyun.com/document_detail/127536.html) and [Overview of Live Face Verification Solution (Liveness Detection Solution) Integration Process](https://help.aliyun.com/document_detail/127687.html).
        Request Method: HTTPS POST and GET
        API Description: Before each authentication, use this interface to obtain an authentication Token (VerifyToken), which is used to link various interfaces in the authentication request.
        Applicable Scope: This interface is suitable for wireless SDK integration.
        Image Address: Use HTTP or HTTPS addresses that are publicly accessible over the Internet. For example, `http://image-demo.img-cn-hangzhou.aliyuncs.com/example.jpg`.
        Image Restrictions:
        - Relative or absolute paths of local images are not supported.
        - The size of a single image should be controlled within 2 MB to avoid algorithm retrieval timeout.
        - The face area in the image must be at least 6464 pixels (px).
        - There is an 8 MB size limit for the Body of a single request. Please calculate the total size of all images and other information in the request to ensure it does not exceed the limit.
        
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
        @summary Call DescribeVerifyToken to initiate an authentication request and obtain an authentication Token. This interface is suitable for authentication solutions using SDK + server-side integration.
        
        @description Preparation for Access: When integrating this API, please ensure that the corresponding preparations have been completed. For details, see [Overview of Real Person Authentication Solution Integration Process](https://help.aliyun.com/document_detail/127536.html) and [Overview of Live Face Verification Solution (Liveness Detection Solution) Integration Process](https://help.aliyun.com/document_detail/127687.html).
        Request Method: HTTPS POST and GET
        API Description: Before each authentication, use this interface to obtain an authentication Token (VerifyToken), which is used to link various interfaces in the authentication request.
        Applicable Scope: This interface is suitable for wireless SDK integration.
        Image Address: Use HTTP or HTTPS addresses that are publicly accessible over the Internet. For example, `http://image-demo.img-cn-hangzhou.aliyuncs.com/example.jpg`.
        Image Restrictions:
        - Relative or absolute paths of local images are not supported.
        - The size of a single image should be controlled within 2 MB to avoid algorithm retrieval timeout.
        - The face area in the image must be at least 6464 pixels (px).
        - There is an 8 MB size limit for the Body of a single request. Please calculate the total size of all images and other information in the request to ensure it does not exceed the limit.
        
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
        @summary Detect Validity Attributes in Face Photos
        
        @description Request Method: Only supports sending requests via HTTPS POST.
        Interface Description: Detects the validity-related attributes of faces in the input photo, which helps the business side to determine whether the photo meets their own business retention or comparison requirements. The currently supported face validity-related attributes include: whether it is a face, whether it is blurry, whether glasses are worn, face pose, whether it is a smile, etc.
        Instructions for Uploading Image Addresses: When passing in images, you need to upload their corresponding HTTP, OSS addresses, or Base64 encoding.
        - HTTP Address: A publicly accessible HTTP address. For example, `http://image-demo.img-cn-hangzhou.aliyuncs.com/example.jpg`.
        - Base64 Encoding: An image encoded through base64, with the format being `base64://<image base64 string>`.
        Image Limitations:
        - Does not support relative or absolute paths of local images.
        - Please keep the size of a single image within 2 MB to avoid algorithm timeout.
        - There is an 8 MB size limit for the Body of a single request; please calculate the total size of all images and other information in the request and do not exceed the limit.
        - When using Base64 to pass images, the request method needs to be changed to POST; the header description of the image Base64 string, such as `data:image/png;base64`, should be removed.
        
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
        @summary Detect Validity Attributes in Face Photos
        
        @description Request Method: Only supports sending requests via HTTPS POST.
        Interface Description: Detects the validity-related attributes of faces in the input photo, which helps the business side to determine whether the photo meets their own business retention or comparison requirements. The currently supported face validity-related attributes include: whether it is a face, whether it is blurry, whether glasses are worn, face pose, whether it is a smile, etc.
        Instructions for Uploading Image Addresses: When passing in images, you need to upload their corresponding HTTP, OSS addresses, or Base64 encoding.
        - HTTP Address: A publicly accessible HTTP address. For example, `http://image-demo.img-cn-hangzhou.aliyuncs.com/example.jpg`.
        - Base64 Encoding: An image encoded through base64, with the format being `base64://<image base64 string>`.
        Image Limitations:
        - Does not support relative or absolute paths of local images.
        - Please keep the size of a single image within 2 MB to avoid algorithm timeout.
        - There is an 8 MB size limit for the Body of a single request; please calculate the total size of all images and other information in the request and do not exceed the limit.
        - When using Base64 to pass images, the request method needs to be changed to POST; the header description of the image Base64 string, such as `data:image/png;base64`, should be removed.
        
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
        @summary Detect Validity Attributes in Face Photos
        
        @description Request Method: Only supports sending requests via HTTPS POST.
        Interface Description: Detects the validity-related attributes of faces in the input photo, which helps the business side to determine whether the photo meets their own business retention or comparison requirements. The currently supported face validity-related attributes include: whether it is a face, whether it is blurry, whether glasses are worn, face pose, whether it is a smile, etc.
        Instructions for Uploading Image Addresses: When passing in images, you need to upload their corresponding HTTP, OSS addresses, or Base64 encoding.
        - HTTP Address: A publicly accessible HTTP address. For example, `http://image-demo.img-cn-hangzhou.aliyuncs.com/example.jpg`.
        - Base64 Encoding: An image encoded through base64, with the format being `base64://<image base64 string>`.
        Image Limitations:
        - Does not support relative or absolute paths of local images.
        - Please keep the size of a single image within 2 MB to avoid algorithm timeout.
        - There is an 8 MB size limit for the Body of a single request; please calculate the total size of all images and other information in the request and do not exceed the limit.
        - When using Base64 to pass images, the request method needs to be changed to POST; the header description of the image Base64 string, such as `data:image/png;base64`, should be removed.
        
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
        @summary Detect Validity Attributes in Face Photos
        
        @description Request Method: Only supports sending requests via HTTPS POST.
        Interface Description: Detects the validity-related attributes of faces in the input photo, which helps the business side to determine whether the photo meets their own business retention or comparison requirements. The currently supported face validity-related attributes include: whether it is a face, whether it is blurry, whether glasses are worn, face pose, whether it is a smile, etc.
        Instructions for Uploading Image Addresses: When passing in images, you need to upload their corresponding HTTP, OSS addresses, or Base64 encoding.
        - HTTP Address: A publicly accessible HTTP address. For example, `http://image-demo.img-cn-hangzhou.aliyuncs.com/example.jpg`.
        - Base64 Encoding: An image encoded through base64, with the format being `base64://<image base64 string>`.
        Image Limitations:
        - Does not support relative or absolute paths of local images.
        - Please keep the size of a single image within 2 MB to avoid algorithm timeout.
        - There is an 8 MB size limit for the Body of a single request; please calculate the total size of all images and other information in the request and do not exceed the limit.
        - When using Base64 to pass images, the request method needs to be changed to POST; the header description of the image Base64 string, such as `data:image/png;base64`, should be removed.
        
        @param request: DetectFaceAttributesRequest
        @return: DetectFaceAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_face_attributes_with_options_async(request, runtime)

    def id_2meta_period_verify_with_options(
        self,
        request: cloudauth_20190307_models.Id2MetaPeriodVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Id2MetaPeriodVerifyResponse:
        """
        @summary Two-Factor Validity Verification API
        
        @param request: Id2MetaPeriodVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Id2MetaPeriodVerifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.validity_end_date):
            body['ValidityEndDate'] = request.validity_end_date
        if not UtilClient.is_unset(request.validity_start_date):
            body['ValidityStartDate'] = request.validity_start_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Id2MetaPeriodVerify',
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
            cloudauth_20190307_models.Id2MetaPeriodVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def id_2meta_period_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.Id2MetaPeriodVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Id2MetaPeriodVerifyResponse:
        """
        @summary Two-Factor Validity Verification API
        
        @param request: Id2MetaPeriodVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Id2MetaPeriodVerifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.identify_num):
            body['IdentifyNum'] = request.identify_num
        if not UtilClient.is_unset(request.param_type):
            body['ParamType'] = request.param_type
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.validity_end_date):
            body['ValidityEndDate'] = request.validity_end_date
        if not UtilClient.is_unset(request.validity_start_date):
            body['ValidityStartDate'] = request.validity_start_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Id2MetaPeriodVerify',
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
            cloudauth_20190307_models.Id2MetaPeriodVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def id_2meta_period_verify(
        self,
        request: cloudauth_20190307_models.Id2MetaPeriodVerifyRequest,
    ) -> cloudauth_20190307_models.Id2MetaPeriodVerifyResponse:
        """
        @summary Two-Factor Validity Verification API
        
        @param request: Id2MetaPeriodVerifyRequest
        @return: Id2MetaPeriodVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.id_2meta_period_verify_with_options(request, runtime)

    async def id_2meta_period_verify_async(
        self,
        request: cloudauth_20190307_models.Id2MetaPeriodVerifyRequest,
    ) -> cloudauth_20190307_models.Id2MetaPeriodVerifyResponse:
        """
        @summary Two-Factor Validity Verification API
        
        @param request: Id2MetaPeriodVerifyRequest
        @return: Id2MetaPeriodVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.id_2meta_period_verify_with_options_async(request, runtime)

    def id_2meta_standard_verify_with_options(
        self,
        request: cloudauth_20190307_models.Id2MetaStandardVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Id2MetaStandardVerifyResponse:
        """
        @summary Identity Two-Factor Standard
        
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
        @summary Identity Two-Factor Standard
        
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
        @summary Identity Two-Factor Standard
        
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
        @summary Identity Two-Factor Standard
        
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
        @summary Identity Two-Factor Interface
        
        @description - Service address: cloudauth.aliyuncs.com (IPv4) or cloudauth-dualstack.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Identity Two-Factor Interface
        
        @description - Service address: cloudauth.aliyuncs.com (IPv4) or cloudauth-dualstack.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Identity Two-Factor Interface
        
        @description - Service address: cloudauth.aliyuncs.com (IPv4) or cloudauth-dualstack.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Identity Two-Factor Interface
        
        @description - Service address: cloudauth.aliyuncs.com (IPv4) or cloudauth-dualstack.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
        @param request: Id2MetaVerifyRequest
        @return: Id2MetaVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.id_2meta_verify_with_options_async(request, runtime)

    def id_2meta_verify_with_ocrwith_options(
        self,
        request: cloudauth_20190307_models.Id2MetaVerifyWithOCRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Id2MetaVerifyWithOCRResponse:
        """
        @summary ID Two-Factor Image Verification
        
        @description Upload both sides of the ID card, and get the verification result of the two factors from an authoritative data source.
        
        @param request: Id2MetaVerifyWithOCRRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Id2MetaVerifyWithOCRResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_file):
            body['CertFile'] = request.cert_file
        if not UtilClient.is_unset(request.cert_national_file):
            body['CertNationalFile'] = request.cert_national_file
        if not UtilClient.is_unset(request.cert_national_url):
            body['CertNationalUrl'] = request.cert_national_url
        if not UtilClient.is_unset(request.cert_url):
            body['CertUrl'] = request.cert_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Id2MetaVerifyWithOCR',
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
            cloudauth_20190307_models.Id2MetaVerifyWithOCRResponse(),
            self.call_api(params, req, runtime)
        )

    async def id_2meta_verify_with_ocrwith_options_async(
        self,
        request: cloudauth_20190307_models.Id2MetaVerifyWithOCRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Id2MetaVerifyWithOCRResponse:
        """
        @summary ID Two-Factor Image Verification
        
        @description Upload both sides of the ID card, and get the verification result of the two factors from an authoritative data source.
        
        @param request: Id2MetaVerifyWithOCRRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Id2MetaVerifyWithOCRResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_file):
            body['CertFile'] = request.cert_file
        if not UtilClient.is_unset(request.cert_national_file):
            body['CertNationalFile'] = request.cert_national_file
        if not UtilClient.is_unset(request.cert_national_url):
            body['CertNationalUrl'] = request.cert_national_url
        if not UtilClient.is_unset(request.cert_url):
            body['CertUrl'] = request.cert_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Id2MetaVerifyWithOCR',
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
            cloudauth_20190307_models.Id2MetaVerifyWithOCRResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def id_2meta_verify_with_ocr(
        self,
        request: cloudauth_20190307_models.Id2MetaVerifyWithOCRRequest,
    ) -> cloudauth_20190307_models.Id2MetaVerifyWithOCRResponse:
        """
        @summary ID Two-Factor Image Verification
        
        @description Upload both sides of the ID card, and get the verification result of the two factors from an authoritative data source.
        
        @param request: Id2MetaVerifyWithOCRRequest
        @return: Id2MetaVerifyWithOCRResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.id_2meta_verify_with_ocrwith_options(request, runtime)

    async def id_2meta_verify_with_ocr_async(
        self,
        request: cloudauth_20190307_models.Id2MetaVerifyWithOCRRequest,
    ) -> cloudauth_20190307_models.Id2MetaVerifyWithOCRResponse:
        """
        @summary ID Two-Factor Image Verification
        
        @description Upload both sides of the ID card, and get the verification result of the two factors from an authoritative data source.
        
        @param request: Id2MetaVerifyWithOCRRequest
        @return: Id2MetaVerifyWithOCRResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.id_2meta_verify_with_ocrwith_options_async(request, runtime)

    def id_2meta_verify_with_ocradvance(
        self,
        request: cloudauth_20190307_models.Id2MetaVerifyWithOCRAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Id2MetaVerifyWithOCRResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
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
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Cloudauth',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        id_2meta_verify_with_ocrreq = cloudauth_20190307_models.Id2MetaVerifyWithOCRRequest()
        OpenApiUtilClient.convert(request, id_2meta_verify_with_ocrreq)
        if not UtilClient.is_unset(request.cert_file_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.cert_file_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            id_2meta_verify_with_ocrreq.cert_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.cert_national_file_object):
            tmp_resp_1 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.cert_national_file_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            id_2meta_verify_with_ocrreq.cert_national_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        id_2meta_verify_with_ocrresp = self.id_2meta_verify_with_ocrwith_options(id_2meta_verify_with_ocrreq, runtime)
        return id_2meta_verify_with_ocrresp

    async def id_2meta_verify_with_ocradvance_async(
        self,
        request: cloudauth_20190307_models.Id2MetaVerifyWithOCRAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Id2MetaVerifyWithOCRResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
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
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Cloudauth',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        id_2meta_verify_with_ocrreq = cloudauth_20190307_models.Id2MetaVerifyWithOCRRequest()
        OpenApiUtilClient.convert(request, id_2meta_verify_with_ocrreq)
        if not UtilClient.is_unset(request.cert_file_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.cert_file_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            id_2meta_verify_with_ocrreq.cert_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        if not UtilClient.is_unset(request.cert_national_file_object):
            tmp_resp_1 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_1)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.cert_national_file_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            id_2meta_verify_with_ocrreq.cert_national_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        id_2meta_verify_with_ocrresp = await self.id_2meta_verify_with_ocrwith_options_async(id_2meta_verify_with_ocrreq, runtime)
        return id_2meta_verify_with_ocrresp

    def id_3meta_verify_with_options(
        self,
        request: cloudauth_20190307_models.Id3MetaVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Id3MetaVerifyResponse:
        """
        @summary Identity Three Elements Verification
        
        @description Input name, ID number, and face photo to verify their authenticity and consistency through authoritative sources.
        
        @param request: Id3MetaVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Id3MetaVerifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.face_file):
            body['FaceFile'] = request.face_file
        if not UtilClient.is_unset(request.face_url):
            body['FaceUrl'] = request.face_url
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
            action='Id3MetaVerify',
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
            cloudauth_20190307_models.Id3MetaVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def id_3meta_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.Id3MetaVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Id3MetaVerifyResponse:
        """
        @summary Identity Three Elements Verification
        
        @description Input name, ID number, and face photo to verify their authenticity and consistency through authoritative sources.
        
        @param request: Id3MetaVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Id3MetaVerifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.crop):
            body['Crop'] = request.crop
        if not UtilClient.is_unset(request.face_file):
            body['FaceFile'] = request.face_file
        if not UtilClient.is_unset(request.face_url):
            body['FaceUrl'] = request.face_url
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
            action='Id3MetaVerify',
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
            cloudauth_20190307_models.Id3MetaVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def id_3meta_verify(
        self,
        request: cloudauth_20190307_models.Id3MetaVerifyRequest,
    ) -> cloudauth_20190307_models.Id3MetaVerifyResponse:
        """
        @summary Identity Three Elements Verification
        
        @description Input name, ID number, and face photo to verify their authenticity and consistency through authoritative sources.
        
        @param request: Id3MetaVerifyRequest
        @return: Id3MetaVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.id_3meta_verify_with_options(request, runtime)

    async def id_3meta_verify_async(
        self,
        request: cloudauth_20190307_models.Id3MetaVerifyRequest,
    ) -> cloudauth_20190307_models.Id3MetaVerifyResponse:
        """
        @summary Identity Three Elements Verification
        
        @description Input name, ID number, and face photo to verify their authenticity and consistency through authoritative sources.
        
        @param request: Id3MetaVerifyRequest
        @return: Id3MetaVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.id_3meta_verify_with_options_async(request, runtime)

    def id_3meta_verify_advance(
        self,
        request: cloudauth_20190307_models.Id3MetaVerifyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Id3MetaVerifyResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = self._credential.get_credential()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
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
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Cloudauth',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        id_3meta_verify_req = cloudauth_20190307_models.Id3MetaVerifyRequest()
        OpenApiUtilClient.convert(request, id_3meta_verify_req)
        if not UtilClient.is_unset(request.face_file_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.face_file_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            self._post_ossobject(auth_response_body.get('Bucket'), oss_header)
            id_3meta_verify_req.face_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        id_3meta_verify_resp = self.id_3meta_verify_with_options(id_3meta_verify_req, runtime)
        return id_3meta_verify_resp

    async def id_3meta_verify_advance_async(
        self,
        request: cloudauth_20190307_models.Id3MetaVerifyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Id3MetaVerifyResponse:
        # Step 0: init client
        credential_model = None
        if UtilClient.is_unset(self._credential):
            raise TeaException({
                'code': 'InvalidCredentials',
                'message': 'Please set up the credentials correctly. If you are setting them through environment variables, please ensure that ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set correctly. See https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems for more details.'
            })
        credential_model = await self._credential.get_credential_async()
        access_key_id = credential_model.access_key_id
        access_key_secret = credential_model.access_key_secret
        security_token = credential_model.security_token
        credential_type = credential_model.type
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
        auth_client = OpenApiClient(auth_config)
        auth_request = {
            'Product': 'Cloudauth',
            'RegionId': self._region_id
        }
        auth_req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(auth_request)
        )
        auth_params = open_api_models.Params(
            action='AuthorizeFileUpload',
            version='2019-12-19',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        auth_response = {}
        file_obj = file_form_models.FileField()
        oss_header = {}
        tmp_body = {}
        use_accelerate = False
        auth_response_body = {}
        id_3meta_verify_req = cloudauth_20190307_models.Id3MetaVerifyRequest()
        OpenApiUtilClient.convert(request, id_3meta_verify_req)
        if not UtilClient.is_unset(request.face_file_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.face_file_object,
                content_type=''
            )
            oss_header = {
                'host': f"{auth_response_body.get('Bucket')}.{OpenApiUtilClient.get_endpoint(auth_response_body.get('Endpoint'), use_accelerate, self._endpoint_type)}",
                'OSSAccessKeyId': auth_response_body.get('AccessKeyId'),
                'policy': auth_response_body.get('EncodedPolicy'),
                'Signature': auth_response_body.get('Signature'),
                'key': auth_response_body.get('ObjectKey'),
                'file': file_obj,
                'success_action_status': '201'
            }
            await self._post_ossobject_async(auth_response_body.get('Bucket'), oss_header)
            id_3meta_verify_req.face_file = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        id_3meta_verify_resp = await self.id_3meta_verify_with_options_async(id_3meta_verify_req, runtime)
        return id_3meta_verify_resp

    def init_card_verify_with_options(
        self,
        request: cloudauth_20190307_models.InitCardVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.InitCardVerifyResponse:
        """
        @summary Initiate an authentication request for image verification
        
        @description Before each authentication, use this interface to obtain the CertifyId, which is used to link various interfaces in the authentication request.
        
        @param request: InitCardVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitCardVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_token):
            query['CallbackToken'] = request.callback_token
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.card_page_number):
            query['CardPageNumber'] = request.card_page_number
        if not UtilClient.is_unset(request.card_type):
            query['CardType'] = request.card_type
        if not UtilClient.is_unset(request.doc_scan_mode):
            query['DocScanMode'] = request.doc_scan_mode
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.meta_info):
            query['MetaInfo'] = request.meta_info
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.picture_save):
            query['PictureSave'] = request.picture_save
        if not UtilClient.is_unset(request.verify_meta):
            query['VerifyMeta'] = request.verify_meta
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitCardVerify',
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
            cloudauth_20190307_models.InitCardVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_card_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.InitCardVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.InitCardVerifyResponse:
        """
        @summary Initiate an authentication request for image verification
        
        @description Before each authentication, use this interface to obtain the CertifyId, which is used to link various interfaces in the authentication request.
        
        @param request: InitCardVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitCardVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_token):
            query['CallbackToken'] = request.callback_token
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.card_page_number):
            query['CardPageNumber'] = request.card_page_number
        if not UtilClient.is_unset(request.card_type):
            query['CardType'] = request.card_type
        if not UtilClient.is_unset(request.doc_scan_mode):
            query['DocScanMode'] = request.doc_scan_mode
        if not UtilClient.is_unset(request.merchant_biz_id):
            query['MerchantBizId'] = request.merchant_biz_id
        if not UtilClient.is_unset(request.meta_info):
            query['MetaInfo'] = request.meta_info
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.picture_save):
            query['PictureSave'] = request.picture_save
        if not UtilClient.is_unset(request.verify_meta):
            query['VerifyMeta'] = request.verify_meta
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitCardVerify',
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
            cloudauth_20190307_models.InitCardVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_card_verify(
        self,
        request: cloudauth_20190307_models.InitCardVerifyRequest,
    ) -> cloudauth_20190307_models.InitCardVerifyResponse:
        """
        @summary Initiate an authentication request for image verification
        
        @description Before each authentication, use this interface to obtain the CertifyId, which is used to link various interfaces in the authentication request.
        
        @param request: InitCardVerifyRequest
        @return: InitCardVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.init_card_verify_with_options(request, runtime)

    async def init_card_verify_async(
        self,
        request: cloudauth_20190307_models.InitCardVerifyRequest,
    ) -> cloudauth_20190307_models.InitCardVerifyResponse:
        """
        @summary Initiate an authentication request for image verification
        
        @description Before each authentication, use this interface to obtain the CertifyId, which is used to link various interfaces in the authentication request.
        
        @param request: InitCardVerifyRequest
        @return: InitCardVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.init_card_verify_with_options_async(request, runtime)

    def init_face_verify_with_options(
        self,
        request: cloudauth_20190307_models.InitFaceVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.InitFaceVerifyResponse:
        """
        @summary Real-Person Server Initialization Interface
        
        @description - Service Address: cloudauth.aliyuncs.com
        - Request Method: HTTPS POST and GET.
        - This interface uses different parameters for different product solutions. For details, please refer to the [official documentation](https://help.aliyun.com/zh/id-verification/financial-grade-id-verification/product-overview/introduction/?spm=a2c4g.11186623.help-menu-2401581.d_0_0.13f644ecRzFHfm&scm=20140722.H_99169._.OR_help-T_cn~zh-V_1).
        #### Image Format Requirements
        When performing real-person authentication, please provide images that meet all of the following conditions:
        - Recent photo with a clear, unobstructed face, natural expression, and facing the camera directly.
        - Clear photo with normal exposure, no overexposure, underexposure, or halo effects, and no significant angle deviation.
        - Resolution not exceeding 19201080, at least 640*480, recommended short side scaled to 720 pixels, compression ratio greater than 0.9.
        - Photo size: <1MB.
        - Supports 90, 180, and 270-degree photos; in the case of multiple faces, the largest face will be selected.
        
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
        if not UtilClient.is_unset(request.camera_selection):
            query['CameraSelection'] = request.camera_selection
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
        if not UtilClient.is_unset(request.need_multi_face_check):
            query['NeedMultiFaceCheck'] = request.need_multi_face_check
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
        @summary Real-Person Server Initialization Interface
        
        @description - Service Address: cloudauth.aliyuncs.com
        - Request Method: HTTPS POST and GET.
        - This interface uses different parameters for different product solutions. For details, please refer to the [official documentation](https://help.aliyun.com/zh/id-verification/financial-grade-id-verification/product-overview/introduction/?spm=a2c4g.11186623.help-menu-2401581.d_0_0.13f644ecRzFHfm&scm=20140722.H_99169._.OR_help-T_cn~zh-V_1).
        #### Image Format Requirements
        When performing real-person authentication, please provide images that meet all of the following conditions:
        - Recent photo with a clear, unobstructed face, natural expression, and facing the camera directly.
        - Clear photo with normal exposure, no overexposure, underexposure, or halo effects, and no significant angle deviation.
        - Resolution not exceeding 19201080, at least 640*480, recommended short side scaled to 720 pixels, compression ratio greater than 0.9.
        - Photo size: <1MB.
        - Supports 90, 180, and 270-degree photos; in the case of multiple faces, the largest face will be selected.
        
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
        if not UtilClient.is_unset(request.camera_selection):
            query['CameraSelection'] = request.camera_selection
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
        if not UtilClient.is_unset(request.need_multi_face_check):
            query['NeedMultiFaceCheck'] = request.need_multi_face_check
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
        @summary Real-Person Server Initialization Interface
        
        @description - Service Address: cloudauth.aliyuncs.com
        - Request Method: HTTPS POST and GET.
        - This interface uses different parameters for different product solutions. For details, please refer to the [official documentation](https://help.aliyun.com/zh/id-verification/financial-grade-id-verification/product-overview/introduction/?spm=a2c4g.11186623.help-menu-2401581.d_0_0.13f644ecRzFHfm&scm=20140722.H_99169._.OR_help-T_cn~zh-V_1).
        #### Image Format Requirements
        When performing real-person authentication, please provide images that meet all of the following conditions:
        - Recent photo with a clear, unobstructed face, natural expression, and facing the camera directly.
        - Clear photo with normal exposure, no overexposure, underexposure, or halo effects, and no significant angle deviation.
        - Resolution not exceeding 19201080, at least 640*480, recommended short side scaled to 720 pixels, compression ratio greater than 0.9.
        - Photo size: <1MB.
        - Supports 90, 180, and 270-degree photos; in the case of multiple faces, the largest face will be selected.
        
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
        @summary Real-Person Server Initialization Interface
        
        @description - Service Address: cloudauth.aliyuncs.com
        - Request Method: HTTPS POST and GET.
        - This interface uses different parameters for different product solutions. For details, please refer to the [official documentation](https://help.aliyun.com/zh/id-verification/financial-grade-id-verification/product-overview/introduction/?spm=a2c4g.11186623.help-menu-2401581.d_0_0.13f644ecRzFHfm&scm=20140722.H_99169._.OR_help-T_cn~zh-V_1).
        #### Image Format Requirements
        When performing real-person authentication, please provide images that meet all of the following conditions:
        - Recent photo with a clear, unobstructed face, natural expression, and facing the camera directly.
        - Clear photo with normal exposure, no overexposure, underexposure, or halo effects, and no significant angle deviation.
        - Resolution not exceeding 19201080, at least 640*480, recommended short side scaled to 720 pixels, compression ratio greater than 0.9.
        - Photo size: <1MB.
        - Supports 90, 180, and 270-degree photos; in the case of multiple faces, the largest face will be selected.
        
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
        @summary Add Real Person Whitelist
        
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
        @summary Add Real Person Whitelist
        
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
        @summary Add Real Person Whitelist
        
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
        @summary Add Real Person Whitelist
        
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
        @summary Silent Liveness Face (LivenessFaceVerify) refers to a service that performs real face detection by inputting pre-obtained face images through an API. The algorithm primarily identifies whether the face is from a screen recording, printed picture, or other types of liveness attacks. This service is suitable for low-risk business scenarios or in conjunction with offline facial recognition SDKs. If your business has higher requirements for real face security, it is recommended to integrate App or WebSDK mode, or integrate with Deepfake face detection services to assist in identifying more dimensions of face forgery risks.
        
        @description Invoke the LivenessFaceVerify interface to perform liveness detection on a face image.
        
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
        @summary Silent Liveness Face (LivenessFaceVerify) refers to a service that performs real face detection by inputting pre-obtained face images through an API. The algorithm primarily identifies whether the face is from a screen recording, printed picture, or other types of liveness attacks. This service is suitable for low-risk business scenarios or in conjunction with offline facial recognition SDKs. If your business has higher requirements for real face security, it is recommended to integrate App or WebSDK mode, or integrate with Deepfake face detection services to assist in identifying more dimensions of face forgery risks.
        
        @description Invoke the LivenessFaceVerify interface to perform liveness detection on a face image.
        
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
        @summary Silent Liveness Face (LivenessFaceVerify) refers to a service that performs real face detection by inputting pre-obtained face images through an API. The algorithm primarily identifies whether the face is from a screen recording, printed picture, or other types of liveness attacks. This service is suitable for low-risk business scenarios or in conjunction with offline facial recognition SDKs. If your business has higher requirements for real face security, it is recommended to integrate App or WebSDK mode, or integrate with Deepfake face detection services to assist in identifying more dimensions of face forgery risks.
        
        @description Invoke the LivenessFaceVerify interface to perform liveness detection on a face image.
        
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
        @summary Silent Liveness Face (LivenessFaceVerify) refers to a service that performs real face detection by inputting pre-obtained face images through an API. The algorithm primarily identifies whether the face is from a screen recording, printed picture, or other types of liveness attacks. This service is suitable for low-risk business scenarios or in conjunction with offline facial recognition SDKs. If your business has higher requirements for real face security, it is recommended to integrate App or WebSDK mode, or integrate with Deepfake face detection services to assist in identifying more dimensions of face forgery risks.
        
        @description Invoke the LivenessFaceVerify interface to perform liveness detection on a face image.
        
        @param request: LivenessFaceVerifyRequest
        @return: LivenessFaceVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.liveness_face_verify_with_options_async(request, runtime)

    def mobile_2meta_verify_with_options(
        self,
        request: cloudauth_20190307_models.Mobile2MetaVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Mobile2MetaVerifyResponse:
        """
        @summary Mobile Two-Factor Verification
        
        @description Input the phone number and name, verify their authenticity and consistency through authoritative data sources.
        
        @param request: Mobile2MetaVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Mobile2MetaVerifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
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
            action='Mobile2MetaVerify',
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
            cloudauth_20190307_models.Mobile2MetaVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_2meta_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.Mobile2MetaVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Mobile2MetaVerifyResponse:
        """
        @summary Mobile Two-Factor Verification
        
        @description Input the phone number and name, verify their authenticity and consistency through authoritative data sources.
        
        @param request: Mobile2MetaVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Mobile2MetaVerifyResponse
        """
        UtilClient.validate_model(request)
        body = {}
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
            action='Mobile2MetaVerify',
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
            cloudauth_20190307_models.Mobile2MetaVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_2meta_verify(
        self,
        request: cloudauth_20190307_models.Mobile2MetaVerifyRequest,
    ) -> cloudauth_20190307_models.Mobile2MetaVerifyResponse:
        """
        @summary Mobile Two-Factor Verification
        
        @description Input the phone number and name, verify their authenticity and consistency through authoritative data sources.
        
        @param request: Mobile2MetaVerifyRequest
        @return: Mobile2MetaVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.mobile_2meta_verify_with_options(request, runtime)

    async def mobile_2meta_verify_async(
        self,
        request: cloudauth_20190307_models.Mobile2MetaVerifyRequest,
    ) -> cloudauth_20190307_models.Mobile2MetaVerifyResponse:
        """
        @summary Mobile Two-Factor Verification
        
        @description Input the phone number and name, verify their authenticity and consistency through authoritative data sources.
        
        @param request: Mobile2MetaVerifyRequest
        @return: Mobile2MetaVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.mobile_2meta_verify_with_options_async(request, runtime)

    def mobile_3meta_detail_standard_verify_with_options(
        self,
        request: cloudauth_20190307_models.Mobile3MetaDetailStandardVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Mobile3MetaDetailStandardVerifyResponse:
        """
        @summary Detailed Three-Element Verification for Phone Number_Standard Version
        
        @description Input the phone number, name, and ID number to verify their authenticity and consistency through authoritative data sources. If they do not match, the reason for the mismatch is returned.
        
        @param request: Mobile3MetaDetailStandardVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Mobile3MetaDetailStandardVerifyResponse
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
            action='Mobile3MetaDetailStandardVerify',
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
            cloudauth_20190307_models.Mobile3MetaDetailStandardVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_3meta_detail_standard_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.Mobile3MetaDetailStandardVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Mobile3MetaDetailStandardVerifyResponse:
        """
        @summary Detailed Three-Element Verification for Phone Number_Standard Version
        
        @description Input the phone number, name, and ID number to verify their authenticity and consistency through authoritative data sources. If they do not match, the reason for the mismatch is returned.
        
        @param request: Mobile3MetaDetailStandardVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Mobile3MetaDetailStandardVerifyResponse
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
            action='Mobile3MetaDetailStandardVerify',
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
            cloudauth_20190307_models.Mobile3MetaDetailStandardVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_3meta_detail_standard_verify(
        self,
        request: cloudauth_20190307_models.Mobile3MetaDetailStandardVerifyRequest,
    ) -> cloudauth_20190307_models.Mobile3MetaDetailStandardVerifyResponse:
        """
        @summary Detailed Three-Element Verification for Phone Number_Standard Version
        
        @description Input the phone number, name, and ID number to verify their authenticity and consistency through authoritative data sources. If they do not match, the reason for the mismatch is returned.
        
        @param request: Mobile3MetaDetailStandardVerifyRequest
        @return: Mobile3MetaDetailStandardVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.mobile_3meta_detail_standard_verify_with_options(request, runtime)

    async def mobile_3meta_detail_standard_verify_async(
        self,
        request: cloudauth_20190307_models.Mobile3MetaDetailStandardVerifyRequest,
    ) -> cloudauth_20190307_models.Mobile3MetaDetailStandardVerifyResponse:
        """
        @summary Detailed Three-Element Verification for Phone Number_Standard Version
        
        @description Input the phone number, name, and ID number to verify their authenticity and consistency through authoritative data sources. If they do not match, the reason for the mismatch is returned.
        
        @param request: Mobile3MetaDetailStandardVerifyRequest
        @return: Mobile3MetaDetailStandardVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.mobile_3meta_detail_standard_verify_with_options_async(request, runtime)

    def mobile_3meta_detail_verify_with_options(
        self,
        request: cloudauth_20190307_models.Mobile3MetaDetailVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Mobile3MetaDetailVerifyResponse:
        """
        @summary Detailed Mobile Three-Element Verification Interface
        
        @description - Service address: cloudauth.aliyuncs.com (IPv4) or cloudauth-dualstack.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Detailed Mobile Three-Element Verification Interface
        
        @description - Service address: cloudauth.aliyuncs.com (IPv4) or cloudauth-dualstack.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Detailed Mobile Three-Element Verification Interface
        
        @description - Service address: cloudauth.aliyuncs.com (IPv4) or cloudauth-dualstack.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Detailed Mobile Three-Element Verification Interface
        
        @description - Service address: cloudauth.aliyuncs.com (IPv4) or cloudauth-dualstack.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
        @param request: Mobile3MetaDetailVerifyRequest
        @return: Mobile3MetaDetailVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.mobile_3meta_detail_verify_with_options_async(request, runtime)

    def mobile_3meta_simple_standard_verify_with_options(
        self,
        request: cloudauth_20190307_models.Mobile3MetaSimpleStandardVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Mobile3MetaSimpleStandardVerifyResponse:
        """
        @summary Simplified Three-Element Verification for Phone Number_Standard Version
        
        @description Input the phone number, name, and ID number to verify their authenticity and consistency through authoritative data sources.
        
        @param request: Mobile3MetaSimpleStandardVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Mobile3MetaSimpleStandardVerifyResponse
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
            action='Mobile3MetaSimpleStandardVerify',
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
            cloudauth_20190307_models.Mobile3MetaSimpleStandardVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def mobile_3meta_simple_standard_verify_with_options_async(
        self,
        request: cloudauth_20190307_models.Mobile3MetaSimpleStandardVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Mobile3MetaSimpleStandardVerifyResponse:
        """
        @summary Simplified Three-Element Verification for Phone Number_Standard Version
        
        @description Input the phone number, name, and ID number to verify their authenticity and consistency through authoritative data sources.
        
        @param request: Mobile3MetaSimpleStandardVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: Mobile3MetaSimpleStandardVerifyResponse
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
            action='Mobile3MetaSimpleStandardVerify',
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
            cloudauth_20190307_models.Mobile3MetaSimpleStandardVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mobile_3meta_simple_standard_verify(
        self,
        request: cloudauth_20190307_models.Mobile3MetaSimpleStandardVerifyRequest,
    ) -> cloudauth_20190307_models.Mobile3MetaSimpleStandardVerifyResponse:
        """
        @summary Simplified Three-Element Verification for Phone Number_Standard Version
        
        @description Input the phone number, name, and ID number to verify their authenticity and consistency through authoritative data sources.
        
        @param request: Mobile3MetaSimpleStandardVerifyRequest
        @return: Mobile3MetaSimpleStandardVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.mobile_3meta_simple_standard_verify_with_options(request, runtime)

    async def mobile_3meta_simple_standard_verify_async(
        self,
        request: cloudauth_20190307_models.Mobile3MetaSimpleStandardVerifyRequest,
    ) -> cloudauth_20190307_models.Mobile3MetaSimpleStandardVerifyResponse:
        """
        @summary Simplified Three-Element Verification for Phone Number_Standard Version
        
        @description Input the phone number, name, and ID number to verify their authenticity and consistency through authoritative data sources.
        
        @param request: Mobile3MetaSimpleStandardVerifyRequest
        @return: Mobile3MetaSimpleStandardVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.mobile_3meta_simple_standard_verify_with_options_async(request, runtime)

    def mobile_3meta_simple_verify_with_options(
        self,
        request: cloudauth_20190307_models.Mobile3MetaSimpleVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20190307_models.Mobile3MetaSimpleVerifyResponse:
        """
        @summary Mobile Three Elements Simplified Interface
        
        @description - Service address: cloudauth.aliyuncs.com (IPv4) or cloudauth-dualstack.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Mobile Three Elements Simplified Interface
        
        @description - Service address: cloudauth.aliyuncs.com (IPv4) or cloudauth-dualstack.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Mobile Three Elements Simplified Interface
        
        @description - Service address: cloudauth.aliyuncs.com (IPv4) or cloudauth-dualstack.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Mobile Three Elements Simplified Interface
        
        @description - Service address: cloudauth.aliyuncs.com (IPv4) or cloudauth-dualstack.aliyuncs.com (IPv6).
        - Request method: POST and GET.
        - Transfer protocol: HTTPS.
        
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
        @summary Number Detection
        
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
        @summary Number Detection
        
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
        @summary Number Detection
        
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
        @summary Number Detection
        
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
        @summary Query the online status of a mobile number
        
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
        @summary Query the online status of a mobile number
        
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
        @summary Query the online status of a mobile number
        
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
        @summary Query the online status of a mobile number
        
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
        @summary Query the online duration of a mobile number
        
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
        @summary Query the online duration of a mobile number
        
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
        @summary Query the online duration of a mobile number
        
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
        @summary Query the online duration of a mobile number
        
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
        @summary Call ModifyDeviceInfo to update device-related information, such as extending the device authorization validity period, updating the business party\\"s custom business identifier, and device ID. Suitable for scenarios like renewing the device validity period.
        
        @description Request Method: Supports sending requests using HTTPS POST and GET methods.
        
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
        @summary Call ModifyDeviceInfo to update device-related information, such as extending the device authorization validity period, updating the business party\\"s custom business identifier, and device ID. Suitable for scenarios like renewing the device validity period.
        
        @description Request Method: Supports sending requests using HTTPS POST and GET methods.
        
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
        @summary Call ModifyDeviceInfo to update device-related information, such as extending the device authorization validity period, updating the business party\\"s custom business identifier, and device ID. Suitable for scenarios like renewing the device validity period.
        
        @description Request Method: Supports sending requests using HTTPS POST and GET methods.
        
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
        @summary Call ModifyDeviceInfo to update device-related information, such as extending the device authorization validity period, updating the business party\\"s custom business identifier, and device ID. Suitable for scenarios like renewing the device validity period.
        
        @description Request Method: Supports sending requests using HTTPS POST and GET methods.
        
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
        @summary Paging Query for Real Person Whitelist Configuration
        
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
        @summary Paging Query for Real Person Whitelist Configuration
        
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
        @summary Paging Query for Real Person Whitelist Configuration
        
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
        @summary Paging Query for Real Person Whitelist Configuration
        
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
        @summary Delete Real Person Whitelist
        
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
        @summary Delete Real Person Whitelist
        
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
        @summary Delete Real Person Whitelist
        
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
        @summary Delete Real Person Whitelist
        
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
        @summary Five-Item Vehicle Information Recognition
        
        @description Query basic vehicle information through the license plate number and vehicle type.
        
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
        @summary Five-Item Vehicle Information Recognition
        
        @description Query basic vehicle information through the license plate number and vehicle type.
        
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
        @summary Five-Item Vehicle Information Recognition
        
        @description Query basic vehicle information through the license plate number and vehicle type.
        
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
        @summary Five-Item Vehicle Information Recognition
        
        @description Query basic vehicle information through the license plate number and vehicle type.
        
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
        @summary Vehicle Insurance Date Inquiry
        
        @description Query the vehicle insurance date through the license plate number, vehicle type, and vehicle identification number (VIN).
        
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
        @summary Vehicle Insurance Date Inquiry
        
        @description Query the vehicle insurance date through the license plate number, vehicle type, and vehicle identification number (VIN).
        
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
        @summary Vehicle Insurance Date Inquiry
        
        @description Query the vehicle insurance date through the license plate number, vehicle type, and vehicle identification number (VIN).
        
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
        @summary Vehicle Insurance Date Inquiry
        
        @description Query the vehicle insurance date through the license plate number, vehicle type, and vehicle identification number (VIN).
        
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
        @summary Vehicle Element Verification
        
        @description Verifies the consistency of name, ID number, vehicle license plate, and vehicle type.
        
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
        @summary Vehicle Element Verification
        
        @description Verifies the consistency of name, ID number, vehicle license plate, and vehicle type.
        
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
        @summary Vehicle Element Verification
        
        @description Verifies the consistency of name, ID number, vehicle license plate, and vehicle type.
        
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
        @summary Vehicle Element Verification
        
        @description Verifies the consistency of name, ID number, vehicle license plate, and vehicle type.
        
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
        @summary Enhanced Vehicle Element Verification
        
        @description Verifies the consistency of name, ID number, license plate number, and vehicle type, and supports returning detailed vehicle information.
        
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
        @summary Enhanced Vehicle Element Verification
        
        @description Verifies the consistency of name, ID number, license plate number, and vehicle type, and supports returning detailed vehicle information.
        
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
        @summary Enhanced Vehicle Element Verification
        
        @description Verifies the consistency of name, ID number, license plate number, and vehicle type, and supports returning detailed vehicle information.
        
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
        @summary Enhanced Vehicle Element Verification
        
        @description Verifies the consistency of name, ID number, license plate number, and vehicle type, and supports returning detailed vehicle information.
        
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
        @summary Vehicle Information Recognition
        
        @description Query detailed vehicle information through the license plate number and vehicle type.
        
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
        @summary Vehicle Information Recognition
        
        @description Query detailed vehicle information through the license plate number and vehicle type.
        
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
        @summary Vehicle Information Recognition
        
        @description Query detailed vehicle information through the license plate number and vehicle type.
        
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
        @summary Vehicle Information Recognition
        
        @description Query detailed vehicle information through the license plate number and vehicle type.
        
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
        @summary Call VerifyMaterial, in a pure server-side access authentication solution, input name, ID number, portrait photo, and front and back photos of the ID card (optional) for real-person authentication, and return the authentication result synchronously.
        
        @description Preparation for Access: When integrating this API, please ensure that the corresponding preparatory work has been completed. For details, please refer to [Server-side Access Preparation](https://help.aliyun.com/document_detail/127471.html).
        Request Method: HTTPS POST and GET.
        API Description: The server of the access party submits the authentication materials to the real-person authentication service for verification and comparison, with the results returned synchronously.
        Applicable Scope: This interface is only applicable to pure server-side access authentication solutions.
        Image Upload Address Explanation:
        - HTTP or HTTPS address: Supports publicly accessible HTTP or HTTPS addresses. For example, `http://image-demo.img-cn-hangzhou.aliyuncs.com/example.jpg`.
        - OSS address: If the images from the access party are local files, Alibaba Cloud also provides an upload SDK, supporting the business party to upload the images to the specified OSS bucket of the real-person authentication service, and use the obtained OSS address as the image address parameter in the interface. If your business needs to use the upload SDK, please submit a [ticket](https://selfservice.console.aliyun.com/ticket/category/cloudauth/today) to contact us for acquisition.
        Image Limitations:
        - Does not support relative or absolute paths of local images.
        - Please keep the size of a single image within 2 MB to avoid algorithm retrieval timeout.
        - The face area in the image should be at least 6464 pixels.
        - There is an 8 MB size limit for the Body of a single request. Please calculate the total size of all images and other information in the request, and do not exceed the limit.
        
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
        @summary Call VerifyMaterial, in a pure server-side access authentication solution, input name, ID number, portrait photo, and front and back photos of the ID card (optional) for real-person authentication, and return the authentication result synchronously.
        
        @description Preparation for Access: When integrating this API, please ensure that the corresponding preparatory work has been completed. For details, please refer to [Server-side Access Preparation](https://help.aliyun.com/document_detail/127471.html).
        Request Method: HTTPS POST and GET.
        API Description: The server of the access party submits the authentication materials to the real-person authentication service for verification and comparison, with the results returned synchronously.
        Applicable Scope: This interface is only applicable to pure server-side access authentication solutions.
        Image Upload Address Explanation:
        - HTTP or HTTPS address: Supports publicly accessible HTTP or HTTPS addresses. For example, `http://image-demo.img-cn-hangzhou.aliyuncs.com/example.jpg`.
        - OSS address: If the images from the access party are local files, Alibaba Cloud also provides an upload SDK, supporting the business party to upload the images to the specified OSS bucket of the real-person authentication service, and use the obtained OSS address as the image address parameter in the interface. If your business needs to use the upload SDK, please submit a [ticket](https://selfservice.console.aliyun.com/ticket/category/cloudauth/today) to contact us for acquisition.
        Image Limitations:
        - Does not support relative or absolute paths of local images.
        - Please keep the size of a single image within 2 MB to avoid algorithm retrieval timeout.
        - The face area in the image should be at least 6464 pixels.
        - There is an 8 MB size limit for the Body of a single request. Please calculate the total size of all images and other information in the request, and do not exceed the limit.
        
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
        @summary Call VerifyMaterial, in a pure server-side access authentication solution, input name, ID number, portrait photo, and front and back photos of the ID card (optional) for real-person authentication, and return the authentication result synchronously.
        
        @description Preparation for Access: When integrating this API, please ensure that the corresponding preparatory work has been completed. For details, please refer to [Server-side Access Preparation](https://help.aliyun.com/document_detail/127471.html).
        Request Method: HTTPS POST and GET.
        API Description: The server of the access party submits the authentication materials to the real-person authentication service for verification and comparison, with the results returned synchronously.
        Applicable Scope: This interface is only applicable to pure server-side access authentication solutions.
        Image Upload Address Explanation:
        - HTTP or HTTPS address: Supports publicly accessible HTTP or HTTPS addresses. For example, `http://image-demo.img-cn-hangzhou.aliyuncs.com/example.jpg`.
        - OSS address: If the images from the access party are local files, Alibaba Cloud also provides an upload SDK, supporting the business party to upload the images to the specified OSS bucket of the real-person authentication service, and use the obtained OSS address as the image address parameter in the interface. If your business needs to use the upload SDK, please submit a [ticket](https://selfservice.console.aliyun.com/ticket/category/cloudauth/today) to contact us for acquisition.
        Image Limitations:
        - Does not support relative or absolute paths of local images.
        - Please keep the size of a single image within 2 MB to avoid algorithm retrieval timeout.
        - The face area in the image should be at least 6464 pixels.
        - There is an 8 MB size limit for the Body of a single request. Please calculate the total size of all images and other information in the request, and do not exceed the limit.
        
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
        @summary Call VerifyMaterial, in a pure server-side access authentication solution, input name, ID number, portrait photo, and front and back photos of the ID card (optional) for real-person authentication, and return the authentication result synchronously.
        
        @description Preparation for Access: When integrating this API, please ensure that the corresponding preparatory work has been completed. For details, please refer to [Server-side Access Preparation](https://help.aliyun.com/document_detail/127471.html).
        Request Method: HTTPS POST and GET.
        API Description: The server of the access party submits the authentication materials to the real-person authentication service for verification and comparison, with the results returned synchronously.
        Applicable Scope: This interface is only applicable to pure server-side access authentication solutions.
        Image Upload Address Explanation:
        - HTTP or HTTPS address: Supports publicly accessible HTTP or HTTPS addresses. For example, `http://image-demo.img-cn-hangzhou.aliyuncs.com/example.jpg`.
        - OSS address: If the images from the access party are local files, Alibaba Cloud also provides an upload SDK, supporting the business party to upload the images to the specified OSS bucket of the real-person authentication service, and use the obtained OSS address as the image address parameter in the interface. If your business needs to use the upload SDK, please submit a [ticket](https://selfservice.console.aliyun.com/ticket/category/cloudauth/today) to contact us for acquisition.
        Image Limitations:
        - Does not support relative or absolute paths of local images.
        - Please keep the size of a single image within 2 MB to avoid algorithm retrieval timeout.
        - The face area in the image should be at least 6464 pixels.
        - There is an 8 MB size limit for the Body of a single request. Please calculate the total size of all images and other information in the request, and do not exceed the limit.
        
        @param request: VerifyMaterialRequest
        @return: VerifyMaterialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_material_with_options_async(request, runtime)
