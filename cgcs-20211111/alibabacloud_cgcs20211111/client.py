# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cgcs20211111 import models as cgcs20211111_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cgcs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_check_session_with_options(
        self,
        tmp_req: cgcs20211111_models.BatchCheckSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.BatchCheckSessionResponse:
        """
        @summary 批量检查异常会话
        
        @param tmp_req: BatchCheckSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCheckSessionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.BatchCheckSessionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.records):
            request.records_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.records, 'Records', 'json')
        query = {}
        if not UtilClient.is_unset(request.records_shrink):
            query['Records'] = request.records_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCheckSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.BatchCheckSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_check_session_with_options_async(
        self,
        tmp_req: cgcs20211111_models.BatchCheckSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.BatchCheckSessionResponse:
        """
        @summary 批量检查异常会话
        
        @param tmp_req: BatchCheckSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCheckSessionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.BatchCheckSessionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.records):
            request.records_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.records, 'Records', 'json')
        query = {}
        if not UtilClient.is_unset(request.records_shrink):
            query['Records'] = request.records_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCheckSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.BatchCheckSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_check_session(
        self,
        request: cgcs20211111_models.BatchCheckSessionRequest,
    ) -> cgcs20211111_models.BatchCheckSessionResponse:
        """
        @summary 批量检查异常会话
        
        @param request: BatchCheckSessionRequest
        @return: BatchCheckSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_check_session_with_options(request, runtime)

    async def batch_check_session_async(
        self,
        request: cgcs20211111_models.BatchCheckSessionRequest,
    ) -> cgcs20211111_models.BatchCheckSessionResponse:
        """
        @summary 批量检查异常会话
        
        @param request: BatchCheckSessionRequest
        @return: BatchCheckSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_check_session_with_options_async(request, runtime)

    def cancel_reserve_task_with_options(
        self,
        request: cgcs20211111_models.CancelReserveTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CancelReserveTaskResponse:
        """
        @summary 取消 session 资源预定任务
        
        @param request: CancelReserveTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelReserveTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelReserveTask',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CancelReserveTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_reserve_task_with_options_async(
        self,
        request: cgcs20211111_models.CancelReserveTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CancelReserveTaskResponse:
        """
        @summary 取消 session 资源预定任务
        
        @param request: CancelReserveTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelReserveTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelReserveTask',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CancelReserveTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_reserve_task(
        self,
        request: cgcs20211111_models.CancelReserveTaskRequest,
    ) -> cgcs20211111_models.CancelReserveTaskResponse:
        """
        @summary 取消 session 资源预定任务
        
        @param request: CancelReserveTaskRequest
        @return: CancelReserveTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_reserve_task_with_options(request, runtime)

    async def cancel_reserve_task_async(
        self,
        request: cgcs20211111_models.CancelReserveTaskRequest,
    ) -> cgcs20211111_models.CancelReserveTaskResponse:
        """
        @summary 取消 session 资源预定任务
        
        @param request: CancelReserveTaskRequest
        @return: CancelReserveTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_reserve_task_with_options_async(request, runtime)

    def create_adaptation_with_options(
        self,
        tmp_req: cgcs20211111_models.CreateAdaptationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAdaptationResponse:
        """
        @summary 提交适配请求
        
        @param tmp_req: CreateAdaptationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAdaptationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.CreateAdaptationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.adapt_target):
            request.adapt_target_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.adapt_target, 'AdaptTarget', 'json')
        body = {}
        if not UtilClient.is_unset(request.adapt_target_shrink):
            body['AdaptTarget'] = request.adapt_target_shrink
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAdaptation',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAdaptationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_adaptation_with_options_async(
        self,
        tmp_req: cgcs20211111_models.CreateAdaptationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAdaptationResponse:
        """
        @summary 提交适配请求
        
        @param tmp_req: CreateAdaptationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAdaptationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.CreateAdaptationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.adapt_target):
            request.adapt_target_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.adapt_target, 'AdaptTarget', 'json')
        body = {}
        if not UtilClient.is_unset(request.adapt_target_shrink):
            body['AdaptTarget'] = request.adapt_target_shrink
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAdaptation',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAdaptationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_adaptation(
        self,
        request: cgcs20211111_models.CreateAdaptationRequest,
    ) -> cgcs20211111_models.CreateAdaptationResponse:
        """
        @summary 提交适配请求
        
        @param request: CreateAdaptationRequest
        @return: CreateAdaptationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_adaptation_with_options(request, runtime)

    async def create_adaptation_async(
        self,
        request: cgcs20211111_models.CreateAdaptationRequest,
    ) -> cgcs20211111_models.CreateAdaptationResponse:
        """
        @summary 提交适配请求
        
        @param request: CreateAdaptationRequest
        @return: CreateAdaptationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_adaptation_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        request: cgcs20211111_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppResponse:
        """
        @summary 应用创建服务
        
        @param request: CreateAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.streaming_app_id):
            body['StreamingAppId'] = request.streaming_app_id
        if not UtilClient.is_unset(request.streaming_solution):
            body['StreamingSolution'] = request.streaming_solution
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: cgcs20211111_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppResponse:
        """
        @summary 应用创建服务
        
        @param request: CreateAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.streaming_app_id):
            body['StreamingAppId'] = request.streaming_app_id
        if not UtilClient.is_unset(request.streaming_solution):
            body['StreamingSolution'] = request.streaming_solution
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        request: cgcs20211111_models.CreateAppRequest,
    ) -> cgcs20211111_models.CreateAppResponse:
        """
        @summary 应用创建服务
        
        @param request: CreateAppRequest
        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: cgcs20211111_models.CreateAppRequest,
    ) -> cgcs20211111_models.CreateAppResponse:
        """
        @summary 应用创建服务
        
        @param request: CreateAppRequest
        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_app_session_with_options(
        self,
        request: cgcs20211111_models.CreateAppSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppSessionResponse:
        """
        @summary 增加实时生产资源的相关字段
        
        @param request: CreateAppSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adapter_file_id):
            query['AdapterFileId'] = request.adapter_file_id
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.district_id):
            query['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.enable_postpaid):
            query['EnablePostpaid'] = request.enable_postpaid
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.start_parameters):
            query['StartParameters'] = request.start_parameters
        if not UtilClient.is_unset(request.system_info):
            query['SystemInfo'] = request.system_info
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_session_with_options_async(
        self,
        request: cgcs20211111_models.CreateAppSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppSessionResponse:
        """
        @summary 增加实时生产资源的相关字段
        
        @param request: CreateAppSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adapter_file_id):
            query['AdapterFileId'] = request.adapter_file_id
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.district_id):
            query['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.enable_postpaid):
            query['EnablePostpaid'] = request.enable_postpaid
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.start_parameters):
            query['StartParameters'] = request.start_parameters
        if not UtilClient.is_unset(request.system_info):
            query['SystemInfo'] = request.system_info
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_session(
        self,
        request: cgcs20211111_models.CreateAppSessionRequest,
    ) -> cgcs20211111_models.CreateAppSessionResponse:
        """
        @summary 增加实时生产资源的相关字段
        
        @param request: CreateAppSessionRequest
        @return: CreateAppSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_session_with_options(request, runtime)

    async def create_app_session_async(
        self,
        request: cgcs20211111_models.CreateAppSessionRequest,
    ) -> cgcs20211111_models.CreateAppSessionResponse:
        """
        @summary 增加实时生产资源的相关字段
        
        @param request: CreateAppSessionRequest
        @return: CreateAppSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_session_with_options_async(request, runtime)

    def create_app_session_batch_with_options(
        self,
        tmp_req: cgcs20211111_models.CreateAppSessionBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppSessionBatchResponse:
        """
        @summary 批量创建会话
        
        @param tmp_req: CreateAppSessionBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppSessionBatchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.CreateAppSessionBatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app_infos):
            request.app_infos_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app_infos, 'AppInfos', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_infos_shrink):
            query['AppInfos'] = request.app_infos_shrink
        if not UtilClient.is_unset(request.custom_task_id):
            query['CustomTaskId'] = request.custom_task_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSessionBatch',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppSessionBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_session_batch_with_options_async(
        self,
        tmp_req: cgcs20211111_models.CreateAppSessionBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppSessionBatchResponse:
        """
        @summary 批量创建会话
        
        @param tmp_req: CreateAppSessionBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppSessionBatchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.CreateAppSessionBatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app_infos):
            request.app_infos_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app_infos, 'AppInfos', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_infos_shrink):
            query['AppInfos'] = request.app_infos_shrink
        if not UtilClient.is_unset(request.custom_task_id):
            query['CustomTaskId'] = request.custom_task_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSessionBatch',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppSessionBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_session_batch(
        self,
        request: cgcs20211111_models.CreateAppSessionBatchRequest,
    ) -> cgcs20211111_models.CreateAppSessionBatchResponse:
        """
        @summary 批量创建会话
        
        @param request: CreateAppSessionBatchRequest
        @return: CreateAppSessionBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_session_batch_with_options(request, runtime)

    async def create_app_session_batch_async(
        self,
        request: cgcs20211111_models.CreateAppSessionBatchRequest,
    ) -> cgcs20211111_models.CreateAppSessionBatchResponse:
        """
        @summary 批量创建会话
        
        @param request: CreateAppSessionBatchRequest
        @return: CreateAppSessionBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_session_batch_with_options_async(request, runtime)

    def create_app_session_batch_sync_with_options(
        self,
        tmp_req: cgcs20211111_models.CreateAppSessionBatchSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppSessionBatchSyncResponse:
        """
        @summary 同步批量创建多个会话
        
        @param tmp_req: CreateAppSessionBatchSyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppSessionBatchSyncResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.CreateAppSessionBatchSyncShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app_infos):
            request.app_infos_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app_infos, 'AppInfos', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_infos_shrink):
            query['AppInfos'] = request.app_infos_shrink
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSessionBatchSync',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppSessionBatchSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_session_batch_sync_with_options_async(
        self,
        tmp_req: cgcs20211111_models.CreateAppSessionBatchSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppSessionBatchSyncResponse:
        """
        @summary 同步批量创建多个会话
        
        @param tmp_req: CreateAppSessionBatchSyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppSessionBatchSyncResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.CreateAppSessionBatchSyncShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app_infos):
            request.app_infos_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app_infos, 'AppInfos', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_infos_shrink):
            query['AppInfos'] = request.app_infos_shrink
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSessionBatchSync',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppSessionBatchSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_session_batch_sync(
        self,
        request: cgcs20211111_models.CreateAppSessionBatchSyncRequest,
    ) -> cgcs20211111_models.CreateAppSessionBatchSyncResponse:
        """
        @summary 同步批量创建多个会话
        
        @param request: CreateAppSessionBatchSyncRequest
        @return: CreateAppSessionBatchSyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_session_batch_sync_with_options(request, runtime)

    async def create_app_session_batch_sync_async(
        self,
        request: cgcs20211111_models.CreateAppSessionBatchSyncRequest,
    ) -> cgcs20211111_models.CreateAppSessionBatchSyncResponse:
        """
        @summary 同步批量创建多个会话
        
        @param request: CreateAppSessionBatchSyncRequest
        @return: CreateAppSessionBatchSyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_session_batch_sync_with_options_async(request, runtime)

    def create_app_session_sync_with_options(
        self,
        request: cgcs20211111_models.CreateAppSessionSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppSessionSyncResponse:
        """
        @summary 同步创建会话
        
        @param request: CreateAppSessionSyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppSessionSyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adapter_file_id):
            query['AdapterFileId'] = request.adapter_file_id
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.district_id):
            query['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.match_rules):
            query['MatchRules'] = request.match_rules
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.start_parameters):
            query['StartParameters'] = request.start_parameters
        if not UtilClient.is_unset(request.system_info):
            query['SystemInfo'] = request.system_info
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSessionSync',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppSessionSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_session_sync_with_options_async(
        self,
        request: cgcs20211111_models.CreateAppSessionSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppSessionSyncResponse:
        """
        @summary 同步创建会话
        
        @param request: CreateAppSessionSyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppSessionSyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adapter_file_id):
            query['AdapterFileId'] = request.adapter_file_id
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.district_id):
            query['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.match_rules):
            query['MatchRules'] = request.match_rules
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.start_parameters):
            query['StartParameters'] = request.start_parameters
        if not UtilClient.is_unset(request.system_info):
            query['SystemInfo'] = request.system_info
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppSessionSync',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppSessionSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_session_sync(
        self,
        request: cgcs20211111_models.CreateAppSessionSyncRequest,
    ) -> cgcs20211111_models.CreateAppSessionSyncResponse:
        """
        @summary 同步创建会话
        
        @param request: CreateAppSessionSyncRequest
        @return: CreateAppSessionSyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_session_sync_with_options(request, runtime)

    async def create_app_session_sync_async(
        self,
        request: cgcs20211111_models.CreateAppSessionSyncRequest,
    ) -> cgcs20211111_models.CreateAppSessionSyncResponse:
        """
        @summary 同步创建会话
        
        @param request: CreateAppSessionSyncRequest
        @return: CreateAppSessionSyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_session_sync_with_options_async(request, runtime)

    def create_app_version_with_options(
        self,
        request: cgcs20211111_models.CreateAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppVersionResponse:
        """
        @summary 应用版本创建服务
        
        @param request: CreateAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version_name):
            body['AppVersionName'] = request.app_version_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_version_with_options_async(
        self,
        request: cgcs20211111_models.CreateAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateAppVersionResponse:
        """
        @summary 应用版本创建服务
        
        @param request: CreateAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version_name):
            body['AppVersionName'] = request.app_version_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateAppVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_version(
        self,
        request: cgcs20211111_models.CreateAppVersionRequest,
    ) -> cgcs20211111_models.CreateAppVersionResponse:
        """
        @summary 应用版本创建服务
        
        @param request: CreateAppVersionRequest
        @return: CreateAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_version_with_options(request, runtime)

    async def create_app_version_async(
        self,
        request: cgcs20211111_models.CreateAppVersionRequest,
    ) -> cgcs20211111_models.CreateAppVersionResponse:
        """
        @summary 应用版本创建服务
        
        @param request: CreateAppVersionRequest
        @return: CreateAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_version_with_options_async(request, runtime)

    def create_capacity_reservation_with_options(
        self,
        request: cgcs20211111_models.CreateCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateCapacityReservationResponse:
        """
        @summary 预定session资源
        
        @param request: CreateCapacityReservationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCapacityReservationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.district_id):
            body['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.expect_resource_ready_time):
            body['ExpectResourceReadyTime'] = request.expect_resource_ready_time
        if not UtilClient.is_unset(request.expect_session_capacity):
            body['ExpectSessionCapacity'] = request.expect_session_capacity
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCapacityReservation',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateCapacityReservationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_capacity_reservation_with_options_async(
        self,
        request: cgcs20211111_models.CreateCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.CreateCapacityReservationResponse:
        """
        @summary 预定session资源
        
        @param request: CreateCapacityReservationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCapacityReservationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.district_id):
            body['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.expect_resource_ready_time):
            body['ExpectResourceReadyTime'] = request.expect_resource_ready_time
        if not UtilClient.is_unset(request.expect_session_capacity):
            body['ExpectSessionCapacity'] = request.expect_session_capacity
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCapacityReservation',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.CreateCapacityReservationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_capacity_reservation(
        self,
        request: cgcs20211111_models.CreateCapacityReservationRequest,
    ) -> cgcs20211111_models.CreateCapacityReservationResponse:
        """
        @summary 预定session资源
        
        @param request: CreateCapacityReservationRequest
        @return: CreateCapacityReservationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_capacity_reservation_with_options(request, runtime)

    async def create_capacity_reservation_async(
        self,
        request: cgcs20211111_models.CreateCapacityReservationRequest,
    ) -> cgcs20211111_models.CreateCapacityReservationResponse:
        """
        @summary 预定session资源
        
        @param request: CreateCapacityReservationRequest
        @return: CreateCapacityReservationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_capacity_reservation_with_options_async(request, runtime)

    def delete_app_with_options(
        self,
        request: cgcs20211111_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.DeleteAppResponse:
        """
        @summary 应用删除接口
        
        @param request: DeleteAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        request: cgcs20211111_models.DeleteAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.DeleteAppResponse:
        """
        @summary 应用删除接口
        
        @param request: DeleteAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.DeleteAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app(
        self,
        request: cgcs20211111_models.DeleteAppRequest,
    ) -> cgcs20211111_models.DeleteAppResponse:
        """
        @summary 应用删除接口
        
        @param request: DeleteAppRequest
        @return: DeleteAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_with_options(request, runtime)

    async def delete_app_async(
        self,
        request: cgcs20211111_models.DeleteAppRequest,
    ) -> cgcs20211111_models.DeleteAppResponse:
        """
        @summary 应用删除接口
        
        @param request: DeleteAppRequest
        @return: DeleteAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_with_options_async(request, runtime)

    def delete_app_version_with_options(
        self,
        request: cgcs20211111_models.DeleteAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.DeleteAppVersionResponse:
        """
        @summary 应用版本删除接口
        
        @param request: DeleteAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.DeleteAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_version_with_options_async(
        self,
        request: cgcs20211111_models.DeleteAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.DeleteAppVersionResponse:
        """
        @summary 应用版本删除接口
        
        @param request: DeleteAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.DeleteAppVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_version(
        self,
        request: cgcs20211111_models.DeleteAppVersionRequest,
    ) -> cgcs20211111_models.DeleteAppVersionResponse:
        """
        @summary 应用版本删除接口
        
        @param request: DeleteAppVersionRequest
        @return: DeleteAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_version_with_options(request, runtime)

    async def delete_app_version_async(
        self,
        request: cgcs20211111_models.DeleteAppVersionRequest,
    ) -> cgcs20211111_models.DeleteAppVersionResponse:
        """
        @summary 应用版本删除接口
        
        @param request: DeleteAppVersionRequest
        @return: DeleteAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_version_with_options_async(request, runtime)

    def get_adaptation_with_options(
        self,
        request: cgcs20211111_models.GetAdaptationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAdaptationResponse:
        """
        @summary 获取适配申请详情
        
        @param request: GetAdaptationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAdaptationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.adapt_apply_id):
            body['AdaptApplyId'] = request.adapt_apply_id
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAdaptation',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAdaptationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_adaptation_with_options_async(
        self,
        request: cgcs20211111_models.GetAdaptationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAdaptationResponse:
        """
        @summary 获取适配申请详情
        
        @param request: GetAdaptationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAdaptationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.adapt_apply_id):
            body['AdaptApplyId'] = request.adapt_apply_id
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAdaptation',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAdaptationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_adaptation(
        self,
        request: cgcs20211111_models.GetAdaptationRequest,
    ) -> cgcs20211111_models.GetAdaptationResponse:
        """
        @summary 获取适配申请详情
        
        @param request: GetAdaptationRequest
        @return: GetAdaptationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_adaptation_with_options(request, runtime)

    async def get_adaptation_async(
        self,
        request: cgcs20211111_models.GetAdaptationRequest,
    ) -> cgcs20211111_models.GetAdaptationResponse:
        """
        @summary 获取适配申请详情
        
        @param request: GetAdaptationRequest
        @return: GetAdaptationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_adaptation_with_options_async(request, runtime)

    def get_app_with_options(
        self,
        request: cgcs20211111_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAppResponse:
        """
        @summary 应用详情接口
        
        @param request: GetAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_with_options_async(
        self,
        request: cgcs20211111_models.GetAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAppResponse:
        """
        @summary 应用详情接口
        
        @param request: GetAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app(
        self,
        request: cgcs20211111_models.GetAppRequest,
    ) -> cgcs20211111_models.GetAppResponse:
        """
        @summary 应用详情接口
        
        @param request: GetAppRequest
        @return: GetAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_app_with_options(request, runtime)

    async def get_app_async(
        self,
        request: cgcs20211111_models.GetAppRequest,
    ) -> cgcs20211111_models.GetAppResponse:
        """
        @summary 应用详情接口
        
        @param request: GetAppRequest
        @return: GetAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_app_with_options_async(request, runtime)

    def get_app_ccu_with_options(
        self,
        request: cgcs20211111_models.GetAppCcuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAppCcuResponse:
        """
        @summary 查询会话并发数
        
        @param request: GetAppCcuRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppCcuResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppCcu',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppCcuResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_ccu_with_options_async(
        self,
        request: cgcs20211111_models.GetAppCcuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAppCcuResponse:
        """
        @summary 查询会话并发数
        
        @param request: GetAppCcuRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppCcuResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppCcu',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppCcuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_ccu(
        self,
        request: cgcs20211111_models.GetAppCcuRequest,
    ) -> cgcs20211111_models.GetAppCcuResponse:
        """
        @summary 查询会话并发数
        
        @param request: GetAppCcuRequest
        @return: GetAppCcuResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_app_ccu_with_options(request, runtime)

    async def get_app_ccu_async(
        self,
        request: cgcs20211111_models.GetAppCcuRequest,
    ) -> cgcs20211111_models.GetAppCcuResponse:
        """
        @summary 查询会话并发数
        
        @param request: GetAppCcuRequest
        @return: GetAppCcuResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_app_ccu_with_options_async(request, runtime)

    def get_app_session_with_options(
        self,
        request: cgcs20211111_models.GetAppSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAppSessionResponse:
        """
        @summary 获取App会话信息
        
        @param request: GetAppSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.platform_session_id):
            query['PlatformSessionId'] = request.platform_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_session_with_options_async(
        self,
        request: cgcs20211111_models.GetAppSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAppSessionResponse:
        """
        @summary 获取App会话信息
        
        @param request: GetAppSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.platform_session_id):
            query['PlatformSessionId'] = request.platform_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_session(
        self,
        request: cgcs20211111_models.GetAppSessionRequest,
    ) -> cgcs20211111_models.GetAppSessionResponse:
        """
        @summary 获取App会话信息
        
        @param request: GetAppSessionRequest
        @return: GetAppSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_app_session_with_options(request, runtime)

    async def get_app_session_async(
        self,
        request: cgcs20211111_models.GetAppSessionRequest,
    ) -> cgcs20211111_models.GetAppSessionResponse:
        """
        @summary 获取App会话信息
        
        @param request: GetAppSessionRequest
        @return: GetAppSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_app_session_with_options_async(request, runtime)

    def get_app_version_with_options(
        self,
        request: cgcs20211111_models.GetAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAppVersionResponse:
        """
        @summary 应用版本详情接口
        
        @param request: GetAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_version_with_options_async(
        self,
        request: cgcs20211111_models.GetAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetAppVersionResponse:
        """
        @summary 应用版本详情接口
        
        @param request: GetAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetAppVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_version(
        self,
        request: cgcs20211111_models.GetAppVersionRequest,
    ) -> cgcs20211111_models.GetAppVersionResponse:
        """
        @summary 应用版本详情接口
        
        @param request: GetAppVersionRequest
        @return: GetAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_app_version_with_options(request, runtime)

    async def get_app_version_async(
        self,
        request: cgcs20211111_models.GetAppVersionRequest,
    ) -> cgcs20211111_models.GetAppVersionResponse:
        """
        @summary 应用版本详情接口
        
        @param request: GetAppVersionRequest
        @return: GetAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_app_version_with_options_async(request, runtime)

    def get_capacity_with_options(
        self,
        request: cgcs20211111_models.GetCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetCapacityResponse:
        """
        @summary 查询 session 会话容量信息
        
        @param request: GetCapacityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCapacityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.district_id):
            body['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCapacity',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_capacity_with_options_async(
        self,
        request: cgcs20211111_models.GetCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetCapacityResponse:
        """
        @summary 查询 session 会话容量信息
        
        @param request: GetCapacityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCapacityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.district_id):
            body['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCapacity',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetCapacityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_capacity(
        self,
        request: cgcs20211111_models.GetCapacityRequest,
    ) -> cgcs20211111_models.GetCapacityResponse:
        """
        @summary 查询 session 会话容量信息
        
        @param request: GetCapacityRequest
        @return: GetCapacityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_capacity_with_options(request, runtime)

    async def get_capacity_async(
        self,
        request: cgcs20211111_models.GetCapacityRequest,
    ) -> cgcs20211111_models.GetCapacityResponse:
        """
        @summary 查询 session 会话容量信息
        
        @param request: GetCapacityRequest
        @return: GetCapacityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_capacity_with_options_async(request, runtime)

    def get_reserve_task_detail_with_options(
        self,
        request: cgcs20211111_models.GetReserveTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetReserveTaskDetailResponse:
        """
        @summary 查询预定任务的详情信息
        
        @param request: GetReserveTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetReserveTaskDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetReserveTaskDetail',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetReserveTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_reserve_task_detail_with_options_async(
        self,
        request: cgcs20211111_models.GetReserveTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetReserveTaskDetailResponse:
        """
        @summary 查询预定任务的详情信息
        
        @param request: GetReserveTaskDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetReserveTaskDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetReserveTaskDetail',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetReserveTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_reserve_task_detail(
        self,
        request: cgcs20211111_models.GetReserveTaskDetailRequest,
    ) -> cgcs20211111_models.GetReserveTaskDetailResponse:
        """
        @summary 查询预定任务的详情信息
        
        @param request: GetReserveTaskDetailRequest
        @return: GetReserveTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_reserve_task_detail_with_options(request, runtime)

    async def get_reserve_task_detail_async(
        self,
        request: cgcs20211111_models.GetReserveTaskDetailRequest,
    ) -> cgcs20211111_models.GetReserveTaskDetailResponse:
        """
        @summary 查询预定任务的详情信息
        
        @param request: GetReserveTaskDetailRequest
        @return: GetReserveTaskDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_reserve_task_detail_with_options_async(request, runtime)

    def get_resource_public_ips_with_options(
        self,
        request: cgcs20211111_models.GetResourcePublicIPsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetResourcePublicIPsResponse:
        """
        @summary 查询公网ip
        
        @param request: GetResourcePublicIPsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourcePublicIPsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetResourcePublicIPs',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetResourcePublicIPsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_public_ips_with_options_async(
        self,
        request: cgcs20211111_models.GetResourcePublicIPsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.GetResourcePublicIPsResponse:
        """
        @summary 查询公网ip
        
        @param request: GetResourcePublicIPsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourcePublicIPsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetResourcePublicIPs',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.GetResourcePublicIPsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_public_ips(
        self,
        request: cgcs20211111_models.GetResourcePublicIPsRequest,
    ) -> cgcs20211111_models.GetResourcePublicIPsResponse:
        """
        @summary 查询公网ip
        
        @param request: GetResourcePublicIPsRequest
        @return: GetResourcePublicIPsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_public_ips_with_options(request, runtime)

    async def get_resource_public_ips_async(
        self,
        request: cgcs20211111_models.GetResourcePublicIPsRequest,
    ) -> cgcs20211111_models.GetResourcePublicIPsResponse:
        """
        @summary 查询公网ip
        
        @param request: GetResourcePublicIPsRequest
        @return: GetResourcePublicIPsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_public_ips_with_options_async(request, runtime)

    def list_app_with_options(
        self,
        request: cgcs20211111_models.ListAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ListAppResponse:
        """
        @summary 应用列表接口
        
        @param request: ListAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key_search):
            body['KeySearch'] = request.key_search
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ListAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_with_options_async(
        self,
        request: cgcs20211111_models.ListAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ListAppResponse:
        """
        @summary 应用列表接口
        
        @param request: ListAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.key_search):
            body['KeySearch'] = request.key_search
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ListAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app(
        self,
        request: cgcs20211111_models.ListAppRequest,
    ) -> cgcs20211111_models.ListAppResponse:
        """
        @summary 应用列表接口
        
        @param request: ListAppRequest
        @return: ListAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_app_with_options(request, runtime)

    async def list_app_async(
        self,
        request: cgcs20211111_models.ListAppRequest,
    ) -> cgcs20211111_models.ListAppResponse:
        """
        @summary 应用列表接口
        
        @param request: ListAppRequest
        @return: ListAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_app_with_options_async(request, runtime)

    def list_app_sessions_with_options(
        self,
        request: cgcs20211111_models.ListAppSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ListAppSessionsResponse:
        """
        @summary 查询App会话
        
        @param request: ListAppSessionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppSessionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.custom_session_ids):
            query['CustomSessionIds'] = request.custom_session_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform_session_ids):
            query['PlatformSessionIds'] = request.platform_session_ids
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppSessions',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ListAppSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_sessions_with_options_async(
        self,
        request: cgcs20211111_models.ListAppSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ListAppSessionsResponse:
        """
        @summary 查询App会话
        
        @param request: ListAppSessionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppSessionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.custom_session_ids):
            query['CustomSessionIds'] = request.custom_session_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform_session_ids):
            query['PlatformSessionIds'] = request.platform_session_ids
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppSessions',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ListAppSessionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_sessions(
        self,
        request: cgcs20211111_models.ListAppSessionsRequest,
    ) -> cgcs20211111_models.ListAppSessionsResponse:
        """
        @summary 查询App会话
        
        @param request: ListAppSessionsRequest
        @return: ListAppSessionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_app_sessions_with_options(request, runtime)

    async def list_app_sessions_async(
        self,
        request: cgcs20211111_models.ListAppSessionsRequest,
    ) -> cgcs20211111_models.ListAppSessionsResponse:
        """
        @summary 查询App会话
        
        @param request: ListAppSessionsRequest
        @return: ListAppSessionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_app_sessions_with_options_async(request, runtime)

    def list_app_version_with_options(
        self,
        request: cgcs20211111_models.ListAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ListAppVersionResponse:
        """
        @summary 应用版本列表接口
        
        @param request: ListAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ListAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_version_with_options_async(
        self,
        request: cgcs20211111_models.ListAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ListAppVersionResponse:
        """
        @summary 应用版本列表接口
        
        @param request: ListAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ListAppVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_version(
        self,
        request: cgcs20211111_models.ListAppVersionRequest,
    ) -> cgcs20211111_models.ListAppVersionResponse:
        """
        @summary 应用版本列表接口
        
        @param request: ListAppVersionRequest
        @return: ListAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_app_version_with_options(request, runtime)

    async def list_app_version_async(
        self,
        request: cgcs20211111_models.ListAppVersionRequest,
    ) -> cgcs20211111_models.ListAppVersionResponse:
        """
        @summary 应用版本列表接口
        
        @param request: ListAppVersionRequest
        @return: ListAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_app_version_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: cgcs20211111_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ListInstancesResponse:
        """
        @summary 查询GCS实例列表
        
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: cgcs20211111_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ListInstancesResponse:
        """
        @summary 查询GCS实例列表
        
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: cgcs20211111_models.ListInstancesRequest,
    ) -> cgcs20211111_models.ListInstancesResponse:
        """
        @summary 查询GCS实例列表
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: cgcs20211111_models.ListInstancesRequest,
    ) -> cgcs20211111_models.ListInstancesResponse:
        """
        @summary 查询GCS实例列表
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def modify_app_with_options(
        self,
        request: cgcs20211111_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ModifyAppResponse:
        """
        @summary 应用修改服务
        
        @param request: ModifyAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ModifyAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_with_options_async(
        self,
        request: cgcs20211111_models.ModifyAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ModifyAppResponse:
        """
        @summary 应用修改服务
        
        @param request: ModifyAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyApp',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ModifyAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app(
        self,
        request: cgcs20211111_models.ModifyAppRequest,
    ) -> cgcs20211111_models.ModifyAppResponse:
        """
        @summary 应用修改服务
        
        @param request: ModifyAppRequest
        @return: ModifyAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    async def modify_app_async(
        self,
        request: cgcs20211111_models.ModifyAppRequest,
    ) -> cgcs20211111_models.ModifyAppResponse:
        """
        @summary 应用修改服务
        
        @param request: ModifyAppRequest
        @return: ModifyAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_with_options_async(request, runtime)

    def modify_app_version_with_options(
        self,
        request: cgcs20211111_models.ModifyAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ModifyAppVersionResponse:
        """
        @summary 应用版本修改服务
        
        @param request: ModifyAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        if not UtilClient.is_unset(request.app_version_name):
            body['AppVersionName'] = request.app_version_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ModifyAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_version_with_options_async(
        self,
        request: cgcs20211111_models.ModifyAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ModifyAppVersionResponse:
        """
        @summary 应用版本修改服务
        
        @param request: ModifyAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAppVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_version_id):
            body['AppVersionId'] = request.app_version_id
        if not UtilClient.is_unset(request.app_version_name):
            body['AppVersionName'] = request.app_version_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyAppVersion',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ModifyAppVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_version(
        self,
        request: cgcs20211111_models.ModifyAppVersionRequest,
    ) -> cgcs20211111_models.ModifyAppVersionResponse:
        """
        @summary 应用版本修改服务
        
        @param request: ModifyAppVersionRequest
        @return: ModifyAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_app_version_with_options(request, runtime)

    async def modify_app_version_async(
        self,
        request: cgcs20211111_models.ModifyAppVersionRequest,
    ) -> cgcs20211111_models.ModifyAppVersionResponse:
        """
        @summary 应用版本修改服务
        
        @param request: ModifyAppVersionRequest
        @return: ModifyAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_app_version_with_options_async(request, runtime)

    def release_capacity_with_options(
        self,
        request: cgcs20211111_models.ReleaseCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ReleaseCapacityResponse:
        """
        @summary 释放 session 资源预定的资源
        
        @param request: ReleaseCapacityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseCapacityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.district_id):
            body['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.expect_release_session_capacity):
            body['ExpectReleaseSessionCapacity'] = request.expect_release_session_capacity
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseCapacity',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ReleaseCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_capacity_with_options_async(
        self,
        request: cgcs20211111_models.ReleaseCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ReleaseCapacityResponse:
        """
        @summary 释放 session 资源预定的资源
        
        @param request: ReleaseCapacityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseCapacityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.district_id):
            body['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.expect_release_session_capacity):
            body['ExpectReleaseSessionCapacity'] = request.expect_release_session_capacity
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseCapacity',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ReleaseCapacityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_capacity(
        self,
        request: cgcs20211111_models.ReleaseCapacityRequest,
    ) -> cgcs20211111_models.ReleaseCapacityResponse:
        """
        @summary 释放 session 资源预定的资源
        
        @param request: ReleaseCapacityRequest
        @return: ReleaseCapacityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_capacity_with_options(request, runtime)

    async def release_capacity_async(
        self,
        request: cgcs20211111_models.ReleaseCapacityRequest,
    ) -> cgcs20211111_models.ReleaseCapacityResponse:
        """
        @summary 释放 session 资源预定的资源
        
        @param request: ReleaseCapacityRequest
        @return: ReleaseCapacityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_capacity_with_options_async(request, runtime)

    def release_capacity_by_batch_with_options(
        self,
        request: cgcs20211111_models.ReleaseCapacityByBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ReleaseCapacityByBatchResponse:
        """
        @summary 根据资源批次号释放 session 资源预定的资源
        
        @param request: ReleaseCapacityByBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseCapacityByBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.res_batch_id):
            body['ResBatchId'] = request.res_batch_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseCapacityByBatch',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ReleaseCapacityByBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_capacity_by_batch_with_options_async(
        self,
        request: cgcs20211111_models.ReleaseCapacityByBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ReleaseCapacityByBatchResponse:
        """
        @summary 根据资源批次号释放 session 资源预定的资源
        
        @param request: ReleaseCapacityByBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseCapacityByBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.res_batch_id):
            body['ResBatchId'] = request.res_batch_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseCapacityByBatch',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ReleaseCapacityByBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_capacity_by_batch(
        self,
        request: cgcs20211111_models.ReleaseCapacityByBatchRequest,
    ) -> cgcs20211111_models.ReleaseCapacityByBatchResponse:
        """
        @summary 根据资源批次号释放 session 资源预定的资源
        
        @param request: ReleaseCapacityByBatchRequest
        @return: ReleaseCapacityByBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_capacity_by_batch_with_options(request, runtime)

    async def release_capacity_by_batch_async(
        self,
        request: cgcs20211111_models.ReleaseCapacityByBatchRequest,
    ) -> cgcs20211111_models.ReleaseCapacityByBatchResponse:
        """
        @summary 根据资源批次号释放 session 资源预定的资源
        
        @param request: ReleaseCapacityByBatchRequest
        @return: ReleaseCapacityByBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_capacity_by_batch_with_options_async(request, runtime)

    def release_instances_with_options(
        self,
        request: cgcs20211111_models.ReleaseInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ReleaseInstancesResponse:
        """
        @summary 退订GCS实例
        
        @param request: ReleaseInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstancesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amount):
            body['Amount'] = request.amount
        if not UtilClient.is_unset(request.district_id):
            body['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseInstances',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ReleaseInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instances_with_options_async(
        self,
        request: cgcs20211111_models.ReleaseInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ReleaseInstancesResponse:
        """
        @summary 退订GCS实例
        
        @param request: ReleaseInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstancesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amount):
            body['Amount'] = request.amount
        if not UtilClient.is_unset(request.district_id):
            body['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseInstances',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ReleaseInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instances(
        self,
        request: cgcs20211111_models.ReleaseInstancesRequest,
    ) -> cgcs20211111_models.ReleaseInstancesResponse:
        """
        @summary 退订GCS实例
        
        @param request: ReleaseInstancesRequest
        @return: ReleaseInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_instances_with_options(request, runtime)

    async def release_instances_async(
        self,
        request: cgcs20211111_models.ReleaseInstancesRequest,
    ) -> cgcs20211111_models.ReleaseInstancesResponse:
        """
        @summary 退订GCS实例
        
        @param request: ReleaseInstancesRequest
        @return: ReleaseInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_instances_with_options_async(request, runtime)

    def reserve_instances_with_options(
        self,
        request: cgcs20211111_models.ReserveInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ReserveInstancesResponse:
        """
        @summary 预定GCS实例
        
        @param request: ReserveInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReserveInstancesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amount):
            body['Amount'] = request.amount
        if not UtilClient.is_unset(request.district_id):
            body['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReserveInstances',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ReserveInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def reserve_instances_with_options_async(
        self,
        request: cgcs20211111_models.ReserveInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.ReserveInstancesResponse:
        """
        @summary 预定GCS实例
        
        @param request: ReserveInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReserveInstancesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amount):
            body['Amount'] = request.amount
        if not UtilClient.is_unset(request.district_id):
            body['DistrictId'] = request.district_id
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReserveInstances',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.ReserveInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reserve_instances(
        self,
        request: cgcs20211111_models.ReserveInstancesRequest,
    ) -> cgcs20211111_models.ReserveInstancesResponse:
        """
        @summary 预定GCS实例
        
        @param request: ReserveInstancesRequest
        @return: ReserveInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reserve_instances_with_options(request, runtime)

    async def reserve_instances_async(
        self,
        request: cgcs20211111_models.ReserveInstancesRequest,
    ) -> cgcs20211111_models.ReserveInstancesResponse:
        """
        @summary 预定GCS实例
        
        @param request: ReserveInstancesRequest
        @return: ReserveInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reserve_instances_with_options_async(request, runtime)

    def send_biz_coc_change_callback_with_options(
        self,
        request: cgcs20211111_models.SendBizCocChangeCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.SendBizCocChangeCallbackResponse:
        """
        @summary 发送业务能力变更结果回调
        
        @param request: SendBizCocChangeCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendBizCocChangeCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.platform_session_id):
            query['PlatformSessionId'] = request.platform_session_id
        if not UtilClient.is_unset(request.result):
            query['Result'] = request.result
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendBizCocChangeCallback',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.SendBizCocChangeCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_biz_coc_change_callback_with_options_async(
        self,
        request: cgcs20211111_models.SendBizCocChangeCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.SendBizCocChangeCallbackResponse:
        """
        @summary 发送业务能力变更结果回调
        
        @param request: SendBizCocChangeCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendBizCocChangeCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.platform_session_id):
            query['PlatformSessionId'] = request.platform_session_id
        if not UtilClient.is_unset(request.result):
            query['Result'] = request.result
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendBizCocChangeCallback',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.SendBizCocChangeCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_biz_coc_change_callback(
        self,
        request: cgcs20211111_models.SendBizCocChangeCallbackRequest,
    ) -> cgcs20211111_models.SendBizCocChangeCallbackResponse:
        """
        @summary 发送业务能力变更结果回调
        
        @param request: SendBizCocChangeCallbackRequest
        @return: SendBizCocChangeCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_biz_coc_change_callback_with_options(request, runtime)

    async def send_biz_coc_change_callback_async(
        self,
        request: cgcs20211111_models.SendBizCocChangeCallbackRequest,
    ) -> cgcs20211111_models.SendBizCocChangeCallbackResponse:
        """
        @summary 发送业务能力变更结果回调
        
        @param request: SendBizCocChangeCallbackRequest
        @return: SendBizCocChangeCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_biz_coc_change_callback_with_options_async(request, runtime)

    def stop_app_session_with_options(
        self,
        tmp_req: cgcs20211111_models.StopAppSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.StopAppSessionResponse:
        """
        @summary 停止App会话
        
        @param tmp_req: StopAppSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAppSessionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.StopAppSessionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stop_param):
            request.stop_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stop_param, 'StopParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.platform_session_id):
            query['PlatformSessionId'] = request.platform_session_id
        if not UtilClient.is_unset(request.stop_param_shrink):
            query['StopParam'] = request.stop_param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.StopAppSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_app_session_with_options_async(
        self,
        tmp_req: cgcs20211111_models.StopAppSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.StopAppSessionResponse:
        """
        @summary 停止App会话
        
        @param tmp_req: StopAppSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAppSessionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.StopAppSessionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stop_param):
            request.stop_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stop_param, 'StopParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.custom_session_id):
            query['CustomSessionId'] = request.custom_session_id
        if not UtilClient.is_unset(request.platform_session_id):
            query['PlatformSessionId'] = request.platform_session_id
        if not UtilClient.is_unset(request.stop_param_shrink):
            query['StopParam'] = request.stop_param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAppSession',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.StopAppSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_app_session(
        self,
        request: cgcs20211111_models.StopAppSessionRequest,
    ) -> cgcs20211111_models.StopAppSessionResponse:
        """
        @summary 停止App会话
        
        @param request: StopAppSessionRequest
        @return: StopAppSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_app_session_with_options(request, runtime)

    async def stop_app_session_async(
        self,
        request: cgcs20211111_models.StopAppSessionRequest,
    ) -> cgcs20211111_models.StopAppSessionResponse:
        """
        @summary 停止App会话
        
        @param request: StopAppSessionRequest
        @return: StopAppSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_app_session_with_options_async(request, runtime)

    def stop_app_session_batch_with_options(
        self,
        tmp_req: cgcs20211111_models.StopAppSessionBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.StopAppSessionBatchResponse:
        """
        @summary 批量停止会话接口
        
        @param tmp_req: StopAppSessionBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAppSessionBatchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.StopAppSessionBatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stop_param):
            request.stop_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stop_param, 'StopParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.stop_param_shrink):
            query['StopParam'] = request.stop_param_shrink
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAppSessionBatch',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.StopAppSessionBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_app_session_batch_with_options_async(
        self,
        tmp_req: cgcs20211111_models.StopAppSessionBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.StopAppSessionBatchResponse:
        """
        @summary 批量停止会话接口
        
        @param tmp_req: StopAppSessionBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAppSessionBatchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cgcs20211111_models.StopAppSessionBatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stop_param):
            request.stop_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stop_param, 'StopParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.stop_param_shrink):
            query['StopParam'] = request.stop_param_shrink
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAppSessionBatch',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.StopAppSessionBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_app_session_batch(
        self,
        request: cgcs20211111_models.StopAppSessionBatchRequest,
    ) -> cgcs20211111_models.StopAppSessionBatchResponse:
        """
        @summary 批量停止会话接口
        
        @param request: StopAppSessionBatchRequest
        @return: StopAppSessionBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_app_session_batch_with_options(request, runtime)

    async def stop_app_session_batch_async(
        self,
        request: cgcs20211111_models.StopAppSessionBatchRequest,
    ) -> cgcs20211111_models.StopAppSessionBatchResponse:
        """
        @summary 批量停止会话接口
        
        @param request: StopAppSessionBatchRequest
        @return: StopAppSessionBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_app_session_batch_with_options_async(request, runtime)

    def update_session_biz_status_with_options(
        self,
        request: cgcs20211111_models.UpdateSessionBizStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.UpdateSessionBizStatusResponse:
        """
        @summary 更新会话状态
        
        @param request: UpdateSessionBizStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSessionBizStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_status):
            query['BizStatus'] = request.biz_status
        if not UtilClient.is_unset(request.platform_session_id):
            query['PlatformSessionId'] = request.platform_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSessionBizStatus',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.UpdateSessionBizStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_session_biz_status_with_options_async(
        self,
        request: cgcs20211111_models.UpdateSessionBizStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cgcs20211111_models.UpdateSessionBizStatusResponse:
        """
        @summary 更新会话状态
        
        @param request: UpdateSessionBizStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSessionBizStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_status):
            query['BizStatus'] = request.biz_status
        if not UtilClient.is_unset(request.platform_session_id):
            query['PlatformSessionId'] = request.platform_session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSessionBizStatus',
            version='2021-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cgcs20211111_models.UpdateSessionBizStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_session_biz_status(
        self,
        request: cgcs20211111_models.UpdateSessionBizStatusRequest,
    ) -> cgcs20211111_models.UpdateSessionBizStatusResponse:
        """
        @summary 更新会话状态
        
        @param request: UpdateSessionBizStatusRequest
        @return: UpdateSessionBizStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_session_biz_status_with_options(request, runtime)

    async def update_session_biz_status_async(
        self,
        request: cgcs20211111_models.UpdateSessionBizStatusRequest,
    ) -> cgcs20211111_models.UpdateSessionBizStatusResponse:
        """
        @summary 更新会话状态
        
        @param request: UpdateSessionBizStatusRequest
        @return: UpdateSessionBizStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_session_biz_status_with_options_async(request, runtime)
