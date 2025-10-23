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
from alibabacloud_energyexpertexternal20220923 import models as energy_expert_external_20220923_models
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
        self._endpoint = self.get_endpoint('energyexpertexternal', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_folder_with_options(
        self,
        request: energy_expert_external_20220923_models.AddFolderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.AddFolderResponse:
        """
        @summary 创建文件夹
        
        @param request: AddFolderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFolderResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.folder_name):
            body['folderName'] = request.folder_name
        if not UtilClient.is_unset(request.parent_folder_id):
            body['parentFolderId'] = request.parent_folder_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFolder',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/aidoc/folder/add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.AddFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_folder_with_options_async(
        self,
        request: energy_expert_external_20220923_models.AddFolderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.AddFolderResponse:
        """
        @summary 创建文件夹
        
        @param request: AddFolderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFolderResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.folder_name):
            body['folderName'] = request.folder_name
        if not UtilClient.is_unset(request.parent_folder_id):
            body['parentFolderId'] = request.parent_folder_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFolder',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/aidoc/folder/add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.AddFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_folder(
        self,
        request: energy_expert_external_20220923_models.AddFolderRequest,
    ) -> energy_expert_external_20220923_models.AddFolderResponse:
        """
        @summary 创建文件夹
        
        @param request: AddFolderRequest
        @return: AddFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_folder_with_options(request, headers, runtime)

    async def add_folder_async(
        self,
        request: energy_expert_external_20220923_models.AddFolderRequest,
    ) -> energy_expert_external_20220923_models.AddFolderResponse:
        """
        @summary 创建文件夹
        
        @param request: AddFolderRequest
        @return: AddFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_folder_with_options_async(request, headers, runtime)

    def analyze_vl_realtime_with_options(
        self,
        request: energy_expert_external_20220923_models.AnalyzeVlRealtimeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.AnalyzeVlRealtimeResponse:
        """
        @summary Get Document Results
        
        @description Users obtain real-time VL results by uploading a document URL.
        
        @param request: AnalyzeVlRealtimeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AnalyzeVlRealtimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_url):
            query['fileUrl'] = request.file_url
        if not UtilClient.is_unset(request.language):
            query['language'] = request.language
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AnalyzeVlRealtime',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/aidoc/document/analyzeVlRealtime',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.AnalyzeVlRealtimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def analyze_vl_realtime_with_options_async(
        self,
        request: energy_expert_external_20220923_models.AnalyzeVlRealtimeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.AnalyzeVlRealtimeResponse:
        """
        @summary Get Document Results
        
        @description Users obtain real-time VL results by uploading a document URL.
        
        @param request: AnalyzeVlRealtimeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AnalyzeVlRealtimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_url):
            query['fileUrl'] = request.file_url
        if not UtilClient.is_unset(request.language):
            query['language'] = request.language
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AnalyzeVlRealtime',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/aidoc/document/analyzeVlRealtime',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.AnalyzeVlRealtimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def analyze_vl_realtime(
        self,
        request: energy_expert_external_20220923_models.AnalyzeVlRealtimeRequest,
    ) -> energy_expert_external_20220923_models.AnalyzeVlRealtimeResponse:
        """
        @summary Get Document Results
        
        @description Users obtain real-time VL results by uploading a document URL.
        
        @param request: AnalyzeVlRealtimeRequest
        @return: AnalyzeVlRealtimeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.analyze_vl_realtime_with_options(request, headers, runtime)

    async def analyze_vl_realtime_async(
        self,
        request: energy_expert_external_20220923_models.AnalyzeVlRealtimeRequest,
    ) -> energy_expert_external_20220923_models.AnalyzeVlRealtimeResponse:
        """
        @summary Get Document Results
        
        @description Users obtain real-time VL results by uploading a document URL.
        
        @param request: AnalyzeVlRealtimeRequest
        @return: AnalyzeVlRealtimeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.analyze_vl_realtime_with_options_async(request, headers, runtime)

    def analyze_vl_realtime_advance(
        self,
        request: energy_expert_external_20220923_models.AnalyzeVlRealtimeAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.AnalyzeVlRealtimeResponse:
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
            'Product': 'energyExpertExternal',
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
        analyze_vl_realtime_req = energy_expert_external_20220923_models.AnalyzeVlRealtimeRequest()
        OpenApiUtilClient.convert(request, analyze_vl_realtime_req)
        if not UtilClient.is_unset(request.file_url_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_url_object,
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
            analyze_vl_realtime_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        analyze_vl_realtime_resp = self.analyze_vl_realtime_with_options(analyze_vl_realtime_req, headers, runtime)
        return analyze_vl_realtime_resp

    async def analyze_vl_realtime_advance_async(
        self,
        request: energy_expert_external_20220923_models.AnalyzeVlRealtimeAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.AnalyzeVlRealtimeResponse:
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
            'Product': 'energyExpertExternal',
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
        analyze_vl_realtime_req = energy_expert_external_20220923_models.AnalyzeVlRealtimeRequest()
        OpenApiUtilClient.convert(request, analyze_vl_realtime_req)
        if not UtilClient.is_unset(request.file_url_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_url_object,
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
            analyze_vl_realtime_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        analyze_vl_realtime_resp = await self.analyze_vl_realtime_with_options_async(analyze_vl_realtime_req, headers, runtime)
        return analyze_vl_realtime_resp

    def batch_save_instruction_status_with_options(
        self,
        request: energy_expert_external_20220923_models.BatchSaveInstructionStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.BatchSaveInstructionStatusResponse:
        """
        @summary 策略执行状态反馈
        
        @param request: BatchSaveInstructionStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSaveInstructionStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.factory_id):
            body['factoryId'] = request.factory_id
        if not UtilClient.is_unset(request.p_key):
            body['pKey'] = request.p_key
        if not UtilClient.is_unset(request.status_list):
            body['statusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchSaveInstructionStatus',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/hvac/batchSaveInstructionStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.BatchSaveInstructionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_save_instruction_status_with_options_async(
        self,
        request: energy_expert_external_20220923_models.BatchSaveInstructionStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.BatchSaveInstructionStatusResponse:
        """
        @summary 策略执行状态反馈
        
        @param request: BatchSaveInstructionStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSaveInstructionStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.factory_id):
            body['factoryId'] = request.factory_id
        if not UtilClient.is_unset(request.p_key):
            body['pKey'] = request.p_key
        if not UtilClient.is_unset(request.status_list):
            body['statusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchSaveInstructionStatus',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/hvac/batchSaveInstructionStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.BatchSaveInstructionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_save_instruction_status(
        self,
        request: energy_expert_external_20220923_models.BatchSaveInstructionStatusRequest,
    ) -> energy_expert_external_20220923_models.BatchSaveInstructionStatusResponse:
        """
        @summary 策略执行状态反馈
        
        @param request: BatchSaveInstructionStatusRequest
        @return: BatchSaveInstructionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_save_instruction_status_with_options(request, headers, runtime)

    async def batch_save_instruction_status_async(
        self,
        request: energy_expert_external_20220923_models.BatchSaveInstructionStatusRequest,
    ) -> energy_expert_external_20220923_models.BatchSaveInstructionStatusResponse:
        """
        @summary 策略执行状态反馈
        
        @param request: BatchSaveInstructionStatusRequest
        @return: BatchSaveInstructionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_save_instruction_status_with_options_async(request, headers, runtime)

    def batch_update_system_running_plan_with_options(
        self,
        request: energy_expert_external_20220923_models.BatchUpdateSystemRunningPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.BatchUpdateSystemRunningPlanResponse:
        """
        @summary 批量设置空调站点运行计划
        
        @param request: BatchUpdateSystemRunningPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUpdateSystemRunningPlanResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.control_type):
            body['controlType'] = request.control_type
        if not UtilClient.is_unset(request.date_type):
            body['dateType'] = request.date_type
        if not UtilClient.is_unset(request.earliest_startup_time):
            body['earliestStartupTime'] = request.earliest_startup_time
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.factory_id):
            body['factoryId'] = request.factory_id
        if not UtilClient.is_unset(request.latest_shutdown_time):
            body['latestShutdownTime'] = request.latest_shutdown_time
        if not UtilClient.is_unset(request.max_carbon_dioxide):
            body['maxCarbonDioxide'] = request.max_carbon_dioxide
        if not UtilClient.is_unset(request.max_tem):
            body['maxTem'] = request.max_tem
        if not UtilClient.is_unset(request.min_tem):
            body['minTem'] = request.min_tem
        if not UtilClient.is_unset(request.season_mode):
            body['seasonMode'] = request.season_mode
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.system_id):
            body['systemId'] = request.system_id
        if not UtilClient.is_unset(request.working_end_time):
            body['workingEndTime'] = request.working_end_time
        if not UtilClient.is_unset(request.working_start_time):
            body['workingStartTime'] = request.working_start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUpdateSystemRunningPlan',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/hvac/batchUpdateSystemRunningPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.BatchUpdateSystemRunningPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_update_system_running_plan_with_options_async(
        self,
        request: energy_expert_external_20220923_models.BatchUpdateSystemRunningPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.BatchUpdateSystemRunningPlanResponse:
        """
        @summary 批量设置空调站点运行计划
        
        @param request: BatchUpdateSystemRunningPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUpdateSystemRunningPlanResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.control_type):
            body['controlType'] = request.control_type
        if not UtilClient.is_unset(request.date_type):
            body['dateType'] = request.date_type
        if not UtilClient.is_unset(request.earliest_startup_time):
            body['earliestStartupTime'] = request.earliest_startup_time
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.factory_id):
            body['factoryId'] = request.factory_id
        if not UtilClient.is_unset(request.latest_shutdown_time):
            body['latestShutdownTime'] = request.latest_shutdown_time
        if not UtilClient.is_unset(request.max_carbon_dioxide):
            body['maxCarbonDioxide'] = request.max_carbon_dioxide
        if not UtilClient.is_unset(request.max_tem):
            body['maxTem'] = request.max_tem
        if not UtilClient.is_unset(request.min_tem):
            body['minTem'] = request.min_tem
        if not UtilClient.is_unset(request.season_mode):
            body['seasonMode'] = request.season_mode
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.system_id):
            body['systemId'] = request.system_id
        if not UtilClient.is_unset(request.working_end_time):
            body['workingEndTime'] = request.working_end_time
        if not UtilClient.is_unset(request.working_start_time):
            body['workingStartTime'] = request.working_start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUpdateSystemRunningPlan',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/hvac/batchUpdateSystemRunningPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.BatchUpdateSystemRunningPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_update_system_running_plan(
        self,
        request: energy_expert_external_20220923_models.BatchUpdateSystemRunningPlanRequest,
    ) -> energy_expert_external_20220923_models.BatchUpdateSystemRunningPlanResponse:
        """
        @summary 批量设置空调站点运行计划
        
        @param request: BatchUpdateSystemRunningPlanRequest
        @return: BatchUpdateSystemRunningPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.batch_update_system_running_plan_with_options(request, headers, runtime)

    async def batch_update_system_running_plan_async(
        self,
        request: energy_expert_external_20220923_models.BatchUpdateSystemRunningPlanRequest,
    ) -> energy_expert_external_20220923_models.BatchUpdateSystemRunningPlanResponse:
        """
        @summary 批量设置空调站点运行计划
        
        @param request: BatchUpdateSystemRunningPlanRequest
        @return: BatchUpdateSystemRunningPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.batch_update_system_running_plan_with_options_async(request, headers, runtime)

    def chat_with_options(
        self,
        request: energy_expert_external_20220923_models.ChatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.ChatResponse:
        """
        @summary Knowledge Base Q\\&A
        
        @description - The interface provides Q&A services within the scope of the selected directory in the session.
        - The sessionId information is obtained through GetChatSessionList.
        - You can also create a new session via the CreateChatSession interface.
        
        @param request: ChatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.question):
            body['question'] = request.question
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Chat',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/chat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.ChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_with_options_async(
        self,
        request: energy_expert_external_20220923_models.ChatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.ChatResponse:
        """
        @summary Knowledge Base Q\\&A
        
        @description - The interface provides Q&A services within the scope of the selected directory in the session.
        - The sessionId information is obtained through GetChatSessionList.
        - You can also create a new session via the CreateChatSession interface.
        
        @param request: ChatRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.question):
            body['question'] = request.question
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Chat',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/chat',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.ChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat(
        self,
        request: energy_expert_external_20220923_models.ChatRequest,
    ) -> energy_expert_external_20220923_models.ChatResponse:
        """
        @summary Knowledge Base Q\\&A
        
        @description - The interface provides Q&A services within the scope of the selected directory in the session.
        - The sessionId information is obtained through GetChatSessionList.
        - You can also create a new session via the CreateChatSession interface.
        
        @param request: ChatRequest
        @return: ChatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.chat_with_options(request, headers, runtime)

    async def chat_async(
        self,
        request: energy_expert_external_20220923_models.ChatRequest,
    ) -> energy_expert_external_20220923_models.ChatResponse:
        """
        @summary Knowledge Base Q\\&A
        
        @description - The interface provides Q&A services within the scope of the selected directory in the session.
        - The sessionId information is obtained through GetChatSessionList.
        - You can also create a new session via the CreateChatSession interface.
        
        @param request: ChatRequest
        @return: ChatResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.chat_with_options_async(request, headers, runtime)

    def chat_stream_with_options(
        self,
        request: energy_expert_external_20220923_models.ChatStreamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.ChatStreamResponse:
        """
        @summary Knowledge Base Q&A
        
        @description - The interface provides Q&A services within the scope of the selected directory in the session.
        - The sessionId information is obtained through GetChatSessionList.
        - You can also create a new session via the CreateChatSession interface.
        
        @param request: ChatStreamRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatStreamResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.question):
            body['question'] = request.question
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChatStream',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/chat/stream',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.ChatStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_stream_with_options_async(
        self,
        request: energy_expert_external_20220923_models.ChatStreamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.ChatStreamResponse:
        """
        @summary Knowledge Base Q&A
        
        @description - The interface provides Q&A services within the scope of the selected directory in the session.
        - The sessionId information is obtained through GetChatSessionList.
        - You can also create a new session via the CreateChatSession interface.
        
        @param request: ChatStreamRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChatStreamResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.question):
            body['question'] = request.question
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChatStream',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/chat/stream',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.ChatStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_stream(
        self,
        request: energy_expert_external_20220923_models.ChatStreamRequest,
    ) -> energy_expert_external_20220923_models.ChatStreamResponse:
        """
        @summary Knowledge Base Q&A
        
        @description - The interface provides Q&A services within the scope of the selected directory in the session.
        - The sessionId information is obtained through GetChatSessionList.
        - You can also create a new session via the CreateChatSession interface.
        
        @param request: ChatStreamRequest
        @return: ChatStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.chat_stream_with_options(request, headers, runtime)

    async def chat_stream_async(
        self,
        request: energy_expert_external_20220923_models.ChatStreamRequest,
    ) -> energy_expert_external_20220923_models.ChatStreamResponse:
        """
        @summary Knowledge Base Q&A
        
        @description - The interface provides Q&A services within the scope of the selected directory in the session.
        - The sessionId information is obtained through GetChatSessionList.
        - You can also create a new session via the CreateChatSession interface.
        
        @param request: ChatStreamRequest
        @return: ChatStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.chat_stream_with_options_async(request, headers, runtime)

    def create_chat_session_with_options(
        self,
        request: energy_expert_external_20220923_models.CreateChatSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.CreateChatSessionResponse:
        """
        @summary Create Q&A Window
        
        @param request: CreateChatSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.folder_id):
            body['folderId'] = request.folder_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateChatSession',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/chat/session/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.CreateChatSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chat_session_with_options_async(
        self,
        request: energy_expert_external_20220923_models.CreateChatSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.CreateChatSessionResponse:
        """
        @summary Create Q&A Window
        
        @param request: CreateChatSessionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChatSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.folder_id):
            body['folderId'] = request.folder_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateChatSession',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/chat/session/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.CreateChatSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chat_session(
        self,
        request: energy_expert_external_20220923_models.CreateChatSessionRequest,
    ) -> energy_expert_external_20220923_models.CreateChatSessionResponse:
        """
        @summary Create Q&A Window
        
        @param request: CreateChatSessionRequest
        @return: CreateChatSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_chat_session_with_options(request, headers, runtime)

    async def create_chat_session_async(
        self,
        request: energy_expert_external_20220923_models.CreateChatSessionRequest,
    ) -> energy_expert_external_20220923_models.CreateChatSessionResponse:
        """
        @summary Create Q&A Window
        
        @param request: CreateChatSessionRequest
        @return: CreateChatSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_chat_session_with_options_async(request, headers, runtime)

    def delete_document_with_options(
        self,
        request: energy_expert_external_20220923_models.DeleteDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.DeleteDocumentResponse:
        """
        @summary 删除解析过的文件
        
        @param request: DeleteDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDocumentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDocument',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/aidoc/document/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.DeleteDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_document_with_options_async(
        self,
        request: energy_expert_external_20220923_models.DeleteDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.DeleteDocumentResponse:
        """
        @summary 删除解析过的文件
        
        @param request: DeleteDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDocumentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDocument',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/aidoc/document/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.DeleteDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_document(
        self,
        request: energy_expert_external_20220923_models.DeleteDocumentRequest,
    ) -> energy_expert_external_20220923_models.DeleteDocumentResponse:
        """
        @summary 删除解析过的文件
        
        @param request: DeleteDocumentRequest
        @return: DeleteDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_document_with_options(request, headers, runtime)

    async def delete_document_async(
        self,
        request: energy_expert_external_20220923_models.DeleteDocumentRequest,
    ) -> energy_expert_external_20220923_models.DeleteDocumentResponse:
        """
        @summary 删除解析过的文件
        
        @param request: DeleteDocumentRequest
        @return: DeleteDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_document_with_options_async(request, headers, runtime)

    def delete_folder_with_options(
        self,
        request: energy_expert_external_20220923_models.DeleteFolderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.DeleteFolderResponse:
        """
        @summary 删除文件夹
        
        @param request: DeleteFolderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFolderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['folderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFolder',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/aidoc/folder/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.DeleteFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_folder_with_options_async(
        self,
        request: energy_expert_external_20220923_models.DeleteFolderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.DeleteFolderResponse:
        """
        @summary 删除文件夹
        
        @param request: DeleteFolderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFolderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['folderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFolder',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/aidoc/folder/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.DeleteFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_folder(
        self,
        request: energy_expert_external_20220923_models.DeleteFolderRequest,
    ) -> energy_expert_external_20220923_models.DeleteFolderResponse:
        """
        @summary 删除文件夹
        
        @param request: DeleteFolderRequest
        @return: DeleteFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_folder_with_options(request, headers, runtime)

    async def delete_folder_async(
        self,
        request: energy_expert_external_20220923_models.DeleteFolderRequest,
    ) -> energy_expert_external_20220923_models.DeleteFolderResponse:
        """
        @summary 删除文件夹
        
        @param request: DeleteFolderRequest
        @return: DeleteFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_folder_with_options_async(request, headers, runtime)

    def detail_document_with_options(
        self,
        request: energy_expert_external_20220923_models.DetailDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.DetailDocumentResponse:
        """
        @summary 获取文档detail
        
        @param request: DetailDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetailDocumentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetailDocument',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/aidoc/document/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.DetailDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def detail_document_with_options_async(
        self,
        request: energy_expert_external_20220923_models.DetailDocumentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.DetailDocumentResponse:
        """
        @summary 获取文档detail
        
        @param request: DetailDocumentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetailDocumentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetailDocument',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/aidoc/document/detail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.DetailDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detail_document(
        self,
        request: energy_expert_external_20220923_models.DetailDocumentRequest,
    ) -> energy_expert_external_20220923_models.DetailDocumentResponse:
        """
        @summary 获取文档detail
        
        @param request: DetailDocumentRequest
        @return: DetailDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.detail_document_with_options(request, headers, runtime)

    async def detail_document_async(
        self,
        request: energy_expert_external_20220923_models.DetailDocumentRequest,
    ) -> energy_expert_external_20220923_models.DetailDocumentResponse:
        """
        @summary 获取文档detail
        
        @param request: DetailDocumentRequest
        @return: DetailDocumentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.detail_document_with_options_async(request, headers, runtime)

    def edit_prohibited_devices_with_options(
        self,
        request: energy_expert_external_20220923_models.EditProhibitedDevicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.EditProhibitedDevicesResponse:
        """
        @summary 编辑禁用设备
        
        @param request: EditProhibitedDevicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditProhibitedDevicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.factory_id):
            body['factoryId'] = request.factory_id
        if not UtilClient.is_unset(request.hvac_device_config_volist):
            body['hvacDeviceConfigVOList'] = request.hvac_device_config_volist
        if not UtilClient.is_unset(request.system_id):
            body['systemId'] = request.system_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EditProhibitedDevices',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/hvac/editProhibitedDevices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.EditProhibitedDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_prohibited_devices_with_options_async(
        self,
        request: energy_expert_external_20220923_models.EditProhibitedDevicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.EditProhibitedDevicesResponse:
        """
        @summary 编辑禁用设备
        
        @param request: EditProhibitedDevicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditProhibitedDevicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.factory_id):
            body['factoryId'] = request.factory_id
        if not UtilClient.is_unset(request.hvac_device_config_volist):
            body['hvacDeviceConfigVOList'] = request.hvac_device_config_volist
        if not UtilClient.is_unset(request.system_id):
            body['systemId'] = request.system_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EditProhibitedDevices',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/hvac/editProhibitedDevices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.EditProhibitedDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_prohibited_devices(
        self,
        request: energy_expert_external_20220923_models.EditProhibitedDevicesRequest,
    ) -> energy_expert_external_20220923_models.EditProhibitedDevicesResponse:
        """
        @summary 编辑禁用设备
        
        @param request: EditProhibitedDevicesRequest
        @return: EditProhibitedDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.edit_prohibited_devices_with_options(request, headers, runtime)

    async def edit_prohibited_devices_async(
        self,
        request: energy_expert_external_20220923_models.EditProhibitedDevicesRequest,
    ) -> energy_expert_external_20220923_models.EditProhibitedDevicesResponse:
        """
        @summary 编辑禁用设备
        
        @param request: EditProhibitedDevicesRequest
        @return: EditProhibitedDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.edit_prohibited_devices_with_options_async(request, headers, runtime)

    def edit_unfavorable_area_devices_with_options(
        self,
        request: energy_expert_external_20220923_models.EditUnfavorableAreaDevicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.EditUnfavorableAreaDevicesResponse:
        """
        @summary 编辑不利区设备
        
        @param request: EditUnfavorableAreaDevicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditUnfavorableAreaDevicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.factory_id):
            body['factoryId'] = request.factory_id
        if not UtilClient.is_unset(request.hvac_device_config_volist):
            body['hvacDeviceConfigVOList'] = request.hvac_device_config_volist
        if not UtilClient.is_unset(request.system_id):
            body['systemId'] = request.system_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EditUnfavorableAreaDevices',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/hvac/editUnfavorableAreaDevices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.EditUnfavorableAreaDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_unfavorable_area_devices_with_options_async(
        self,
        request: energy_expert_external_20220923_models.EditUnfavorableAreaDevicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.EditUnfavorableAreaDevicesResponse:
        """
        @summary 编辑不利区设备
        
        @param request: EditUnfavorableAreaDevicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditUnfavorableAreaDevicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.factory_id):
            body['factoryId'] = request.factory_id
        if not UtilClient.is_unset(request.hvac_device_config_volist):
            body['hvacDeviceConfigVOList'] = request.hvac_device_config_volist
        if not UtilClient.is_unset(request.system_id):
            body['systemId'] = request.system_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EditUnfavorableAreaDevices',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/hvac/editUnfavorableAreaDevices',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.EditUnfavorableAreaDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_unfavorable_area_devices(
        self,
        request: energy_expert_external_20220923_models.EditUnfavorableAreaDevicesRequest,
    ) -> energy_expert_external_20220923_models.EditUnfavorableAreaDevicesResponse:
        """
        @summary 编辑不利区设备
        
        @param request: EditUnfavorableAreaDevicesRequest
        @return: EditUnfavorableAreaDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.edit_unfavorable_area_devices_with_options(request, headers, runtime)

    async def edit_unfavorable_area_devices_async(
        self,
        request: energy_expert_external_20220923_models.EditUnfavorableAreaDevicesRequest,
    ) -> energy_expert_external_20220923_models.EditUnfavorableAreaDevicesResponse:
        """
        @summary 编辑不利区设备
        
        @param request: EditUnfavorableAreaDevicesRequest
        @return: EditUnfavorableAreaDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.edit_unfavorable_area_devices_with_options_async(request, headers, runtime)

    def generate_result_with_options(
        self,
        request: energy_expert_external_20220923_models.GenerateResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GenerateResultResponse:
        """
        @summary Generate a report of the specified carbon footprint.
        
        @description Given a product ID, this API initiates a task to calculate the carbon footprint result for the corresponding product. The task\\"s status can be checked using the `IsCompleted` API. Following the generation of results, other result inquiry APIs can be accessed for display content.
        
        @param request: GenerateResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateResult',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/generate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GenerateResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_result_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GenerateResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GenerateResultResponse:
        """
        @summary Generate a report of the specified carbon footprint.
        
        @description Given a product ID, this API initiates a task to calculate the carbon footprint result for the corresponding product. The task\\"s status can be checked using the `IsCompleted` API. Following the generation of results, other result inquiry APIs can be accessed for display content.
        
        @param request: GenerateResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateResult',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/generate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GenerateResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_result(
        self,
        request: energy_expert_external_20220923_models.GenerateResultRequest,
    ) -> energy_expert_external_20220923_models.GenerateResultResponse:
        """
        @summary Generate a report of the specified carbon footprint.
        
        @description Given a product ID, this API initiates a task to calculate the carbon footprint result for the corresponding product. The task\\"s status can be checked using the `IsCompleted` API. Following the generation of results, other result inquiry APIs can be accessed for display content.
        
        @param request: GenerateResultRequest
        @return: GenerateResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_result_with_options(request, headers, runtime)

    async def generate_result_async(
        self,
        request: energy_expert_external_20220923_models.GenerateResultRequest,
    ) -> energy_expert_external_20220923_models.GenerateResultResponse:
        """
        @summary Generate a report of the specified carbon footprint.
        
        @description Given a product ID, this API initiates a task to calculate the carbon footprint result for the corresponding product. The task\\"s status can be checked using the `IsCompleted` API. Following the generation of results, other result inquiry APIs can be accessed for display content.
        
        @param request: GenerateResultRequest
        @return: GenerateResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_result_with_options_async(request, headers, runtime)

    def get_area_elec_constitute_with_options(
        self,
        request: energy_expert_external_20220923_models.GetAreaElecConstituteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetAreaElecConstituteResponse:
        """
        @summary This interface is used to obtain electrical constitute analysis data.
        
        @param request: GetAreaElecConstituteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAreaElecConstituteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAreaElecConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/analysis/elec/area',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetAreaElecConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_area_elec_constitute_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetAreaElecConstituteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetAreaElecConstituteResponse:
        """
        @summary This interface is used to obtain electrical constitute analysis data.
        
        @param request: GetAreaElecConstituteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAreaElecConstituteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAreaElecConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/analysis/elec/area',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetAreaElecConstituteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_area_elec_constitute(
        self,
        request: energy_expert_external_20220923_models.GetAreaElecConstituteRequest,
    ) -> energy_expert_external_20220923_models.GetAreaElecConstituteResponse:
        """
        @summary This interface is used to obtain electrical constitute analysis data.
        
        @param request: GetAreaElecConstituteRequest
        @return: GetAreaElecConstituteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_area_elec_constitute_with_options(request, headers, runtime)

    async def get_area_elec_constitute_async(
        self,
        request: energy_expert_external_20220923_models.GetAreaElecConstituteRequest,
    ) -> energy_expert_external_20220923_models.GetAreaElecConstituteResponse:
        """
        @summary This interface is used to obtain electrical constitute analysis data.
        
        @param request: GetAreaElecConstituteRequest
        @return: GetAreaElecConstituteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_area_elec_constitute_with_options_async(request, headers, runtime)

    def get_carbon_emission_trend_with_options(
        self,
        request: energy_expert_external_20220923_models.GetCarbonEmissionTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetCarbonEmissionTrendResponse:
        """
        @summary Get trends in carbon emissions.
        
        @param request: GetCarbonEmissionTrendRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCarbonEmissionTrendResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.module_code):
            body['moduleCode'] = request.module_code
        if not UtilClient.is_unset(request.module_type):
            body['moduleType'] = request.module_type
        if not UtilClient.is_unset(request.trend_type):
            body['trendType'] = request.trend_type
        if not UtilClient.is_unset(request.year_list):
            body['yearList'] = request.year_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCarbonEmissionTrend',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/analysis/trend',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetCarbonEmissionTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_carbon_emission_trend_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetCarbonEmissionTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetCarbonEmissionTrendResponse:
        """
        @summary Get trends in carbon emissions.
        
        @param request: GetCarbonEmissionTrendRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCarbonEmissionTrendResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.module_code):
            body['moduleCode'] = request.module_code
        if not UtilClient.is_unset(request.module_type):
            body['moduleType'] = request.module_type
        if not UtilClient.is_unset(request.trend_type):
            body['trendType'] = request.trend_type
        if not UtilClient.is_unset(request.year_list):
            body['yearList'] = request.year_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCarbonEmissionTrend',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/analysis/trend',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetCarbonEmissionTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_carbon_emission_trend(
        self,
        request: energy_expert_external_20220923_models.GetCarbonEmissionTrendRequest,
    ) -> energy_expert_external_20220923_models.GetCarbonEmissionTrendResponse:
        """
        @summary Get trends in carbon emissions.
        
        @param request: GetCarbonEmissionTrendRequest
        @return: GetCarbonEmissionTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_carbon_emission_trend_with_options(request, headers, runtime)

    async def get_carbon_emission_trend_async(
        self,
        request: energy_expert_external_20220923_models.GetCarbonEmissionTrendRequest,
    ) -> energy_expert_external_20220923_models.GetCarbonEmissionTrendResponse:
        """
        @summary Get trends in carbon emissions.
        
        @param request: GetCarbonEmissionTrendRequest
        @return: GetCarbonEmissionTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_carbon_emission_trend_with_options_async(request, headers, runtime)

    def get_chat_folder_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetChatFolderListResponse:
        """
        @summary Get Q&A folder List
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatFolderListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetChatFolderList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/chat/folder/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetChatFolderListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_folder_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetChatFolderListResponse:
        """
        @summary Get Q&A folder List
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatFolderListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetChatFolderList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/chat/folder/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetChatFolderListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat_folder_list(self) -> energy_expert_external_20220923_models.GetChatFolderListResponse:
        """
        @summary Get Q&A folder List
        
        @return: GetChatFolderListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_chat_folder_list_with_options(headers, runtime)

    async def get_chat_folder_list_async(self) -> energy_expert_external_20220923_models.GetChatFolderListResponse:
        """
        @summary Get Q&A folder List
        
        @return: GetChatFolderListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_chat_folder_list_with_options_async(headers, runtime)

    def get_chat_list_with_options(
        self,
        request: energy_expert_external_20220923_models.GetChatListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetChatListResponse:
        """
        @summary Retrieve the historical documents of a session
        
        @description - This API retrieves the list of historical documents within a session by passing in the session ID.
        - The sessionId information is obtained through GetChatSessionList.
        - A new session can also be created using the CreateChatSession interface.
        
        @param request: GetChatListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetChatList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/chat/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetChatListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_list_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetChatListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetChatListResponse:
        """
        @summary Retrieve the historical documents of a session
        
        @description - This API retrieves the list of historical documents within a session by passing in the session ID.
        - The sessionId information is obtained through GetChatSessionList.
        - A new session can also be created using the CreateChatSession interface.
        
        @param request: GetChatListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetChatList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/chat/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetChatListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat_list(
        self,
        request: energy_expert_external_20220923_models.GetChatListRequest,
    ) -> energy_expert_external_20220923_models.GetChatListResponse:
        """
        @summary Retrieve the historical documents of a session
        
        @description - This API retrieves the list of historical documents within a session by passing in the session ID.
        - The sessionId information is obtained through GetChatSessionList.
        - A new session can also be created using the CreateChatSession interface.
        
        @param request: GetChatListRequest
        @return: GetChatListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_chat_list_with_options(request, headers, runtime)

    async def get_chat_list_async(
        self,
        request: energy_expert_external_20220923_models.GetChatListRequest,
    ) -> energy_expert_external_20220923_models.GetChatListResponse:
        """
        @summary Retrieve the historical documents of a session
        
        @description - This API retrieves the list of historical documents within a session by passing in the session ID.
        - The sessionId information is obtained through GetChatSessionList.
        - A new session can also be created using the CreateChatSession interface.
        
        @param request: GetChatListRequest
        @return: GetChatListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_chat_list_with_options_async(request, headers, runtime)

    def get_chat_session_list_with_options(
        self,
        request: energy_expert_external_20220923_models.GetChatSessionListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetChatSessionListResponse:
        """
        @summary Get Q&A Session List
        
        @param request: GetChatSessionListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatSessionListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetChatSessionList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/chat/session/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetChatSessionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_session_list_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetChatSessionListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetChatSessionListResponse:
        """
        @summary Get Q&A Session List
        
        @param request: GetChatSessionListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatSessionListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetChatSessionList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/chat/session/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetChatSessionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat_session_list(
        self,
        request: energy_expert_external_20220923_models.GetChatSessionListRequest,
    ) -> energy_expert_external_20220923_models.GetChatSessionListResponse:
        """
        @summary Get Q&A Session List
        
        @param request: GetChatSessionListRequest
        @return: GetChatSessionListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_chat_session_list_with_options(request, headers, runtime)

    async def get_chat_session_list_async(
        self,
        request: energy_expert_external_20220923_models.GetChatSessionListRequest,
    ) -> energy_expert_external_20220923_models.GetChatSessionListResponse:
        """
        @summary Get Q&A Session List
        
        @param request: GetChatSessionListRequest
        @return: GetChatSessionListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_chat_session_list_with_options_async(request, headers, runtime)

    def get_data_item_list_with_options(
        self,
        request: energy_expert_external_20220923_models.GetDataItemListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDataItemListResponse:
        """
        @summary This interface is used to obtain the details category of a data item.
        
        @description - obtain data item detail list under the current enterprise.
        
        @param request: GetDataItemListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataItemListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataItemList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/data/item/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDataItemListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_item_list_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetDataItemListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDataItemListResponse:
        """
        @summary This interface is used to obtain the details category of a data item.
        
        @description - obtain data item detail list under the current enterprise.
        
        @param request: GetDataItemListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataItemListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataItemList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/data/item/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDataItemListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_item_list(
        self,
        request: energy_expert_external_20220923_models.GetDataItemListRequest,
    ) -> energy_expert_external_20220923_models.GetDataItemListResponse:
        """
        @summary This interface is used to obtain the details category of a data item.
        
        @description - obtain data item detail list under the current enterprise.
        
        @param request: GetDataItemListRequest
        @return: GetDataItemListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_data_item_list_with_options(request, headers, runtime)

    async def get_data_item_list_async(
        self,
        request: energy_expert_external_20220923_models.GetDataItemListRequest,
    ) -> energy_expert_external_20220923_models.GetDataItemListResponse:
        """
        @summary This interface is used to obtain the details category of a data item.
        
        @description - obtain data item detail list under the current enterprise.
        
        @param request: GetDataItemListRequest
        @return: GetDataItemListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_data_item_list_with_options_async(request, headers, runtime)

    def get_data_quality_analysis_with_options(
        self,
        request: energy_expert_external_20220923_models.GetDataQualityAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDataQualityAnalysisResponse:
        """
        @summary Obtain the data quality evaluation results DQR and DQI.
        
        @description This API returns the data quality evaluation results based on the user-provided product ID. It\\"s useful for understanding the data quality of the carbon emission factors for each inventory of the product.
        
        @param request: GetDataQualityAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataQualityAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.data_quality_evaluation_type):
            body['dataQualityEvaluationType'] = request.data_quality_evaluation_type
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataQualityAnalysis',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/data/quality/analysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDataQualityAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_quality_analysis_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetDataQualityAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDataQualityAnalysisResponse:
        """
        @summary Obtain the data quality evaluation results DQR and DQI.
        
        @description This API returns the data quality evaluation results based on the user-provided product ID. It\\"s useful for understanding the data quality of the carbon emission factors for each inventory of the product.
        
        @param request: GetDataQualityAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataQualityAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.data_quality_evaluation_type):
            body['dataQualityEvaluationType'] = request.data_quality_evaluation_type
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataQualityAnalysis',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/data/quality/analysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDataQualityAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_quality_analysis(
        self,
        request: energy_expert_external_20220923_models.GetDataQualityAnalysisRequest,
    ) -> energy_expert_external_20220923_models.GetDataQualityAnalysisResponse:
        """
        @summary Obtain the data quality evaluation results DQR and DQI.
        
        @description This API returns the data quality evaluation results based on the user-provided product ID. It\\"s useful for understanding the data quality of the carbon emission factors for each inventory of the product.
        
        @param request: GetDataQualityAnalysisRequest
        @return: GetDataQualityAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_data_quality_analysis_with_options(request, headers, runtime)

    async def get_data_quality_analysis_async(
        self,
        request: energy_expert_external_20220923_models.GetDataQualityAnalysisRequest,
    ) -> energy_expert_external_20220923_models.GetDataQualityAnalysisResponse:
        """
        @summary Obtain the data quality evaluation results DQR and DQI.
        
        @description This API returns the data quality evaluation results based on the user-provided product ID. It\\"s useful for understanding the data quality of the carbon emission factors for each inventory of the product.
        
        @param request: GetDataQualityAnalysisRequest
        @return: GetDataQualityAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_data_quality_analysis_with_options_async(request, headers, runtime)

    def get_device_info_with_options(
        self,
        request: energy_expert_external_20220923_models.GetDeviceInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDeviceInfoResponse:
        """
        @summary Queries the information about a device at a site that is activated by using an Alibaba Cloud account.
        
        @description    You can call this operation to query the parameters of a data collection device based on the device ID. If the verification is passed, the device parameters are returned. If the verification fails, a null value is returned.
        You can query the parameters of a single device by day. If data of the device does not exist, a null value is returned.
        - By current, endpoint only supports Hangzhou: `energyexpertexternal.cn-hangzhou.aliyuncs.com`.
        - To use this API, you need to be added to the whitelist. Please contact us through  <props="china">[official website](https://energy.aliyun.com/ifa/web/defaultLoginPage?adapter=aliyun#/consult?source=%E8%83%BD%E8%80%97%E5%AE%9D%E7%99%BB%E5%BD%95%E9%A1%B5%EF%BC%88WEB%EF%BC%89)
        <props="intl">[official website](https://energy.alibabacloud.com/common?adapter=aliyun&lang=en-US#/home/en) to apply for whitelist activation.
        
        @param request: GetDeviceInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['deviceId'] = request.device_id
        if not UtilClient.is_unset(request.ds):
            query['ds'] = request.ds
        if not UtilClient.is_unset(request.factory_id):
            query['factoryId'] = request.factory_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceInfo',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/external/getDeviceInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_info_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetDeviceInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDeviceInfoResponse:
        """
        @summary Queries the information about a device at a site that is activated by using an Alibaba Cloud account.
        
        @description    You can call this operation to query the parameters of a data collection device based on the device ID. If the verification is passed, the device parameters are returned. If the verification fails, a null value is returned.
        You can query the parameters of a single device by day. If data of the device does not exist, a null value is returned.
        - By current, endpoint only supports Hangzhou: `energyexpertexternal.cn-hangzhou.aliyuncs.com`.
        - To use this API, you need to be added to the whitelist. Please contact us through  <props="china">[official website](https://energy.aliyun.com/ifa/web/defaultLoginPage?adapter=aliyun#/consult?source=%E8%83%BD%E8%80%97%E5%AE%9D%E7%99%BB%E5%BD%95%E9%A1%B5%EF%BC%88WEB%EF%BC%89)
        <props="intl">[official website](https://energy.alibabacloud.com/common?adapter=aliyun&lang=en-US#/home/en) to apply for whitelist activation.
        
        @param request: GetDeviceInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['deviceId'] = request.device_id
        if not UtilClient.is_unset(request.ds):
            query['ds'] = request.ds
        if not UtilClient.is_unset(request.factory_id):
            query['factoryId'] = request.factory_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceInfo',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/external/getDeviceInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDeviceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_info(
        self,
        request: energy_expert_external_20220923_models.GetDeviceInfoRequest,
    ) -> energy_expert_external_20220923_models.GetDeviceInfoResponse:
        """
        @summary Queries the information about a device at a site that is activated by using an Alibaba Cloud account.
        
        @description    You can call this operation to query the parameters of a data collection device based on the device ID. If the verification is passed, the device parameters are returned. If the verification fails, a null value is returned.
        You can query the parameters of a single device by day. If data of the device does not exist, a null value is returned.
        - By current, endpoint only supports Hangzhou: `energyexpertexternal.cn-hangzhou.aliyuncs.com`.
        - To use this API, you need to be added to the whitelist. Please contact us through  <props="china">[official website](https://energy.aliyun.com/ifa/web/defaultLoginPage?adapter=aliyun#/consult?source=%E8%83%BD%E8%80%97%E5%AE%9D%E7%99%BB%E5%BD%95%E9%A1%B5%EF%BC%88WEB%EF%BC%89)
        <props="intl">[official website](https://energy.alibabacloud.com/common?adapter=aliyun&lang=en-US#/home/en) to apply for whitelist activation.
        
        @param request: GetDeviceInfoRequest
        @return: GetDeviceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_device_info_with_options(request, headers, runtime)

    async def get_device_info_async(
        self,
        request: energy_expert_external_20220923_models.GetDeviceInfoRequest,
    ) -> energy_expert_external_20220923_models.GetDeviceInfoResponse:
        """
        @summary Queries the information about a device at a site that is activated by using an Alibaba Cloud account.
        
        @description    You can call this operation to query the parameters of a data collection device based on the device ID. If the verification is passed, the device parameters are returned. If the verification fails, a null value is returned.
        You can query the parameters of a single device by day. If data of the device does not exist, a null value is returned.
        - By current, endpoint only supports Hangzhou: `energyexpertexternal.cn-hangzhou.aliyuncs.com`.
        - To use this API, you need to be added to the whitelist. Please contact us through  <props="china">[official website](https://energy.aliyun.com/ifa/web/defaultLoginPage?adapter=aliyun#/consult?source=%E8%83%BD%E8%80%97%E5%AE%9D%E7%99%BB%E5%BD%95%E9%A1%B5%EF%BC%88WEB%EF%BC%89)
        <props="intl">[official website](https://energy.alibabacloud.com/common?adapter=aliyun&lang=en-US#/home/en) to apply for whitelist activation.
        
        @param request: GetDeviceInfoRequest
        @return: GetDeviceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_device_info_with_options_async(request, headers, runtime)

    def get_device_list_with_options(
        self,
        request: energy_expert_external_20220923_models.GetDeviceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDeviceListResponse:
        """
        @summary Queries the devices of a site that is activated by using an Alibaba Cloud account.
        
        @description    You can query the information about data collection devices of a site based on the ID of the site. If the verification is passed, the information about the devices of the site is returned. If the verification fails, a null value is returned.
        Virtual meters at the site are not returned.
        - By current, endpoint only supports Hangzhou: `energyexpertexternal.cn-hangzhou.aliyuncs.com`.
        - To use this API, you need to be added to the whitelist. Please contact us through  <props="china">[official website](https://energy.aliyun.com/ifa/web/defaultLoginPage?adapter=aliyun#/consult?source=%E8%83%BD%E8%80%97%E5%AE%9D%E7%99%BB%E5%BD%95%E9%A1%B5%EF%BC%88WEB%EF%BC%89)
        <props="intl">[official website](https://energy.alibabacloud.com/common?adapter=aliyun&lang=en-US#/home/en) to apply for whitelist activation.
        
        @param request: GetDeviceListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.factory_id):
            query['factoryId'] = request.factory_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/external/getDeviceList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDeviceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_list_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetDeviceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDeviceListResponse:
        """
        @summary Queries the devices of a site that is activated by using an Alibaba Cloud account.
        
        @description    You can query the information about data collection devices of a site based on the ID of the site. If the verification is passed, the information about the devices of the site is returned. If the verification fails, a null value is returned.
        Virtual meters at the site are not returned.
        - By current, endpoint only supports Hangzhou: `energyexpertexternal.cn-hangzhou.aliyuncs.com`.
        - To use this API, you need to be added to the whitelist. Please contact us through  <props="china">[official website](https://energy.aliyun.com/ifa/web/defaultLoginPage?adapter=aliyun#/consult?source=%E8%83%BD%E8%80%97%E5%AE%9D%E7%99%BB%E5%BD%95%E9%A1%B5%EF%BC%88WEB%EF%BC%89)
        <props="intl">[official website](https://energy.alibabacloud.com/common?adapter=aliyun&lang=en-US#/home/en) to apply for whitelist activation.
        
        @param request: GetDeviceListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeviceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.factory_id):
            query['factoryId'] = request.factory_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/external/getDeviceList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDeviceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_list(
        self,
        request: energy_expert_external_20220923_models.GetDeviceListRequest,
    ) -> energy_expert_external_20220923_models.GetDeviceListResponse:
        """
        @summary Queries the devices of a site that is activated by using an Alibaba Cloud account.
        
        @description    You can query the information about data collection devices of a site based on the ID of the site. If the verification is passed, the information about the devices of the site is returned. If the verification fails, a null value is returned.
        Virtual meters at the site are not returned.
        - By current, endpoint only supports Hangzhou: `energyexpertexternal.cn-hangzhou.aliyuncs.com`.
        - To use this API, you need to be added to the whitelist. Please contact us through  <props="china">[official website](https://energy.aliyun.com/ifa/web/defaultLoginPage?adapter=aliyun#/consult?source=%E8%83%BD%E8%80%97%E5%AE%9D%E7%99%BB%E5%BD%95%E9%A1%B5%EF%BC%88WEB%EF%BC%89)
        <props="intl">[official website](https://energy.alibabacloud.com/common?adapter=aliyun&lang=en-US#/home/en) to apply for whitelist activation.
        
        @param request: GetDeviceListRequest
        @return: GetDeviceListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_device_list_with_options(request, headers, runtime)

    async def get_device_list_async(
        self,
        request: energy_expert_external_20220923_models.GetDeviceListRequest,
    ) -> energy_expert_external_20220923_models.GetDeviceListResponse:
        """
        @summary Queries the devices of a site that is activated by using an Alibaba Cloud account.
        
        @description    You can query the information about data collection devices of a site based on the ID of the site. If the verification is passed, the information about the devices of the site is returned. If the verification fails, a null value is returned.
        Virtual meters at the site are not returned.
        - By current, endpoint only supports Hangzhou: `energyexpertexternal.cn-hangzhou.aliyuncs.com`.
        - To use this API, you need to be added to the whitelist. Please contact us through  <props="china">[official website](https://energy.aliyun.com/ifa/web/defaultLoginPage?adapter=aliyun#/consult?source=%E8%83%BD%E8%80%97%E5%AE%9D%E7%99%BB%E5%BD%95%E9%A1%B5%EF%BC%88WEB%EF%BC%89)
        <props="intl">[official website](https://energy.alibabacloud.com/common?adapter=aliyun&lang=en-US#/home/en) to apply for whitelist activation.
        
        @param request: GetDeviceListRequest
        @return: GetDeviceListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_device_list_with_options_async(request, headers, runtime)

    def get_doc_extraction_result_with_options(
        self,
        request: energy_expert_external_20220923_models.GetDocExtractionResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDocExtractionResultResponse:
        """
        @summary For Querying Information Extraction Result.
        The input parameter taskId is obtained from the taskId returned by the interfaces SubmitDocExtractionTaskAdvance or SubmitDocExtractionTask.
        The query results can reflect one of three statuses: processing, successfully completed, or failed.
        
        @param request: GetDocExtractionResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocExtractionResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocExtractionResult',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/getDocExtractionResult',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDocExtractionResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doc_extraction_result_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetDocExtractionResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDocExtractionResultResponse:
        """
        @summary For Querying Information Extraction Result.
        The input parameter taskId is obtained from the taskId returned by the interfaces SubmitDocExtractionTaskAdvance or SubmitDocExtractionTask.
        The query results can reflect one of three statuses: processing, successfully completed, or failed.
        
        @param request: GetDocExtractionResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocExtractionResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocExtractionResult',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/getDocExtractionResult',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDocExtractionResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doc_extraction_result(
        self,
        request: energy_expert_external_20220923_models.GetDocExtractionResultRequest,
    ) -> energy_expert_external_20220923_models.GetDocExtractionResultResponse:
        """
        @summary For Querying Information Extraction Result.
        The input parameter taskId is obtained from the taskId returned by the interfaces SubmitDocExtractionTaskAdvance or SubmitDocExtractionTask.
        The query results can reflect one of three statuses: processing, successfully completed, or failed.
        
        @param request: GetDocExtractionResultRequest
        @return: GetDocExtractionResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_doc_extraction_result_with_options(request, headers, runtime)

    async def get_doc_extraction_result_async(
        self,
        request: energy_expert_external_20220923_models.GetDocExtractionResultRequest,
    ) -> energy_expert_external_20220923_models.GetDocExtractionResultResponse:
        """
        @summary For Querying Information Extraction Result.
        The input parameter taskId is obtained from the taskId returned by the interfaces SubmitDocExtractionTaskAdvance or SubmitDocExtractionTask.
        The query results can reflect one of three statuses: processing, successfully completed, or failed.
        
        @param request: GetDocExtractionResultRequest
        @return: GetDocExtractionResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_doc_extraction_result_with_options_async(request, headers, runtime)

    def get_doc_parsing_result_with_options(
        self,
        request: energy_expert_external_20220923_models.GetDocParsingResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDocParsingResultResponse:
        """
        @summary For Querying Document Parsing Results.
        The input parameter taskId is obtained from the taskId returned by the interfaces SubmitDocParsingTaskAdvance or SubmitDocParsingTask.
        The query results can be one of three statuses: processing, successful, or failed.
        
        @param request: GetDocParsingResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocParsingResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.return_format):
            body['returnFormat'] = request.return_format
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocParsingResult',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/getDocParsingResult',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDocParsingResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doc_parsing_result_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetDocParsingResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDocParsingResultResponse:
        """
        @summary For Querying Document Parsing Results.
        The input parameter taskId is obtained from the taskId returned by the interfaces SubmitDocParsingTaskAdvance or SubmitDocParsingTask.
        The query results can be one of three statuses: processing, successful, or failed.
        
        @param request: GetDocParsingResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocParsingResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.return_format):
            body['returnFormat'] = request.return_format
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocParsingResult',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/getDocParsingResult',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDocParsingResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doc_parsing_result(
        self,
        request: energy_expert_external_20220923_models.GetDocParsingResultRequest,
    ) -> energy_expert_external_20220923_models.GetDocParsingResultResponse:
        """
        @summary For Querying Document Parsing Results.
        The input parameter taskId is obtained from the taskId returned by the interfaces SubmitDocParsingTaskAdvance or SubmitDocParsingTask.
        The query results can be one of three statuses: processing, successful, or failed.
        
        @param request: GetDocParsingResultRequest
        @return: GetDocParsingResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_doc_parsing_result_with_options(request, headers, runtime)

    async def get_doc_parsing_result_async(
        self,
        request: energy_expert_external_20220923_models.GetDocParsingResultRequest,
    ) -> energy_expert_external_20220923_models.GetDocParsingResultResponse:
        """
        @summary For Querying Document Parsing Results.
        The input parameter taskId is obtained from the taskId returned by the interfaces SubmitDocParsingTaskAdvance or SubmitDocParsingTask.
        The query results can be one of three statuses: processing, successful, or failed.
        
        @param request: GetDocParsingResultRequest
        @return: GetDocParsingResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_doc_parsing_result_with_options_async(request, headers, runtime)

    def get_document_analyze_result_with_options(
        self,
        request: energy_expert_external_20220923_models.GetDocumentAnalyzeResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDocumentAnalyzeResultResponse:
        """
        @summary [Important] The api is no longer maintained, please use GetDocExtractionResult, GetVLExtractionResult to get the extraction results.
        
        @param request: GetDocumentAnalyzeResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentAnalyzeResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['jobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocumentAnalyzeResult',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/aidoc/document/getDocumentAnalyzeResult',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDocumentAnalyzeResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_document_analyze_result_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetDocumentAnalyzeResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetDocumentAnalyzeResultResponse:
        """
        @summary [Important] The api is no longer maintained, please use GetDocExtractionResult, GetVLExtractionResult to get the extraction results.
        
        @param request: GetDocumentAnalyzeResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDocumentAnalyzeResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['jobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDocumentAnalyzeResult',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/aidoc/document/getDocumentAnalyzeResult',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetDocumentAnalyzeResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_document_analyze_result(
        self,
        request: energy_expert_external_20220923_models.GetDocumentAnalyzeResultRequest,
    ) -> energy_expert_external_20220923_models.GetDocumentAnalyzeResultResponse:
        """
        @summary [Important] The api is no longer maintained, please use GetDocExtractionResult, GetVLExtractionResult to get the extraction results.
        
        @param request: GetDocumentAnalyzeResultRequest
        @return: GetDocumentAnalyzeResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_document_analyze_result_with_options(request, headers, runtime)

    async def get_document_analyze_result_async(
        self,
        request: energy_expert_external_20220923_models.GetDocumentAnalyzeResultRequest,
    ) -> energy_expert_external_20220923_models.GetDocumentAnalyzeResultResponse:
        """
        @summary [Important] The api is no longer maintained, please use GetDocExtractionResult, GetVLExtractionResult to get the extraction results.
        
        @param request: GetDocumentAnalyzeResultRequest
        @return: GetDocumentAnalyzeResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_document_analyze_result_with_options_async(request, headers, runtime)

    def get_elec_constitute_with_options(
        self,
        request: energy_expert_external_20220923_models.GetElecConstituteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetElecConstituteResponse:
        """
        @summary This interface is used to obtain power composition analysis data.
        
        @param request: GetElecConstituteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetElecConstituteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetElecConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/analysis/elec/constitute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetElecConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_elec_constitute_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetElecConstituteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetElecConstituteResponse:
        """
        @summary This interface is used to obtain power composition analysis data.
        
        @param request: GetElecConstituteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetElecConstituteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetElecConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/analysis/elec/constitute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetElecConstituteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_elec_constitute(
        self,
        request: energy_expert_external_20220923_models.GetElecConstituteRequest,
    ) -> energy_expert_external_20220923_models.GetElecConstituteResponse:
        """
        @summary This interface is used to obtain power composition analysis data.
        
        @param request: GetElecConstituteRequest
        @return: GetElecConstituteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_elec_constitute_with_options(request, headers, runtime)

    async def get_elec_constitute_async(
        self,
        request: energy_expert_external_20220923_models.GetElecConstituteRequest,
    ) -> energy_expert_external_20220923_models.GetElecConstituteResponse:
        """
        @summary This interface is used to obtain power composition analysis data.
        
        @param request: GetElecConstituteRequest
        @return: GetElecConstituteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_elec_constitute_with_options_async(request, headers, runtime)

    def get_elec_trend_with_options(
        self,
        request: energy_expert_external_20220923_models.GetElecTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetElecTrendResponse:
        """
        @summary This interface is used to obtain power trend analysis data.
        
        @param request: GetElecTrendRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetElecTrendResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.year_list):
            body['yearList'] = request.year_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetElecTrend',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/analysis/elec/trend',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetElecTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_elec_trend_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetElecTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetElecTrendResponse:
        """
        @summary This interface is used to obtain power trend analysis data.
        
        @param request: GetElecTrendRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetElecTrendResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.year_list):
            body['yearList'] = request.year_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetElecTrend',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/analysis/elec/trend',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetElecTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_elec_trend(
        self,
        request: energy_expert_external_20220923_models.GetElecTrendRequest,
    ) -> energy_expert_external_20220923_models.GetElecTrendResponse:
        """
        @summary This interface is used to obtain power trend analysis data.
        
        @param request: GetElecTrendRequest
        @return: GetElecTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_elec_trend_with_options(request, headers, runtime)

    async def get_elec_trend_async(
        self,
        request: energy_expert_external_20220923_models.GetElecTrendRequest,
    ) -> energy_expert_external_20220923_models.GetElecTrendResponse:
        """
        @summary This interface is used to obtain power trend analysis data.
        
        @param request: GetElecTrendRequest
        @return: GetElecTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_elec_trend_with_options_async(request, headers, runtime)

    def get_emission_source_constitute_with_options(
        self,
        request: energy_expert_external_20220923_models.GetEmissionSourceConstituteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetEmissionSourceConstituteResponse:
        """
        @summary Obtain the emission source composition.
        
        @param request: GetEmissionSourceConstituteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEmissionSourceConstituteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.module_code):
            body['moduleCode'] = request.module_code
        if not UtilClient.is_unset(request.module_type):
            body['moduleType'] = request.module_type
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEmissionSourceConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/analysis/constitute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetEmissionSourceConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_emission_source_constitute_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetEmissionSourceConstituteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetEmissionSourceConstituteResponse:
        """
        @summary Obtain the emission source composition.
        
        @param request: GetEmissionSourceConstituteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEmissionSourceConstituteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.module_code):
            body['moduleCode'] = request.module_code
        if not UtilClient.is_unset(request.module_type):
            body['moduleType'] = request.module_type
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEmissionSourceConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/analysis/constitute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetEmissionSourceConstituteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_emission_source_constitute(
        self,
        request: energy_expert_external_20220923_models.GetEmissionSourceConstituteRequest,
    ) -> energy_expert_external_20220923_models.GetEmissionSourceConstituteResponse:
        """
        @summary Obtain the emission source composition.
        
        @param request: GetEmissionSourceConstituteRequest
        @return: GetEmissionSourceConstituteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_emission_source_constitute_with_options(request, headers, runtime)

    async def get_emission_source_constitute_async(
        self,
        request: energy_expert_external_20220923_models.GetEmissionSourceConstituteRequest,
    ) -> energy_expert_external_20220923_models.GetEmissionSourceConstituteResponse:
        """
        @summary Obtain the emission source composition.
        
        @param request: GetEmissionSourceConstituteRequest
        @return: GetEmissionSourceConstituteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_emission_source_constitute_with_options_async(request, headers, runtime)

    def get_emission_summary_with_options(
        self,
        request: energy_expert_external_20220923_models.GetEmissionSummaryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetEmissionSummaryResponse:
        """
        @summary Get a summary of carbon emissions.
        
        @param request: GetEmissionSummaryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEmissionSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.module_code):
            body['moduleCode'] = request.module_code
        if not UtilClient.is_unset(request.module_type):
            body['moduleType'] = request.module_type
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEmissionSummary',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/analysis/summary',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetEmissionSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_emission_summary_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetEmissionSummaryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetEmissionSummaryResponse:
        """
        @summary Get a summary of carbon emissions.
        
        @param request: GetEmissionSummaryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEmissionSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.module_code):
            body['moduleCode'] = request.module_code
        if not UtilClient.is_unset(request.module_type):
            body['moduleType'] = request.module_type
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEmissionSummary',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/analysis/summary',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetEmissionSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_emission_summary(
        self,
        request: energy_expert_external_20220923_models.GetEmissionSummaryRequest,
    ) -> energy_expert_external_20220923_models.GetEmissionSummaryResponse:
        """
        @summary Get a summary of carbon emissions.
        
        @param request: GetEmissionSummaryRequest
        @return: GetEmissionSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_emission_summary_with_options(request, headers, runtime)

    async def get_emission_summary_async(
        self,
        request: energy_expert_external_20220923_models.GetEmissionSummaryRequest,
    ) -> energy_expert_external_20220923_models.GetEmissionSummaryResponse:
        """
        @summary Get a summary of carbon emissions.
        
        @param request: GetEmissionSummaryRequest
        @return: GetEmissionSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_emission_summary_with_options_async(request, headers, runtime)

    def get_epd_inventory_constitute_with_options(
        self,
        request: energy_expert_external_20220923_models.GetEpdInventoryConstituteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetEpdInventoryConstituteResponse:
        """
        @summary Gets the result details of the environmental impact category.
        
        @description This API returns the emission amounts for various environmental impact categories at different levels for the given product ID. It helps understand the emission quantities for different environmental impact categories and inventories of the product.
        
        @param request: GetEpdInventoryConstituteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEpdInventoryConstituteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEpdInventoryConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/epd/inventory/constitute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetEpdInventoryConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_epd_inventory_constitute_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetEpdInventoryConstituteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetEpdInventoryConstituteResponse:
        """
        @summary Gets the result details of the environmental impact category.
        
        @description This API returns the emission amounts for various environmental impact categories at different levels for the given product ID. It helps understand the emission quantities for different environmental impact categories and inventories of the product.
        
        @param request: GetEpdInventoryConstituteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEpdInventoryConstituteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEpdInventoryConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/epd/inventory/constitute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetEpdInventoryConstituteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_epd_inventory_constitute(
        self,
        request: energy_expert_external_20220923_models.GetEpdInventoryConstituteRequest,
    ) -> energy_expert_external_20220923_models.GetEpdInventoryConstituteResponse:
        """
        @summary Gets the result details of the environmental impact category.
        
        @description This API returns the emission amounts for various environmental impact categories at different levels for the given product ID. It helps understand the emission quantities for different environmental impact categories and inventories of the product.
        
        @param request: GetEpdInventoryConstituteRequest
        @return: GetEpdInventoryConstituteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_epd_inventory_constitute_with_options(request, headers, runtime)

    async def get_epd_inventory_constitute_async(
        self,
        request: energy_expert_external_20220923_models.GetEpdInventoryConstituteRequest,
    ) -> energy_expert_external_20220923_models.GetEpdInventoryConstituteResponse:
        """
        @summary Gets the result details of the environmental impact category.
        
        @description This API returns the emission amounts for various environmental impact categories at different levels for the given product ID. It helps understand the emission quantities for different environmental impact categories and inventories of the product.
        
        @param request: GetEpdInventoryConstituteRequest
        @return: GetEpdInventoryConstituteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_epd_inventory_constitute_with_options_async(request, headers, runtime)

    def get_epd_summary_with_options(
        self,
        request: energy_expert_external_20220923_models.GetEpdSummaryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetEpdSummaryResponse:
        """
        @summary Obtain the total amount of emissions for various environmental impacts.
        
        @description This API takes a product ID from the user and returns the summary of environmental impact generated for the product. This info helps understand the overall emissions for different environmental impact categories of the product.
        
        @param request: GetEpdSummaryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEpdSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEpdSummary',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/epd/summary',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetEpdSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_epd_summary_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetEpdSummaryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetEpdSummaryResponse:
        """
        @summary Obtain the total amount of emissions for various environmental impacts.
        
        @description This API takes a product ID from the user and returns the summary of environmental impact generated for the product. This info helps understand the overall emissions for different environmental impact categories of the product.
        
        @param request: GetEpdSummaryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEpdSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEpdSummary',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/epd/summary',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetEpdSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_epd_summary(
        self,
        request: energy_expert_external_20220923_models.GetEpdSummaryRequest,
    ) -> energy_expert_external_20220923_models.GetEpdSummaryResponse:
        """
        @summary Obtain the total amount of emissions for various environmental impacts.
        
        @description This API takes a product ID from the user and returns the summary of environmental impact generated for the product. This info helps understand the overall emissions for different environmental impact categories of the product.
        
        @param request: GetEpdSummaryRequest
        @return: GetEpdSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_epd_summary_with_options(request, headers, runtime)

    async def get_epd_summary_async(
        self,
        request: energy_expert_external_20220923_models.GetEpdSummaryRequest,
    ) -> energy_expert_external_20220923_models.GetEpdSummaryResponse:
        """
        @summary Obtain the total amount of emissions for various environmental impacts.
        
        @description This API takes a product ID from the user and returns the summary of environmental impact generated for the product. This info helps understand the overall emissions for different environmental impact categories of the product.
        
        @param request: GetEpdSummaryRequest
        @return: GetEpdSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_epd_summary_with_options_async(request, headers, runtime)

    def get_footprint_list_with_options(
        self,
        request: energy_expert_external_20220923_models.GetFootprintListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetFootprintListResponse:
        """
        @summary Get the list of product carbon footprints.
        
        @description With user-specified parameters such as enterprise code, current page, and page size, this API returns a list of matching product carbon footprints (or supply chain carbon footprints), including product names and product IDs. The product ID can be used as input parameters in other APIs to get the corresponding product\\"s detailed information.
        
        @param request: GetFootprintListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFootprintListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.current_page):
            body['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFootprintList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/product/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetFootprintListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_footprint_list_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetFootprintListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetFootprintListResponse:
        """
        @summary Get the list of product carbon footprints.
        
        @description With user-specified parameters such as enterprise code, current page, and page size, this API returns a list of matching product carbon footprints (or supply chain carbon footprints), including product names and product IDs. The product ID can be used as input parameters in other APIs to get the corresponding product\\"s detailed information.
        
        @param request: GetFootprintListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFootprintListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.current_page):
            body['currentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFootprintList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/product/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetFootprintListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_footprint_list(
        self,
        request: energy_expert_external_20220923_models.GetFootprintListRequest,
    ) -> energy_expert_external_20220923_models.GetFootprintListResponse:
        """
        @summary Get the list of product carbon footprints.
        
        @description With user-specified parameters such as enterprise code, current page, and page size, this API returns a list of matching product carbon footprints (or supply chain carbon footprints), including product names and product IDs. The product ID can be used as input parameters in other APIs to get the corresponding product\\"s detailed information.
        
        @param request: GetFootprintListRequest
        @return: GetFootprintListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_footprint_list_with_options(request, headers, runtime)

    async def get_footprint_list_async(
        self,
        request: energy_expert_external_20220923_models.GetFootprintListRequest,
    ) -> energy_expert_external_20220923_models.GetFootprintListResponse:
        """
        @summary Get the list of product carbon footprints.
        
        @description With user-specified parameters such as enterprise code, current page, and page size, this API returns a list of matching product carbon footprints (or supply chain carbon footprints), including product names and product IDs. The product ID can be used as input parameters in other APIs to get the corresponding product\\"s detailed information.
        
        @param request: GetFootprintListRequest
        @return: GetFootprintListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_footprint_list_with_options_async(request, headers, runtime)

    def get_gas_constitute_with_options(
        self,
        request: energy_expert_external_20220923_models.GetGasConstituteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetGasConstituteResponse:
        """
        @summary This interface is used to obtain gas composition analysis.
        
        @param request: GetGasConstituteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGasConstituteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.module_code):
            body['moduleCode'] = request.module_code
        if not UtilClient.is_unset(request.module_type):
            body['moduleType'] = request.module_type
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGasConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/analysis/gas/constitute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetGasConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gas_constitute_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetGasConstituteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetGasConstituteResponse:
        """
        @summary This interface is used to obtain gas composition analysis.
        
        @param request: GetGasConstituteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGasConstituteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.module_code):
            body['moduleCode'] = request.module_code
        if not UtilClient.is_unset(request.module_type):
            body['moduleType'] = request.module_type
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGasConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/analysis/gas/constitute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetGasConstituteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gas_constitute(
        self,
        request: energy_expert_external_20220923_models.GetGasConstituteRequest,
    ) -> energy_expert_external_20220923_models.GetGasConstituteResponse:
        """
        @summary This interface is used to obtain gas composition analysis.
        
        @param request: GetGasConstituteRequest
        @return: GetGasConstituteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_gas_constitute_with_options(request, headers, runtime)

    async def get_gas_constitute_async(
        self,
        request: energy_expert_external_20220923_models.GetGasConstituteRequest,
    ) -> energy_expert_external_20220923_models.GetGasConstituteResponse:
        """
        @summary This interface is used to obtain gas composition analysis.
        
        @param request: GetGasConstituteRequest
        @return: GetGasConstituteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_gas_constitute_with_options_async(request, headers, runtime)

    def get_gwp_benchmark_list_with_options(
        self,
        request: energy_expert_external_20220923_models.GetGwpBenchmarkListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetGwpBenchmarkListResponse:
        """
        @summary obtain the active carbon reduction ranking list.
        
        @description This interface returns a list of proactive carbon reduction information given product ID. It\\"s used to understand the carbon reduction efforts at various levels of the product.
        
        @param request: GetGwpBenchmarkListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGwpBenchmarkListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGwpBenchmarkList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/gwp/benchmark/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetGwpBenchmarkListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gwp_benchmark_list_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetGwpBenchmarkListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetGwpBenchmarkListResponse:
        """
        @summary obtain the active carbon reduction ranking list.
        
        @description This interface returns a list of proactive carbon reduction information given product ID. It\\"s used to understand the carbon reduction efforts at various levels of the product.
        
        @param request: GetGwpBenchmarkListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGwpBenchmarkListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGwpBenchmarkList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/gwp/benchmark/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetGwpBenchmarkListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gwp_benchmark_list(
        self,
        request: energy_expert_external_20220923_models.GetGwpBenchmarkListRequest,
    ) -> energy_expert_external_20220923_models.GetGwpBenchmarkListResponse:
        """
        @summary obtain the active carbon reduction ranking list.
        
        @description This interface returns a list of proactive carbon reduction information given product ID. It\\"s used to understand the carbon reduction efforts at various levels of the product.
        
        @param request: GetGwpBenchmarkListRequest
        @return: GetGwpBenchmarkListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_gwp_benchmark_list_with_options(request, headers, runtime)

    async def get_gwp_benchmark_list_async(
        self,
        request: energy_expert_external_20220923_models.GetGwpBenchmarkListRequest,
    ) -> energy_expert_external_20220923_models.GetGwpBenchmarkListResponse:
        """
        @summary obtain the active carbon reduction ranking list.
        
        @description This interface returns a list of proactive carbon reduction information given product ID. It\\"s used to understand the carbon reduction efforts at various levels of the product.
        
        @param request: GetGwpBenchmarkListRequest
        @return: GetGwpBenchmarkListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_gwp_benchmark_list_with_options_async(request, headers, runtime)

    def get_gwp_benchmark_summary_with_options(
        self,
        request: energy_expert_external_20220923_models.GetGwpBenchmarkSummaryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetGwpBenchmarkSummaryResponse:
        """
        @summary This API is to obtain the total amount of active carbon reduction.
        
        @description The API takes a product ID and returns data on the carbon emissions reduction along with a list of the top four contributors to carbon reduction. This info helps understand the total carbon reduction of the product and its main sources.
        
        @param request: GetGwpBenchmarkSummaryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGwpBenchmarkSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGwpBenchmarkSummary',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/gwp/benchmark/summary',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetGwpBenchmarkSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gwp_benchmark_summary_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetGwpBenchmarkSummaryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetGwpBenchmarkSummaryResponse:
        """
        @summary This API is to obtain the total amount of active carbon reduction.
        
        @description The API takes a product ID and returns data on the carbon emissions reduction along with a list of the top four contributors to carbon reduction. This info helps understand the total carbon reduction of the product and its main sources.
        
        @param request: GetGwpBenchmarkSummaryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGwpBenchmarkSummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGwpBenchmarkSummary',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/gwp/benchmark/summary',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetGwpBenchmarkSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gwp_benchmark_summary(
        self,
        request: energy_expert_external_20220923_models.GetGwpBenchmarkSummaryRequest,
    ) -> energy_expert_external_20220923_models.GetGwpBenchmarkSummaryResponse:
        """
        @summary This API is to obtain the total amount of active carbon reduction.
        
        @description The API takes a product ID and returns data on the carbon emissions reduction along with a list of the top four contributors to carbon reduction. This info helps understand the total carbon reduction of the product and its main sources.
        
        @param request: GetGwpBenchmarkSummaryRequest
        @return: GetGwpBenchmarkSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_gwp_benchmark_summary_with_options(request, headers, runtime)

    async def get_gwp_benchmark_summary_async(
        self,
        request: energy_expert_external_20220923_models.GetGwpBenchmarkSummaryRequest,
    ) -> energy_expert_external_20220923_models.GetGwpBenchmarkSummaryResponse:
        """
        @summary This API is to obtain the total amount of active carbon reduction.
        
        @description The API takes a product ID and returns data on the carbon emissions reduction along with a list of the top four contributors to carbon reduction. This info helps understand the total carbon reduction of the product and its main sources.
        
        @param request: GetGwpBenchmarkSummaryRequest
        @return: GetGwpBenchmarkSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_gwp_benchmark_summary_with_options_async(request, headers, runtime)

    def get_gwp_inventory_constitute_with_options(
        self,
        request: energy_expert_external_20220923_models.GetGwpInventoryConstituteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetGwpInventoryConstituteResponse:
        """
        @summary Used to obtain the carbon emission composition analysis of a specified product. Carbon emission composition analysis includes two analysis dimensions: inventory and type. In the rendering effect, including a hierarchical list and pie chart.
        
        @description Used to obtain the carbon emission composition analysis of a specified product. Carbon emission composition analysis includes two analysis dimensions: inventory and type. In the rendering effect, including a hierarchical list and pie chart.
        
        @param request: GetGwpInventoryConstituteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGwpInventoryConstituteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGwpInventoryConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/gwp/inventory/constitute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetGwpInventoryConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gwp_inventory_constitute_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetGwpInventoryConstituteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetGwpInventoryConstituteResponse:
        """
        @summary Used to obtain the carbon emission composition analysis of a specified product. Carbon emission composition analysis includes two analysis dimensions: inventory and type. In the rendering effect, including a hierarchical list and pie chart.
        
        @description Used to obtain the carbon emission composition analysis of a specified product. Carbon emission composition analysis includes two analysis dimensions: inventory and type. In the rendering effect, including a hierarchical list and pie chart.
        
        @param request: GetGwpInventoryConstituteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGwpInventoryConstituteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGwpInventoryConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/gwp/inventory/constitute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetGwpInventoryConstituteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gwp_inventory_constitute(
        self,
        request: energy_expert_external_20220923_models.GetGwpInventoryConstituteRequest,
    ) -> energy_expert_external_20220923_models.GetGwpInventoryConstituteResponse:
        """
        @summary Used to obtain the carbon emission composition analysis of a specified product. Carbon emission composition analysis includes two analysis dimensions: inventory and type. In the rendering effect, including a hierarchical list and pie chart.
        
        @description Used to obtain the carbon emission composition analysis of a specified product. Carbon emission composition analysis includes two analysis dimensions: inventory and type. In the rendering effect, including a hierarchical list and pie chart.
        
        @param request: GetGwpInventoryConstituteRequest
        @return: GetGwpInventoryConstituteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_gwp_inventory_constitute_with_options(request, headers, runtime)

    async def get_gwp_inventory_constitute_async(
        self,
        request: energy_expert_external_20220923_models.GetGwpInventoryConstituteRequest,
    ) -> energy_expert_external_20220923_models.GetGwpInventoryConstituteResponse:
        """
        @summary Used to obtain the carbon emission composition analysis of a specified product. Carbon emission composition analysis includes two analysis dimensions: inventory and type. In the rendering effect, including a hierarchical list and pie chart.
        
        @description Used to obtain the carbon emission composition analysis of a specified product. Carbon emission composition analysis includes two analysis dimensions: inventory and type. In the rendering effect, including a hierarchical list and pie chart.
        
        @param request: GetGwpInventoryConstituteRequest
        @return: GetGwpInventoryConstituteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_gwp_inventory_constitute_with_options_async(request, headers, runtime)

    def get_gwp_inventory_summary_with_options(
        self,
        request: energy_expert_external_20220923_models.GetGwpInventorySummaryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetGwpInventorySummaryResponse:
        """
        @summary This API is used to obtain the total carbon footprint of a product and the top four types of carbon footprint contribution.
        
        @description Returns the total carbon footprint data for the user-specified product ID, along with details on the top four contributors to the carbon footprint, helping to understand the overall carbon footprint and its main components.
        
        @param request: GetGwpInventorySummaryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGwpInventorySummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGwpInventorySummary',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/gwp/inventory/summary',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetGwpInventorySummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gwp_inventory_summary_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetGwpInventorySummaryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetGwpInventorySummaryResponse:
        """
        @summary This API is used to obtain the total carbon footprint of a product and the top four types of carbon footprint contribution.
        
        @description Returns the total carbon footprint data for the user-specified product ID, along with details on the top four contributors to the carbon footprint, helping to understand the overall carbon footprint and its main components.
        
        @param request: GetGwpInventorySummaryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGwpInventorySummaryResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGwpInventorySummary',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/gwp/inventory/summary',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetGwpInventorySummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gwp_inventory_summary(
        self,
        request: energy_expert_external_20220923_models.GetGwpInventorySummaryRequest,
    ) -> energy_expert_external_20220923_models.GetGwpInventorySummaryResponse:
        """
        @summary This API is used to obtain the total carbon footprint of a product and the top four types of carbon footprint contribution.
        
        @description Returns the total carbon footprint data for the user-specified product ID, along with details on the top four contributors to the carbon footprint, helping to understand the overall carbon footprint and its main components.
        
        @param request: GetGwpInventorySummaryRequest
        @return: GetGwpInventorySummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_gwp_inventory_summary_with_options(request, headers, runtime)

    async def get_gwp_inventory_summary_async(
        self,
        request: energy_expert_external_20220923_models.GetGwpInventorySummaryRequest,
    ) -> energy_expert_external_20220923_models.GetGwpInventorySummaryResponse:
        """
        @summary This API is used to obtain the total carbon footprint of a product and the top four types of carbon footprint contribution.
        
        @description Returns the total carbon footprint data for the user-specified product ID, along with details on the top four contributors to the carbon footprint, helping to understand the overall carbon footprint and its main components.
        
        @param request: GetGwpInventorySummaryRequest
        @return: GetGwpInventorySummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_gwp_inventory_summary_with_options_async(request, headers, runtime)

    def get_inventory_list_with_options(
        self,
        request: energy_expert_external_20220923_models.GetInventoryListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetInventoryListResponse:
        """
        @summary Get the list of emissions in descending order under the specified environmental impact (methodType), specified aggregate level (group), and specified calculation mode (emissionType).
        
        @description This interface retrieves a descending order list of emissions for a specified product ID, environmental impact method, group level, and calculation method. It\\"s used to understand various environmental impact emission scenarios.
        
        @param request: GetInventoryListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInventoryListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.emission_type):
            body['emissionType'] = request.emission_type
        if not UtilClient.is_unset(request.group):
            body['group'] = request.group
        if not UtilClient.is_unset(request.method_type):
            body['methodType'] = request.method_type
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInventoryList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/inventory/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetInventoryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_inventory_list_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetInventoryListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetInventoryListResponse:
        """
        @summary Get the list of emissions in descending order under the specified environmental impact (methodType), specified aggregate level (group), and specified calculation mode (emissionType).
        
        @description This interface retrieves a descending order list of emissions for a specified product ID, environmental impact method, group level, and calculation method. It\\"s used to understand various environmental impact emission scenarios.
        
        @param request: GetInventoryListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInventoryListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.emission_type):
            body['emissionType'] = request.emission_type
        if not UtilClient.is_unset(request.group):
            body['group'] = request.group
        if not UtilClient.is_unset(request.method_type):
            body['methodType'] = request.method_type
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInventoryList',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/inventory/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetInventoryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_inventory_list(
        self,
        request: energy_expert_external_20220923_models.GetInventoryListRequest,
    ) -> energy_expert_external_20220923_models.GetInventoryListResponse:
        """
        @summary Get the list of emissions in descending order under the specified environmental impact (methodType), specified aggregate level (group), and specified calculation mode (emissionType).
        
        @description This interface retrieves a descending order list of emissions for a specified product ID, environmental impact method, group level, and calculation method. It\\"s used to understand various environmental impact emission scenarios.
        
        @param request: GetInventoryListRequest
        @return: GetInventoryListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_inventory_list_with_options(request, headers, runtime)

    async def get_inventory_list_async(
        self,
        request: energy_expert_external_20220923_models.GetInventoryListRequest,
    ) -> energy_expert_external_20220923_models.GetInventoryListResponse:
        """
        @summary Get the list of emissions in descending order under the specified environmental impact (methodType), specified aggregate level (group), and specified calculation mode (emissionType).
        
        @description This interface retrieves a descending order list of emissions for a specified product ID, environmental impact method, group level, and calculation method. It\\"s used to understand various environmental impact emission scenarios.
        
        @param request: GetInventoryListRequest
        @return: GetInventoryListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_inventory_list_with_options_async(request, headers, runtime)

    def get_org_and_factory_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetOrgAndFactoryResponse:
        """
        @summary Queries the organizations and sites that are activated by using an Alibaba Cloud account. You cannot call this operation to query the organizations or sites that have not been activated in the console.
        
        @description    If an activated site exists, the information about the site and the organization to which the site belongs is returned. If no activated site exists, null is returned.
        - By current, endpoint only supports Hangzhou: `energyexpertexternal.cn-hangzhou.aliyuncs.com`.
        - To use this API, you need to be added to the whitelist. Please contact us through  <props="china">[official website](https://energy.aliyun.com/ifa/web/defaultLoginPage?adapter=aliyun#/consult?source=%E8%83%BD%E8%80%97%E5%AE%9D%E7%99%BB%E5%BD%95%E9%A1%B5%EF%BC%88WEB%EF%BC%89)
        <props="intl">[official website](https://energy.alibabacloud.com/common?adapter=aliyun&lang=en-US#/home/en) to apply for whitelist activation.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrgAndFactoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOrgAndFactory',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/external/getOrgAndFactory',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetOrgAndFactoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_org_and_factory_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetOrgAndFactoryResponse:
        """
        @summary Queries the organizations and sites that are activated by using an Alibaba Cloud account. You cannot call this operation to query the organizations or sites that have not been activated in the console.
        
        @description    If an activated site exists, the information about the site and the organization to which the site belongs is returned. If no activated site exists, null is returned.
        - By current, endpoint only supports Hangzhou: `energyexpertexternal.cn-hangzhou.aliyuncs.com`.
        - To use this API, you need to be added to the whitelist. Please contact us through  <props="china">[official website](https://energy.aliyun.com/ifa/web/defaultLoginPage?adapter=aliyun#/consult?source=%E8%83%BD%E8%80%97%E5%AE%9D%E7%99%BB%E5%BD%95%E9%A1%B5%EF%BC%88WEB%EF%BC%89)
        <props="intl">[official website](https://energy.alibabacloud.com/common?adapter=aliyun&lang=en-US#/home/en) to apply for whitelist activation.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrgAndFactoryResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOrgAndFactory',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/external/getOrgAndFactory',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetOrgAndFactoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_org_and_factory(self) -> energy_expert_external_20220923_models.GetOrgAndFactoryResponse:
        """
        @summary Queries the organizations and sites that are activated by using an Alibaba Cloud account. You cannot call this operation to query the organizations or sites that have not been activated in the console.
        
        @description    If an activated site exists, the information about the site and the organization to which the site belongs is returned. If no activated site exists, null is returned.
        - By current, endpoint only supports Hangzhou: `energyexpertexternal.cn-hangzhou.aliyuncs.com`.
        - To use this API, you need to be added to the whitelist. Please contact us through  <props="china">[official website](https://energy.aliyun.com/ifa/web/defaultLoginPage?adapter=aliyun#/consult?source=%E8%83%BD%E8%80%97%E5%AE%9D%E7%99%BB%E5%BD%95%E9%A1%B5%EF%BC%88WEB%EF%BC%89)
        <props="intl">[official website](https://energy.alibabacloud.com/common?adapter=aliyun&lang=en-US#/home/en) to apply for whitelist activation.
        
        @return: GetOrgAndFactoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_org_and_factory_with_options(headers, runtime)

    async def get_org_and_factory_async(self) -> energy_expert_external_20220923_models.GetOrgAndFactoryResponse:
        """
        @summary Queries the organizations and sites that are activated by using an Alibaba Cloud account. You cannot call this operation to query the organizations or sites that have not been activated in the console.
        
        @description    If an activated site exists, the information about the site and the organization to which the site belongs is returned. If no activated site exists, null is returned.
        - By current, endpoint only supports Hangzhou: `energyexpertexternal.cn-hangzhou.aliyuncs.com`.
        - To use this API, you need to be added to the whitelist. Please contact us through  <props="china">[official website](https://energy.aliyun.com/ifa/web/defaultLoginPage?adapter=aliyun#/consult?source=%E8%83%BD%E8%80%97%E5%AE%9D%E7%99%BB%E5%BD%95%E9%A1%B5%EF%BC%88WEB%EF%BC%89)
        <props="intl">[official website](https://energy.alibabacloud.com/common?adapter=aliyun&lang=en-US#/home/en) to apply for whitelist activation.
        
        @return: GetOrgAndFactoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_org_and_factory_with_options_async(headers, runtime)

    def get_org_constitute_with_options(
        self,
        request: energy_expert_external_20220923_models.GetOrgConstituteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetOrgConstituteResponse:
        """
        @summary This interface is used to obtain carbon inventory organization analysis data.
        
        @param request: GetOrgConstituteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrgConstituteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.module_code):
            body['moduleCode'] = request.module_code
        if not UtilClient.is_unset(request.module_type):
            body['moduleType'] = request.module_type
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOrgConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/analysis/org',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetOrgConstituteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_org_constitute_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetOrgConstituteRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetOrgConstituteResponse:
        """
        @summary This interface is used to obtain carbon inventory organization analysis data.
        
        @param request: GetOrgConstituteRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrgConstituteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.module_code):
            body['moduleCode'] = request.module_code
        if not UtilClient.is_unset(request.module_type):
            body['moduleType'] = request.module_type
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOrgConstitute',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/analysis/org',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetOrgConstituteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_org_constitute(
        self,
        request: energy_expert_external_20220923_models.GetOrgConstituteRequest,
    ) -> energy_expert_external_20220923_models.GetOrgConstituteResponse:
        """
        @summary This interface is used to obtain carbon inventory organization analysis data.
        
        @param request: GetOrgConstituteRequest
        @return: GetOrgConstituteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_org_constitute_with_options(request, headers, runtime)

    async def get_org_constitute_async(
        self,
        request: energy_expert_external_20220923_models.GetOrgConstituteRequest,
    ) -> energy_expert_external_20220923_models.GetOrgConstituteResponse:
        """
        @summary This interface is used to obtain carbon inventory organization analysis data.
        
        @param request: GetOrgConstituteRequest
        @return: GetOrgConstituteResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_org_constitute_with_options_async(request, headers, runtime)

    def get_pcr_info_with_options(
        self,
        request: energy_expert_external_20220923_models.GetPcrInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetPcrInfoResponse:
        """
        @summary Obtains the oss address of the Product Carbon footprint Report.
        
        @description With the user-specified product ID, this interface retrieves detailed information and download links for previously generated PCR reports. To use it, two conditions must be met: 1) the result has already been generated; 2) the PCR report has been created.
        
        @param request: GetPcrInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPcrInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPcrInfo',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/pcr/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetPcrInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pcr_info_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetPcrInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetPcrInfoResponse:
        """
        @summary Obtains the oss address of the Product Carbon footprint Report.
        
        @description With the user-specified product ID, this interface retrieves detailed information and download links for previously generated PCR reports. To use it, two conditions must be met: 1) the result has already been generated; 2) the PCR report has been created.
        
        @param request: GetPcrInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPcrInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPcrInfo',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/pcr/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetPcrInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pcr_info(
        self,
        request: energy_expert_external_20220923_models.GetPcrInfoRequest,
    ) -> energy_expert_external_20220923_models.GetPcrInfoResponse:
        """
        @summary Obtains the oss address of the Product Carbon footprint Report.
        
        @description With the user-specified product ID, this interface retrieves detailed information and download links for previously generated PCR reports. To use it, two conditions must be met: 1) the result has already been generated; 2) the PCR report has been created.
        
        @param request: GetPcrInfoRequest
        @return: GetPcrInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_pcr_info_with_options(request, headers, runtime)

    async def get_pcr_info_async(
        self,
        request: energy_expert_external_20220923_models.GetPcrInfoRequest,
    ) -> energy_expert_external_20220923_models.GetPcrInfoResponse:
        """
        @summary Obtains the oss address of the Product Carbon footprint Report.
        
        @description With the user-specified product ID, this interface retrieves detailed information and download links for previously generated PCR reports. To use it, two conditions must be met: 1) the result has already been generated; 2) the PCR report has been created.
        
        @param request: GetPcrInfoRequest
        @return: GetPcrInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_pcr_info_with_options_async(request, headers, runtime)

    def get_reduction_proposal_with_options(
        self,
        request: energy_expert_external_20220923_models.GetReductionProposalRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetReductionProposalResponse:
        """
        @summary Get carbon reduction recommendations.
        
        @description This API returns carbon reduction proposals based on the product ID. It\\"s useful for understanding optimization tips to reduce the carbon emissions associated with a product.
        
        @param request: GetReductionProposalRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetReductionProposalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.data_quality_evaluation_type):
            body['dataQualityEvaluationType'] = request.data_quality_evaluation_type
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetReductionProposal',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/reduction/proposal',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetReductionProposalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_reduction_proposal_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetReductionProposalRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetReductionProposalResponse:
        """
        @summary Get carbon reduction recommendations.
        
        @description This API returns carbon reduction proposals based on the product ID. It\\"s useful for understanding optimization tips to reduce the carbon emissions associated with a product.
        
        @param request: GetReductionProposalRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetReductionProposalResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.data_quality_evaluation_type):
            body['dataQualityEvaluationType'] = request.data_quality_evaluation_type
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetReductionProposal',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/reduction/proposal',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetReductionProposalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_reduction_proposal(
        self,
        request: energy_expert_external_20220923_models.GetReductionProposalRequest,
    ) -> energy_expert_external_20220923_models.GetReductionProposalResponse:
        """
        @summary Get carbon reduction recommendations.
        
        @description This API returns carbon reduction proposals based on the product ID. It\\"s useful for understanding optimization tips to reduce the carbon emissions associated with a product.
        
        @param request: GetReductionProposalRequest
        @return: GetReductionProposalResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_reduction_proposal_with_options(request, headers, runtime)

    async def get_reduction_proposal_async(
        self,
        request: energy_expert_external_20220923_models.GetReductionProposalRequest,
    ) -> energy_expert_external_20220923_models.GetReductionProposalResponse:
        """
        @summary Get carbon reduction recommendations.
        
        @description This API returns carbon reduction proposals based on the product ID. It\\"s useful for understanding optimization tips to reduce the carbon emissions associated with a product.
        
        @param request: GetReductionProposalRequest
        @return: GetReductionProposalResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_reduction_proposal_with_options_async(request, headers, runtime)

    def get_vlextraction_result_with_options(
        self,
        request: energy_expert_external_20220923_models.GetVLExtractionResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetVLExtractionResultResponse:
        """
        @summary For Querying Qwen-VL Model Information Extraction Results.
        The input parameter taskId is obtained from the taskId returned by the interfaces SubmitVLExtractionTask or SubmitVLExtractionTaskAdvance.
        The query results can be in one of three statuses: processing, successfully completed, or failed.
        
        @param request: GetVLExtractionResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVLExtractionResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVLExtractionResult',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/getVLExtractionResult',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetVLExtractionResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vlextraction_result_with_options_async(
        self,
        request: energy_expert_external_20220923_models.GetVLExtractionResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.GetVLExtractionResultResponse:
        """
        @summary For Querying Qwen-VL Model Information Extraction Results.
        The input parameter taskId is obtained from the taskId returned by the interfaces SubmitVLExtractionTask or SubmitVLExtractionTaskAdvance.
        The query results can be in one of three statuses: processing, successfully completed, or failed.
        
        @param request: GetVLExtractionResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVLExtractionResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVLExtractionResult',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/getVLExtractionResult',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.GetVLExtractionResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vlextraction_result(
        self,
        request: energy_expert_external_20220923_models.GetVLExtractionResultRequest,
    ) -> energy_expert_external_20220923_models.GetVLExtractionResultResponse:
        """
        @summary For Querying Qwen-VL Model Information Extraction Results.
        The input parameter taskId is obtained from the taskId returned by the interfaces SubmitVLExtractionTask or SubmitVLExtractionTaskAdvance.
        The query results can be in one of three statuses: processing, successfully completed, or failed.
        
        @param request: GetVLExtractionResultRequest
        @return: GetVLExtractionResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_vlextraction_result_with_options(request, headers, runtime)

    async def get_vlextraction_result_async(
        self,
        request: energy_expert_external_20220923_models.GetVLExtractionResultRequest,
    ) -> energy_expert_external_20220923_models.GetVLExtractionResultResponse:
        """
        @summary For Querying Qwen-VL Model Information Extraction Results.
        The input parameter taskId is obtained from the taskId returned by the interfaces SubmitVLExtractionTask or SubmitVLExtractionTaskAdvance.
        The query results can be in one of three statuses: processing, successfully completed, or failed.
        
        @param request: GetVLExtractionResultRequest
        @return: GetVLExtractionResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_vlextraction_result_with_options_async(request, headers, runtime)

    def is_completed_with_options(
        self,
        request: energy_expert_external_20220923_models.IsCompletedRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.IsCompletedResponse:
        """
        @summary Check if the result generation is complete.
        
        @description This API checks the completion status of generating a report. It should be used before calling other result APIs, as they will only display content once the report generation is complete.
        
        @param request: IsCompletedRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: IsCompletedResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IsCompleted',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/completed',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.IsCompletedResponse(),
            self.call_api(params, req, runtime)
        )

    async def is_completed_with_options_async(
        self,
        request: energy_expert_external_20220923_models.IsCompletedRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.IsCompletedResponse:
        """
        @summary Check if the result generation is complete.
        
        @description This API checks the completion status of generating a report. It should be used before calling other result APIs, as they will only display content once the report generation is complete.
        
        @param request: IsCompletedRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: IsCompletedResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.product_id):
            body['productId'] = request.product_id
        if not UtilClient.is_unset(request.product_type):
            body['productType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IsCompleted',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/footprint/result/completed',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.IsCompletedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def is_completed(
        self,
        request: energy_expert_external_20220923_models.IsCompletedRequest,
    ) -> energy_expert_external_20220923_models.IsCompletedResponse:
        """
        @summary Check if the result generation is complete.
        
        @description This API checks the completion status of generating a report. It should be used before calling other result APIs, as they will only display content once the report generation is complete.
        
        @param request: IsCompletedRequest
        @return: IsCompletedResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.is_completed_with_options(request, headers, runtime)

    async def is_completed_async(
        self,
        request: energy_expert_external_20220923_models.IsCompletedRequest,
    ) -> energy_expert_external_20220923_models.IsCompletedResponse:
        """
        @summary Check if the result generation is complete.
        
        @description This API checks the completion status of generating a report. It should be used before calling other result APIs, as they will only display content once the report generation is complete.
        
        @param request: IsCompletedRequest
        @return: IsCompletedResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.is_completed_with_options_async(request, headers, runtime)

    def push_device_data_with_options(
        self,
        request: energy_expert_external_20220923_models.PushDeviceDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.PushDeviceDataResponse:
        """
        @summary This interface is used to push device measuring point data, such as power meter voltage and other data.
        
        @param request: PushDeviceDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushDeviceDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_type):
            body['deviceType'] = request.device_type
        if not UtilClient.is_unset(request.devices):
            body['devices'] = request.devices
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushDeviceData',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/data/increment/push',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.PushDeviceDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_device_data_with_options_async(
        self,
        request: energy_expert_external_20220923_models.PushDeviceDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.PushDeviceDataResponse:
        """
        @summary This interface is used to push device measuring point data, such as power meter voltage and other data.
        
        @param request: PushDeviceDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushDeviceDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_type):
            body['deviceType'] = request.device_type
        if not UtilClient.is_unset(request.devices):
            body['devices'] = request.devices
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushDeviceData',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/data/increment/push',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.PushDeviceDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_device_data(
        self,
        request: energy_expert_external_20220923_models.PushDeviceDataRequest,
    ) -> energy_expert_external_20220923_models.PushDeviceDataResponse:
        """
        @summary This interface is used to push device measuring point data, such as power meter voltage and other data.
        
        @param request: PushDeviceDataRequest
        @return: PushDeviceDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_device_data_with_options(request, headers, runtime)

    async def push_device_data_async(
        self,
        request: energy_expert_external_20220923_models.PushDeviceDataRequest,
    ) -> energy_expert_external_20220923_models.PushDeviceDataResponse:
        """
        @summary This interface is used to push device measuring point data, such as power meter voltage and other data.
        
        @param request: PushDeviceDataRequest
        @return: PushDeviceDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_device_data_with_options_async(request, headers, runtime)

    def push_item_data_with_options(
        self,
        request: energy_expert_external_20220923_models.PushItemDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.PushItemDataResponse:
        """
        @summary This interface is used to push data items.
        
        @description - This interface is used for individual data item data.
        - Data items can link data to services such as carbon footprints and carbon inventories.
        - Depending on the platform configuration, active data on a yearly and monthly basis is supported.
        
        @param request: PushItemDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushItemDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.items):
            body['items'] = request.items
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushItemData',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/data/item/push',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.PushItemDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_item_data_with_options_async(
        self,
        request: energy_expert_external_20220923_models.PushItemDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.PushItemDataResponse:
        """
        @summary This interface is used to push data items.
        
        @description - This interface is used for individual data item data.
        - Data items can link data to services such as carbon footprints and carbon inventories.
        - Depending on the platform configuration, active data on a yearly and monthly basis is supported.
        
        @param request: PushItemDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushItemDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.items):
            body['items'] = request.items
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushItemData',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/data/item/push',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.PushItemDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_item_data(
        self,
        request: energy_expert_external_20220923_models.PushItemDataRequest,
    ) -> energy_expert_external_20220923_models.PushItemDataResponse:
        """
        @summary This interface is used to push data items.
        
        @description - This interface is used for individual data item data.
        - Data items can link data to services such as carbon footprints and carbon inventories.
        - Depending on the platform configuration, active data on a yearly and monthly basis is supported.
        
        @param request: PushItemDataRequest
        @return: PushItemDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_item_data_with_options(request, headers, runtime)

    async def push_item_data_async(
        self,
        request: energy_expert_external_20220923_models.PushItemDataRequest,
    ) -> energy_expert_external_20220923_models.PushItemDataResponse:
        """
        @summary This interface is used to push data items.
        
        @description - This interface is used for individual data item data.
        - Data items can link data to services such as carbon footprints and carbon inventories.
        - Depending on the platform configuration, active data on a yearly and monthly basis is supported.
        
        @param request: PushItemDataRequest
        @return: PushItemDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_item_data_with_options_async(request, headers, runtime)

    def recalculate_carbon_emission_with_options(
        self,
        request: energy_expert_external_20220923_models.RecalculateCarbonEmissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.RecalculateCarbonEmissionResponse:
        """
        @summary Recalculate carbon emissions.
        
        @description - After uploading the data items, you need to call this interface to recalculate the carbon inventory data.
        
        @param request: RecalculateCarbonEmissionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecalculateCarbonEmissionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecalculateCarbonEmission',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/data/item/recalculate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.RecalculateCarbonEmissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def recalculate_carbon_emission_with_options_async(
        self,
        request: energy_expert_external_20220923_models.RecalculateCarbonEmissionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.RecalculateCarbonEmissionResponse:
        """
        @summary Recalculate carbon emissions.
        
        @description - After uploading the data items, you need to call this interface to recalculate the carbon inventory data.
        
        @param request: RecalculateCarbonEmissionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecalculateCarbonEmissionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.year):
            body['year'] = request.year
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecalculateCarbonEmission',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/emission/data/item/recalculate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.RecalculateCarbonEmissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recalculate_carbon_emission(
        self,
        request: energy_expert_external_20220923_models.RecalculateCarbonEmissionRequest,
    ) -> energy_expert_external_20220923_models.RecalculateCarbonEmissionResponse:
        """
        @summary Recalculate carbon emissions.
        
        @description - After uploading the data items, you need to call this interface to recalculate the carbon inventory data.
        
        @param request: RecalculateCarbonEmissionRequest
        @return: RecalculateCarbonEmissionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recalculate_carbon_emission_with_options(request, headers, runtime)

    async def recalculate_carbon_emission_async(
        self,
        request: energy_expert_external_20220923_models.RecalculateCarbonEmissionRequest,
    ) -> energy_expert_external_20220923_models.RecalculateCarbonEmissionResponse:
        """
        @summary Recalculate carbon emissions.
        
        @description - After uploading the data items, you need to call this interface to recalculate the carbon inventory data.
        
        @param request: RecalculateCarbonEmissionRequest
        @return: RecalculateCarbonEmissionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.recalculate_carbon_emission_with_options_async(request, headers, runtime)

    def send_document_ask_question_with_options(
        self,
        request: energy_expert_external_20220923_models.SendDocumentAskQuestionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SendDocumentAskQuestionResponse:
        """
        @summary [Important] This api is no longer maintained, please use the Chat api.
        
        @param request: SendDocumentAskQuestionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendDocumentAskQuestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.folder_id):
            body['folderId'] = request.folder_id
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendDocumentAskQuestion',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/aidoc/document/sendDocumentAskQuestion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.SendDocumentAskQuestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_document_ask_question_with_options_async(
        self,
        request: energy_expert_external_20220923_models.SendDocumentAskQuestionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SendDocumentAskQuestionResponse:
        """
        @summary [Important] This api is no longer maintained, please use the Chat api.
        
        @param request: SendDocumentAskQuestionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendDocumentAskQuestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.folder_id):
            body['folderId'] = request.folder_id
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendDocumentAskQuestion',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/aidoc/document/sendDocumentAskQuestion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.SendDocumentAskQuestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_document_ask_question(
        self,
        request: energy_expert_external_20220923_models.SendDocumentAskQuestionRequest,
    ) -> energy_expert_external_20220923_models.SendDocumentAskQuestionResponse:
        """
        @summary [Important] This api is no longer maintained, please use the Chat api.
        
        @param request: SendDocumentAskQuestionRequest
        @return: SendDocumentAskQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.send_document_ask_question_with_options(request, headers, runtime)

    async def send_document_ask_question_async(
        self,
        request: energy_expert_external_20220923_models.SendDocumentAskQuestionRequest,
    ) -> energy_expert_external_20220923_models.SendDocumentAskQuestionResponse:
        """
        @summary [Important] This api is no longer maintained, please use the Chat api.
        
        @param request: SendDocumentAskQuestionRequest
        @return: SendDocumentAskQuestionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.send_document_ask_question_with_options_async(request, headers, runtime)

    def set_running_plan_with_options(
        self,
        request: energy_expert_external_20220923_models.SetRunningPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SetRunningPlanResponse:
        """
        @summary 设置运行计划
        
        @param request: SetRunningPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetRunningPlanResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.control_type):
            body['controlType'] = request.control_type
        if not UtilClient.is_unset(request.date_type):
            body['dateType'] = request.date_type
        if not UtilClient.is_unset(request.earliest_startup_time):
            body['earliestStartupTime'] = request.earliest_startup_time
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.factory_id):
            body['factoryId'] = request.factory_id
        if not UtilClient.is_unset(request.latest_shutdown_time):
            body['latestShutdownTime'] = request.latest_shutdown_time
        if not UtilClient.is_unset(request.max_carbon_dioxide):
            body['maxCarbonDioxide'] = request.max_carbon_dioxide
        if not UtilClient.is_unset(request.max_tem):
            body['maxTem'] = request.max_tem
        if not UtilClient.is_unset(request.min_tem):
            body['minTem'] = request.min_tem
        if not UtilClient.is_unset(request.p_key):
            body['pKey'] = request.p_key
        if not UtilClient.is_unset(request.season_mode):
            body['seasonMode'] = request.season_mode
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.statistics_time):
            body['statisticsTime'] = request.statistics_time
        if not UtilClient.is_unset(request.system_id):
            body['systemId'] = request.system_id
        if not UtilClient.is_unset(request.working_end_time):
            body['workingEndTime'] = request.working_end_time
        if not UtilClient.is_unset(request.working_start_time):
            body['workingStartTime'] = request.working_start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetRunningPlan',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/hvac/setRunningPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.SetRunningPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_running_plan_with_options_async(
        self,
        request: energy_expert_external_20220923_models.SetRunningPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SetRunningPlanResponse:
        """
        @summary 设置运行计划
        
        @param request: SetRunningPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetRunningPlanResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.control_type):
            body['controlType'] = request.control_type
        if not UtilClient.is_unset(request.date_type):
            body['dateType'] = request.date_type
        if not UtilClient.is_unset(request.earliest_startup_time):
            body['earliestStartupTime'] = request.earliest_startup_time
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.factory_id):
            body['factoryId'] = request.factory_id
        if not UtilClient.is_unset(request.latest_shutdown_time):
            body['latestShutdownTime'] = request.latest_shutdown_time
        if not UtilClient.is_unset(request.max_carbon_dioxide):
            body['maxCarbonDioxide'] = request.max_carbon_dioxide
        if not UtilClient.is_unset(request.max_tem):
            body['maxTem'] = request.max_tem
        if not UtilClient.is_unset(request.min_tem):
            body['minTem'] = request.min_tem
        if not UtilClient.is_unset(request.p_key):
            body['pKey'] = request.p_key
        if not UtilClient.is_unset(request.season_mode):
            body['seasonMode'] = request.season_mode
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.statistics_time):
            body['statisticsTime'] = request.statistics_time
        if not UtilClient.is_unset(request.system_id):
            body['systemId'] = request.system_id
        if not UtilClient.is_unset(request.working_end_time):
            body['workingEndTime'] = request.working_end_time
        if not UtilClient.is_unset(request.working_start_time):
            body['workingStartTime'] = request.working_start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetRunningPlan',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/carbon/hvac/setRunningPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.SetRunningPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_running_plan(
        self,
        request: energy_expert_external_20220923_models.SetRunningPlanRequest,
    ) -> energy_expert_external_20220923_models.SetRunningPlanResponse:
        """
        @summary 设置运行计划
        
        @param request: SetRunningPlanRequest
        @return: SetRunningPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.set_running_plan_with_options(request, headers, runtime)

    async def set_running_plan_async(
        self,
        request: energy_expert_external_20220923_models.SetRunningPlanRequest,
    ) -> energy_expert_external_20220923_models.SetRunningPlanResponse:
        """
        @summary 设置运行计划
        
        @param request: SetRunningPlanRequest
        @return: SetRunningPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.set_running_plan_with_options_async(request, headers, runtime)

    def submit_doc_extraction_task_with_options(
        self,
        request: energy_expert_external_20220923_models.SubmitDocExtractionTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SubmitDocExtractionTaskResponse:
        """
        @summary Extracts key information from documents using user-defined Key-Value or prompt templates. A taskId is returned upon successful execution for retrieving extraction results via GetDocExtractionResult.
        Supports:
        URL Upload: SubmitDocExtractionTask
        Local File Upload: SubmitDocExtractionTask
        
        @param request: SubmitDocExtractionTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocExtractionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extract_type):
            query['extractType'] = request.extract_type
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['fileUrl'] = request.file_url
        if not UtilClient.is_unset(request.folder_id):
            query['folderId'] = request.folder_id
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDocExtractionTask',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/submitDocExtractionTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.SubmitDocExtractionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_doc_extraction_task_with_options_async(
        self,
        request: energy_expert_external_20220923_models.SubmitDocExtractionTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SubmitDocExtractionTaskResponse:
        """
        @summary Extracts key information from documents using user-defined Key-Value or prompt templates. A taskId is returned upon successful execution for retrieving extraction results via GetDocExtractionResult.
        Supports:
        URL Upload: SubmitDocExtractionTask
        Local File Upload: SubmitDocExtractionTask
        
        @param request: SubmitDocExtractionTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocExtractionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extract_type):
            query['extractType'] = request.extract_type
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['fileUrl'] = request.file_url
        if not UtilClient.is_unset(request.folder_id):
            query['folderId'] = request.folder_id
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDocExtractionTask',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/submitDocExtractionTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.SubmitDocExtractionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_doc_extraction_task(
        self,
        request: energy_expert_external_20220923_models.SubmitDocExtractionTaskRequest,
    ) -> energy_expert_external_20220923_models.SubmitDocExtractionTaskResponse:
        """
        @summary Extracts key information from documents using user-defined Key-Value or prompt templates. A taskId is returned upon successful execution for retrieving extraction results via GetDocExtractionResult.
        Supports:
        URL Upload: SubmitDocExtractionTask
        Local File Upload: SubmitDocExtractionTask
        
        @param request: SubmitDocExtractionTaskRequest
        @return: SubmitDocExtractionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_doc_extraction_task_with_options(request, headers, runtime)

    async def submit_doc_extraction_task_async(
        self,
        request: energy_expert_external_20220923_models.SubmitDocExtractionTaskRequest,
    ) -> energy_expert_external_20220923_models.SubmitDocExtractionTaskResponse:
        """
        @summary Extracts key information from documents using user-defined Key-Value or prompt templates. A taskId is returned upon successful execution for retrieving extraction results via GetDocExtractionResult.
        Supports:
        URL Upload: SubmitDocExtractionTask
        Local File Upload: SubmitDocExtractionTask
        
        @param request: SubmitDocExtractionTaskRequest
        @return: SubmitDocExtractionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_doc_extraction_task_with_options_async(request, headers, runtime)

    def submit_doc_extraction_task_advance(
        self,
        request: energy_expert_external_20220923_models.SubmitDocExtractionTaskAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SubmitDocExtractionTaskResponse:
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
            'Product': 'energyExpertExternal',
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
        submit_doc_extraction_task_req = energy_expert_external_20220923_models.SubmitDocExtractionTaskRequest()
        OpenApiUtilClient.convert(request, submit_doc_extraction_task_req)
        if not UtilClient.is_unset(request.file_url_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_url_object,
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
            submit_doc_extraction_task_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_doc_extraction_task_resp = self.submit_doc_extraction_task_with_options(submit_doc_extraction_task_req, headers, runtime)
        return submit_doc_extraction_task_resp

    async def submit_doc_extraction_task_advance_async(
        self,
        request: energy_expert_external_20220923_models.SubmitDocExtractionTaskAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SubmitDocExtractionTaskResponse:
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
            'Product': 'energyExpertExternal',
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
        submit_doc_extraction_task_req = energy_expert_external_20220923_models.SubmitDocExtractionTaskRequest()
        OpenApiUtilClient.convert(request, submit_doc_extraction_task_req)
        if not UtilClient.is_unset(request.file_url_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_url_object,
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
            submit_doc_extraction_task_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_doc_extraction_task_resp = await self.submit_doc_extraction_task_with_options_async(submit_doc_extraction_task_req, headers, runtime)
        return submit_doc_extraction_task_resp

    def submit_doc_parsing_task_with_options(
        self,
        request: energy_expert_external_20220923_models.SubmitDocParsingTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SubmitDocParsingTaskResponse:
        """
        @summary Parses text, tables, images, and more from documents. After execution, a taskId is returned for retrieving document parsing results via GetDocParsingResult.
        Supports:
        URL Upload: SubmitDocParsingTask
        Local File Upload: SubmitDocParsingTaskAdvance
        
        @param request: SubmitDocParsingTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocParsingTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['fileUrl'] = request.file_url
        if not UtilClient.is_unset(request.folder_id):
            query['folderId'] = request.folder_id
        if not UtilClient.is_unset(request.need_analyze_img):
            query['needAnalyzeImg'] = request.need_analyze_img
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDocParsingTask',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/submitDocParsingTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.SubmitDocParsingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_doc_parsing_task_with_options_async(
        self,
        request: energy_expert_external_20220923_models.SubmitDocParsingTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SubmitDocParsingTaskResponse:
        """
        @summary Parses text, tables, images, and more from documents. After execution, a taskId is returned for retrieving document parsing results via GetDocParsingResult.
        Supports:
        URL Upload: SubmitDocParsingTask
        Local File Upload: SubmitDocParsingTaskAdvance
        
        @param request: SubmitDocParsingTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocParsingTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['fileUrl'] = request.file_url
        if not UtilClient.is_unset(request.folder_id):
            query['folderId'] = request.folder_id
        if not UtilClient.is_unset(request.need_analyze_img):
            query['needAnalyzeImg'] = request.need_analyze_img
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDocParsingTask',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/submitDocParsingTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.SubmitDocParsingTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_doc_parsing_task(
        self,
        request: energy_expert_external_20220923_models.SubmitDocParsingTaskRequest,
    ) -> energy_expert_external_20220923_models.SubmitDocParsingTaskResponse:
        """
        @summary Parses text, tables, images, and more from documents. After execution, a taskId is returned for retrieving document parsing results via GetDocParsingResult.
        Supports:
        URL Upload: SubmitDocParsingTask
        Local File Upload: SubmitDocParsingTaskAdvance
        
        @param request: SubmitDocParsingTaskRequest
        @return: SubmitDocParsingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_doc_parsing_task_with_options(request, headers, runtime)

    async def submit_doc_parsing_task_async(
        self,
        request: energy_expert_external_20220923_models.SubmitDocParsingTaskRequest,
    ) -> energy_expert_external_20220923_models.SubmitDocParsingTaskResponse:
        """
        @summary Parses text, tables, images, and more from documents. After execution, a taskId is returned for retrieving document parsing results via GetDocParsingResult.
        Supports:
        URL Upload: SubmitDocParsingTask
        Local File Upload: SubmitDocParsingTaskAdvance
        
        @param request: SubmitDocParsingTaskRequest
        @return: SubmitDocParsingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_doc_parsing_task_with_options_async(request, headers, runtime)

    def submit_doc_parsing_task_advance(
        self,
        request: energy_expert_external_20220923_models.SubmitDocParsingTaskAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SubmitDocParsingTaskResponse:
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
            'Product': 'energyExpertExternal',
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
        submit_doc_parsing_task_req = energy_expert_external_20220923_models.SubmitDocParsingTaskRequest()
        OpenApiUtilClient.convert(request, submit_doc_parsing_task_req)
        if not UtilClient.is_unset(request.file_url_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_url_object,
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
            submit_doc_parsing_task_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_doc_parsing_task_resp = self.submit_doc_parsing_task_with_options(submit_doc_parsing_task_req, headers, runtime)
        return submit_doc_parsing_task_resp

    async def submit_doc_parsing_task_advance_async(
        self,
        request: energy_expert_external_20220923_models.SubmitDocParsingTaskAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SubmitDocParsingTaskResponse:
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
            'Product': 'energyExpertExternal',
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
        submit_doc_parsing_task_req = energy_expert_external_20220923_models.SubmitDocParsingTaskRequest()
        OpenApiUtilClient.convert(request, submit_doc_parsing_task_req)
        if not UtilClient.is_unset(request.file_url_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_url_object,
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
            submit_doc_parsing_task_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_doc_parsing_task_resp = await self.submit_doc_parsing_task_with_options_async(submit_doc_parsing_task_req, headers, runtime)
        return submit_doc_parsing_task_resp

    def submit_document_analyze_job_with_options(
        self,
        request: energy_expert_external_20220923_models.SubmitDocumentAnalyzeJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SubmitDocumentAnalyzeJobResponse:
        """
        @summary [Important] The api is no longer maintained, please use the following api:
        Document parsing using SubmitDocParsingTask.
        Document extraction using SubmitVLExtractionTask, SubmitDocExtractionTask.
        
        @param request: SubmitDocumentAnalyzeJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocumentAnalyzeJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_type):
            query['analysisType'] = request.analysis_type
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['fileUrl'] = request.file_url
        if not UtilClient.is_unset(request.folder_id):
            query['folderId'] = request.folder_id
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDocumentAnalyzeJob',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/aidoc/document/submitDocumentAnalyzeJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.SubmitDocumentAnalyzeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_document_analyze_job_with_options_async(
        self,
        request: energy_expert_external_20220923_models.SubmitDocumentAnalyzeJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SubmitDocumentAnalyzeJobResponse:
        """
        @summary [Important] The api is no longer maintained, please use the following api:
        Document parsing using SubmitDocParsingTask.
        Document extraction using SubmitVLExtractionTask, SubmitDocExtractionTask.
        
        @param request: SubmitDocumentAnalyzeJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitDocumentAnalyzeJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_type):
            query['analysisType'] = request.analysis_type
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['fileUrl'] = request.file_url
        if not UtilClient.is_unset(request.folder_id):
            query['folderId'] = request.folder_id
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDocumentAnalyzeJob',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v1/aidoc/document/submitDocumentAnalyzeJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.SubmitDocumentAnalyzeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_document_analyze_job(
        self,
        request: energy_expert_external_20220923_models.SubmitDocumentAnalyzeJobRequest,
    ) -> energy_expert_external_20220923_models.SubmitDocumentAnalyzeJobResponse:
        """
        @summary [Important] The api is no longer maintained, please use the following api:
        Document parsing using SubmitDocParsingTask.
        Document extraction using SubmitVLExtractionTask, SubmitDocExtractionTask.
        
        @param request: SubmitDocumentAnalyzeJobRequest
        @return: SubmitDocumentAnalyzeJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_document_analyze_job_with_options(request, headers, runtime)

    async def submit_document_analyze_job_async(
        self,
        request: energy_expert_external_20220923_models.SubmitDocumentAnalyzeJobRequest,
    ) -> energy_expert_external_20220923_models.SubmitDocumentAnalyzeJobResponse:
        """
        @summary [Important] The api is no longer maintained, please use the following api:
        Document parsing using SubmitDocParsingTask.
        Document extraction using SubmitVLExtractionTask, SubmitDocExtractionTask.
        
        @param request: SubmitDocumentAnalyzeJobRequest
        @return: SubmitDocumentAnalyzeJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_document_analyze_job_with_options_async(request, headers, runtime)

    def submit_document_analyze_job_advance(
        self,
        request: energy_expert_external_20220923_models.SubmitDocumentAnalyzeJobAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SubmitDocumentAnalyzeJobResponse:
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
            'Product': 'energyExpertExternal',
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
        submit_document_analyze_job_req = energy_expert_external_20220923_models.SubmitDocumentAnalyzeJobRequest()
        OpenApiUtilClient.convert(request, submit_document_analyze_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_url_object,
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
            submit_document_analyze_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_document_analyze_job_resp = self.submit_document_analyze_job_with_options(submit_document_analyze_job_req, headers, runtime)
        return submit_document_analyze_job_resp

    async def submit_document_analyze_job_advance_async(
        self,
        request: energy_expert_external_20220923_models.SubmitDocumentAnalyzeJobAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SubmitDocumentAnalyzeJobResponse:
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
            'Product': 'energyExpertExternal',
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
        submit_document_analyze_job_req = energy_expert_external_20220923_models.SubmitDocumentAnalyzeJobRequest()
        OpenApiUtilClient.convert(request, submit_document_analyze_job_req)
        if not UtilClient.is_unset(request.file_url_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_url_object,
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
            submit_document_analyze_job_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_document_analyze_job_resp = await self.submit_document_analyze_job_with_options_async(submit_document_analyze_job_req, headers, runtime)
        return submit_document_analyze_job_resp

    def submit_vlextraction_task_with_options(
        self,
        request: energy_expert_external_20220923_models.SubmitVLExtractionTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SubmitVLExtractionTaskResponse:
        """
        @summary Extracts key information from documents using KV templates or prompts with the Qwen-VL model, ideal for image extraction.
        Supports:
        URL Upload: SubmitVLExtractionTask.
        Local File Upload: SubmitVLExtractionTaskAdvance
        
        @param request: SubmitVLExtractionTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitVLExtractionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['fileUrl'] = request.file_url
        if not UtilClient.is_unset(request.folder_id):
            query['folderId'] = request.folder_id
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitVLExtractionTask',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/submitVLExtractionTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.SubmitVLExtractionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_vlextraction_task_with_options_async(
        self,
        request: energy_expert_external_20220923_models.SubmitVLExtractionTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SubmitVLExtractionTaskResponse:
        """
        @summary Extracts key information from documents using KV templates or prompts with the Qwen-VL model, ideal for image extraction.
        Supports:
        URL Upload: SubmitVLExtractionTask.
        Local File Upload: SubmitVLExtractionTaskAdvance
        
        @param request: SubmitVLExtractionTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitVLExtractionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_url):
            query['fileUrl'] = request.file_url
        if not UtilClient.is_unset(request.folder_id):
            query['folderId'] = request.folder_id
        if not UtilClient.is_unset(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitVLExtractionTask',
            version='2022-09-23',
            protocol='HTTPS',
            pathname=f'/api/v2/aidoc/document/submitVLExtractionTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            energy_expert_external_20220923_models.SubmitVLExtractionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_vlextraction_task(
        self,
        request: energy_expert_external_20220923_models.SubmitVLExtractionTaskRequest,
    ) -> energy_expert_external_20220923_models.SubmitVLExtractionTaskResponse:
        """
        @summary Extracts key information from documents using KV templates or prompts with the Qwen-VL model, ideal for image extraction.
        Supports:
        URL Upload: SubmitVLExtractionTask.
        Local File Upload: SubmitVLExtractionTaskAdvance
        
        @param request: SubmitVLExtractionTaskRequest
        @return: SubmitVLExtractionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_vlextraction_task_with_options(request, headers, runtime)

    async def submit_vlextraction_task_async(
        self,
        request: energy_expert_external_20220923_models.SubmitVLExtractionTaskRequest,
    ) -> energy_expert_external_20220923_models.SubmitVLExtractionTaskResponse:
        """
        @summary Extracts key information from documents using KV templates or prompts with the Qwen-VL model, ideal for image extraction.
        Supports:
        URL Upload: SubmitVLExtractionTask.
        Local File Upload: SubmitVLExtractionTaskAdvance
        
        @param request: SubmitVLExtractionTaskRequest
        @return: SubmitVLExtractionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_vlextraction_task_with_options_async(request, headers, runtime)

    def submit_vlextraction_task_advance(
        self,
        request: energy_expert_external_20220923_models.SubmitVLExtractionTaskAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SubmitVLExtractionTaskResponse:
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
            'Product': 'energyExpertExternal',
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
        submit_vlextraction_task_req = energy_expert_external_20220923_models.SubmitVLExtractionTaskRequest()
        OpenApiUtilClient.convert(request, submit_vlextraction_task_req)
        if not UtilClient.is_unset(request.file_url_object):
            tmp_resp_0 = auth_client.call_api(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_url_object,
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
            submit_vlextraction_task_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_vlextraction_task_resp = self.submit_vlextraction_task_with_options(submit_vlextraction_task_req, headers, runtime)
        return submit_vlextraction_task_resp

    async def submit_vlextraction_task_advance_async(
        self,
        request: energy_expert_external_20220923_models.SubmitVLExtractionTaskAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> energy_expert_external_20220923_models.SubmitVLExtractionTaskResponse:
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
            'Product': 'energyExpertExternal',
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
        submit_vlextraction_task_req = energy_expert_external_20220923_models.SubmitVLExtractionTaskRequest()
        OpenApiUtilClient.convert(request, submit_vlextraction_task_req)
        if not UtilClient.is_unset(request.file_url_object):
            tmp_resp_0 = await auth_client.call_api_async(auth_params, auth_req, runtime)
            auth_response = UtilClient.assert_as_map(tmp_resp_0)
            tmp_body = UtilClient.assert_as_map(auth_response.get('body'))
            use_accelerate = UtilClient.assert_as_boolean(tmp_body.get('UseAccelerate'))
            auth_response_body = UtilClient.stringify_map_value(tmp_body)
            file_obj = file_form_models.FileField(
                filename=auth_response_body.get('ObjectKey'),
                content=request.file_url_object,
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
            submit_vlextraction_task_req.file_url = f"http://{auth_response_body.get('Bucket')}.{auth_response_body.get('Endpoint')}/{auth_response_body.get('ObjectKey')}"
        submit_vlextraction_task_resp = await self.submit_vlextraction_task_with_options_async(submit_vlextraction_task_req, headers, runtime)
        return submit_vlextraction_task_resp
