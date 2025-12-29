# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dyvmsapi20170525 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('dyvmsapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_virtual_number_relation_with_options(
        self,
        request: main_models.AddVirtualNumberRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddVirtualNumberRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.corp_name_list):
            query['CorpNameList'] = request.corp_name_list
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_type):
            query['RouteType'] = request.route_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddVirtualNumberRelation',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddVirtualNumberRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_virtual_number_relation_with_options_async(
        self,
        request: main_models.AddVirtualNumberRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddVirtualNumberRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.corp_name_list):
            query['CorpNameList'] = request.corp_name_list
        if not DaraCore.is_null(request.number_list):
            query['NumberList'] = request.number_list
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_type):
            query['RouteType'] = request.route_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddVirtualNumberRelation',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddVirtualNumberRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_virtual_number_relation(
        self,
        request: main_models.AddVirtualNumberRelationRequest,
    ) -> main_models.AddVirtualNumberRelationResponse:
        runtime = RuntimeOptions()
        return self.add_virtual_number_relation_with_options(request, runtime)

    async def add_virtual_number_relation_async(
        self,
        request: main_models.AddVirtualNumberRelationRequest,
    ) -> main_models.AddVirtualNumberRelationResponse:
        runtime = RuntimeOptions()
        return await self.add_virtual_number_relation_with_options_async(request, runtime)

    def batch_robot_smart_call_with_options(
        self,
        request: main_models.BatchRobotSmartCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchRobotSmartCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.corp_name):
            query['CorpName'] = request.corp_name
        if not DaraCore.is_null(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not DaraCore.is_null(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not DaraCore.is_null(request.is_self_line):
            query['IsSelfLine'] = request.is_self_line
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schedule_call):
            query['ScheduleCall'] = request.schedule_call
        if not DaraCore.is_null(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not DaraCore.is_null(request.tts_param_head):
            query['TtsParamHead'] = request.tts_param_head
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchRobotSmartCall',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchRobotSmartCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_robot_smart_call_with_options_async(
        self,
        request: main_models.BatchRobotSmartCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchRobotSmartCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.corp_name):
            query['CorpName'] = request.corp_name
        if not DaraCore.is_null(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not DaraCore.is_null(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not DaraCore.is_null(request.is_self_line):
            query['IsSelfLine'] = request.is_self_line
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schedule_call):
            query['ScheduleCall'] = request.schedule_call
        if not DaraCore.is_null(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not DaraCore.is_null(request.tts_param_head):
            query['TtsParamHead'] = request.tts_param_head
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchRobotSmartCall',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchRobotSmartCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_robot_smart_call(
        self,
        request: main_models.BatchRobotSmartCallRequest,
    ) -> main_models.BatchRobotSmartCallResponse:
        runtime = RuntimeOptions()
        return self.batch_robot_smart_call_with_options(request, runtime)

    async def batch_robot_smart_call_async(
        self,
        request: main_models.BatchRobotSmartCallRequest,
    ) -> main_models.BatchRobotSmartCallResponse:
        runtime = RuntimeOptions()
        return await self.batch_robot_smart_call_with_options_async(request, runtime)

    def cancel_call_with_options(
        self,
        request: main_models.CancelCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelCall',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_call_with_options_async(
        self,
        request: main_models.CancelCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelCall',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_call(
        self,
        request: main_models.CancelCallRequest,
    ) -> main_models.CancelCallResponse:
        runtime = RuntimeOptions()
        return self.cancel_call_with_options(request, runtime)

    async def cancel_call_async(
        self,
        request: main_models.CancelCallRequest,
    ) -> main_models.CancelCallResponse:
        runtime = RuntimeOptions()
        return await self.cancel_call_with_options_async(request, runtime)

    def cancel_order_robot_task_with_options(
        self,
        request: main_models.CancelOrderRobotTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelOrderRobotTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelOrderRobotTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelOrderRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_order_robot_task_with_options_async(
        self,
        request: main_models.CancelOrderRobotTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelOrderRobotTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelOrderRobotTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelOrderRobotTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_order_robot_task(
        self,
        request: main_models.CancelOrderRobotTaskRequest,
    ) -> main_models.CancelOrderRobotTaskResponse:
        runtime = RuntimeOptions()
        return self.cancel_order_robot_task_with_options(request, runtime)

    async def cancel_order_robot_task_async(
        self,
        request: main_models.CancelOrderRobotTaskRequest,
    ) -> main_models.CancelOrderRobotTaskResponse:
        runtime = RuntimeOptions()
        return await self.cancel_order_robot_task_with_options_async(request, runtime)

    def cancel_robot_task_with_options(
        self,
        request: main_models.CancelRobotTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelRobotTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelRobotTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_robot_task_with_options_async(
        self,
        request: main_models.CancelRobotTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelRobotTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelRobotTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelRobotTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_robot_task(
        self,
        request: main_models.CancelRobotTaskRequest,
    ) -> main_models.CancelRobotTaskResponse:
        runtime = RuntimeOptions()
        return self.cancel_robot_task_with_options(request, runtime)

    async def cancel_robot_task_async(
        self,
        request: main_models.CancelRobotTaskRequest,
    ) -> main_models.CancelRobotTaskResponse:
        runtime = RuntimeOptions()
        return await self.cancel_robot_task_with_options_async(request, runtime)

    def change_media_type_with_options(
        self,
        request: main_models.ChangeMediaTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeMediaTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_num):
            query['CalledNum'] = request.called_num
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeMediaType',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeMediaTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_media_type_with_options_async(
        self,
        request: main_models.ChangeMediaTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeMediaTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_num):
            query['CalledNum'] = request.called_num
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeMediaType',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeMediaTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_media_type(
        self,
        request: main_models.ChangeMediaTypeRequest,
    ) -> main_models.ChangeMediaTypeResponse:
        runtime = RuntimeOptions()
        return self.change_media_type_with_options(request, runtime)

    async def change_media_type_async(
        self,
        request: main_models.ChangeMediaTypeRequest,
    ) -> main_models.ChangeMediaTypeResponse:
        runtime = RuntimeOptions()
        return await self.change_media_type_with_options_async(request, runtime)

    def create_call_task_with_options(
        self,
        request: main_models.CreateCallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCallTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.fire_time):
            query['FireTime'] = request.fire_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not DaraCore.is_null(request.stop_time):
            query['StopTime'] = request.stop_time
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCallTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_call_task_with_options_async(
        self,
        request: main_models.CreateCallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCallTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.fire_time):
            query['FireTime'] = request.fire_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource):
            query['Resource'] = request.resource
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not DaraCore.is_null(request.stop_time):
            query['StopTime'] = request.stop_time
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.template_code):
            query['TemplateCode'] = request.template_code
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCallTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCallTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_call_task(
        self,
        request: main_models.CreateCallTaskRequest,
    ) -> main_models.CreateCallTaskResponse:
        runtime = RuntimeOptions()
        return self.create_call_task_with_options(request, runtime)

    async def create_call_task_async(
        self,
        request: main_models.CreateCallTaskRequest,
    ) -> main_models.CreateCallTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_call_task_with_options_async(request, runtime)

    def create_robot_task_with_options(
        self,
        request: main_models.CreateRobotTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRobotTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.corp_name):
            query['CorpName'] = request.corp_name
        if not DaraCore.is_null(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not DaraCore.is_null(request.is_self_line):
            query['IsSelfLine'] = request.is_self_line
        if not DaraCore.is_null(request.number_status_ident):
            query['NumberStatusIdent'] = request.number_status_ident
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.recall_interval):
            query['RecallInterval'] = request.recall_interval
        if not DaraCore.is_null(request.recall_state_codes):
            query['RecallStateCodes'] = request.recall_state_codes
        if not DaraCore.is_null(request.recall_times):
            query['RecallTimes'] = request.recall_times
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.retry_type):
            query['RetryType'] = request.retry_type
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRobotTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_robot_task_with_options_async(
        self,
        request: main_models.CreateRobotTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRobotTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller):
            query['Caller'] = request.caller
        if not DaraCore.is_null(request.corp_name):
            query['CorpName'] = request.corp_name
        if not DaraCore.is_null(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not DaraCore.is_null(request.is_self_line):
            query['IsSelfLine'] = request.is_self_line
        if not DaraCore.is_null(request.number_status_ident):
            query['NumberStatusIdent'] = request.number_status_ident
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.recall_interval):
            query['RecallInterval'] = request.recall_interval
        if not DaraCore.is_null(request.recall_state_codes):
            query['RecallStateCodes'] = request.recall_state_codes
        if not DaraCore.is_null(request.recall_times):
            query['RecallTimes'] = request.recall_times
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.retry_type):
            query['RetryType'] = request.retry_type
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRobotTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRobotTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_robot_task(
        self,
        request: main_models.CreateRobotTaskRequest,
    ) -> main_models.CreateRobotTaskResponse:
        runtime = RuntimeOptions()
        return self.create_robot_task_with_options(request, runtime)

    async def create_robot_task_async(
        self,
        request: main_models.CreateRobotTaskRequest,
    ) -> main_models.CreateRobotTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_robot_task_with_options_async(request, runtime)

    def degrade_video_file_with_options(
        self,
        request: main_models.DegradeVideoFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DegradeVideoFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DegradeVideoFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DegradeVideoFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def degrade_video_file_with_options_async(
        self,
        request: main_models.DegradeVideoFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DegradeVideoFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DegradeVideoFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DegradeVideoFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def degrade_video_file(
        self,
        request: main_models.DegradeVideoFileRequest,
    ) -> main_models.DegradeVideoFileResponse:
        runtime = RuntimeOptions()
        return self.degrade_video_file_with_options(request, runtime)

    async def degrade_video_file_async(
        self,
        request: main_models.DegradeVideoFileRequest,
    ) -> main_models.DegradeVideoFileResponse:
        runtime = RuntimeOptions()
        return await self.degrade_video_file_with_options_async(request, runtime)

    def delete_robot_task_with_options(
        self,
        request: main_models.DeleteRobotTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRobotTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRobotTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_robot_task_with_options_async(
        self,
        request: main_models.DeleteRobotTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRobotTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRobotTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRobotTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_robot_task(
        self,
        request: main_models.DeleteRobotTaskRequest,
    ) -> main_models.DeleteRobotTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_robot_task_with_options(request, runtime)

    async def delete_robot_task_async(
        self,
        request: main_models.DeleteRobotTaskRequest,
    ) -> main_models.DeleteRobotTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_robot_task_with_options_async(request, runtime)

    def execute_call_task_with_options(
        self,
        request: main_models.ExecuteCallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteCallTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fire_time):
            query['FireTime'] = request.fire_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteCallTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteCallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_call_task_with_options_async(
        self,
        request: main_models.ExecuteCallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteCallTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fire_time):
            query['FireTime'] = request.fire_time
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteCallTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteCallTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_call_task(
        self,
        request: main_models.ExecuteCallTaskRequest,
    ) -> main_models.ExecuteCallTaskResponse:
        runtime = RuntimeOptions()
        return self.execute_call_task_with_options(request, runtime)

    async def execute_call_task_async(
        self,
        request: main_models.ExecuteCallTaskRequest,
    ) -> main_models.ExecuteCallTaskResponse:
        runtime = RuntimeOptions()
        return await self.execute_call_task_with_options_async(request, runtime)

    def get_call_media_type_with_options(
        self,
        request: main_models.GetCallMediaTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCallMediaTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCallMediaType',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCallMediaTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_call_media_type_with_options_async(
        self,
        request: main_models.GetCallMediaTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCallMediaTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCallMediaType',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCallMediaTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_call_media_type(
        self,
        request: main_models.GetCallMediaTypeRequest,
    ) -> main_models.GetCallMediaTypeResponse:
        runtime = RuntimeOptions()
        return self.get_call_media_type_with_options(request, runtime)

    async def get_call_media_type_async(
        self,
        request: main_models.GetCallMediaTypeRequest,
    ) -> main_models.GetCallMediaTypeResponse:
        runtime = RuntimeOptions()
        return await self.get_call_media_type_with_options_async(request, runtime)

    def get_call_progress_with_options(
        self,
        request: main_models.GetCallProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCallProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_num):
            query['CalledNum'] = request.called_num
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCallProgress',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCallProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_call_progress_with_options_async(
        self,
        request: main_models.GetCallProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCallProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_num):
            query['CalledNum'] = request.called_num
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCallProgress',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCallProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_call_progress(
        self,
        request: main_models.GetCallProgressRequest,
    ) -> main_models.GetCallProgressResponse:
        runtime = RuntimeOptions()
        return self.get_call_progress_with_options(request, runtime)

    async def get_call_progress_async(
        self,
        request: main_models.GetCallProgressRequest,
    ) -> main_models.GetCallProgressResponse:
        runtime = RuntimeOptions()
        return await self.get_call_progress_with_options_async(request, runtime)

    def get_hotline_qualification_by_order_with_options(
        self,
        request: main_models.GetHotlineQualificationByOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineQualificationByOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineQualificationByOrder',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineQualificationByOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hotline_qualification_by_order_with_options_async(
        self,
        request: main_models.GetHotlineQualificationByOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetHotlineQualificationByOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHotlineQualificationByOrder',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHotlineQualificationByOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hotline_qualification_by_order(
        self,
        request: main_models.GetHotlineQualificationByOrderRequest,
    ) -> main_models.GetHotlineQualificationByOrderResponse:
        runtime = RuntimeOptions()
        return self.get_hotline_qualification_by_order_with_options(request, runtime)

    async def get_hotline_qualification_by_order_async(
        self,
        request: main_models.GetHotlineQualificationByOrderRequest,
    ) -> main_models.GetHotlineQualificationByOrderResponse:
        runtime = RuntimeOptions()
        return await self.get_hotline_qualification_by_order_with_options_async(request, runtime)

    def get_temporary_file_url_with_options(
        self,
        request: main_models.GetTemporaryFileUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemporaryFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemporaryFileUrl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemporaryFileUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_temporary_file_url_with_options_async(
        self,
        request: main_models.GetTemporaryFileUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemporaryFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemporaryFileUrl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemporaryFileUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_temporary_file_url(
        self,
        request: main_models.GetTemporaryFileUrlRequest,
    ) -> main_models.GetTemporaryFileUrlResponse:
        runtime = RuntimeOptions()
        return self.get_temporary_file_url_with_options(request, runtime)

    async def get_temporary_file_url_async(
        self,
        request: main_models.GetTemporaryFileUrlRequest,
    ) -> main_models.GetTemporaryFileUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_temporary_file_url_with_options_async(request, runtime)

    def get_token_with_options(
        self,
        request: main_models.GetTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.token_type):
            query['TokenType'] = request.token_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetToken',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: main_models.GetTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.token_type):
            query['TokenType'] = request.token_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetToken',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token(
        self,
        request: main_models.GetTokenRequest,
    ) -> main_models.GetTokenResponse:
        runtime = RuntimeOptions()
        return self.get_token_with_options(request, runtime)

    async def get_token_async(
        self,
        request: main_models.GetTokenRequest,
    ) -> main_models.GetTokenResponse:
        runtime = RuntimeOptions()
        return await self.get_token_with_options_async(request, runtime)

    def get_video_field_url_with_options(
        self,
        request: main_models.GetVideoFieldUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoFieldUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.video_file):
            query['VideoFile'] = request.video_file
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoFieldUrl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoFieldUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_field_url_with_options_async(
        self,
        request: main_models.GetVideoFieldUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoFieldUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.video_file):
            query['VideoFile'] = request.video_file
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoFieldUrl',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoFieldUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_field_url(
        self,
        request: main_models.GetVideoFieldUrlRequest,
    ) -> main_models.GetVideoFieldUrlResponse:
        runtime = RuntimeOptions()
        return self.get_video_field_url_with_options(request, runtime)

    async def get_video_field_url_async(
        self,
        request: main_models.GetVideoFieldUrlRequest,
    ) -> main_models.GetVideoFieldUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_video_field_url_with_options_async(request, runtime)

    def ivr_call_with_options(
        self,
        request: main_models.IvrCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IvrCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bye_code):
            query['ByeCode'] = request.bye_code
        if not DaraCore.is_null(request.bye_tts_params):
            query['ByeTtsParams'] = request.bye_tts_params
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.menu_key_map):
            query['MenuKeyMap'] = request.menu_key_map
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_times):
            query['PlayTimes'] = request.play_times
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_code):
            query['StartCode'] = request.start_code
        if not DaraCore.is_null(request.start_tts_params):
            query['StartTtsParams'] = request.start_tts_params
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IvrCall',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IvrCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def ivr_call_with_options_async(
        self,
        request: main_models.IvrCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IvrCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bye_code):
            query['ByeCode'] = request.bye_code
        if not DaraCore.is_null(request.bye_tts_params):
            query['ByeTtsParams'] = request.bye_tts_params
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.menu_key_map):
            query['MenuKeyMap'] = request.menu_key_map
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_times):
            query['PlayTimes'] = request.play_times
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_code):
            query['StartCode'] = request.start_code
        if not DaraCore.is_null(request.start_tts_params):
            query['StartTtsParams'] = request.start_tts_params
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IvrCall',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IvrCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ivr_call(
        self,
        request: main_models.IvrCallRequest,
    ) -> main_models.IvrCallResponse:
        runtime = RuntimeOptions()
        return self.ivr_call_with_options(request, runtime)

    async def ivr_call_async(
        self,
        request: main_models.IvrCallRequest,
    ) -> main_models.IvrCallResponse:
        runtime = RuntimeOptions()
        return await self.ivr_call_with_options_async(request, runtime)

    def list_call_task_with_options(
        self,
        request: main_models.ListCallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCallTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCallTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCallTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_call_task_with_options_async(
        self,
        request: main_models.ListCallTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCallTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCallTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCallTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_call_task(
        self,
        request: main_models.ListCallTaskRequest,
    ) -> main_models.ListCallTaskResponse:
        runtime = RuntimeOptions()
        return self.list_call_task_with_options(request, runtime)

    async def list_call_task_async(
        self,
        request: main_models.ListCallTaskRequest,
    ) -> main_models.ListCallTaskResponse:
        runtime = RuntimeOptions()
        return await self.list_call_task_with_options_async(request, runtime)

    def list_call_task_detail_with_options(
        self,
        request: main_models.ListCallTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCallTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_num):
            query['CalledNum'] = request.called_num
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCallTaskDetail',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCallTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_call_task_detail_with_options_async(
        self,
        request: main_models.ListCallTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCallTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_num):
            query['CalledNum'] = request.called_num
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCallTaskDetail',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCallTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_call_task_detail(
        self,
        request: main_models.ListCallTaskDetailRequest,
    ) -> main_models.ListCallTaskDetailResponse:
        runtime = RuntimeOptions()
        return self.list_call_task_detail_with_options(request, runtime)

    async def list_call_task_detail_async(
        self,
        request: main_models.ListCallTaskDetailRequest,
    ) -> main_models.ListCallTaskDetailResponse:
        runtime = RuntimeOptions()
        return await self.list_call_task_detail_with_options_async(request, runtime)

    def list_hotline_transfer_register_file_with_options(
        self,
        request: main_models.ListHotlineTransferRegisterFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotlineTransferRegisterFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hotline_number):
            query['HotlineNumber'] = request.hotline_number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHotlineTransferRegisterFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotlineTransferRegisterFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hotline_transfer_register_file_with_options_async(
        self,
        request: main_models.ListHotlineTransferRegisterFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHotlineTransferRegisterFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.hotline_number):
            query['HotlineNumber'] = request.hotline_number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHotlineTransferRegisterFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHotlineTransferRegisterFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hotline_transfer_register_file(
        self,
        request: main_models.ListHotlineTransferRegisterFileRequest,
    ) -> main_models.ListHotlineTransferRegisterFileResponse:
        runtime = RuntimeOptions()
        return self.list_hotline_transfer_register_file_with_options(request, runtime)

    async def list_hotline_transfer_register_file_async(
        self,
        request: main_models.ListHotlineTransferRegisterFileRequest,
    ) -> main_models.ListHotlineTransferRegisterFileResponse:
        runtime = RuntimeOptions()
        return await self.list_hotline_transfer_register_file_with_options_async(request, runtime)

    def list_service_instance_for_page_with_options(
        self,
        tmp_req: main_models.ListServiceInstanceForPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstanceForPageResponse:
        tmp_req.validate()
        request = main_models.ListServiceInstanceForPageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.pager):
            request.pager_shrink = Utils.array_to_string_with_specified_style(tmp_req.pager, 'Pager', 'json')
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pager_shrink):
            query['Pager'] = request.pager_shrink
        if not DaraCore.is_null(request.relation_number):
            query['RelationNumber'] = request.relation_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.usage_id):
            query['UsageId'] = request.usage_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstanceForPage',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstanceForPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_instance_for_page_with_options_async(
        self,
        tmp_req: main_models.ListServiceInstanceForPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstanceForPageResponse:
        tmp_req.validate()
        request = main_models.ListServiceInstanceForPageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.pager):
            request.pager_shrink = Utils.array_to_string_with_specified_style(tmp_req.pager, 'Pager', 'json')
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pager_shrink):
            query['Pager'] = request.pager_shrink
        if not DaraCore.is_null(request.relation_number):
            query['RelationNumber'] = request.relation_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scene_id):
            query['SceneId'] = request.scene_id
        if not DaraCore.is_null(request.usage_id):
            query['UsageId'] = request.usage_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstanceForPage',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstanceForPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_instance_for_page(
        self,
        request: main_models.ListServiceInstanceForPageRequest,
    ) -> main_models.ListServiceInstanceForPageResponse:
        runtime = RuntimeOptions()
        return self.list_service_instance_for_page_with_options(request, runtime)

    async def list_service_instance_for_page_async(
        self,
        request: main_models.ListServiceInstanceForPageRequest,
    ) -> main_models.ListServiceInstanceForPageResponse:
        runtime = RuntimeOptions()
        return await self.list_service_instance_for_page_with_options_async(request, runtime)

    def pause_video_file_with_options(
        self,
        request: main_models.PauseVideoFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PauseVideoFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PauseVideoFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PauseVideoFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_video_file_with_options_async(
        self,
        request: main_models.PauseVideoFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PauseVideoFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PauseVideoFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PauseVideoFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_video_file(
        self,
        request: main_models.PauseVideoFileRequest,
    ) -> main_models.PauseVideoFileResponse:
        runtime = RuntimeOptions()
        return self.pause_video_file_with_options(request, runtime)

    async def pause_video_file_async(
        self,
        request: main_models.PauseVideoFileRequest,
    ) -> main_models.PauseVideoFileResponse:
        runtime = RuntimeOptions()
        return await self.pause_video_file_with_options_async(request, runtime)

    def play_video_file_with_options(
        self,
        request: main_models.PlayVideoFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PlayVideoFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.only_phone):
            query['OnlyPhone'] = request.only_phone
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PlayVideoFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PlayVideoFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def play_video_file_with_options_async(
        self,
        request: main_models.PlayVideoFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PlayVideoFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.only_phone):
            query['OnlyPhone'] = request.only_phone
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.video_id):
            query['VideoId'] = request.video_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PlayVideoFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PlayVideoFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def play_video_file(
        self,
        request: main_models.PlayVideoFileRequest,
    ) -> main_models.PlayVideoFileResponse:
        runtime = RuntimeOptions()
        return self.play_video_file_with_options(request, runtime)

    async def play_video_file_async(
        self,
        request: main_models.PlayVideoFileRequest,
    ) -> main_models.PlayVideoFileResponse:
        runtime = RuntimeOptions()
        return await self.play_video_file_with_options_async(request, runtime)

    def query_call_detail_by_call_id_with_options(
        self,
        request: main_models.QueryCallDetailByCallIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCallDetailByCallIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_id):
            query['ProdId'] = request.prod_id
        if not DaraCore.is_null(request.query_date):
            query['QueryDate'] = request.query_date
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCallDetailByCallId',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCallDetailByCallIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_call_detail_by_call_id_with_options_async(
        self,
        request: main_models.QueryCallDetailByCallIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCallDetailByCallIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.prod_id):
            query['ProdId'] = request.prod_id
        if not DaraCore.is_null(request.query_date):
            query['QueryDate'] = request.query_date
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCallDetailByCallId',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCallDetailByCallIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_call_detail_by_call_id(
        self,
        request: main_models.QueryCallDetailByCallIdRequest,
    ) -> main_models.QueryCallDetailByCallIdResponse:
        runtime = RuntimeOptions()
        return self.query_call_detail_by_call_id_with_options(request, runtime)

    async def query_call_detail_by_call_id_async(
        self,
        request: main_models.QueryCallDetailByCallIdRequest,
    ) -> main_models.QueryCallDetailByCallIdResponse:
        runtime = RuntimeOptions()
        return await self.query_call_detail_by_call_id_with_options_async(request, runtime)

    def query_call_detail_by_task_id_with_options(
        self,
        request: main_models.QueryCallDetailByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCallDetailByTaskIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_date):
            query['QueryDate'] = request.query_date
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCallDetailByTaskId',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCallDetailByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_call_detail_by_task_id_with_options_async(
        self,
        request: main_models.QueryCallDetailByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCallDetailByTaskIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_date):
            query['QueryDate'] = request.query_date
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCallDetailByTaskId',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCallDetailByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_call_detail_by_task_id(
        self,
        request: main_models.QueryCallDetailByTaskIdRequest,
    ) -> main_models.QueryCallDetailByTaskIdResponse:
        runtime = RuntimeOptions()
        return self.query_call_detail_by_task_id_with_options(request, runtime)

    async def query_call_detail_by_task_id_async(
        self,
        request: main_models.QueryCallDetailByTaskIdRequest,
    ) -> main_models.QueryCallDetailByTaskIdResponse:
        runtime = RuntimeOptions()
        return await self.query_call_detail_by_task_id_with_options_async(request, runtime)

    def query_call_in_pool_transfer_config_with_options(
        self,
        request: main_models.QueryCallInPoolTransferConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCallInPoolTransferConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCallInPoolTransferConfig',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCallInPoolTransferConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_call_in_pool_transfer_config_with_options_async(
        self,
        request: main_models.QueryCallInPoolTransferConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCallInPoolTransferConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCallInPoolTransferConfig',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCallInPoolTransferConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_call_in_pool_transfer_config(
        self,
        request: main_models.QueryCallInPoolTransferConfigRequest,
    ) -> main_models.QueryCallInPoolTransferConfigResponse:
        runtime = RuntimeOptions()
        return self.query_call_in_pool_transfer_config_with_options(request, runtime)

    async def query_call_in_pool_transfer_config_async(
        self,
        request: main_models.QueryCallInPoolTransferConfigRequest,
    ) -> main_models.QueryCallInPoolTransferConfigResponse:
        runtime = RuntimeOptions()
        return await self.query_call_in_pool_transfer_config_with_options_async(request, runtime)

    def query_call_in_transfer_record_with_options(
        self,
        request: main_models.QueryCallInTransferRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCallInTransferRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_in_caller):
            query['CallInCaller'] = request.call_in_caller
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.query_date):
            query['QueryDate'] = request.query_date
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCallInTransferRecord',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCallInTransferRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_call_in_transfer_record_with_options_async(
        self,
        request: main_models.QueryCallInTransferRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCallInTransferRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_in_caller):
            query['CallInCaller'] = request.call_in_caller
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.query_date):
            query['QueryDate'] = request.query_date
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCallInTransferRecord',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCallInTransferRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_call_in_transfer_record(
        self,
        request: main_models.QueryCallInTransferRecordRequest,
    ) -> main_models.QueryCallInTransferRecordResponse:
        runtime = RuntimeOptions()
        return self.query_call_in_transfer_record_with_options(request, runtime)

    async def query_call_in_transfer_record_async(
        self,
        request: main_models.QueryCallInTransferRecordRequest,
    ) -> main_models.QueryCallInTransferRecordResponse:
        runtime = RuntimeOptions()
        return await self.query_call_in_transfer_record_with_options_async(request, runtime)

    def query_robot_info_list_with_options(
        self,
        request: main_models.QueryRobotInfoListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRobotInfoListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRobotInfoList',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRobotInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_robot_info_list_with_options_async(
        self,
        request: main_models.QueryRobotInfoListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRobotInfoListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRobotInfoList',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRobotInfoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_robot_info_list(
        self,
        request: main_models.QueryRobotInfoListRequest,
    ) -> main_models.QueryRobotInfoListResponse:
        runtime = RuntimeOptions()
        return self.query_robot_info_list_with_options(request, runtime)

    async def query_robot_info_list_async(
        self,
        request: main_models.QueryRobotInfoListRequest,
    ) -> main_models.QueryRobotInfoListResponse:
        runtime = RuntimeOptions()
        return await self.query_robot_info_list_with_options_async(request, runtime)

    def query_robot_task_call_detail_with_options(
        self,
        request: main_models.QueryRobotTaskCallDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRobotTaskCallDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_date):
            query['QueryDate'] = request.query_date
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRobotTaskCallDetail',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRobotTaskCallDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_robot_task_call_detail_with_options_async(
        self,
        request: main_models.QueryRobotTaskCallDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRobotTaskCallDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.callee):
            query['Callee'] = request.callee
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_date):
            query['QueryDate'] = request.query_date
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRobotTaskCallDetail',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRobotTaskCallDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_robot_task_call_detail(
        self,
        request: main_models.QueryRobotTaskCallDetailRequest,
    ) -> main_models.QueryRobotTaskCallDetailResponse:
        runtime = RuntimeOptions()
        return self.query_robot_task_call_detail_with_options(request, runtime)

    async def query_robot_task_call_detail_async(
        self,
        request: main_models.QueryRobotTaskCallDetailRequest,
    ) -> main_models.QueryRobotTaskCallDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_robot_task_call_detail_with_options_async(request, runtime)

    def query_robot_task_call_list_with_options(
        self,
        request: main_models.QueryRobotTaskCallListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRobotTaskCallListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_result):
            query['CallResult'] = request.call_result
        if not DaraCore.is_null(request.called):
            query['Called'] = request.called
        if not DaraCore.is_null(request.dialog_count_from):
            query['DialogCountFrom'] = request.dialog_count_from
        if not DaraCore.is_null(request.dialog_count_to):
            query['DialogCountTo'] = request.dialog_count_to
        if not DaraCore.is_null(request.duration_from):
            query['DurationFrom'] = request.duration_from
        if not DaraCore.is_null(request.duration_to):
            query['DurationTo'] = request.duration_to
        if not DaraCore.is_null(request.hangup_direction):
            query['HangupDirection'] = request.hangup_direction
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRobotTaskCallList',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRobotTaskCallListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_robot_task_call_list_with_options_async(
        self,
        request: main_models.QueryRobotTaskCallListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRobotTaskCallListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_result):
            query['CallResult'] = request.call_result
        if not DaraCore.is_null(request.called):
            query['Called'] = request.called
        if not DaraCore.is_null(request.dialog_count_from):
            query['DialogCountFrom'] = request.dialog_count_from
        if not DaraCore.is_null(request.dialog_count_to):
            query['DialogCountTo'] = request.dialog_count_to
        if not DaraCore.is_null(request.duration_from):
            query['DurationFrom'] = request.duration_from
        if not DaraCore.is_null(request.duration_to):
            query['DurationTo'] = request.duration_to
        if not DaraCore.is_null(request.hangup_direction):
            query['HangupDirection'] = request.hangup_direction
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRobotTaskCallList',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRobotTaskCallListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_robot_task_call_list(
        self,
        request: main_models.QueryRobotTaskCallListRequest,
    ) -> main_models.QueryRobotTaskCallListResponse:
        runtime = RuntimeOptions()
        return self.query_robot_task_call_list_with_options(request, runtime)

    async def query_robot_task_call_list_async(
        self,
        request: main_models.QueryRobotTaskCallListRequest,
    ) -> main_models.QueryRobotTaskCallListResponse:
        runtime = RuntimeOptions()
        return await self.query_robot_task_call_list_with_options_async(request, runtime)

    def query_robot_task_detail_with_options(
        self,
        request: main_models.QueryRobotTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRobotTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRobotTaskDetail',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRobotTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_robot_task_detail_with_options_async(
        self,
        request: main_models.QueryRobotTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRobotTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRobotTaskDetail',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRobotTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_robot_task_detail(
        self,
        request: main_models.QueryRobotTaskDetailRequest,
    ) -> main_models.QueryRobotTaskDetailResponse:
        runtime = RuntimeOptions()
        return self.query_robot_task_detail_with_options(request, runtime)

    async def query_robot_task_detail_async(
        self,
        request: main_models.QueryRobotTaskDetailRequest,
    ) -> main_models.QueryRobotTaskDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_robot_task_detail_with_options_async(request, runtime)

    def query_robot_task_list_with_options(
        self,
        request: main_models.QueryRobotTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRobotTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRobotTaskList',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRobotTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_robot_task_list_with_options_async(
        self,
        request: main_models.QueryRobotTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRobotTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.time):
            query['Time'] = request.time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRobotTaskList',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRobotTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_robot_task_list(
        self,
        request: main_models.QueryRobotTaskListRequest,
    ) -> main_models.QueryRobotTaskListResponse:
        runtime = RuntimeOptions()
        return self.query_robot_task_list_with_options(request, runtime)

    async def query_robot_task_list_async(
        self,
        request: main_models.QueryRobotTaskListRequest,
    ) -> main_models.QueryRobotTaskListResponse:
        runtime = RuntimeOptions()
        return await self.query_robot_task_list_with_options_async(request, runtime)

    def query_robotv_2all_list_with_options(
        self,
        request: main_models.QueryRobotv2AllListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRobotv2AllListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRobotv2AllList',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRobotv2AllListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_robotv_2all_list_with_options_async(
        self,
        request: main_models.QueryRobotv2AllListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRobotv2AllListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRobotv2AllList',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRobotv2AllListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_robotv_2all_list(
        self,
        request: main_models.QueryRobotv2AllListRequest,
    ) -> main_models.QueryRobotv2AllListResponse:
        runtime = RuntimeOptions()
        return self.query_robotv_2all_list_with_options(request, runtime)

    async def query_robotv_2all_list_async(
        self,
        request: main_models.QueryRobotv2AllListRequest,
    ) -> main_models.QueryRobotv2AllListResponse:
        runtime = RuntimeOptions()
        return await self.query_robotv_2all_list_with_options_async(request, runtime)

    def query_video_play_progress_with_options(
        self,
        request: main_models.QueryVideoPlayProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVideoPlayProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVideoPlayProgress',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVideoPlayProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_video_play_progress_with_options_async(
        self,
        request: main_models.QueryVideoPlayProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVideoPlayProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVideoPlayProgress',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVideoPlayProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_video_play_progress(
        self,
        request: main_models.QueryVideoPlayProgressRequest,
    ) -> main_models.QueryVideoPlayProgressResponse:
        runtime = RuntimeOptions()
        return self.query_video_play_progress_with_options(request, runtime)

    async def query_video_play_progress_async(
        self,
        request: main_models.QueryVideoPlayProgressRequest,
    ) -> main_models.QueryVideoPlayProgressResponse:
        runtime = RuntimeOptions()
        return await self.query_video_play_progress_with_options_async(request, runtime)

    def query_virtual_number_with_options(
        self,
        request: main_models.QueryVirtualNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVirtualNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_type):
            query['RouteType'] = request.route_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVirtualNumber',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVirtualNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_virtual_number_with_options_async(
        self,
        request: main_models.QueryVirtualNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVirtualNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_type):
            query['RouteType'] = request.route_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVirtualNumber',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVirtualNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_virtual_number(
        self,
        request: main_models.QueryVirtualNumberRequest,
    ) -> main_models.QueryVirtualNumberResponse:
        runtime = RuntimeOptions()
        return self.query_virtual_number_with_options(request, runtime)

    async def query_virtual_number_async(
        self,
        request: main_models.QueryVirtualNumberRequest,
    ) -> main_models.QueryVirtualNumberResponse:
        runtime = RuntimeOptions()
        return await self.query_virtual_number_with_options_async(request, runtime)

    def query_virtual_number_relation_with_options(
        self,
        request: main_models.QueryVirtualNumberRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVirtualNumberRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not DaraCore.is_null(request.region_name_city):
            query['RegionNameCity'] = request.region_name_city
        if not DaraCore.is_null(request.related_num):
            query['RelatedNum'] = request.related_num
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_type):
            query['RouteType'] = request.route_type
        if not DaraCore.is_null(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVirtualNumberRelation',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVirtualNumberRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_virtual_number_relation_with_options_async(
        self,
        request: main_models.QueryVirtualNumberRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVirtualNumberRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not DaraCore.is_null(request.region_name_city):
            query['RegionNameCity'] = request.region_name_city
        if not DaraCore.is_null(request.related_num):
            query['RelatedNum'] = request.related_num
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.route_type):
            query['RouteType'] = request.route_type
        if not DaraCore.is_null(request.spec_id):
            query['SpecId'] = request.spec_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVirtualNumberRelation',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVirtualNumberRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_virtual_number_relation(
        self,
        request: main_models.QueryVirtualNumberRelationRequest,
    ) -> main_models.QueryVirtualNumberRelationResponse:
        runtime = RuntimeOptions()
        return self.query_virtual_number_relation_with_options(request, runtime)

    async def query_virtual_number_relation_async(
        self,
        request: main_models.QueryVirtualNumberRelationRequest,
    ) -> main_models.QueryVirtualNumberRelationResponse:
        runtime = RuntimeOptions()
        return await self.query_virtual_number_relation_with_options_async(request, runtime)

    def query_vms_real_number_call_connection_rate_info_with_options(
        self,
        request: main_models.QueryVmsRealNumberCallConnectionRateInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVmsRealNumberCallConnectionRateInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.real_number):
            query['RealNumber'] = request.real_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.time_period):
            query['TimePeriod'] = request.time_period
        if not DaraCore.is_null(request.virtual_number):
            query['VirtualNumber'] = request.virtual_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVmsRealNumberCallConnectionRateInfo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVmsRealNumberCallConnectionRateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_vms_real_number_call_connection_rate_info_with_options_async(
        self,
        request: main_models.QueryVmsRealNumberCallConnectionRateInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVmsRealNumberCallConnectionRateInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.real_number):
            query['RealNumber'] = request.real_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.time_period):
            query['TimePeriod'] = request.time_period
        if not DaraCore.is_null(request.virtual_number):
            query['VirtualNumber'] = request.virtual_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVmsRealNumberCallConnectionRateInfo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVmsRealNumberCallConnectionRateInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_vms_real_number_call_connection_rate_info(
        self,
        request: main_models.QueryVmsRealNumberCallConnectionRateInfoRequest,
    ) -> main_models.QueryVmsRealNumberCallConnectionRateInfoResponse:
        runtime = RuntimeOptions()
        return self.query_vms_real_number_call_connection_rate_info_with_options(request, runtime)

    async def query_vms_real_number_call_connection_rate_info_async(
        self,
        request: main_models.QueryVmsRealNumberCallConnectionRateInfoRequest,
    ) -> main_models.QueryVmsRealNumberCallConnectionRateInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_vms_real_number_call_connection_rate_info_with_options_async(request, runtime)

    def query_vms_virtual_number_relation_by_page_with_options(
        self,
        request: main_models.QueryVmsVirtualNumberRelationByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVmsVirtualNumberRelationByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.number_city):
            query['NumberCity'] = request.number_city
        if not DaraCore.is_null(request.number_province):
            query['NumberProvince'] = request.number_province
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.real_number):
            query['RealNumber'] = request.real_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.virtual_number):
            query['VirtualNumber'] = request.virtual_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVmsVirtualNumberRelationByPage',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVmsVirtualNumberRelationByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_vms_virtual_number_relation_by_page_with_options_async(
        self,
        request: main_models.QueryVmsVirtualNumberRelationByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVmsVirtualNumberRelationByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.number_city):
            query['NumberCity'] = request.number_city
        if not DaraCore.is_null(request.number_province):
            query['NumberProvince'] = request.number_province
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.real_number):
            query['RealNumber'] = request.real_number
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.virtual_number):
            query['VirtualNumber'] = request.virtual_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVmsVirtualNumberRelationByPage',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVmsVirtualNumberRelationByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_vms_virtual_number_relation_by_page(
        self,
        request: main_models.QueryVmsVirtualNumberRelationByPageRequest,
    ) -> main_models.QueryVmsVirtualNumberRelationByPageResponse:
        runtime = RuntimeOptions()
        return self.query_vms_virtual_number_relation_by_page_with_options(request, runtime)

    async def query_vms_virtual_number_relation_by_page_async(
        self,
        request: main_models.QueryVmsVirtualNumberRelationByPageRequest,
    ) -> main_models.QueryVmsVirtualNumberRelationByPageResponse:
        runtime = RuntimeOptions()
        return await self.query_vms_virtual_number_relation_by_page_with_options_async(request, runtime)

    def query_voice_file_audit_info_with_options(
        self,
        request: main_models.QueryVoiceFileAuditInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVoiceFileAuditInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.voice_codes):
            query['VoiceCodes'] = request.voice_codes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVoiceFileAuditInfo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVoiceFileAuditInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_voice_file_audit_info_with_options_async(
        self,
        request: main_models.QueryVoiceFileAuditInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryVoiceFileAuditInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.voice_codes):
            query['VoiceCodes'] = request.voice_codes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryVoiceFileAuditInfo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryVoiceFileAuditInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_voice_file_audit_info(
        self,
        request: main_models.QueryVoiceFileAuditInfoRequest,
    ) -> main_models.QueryVoiceFileAuditInfoResponse:
        runtime = RuntimeOptions()
        return self.query_voice_file_audit_info_with_options(request, runtime)

    async def query_voice_file_audit_info_async(
        self,
        request: main_models.QueryVoiceFileAuditInfoRequest,
    ) -> main_models.QueryVoiceFileAuditInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_voice_file_audit_info_with_options_async(request, runtime)

    def recover_call_in_config_with_options(
        self,
        request: main_models.RecoverCallInConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecoverCallInConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecoverCallInConfig',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecoverCallInConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def recover_call_in_config_with_options_async(
        self,
        request: main_models.RecoverCallInConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RecoverCallInConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RecoverCallInConfig',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RecoverCallInConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recover_call_in_config(
        self,
        request: main_models.RecoverCallInConfigRequest,
    ) -> main_models.RecoverCallInConfigResponse:
        runtime = RuntimeOptions()
        return self.recover_call_in_config_with_options(request, runtime)

    async def recover_call_in_config_async(
        self,
        request: main_models.RecoverCallInConfigRequest,
    ) -> main_models.RecoverCallInConfigResponse:
        runtime = RuntimeOptions()
        return await self.recover_call_in_config_with_options_async(request, runtime)

    def resume_video_file_with_options(
        self,
        request: main_models.ResumeVideoFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeVideoFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeVideoFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeVideoFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_video_file_with_options_async(
        self,
        request: main_models.ResumeVideoFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeVideoFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResumeVideoFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeVideoFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_video_file(
        self,
        request: main_models.ResumeVideoFileRequest,
    ) -> main_models.ResumeVideoFileResponse:
        runtime = RuntimeOptions()
        return self.resume_video_file_with_options(request, runtime)

    async def resume_video_file_async(
        self,
        request: main_models.ResumeVideoFileRequest,
    ) -> main_models.ResumeVideoFileResponse:
        runtime = RuntimeOptions()
        return await self.resume_video_file_with_options_async(request, runtime)

    def seek_video_file_with_options(
        self,
        request: main_models.SeekVideoFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SeekVideoFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.seek_times):
            query['SeekTimes'] = request.seek_times
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SeekVideoFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SeekVideoFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def seek_video_file_with_options_async(
        self,
        request: main_models.SeekVideoFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SeekVideoFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.seek_times):
            query['SeekTimes'] = request.seek_times
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SeekVideoFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SeekVideoFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def seek_video_file(
        self,
        request: main_models.SeekVideoFileRequest,
    ) -> main_models.SeekVideoFileResponse:
        runtime = RuntimeOptions()
        return self.seek_video_file_with_options(request, runtime)

    async def seek_video_file_async(
        self,
        request: main_models.SeekVideoFileRequest,
    ) -> main_models.SeekVideoFileResponse:
        runtime = RuntimeOptions()
        return await self.seek_video_file_with_options_async(request, runtime)

    def send_verification_with_options(
        self,
        request: main_models.SendVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendVerification',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendVerificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_verification_with_options_async(
        self,
        request: main_models.SendVerificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendVerificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendVerification',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendVerificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_verification(
        self,
        request: main_models.SendVerificationRequest,
    ) -> main_models.SendVerificationResponse:
        runtime = RuntimeOptions()
        return self.send_verification_with_options(request, runtime)

    async def send_verification_async(
        self,
        request: main_models.SendVerificationRequest,
    ) -> main_models.SendVerificationResponse:
        runtime = RuntimeOptions()
        return await self.send_verification_with_options_async(request, runtime)

    def set_transfer_callee_pool_config_with_options(
        self,
        request: main_models.SetTransferCalleePoolConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetTransferCalleePoolConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_route_mode):
            query['CalledRouteMode'] = request.called_route_mode
        if not DaraCore.is_null(request.details):
            query['Details'] = request.details
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetTransferCalleePoolConfig',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetTransferCalleePoolConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_transfer_callee_pool_config_with_options_async(
        self,
        request: main_models.SetTransferCalleePoolConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetTransferCalleePoolConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_route_mode):
            query['CalledRouteMode'] = request.called_route_mode
        if not DaraCore.is_null(request.details):
            query['Details'] = request.details
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetTransferCalleePoolConfig',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetTransferCalleePoolConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_transfer_callee_pool_config(
        self,
        request: main_models.SetTransferCalleePoolConfigRequest,
    ) -> main_models.SetTransferCalleePoolConfigResponse:
        runtime = RuntimeOptions()
        return self.set_transfer_callee_pool_config_with_options(request, runtime)

    async def set_transfer_callee_pool_config_async(
        self,
        request: main_models.SetTransferCalleePoolConfigRequest,
    ) -> main_models.SetTransferCalleePoolConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_transfer_callee_pool_config_with_options_async(request, runtime)

    def single_call_by_tts_with_options(
        self,
        request: main_models.SingleCallByTtsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SingleCallByTtsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_times):
            query['PlayTimes'] = request.play_times
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.speed):
            query['Speed'] = request.speed
        if not DaraCore.is_null(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not DaraCore.is_null(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SingleCallByTts',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SingleCallByTtsResponse(),
            self.call_api(params, req, runtime)
        )

    async def single_call_by_tts_with_options_async(
        self,
        request: main_models.SingleCallByTtsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SingleCallByTtsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_times):
            query['PlayTimes'] = request.play_times
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.speed):
            query['Speed'] = request.speed
        if not DaraCore.is_null(request.tts_code):
            query['TtsCode'] = request.tts_code
        if not DaraCore.is_null(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SingleCallByTts',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SingleCallByTtsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def single_call_by_tts(
        self,
        request: main_models.SingleCallByTtsRequest,
    ) -> main_models.SingleCallByTtsResponse:
        runtime = RuntimeOptions()
        return self.single_call_by_tts_with_options(request, runtime)

    async def single_call_by_tts_async(
        self,
        request: main_models.SingleCallByTtsRequest,
    ) -> main_models.SingleCallByTtsResponse:
        runtime = RuntimeOptions()
        return await self.single_call_by_tts_with_options_async(request, runtime)

    def single_call_by_video_with_options(
        self,
        request: main_models.SingleCallByVideoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SingleCallByVideoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_times):
            query['PlayTimes'] = request.play_times
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.speed):
            query['Speed'] = request.speed
        if not DaraCore.is_null(request.video_code):
            query['VideoCode'] = request.video_code
        if not DaraCore.is_null(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SingleCallByVideo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SingleCallByVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def single_call_by_video_with_options_async(
        self,
        request: main_models.SingleCallByVideoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SingleCallByVideoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_times):
            query['PlayTimes'] = request.play_times
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.speed):
            query['Speed'] = request.speed
        if not DaraCore.is_null(request.video_code):
            query['VideoCode'] = request.video_code
        if not DaraCore.is_null(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SingleCallByVideo',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SingleCallByVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def single_call_by_video(
        self,
        request: main_models.SingleCallByVideoRequest,
    ) -> main_models.SingleCallByVideoResponse:
        runtime = RuntimeOptions()
        return self.single_call_by_video_with_options(request, runtime)

    async def single_call_by_video_async(
        self,
        request: main_models.SingleCallByVideoRequest,
    ) -> main_models.SingleCallByVideoResponse:
        runtime = RuntimeOptions()
        return await self.single_call_by_video_with_options_async(request, runtime)

    def single_call_by_voice_with_options(
        self,
        request: main_models.SingleCallByVoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SingleCallByVoiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_times):
            query['PlayTimes'] = request.play_times
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.speed):
            query['Speed'] = request.speed
        if not DaraCore.is_null(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SingleCallByVoice',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SingleCallByVoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def single_call_by_voice_with_options_async(
        self,
        request: main_models.SingleCallByVoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SingleCallByVoiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.play_times):
            query['PlayTimes'] = request.play_times
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.speed):
            query['Speed'] = request.speed
        if not DaraCore.is_null(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SingleCallByVoice',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SingleCallByVoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def single_call_by_voice(
        self,
        request: main_models.SingleCallByVoiceRequest,
    ) -> main_models.SingleCallByVoiceResponse:
        runtime = RuntimeOptions()
        return self.single_call_by_voice_with_options(request, runtime)

    async def single_call_by_voice_async(
        self,
        request: main_models.SingleCallByVoiceRequest,
    ) -> main_models.SingleCallByVoiceResponse:
        runtime = RuntimeOptions()
        return await self.single_call_by_voice_with_options_async(request, runtime)

    def skip_video_file_with_options(
        self,
        request: main_models.SkipVideoFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SkipVideoFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.skip_times):
            query['SkipTimes'] = request.skip_times
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SkipVideoFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SkipVideoFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def skip_video_file_with_options_async(
        self,
        request: main_models.SkipVideoFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SkipVideoFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.skip_times):
            query['SkipTimes'] = request.skip_times
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SkipVideoFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SkipVideoFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def skip_video_file(
        self,
        request: main_models.SkipVideoFileRequest,
    ) -> main_models.SkipVideoFileResponse:
        runtime = RuntimeOptions()
        return self.skip_video_file_with_options(request, runtime)

    async def skip_video_file_async(
        self,
        request: main_models.SkipVideoFileRequest,
    ) -> main_models.SkipVideoFileResponse:
        runtime = RuntimeOptions()
        return await self.skip_video_file_with_options_async(request, runtime)

    def smart_call_with_options(
        self,
        request: main_models.SmartCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SmartCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_code_break):
            query['ActionCodeBreak'] = request.action_code_break
        if not DaraCore.is_null(request.action_code_time_break):
            query['ActionCodeTimeBreak'] = request.action_code_time_break
        if not DaraCore.is_null(request.asr_base_id):
            query['AsrBaseId'] = request.asr_base_id
        if not DaraCore.is_null(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not DaraCore.is_null(request.background_file_code):
            query['BackgroundFileCode'] = request.background_file_code
        if not DaraCore.is_null(request.background_speed):
            query['BackgroundSpeed'] = request.background_speed
        if not DaraCore.is_null(request.background_volume):
            query['BackgroundVolume'] = request.background_volume
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.dynamic_id):
            query['DynamicId'] = request.dynamic_id
        if not DaraCore.is_null(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not DaraCore.is_null(request.enable_itn):
            query['EnableITN'] = request.enable_itn
        if not DaraCore.is_null(request.mute_time):
            query['MuteTime'] = request.mute_time
        if not DaraCore.is_null(request.noise_threshold):
            query['NoiseThreshold'] = request.noise_threshold
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pause_time):
            query['PauseTime'] = request.pause_time
        if not DaraCore.is_null(request.record_flag):
            query['RecordFlag'] = request.record_flag
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        if not DaraCore.is_null(request.speed):
            query['Speed'] = request.speed
        if not DaraCore.is_null(request.stream_asr):
            query['StreamAsr'] = request.stream_asr
        if not DaraCore.is_null(request.tts_conf):
            query['TtsConf'] = request.tts_conf
        if not DaraCore.is_null(request.tts_speed):
            query['TtsSpeed'] = request.tts_speed
        if not DaraCore.is_null(request.tts_style):
            query['TtsStyle'] = request.tts_style
        if not DaraCore.is_null(request.tts_volume):
            query['TtsVolume'] = request.tts_volume
        if not DaraCore.is_null(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not DaraCore.is_null(request.voice_code_param):
            query['VoiceCodeParam'] = request.voice_code_param
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SmartCall',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SmartCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def smart_call_with_options_async(
        self,
        request: main_models.SmartCallRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SmartCallResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_code_break):
            query['ActionCodeBreak'] = request.action_code_break
        if not DaraCore.is_null(request.action_code_time_break):
            query['ActionCodeTimeBreak'] = request.action_code_time_break
        if not DaraCore.is_null(request.asr_base_id):
            query['AsrBaseId'] = request.asr_base_id
        if not DaraCore.is_null(request.asr_model_id):
            query['AsrModelId'] = request.asr_model_id
        if not DaraCore.is_null(request.background_file_code):
            query['BackgroundFileCode'] = request.background_file_code
        if not DaraCore.is_null(request.background_speed):
            query['BackgroundSpeed'] = request.background_speed
        if not DaraCore.is_null(request.background_volume):
            query['BackgroundVolume'] = request.background_volume
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.called_show_number):
            query['CalledShowNumber'] = request.called_show_number
        if not DaraCore.is_null(request.dynamic_id):
            query['DynamicId'] = request.dynamic_id
        if not DaraCore.is_null(request.early_media_asr):
            query['EarlyMediaAsr'] = request.early_media_asr
        if not DaraCore.is_null(request.enable_itn):
            query['EnableITN'] = request.enable_itn
        if not DaraCore.is_null(request.mute_time):
            query['MuteTime'] = request.mute_time
        if not DaraCore.is_null(request.noise_threshold):
            query['NoiseThreshold'] = request.noise_threshold
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pause_time):
            query['PauseTime'] = request.pause_time
        if not DaraCore.is_null(request.record_flag):
            query['RecordFlag'] = request.record_flag
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.session_timeout):
            query['SessionTimeout'] = request.session_timeout
        if not DaraCore.is_null(request.speed):
            query['Speed'] = request.speed
        if not DaraCore.is_null(request.stream_asr):
            query['StreamAsr'] = request.stream_asr
        if not DaraCore.is_null(request.tts_conf):
            query['TtsConf'] = request.tts_conf
        if not DaraCore.is_null(request.tts_speed):
            query['TtsSpeed'] = request.tts_speed
        if not DaraCore.is_null(request.tts_style):
            query['TtsStyle'] = request.tts_style
        if not DaraCore.is_null(request.tts_volume):
            query['TtsVolume'] = request.tts_volume
        if not DaraCore.is_null(request.voice_code):
            query['VoiceCode'] = request.voice_code
        if not DaraCore.is_null(request.voice_code_param):
            query['VoiceCodeParam'] = request.voice_code_param
        if not DaraCore.is_null(request.volume):
            query['Volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SmartCall',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SmartCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def smart_call(
        self,
        request: main_models.SmartCallRequest,
    ) -> main_models.SmartCallResponse:
        runtime = RuntimeOptions()
        return self.smart_call_with_options(request, runtime)

    async def smart_call_async(
        self,
        request: main_models.SmartCallRequest,
    ) -> main_models.SmartCallResponse:
        runtime = RuntimeOptions()
        return await self.smart_call_with_options_async(request, runtime)

    def smart_call_operate_with_options(
        self,
        request: main_models.SmartCallOperateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SmartCallOperateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SmartCallOperate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SmartCallOperateResponse(),
            self.call_api(params, req, runtime)
        )

    async def smart_call_operate_with_options_async(
        self,
        request: main_models.SmartCallOperateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SmartCallOperateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SmartCallOperate',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SmartCallOperateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def smart_call_operate(
        self,
        request: main_models.SmartCallOperateRequest,
    ) -> main_models.SmartCallOperateResponse:
        runtime = RuntimeOptions()
        return self.smart_call_operate_with_options(request, runtime)

    async def smart_call_operate_async(
        self,
        request: main_models.SmartCallOperateRequest,
    ) -> main_models.SmartCallOperateResponse:
        runtime = RuntimeOptions()
        return await self.smart_call_operate_with_options_async(request, runtime)

    def start_robot_task_with_options(
        self,
        request: main_models.StartRobotTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartRobotTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartRobotTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_robot_task_with_options_async(
        self,
        request: main_models.StartRobotTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartRobotTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartRobotTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartRobotTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_robot_task(
        self,
        request: main_models.StartRobotTaskRequest,
    ) -> main_models.StartRobotTaskResponse:
        runtime = RuntimeOptions()
        return self.start_robot_task_with_options(request, runtime)

    async def start_robot_task_async(
        self,
        request: main_models.StartRobotTaskRequest,
    ) -> main_models.StartRobotTaskResponse:
        runtime = RuntimeOptions()
        return await self.start_robot_task_with_options_async(request, runtime)

    def stop_call_in_config_with_options(
        self,
        request: main_models.StopCallInConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopCallInConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopCallInConfig',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopCallInConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_call_in_config_with_options_async(
        self,
        request: main_models.StopCallInConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopCallInConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.number):
            query['Number'] = request.number
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopCallInConfig',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopCallInConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_call_in_config(
        self,
        request: main_models.StopCallInConfigRequest,
    ) -> main_models.StopCallInConfigResponse:
        runtime = RuntimeOptions()
        return self.stop_call_in_config_with_options(request, runtime)

    async def stop_call_in_config_async(
        self,
        request: main_models.StopCallInConfigRequest,
    ) -> main_models.StopCallInConfigResponse:
        runtime = RuntimeOptions()
        return await self.stop_call_in_config_with_options_async(request, runtime)

    def stop_robot_task_with_options(
        self,
        request: main_models.StopRobotTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopRobotTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopRobotTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopRobotTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_robot_task_with_options_async(
        self,
        request: main_models.StopRobotTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopRobotTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopRobotTask',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopRobotTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_robot_task(
        self,
        request: main_models.StopRobotTaskRequest,
    ) -> main_models.StopRobotTaskResponse:
        runtime = RuntimeOptions()
        return self.stop_robot_task_with_options(request, runtime)

    async def stop_robot_task_async(
        self,
        request: main_models.StopRobotTaskRequest,
    ) -> main_models.StopRobotTaskResponse:
        runtime = RuntimeOptions()
        return await self.stop_robot_task_with_options_async(request, runtime)

    def submit_hotline_transfer_register_with_options(
        self,
        request: main_models.SubmitHotlineTransferRegisterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitHotlineTransferRegisterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agreement):
            query['Agreement'] = request.agreement
        if not DaraCore.is_null(request.hotline_number):
            query['HotlineNumber'] = request.hotline_number
        if not DaraCore.is_null(request.operator_identity_card):
            query['OperatorIdentityCard'] = request.operator_identity_card
        if not DaraCore.is_null(request.operator_mail):
            query['OperatorMail'] = request.operator_mail
        if not DaraCore.is_null(request.operator_mail_verify_code):
            query['OperatorMailVerifyCode'] = request.operator_mail_verify_code
        if not DaraCore.is_null(request.operator_mobile):
            query['OperatorMobile'] = request.operator_mobile
        if not DaraCore.is_null(request.operator_mobile_verify_code):
            query['OperatorMobileVerifyCode'] = request.operator_mobile_verify_code
        if not DaraCore.is_null(request.operator_name):
            query['OperatorName'] = request.operator_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transfer_phone_number_infos):
            query['TransferPhoneNumberInfos'] = request.transfer_phone_number_infos
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitHotlineTransferRegister',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitHotlineTransferRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_hotline_transfer_register_with_options_async(
        self,
        request: main_models.SubmitHotlineTransferRegisterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitHotlineTransferRegisterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agreement):
            query['Agreement'] = request.agreement
        if not DaraCore.is_null(request.hotline_number):
            query['HotlineNumber'] = request.hotline_number
        if not DaraCore.is_null(request.operator_identity_card):
            query['OperatorIdentityCard'] = request.operator_identity_card
        if not DaraCore.is_null(request.operator_mail):
            query['OperatorMail'] = request.operator_mail
        if not DaraCore.is_null(request.operator_mail_verify_code):
            query['OperatorMailVerifyCode'] = request.operator_mail_verify_code
        if not DaraCore.is_null(request.operator_mobile):
            query['OperatorMobile'] = request.operator_mobile
        if not DaraCore.is_null(request.operator_mobile_verify_code):
            query['OperatorMobileVerifyCode'] = request.operator_mobile_verify_code
        if not DaraCore.is_null(request.operator_name):
            query['OperatorName'] = request.operator_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.qualification_id):
            query['QualificationId'] = request.qualification_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.transfer_phone_number_infos):
            query['TransferPhoneNumberInfos'] = request.transfer_phone_number_infos
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitHotlineTransferRegister',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitHotlineTransferRegisterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_hotline_transfer_register(
        self,
        request: main_models.SubmitHotlineTransferRegisterRequest,
    ) -> main_models.SubmitHotlineTransferRegisterResponse:
        runtime = RuntimeOptions()
        return self.submit_hotline_transfer_register_with_options(request, runtime)

    async def submit_hotline_transfer_register_async(
        self,
        request: main_models.SubmitHotlineTransferRegisterRequest,
    ) -> main_models.SubmitHotlineTransferRegisterResponse:
        runtime = RuntimeOptions()
        return await self.submit_hotline_transfer_register_with_options_async(request, runtime)

    def upgrade_video_file_with_options(
        self,
        request: main_models.UpgradeVideoFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeVideoFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeVideoFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeVideoFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_video_file_with_options_async(
        self,
        request: main_models.UpgradeVideoFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeVideoFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_id):
            query['CallId'] = request.call_id
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.out_id):
            query['OutId'] = request.out_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeVideoFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeVideoFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_video_file(
        self,
        request: main_models.UpgradeVideoFileRequest,
    ) -> main_models.UpgradeVideoFileResponse:
        runtime = RuntimeOptions()
        return self.upgrade_video_file_with_options(request, runtime)

    async def upgrade_video_file_async(
        self,
        request: main_models.UpgradeVideoFileRequest,
    ) -> main_models.UpgradeVideoFileResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_video_file_with_options_async(request, runtime)

    def upload_robot_task_called_file_with_options(
        self,
        request: main_models.UploadRobotTaskCalledFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadRobotTaskCalledFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not DaraCore.is_null(request.tts_param_head):
            query['TtsParamHead'] = request.tts_param_head
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadRobotTaskCalledFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadRobotTaskCalledFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_robot_task_called_file_with_options_async(
        self,
        request: main_models.UploadRobotTaskCalledFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadRobotTaskCalledFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.called_number):
            query['CalledNumber'] = request.called_number
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tts_param):
            query['TtsParam'] = request.tts_param
        if not DaraCore.is_null(request.tts_param_head):
            query['TtsParamHead'] = request.tts_param_head
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadRobotTaskCalledFile',
            version = '2017-05-25',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadRobotTaskCalledFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_robot_task_called_file(
        self,
        request: main_models.UploadRobotTaskCalledFileRequest,
    ) -> main_models.UploadRobotTaskCalledFileResponse:
        runtime = RuntimeOptions()
        return self.upload_robot_task_called_file_with_options(request, runtime)

    async def upload_robot_task_called_file_async(
        self,
        request: main_models.UploadRobotTaskCalledFileRequest,
    ) -> main_models.UploadRobotTaskCalledFileResponse:
        runtime = RuntimeOptions()
        return await self.upload_robot_task_called_file_with_options_async(request, runtime)
