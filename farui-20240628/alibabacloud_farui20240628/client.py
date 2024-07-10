# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_farui20240628 import models as fa_rui_20240628_models
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
        self._endpoint = self.get_endpoint('farui', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_text_file_with_options(
        self,
        workspace_id: str,
        request: fa_rui_20240628_models.CreateTextFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fa_rui_20240628_models.CreateTextFileResponse:
        """
        @summary 上传合同文件
        
        @param request: CreateTextFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTextFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_time):
            body['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.text_file_name):
            body['TextFileName'] = request.text_file_name
        if not UtilClient.is_unset(request.text_file_url):
            body['TextFileUrl'] = request.text_file_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTextFile',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/data/textFile',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fa_rui_20240628_models.CreateTextFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_text_file_with_options_async(
        self,
        workspace_id: str,
        request: fa_rui_20240628_models.CreateTextFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fa_rui_20240628_models.CreateTextFileResponse:
        """
        @summary 上传合同文件
        
        @param request: CreateTextFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTextFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_time):
            body['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.text_file_name):
            body['TextFileName'] = request.text_file_name
        if not UtilClient.is_unset(request.text_file_url):
            body['TextFileUrl'] = request.text_file_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTextFile',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/data/textFile',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fa_rui_20240628_models.CreateTextFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_text_file(
        self,
        workspace_id: str,
        request: fa_rui_20240628_models.CreateTextFileRequest,
    ) -> fa_rui_20240628_models.CreateTextFileResponse:
        """
        @summary 上传合同文件
        
        @param request: CreateTextFileRequest
        @return: CreateTextFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_text_file_with_options(workspace_id, request, headers, runtime)

    async def create_text_file_async(
        self,
        workspace_id: str,
        request: fa_rui_20240628_models.CreateTextFileRequest,
    ) -> fa_rui_20240628_models.CreateTextFileResponse:
        """
        @summary 上传合同文件
        
        @param request: CreateTextFileRequest
        @return: CreateTextFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_text_file_with_options_async(workspace_id, request, headers, runtime)

    def create_text_file_advance(
        self,
        workspace_id: str,
        request: fa_rui_20240628_models.CreateTextFileAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fa_rui_20240628_models.CreateTextFileResponse:
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
            product='FaRui',
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
        create_text_file_req = fa_rui_20240628_models.CreateTextFileRequest()
        OpenApiUtilClient.convert(request, create_text_file_req)
        if not UtilClient.is_unset(request.text_file_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.text_file_url_object,
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
            create_text_file_req.text_file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        create_text_file_resp = self.create_text_file_with_options(workspace_id, create_text_file_req, headers, runtime)
        return create_text_file_resp

    async def create_text_file_advance_async(
        self,
        workspace_id: str,
        request: fa_rui_20240628_models.CreateTextFileAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fa_rui_20240628_models.CreateTextFileResponse:
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
            product='FaRui',
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
        create_text_file_req = fa_rui_20240628_models.CreateTextFileRequest()
        OpenApiUtilClient.convert(request, create_text_file_req)
        if not UtilClient.is_unset(request.text_file_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.text_file_url_object,
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
            create_text_file_req.text_file_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        create_text_file_resp = await self.create_text_file_with_options_async(workspace_id, create_text_file_req, headers, runtime)
        return create_text_file_resp

    def run_legal_advice_consultation_with_options(
        self,
        workspace_id: str,
        tmp_req: fa_rui_20240628_models.RunLegalAdviceConsultationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fa_rui_20240628_models.RunLegalAdviceConsultationResponse:
        """
        @summary 法律咨询
        
        @param tmp_req: RunLegalAdviceConsultationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunLegalAdviceConsultationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fa_rui_20240628_models.RunLegalAdviceConsultationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.assistant):
            request.assistant_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        if not UtilClient.is_unset(tmp_req.thread):
            request.thread_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.thread, 'thread', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        if not UtilClient.is_unset(request.thread_shrink):
            body['thread'] = request.thread_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunLegalAdviceConsultation',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/farui/legalAdvice/consult',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fa_rui_20240628_models.RunLegalAdviceConsultationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_legal_advice_consultation_with_options_async(
        self,
        workspace_id: str,
        tmp_req: fa_rui_20240628_models.RunLegalAdviceConsultationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fa_rui_20240628_models.RunLegalAdviceConsultationResponse:
        """
        @summary 法律咨询
        
        @param tmp_req: RunLegalAdviceConsultationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunLegalAdviceConsultationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fa_rui_20240628_models.RunLegalAdviceConsultationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.assistant):
            request.assistant_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        if not UtilClient.is_unset(tmp_req.thread):
            request.thread_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.thread, 'thread', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        if not UtilClient.is_unset(request.thread_shrink):
            body['thread'] = request.thread_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunLegalAdviceConsultation',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/farui/legalAdvice/consult',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fa_rui_20240628_models.RunLegalAdviceConsultationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_legal_advice_consultation(
        self,
        workspace_id: str,
        request: fa_rui_20240628_models.RunLegalAdviceConsultationRequest,
    ) -> fa_rui_20240628_models.RunLegalAdviceConsultationResponse:
        """
        @summary 法律咨询
        
        @param request: RunLegalAdviceConsultationRequest
        @return: RunLegalAdviceConsultationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_legal_advice_consultation_with_options(workspace_id, request, headers, runtime)

    async def run_legal_advice_consultation_async(
        self,
        workspace_id: str,
        request: fa_rui_20240628_models.RunLegalAdviceConsultationRequest,
    ) -> fa_rui_20240628_models.RunLegalAdviceConsultationResponse:
        """
        @summary 法律咨询
        
        @param request: RunLegalAdviceConsultationRequest
        @return: RunLegalAdviceConsultationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_legal_advice_consultation_with_options_async(workspace_id, request, headers, runtime)
