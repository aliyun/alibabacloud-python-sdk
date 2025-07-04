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
from alibabacloud_farui20240628 import models as fa_rui_20240628_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('farui', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
            'Product': 'FaRui',
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
        create_text_file_req = fa_rui_20240628_models.CreateTextFileRequest()
        OpenApiUtilClient.convert(request, create_text_file_req)
        if not UtilClient.is_unset(request.text_file_url_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.text_file_url_object,
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
            create_text_file_req.text_file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
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
            'Product': 'FaRui',
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
        create_text_file_req = fa_rui_20240628_models.CreateTextFileRequest()
        OpenApiUtilClient.convert(request, create_text_file_req)
        if not UtilClient.is_unset(request.text_file_url_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.text_file_url_object,
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
            create_text_file_req.text_file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        create_text_file_resp = await self.create_text_file_with_options_async(workspace_id, create_text_file_req, headers, runtime)
        return create_text_file_resp

    def run_contract_result_generation_with_options(
        self,
        workspace_id: str,
        tmp_req: fa_rui_20240628_models.RunContractResultGenerationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fa_rui_20240628_models.RunContractResultGenerationResponse:
        """
        @summary 生成合同审查结果
        
        @param tmp_req: RunContractResultGenerationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunContractResultGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fa_rui_20240628_models.RunContractResultGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.assistant):
            request.assistant_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunContractResultGeneration',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/farui/contract/result/genarate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fa_rui_20240628_models.RunContractResultGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_contract_result_generation_with_options_async(
        self,
        workspace_id: str,
        tmp_req: fa_rui_20240628_models.RunContractResultGenerationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fa_rui_20240628_models.RunContractResultGenerationResponse:
        """
        @summary 生成合同审查结果
        
        @param tmp_req: RunContractResultGenerationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunContractResultGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fa_rui_20240628_models.RunContractResultGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.assistant):
            request.assistant_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunContractResultGeneration',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/farui/contract/result/genarate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fa_rui_20240628_models.RunContractResultGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_contract_result_generation(
        self,
        workspace_id: str,
        request: fa_rui_20240628_models.RunContractResultGenerationRequest,
    ) -> fa_rui_20240628_models.RunContractResultGenerationResponse:
        """
        @summary 生成合同审查结果
        
        @param request: RunContractResultGenerationRequest
        @return: RunContractResultGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_contract_result_generation_with_options(workspace_id, request, headers, runtime)

    async def run_contract_result_generation_async(
        self,
        workspace_id: str,
        request: fa_rui_20240628_models.RunContractResultGenerationRequest,
    ) -> fa_rui_20240628_models.RunContractResultGenerationResponse:
        """
        @summary 生成合同审查结果
        
        @param request: RunContractResultGenerationRequest
        @return: RunContractResultGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_contract_result_generation_with_options_async(workspace_id, request, headers, runtime)

    def run_contract_rule_generation_with_options(
        self,
        workspace_id: str,
        tmp_req: fa_rui_20240628_models.RunContractRuleGenerationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fa_rui_20240628_models.RunContractRuleGenerationResponse:
        """
        @summary 生成合同审查规则
        
        @param tmp_req: RunContractRuleGenerationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunContractRuleGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fa_rui_20240628_models.RunContractRuleGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.assistant):
            request.assistant_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunContractRuleGeneration',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/farui/contract/rule/genarate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fa_rui_20240628_models.RunContractRuleGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_contract_rule_generation_with_options_async(
        self,
        workspace_id: str,
        tmp_req: fa_rui_20240628_models.RunContractRuleGenerationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fa_rui_20240628_models.RunContractRuleGenerationResponse:
        """
        @summary 生成合同审查规则
        
        @param tmp_req: RunContractRuleGenerationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunContractRuleGenerationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fa_rui_20240628_models.RunContractRuleGenerationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.assistant):
            request.assistant_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.assistant, 'assistant', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunContractRuleGeneration',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/farui/contract/rule/genarate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fa_rui_20240628_models.RunContractRuleGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_contract_rule_generation(
        self,
        workspace_id: str,
        request: fa_rui_20240628_models.RunContractRuleGenerationRequest,
    ) -> fa_rui_20240628_models.RunContractRuleGenerationResponse:
        """
        @summary 生成合同审查规则
        
        @param request: RunContractRuleGenerationRequest
        @return: RunContractRuleGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_contract_rule_generation_with_options(workspace_id, request, headers, runtime)

    async def run_contract_rule_generation_async(
        self,
        workspace_id: str,
        request: fa_rui_20240628_models.RunContractRuleGenerationRequest,
    ) -> fa_rui_20240628_models.RunContractRuleGenerationResponse:
        """
        @summary 生成合同审查规则
        
        @param request: RunContractRuleGenerationRequest
        @return: RunContractRuleGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_contract_rule_generation_with_options_async(workspace_id, request, headers, runtime)

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
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'extra', 'json')
        if not UtilClient.is_unset(tmp_req.thread):
            request.thread_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.thread, 'thread', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not UtilClient.is_unset(request.extra_shrink):
            body['extra'] = request.extra_shrink
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
        if not UtilClient.is_unset(tmp_req.extra):
            request.extra_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extra, 'extra', 'json')
        if not UtilClient.is_unset(tmp_req.thread):
            request.thread_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.thread, 'thread', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.assistant_shrink):
            body['assistant'] = request.assistant_shrink
        if not UtilClient.is_unset(request.extra_shrink):
            body['extra'] = request.extra_shrink
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

    def run_search_case_full_text_with_options(
        self,
        workspace_id: str,
        tmp_req: fa_rui_20240628_models.RunSearchCaseFullTextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fa_rui_20240628_models.RunSearchCaseFullTextResponse:
        """
        @summary 案例检索
        
        @param tmp_req: RunSearchCaseFullTextRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSearchCaseFullTextResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fa_rui_20240628_models.RunSearchCaseFullTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_condition):
            request.filter_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_condition, 'filterCondition', 'json')
        if not UtilClient.is_unset(tmp_req.page_param):
            request.page_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page_param, 'pageParam', 'json')
        if not UtilClient.is_unset(tmp_req.query_keywords):
            request.query_keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_keywords, 'queryKeywords', 'json')
        if not UtilClient.is_unset(tmp_req.sort_key_and_direction):
            request.sort_key_and_direction_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort_key_and_direction, 'sortKeyAndDirection', 'json')
        if not UtilClient.is_unset(tmp_req.thread):
            request.thread_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.thread, 'thread', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.filter_condition_shrink):
            body['filterCondition'] = request.filter_condition_shrink
        if not UtilClient.is_unset(request.page_param_shrink):
            body['pageParam'] = request.page_param_shrink
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.query_keywords_shrink):
            body['queryKeywords'] = request.query_keywords_shrink
        if not UtilClient.is_unset(request.refer_level):
            body['referLevel'] = request.refer_level
        if not UtilClient.is_unset(request.sort_key_and_direction_shrink):
            body['sortKeyAndDirection'] = request.sort_key_and_direction_shrink
        if not UtilClient.is_unset(request.thread_shrink):
            body['thread'] = request.thread_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunSearchCaseFullText',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/farui/search/case/fulltext',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fa_rui_20240628_models.RunSearchCaseFullTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_search_case_full_text_with_options_async(
        self,
        workspace_id: str,
        tmp_req: fa_rui_20240628_models.RunSearchCaseFullTextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fa_rui_20240628_models.RunSearchCaseFullTextResponse:
        """
        @summary 案例检索
        
        @param tmp_req: RunSearchCaseFullTextRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSearchCaseFullTextResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fa_rui_20240628_models.RunSearchCaseFullTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_condition):
            request.filter_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_condition, 'filterCondition', 'json')
        if not UtilClient.is_unset(tmp_req.page_param):
            request.page_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page_param, 'pageParam', 'json')
        if not UtilClient.is_unset(tmp_req.query_keywords):
            request.query_keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_keywords, 'queryKeywords', 'json')
        if not UtilClient.is_unset(tmp_req.sort_key_and_direction):
            request.sort_key_and_direction_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort_key_and_direction, 'sortKeyAndDirection', 'json')
        if not UtilClient.is_unset(tmp_req.thread):
            request.thread_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.thread, 'thread', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.filter_condition_shrink):
            body['filterCondition'] = request.filter_condition_shrink
        if not UtilClient.is_unset(request.page_param_shrink):
            body['pageParam'] = request.page_param_shrink
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.query_keywords_shrink):
            body['queryKeywords'] = request.query_keywords_shrink
        if not UtilClient.is_unset(request.refer_level):
            body['referLevel'] = request.refer_level
        if not UtilClient.is_unset(request.sort_key_and_direction_shrink):
            body['sortKeyAndDirection'] = request.sort_key_and_direction_shrink
        if not UtilClient.is_unset(request.thread_shrink):
            body['thread'] = request.thread_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunSearchCaseFullText',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/farui/search/case/fulltext',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fa_rui_20240628_models.RunSearchCaseFullTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_search_case_full_text(
        self,
        workspace_id: str,
        request: fa_rui_20240628_models.RunSearchCaseFullTextRequest,
    ) -> fa_rui_20240628_models.RunSearchCaseFullTextResponse:
        """
        @summary 案例检索
        
        @param request: RunSearchCaseFullTextRequest
        @return: RunSearchCaseFullTextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_search_case_full_text_with_options(workspace_id, request, headers, runtime)

    async def run_search_case_full_text_async(
        self,
        workspace_id: str,
        request: fa_rui_20240628_models.RunSearchCaseFullTextRequest,
    ) -> fa_rui_20240628_models.RunSearchCaseFullTextResponse:
        """
        @summary 案例检索
        
        @param request: RunSearchCaseFullTextRequest
        @return: RunSearchCaseFullTextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_search_case_full_text_with_options_async(workspace_id, request, headers, runtime)

    def run_search_law_query_with_options(
        self,
        workspace_id: str,
        tmp_req: fa_rui_20240628_models.RunSearchLawQueryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fa_rui_20240628_models.RunSearchLawQueryResponse:
        """
        @summary 法规搜索
        
        @param tmp_req: RunSearchLawQueryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSearchLawQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fa_rui_20240628_models.RunSearchLawQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_condition):
            request.filter_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_condition, 'filterCondition', 'json')
        if not UtilClient.is_unset(tmp_req.page_param):
            request.page_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page_param, 'pageParam', 'json')
        if not UtilClient.is_unset(tmp_req.query_keywords):
            request.query_keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_keywords, 'queryKeywords', 'json')
        if not UtilClient.is_unset(tmp_req.thread):
            request.thread_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.thread, 'thread', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.filter_condition_shrink):
            body['filterCondition'] = request.filter_condition_shrink
        if not UtilClient.is_unset(request.page_param_shrink):
            body['pageParam'] = request.page_param_shrink
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.query_keywords_shrink):
            body['queryKeywords'] = request.query_keywords_shrink
        if not UtilClient.is_unset(request.thread_shrink):
            body['thread'] = request.thread_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunSearchLawQuery',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/farui/search/law/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fa_rui_20240628_models.RunSearchLawQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_search_law_query_with_options_async(
        self,
        workspace_id: str,
        tmp_req: fa_rui_20240628_models.RunSearchLawQueryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> fa_rui_20240628_models.RunSearchLawQueryResponse:
        """
        @summary 法规搜索
        
        @param tmp_req: RunSearchLawQueryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSearchLawQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = fa_rui_20240628_models.RunSearchLawQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_condition):
            request.filter_condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_condition, 'filterCondition', 'json')
        if not UtilClient.is_unset(tmp_req.page_param):
            request.page_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page_param, 'pageParam', 'json')
        if not UtilClient.is_unset(tmp_req.query_keywords):
            request.query_keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_keywords, 'queryKeywords', 'json')
        if not UtilClient.is_unset(tmp_req.thread):
            request.thread_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.thread, 'thread', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.filter_condition_shrink):
            body['filterCondition'] = request.filter_condition_shrink
        if not UtilClient.is_unset(request.page_param_shrink):
            body['pageParam'] = request.page_param_shrink
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.query_keywords_shrink):
            body['queryKeywords'] = request.query_keywords_shrink
        if not UtilClient.is_unset(request.thread_shrink):
            body['thread'] = request.thread_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunSearchLawQuery',
            version='2024-06-28',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/farui/search/law/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            fa_rui_20240628_models.RunSearchLawQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_search_law_query(
        self,
        workspace_id: str,
        request: fa_rui_20240628_models.RunSearchLawQueryRequest,
    ) -> fa_rui_20240628_models.RunSearchLawQueryResponse:
        """
        @summary 法规搜索
        
        @param request: RunSearchLawQueryRequest
        @return: RunSearchLawQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_search_law_query_with_options(workspace_id, request, headers, runtime)

    async def run_search_law_query_async(
        self,
        workspace_id: str,
        request: fa_rui_20240628_models.RunSearchLawQueryRequest,
    ) -> fa_rui_20240628_models.RunSearchLawQueryResponse:
        """
        @summary 法规搜索
        
        @param request: RunSearchLawQueryRequest
        @return: RunSearchLawQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_search_law_query_with_options_async(workspace_id, request, headers, runtime)
