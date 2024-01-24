# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudauth20200618 import models as cloudauth_20200618_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_oss_sdk.client import Client as OSSClient


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

    def contrast_smart_verify_with_options(
        self,
        request: cloudauth_20200618_models.ContrastSmartVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.ContrastSmartVerifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_name):
            body['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_no):
            body['CertNo'] = request.cert_no
        if not UtilClient.is_unset(request.cert_type):
            body['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.face_pic_file):
            body['FacePicFile'] = request.face_pic_file
        if not UtilClient.is_unset(request.face_pic_string):
            body['FacePicString'] = request.face_pic_string
        if not UtilClient.is_unset(request.face_pic_url):
            body['FacePicUrl'] = request.face_pic_url
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ContrastSmartVerify',
            version='2020-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20200618_models.ContrastSmartVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def contrast_smart_verify_with_options_async(
        self,
        request: cloudauth_20200618_models.ContrastSmartVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.ContrastSmartVerifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_name):
            body['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_no):
            body['CertNo'] = request.cert_no
        if not UtilClient.is_unset(request.cert_type):
            body['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.face_pic_file):
            body['FacePicFile'] = request.face_pic_file
        if not UtilClient.is_unset(request.face_pic_string):
            body['FacePicString'] = request.face_pic_string
        if not UtilClient.is_unset(request.face_pic_url):
            body['FacePicUrl'] = request.face_pic_url
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ContrastSmartVerify',
            version='2020-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20200618_models.ContrastSmartVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def contrast_smart_verify(
        self,
        request: cloudauth_20200618_models.ContrastSmartVerifyRequest,
    ) -> cloudauth_20200618_models.ContrastSmartVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.contrast_smart_verify_with_options(request, runtime)

    async def contrast_smart_verify_async(
        self,
        request: cloudauth_20200618_models.ContrastSmartVerifyRequest,
    ) -> cloudauth_20200618_models.ContrastSmartVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.contrast_smart_verify_with_options_async(request, runtime)

    def contrast_smart_verify_advance(
        self,
        request: cloudauth_20200618_models.ContrastSmartVerifyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.ContrastSmartVerifyResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
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
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        contrast_smart_verify_req = cloudauth_20200618_models.ContrastSmartVerifyRequest()
        OpenApiUtilClient.convert(request, contrast_smart_verify_req)
        if not UtilClient.is_unset(request.face_pic_file_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.face_pic_file_object,
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
            contrast_smart_verify_req.face_pic_file = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        contrast_smart_verify_resp = self.contrast_smart_verify_with_options(contrast_smart_verify_req, runtime)
        return contrast_smart_verify_resp

    async def contrast_smart_verify_advance_async(
        self,
        request: cloudauth_20200618_models.ContrastSmartVerifyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.ContrastSmartVerifyResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
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
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        contrast_smart_verify_req = cloudauth_20200618_models.ContrastSmartVerifyRequest()
        OpenApiUtilClient.convert(request, contrast_smart_verify_req)
        if not UtilClient.is_unset(request.face_pic_file_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.face_pic_file_object,
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
            contrast_smart_verify_req.face_pic_file = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        contrast_smart_verify_resp = await self.contrast_smart_verify_with_options_async(contrast_smart_verify_req, runtime)
        return contrast_smart_verify_resp

    def describe_smart_verify_with_options(
        self,
        request: cloudauth_20200618_models.DescribeSmartVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.DescribeSmartVerifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.certify_id):
            body['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.picture_return_type):
            body['PictureReturnType'] = request.picture_return_type
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSmartVerify',
            version='2020-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20200618_models.DescribeSmartVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smart_verify_with_options_async(
        self,
        request: cloudauth_20200618_models.DescribeSmartVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.DescribeSmartVerifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.certify_id):
            body['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.picture_return_type):
            body['PictureReturnType'] = request.picture_return_type
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSmartVerify',
            version='2020-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20200618_models.DescribeSmartVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_smart_verify(
        self,
        request: cloudauth_20200618_models.DescribeSmartVerifyRequest,
    ) -> cloudauth_20200618_models.DescribeSmartVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_smart_verify_with_options(request, runtime)

    async def describe_smart_verify_async(
        self,
        request: cloudauth_20200618_models.DescribeSmartVerifyRequest,
    ) -> cloudauth_20200618_models.DescribeSmartVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_smart_verify_with_options_async(request, runtime)

    def describe_sms_detail_with_options(
        self,
        request: cloudauth_20200618_models.DescribeSmsDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.DescribeSmsDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.error_code):
            body['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.send_date):
            body['SendDate'] = request.send_date
        if not UtilClient.is_unset(request.send_status):
            body['SendStatus'] = request.send_status
        if not UtilClient.is_unset(request.sign_name):
            body['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSmsDetail',
            version='2020-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20200618_models.DescribeSmsDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sms_detail_with_options_async(
        self,
        request: cloudauth_20200618_models.DescribeSmsDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.DescribeSmsDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.error_code):
            body['ErrorCode'] = request.error_code
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.send_date):
            body['SendDate'] = request.send_date
        if not UtilClient.is_unset(request.send_status):
            body['SendStatus'] = request.send_status
        if not UtilClient.is_unset(request.sign_name):
            body['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSmsDetail',
            version='2020-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20200618_models.DescribeSmsDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sms_detail(
        self,
        request: cloudauth_20200618_models.DescribeSmsDetailRequest,
    ) -> cloudauth_20200618_models.DescribeSmsDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sms_detail_with_options(request, runtime)

    async def describe_sms_detail_async(
        self,
        request: cloudauth_20200618_models.DescribeSmsDetailRequest,
    ) -> cloudauth_20200618_models.DescribeSmsDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sms_detail_with_options_async(request, runtime)

    def element_smart_verify_with_options(
        self,
        request: cloudauth_20200618_models.ElementSmartVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.ElementSmartVerifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_file):
            body['CertFile'] = request.cert_file
        if not UtilClient.is_unset(request.cert_name):
            body['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_national_emblem_url):
            body['CertNationalEmblemUrl'] = request.cert_national_emblem_url
        if not UtilClient.is_unset(request.cert_no):
            body['CertNo'] = request.cert_no
        if not UtilClient.is_unset(request.cert_type):
            body['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.cert_url):
            body['CertUrl'] = request.cert_url
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ElementSmartVerify',
            version='2020-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20200618_models.ElementSmartVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def element_smart_verify_with_options_async(
        self,
        request: cloudauth_20200618_models.ElementSmartVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.ElementSmartVerifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert_file):
            body['CertFile'] = request.cert_file
        if not UtilClient.is_unset(request.cert_name):
            body['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_national_emblem_url):
            body['CertNationalEmblemUrl'] = request.cert_national_emblem_url
        if not UtilClient.is_unset(request.cert_no):
            body['CertNo'] = request.cert_no
        if not UtilClient.is_unset(request.cert_type):
            body['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.cert_url):
            body['CertUrl'] = request.cert_url
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ElementSmartVerify',
            version='2020-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20200618_models.ElementSmartVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def element_smart_verify(
        self,
        request: cloudauth_20200618_models.ElementSmartVerifyRequest,
    ) -> cloudauth_20200618_models.ElementSmartVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.element_smart_verify_with_options(request, runtime)

    async def element_smart_verify_async(
        self,
        request: cloudauth_20200618_models.ElementSmartVerifyRequest,
    ) -> cloudauth_20200618_models.ElementSmartVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.element_smart_verify_with_options_async(request, runtime)

    def element_smart_verify_advance(
        self,
        request: cloudauth_20200618_models.ElementSmartVerifyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.ElementSmartVerifyResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
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
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        element_smart_verify_req = cloudauth_20200618_models.ElementSmartVerifyRequest()
        OpenApiUtilClient.convert(request, element_smart_verify_req)
        if not UtilClient.is_unset(request.cert_file_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.cert_file_object,
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
            element_smart_verify_req.cert_file = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        element_smart_verify_resp = self.element_smart_verify_with_options(element_smart_verify_req, runtime)
        return element_smart_verify_resp

    async def element_smart_verify_advance_async(
        self,
        request: cloudauth_20200618_models.ElementSmartVerifyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.ElementSmartVerifyResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
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
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        element_smart_verify_req = cloudauth_20200618_models.ElementSmartVerifyRequest()
        OpenApiUtilClient.convert(request, element_smart_verify_req)
        if not UtilClient.is_unset(request.cert_file_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.cert_file_object,
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
            element_smart_verify_req.cert_file = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        element_smart_verify_resp = await self.element_smart_verify_with_options_async(element_smart_verify_req, runtime)
        return element_smart_verify_resp

    def init_smart_verify_with_options(
        self,
        request: cloudauth_20200618_models.InitSmartVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.InitSmartVerifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_token):
            body['CallbackToken'] = request.callback_token
        if not UtilClient.is_unset(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.cert_name):
            body['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_no):
            body['CertNo'] = request.cert_no
        if not UtilClient.is_unset(request.cert_type):
            body['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.certify_id):
            body['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.face_picture_base_64):
            body['FacePictureBase64'] = request.face_picture_base_64
        if not UtilClient.is_unset(request.face_picture_url):
            body['FacePictureUrl'] = request.face_picture_url
        if not UtilClient.is_unset(request.id_name):
            body['IdName'] = request.id_name
        if not UtilClient.is_unset(request.id_no):
            body['IdNo'] = request.id_no
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.meta_info):
            body['MetaInfo'] = request.meta_info
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.ocr):
            body['Ocr'] = request.ocr
        if not UtilClient.is_unset(request.oss_bucket_name):
            body['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_object_name):
            body['OssObjectName'] = request.oss_object_name
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitSmartVerify',
            version='2020-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20200618_models.InitSmartVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_smart_verify_with_options_async(
        self,
        request: cloudauth_20200618_models.InitSmartVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.InitSmartVerifyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.callback_token):
            body['CallbackToken'] = request.callback_token
        if not UtilClient.is_unset(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.cert_name):
            body['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_no):
            body['CertNo'] = request.cert_no
        if not UtilClient.is_unset(request.cert_type):
            body['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.certify_id):
            body['CertifyId'] = request.certify_id
        if not UtilClient.is_unset(request.face_picture_base_64):
            body['FacePictureBase64'] = request.face_picture_base_64
        if not UtilClient.is_unset(request.face_picture_url):
            body['FacePictureUrl'] = request.face_picture_url
        if not UtilClient.is_unset(request.id_name):
            body['IdName'] = request.id_name
        if not UtilClient.is_unset(request.id_no):
            body['IdNo'] = request.id_no
        if not UtilClient.is_unset(request.ip):
            body['Ip'] = request.ip
        if not UtilClient.is_unset(request.meta_info):
            body['MetaInfo'] = request.meta_info
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.ocr):
            body['Ocr'] = request.ocr
        if not UtilClient.is_unset(request.oss_bucket_name):
            body['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_object_name):
            body['OssObjectName'] = request.oss_object_name
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitSmartVerify',
            version='2020-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20200618_models.InitSmartVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_smart_verify(
        self,
        request: cloudauth_20200618_models.InitSmartVerifyRequest,
    ) -> cloudauth_20200618_models.InitSmartVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_smart_verify_with_options(request, runtime)

    async def init_smart_verify_async(
        self,
        request: cloudauth_20200618_models.InitSmartVerifyRequest,
    ) -> cloudauth_20200618_models.InitSmartVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_smart_verify_with_options_async(request, runtime)

    def send_sms_with_options(
        self,
        request: cloudauth_20200618_models.SendSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.SendSmsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.sign_name):
            body['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            body['TemplateParam'] = request.template_param
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendSms',
            version='2020-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20200618_models.SendSmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_sms_with_options_async(
        self,
        request: cloudauth_20200618_models.SendSmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.SendSmsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.sign_name):
            body['SignName'] = request.sign_name
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_param):
            body['TemplateParam'] = request.template_param
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendSms',
            version='2020-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20200618_models.SendSmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_sms(
        self,
        request: cloudauth_20200618_models.SendSmsRequest,
    ) -> cloudauth_20200618_models.SendSmsResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_sms_with_options(request, runtime)

    async def send_sms_async(
        self,
        request: cloudauth_20200618_models.SendSmsRequest,
    ) -> cloudauth_20200618_models.SendSmsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_sms_with_options_async(request, runtime)

    def verify_bank_element_with_options(
        self,
        request: cloudauth_20200618_models.VerifyBankElementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.VerifyBankElementResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bank_card_file):
            body['BankCardFile'] = request.bank_card_file
        if not UtilClient.is_unset(request.bank_card_no):
            body['BankCardNo'] = request.bank_card_no
        if not UtilClient.is_unset(request.bank_card_url):
            body['BankCardUrl'] = request.bank_card_url
        if not UtilClient.is_unset(request.id_name):
            body['IdName'] = request.id_name
        if not UtilClient.is_unset(request.id_no):
            body['IdNo'] = request.id_no
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyBankElement',
            version='2020-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20200618_models.VerifyBankElementResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_bank_element_with_options_async(
        self,
        request: cloudauth_20200618_models.VerifyBankElementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.VerifyBankElementResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bank_card_file):
            body['BankCardFile'] = request.bank_card_file
        if not UtilClient.is_unset(request.bank_card_no):
            body['BankCardNo'] = request.bank_card_no
        if not UtilClient.is_unset(request.bank_card_url):
            body['BankCardUrl'] = request.bank_card_url
        if not UtilClient.is_unset(request.id_name):
            body['IdName'] = request.id_name
        if not UtilClient.is_unset(request.id_no):
            body['IdNo'] = request.id_no
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.outer_order_no):
            body['OuterOrderNo'] = request.outer_order_no
        if not UtilClient.is_unset(request.scene_id):
            body['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyBankElement',
            version='2020-06-18',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudauth_20200618_models.VerifyBankElementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_bank_element(
        self,
        request: cloudauth_20200618_models.VerifyBankElementRequest,
    ) -> cloudauth_20200618_models.VerifyBankElementResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_bank_element_with_options(request, runtime)

    async def verify_bank_element_async(
        self,
        request: cloudauth_20200618_models.VerifyBankElementRequest,
    ) -> cloudauth_20200618_models.VerifyBankElementResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_bank_element_with_options_async(request, runtime)

    def verify_bank_element_advance(
        self,
        request: cloudauth_20200618_models.VerifyBankElementAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.VerifyBankElementResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
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
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        verify_bank_element_req = cloudauth_20200618_models.VerifyBankElementRequest()
        OpenApiUtilClient.convert(request, verify_bank_element_req)
        if not UtilClient.is_unset(request.bank_card_file_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.bank_card_file_object,
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
            verify_bank_element_req.bank_card_file = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        verify_bank_element_resp = self.verify_bank_element_with_options(verify_bank_element_req, runtime)
        return verify_bank_element_resp

    async def verify_bank_element_advance_async(
        self,
        request: cloudauth_20200618_models.VerifyBankElementAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudauth_20200618_models.VerifyBankElementResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
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
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        verify_bank_element_req = cloudauth_20200618_models.VerifyBankElementRequest()
        OpenApiUtilClient.convert(request, verify_bank_element_req)
        if not UtilClient.is_unset(request.bank_card_file_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.bank_card_file_object,
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
            verify_bank_element_req.bank_card_file = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        verify_bank_element_resp = await self.verify_bank_element_with_options_async(verify_bank_element_req, runtime)
        return verify_bank_element_resp
