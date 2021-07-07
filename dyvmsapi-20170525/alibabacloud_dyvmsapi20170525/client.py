# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dyvmsapi20170525 import models as dyvmsapi_20170525_models
from alibabacloud_tea_util import models as util_models


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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_rtc_account_with_options(
        self,
        request: dyvmsapi_20170525_models.AddRtcAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.AddRtcAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.AddRtcAccountResponse(),
            self.do_rpcrequest('AddRtcAccount', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_rtc_account_with_options_async(
        self,
        request: dyvmsapi_20170525_models.AddRtcAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.AddRtcAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.AddRtcAccountResponse(),
            await self.do_rpcrequest_async('AddRtcAccount', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_rtc_account(
        self,
        request: dyvmsapi_20170525_models.AddRtcAccountRequest,
    ) -> dyvmsapi_20170525_models.AddRtcAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_rtc_account_with_options(request, runtime)

    async def add_rtc_account_async(
        self,
        request: dyvmsapi_20170525_models.AddRtcAccountRequest,
    ) -> dyvmsapi_20170525_models.AddRtcAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_rtc_account_with_options_async(request, runtime)

    def add_virtual_number_relation_with_options(
        self,
        request: dyvmsapi_20170525_models.AddVirtualNumberRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.AddVirtualNumberRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.AddVirtualNumberRelationResponse(),
            self.do_rpcrequest('AddVirtualNumberRelation', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_virtual_number_relation_with_options_async(
        self,
        request: dyvmsapi_20170525_models.AddVirtualNumberRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.AddVirtualNumberRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.AddVirtualNumberRelationResponse(),
            await self.do_rpcrequest_async('AddVirtualNumberRelation', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_virtual_number_relation(
        self,
        request: dyvmsapi_20170525_models.AddVirtualNumberRelationRequest,
    ) -> dyvmsapi_20170525_models.AddVirtualNumberRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_virtual_number_relation_with_options(request, runtime)

    async def add_virtual_number_relation_async(
        self,
        request: dyvmsapi_20170525_models.AddVirtualNumberRelationRequest,
    ) -> dyvmsapi_20170525_models.AddVirtualNumberRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_virtual_number_relation_with_options_async(request, runtime)

    def batch_robot_smart_call_with_options(
        self,
        request: dyvmsapi_20170525_models.BatchRobotSmartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.BatchRobotSmartCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.BatchRobotSmartCallResponse(),
            self.do_rpcrequest('BatchRobotSmartCall', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_robot_smart_call_with_options_async(
        self,
        request: dyvmsapi_20170525_models.BatchRobotSmartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.BatchRobotSmartCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.BatchRobotSmartCallResponse(),
            await self.do_rpcrequest_async('BatchRobotSmartCall', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_robot_smart_call(
        self,
        request: dyvmsapi_20170525_models.BatchRobotSmartCallRequest,
    ) -> dyvmsapi_20170525_models.BatchRobotSmartCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_robot_smart_call_with_options(request, runtime)

    async def batch_robot_smart_call_async(
        self,
        request: dyvmsapi_20170525_models.BatchRobotSmartCallRequest,
    ) -> dyvmsapi_20170525_models.BatchRobotSmartCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_robot_smart_call_with_options_async(request, runtime)

    def bind_number_and_voip_id_with_options(
        self,
        request: dyvmsapi_20170525_models.BindNumberAndVoipIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.BindNumberAndVoipIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.BindNumberAndVoipIdResponse(),
            self.do_rpcrequest('BindNumberAndVoipId', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def bind_number_and_voip_id_with_options_async(
        self,
        request: dyvmsapi_20170525_models.BindNumberAndVoipIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.BindNumberAndVoipIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.BindNumberAndVoipIdResponse(),
            await self.do_rpcrequest_async('BindNumberAndVoipId', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_number_and_voip_id(
        self,
        request: dyvmsapi_20170525_models.BindNumberAndVoipIdRequest,
    ) -> dyvmsapi_20170525_models.BindNumberAndVoipIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_number_and_voip_id_with_options(request, runtime)

    async def bind_number_and_voip_id_async(
        self,
        request: dyvmsapi_20170525_models.BindNumberAndVoipIdRequest,
    ) -> dyvmsapi_20170525_models.BindNumberAndVoipIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_number_and_voip_id_with_options_async(request, runtime)

    def cancel_call_with_options(
        self,
        request: dyvmsapi_20170525_models.CancelCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CancelCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CancelCallResponse(),
            self.do_rpcrequest('CancelCall', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_call_with_options_async(
        self,
        request: dyvmsapi_20170525_models.CancelCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CancelCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CancelCallResponse(),
            await self.do_rpcrequest_async('CancelCall', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_call(
        self,
        request: dyvmsapi_20170525_models.CancelCallRequest,
    ) -> dyvmsapi_20170525_models.CancelCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_call_with_options(request, runtime)

    async def cancel_call_async(
        self,
        request: dyvmsapi_20170525_models.CancelCallRequest,
    ) -> dyvmsapi_20170525_models.CancelCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_call_with_options_async(request, runtime)

    def cancel_order_robot_task_with_options(
        self,
        request: dyvmsapi_20170525_models.CancelOrderRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CancelOrderRobotTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CancelOrderRobotTaskResponse(),
            self.do_rpcrequest('CancelOrderRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_order_robot_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.CancelOrderRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CancelOrderRobotTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CancelOrderRobotTaskResponse(),
            await self.do_rpcrequest_async('CancelOrderRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_order_robot_task(
        self,
        request: dyvmsapi_20170525_models.CancelOrderRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.CancelOrderRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_order_robot_task_with_options(request, runtime)

    async def cancel_order_robot_task_async(
        self,
        request: dyvmsapi_20170525_models.CancelOrderRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.CancelOrderRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_order_robot_task_with_options_async(request, runtime)

    def cancel_robot_task_with_options(
        self,
        request: dyvmsapi_20170525_models.CancelRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CancelRobotTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CancelRobotTaskResponse(),
            self.do_rpcrequest('CancelRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_robot_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.CancelRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CancelRobotTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CancelRobotTaskResponse(),
            await self.do_rpcrequest_async('CancelRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_robot_task(
        self,
        request: dyvmsapi_20170525_models.CancelRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.CancelRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_robot_task_with_options(request, runtime)

    async def cancel_robot_task_async(
        self,
        request: dyvmsapi_20170525_models.CancelRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.CancelRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_robot_task_with_options_async(request, runtime)

    def click_to_dial_with_options(
        self,
        request: dyvmsapi_20170525_models.ClickToDialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ClickToDialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ClickToDialResponse(),
            self.do_rpcrequest('ClickToDial', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def click_to_dial_with_options_async(
        self,
        request: dyvmsapi_20170525_models.ClickToDialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ClickToDialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ClickToDialResponse(),
            await self.do_rpcrequest_async('ClickToDial', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def click_to_dial(
        self,
        request: dyvmsapi_20170525_models.ClickToDialRequest,
    ) -> dyvmsapi_20170525_models.ClickToDialResponse:
        runtime = util_models.RuntimeOptions()
        return self.click_to_dial_with_options(request, runtime)

    async def click_to_dial_async(
        self,
        request: dyvmsapi_20170525_models.ClickToDialRequest,
    ) -> dyvmsapi_20170525_models.ClickToDialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.click_to_dial_with_options_async(request, runtime)

    def close_sip_account_with_options(
        self,
        request: dyvmsapi_20170525_models.CloseSipAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CloseSipAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CloseSipAccountResponse(),
            self.do_rpcrequest('CloseSipAccount', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def close_sip_account_with_options_async(
        self,
        request: dyvmsapi_20170525_models.CloseSipAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CloseSipAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CloseSipAccountResponse(),
            await self.do_rpcrequest_async('CloseSipAccount', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def close_sip_account(
        self,
        request: dyvmsapi_20170525_models.CloseSipAccountRequest,
    ) -> dyvmsapi_20170525_models.CloseSipAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_sip_account_with_options(request, runtime)

    async def close_sip_account_async(
        self,
        request: dyvmsapi_20170525_models.CloseSipAccountRequest,
    ) -> dyvmsapi_20170525_models.CloseSipAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_sip_account_with_options_async(request, runtime)

    def create_call_task_with_options(
        self,
        request: dyvmsapi_20170525_models.CreateCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CreateCallTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CreateCallTaskResponse(),
            self.do_rpcrequest('CreateCallTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_call_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.CreateCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CreateCallTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CreateCallTaskResponse(),
            await self.do_rpcrequest_async('CreateCallTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_call_task(
        self,
        request: dyvmsapi_20170525_models.CreateCallTaskRequest,
    ) -> dyvmsapi_20170525_models.CreateCallTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_call_task_with_options(request, runtime)

    async def create_call_task_async(
        self,
        request: dyvmsapi_20170525_models.CreateCallTaskRequest,
    ) -> dyvmsapi_20170525_models.CreateCallTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_call_task_with_options_async(request, runtime)

    def create_robot_task_with_options(
        self,
        request: dyvmsapi_20170525_models.CreateRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CreateRobotTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CreateRobotTaskResponse(),
            self.do_rpcrequest('CreateRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_robot_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.CreateRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CreateRobotTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CreateRobotTaskResponse(),
            await self.do_rpcrequest_async('CreateRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_robot_task(
        self,
        request: dyvmsapi_20170525_models.CreateRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.CreateRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_robot_task_with_options(request, runtime)

    async def create_robot_task_async(
        self,
        request: dyvmsapi_20170525_models.CreateRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.CreateRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_robot_task_with_options_async(request, runtime)

    def create_sip_account_with_options(
        self,
        request: dyvmsapi_20170525_models.CreateSipAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CreateSipAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CreateSipAccountResponse(),
            self.do_rpcrequest('CreateSipAccount', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_sip_account_with_options_async(
        self,
        request: dyvmsapi_20170525_models.CreateSipAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.CreateSipAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.CreateSipAccountResponse(),
            await self.do_rpcrequest_async('CreateSipAccount', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_sip_account(
        self,
        request: dyvmsapi_20170525_models.CreateSipAccountRequest,
    ) -> dyvmsapi_20170525_models.CreateSipAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sip_account_with_options(request, runtime)

    async def create_sip_account_async(
        self,
        request: dyvmsapi_20170525_models.CreateSipAccountRequest,
    ) -> dyvmsapi_20170525_models.CreateSipAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sip_account_with_options_async(request, runtime)

    def delete_robot_task_with_options(
        self,
        request: dyvmsapi_20170525_models.DeleteRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.DeleteRobotTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.DeleteRobotTaskResponse(),
            self.do_rpcrequest('DeleteRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_robot_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.DeleteRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.DeleteRobotTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.DeleteRobotTaskResponse(),
            await self.do_rpcrequest_async('DeleteRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_robot_task(
        self,
        request: dyvmsapi_20170525_models.DeleteRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.DeleteRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_robot_task_with_options(request, runtime)

    async def delete_robot_task_async(
        self,
        request: dyvmsapi_20170525_models.DeleteRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.DeleteRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_robot_task_with_options_async(request, runtime)

    def describe_record_data_with_options(
        self,
        request: dyvmsapi_20170525_models.DescribeRecordDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.DescribeRecordDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.DescribeRecordDataResponse(),
            self.do_rpcrequest('DescribeRecordData', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_record_data_with_options_async(
        self,
        request: dyvmsapi_20170525_models.DescribeRecordDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.DescribeRecordDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.DescribeRecordDataResponse(),
            await self.do_rpcrequest_async('DescribeRecordData', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_record_data(
        self,
        request: dyvmsapi_20170525_models.DescribeRecordDataRequest,
    ) -> dyvmsapi_20170525_models.DescribeRecordDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_record_data_with_options(request, runtime)

    async def describe_record_data_async(
        self,
        request: dyvmsapi_20170525_models.DescribeRecordDataRequest,
    ) -> dyvmsapi_20170525_models.DescribeRecordDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_record_data_with_options_async(request, runtime)

    def do_rtc_number_auth_with_options(
        self,
        request: dyvmsapi_20170525_models.DoRtcNumberAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.DoRtcNumberAuthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.DoRtcNumberAuthResponse(),
            self.do_rpcrequest('DoRtcNumberAuth', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def do_rtc_number_auth_with_options_async(
        self,
        request: dyvmsapi_20170525_models.DoRtcNumberAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.DoRtcNumberAuthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.DoRtcNumberAuthResponse(),
            await self.do_rpcrequest_async('DoRtcNumberAuth', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def do_rtc_number_auth(
        self,
        request: dyvmsapi_20170525_models.DoRtcNumberAuthRequest,
    ) -> dyvmsapi_20170525_models.DoRtcNumberAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.do_rtc_number_auth_with_options(request, runtime)

    async def do_rtc_number_auth_async(
        self,
        request: dyvmsapi_20170525_models.DoRtcNumberAuthRequest,
    ) -> dyvmsapi_20170525_models.DoRtcNumberAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.do_rtc_number_auth_with_options_async(request, runtime)

    def double_call_seat_with_options(
        self,
        request: dyvmsapi_20170525_models.DoubleCallSeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.DoubleCallSeatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.DoubleCallSeatResponse(),
            self.do_rpcrequest('DoubleCallSeat', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def double_call_seat_with_options_async(
        self,
        request: dyvmsapi_20170525_models.DoubleCallSeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.DoubleCallSeatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.DoubleCallSeatResponse(),
            await self.do_rpcrequest_async('DoubleCallSeat', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def double_call_seat(
        self,
        request: dyvmsapi_20170525_models.DoubleCallSeatRequest,
    ) -> dyvmsapi_20170525_models.DoubleCallSeatResponse:
        runtime = util_models.RuntimeOptions()
        return self.double_call_seat_with_options(request, runtime)

    async def double_call_seat_async(
        self,
        request: dyvmsapi_20170525_models.DoubleCallSeatRequest,
    ) -> dyvmsapi_20170525_models.DoubleCallSeatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.double_call_seat_with_options_async(request, runtime)

    def execute_call_task_with_options(
        self,
        request: dyvmsapi_20170525_models.ExecuteCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ExecuteCallTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ExecuteCallTaskResponse(),
            self.do_rpcrequest('ExecuteCallTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def execute_call_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.ExecuteCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ExecuteCallTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ExecuteCallTaskResponse(),
            await self.do_rpcrequest_async('ExecuteCallTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_call_task(
        self,
        request: dyvmsapi_20170525_models.ExecuteCallTaskRequest,
    ) -> dyvmsapi_20170525_models.ExecuteCallTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_call_task_with_options(request, runtime)

    async def execute_call_task_async(
        self,
        request: dyvmsapi_20170525_models.ExecuteCallTaskRequest,
    ) -> dyvmsapi_20170525_models.ExecuteCallTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_call_task_with_options_async(request, runtime)

    def get_rtc_token_with_options(
        self,
        request: dyvmsapi_20170525_models.GetRtcTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.GetRtcTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetRtcTokenResponse(),
            self.do_rpcrequest('GetRtcToken', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_rtc_token_with_options_async(
        self,
        request: dyvmsapi_20170525_models.GetRtcTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.GetRtcTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetRtcTokenResponse(),
            await self.do_rpcrequest_async('GetRtcToken', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_rtc_token(
        self,
        request: dyvmsapi_20170525_models.GetRtcTokenRequest,
    ) -> dyvmsapi_20170525_models.GetRtcTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_rtc_token_with_options(request, runtime)

    async def get_rtc_token_async(
        self,
        request: dyvmsapi_20170525_models.GetRtcTokenRequest,
    ) -> dyvmsapi_20170525_models.GetRtcTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rtc_token_with_options_async(request, runtime)

    def get_token_with_options(
        self,
        request: dyvmsapi_20170525_models.GetTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.GetTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetTokenResponse(),
            self.do_rpcrequest('GetToken', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: dyvmsapi_20170525_models.GetTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.GetTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.GetTokenResponse(),
            await self.do_rpcrequest_async('GetToken', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_token(
        self,
        request: dyvmsapi_20170525_models.GetTokenRequest,
    ) -> dyvmsapi_20170525_models.GetTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_token_with_options(request, runtime)

    async def get_token_async(
        self,
        request: dyvmsapi_20170525_models.GetTokenRequest,
    ) -> dyvmsapi_20170525_models.GetTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_token_with_options_async(request, runtime)

    def ivr_call_with_options(
        self,
        request: dyvmsapi_20170525_models.IvrCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.IvrCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.IvrCallResponse(),
            self.do_rpcrequest('IvrCall', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def ivr_call_with_options_async(
        self,
        request: dyvmsapi_20170525_models.IvrCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.IvrCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.IvrCallResponse(),
            await self.do_rpcrequest_async('IvrCall', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def ivr_call(
        self,
        request: dyvmsapi_20170525_models.IvrCallRequest,
    ) -> dyvmsapi_20170525_models.IvrCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.ivr_call_with_options(request, runtime)

    async def ivr_call_async(
        self,
        request: dyvmsapi_20170525_models.IvrCallRequest,
    ) -> dyvmsapi_20170525_models.IvrCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.ivr_call_with_options_async(request, runtime)

    def list_call_task_with_options(
        self,
        request: dyvmsapi_20170525_models.ListCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListCallTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListCallTaskResponse(),
            self.do_rpcrequest('ListCallTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_call_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.ListCallTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListCallTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListCallTaskResponse(),
            await self.do_rpcrequest_async('ListCallTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_call_task(
        self,
        request: dyvmsapi_20170525_models.ListCallTaskRequest,
    ) -> dyvmsapi_20170525_models.ListCallTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_call_task_with_options(request, runtime)

    async def list_call_task_async(
        self,
        request: dyvmsapi_20170525_models.ListCallTaskRequest,
    ) -> dyvmsapi_20170525_models.ListCallTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_call_task_with_options_async(request, runtime)

    def list_call_task_detail_with_options(
        self,
        request: dyvmsapi_20170525_models.ListCallTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListCallTaskDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListCallTaskDetailResponse(),
            self.do_rpcrequest('ListCallTaskDetail', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_call_task_detail_with_options_async(
        self,
        request: dyvmsapi_20170525_models.ListCallTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListCallTaskDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListCallTaskDetailResponse(),
            await self.do_rpcrequest_async('ListCallTaskDetail', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_call_task_detail(
        self,
        request: dyvmsapi_20170525_models.ListCallTaskDetailRequest,
    ) -> dyvmsapi_20170525_models.ListCallTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_call_task_detail_with_options(request, runtime)

    async def list_call_task_detail_async(
        self,
        request: dyvmsapi_20170525_models.ListCallTaskDetailRequest,
    ) -> dyvmsapi_20170525_models.ListCallTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_call_task_detail_with_options_async(request, runtime)

    def list_ordered_numbers_with_options(
        self,
        request: dyvmsapi_20170525_models.ListOrderedNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListOrderedNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListOrderedNumbersResponse(),
            self.do_rpcrequest('ListOrderedNumbers', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_ordered_numbers_with_options_async(
        self,
        request: dyvmsapi_20170525_models.ListOrderedNumbersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListOrderedNumbersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListOrderedNumbersResponse(),
            await self.do_rpcrequest_async('ListOrderedNumbers', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ordered_numbers(
        self,
        request: dyvmsapi_20170525_models.ListOrderedNumbersRequest,
    ) -> dyvmsapi_20170525_models.ListOrderedNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ordered_numbers_with_options(request, runtime)

    async def list_ordered_numbers_async(
        self,
        request: dyvmsapi_20170525_models.ListOrderedNumbersRequest,
    ) -> dyvmsapi_20170525_models.ListOrderedNumbersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ordered_numbers_with_options_async(request, runtime)

    def list_outbound_strategies_with_options(
        self,
        request: dyvmsapi_20170525_models.ListOutboundStrategiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListOutboundStrategiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListOutboundStrategiesResponse(),
            self.do_rpcrequest('ListOutboundStrategies', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_outbound_strategies_with_options_async(
        self,
        request: dyvmsapi_20170525_models.ListOutboundStrategiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListOutboundStrategiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListOutboundStrategiesResponse(),
            await self.do_rpcrequest_async('ListOutboundStrategies', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_outbound_strategies(
        self,
        request: dyvmsapi_20170525_models.ListOutboundStrategiesRequest,
    ) -> dyvmsapi_20170525_models.ListOutboundStrategiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_outbound_strategies_with_options(request, runtime)

    async def list_outbound_strategies_async(
        self,
        request: dyvmsapi_20170525_models.ListOutboundStrategiesRequest,
    ) -> dyvmsapi_20170525_models.ListOutboundStrategiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_outbound_strategies_with_options_async(request, runtime)

    def list_robot_task_calls_with_options(
        self,
        request: dyvmsapi_20170525_models.ListRobotTaskCallsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListRobotTaskCallsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListRobotTaskCallsResponse(),
            self.do_rpcrequest('ListRobotTaskCalls', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_robot_task_calls_with_options_async(
        self,
        request: dyvmsapi_20170525_models.ListRobotTaskCallsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ListRobotTaskCallsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ListRobotTaskCallsResponse(),
            await self.do_rpcrequest_async('ListRobotTaskCalls', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_robot_task_calls(
        self,
        request: dyvmsapi_20170525_models.ListRobotTaskCallsRequest,
    ) -> dyvmsapi_20170525_models.ListRobotTaskCallsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_robot_task_calls_with_options(request, runtime)

    async def list_robot_task_calls_async(
        self,
        request: dyvmsapi_20170525_models.ListRobotTaskCallsRequest,
    ) -> dyvmsapi_20170525_models.ListRobotTaskCallsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_robot_task_calls_with_options_async(request, runtime)

    def query_call_detail_by_call_id_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryCallDetailByCallIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryCallDetailByCallIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallDetailByCallIdResponse(),
            self.do_rpcrequest('QueryCallDetailByCallId', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_call_detail_by_call_id_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryCallDetailByCallIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryCallDetailByCallIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallDetailByCallIdResponse(),
            await self.do_rpcrequest_async('QueryCallDetailByCallId', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_call_detail_by_call_id(
        self,
        request: dyvmsapi_20170525_models.QueryCallDetailByCallIdRequest,
    ) -> dyvmsapi_20170525_models.QueryCallDetailByCallIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_call_detail_by_call_id_with_options(request, runtime)

    async def query_call_detail_by_call_id_async(
        self,
        request: dyvmsapi_20170525_models.QueryCallDetailByCallIdRequest,
    ) -> dyvmsapi_20170525_models.QueryCallDetailByCallIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_call_detail_by_call_id_with_options_async(request, runtime)

    def query_call_detail_by_task_id_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryCallDetailByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryCallDetailByTaskIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallDetailByTaskIdResponse(),
            self.do_rpcrequest('QueryCallDetailByTaskId', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_call_detail_by_task_id_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryCallDetailByTaskIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryCallDetailByTaskIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryCallDetailByTaskIdResponse(),
            await self.do_rpcrequest_async('QueryCallDetailByTaskId', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_call_detail_by_task_id(
        self,
        request: dyvmsapi_20170525_models.QueryCallDetailByTaskIdRequest,
    ) -> dyvmsapi_20170525_models.QueryCallDetailByTaskIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_call_detail_by_task_id_with_options(request, runtime)

    async def query_call_detail_by_task_id_async(
        self,
        request: dyvmsapi_20170525_models.QueryCallDetailByTaskIdRequest,
    ) -> dyvmsapi_20170525_models.QueryCallDetailByTaskIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_call_detail_by_task_id_with_options_async(request, runtime)

    def query_robot_info_list_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryRobotInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotInfoListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotInfoListResponse(),
            self.do_rpcrequest('QueryRobotInfoList', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_robot_info_list_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotInfoListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotInfoListResponse(),
            await self.do_rpcrequest_async('QueryRobotInfoList', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_robot_info_list(
        self,
        request: dyvmsapi_20170525_models.QueryRobotInfoListRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_robot_info_list_with_options(request, runtime)

    async def query_robot_info_list_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotInfoListRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_robot_info_list_with_options_async(request, runtime)

    def query_robot_task_call_detail_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskCallDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskCallDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskCallDetailResponse(),
            self.do_rpcrequest('QueryRobotTaskCallDetail', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_robot_task_call_detail_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskCallDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskCallDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskCallDetailResponse(),
            await self.do_rpcrequest_async('QueryRobotTaskCallDetail', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_robot_task_call_detail(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskCallDetailRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskCallDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_robot_task_call_detail_with_options(request, runtime)

    async def query_robot_task_call_detail_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskCallDetailRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskCallDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_robot_task_call_detail_with_options_async(request, runtime)

    def query_robot_task_call_list_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskCallListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskCallListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskCallListResponse(),
            self.do_rpcrequest('QueryRobotTaskCallList', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_robot_task_call_list_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskCallListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskCallListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskCallListResponse(),
            await self.do_rpcrequest_async('QueryRobotTaskCallList', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_robot_task_call_list(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskCallListRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskCallListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_robot_task_call_list_with_options(request, runtime)

    async def query_robot_task_call_list_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskCallListRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskCallListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_robot_task_call_list_with_options_async(request, runtime)

    def query_robot_task_detail_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskDetailResponse(),
            self.do_rpcrequest('QueryRobotTaskDetail', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_robot_task_detail_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskDetailResponse(),
            await self.do_rpcrequest_async('QueryRobotTaskDetail', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_robot_task_detail(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskDetailRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_robot_task_detail_with_options(request, runtime)

    async def query_robot_task_detail_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskDetailRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_robot_task_detail_with_options_async(request, runtime)

    def query_robot_task_list_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskListResponse(),
            self.do_rpcrequest('QueryRobotTaskList', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_robot_task_list_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotTaskListResponse(),
            await self.do_rpcrequest_async('QueryRobotTaskList', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_robot_task_list(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskListRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_robot_task_list_with_options(request, runtime)

    async def query_robot_task_list_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotTaskListRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_robot_task_list_with_options_async(request, runtime)

    def query_robotv_2all_list_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryRobotv2AllListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotv2AllListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotv2AllListResponse(),
            self.do_rpcrequest('QueryRobotv2AllList', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_robotv_2all_list_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotv2AllListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRobotv2AllListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRobotv2AllListResponse(),
            await self.do_rpcrequest_async('QueryRobotv2AllList', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_robotv_2all_list(
        self,
        request: dyvmsapi_20170525_models.QueryRobotv2AllListRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotv2AllListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_robotv_2all_list_with_options(request, runtime)

    async def query_robotv_2all_list_async(
        self,
        request: dyvmsapi_20170525_models.QueryRobotv2AllListRequest,
    ) -> dyvmsapi_20170525_models.QueryRobotv2AllListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_robotv_2all_list_with_options_async(request, runtime)

    def query_rtc_number_auth_status_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryRtcNumberAuthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRtcNumberAuthStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRtcNumberAuthStatusResponse(),
            self.do_rpcrequest('QueryRtcNumberAuthStatus', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_rtc_number_auth_status_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryRtcNumberAuthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryRtcNumberAuthStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryRtcNumberAuthStatusResponse(),
            await self.do_rpcrequest_async('QueryRtcNumberAuthStatus', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_rtc_number_auth_status(
        self,
        request: dyvmsapi_20170525_models.QueryRtcNumberAuthStatusRequest,
    ) -> dyvmsapi_20170525_models.QueryRtcNumberAuthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_rtc_number_auth_status_with_options(request, runtime)

    async def query_rtc_number_auth_status_async(
        self,
        request: dyvmsapi_20170525_models.QueryRtcNumberAuthStatusRequest,
    ) -> dyvmsapi_20170525_models.QueryRtcNumberAuthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_rtc_number_auth_status_with_options_async(request, runtime)

    def query_virtual_number_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryVirtualNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryVirtualNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryVirtualNumberResponse(),
            self.do_rpcrequest('QueryVirtualNumber', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_virtual_number_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryVirtualNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryVirtualNumberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryVirtualNumberResponse(),
            await self.do_rpcrequest_async('QueryVirtualNumber', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_virtual_number(
        self,
        request: dyvmsapi_20170525_models.QueryVirtualNumberRequest,
    ) -> dyvmsapi_20170525_models.QueryVirtualNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_virtual_number_with_options(request, runtime)

    async def query_virtual_number_async(
        self,
        request: dyvmsapi_20170525_models.QueryVirtualNumberRequest,
    ) -> dyvmsapi_20170525_models.QueryVirtualNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_virtual_number_with_options_async(request, runtime)

    def query_virtual_number_relation_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryVirtualNumberRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryVirtualNumberRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryVirtualNumberRelationResponse(),
            self.do_rpcrequest('QueryVirtualNumberRelation', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_virtual_number_relation_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryVirtualNumberRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryVirtualNumberRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryVirtualNumberRelationResponse(),
            await self.do_rpcrequest_async('QueryVirtualNumberRelation', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_virtual_number_relation(
        self,
        request: dyvmsapi_20170525_models.QueryVirtualNumberRelationRequest,
    ) -> dyvmsapi_20170525_models.QueryVirtualNumberRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_virtual_number_relation_with_options(request, runtime)

    async def query_virtual_number_relation_async(
        self,
        request: dyvmsapi_20170525_models.QueryVirtualNumberRelationRequest,
    ) -> dyvmsapi_20170525_models.QueryVirtualNumberRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_virtual_number_relation_with_options_async(request, runtime)

    def query_voip_number_bind_infos_with_options(
        self,
        request: dyvmsapi_20170525_models.QueryVoipNumberBindInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryVoipNumberBindInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryVoipNumberBindInfosResponse(),
            self.do_rpcrequest('QueryVoipNumberBindInfos', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_voip_number_bind_infos_with_options_async(
        self,
        request: dyvmsapi_20170525_models.QueryVoipNumberBindInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.QueryVoipNumberBindInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.QueryVoipNumberBindInfosResponse(),
            await self.do_rpcrequest_async('QueryVoipNumberBindInfos', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_voip_number_bind_infos(
        self,
        request: dyvmsapi_20170525_models.QueryVoipNumberBindInfosRequest,
    ) -> dyvmsapi_20170525_models.QueryVoipNumberBindInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_voip_number_bind_infos_with_options(request, runtime)

    async def query_voip_number_bind_infos_async(
        self,
        request: dyvmsapi_20170525_models.QueryVoipNumberBindInfosRequest,
    ) -> dyvmsapi_20170525_models.QueryVoipNumberBindInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_voip_number_bind_infos_with_options_async(request, runtime)

    def report_voip_problems_with_options(
        self,
        request: dyvmsapi_20170525_models.ReportVoipProblemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ReportVoipProblemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ReportVoipProblemsResponse(),
            self.do_rpcrequest('ReportVoipProblems', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def report_voip_problems_with_options_async(
        self,
        request: dyvmsapi_20170525_models.ReportVoipProblemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.ReportVoipProblemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.ReportVoipProblemsResponse(),
            await self.do_rpcrequest_async('ReportVoipProblems', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_voip_problems(
        self,
        request: dyvmsapi_20170525_models.ReportVoipProblemsRequest,
    ) -> dyvmsapi_20170525_models.ReportVoipProblemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_voip_problems_with_options(request, runtime)

    async def report_voip_problems_async(
        self,
        request: dyvmsapi_20170525_models.ReportVoipProblemsRequest,
    ) -> dyvmsapi_20170525_models.ReportVoipProblemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_voip_problems_with_options_async(request, runtime)

    def single_call_by_tts_with_options(
        self,
        request: dyvmsapi_20170525_models.SingleCallByTtsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SingleCallByTtsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SingleCallByTtsResponse(),
            self.do_rpcrequest('SingleCallByTts', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def single_call_by_tts_with_options_async(
        self,
        request: dyvmsapi_20170525_models.SingleCallByTtsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SingleCallByTtsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SingleCallByTtsResponse(),
            await self.do_rpcrequest_async('SingleCallByTts', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def single_call_by_tts(
        self,
        request: dyvmsapi_20170525_models.SingleCallByTtsRequest,
    ) -> dyvmsapi_20170525_models.SingleCallByTtsResponse:
        runtime = util_models.RuntimeOptions()
        return self.single_call_by_tts_with_options(request, runtime)

    async def single_call_by_tts_async(
        self,
        request: dyvmsapi_20170525_models.SingleCallByTtsRequest,
    ) -> dyvmsapi_20170525_models.SingleCallByTtsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.single_call_by_tts_with_options_async(request, runtime)

    def single_call_by_voice_with_options(
        self,
        request: dyvmsapi_20170525_models.SingleCallByVoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SingleCallByVoiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SingleCallByVoiceResponse(),
            self.do_rpcrequest('SingleCallByVoice', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def single_call_by_voice_with_options_async(
        self,
        request: dyvmsapi_20170525_models.SingleCallByVoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SingleCallByVoiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SingleCallByVoiceResponse(),
            await self.do_rpcrequest_async('SingleCallByVoice', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def single_call_by_voice(
        self,
        request: dyvmsapi_20170525_models.SingleCallByVoiceRequest,
    ) -> dyvmsapi_20170525_models.SingleCallByVoiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.single_call_by_voice_with_options(request, runtime)

    async def single_call_by_voice_async(
        self,
        request: dyvmsapi_20170525_models.SingleCallByVoiceRequest,
    ) -> dyvmsapi_20170525_models.SingleCallByVoiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.single_call_by_voice_with_options_async(request, runtime)

    def smart_call_with_options(
        self,
        request: dyvmsapi_20170525_models.SmartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SmartCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SmartCallResponse(),
            self.do_rpcrequest('SmartCall', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def smart_call_with_options_async(
        self,
        request: dyvmsapi_20170525_models.SmartCallRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SmartCallResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SmartCallResponse(),
            await self.do_rpcrequest_async('SmartCall', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def smart_call(
        self,
        request: dyvmsapi_20170525_models.SmartCallRequest,
    ) -> dyvmsapi_20170525_models.SmartCallResponse:
        runtime = util_models.RuntimeOptions()
        return self.smart_call_with_options(request, runtime)

    async def smart_call_async(
        self,
        request: dyvmsapi_20170525_models.SmartCallRequest,
    ) -> dyvmsapi_20170525_models.SmartCallResponse:
        runtime = util_models.RuntimeOptions()
        return await self.smart_call_with_options_async(request, runtime)

    def smart_call_operate_with_options(
        self,
        request: dyvmsapi_20170525_models.SmartCallOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SmartCallOperateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SmartCallOperateResponse(),
            self.do_rpcrequest('SmartCallOperate', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def smart_call_operate_with_options_async(
        self,
        request: dyvmsapi_20170525_models.SmartCallOperateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.SmartCallOperateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.SmartCallOperateResponse(),
            await self.do_rpcrequest_async('SmartCallOperate', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def smart_call_operate(
        self,
        request: dyvmsapi_20170525_models.SmartCallOperateRequest,
    ) -> dyvmsapi_20170525_models.SmartCallOperateResponse:
        runtime = util_models.RuntimeOptions()
        return self.smart_call_operate_with_options(request, runtime)

    async def smart_call_operate_async(
        self,
        request: dyvmsapi_20170525_models.SmartCallOperateRequest,
    ) -> dyvmsapi_20170525_models.SmartCallOperateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.smart_call_operate_with_options_async(request, runtime)

    def start_micro_outbound_with_options(
        self,
        request: dyvmsapi_20170525_models.StartMicroOutboundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.StartMicroOutboundResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.StartMicroOutboundResponse(),
            self.do_rpcrequest('StartMicroOutbound', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_micro_outbound_with_options_async(
        self,
        request: dyvmsapi_20170525_models.StartMicroOutboundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.StartMicroOutboundResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.StartMicroOutboundResponse(),
            await self.do_rpcrequest_async('StartMicroOutbound', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_micro_outbound(
        self,
        request: dyvmsapi_20170525_models.StartMicroOutboundRequest,
    ) -> dyvmsapi_20170525_models.StartMicroOutboundResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_micro_outbound_with_options(request, runtime)

    async def start_micro_outbound_async(
        self,
        request: dyvmsapi_20170525_models.StartMicroOutboundRequest,
    ) -> dyvmsapi_20170525_models.StartMicroOutboundResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_micro_outbound_with_options_async(request, runtime)

    def start_robot_task_with_options(
        self,
        request: dyvmsapi_20170525_models.StartRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.StartRobotTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.StartRobotTaskResponse(),
            self.do_rpcrequest('StartRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_robot_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.StartRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.StartRobotTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.StartRobotTaskResponse(),
            await self.do_rpcrequest_async('StartRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_robot_task(
        self,
        request: dyvmsapi_20170525_models.StartRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.StartRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_robot_task_with_options(request, runtime)

    async def start_robot_task_async(
        self,
        request: dyvmsapi_20170525_models.StartRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.StartRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_robot_task_with_options_async(request, runtime)

    def stop_robot_task_with_options(
        self,
        request: dyvmsapi_20170525_models.StopRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.StopRobotTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.StopRobotTaskResponse(),
            self.do_rpcrequest('StopRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_robot_task_with_options_async(
        self,
        request: dyvmsapi_20170525_models.StopRobotTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.StopRobotTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.StopRobotTaskResponse(),
            await self.do_rpcrequest_async('StopRobotTask', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_robot_task(
        self,
        request: dyvmsapi_20170525_models.StopRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.StopRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_robot_task_with_options(request, runtime)

    async def stop_robot_task_async(
        self,
        request: dyvmsapi_20170525_models.StopRobotTaskRequest,
    ) -> dyvmsapi_20170525_models.StopRobotTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_robot_task_with_options_async(request, runtime)

    def unbind_number_and_voip_id_with_options(
        self,
        request: dyvmsapi_20170525_models.UnbindNumberAndVoipIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.UnbindNumberAndVoipIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.UnbindNumberAndVoipIdResponse(),
            self.do_rpcrequest('UnbindNumberAndVoipId', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unbind_number_and_voip_id_with_options_async(
        self,
        request: dyvmsapi_20170525_models.UnbindNumberAndVoipIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.UnbindNumberAndVoipIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.UnbindNumberAndVoipIdResponse(),
            await self.do_rpcrequest_async('UnbindNumberAndVoipId', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_number_and_voip_id(
        self,
        request: dyvmsapi_20170525_models.UnbindNumberAndVoipIdRequest,
    ) -> dyvmsapi_20170525_models.UnbindNumberAndVoipIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_number_and_voip_id_with_options(request, runtime)

    async def unbind_number_and_voip_id_async(
        self,
        request: dyvmsapi_20170525_models.UnbindNumberAndVoipIdRequest,
    ) -> dyvmsapi_20170525_models.UnbindNumberAndVoipIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_number_and_voip_id_with_options_async(request, runtime)

    def undo_rtc_number_auth_with_options(
        self,
        request: dyvmsapi_20170525_models.UndoRtcNumberAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.UndoRtcNumberAuthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.UndoRtcNumberAuthResponse(),
            self.do_rpcrequest('UndoRtcNumberAuth', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def undo_rtc_number_auth_with_options_async(
        self,
        request: dyvmsapi_20170525_models.UndoRtcNumberAuthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.UndoRtcNumberAuthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.UndoRtcNumberAuthResponse(),
            await self.do_rpcrequest_async('UndoRtcNumberAuth', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def undo_rtc_number_auth(
        self,
        request: dyvmsapi_20170525_models.UndoRtcNumberAuthRequest,
    ) -> dyvmsapi_20170525_models.UndoRtcNumberAuthResponse:
        runtime = util_models.RuntimeOptions()
        return self.undo_rtc_number_auth_with_options(request, runtime)

    async def undo_rtc_number_auth_async(
        self,
        request: dyvmsapi_20170525_models.UndoRtcNumberAuthRequest,
    ) -> dyvmsapi_20170525_models.UndoRtcNumberAuthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.undo_rtc_number_auth_with_options_async(request, runtime)

    def upload_robot_task_called_file_with_options(
        self,
        request: dyvmsapi_20170525_models.UploadRobotTaskCalledFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.UploadRobotTaskCalledFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.UploadRobotTaskCalledFileResponse(),
            self.do_rpcrequest('UploadRobotTaskCalledFile', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_robot_task_called_file_with_options_async(
        self,
        request: dyvmsapi_20170525_models.UploadRobotTaskCalledFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.UploadRobotTaskCalledFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.UploadRobotTaskCalledFileResponse(),
            await self.do_rpcrequest_async('UploadRobotTaskCalledFile', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_robot_task_called_file(
        self,
        request: dyvmsapi_20170525_models.UploadRobotTaskCalledFileRequest,
    ) -> dyvmsapi_20170525_models.UploadRobotTaskCalledFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_robot_task_called_file_with_options(request, runtime)

    async def upload_robot_task_called_file_async(
        self,
        request: dyvmsapi_20170525_models.UploadRobotTaskCalledFileRequest,
    ) -> dyvmsapi_20170525_models.UploadRobotTaskCalledFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_robot_task_called_file_with_options_async(request, runtime)

    def voip_add_account_with_options(
        self,
        request: dyvmsapi_20170525_models.VoipAddAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.VoipAddAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.VoipAddAccountResponse(),
            self.do_rpcrequest('VoipAddAccount', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def voip_add_account_with_options_async(
        self,
        request: dyvmsapi_20170525_models.VoipAddAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.VoipAddAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.VoipAddAccountResponse(),
            await self.do_rpcrequest_async('VoipAddAccount', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def voip_add_account(
        self,
        request: dyvmsapi_20170525_models.VoipAddAccountRequest,
    ) -> dyvmsapi_20170525_models.VoipAddAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.voip_add_account_with_options(request, runtime)

    async def voip_add_account_async(
        self,
        request: dyvmsapi_20170525_models.VoipAddAccountRequest,
    ) -> dyvmsapi_20170525_models.VoipAddAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.voip_add_account_with_options_async(request, runtime)

    def voip_get_token_with_options(
        self,
        request: dyvmsapi_20170525_models.VoipGetTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.VoipGetTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.VoipGetTokenResponse(),
            self.do_rpcrequest('VoipGetToken', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def voip_get_token_with_options_async(
        self,
        request: dyvmsapi_20170525_models.VoipGetTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dyvmsapi_20170525_models.VoipGetTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dyvmsapi_20170525_models.VoipGetTokenResponse(),
            await self.do_rpcrequest_async('VoipGetToken', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def voip_get_token(
        self,
        request: dyvmsapi_20170525_models.VoipGetTokenRequest,
    ) -> dyvmsapi_20170525_models.VoipGetTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.voip_get_token_with_options(request, runtime)

    async def voip_get_token_async(
        self,
        request: dyvmsapi_20170525_models.VoipGetTokenRequest,
    ) -> dyvmsapi_20170525_models.VoipGetTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.voip_get_token_with_options_async(request, runtime)
