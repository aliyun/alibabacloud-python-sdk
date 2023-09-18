# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_avatar20220130 import models as avatar_20220130_models
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
        self._endpoint = self.get_endpoint('avatar', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_video_task_with_options(
        self,
        tmp_req: avatar_20220130_models.CancelVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.CancelVideoTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.CancelVideoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.task_uuid):
            query['TaskUuid'] = request.task_uuid
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelVideoTask',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.CancelVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_video_task_with_options_async(
        self,
        tmp_req: avatar_20220130_models.CancelVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.CancelVideoTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.CancelVideoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.task_uuid):
            query['TaskUuid'] = request.task_uuid
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelVideoTask',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.CancelVideoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_video_task(
        self,
        request: avatar_20220130_models.CancelVideoTaskRequest,
    ) -> avatar_20220130_models.CancelVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_video_task_with_options(request, runtime)

    async def cancel_video_task_async(
        self,
        request: avatar_20220130_models.CancelVideoTaskRequest,
    ) -> avatar_20220130_models.CancelVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_video_task_with_options_async(request, runtime)

    def client_auth_with_options(
        self,
        request: avatar_20220130_models.ClientAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.ClientAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.device_info):
            query['DeviceInfo'] = request.device_info
        if not UtilClient.is_unset(request.device_type):
            query['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.license):
            query['License'] = request.license
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClientAuth',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.ClientAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def client_auth_with_options_async(
        self,
        request: avatar_20220130_models.ClientAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.ClientAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.device_info):
            query['DeviceInfo'] = request.device_info
        if not UtilClient.is_unset(request.device_type):
            query['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.license):
            query['License'] = request.license
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClientAuth',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.ClientAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def client_auth(
        self,
        request: avatar_20220130_models.ClientAuthRequest,
    ) -> avatar_20220130_models.ClientAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.client_auth_with_options(request, runtime)

    async def client_auth_async(
        self,
        request: avatar_20220130_models.ClientAuthRequest,
    ) -> avatar_20220130_models.ClientAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.client_auth_with_options_async(request, runtime)

    def client_start_with_options(
        self,
        request: avatar_20220130_models.ClientStartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.ClientStartResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClientStart',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.ClientStartResponse(),
            self.call_api(params, req, runtime)
        )

    async def client_start_with_options_async(
        self,
        request: avatar_20220130_models.ClientStartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.ClientStartResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClientStart',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.ClientStartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def client_start(
        self,
        request: avatar_20220130_models.ClientStartRequest,
    ) -> avatar_20220130_models.ClientStartResponse:
        runtime = util_models.RuntimeOptions()
        return self.client_start_with_options(request, runtime)

    async def client_start_async(
        self,
        request: avatar_20220130_models.ClientStartRequest,
    ) -> avatar_20220130_models.ClientStartResponse:
        runtime = util_models.RuntimeOptions()
        return await self.client_start_with_options_async(request, runtime)

    def close_timed_reset_operate_with_options(
        self,
        request: avatar_20220130_models.CloseTimedResetOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.CloseTimedResetOperateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseTimedResetOperate',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.CloseTimedResetOperateResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_timed_reset_operate_with_options_async(
        self,
        request: avatar_20220130_models.CloseTimedResetOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.CloseTimedResetOperateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseTimedResetOperate',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.CloseTimedResetOperateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_timed_reset_operate(
        self,
        request: avatar_20220130_models.CloseTimedResetOperateRequest,
    ) -> avatar_20220130_models.CloseTimedResetOperateResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_timed_reset_operate_with_options(request, runtime)

    async def close_timed_reset_operate_async(
        self,
        request: avatar_20220130_models.CloseTimedResetOperateRequest,
    ) -> avatar_20220130_models.CloseTimedResetOperateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_timed_reset_operate_with_options_async(request, runtime)

    def create_2d_avatar_with_options(
        self,
        request: avatar_20220130_models.Create2dAvatarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.Create2dAvatarResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.orientation):
            query['Orientation'] = request.orientation
        if not UtilClient.is_unset(request.portrait):
            query['Portrait'] = request.portrait
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.transparent):
            query['Transparent'] = request.transparent
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Create2dAvatar',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.Create2dAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_2d_avatar_with_options_async(
        self,
        request: avatar_20220130_models.Create2dAvatarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.Create2dAvatarResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.orientation):
            query['Orientation'] = request.orientation
        if not UtilClient.is_unset(request.portrait):
            query['Portrait'] = request.portrait
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.transparent):
            query['Transparent'] = request.transparent
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Create2dAvatar',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.Create2dAvatarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_2d_avatar(
        self,
        request: avatar_20220130_models.Create2dAvatarRequest,
    ) -> avatar_20220130_models.Create2dAvatarResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_2d_avatar_with_options(request, runtime)

    async def create_2d_avatar_async(
        self,
        request: avatar_20220130_models.Create2dAvatarRequest,
    ) -> avatar_20220130_models.Create2dAvatarResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_2d_avatar_with_options_async(request, runtime)

    def delete_avatar_with_options(
        self,
        request: avatar_20220130_models.DeleteAvatarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.DeleteAvatarResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAvatar',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.DeleteAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_avatar_with_options_async(
        self,
        request: avatar_20220130_models.DeleteAvatarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.DeleteAvatarResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAvatar',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.DeleteAvatarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_avatar(
        self,
        request: avatar_20220130_models.DeleteAvatarRequest,
    ) -> avatar_20220130_models.DeleteAvatarResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_avatar_with_options(request, runtime)

    async def delete_avatar_async(
        self,
        request: avatar_20220130_models.DeleteAvatarRequest,
    ) -> avatar_20220130_models.DeleteAvatarResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_avatar_with_options_async(request, runtime)

    def duplex_decision_with_options(
        self,
        tmp_req: avatar_20220130_models.DuplexDecisionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.DuplexDecisionResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.DuplexDecisionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_keywords):
            request.custom_keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_keywords, 'CustomKeywords', 'json')
        if not UtilClient.is_unset(tmp_req.dialog_context):
            request.dialog_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dialog_context, 'DialogContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.biz_request_id):
            query['BizRequestId'] = request.biz_request_id
        if not UtilClient.is_unset(request.call_time):
            query['CallTime'] = request.call_time
        if not UtilClient.is_unset(request.custom_keywords_shrink):
            query['CustomKeywords'] = request.custom_keywords_shrink
        if not UtilClient.is_unset(request.dialog_context_shrink):
            query['DialogContext'] = request.dialog_context_shrink
        if not UtilClient.is_unset(request.dialog_status):
            query['DialogStatus'] = request.dialog_status
        if not UtilClient.is_unset(request.interrupt_type):
            query['InterruptType'] = request.interrupt_type
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DuplexDecision',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.DuplexDecisionResponse(),
            self.call_api(params, req, runtime)
        )

    async def duplex_decision_with_options_async(
        self,
        tmp_req: avatar_20220130_models.DuplexDecisionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.DuplexDecisionResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.DuplexDecisionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_keywords):
            request.custom_keywords_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_keywords, 'CustomKeywords', 'json')
        if not UtilClient.is_unset(tmp_req.dialog_context):
            request.dialog_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dialog_context, 'DialogContext', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.biz_request_id):
            query['BizRequestId'] = request.biz_request_id
        if not UtilClient.is_unset(request.call_time):
            query['CallTime'] = request.call_time
        if not UtilClient.is_unset(request.custom_keywords_shrink):
            query['CustomKeywords'] = request.custom_keywords_shrink
        if not UtilClient.is_unset(request.dialog_context_shrink):
            query['DialogContext'] = request.dialog_context_shrink
        if not UtilClient.is_unset(request.dialog_status):
            query['DialogStatus'] = request.dialog_status
        if not UtilClient.is_unset(request.interrupt_type):
            query['InterruptType'] = request.interrupt_type
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DuplexDecision',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.DuplexDecisionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def duplex_decision(
        self,
        request: avatar_20220130_models.DuplexDecisionRequest,
    ) -> avatar_20220130_models.DuplexDecisionResponse:
        runtime = util_models.RuntimeOptions()
        return self.duplex_decision_with_options(request, runtime)

    async def duplex_decision_async(
        self,
        request: avatar_20220130_models.DuplexDecisionRequest,
    ) -> avatar_20220130_models.DuplexDecisionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.duplex_decision_with_options_async(request, runtime)

    def get_video_task_info_with_options(
        self,
        tmp_req: avatar_20220130_models.GetVideoTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.GetVideoTaskInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.GetVideoTaskInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoTaskInfo',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.GetVideoTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_task_info_with_options_async(
        self,
        tmp_req: avatar_20220130_models.GetVideoTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.GetVideoTaskInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.GetVideoTaskInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoTaskInfo',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.GetVideoTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_task_info(
        self,
        request: avatar_20220130_models.GetVideoTaskInfoRequest,
    ) -> avatar_20220130_models.GetVideoTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_task_info_with_options(request, runtime)

    async def get_video_task_info_async(
        self,
        request: avatar_20220130_models.GetVideoTaskInfoRequest,
    ) -> avatar_20220130_models.GetVideoTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_task_info_with_options_async(request, runtime)

    def license_auth_with_options(
        self,
        request: avatar_20220130_models.LicenseAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.LicenseAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.license):
            query['License'] = request.license
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LicenseAuth',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.LicenseAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def license_auth_with_options_async(
        self,
        request: avatar_20220130_models.LicenseAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.LicenseAuthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.license):
            query['License'] = request.license
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LicenseAuth',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.LicenseAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def license_auth(
        self,
        request: avatar_20220130_models.LicenseAuthRequest,
    ) -> avatar_20220130_models.LicenseAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.license_auth_with_options(request, runtime)

    async def license_auth_async(
        self,
        request: avatar_20220130_models.LicenseAuthRequest,
    ) -> avatar_20220130_models.LicenseAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.license_auth_with_options_async(request, runtime)

    def query_avatar_with_options(
        self,
        request: avatar_20220130_models.QueryAvatarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.QueryAvatarResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAvatar',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.QueryAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_avatar_with_options_async(
        self,
        request: avatar_20220130_models.QueryAvatarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.QueryAvatarResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAvatar',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.QueryAvatarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_avatar(
        self,
        request: avatar_20220130_models.QueryAvatarRequest,
    ) -> avatar_20220130_models.QueryAvatarResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_avatar_with_options(request, runtime)

    async def query_avatar_async(
        self,
        request: avatar_20220130_models.QueryAvatarRequest,
    ) -> avatar_20220130_models.QueryAvatarResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_avatar_with_options_async(request, runtime)

    def query_avatar_list_with_options(
        self,
        request: avatar_20220130_models.QueryAvatarListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.QueryAvatarListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_type):
            query['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAvatarList',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.QueryAvatarListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_avatar_list_with_options_async(
        self,
        request: avatar_20220130_models.QueryAvatarListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.QueryAvatarListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_type):
            query['ModelType'] = request.model_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAvatarList',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.QueryAvatarListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_avatar_list(
        self,
        request: avatar_20220130_models.QueryAvatarListRequest,
    ) -> avatar_20220130_models.QueryAvatarListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_avatar_list_with_options(request, runtime)

    async def query_avatar_list_async(
        self,
        request: avatar_20220130_models.QueryAvatarListRequest,
    ) -> avatar_20220130_models.QueryAvatarListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_avatar_list_with_options_async(request, runtime)

    def query_running_instance_with_options(
        self,
        tmp_req: avatar_20220130_models.QueryRunningInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.QueryRunningInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.QueryRunningInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRunningInstance',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.QueryRunningInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_running_instance_with_options_async(
        self,
        tmp_req: avatar_20220130_models.QueryRunningInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.QueryRunningInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.QueryRunningInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRunningInstance',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.QueryRunningInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_running_instance(
        self,
        request: avatar_20220130_models.QueryRunningInstanceRequest,
    ) -> avatar_20220130_models.QueryRunningInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_running_instance_with_options(request, runtime)

    async def query_running_instance_async(
        self,
        request: avatar_20220130_models.QueryRunningInstanceRequest,
    ) -> avatar_20220130_models.QueryRunningInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_running_instance_with_options_async(request, runtime)

    def query_timed_reset_operate_status_with_options(
        self,
        request: avatar_20220130_models.QueryTimedResetOperateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.QueryTimedResetOperateStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTimedResetOperateStatus',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.QueryTimedResetOperateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_timed_reset_operate_status_with_options_async(
        self,
        request: avatar_20220130_models.QueryTimedResetOperateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.QueryTimedResetOperateStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTimedResetOperateStatus',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.QueryTimedResetOperateStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_timed_reset_operate_status(
        self,
        request: avatar_20220130_models.QueryTimedResetOperateStatusRequest,
    ) -> avatar_20220130_models.QueryTimedResetOperateStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_timed_reset_operate_status_with_options(request, runtime)

    async def query_timed_reset_operate_status_async(
        self,
        request: avatar_20220130_models.QueryTimedResetOperateStatusRequest,
    ) -> avatar_20220130_models.QueryTimedResetOperateStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_timed_reset_operate_status_with_options_async(request, runtime)

    def query_video_task_info_with_options(
        self,
        tmp_req: avatar_20220130_models.QueryVideoTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.QueryVideoTaskInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.QueryVideoTaskInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.order_by_id):
            query['OrderById'] = request.order_by_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_uuid):
            query['TaskUuid'] = request.task_uuid
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryVideoTaskInfo',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.QueryVideoTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_video_task_info_with_options_async(
        self,
        tmp_req: avatar_20220130_models.QueryVideoTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.QueryVideoTaskInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.QueryVideoTaskInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.order_by_id):
            query['OrderById'] = request.order_by_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_uuid):
            query['TaskUuid'] = request.task_uuid
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryVideoTaskInfo',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.QueryVideoTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_video_task_info(
        self,
        request: avatar_20220130_models.QueryVideoTaskInfoRequest,
    ) -> avatar_20220130_models.QueryVideoTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_video_task_info_with_options(request, runtime)

    async def query_video_task_info_async(
        self,
        request: avatar_20220130_models.QueryVideoTaskInfoRequest,
    ) -> avatar_20220130_models.QueryVideoTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_video_task_info_with_options_async(request, runtime)

    def render_3d_avatar_with_options(
        self,
        request: avatar_20220130_models.Render3dAvatarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.Render3dAvatarResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Render3dAvatar',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.Render3dAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    async def render_3d_avatar_with_options_async(
        self,
        request: avatar_20220130_models.Render3dAvatarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.Render3dAvatarResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Render3dAvatar',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.Render3dAvatarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def render_3d_avatar(
        self,
        request: avatar_20220130_models.Render3dAvatarRequest,
    ) -> avatar_20220130_models.Render3dAvatarResponse:
        runtime = util_models.RuntimeOptions()
        return self.render_3d_avatar_with_options(request, runtime)

    async def render_3d_avatar_async(
        self,
        request: avatar_20220130_models.Render3dAvatarRequest,
    ) -> avatar_20220130_models.Render3dAvatarResponse:
        runtime = util_models.RuntimeOptions()
        return await self.render_3d_avatar_with_options_async(request, runtime)

    def send_command_with_options(
        self,
        tmp_req: avatar_20220130_models.SendCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.SendCommandResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SendCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.content):
            request.content_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.content_shrink):
            query['Content'] = request.content_shrink
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.unique_code):
            query['UniqueCode'] = request.unique_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendCommand',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SendCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_command_with_options_async(
        self,
        tmp_req: avatar_20220130_models.SendCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.SendCommandResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SendCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.content):
            request.content_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        query = {}
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.content_shrink):
            query['Content'] = request.content_shrink
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.unique_code):
            query['UniqueCode'] = request.unique_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendCommand',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SendCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_command(
        self,
        request: avatar_20220130_models.SendCommandRequest,
    ) -> avatar_20220130_models.SendCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_command_with_options(request, runtime)

    async def send_command_async(
        self,
        request: avatar_20220130_models.SendCommandRequest,
    ) -> avatar_20220130_models.SendCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_command_with_options_async(request, runtime)

    def send_message_with_options(
        self,
        tmp_req: avatar_20220130_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.SendMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SendMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stream_extension):
            request.stream_extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_extension, 'StreamExtension', 'json')
        if not UtilClient.is_unset(tmp_req.text_request):
            request.text_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text_request, 'TextRequest', 'json')
        if not UtilClient.is_unset(tmp_req.vamlrequest):
            request.vamlrequest_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vamlrequest, 'VAMLRequest', 'json')
        query = {}
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.stream_extension_shrink):
            query['StreamExtension'] = request.stream_extension_shrink
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text_request_shrink):
            query['TextRequest'] = request.text_request_shrink
        if not UtilClient.is_unset(request.vamlrequest_shrink):
            query['VAMLRequest'] = request.vamlrequest_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_message_with_options_async(
        self,
        tmp_req: avatar_20220130_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.SendMessageResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SendMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stream_extension):
            request.stream_extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_extension, 'StreamExtension', 'json')
        if not UtilClient.is_unset(tmp_req.text_request):
            request.text_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.text_request, 'TextRequest', 'json')
        if not UtilClient.is_unset(tmp_req.vamlrequest):
            request.vamlrequest_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vamlrequest, 'VAMLRequest', 'json')
        query = {}
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.stream_extension_shrink):
            query['StreamExtension'] = request.stream_extension_shrink
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text_request_shrink):
            query['TextRequest'] = request.text_request_shrink
        if not UtilClient.is_unset(request.vamlrequest_shrink):
            query['VAMLRequest'] = request.vamlrequest_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendMessage',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SendMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_message(
        self,
        request: avatar_20220130_models.SendMessageRequest,
    ) -> avatar_20220130_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_message_with_options(request, runtime)

    async def send_message_async(
        self,
        request: avatar_20220130_models.SendMessageRequest,
    ) -> avatar_20220130_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_message_with_options_async(request, runtime)

    def send_text_with_options(
        self,
        tmp_req: avatar_20220130_models.SendTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.SendTextResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SendTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stream_extension):
            request.stream_extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_extension, 'StreamExtension', 'json')
        query = {}
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.interrupt):
            query['Interrupt'] = request.interrupt
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.stream_extension_shrink):
            query['StreamExtension'] = request.stream_extension_shrink
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        if not UtilClient.is_unset(request.unique_code):
            query['UniqueCode'] = request.unique_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendText',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SendTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_text_with_options_async(
        self,
        tmp_req: avatar_20220130_models.SendTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.SendTextResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SendTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stream_extension):
            request.stream_extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_extension, 'StreamExtension', 'json')
        query = {}
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.interrupt):
            query['Interrupt'] = request.interrupt
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.stream_extension_shrink):
            query['StreamExtension'] = request.stream_extension_shrink
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        if not UtilClient.is_unset(request.unique_code):
            query['UniqueCode'] = request.unique_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendText',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SendTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_text(
        self,
        request: avatar_20220130_models.SendTextRequest,
    ) -> avatar_20220130_models.SendTextResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_text_with_options(request, runtime)

    async def send_text_async(
        self,
        request: avatar_20220130_models.SendTextRequest,
    ) -> avatar_20220130_models.SendTextResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_text_with_options_async(request, runtime)

    def send_vaml_with_options(
        self,
        request: avatar_20220130_models.SendVamlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.SendVamlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.vaml):
            query['Vaml'] = request.vaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVaml',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SendVamlResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_vaml_with_options_async(
        self,
        request: avatar_20220130_models.SendVamlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.SendVamlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.vaml):
            query['Vaml'] = request.vaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVaml',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SendVamlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_vaml(
        self,
        request: avatar_20220130_models.SendVamlRequest,
    ) -> avatar_20220130_models.SendVamlResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_vaml_with_options(request, runtime)

    async def send_vaml_async(
        self,
        request: avatar_20220130_models.SendVamlRequest,
    ) -> avatar_20220130_models.SendVamlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_vaml_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        tmp_req: avatar_20220130_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.StartInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.StartInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        if not UtilClient.is_unset(tmp_req.channel):
            request.channel_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.channel, 'Channel', 'json')
        if not UtilClient.is_unset(tmp_req.command_request):
            request.command_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.command_request, 'CommandRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.channel_shrink):
            query['Channel'] = request.channel_shrink
        if not UtilClient.is_unset(request.command_request_shrink):
            query['CommandRequest'] = request.command_request_shrink
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_shrink):
            query['User'] = request.user_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        tmp_req: avatar_20220130_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.StartInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.StartInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        if not UtilClient.is_unset(tmp_req.channel):
            request.channel_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.channel, 'Channel', 'json')
        if not UtilClient.is_unset(tmp_req.command_request):
            request.command_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.command_request, 'CommandRequest', 'json')
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.channel_shrink):
            query['Channel'] = request.channel_shrink
        if not UtilClient.is_unset(request.command_request_shrink):
            query['CommandRequest'] = request.command_request_shrink
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_shrink):
            query['User'] = request.user_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.StartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instance(
        self,
        request: avatar_20220130_models.StartInstanceRequest,
    ) -> avatar_20220130_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: avatar_20220130_models.StartInstanceRequest,
    ) -> avatar_20220130_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def start_timed_reset_operate_with_options(
        self,
        request: avatar_20220130_models.StartTimedResetOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.StartTimedResetOperateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartTimedResetOperate',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.StartTimedResetOperateResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_timed_reset_operate_with_options_async(
        self,
        request: avatar_20220130_models.StartTimedResetOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.StartTimedResetOperateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartTimedResetOperate',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.StartTimedResetOperateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_timed_reset_operate(
        self,
        request: avatar_20220130_models.StartTimedResetOperateRequest,
    ) -> avatar_20220130_models.StartTimedResetOperateResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_timed_reset_operate_with_options(request, runtime)

    async def start_timed_reset_operate_async(
        self,
        request: avatar_20220130_models.StartTimedResetOperateRequest,
    ) -> avatar_20220130_models.StartTimedResetOperateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_timed_reset_operate_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: avatar_20220130_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: avatar_20220130_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance(
        self,
        request: avatar_20220130_models.StopInstanceRequest,
    ) -> avatar_20220130_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    async def stop_instance_async(
        self,
        request: avatar_20220130_models.StopInstanceRequest,
    ) -> avatar_20220130_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_instance_with_options_async(request, runtime)

    def submit_audio_to_2davatar_video_task_with_options(
        self,
        tmp_req: avatar_20220130_models.SubmitAudioTo2DAvatarVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.SubmitAudioTo2DAvatarVideoTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SubmitAudioTo2DAvatarVideoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        if not UtilClient.is_unset(tmp_req.avatar_info):
            request.avatar_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.avatar_info, 'AvatarInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_info):
            request.video_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_info, 'VideoInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.avatar_info_shrink):
            query['AvatarInfo'] = request.avatar_info_shrink
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_params):
            query['CallbackParams'] = request.callback_params
        if not UtilClient.is_unset(request.ext_params):
            query['ExtParams'] = request.ext_params
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.video_info_shrink):
            query['VideoInfo'] = request.video_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAudioTo2DAvatarVideoTask',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SubmitAudioTo2DAvatarVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_audio_to_2davatar_video_task_with_options_async(
        self,
        tmp_req: avatar_20220130_models.SubmitAudioTo2DAvatarVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.SubmitAudioTo2DAvatarVideoTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SubmitAudioTo2DAvatarVideoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        if not UtilClient.is_unset(tmp_req.avatar_info):
            request.avatar_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.avatar_info, 'AvatarInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_info):
            request.video_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_info, 'VideoInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.avatar_info_shrink):
            query['AvatarInfo'] = request.avatar_info_shrink
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_params):
            query['CallbackParams'] = request.callback_params
        if not UtilClient.is_unset(request.ext_params):
            query['ExtParams'] = request.ext_params
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.video_info_shrink):
            query['VideoInfo'] = request.video_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAudioTo2DAvatarVideoTask',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SubmitAudioTo2DAvatarVideoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_audio_to_2davatar_video_task(
        self,
        request: avatar_20220130_models.SubmitAudioTo2DAvatarVideoTaskRequest,
    ) -> avatar_20220130_models.SubmitAudioTo2DAvatarVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_audio_to_2davatar_video_task_with_options(request, runtime)

    async def submit_audio_to_2davatar_video_task_async(
        self,
        request: avatar_20220130_models.SubmitAudioTo2DAvatarVideoTaskRequest,
    ) -> avatar_20220130_models.SubmitAudioTo2DAvatarVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_audio_to_2davatar_video_task_with_options_async(request, runtime)

    def submit_audio_to_3davatar_video_task_with_options(
        self,
        tmp_req: avatar_20220130_models.SubmitAudioTo3DAvatarVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.SubmitAudioTo3DAvatarVideoTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SubmitAudioTo3DAvatarVideoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        if not UtilClient.is_unset(tmp_req.avatar_info):
            request.avatar_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.avatar_info, 'AvatarInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_info):
            request.video_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_info, 'VideoInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.avatar_info_shrink):
            query['AvatarInfo'] = request.avatar_info_shrink
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_params):
            query['CallbackParams'] = request.callback_params
        if not UtilClient.is_unset(request.ext_params):
            query['ExtParams'] = request.ext_params
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.video_info_shrink):
            query['VideoInfo'] = request.video_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAudioTo3DAvatarVideoTask',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SubmitAudioTo3DAvatarVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_audio_to_3davatar_video_task_with_options_async(
        self,
        tmp_req: avatar_20220130_models.SubmitAudioTo3DAvatarVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.SubmitAudioTo3DAvatarVideoTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SubmitAudioTo3DAvatarVideoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        if not UtilClient.is_unset(tmp_req.avatar_info):
            request.avatar_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.avatar_info, 'AvatarInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_info):
            request.video_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_info, 'VideoInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.avatar_info_shrink):
            query['AvatarInfo'] = request.avatar_info_shrink
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_params):
            query['CallbackParams'] = request.callback_params
        if not UtilClient.is_unset(request.ext_params):
            query['ExtParams'] = request.ext_params
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.video_info_shrink):
            query['VideoInfo'] = request.video_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAudioTo3DAvatarVideoTask',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SubmitAudioTo3DAvatarVideoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_audio_to_3davatar_video_task(
        self,
        request: avatar_20220130_models.SubmitAudioTo3DAvatarVideoTaskRequest,
    ) -> avatar_20220130_models.SubmitAudioTo3DAvatarVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_audio_to_3davatar_video_task_with_options(request, runtime)

    async def submit_audio_to_3davatar_video_task_async(
        self,
        request: avatar_20220130_models.SubmitAudioTo3DAvatarVideoTaskRequest,
    ) -> avatar_20220130_models.SubmitAudioTo3DAvatarVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_audio_to_3davatar_video_task_with_options_async(request, runtime)

    def submit_text_to_2davatar_video_task_with_options(
        self,
        tmp_req: avatar_20220130_models.SubmitTextTo2DAvatarVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.SubmitTextTo2DAvatarVideoTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SubmitTextTo2DAvatarVideoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        if not UtilClient.is_unset(tmp_req.audio_info):
            request.audio_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.audio_info, 'AudioInfo', 'json')
        if not UtilClient.is_unset(tmp_req.avatar_info):
            request.avatar_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.avatar_info, 'AvatarInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_info):
            request.video_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_info, 'VideoInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.audio_info_shrink):
            query['AudioInfo'] = request.audio_info_shrink
        if not UtilClient.is_unset(request.avatar_info_shrink):
            query['AvatarInfo'] = request.avatar_info_shrink
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_params):
            query['CallbackParams'] = request.callback_params
        if not UtilClient.is_unset(request.ext_params):
            query['ExtParams'] = request.ext_params
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.video_info_shrink):
            query['VideoInfo'] = request.video_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTextTo2DAvatarVideoTask',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SubmitTextTo2DAvatarVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_text_to_2davatar_video_task_with_options_async(
        self,
        tmp_req: avatar_20220130_models.SubmitTextTo2DAvatarVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.SubmitTextTo2DAvatarVideoTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SubmitTextTo2DAvatarVideoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        if not UtilClient.is_unset(tmp_req.audio_info):
            request.audio_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.audio_info, 'AudioInfo', 'json')
        if not UtilClient.is_unset(tmp_req.avatar_info):
            request.avatar_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.avatar_info, 'AvatarInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_info):
            request.video_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_info, 'VideoInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.audio_info_shrink):
            query['AudioInfo'] = request.audio_info_shrink
        if not UtilClient.is_unset(request.avatar_info_shrink):
            query['AvatarInfo'] = request.avatar_info_shrink
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_params):
            query['CallbackParams'] = request.callback_params
        if not UtilClient.is_unset(request.ext_params):
            query['ExtParams'] = request.ext_params
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.video_info_shrink):
            query['VideoInfo'] = request.video_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTextTo2DAvatarVideoTask',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SubmitTextTo2DAvatarVideoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_text_to_2davatar_video_task(
        self,
        request: avatar_20220130_models.SubmitTextTo2DAvatarVideoTaskRequest,
    ) -> avatar_20220130_models.SubmitTextTo2DAvatarVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_text_to_2davatar_video_task_with_options(request, runtime)

    async def submit_text_to_2davatar_video_task_async(
        self,
        request: avatar_20220130_models.SubmitTextTo2DAvatarVideoTaskRequest,
    ) -> avatar_20220130_models.SubmitTextTo2DAvatarVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_text_to_2davatar_video_task_with_options_async(request, runtime)

    def submit_text_to_3davatar_video_task_with_options(
        self,
        tmp_req: avatar_20220130_models.SubmitTextTo3DAvatarVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.SubmitTextTo3DAvatarVideoTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SubmitTextTo3DAvatarVideoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        if not UtilClient.is_unset(tmp_req.audio_info):
            request.audio_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.audio_info, 'AudioInfo', 'json')
        if not UtilClient.is_unset(tmp_req.avatar_info):
            request.avatar_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.avatar_info, 'AvatarInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_info):
            request.video_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_info, 'VideoInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.audio_info_shrink):
            query['AudioInfo'] = request.audio_info_shrink
        if not UtilClient.is_unset(request.avatar_info_shrink):
            query['AvatarInfo'] = request.avatar_info_shrink
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_params):
            query['CallbackParams'] = request.callback_params
        if not UtilClient.is_unset(request.ext_params):
            query['ExtParams'] = request.ext_params
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.video_info_shrink):
            query['VideoInfo'] = request.video_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTextTo3DAvatarVideoTask',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SubmitTextTo3DAvatarVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_text_to_3davatar_video_task_with_options_async(
        self,
        tmp_req: avatar_20220130_models.SubmitTextTo3DAvatarVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.SubmitTextTo3DAvatarVideoTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = avatar_20220130_models.SubmitTextTo3DAvatarVideoTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app):
            request.app_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app, 'App', 'json')
        if not UtilClient.is_unset(tmp_req.audio_info):
            request.audio_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.audio_info, 'AudioInfo', 'json')
        if not UtilClient.is_unset(tmp_req.avatar_info):
            request.avatar_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.avatar_info, 'AvatarInfo', 'json')
        if not UtilClient.is_unset(tmp_req.video_info):
            request.video_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.video_info, 'VideoInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_shrink):
            query['App'] = request.app_shrink
        if not UtilClient.is_unset(request.audio_info_shrink):
            query['AudioInfo'] = request.audio_info_shrink
        if not UtilClient.is_unset(request.avatar_info_shrink):
            query['AvatarInfo'] = request.avatar_info_shrink
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_params):
            query['CallbackParams'] = request.callback_params
        if not UtilClient.is_unset(request.ext_params):
            query['ExtParams'] = request.ext_params
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.video_info_shrink):
            query['VideoInfo'] = request.video_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTextTo3DAvatarVideoTask',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.SubmitTextTo3DAvatarVideoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_text_to_3davatar_video_task(
        self,
        request: avatar_20220130_models.SubmitTextTo3DAvatarVideoTaskRequest,
    ) -> avatar_20220130_models.SubmitTextTo3DAvatarVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_text_to_3davatar_video_task_with_options(request, runtime)

    async def submit_text_to_3davatar_video_task_async(
        self,
        request: avatar_20220130_models.SubmitTextTo3DAvatarVideoTaskRequest,
    ) -> avatar_20220130_models.SubmitTextTo3DAvatarVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_text_to_3davatar_video_task_with_options_async(request, runtime)

    def update_2d_avatar_with_options(
        self,
        request: avatar_20220130_models.Update2dAvatarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.Update2dAvatarResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.orientation):
            query['Orientation'] = request.orientation
        if not UtilClient.is_unset(request.portrait):
            query['Portrait'] = request.portrait
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.transparent):
            query['Transparent'] = request.transparent
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Update2dAvatar',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.Update2dAvatarResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_2d_avatar_with_options_async(
        self,
        request: avatar_20220130_models.Update2dAvatarRequest,
        runtime: util_models.RuntimeOptions,
    ) -> avatar_20220130_models.Update2dAvatarResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.code):
            query['Code'] = request.code
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.orientation):
            query['Orientation'] = request.orientation
        if not UtilClient.is_unset(request.portrait):
            query['Portrait'] = request.portrait
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.transparent):
            query['Transparent'] = request.transparent
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Update2dAvatar',
            version='2022-01-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            avatar_20220130_models.Update2dAvatarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_2d_avatar(
        self,
        request: avatar_20220130_models.Update2dAvatarRequest,
    ) -> avatar_20220130_models.Update2dAvatarResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_2d_avatar_with_options(request, runtime)

    async def update_2d_avatar_async(
        self,
        request: avatar_20220130_models.Update2dAvatarRequest,
    ) -> avatar_20220130_models.Update2dAvatarResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_2d_avatar_with_options_async(request, runtime)
