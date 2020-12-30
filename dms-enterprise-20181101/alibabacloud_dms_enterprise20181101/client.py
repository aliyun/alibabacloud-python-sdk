# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dms_enterprise20181101 import models as dms_enterprise_20181101_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('dms-enterprise', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def approve_order_with_options(
        self,
        request: dms_enterprise_20181101_models.ApproveOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ApproveOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ApproveOrderResponse().from_map(
            self.do_rpcrequest('ApproveOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def approve_order_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ApproveOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ApproveOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ApproveOrderResponse().from_map(
            await self.do_rpcrequest_async('ApproveOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def approve_order(
        self,
        request: dms_enterprise_20181101_models.ApproveOrderRequest,
    ) -> dms_enterprise_20181101_models.ApproveOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.approve_order_with_options(request, runtime)

    async def approve_order_async(
        self,
        request: dms_enterprise_20181101_models.ApproveOrderRequest,
    ) -> dms_enterprise_20181101_models.ApproveOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.approve_order_with_options_async(request, runtime)

    def check_finish_mission_with_options(
        self,
        request: dms_enterprise_20181101_models.CheckFinishMissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CheckFinishMissionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return dms_enterprise_20181101_models.CheckFinishMissionResponse().from_map(
            self.do_rpcrequest('CheckFinishMission', '2018-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def check_finish_mission_with_options_async(
        self,
        request: dms_enterprise_20181101_models.CheckFinishMissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CheckFinishMissionResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return dms_enterprise_20181101_models.CheckFinishMissionResponse().from_map(
            await self.do_rpcrequest_async('CheckFinishMission', '2018-11-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def check_finish_mission(
        self,
        request: dms_enterprise_20181101_models.CheckFinishMissionRequest,
    ) -> dms_enterprise_20181101_models.CheckFinishMissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_finish_mission_with_options(request, runtime)

    async def check_finish_mission_async(
        self,
        request: dms_enterprise_20181101_models.CheckFinishMissionRequest,
    ) -> dms_enterprise_20181101_models.CheckFinishMissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_finish_mission_with_options_async(request, runtime)

    def close_order_with_options(
        self,
        request: dms_enterprise_20181101_models.CloseOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CloseOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.CloseOrderResponse().from_map(
            self.do_rpcrequest('CloseOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def close_order_with_options_async(
        self,
        request: dms_enterprise_20181101_models.CloseOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CloseOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.CloseOrderResponse().from_map(
            await self.do_rpcrequest_async('CloseOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def close_order(
        self,
        request: dms_enterprise_20181101_models.CloseOrderRequest,
    ) -> dms_enterprise_20181101_models.CloseOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_order_with_options(request, runtime)

    async def close_order_async(
        self,
        request: dms_enterprise_20181101_models.CloseOrderRequest,
    ) -> dms_enterprise_20181101_models.CloseOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_order_with_options_async(request, runtime)

    def create_order_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.plugin_param):
            request.plugin_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.plugin_param, 'PluginParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.CreateOrderResponse().from_map(
            self.do_rpcrequest('CreateOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_order_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.plugin_param):
            request.plugin_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.plugin_param, 'PluginParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.CreateOrderResponse().from_map(
            await self.do_rpcrequest_async('CreateOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_order(
        self,
        request: dms_enterprise_20181101_models.CreateOrderRequest,
    ) -> dms_enterprise_20181101_models.CreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    async def create_order_async(
        self,
        request: dms_enterprise_20181101_models.CreateOrderRequest,
    ) -> dms_enterprise_20181101_models.CreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_order_with_options_async(request, runtime)

    def create_publish_group_task_with_options(
        self,
        request: dms_enterprise_20181101_models.CreatePublishGroupTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreatePublishGroupTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.CreatePublishGroupTaskResponse().from_map(
            self.do_rpcrequest('CreatePublishGroupTask', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_publish_group_task_with_options_async(
        self,
        request: dms_enterprise_20181101_models.CreatePublishGroupTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreatePublishGroupTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.CreatePublishGroupTaskResponse().from_map(
            await self.do_rpcrequest_async('CreatePublishGroupTask', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_publish_group_task(
        self,
        request: dms_enterprise_20181101_models.CreatePublishGroupTaskRequest,
    ) -> dms_enterprise_20181101_models.CreatePublishGroupTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_publish_group_task_with_options(request, runtime)

    async def create_publish_group_task_async(
        self,
        request: dms_enterprise_20181101_models.CreatePublishGroupTaskRequest,
    ) -> dms_enterprise_20181101_models.CreatePublishGroupTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_publish_group_task_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: dms_enterprise_20181101_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.DeleteInstanceResponse().from_map(
            self.do_rpcrequest('DeleteInstance', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: dms_enterprise_20181101_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.DeleteInstanceResponse().from_map(
            await self.do_rpcrequest_async('DeleteInstance', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance(
        self,
        request: dms_enterprise_20181101_models.DeleteInstanceRequest,
    ) -> dms_enterprise_20181101_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: dms_enterprise_20181101_models.DeleteInstanceRequest,
    ) -> dms_enterprise_20181101_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: dms_enterprise_20181101_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.DeleteUserResponse().from_map(
            self.do_rpcrequest('DeleteUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: dms_enterprise_20181101_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.DeleteUserResponse().from_map(
            await self.do_rpcrequest_async('DeleteUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user(
        self,
        request: dms_enterprise_20181101_models.DeleteUserRequest,
    ) -> dms_enterprise_20181101_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: dms_enterprise_20181101_models.DeleteUserRequest,
    ) -> dms_enterprise_20181101_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def disable_user_with_options(
        self,
        request: dms_enterprise_20181101_models.DisableUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DisableUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.DisableUserResponse().from_map(
            self.do_rpcrequest('DisableUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_user_with_options_async(
        self,
        request: dms_enterprise_20181101_models.DisableUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DisableUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.DisableUserResponse().from_map(
            await self.do_rpcrequest_async('DisableUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_user(
        self,
        request: dms_enterprise_20181101_models.DisableUserRequest,
    ) -> dms_enterprise_20181101_models.DisableUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_user_with_options(request, runtime)

    async def disable_user_async(
        self,
        request: dms_enterprise_20181101_models.DisableUserRequest,
    ) -> dms_enterprise_20181101_models.DisableUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_user_with_options_async(request, runtime)

    def enable_user_with_options(
        self,
        request: dms_enterprise_20181101_models.EnableUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.EnableUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.EnableUserResponse().from_map(
            self.do_rpcrequest('EnableUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_user_with_options_async(
        self,
        request: dms_enterprise_20181101_models.EnableUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.EnableUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.EnableUserResponse().from_map(
            await self.do_rpcrequest_async('EnableUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_user(
        self,
        request: dms_enterprise_20181101_models.EnableUserRequest,
    ) -> dms_enterprise_20181101_models.EnableUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_user_with_options(request, runtime)

    async def enable_user_async(
        self,
        request: dms_enterprise_20181101_models.EnableUserRequest,
    ) -> dms_enterprise_20181101_models.EnableUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_user_with_options_async(request, runtime)

    def execute_data_correct_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.ExecuteDataCorrectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ExecuteDataCorrectResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.ExecuteDataCorrectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.action_detail):
            request.action_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.action_detail, 'ActionDetail', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ExecuteDataCorrectResponse().from_map(
            self.do_rpcrequest('ExecuteDataCorrect', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def execute_data_correct_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.ExecuteDataCorrectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ExecuteDataCorrectResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.ExecuteDataCorrectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.action_detail):
            request.action_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.action_detail, 'ActionDetail', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ExecuteDataCorrectResponse().from_map(
            await self.do_rpcrequest_async('ExecuteDataCorrect', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_data_correct(
        self,
        request: dms_enterprise_20181101_models.ExecuteDataCorrectRequest,
    ) -> dms_enterprise_20181101_models.ExecuteDataCorrectResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_data_correct_with_options(request, runtime)

    async def execute_data_correct_async(
        self,
        request: dms_enterprise_20181101_models.ExecuteDataCorrectRequest,
    ) -> dms_enterprise_20181101_models.ExecuteDataCorrectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_data_correct_with_options_async(request, runtime)

    def execute_data_export_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.ExecuteDataExportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ExecuteDataExportResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.ExecuteDataExportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.action_detail):
            request.action_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.action_detail, 'ActionDetail', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ExecuteDataExportResponse().from_map(
            self.do_rpcrequest('ExecuteDataExport', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def execute_data_export_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.ExecuteDataExportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ExecuteDataExportResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.ExecuteDataExportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.action_detail):
            request.action_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.action_detail, 'ActionDetail', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ExecuteDataExportResponse().from_map(
            await self.do_rpcrequest_async('ExecuteDataExport', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_data_export(
        self,
        request: dms_enterprise_20181101_models.ExecuteDataExportRequest,
    ) -> dms_enterprise_20181101_models.ExecuteDataExportResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_data_export_with_options(request, runtime)

    async def execute_data_export_async(
        self,
        request: dms_enterprise_20181101_models.ExecuteDataExportRequest,
    ) -> dms_enterprise_20181101_models.ExecuteDataExportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_data_export_with_options_async(request, runtime)

    def execute_script_with_options(
        self,
        request: dms_enterprise_20181101_models.ExecuteScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ExecuteScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ExecuteScriptResponse().from_map(
            self.do_rpcrequest('ExecuteScript', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def execute_script_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ExecuteScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ExecuteScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ExecuteScriptResponse().from_map(
            await self.do_rpcrequest_async('ExecuteScript', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_script(
        self,
        request: dms_enterprise_20181101_models.ExecuteScriptRequest,
    ) -> dms_enterprise_20181101_models.ExecuteScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_script_with_options(request, runtime)

    async def execute_script_async(
        self,
        request: dms_enterprise_20181101_models.ExecuteScriptRequest,
    ) -> dms_enterprise_20181101_models.ExecuteScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_script_with_options_async(request, runtime)

    def get_approval_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetApprovalDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetApprovalDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetApprovalDetailResponse().from_map(
            self.do_rpcrequest('GetApprovalDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_approval_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetApprovalDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetApprovalDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetApprovalDetailResponse().from_map(
            await self.do_rpcrequest_async('GetApprovalDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_approval_detail(
        self,
        request: dms_enterprise_20181101_models.GetApprovalDetailRequest,
    ) -> dms_enterprise_20181101_models.GetApprovalDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_approval_detail_with_options(request, runtime)

    async def get_approval_detail_async(
        self,
        request: dms_enterprise_20181101_models.GetApprovalDetailRequest,
    ) -> dms_enterprise_20181101_models.GetApprovalDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_approval_detail_with_options_async(request, runtime)

    def get_database_with_options(
        self,
        request: dms_enterprise_20181101_models.GetDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDatabaseResponse().from_map(
            self.do_rpcrequest('GetDatabase', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_database_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDatabaseResponse().from_map(
            await self.do_rpcrequest_async('GetDatabase', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_database(
        self,
        request: dms_enterprise_20181101_models.GetDatabaseRequest,
    ) -> dms_enterprise_20181101_models.GetDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_database_with_options(request, runtime)

    async def get_database_async(
        self,
        request: dms_enterprise_20181101_models.GetDatabaseRequest,
    ) -> dms_enterprise_20181101_models.GetDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_database_with_options_async(request, runtime)

    def get_data_correct_backup_files_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.GetDataCorrectBackupFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCorrectBackupFilesResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.GetDataCorrectBackupFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.action_detail):
            request.action_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.action_detail, 'ActionDetail', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDataCorrectBackupFilesResponse().from_map(
            self.do_rpcrequest('GetDataCorrectBackupFiles', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_data_correct_backup_files_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.GetDataCorrectBackupFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCorrectBackupFilesResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.GetDataCorrectBackupFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.action_detail):
            request.action_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.action_detail, 'ActionDetail', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDataCorrectBackupFilesResponse().from_map(
            await self.do_rpcrequest_async('GetDataCorrectBackupFiles', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_correct_backup_files(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectBackupFilesRequest,
    ) -> dms_enterprise_20181101_models.GetDataCorrectBackupFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_correct_backup_files_with_options(request, runtime)

    async def get_data_correct_backup_files_async(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectBackupFilesRequest,
    ) -> dms_enterprise_20181101_models.GetDataCorrectBackupFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_correct_backup_files_with_options_async(request, runtime)

    def get_data_correct_order_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCorrectOrderDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDataCorrectOrderDetailResponse().from_map(
            self.do_rpcrequest('GetDataCorrectOrderDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_data_correct_order_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCorrectOrderDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDataCorrectOrderDetailResponse().from_map(
            await self.do_rpcrequest_async('GetDataCorrectOrderDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_correct_order_detail(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectOrderDetailRequest,
    ) -> dms_enterprise_20181101_models.GetDataCorrectOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_correct_order_detail_with_options(request, runtime)

    async def get_data_correct_order_detail_async(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectOrderDetailRequest,
    ) -> dms_enterprise_20181101_models.GetDataCorrectOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_correct_order_detail_with_options_async(request, runtime)

    def get_data_export_download_urlwith_options(
        self,
        request: dms_enterprise_20181101_models.GetDataExportDownloadURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataExportDownloadURLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDataExportDownloadURLResponse().from_map(
            self.do_rpcrequest('GetDataExportDownloadURL', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_data_export_download_urlwith_options_async(
        self,
        request: dms_enterprise_20181101_models.GetDataExportDownloadURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataExportDownloadURLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDataExportDownloadURLResponse().from_map(
            await self.do_rpcrequest_async('GetDataExportDownloadURL', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_export_download_url(
        self,
        request: dms_enterprise_20181101_models.GetDataExportDownloadURLRequest,
    ) -> dms_enterprise_20181101_models.GetDataExportDownloadURLResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_export_download_urlwith_options(request, runtime)

    async def get_data_export_download_url_async(
        self,
        request: dms_enterprise_20181101_models.GetDataExportDownloadURLRequest,
    ) -> dms_enterprise_20181101_models.GetDataExportDownloadURLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_export_download_urlwith_options_async(request, runtime)

    def get_data_export_order_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetDataExportOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataExportOrderDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDataExportOrderDetailResponse().from_map(
            self.do_rpcrequest('GetDataExportOrderDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_data_export_order_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetDataExportOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataExportOrderDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetDataExportOrderDetailResponse().from_map(
            await self.do_rpcrequest_async('GetDataExportOrderDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_export_order_detail(
        self,
        request: dms_enterprise_20181101_models.GetDataExportOrderDetailRequest,
    ) -> dms_enterprise_20181101_models.GetDataExportOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_export_order_detail_with_options(request, runtime)

    async def get_data_export_order_detail_async(
        self,
        request: dms_enterprise_20181101_models.GetDataExportOrderDetailRequest,
    ) -> dms_enterprise_20181101_models.GetDataExportOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_export_order_detail_with_options_async(request, runtime)

    def get_instance_with_options(
        self,
        request: dms_enterprise_20181101_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetInstanceResponse().from_map(
            self.do_rpcrequest('GetInstance', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetInstanceResponse().from_map(
            await self.do_rpcrequest_async('GetInstance', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance(
        self,
        request: dms_enterprise_20181101_models.GetInstanceRequest,
    ) -> dms_enterprise_20181101_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    async def get_instance_async(
        self,
        request: dms_enterprise_20181101_models.GetInstanceRequest,
    ) -> dms_enterprise_20181101_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_with_options_async(request, runtime)

    def get_logic_database_with_options(
        self,
        request: dms_enterprise_20181101_models.GetLogicDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetLogicDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetLogicDatabaseResponse().from_map(
            self.do_rpcrequest('GetLogicDatabase', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_logic_database_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetLogicDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetLogicDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetLogicDatabaseResponse().from_map(
            await self.do_rpcrequest_async('GetLogicDatabase', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_logic_database(
        self,
        request: dms_enterprise_20181101_models.GetLogicDatabaseRequest,
    ) -> dms_enterprise_20181101_models.GetLogicDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_logic_database_with_options(request, runtime)

    async def get_logic_database_async(
        self,
        request: dms_enterprise_20181101_models.GetLogicDatabaseRequest,
    ) -> dms_enterprise_20181101_models.GetLogicDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_logic_database_with_options_async(request, runtime)

    def get_meta_table_column_with_options(
        self,
        request: dms_enterprise_20181101_models.GetMetaTableColumnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetMetaTableColumnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetMetaTableColumnResponse().from_map(
            self.do_rpcrequest('GetMetaTableColumn', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_meta_table_column_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetMetaTableColumnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetMetaTableColumnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetMetaTableColumnResponse().from_map(
            await self.do_rpcrequest_async('GetMetaTableColumn', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_table_column(
        self,
        request: dms_enterprise_20181101_models.GetMetaTableColumnRequest,
    ) -> dms_enterprise_20181101_models.GetMetaTableColumnResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_column_with_options(request, runtime)

    async def get_meta_table_column_async(
        self,
        request: dms_enterprise_20181101_models.GetMetaTableColumnRequest,
    ) -> dms_enterprise_20181101_models.GetMetaTableColumnResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_meta_table_column_with_options_async(request, runtime)

    def get_meta_table_detail_info_with_options(
        self,
        request: dms_enterprise_20181101_models.GetMetaTableDetailInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetMetaTableDetailInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetMetaTableDetailInfoResponse().from_map(
            self.do_rpcrequest('GetMetaTableDetailInfo', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_meta_table_detail_info_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetMetaTableDetailInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetMetaTableDetailInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetMetaTableDetailInfoResponse().from_map(
            await self.do_rpcrequest_async('GetMetaTableDetailInfo', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_table_detail_info(
        self,
        request: dms_enterprise_20181101_models.GetMetaTableDetailInfoRequest,
    ) -> dms_enterprise_20181101_models.GetMetaTableDetailInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_detail_info_with_options(request, runtime)

    async def get_meta_table_detail_info_async(
        self,
        request: dms_enterprise_20181101_models.GetMetaTableDetailInfoRequest,
    ) -> dms_enterprise_20181101_models.GetMetaTableDetailInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_meta_table_detail_info_with_options_async(request, runtime)

    def get_op_log_with_options(
        self,
        request: dms_enterprise_20181101_models.GetOpLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetOpLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetOpLogResponse().from_map(
            self.do_rpcrequest('GetOpLog', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_op_log_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetOpLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetOpLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetOpLogResponse().from_map(
            await self.do_rpcrequest_async('GetOpLog', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_op_log(
        self,
        request: dms_enterprise_20181101_models.GetOpLogRequest,
    ) -> dms_enterprise_20181101_models.GetOpLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_op_log_with_options(request, runtime)

    async def get_op_log_async(
        self,
        request: dms_enterprise_20181101_models.GetOpLogRequest,
    ) -> dms_enterprise_20181101_models.GetOpLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_op_log_with_options_async(request, runtime)

    def get_order_base_info_with_options(
        self,
        request: dms_enterprise_20181101_models.GetOrderBaseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetOrderBaseInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetOrderBaseInfoResponse().from_map(
            self.do_rpcrequest('GetOrderBaseInfo', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_order_base_info_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetOrderBaseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetOrderBaseInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetOrderBaseInfoResponse().from_map(
            await self.do_rpcrequest_async('GetOrderBaseInfo', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_order_base_info(
        self,
        request: dms_enterprise_20181101_models.GetOrderBaseInfoRequest,
    ) -> dms_enterprise_20181101_models.GetOrderBaseInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_order_base_info_with_options(request, runtime)

    async def get_order_base_info_async(
        self,
        request: dms_enterprise_20181101_models.GetOrderBaseInfoRequest,
    ) -> dms_enterprise_20181101_models.GetOrderBaseInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_order_base_info_with_options_async(request, runtime)

    def get_table_dbtopology_with_options(
        self,
        request: dms_enterprise_20181101_models.GetTableDBTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetTableDBTopologyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetTableDBTopologyResponse().from_map(
            self.do_rpcrequest('GetTableDBTopology', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_table_dbtopology_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetTableDBTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetTableDBTopologyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetTableDBTopologyResponse().from_map(
            await self.do_rpcrequest_async('GetTableDBTopology', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_table_dbtopology(
        self,
        request: dms_enterprise_20181101_models.GetTableDBTopologyRequest,
    ) -> dms_enterprise_20181101_models.GetTableDBTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_table_dbtopology_with_options(request, runtime)

    async def get_table_dbtopology_async(
        self,
        request: dms_enterprise_20181101_models.GetTableDBTopologyRequest,
    ) -> dms_enterprise_20181101_models.GetTableDBTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_table_dbtopology_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: dms_enterprise_20181101_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetUserResponse().from_map(
            self.do_rpcrequest('GetUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GetUserResponse().from_map(
            await self.do_rpcrequest_async('GetUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user(
        self,
        request: dms_enterprise_20181101_models.GetUserRequest,
    ) -> dms_enterprise_20181101_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: dms_enterprise_20181101_models.GetUserRequest,
    ) -> dms_enterprise_20181101_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def get_user_active_tenant_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetUserActiveTenantResponse:
        req = open_api_models.OpenApiRequest()
        return dms_enterprise_20181101_models.GetUserActiveTenantResponse().from_map(
            self.do_rpcrequest('GetUserActiveTenant', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_active_tenant_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetUserActiveTenantResponse:
        req = open_api_models.OpenApiRequest()
        return dms_enterprise_20181101_models.GetUserActiveTenantResponse().from_map(
            await self.do_rpcrequest_async('GetUserActiveTenant', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_active_tenant(self) -> dms_enterprise_20181101_models.GetUserActiveTenantResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_active_tenant_with_options(runtime)

    async def get_user_active_tenant_async(self) -> dms_enterprise_20181101_models.GetUserActiveTenantResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_active_tenant_with_options_async(runtime)

    def grant_user_permission_with_options(
        self,
        request: dms_enterprise_20181101_models.GrantUserPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GrantUserPermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GrantUserPermissionResponse().from_map(
            self.do_rpcrequest('GrantUserPermission', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def grant_user_permission_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GrantUserPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GrantUserPermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.GrantUserPermissionResponse().from_map(
            await self.do_rpcrequest_async('GrantUserPermission', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grant_user_permission(
        self,
        request: dms_enterprise_20181101_models.GrantUserPermissionRequest,
    ) -> dms_enterprise_20181101_models.GrantUserPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_user_permission_with_options(request, runtime)

    async def grant_user_permission_async(
        self,
        request: dms_enterprise_20181101_models.GrantUserPermissionRequest,
    ) -> dms_enterprise_20181101_models.GrantUserPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_user_permission_with_options_async(request, runtime)

    def list_columns_with_options(
        self,
        request: dms_enterprise_20181101_models.ListColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListColumnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListColumnsResponse().from_map(
            self.do_rpcrequest('ListColumns', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_columns_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListColumnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListColumnsResponse().from_map(
            await self.do_rpcrequest_async('ListColumns', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_columns(
        self,
        request: dms_enterprise_20181101_models.ListColumnsRequest,
    ) -> dms_enterprise_20181101_models.ListColumnsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_columns_with_options(request, runtime)

    async def list_columns_async(
        self,
        request: dms_enterprise_20181101_models.ListColumnsRequest,
    ) -> dms_enterprise_20181101_models.ListColumnsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_columns_with_options_async(request, runtime)

    def list_databases_with_options(
        self,
        request: dms_enterprise_20181101_models.ListDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDatabasesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListDatabasesResponse().from_map(
            self.do_rpcrequest('ListDatabases', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_databases_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDatabasesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListDatabasesResponse().from_map(
            await self.do_rpcrequest_async('ListDatabases', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_databases(
        self,
        request: dms_enterprise_20181101_models.ListDatabasesRequest,
    ) -> dms_enterprise_20181101_models.ListDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_databases_with_options(request, runtime)

    async def list_databases_async(
        self,
        request: dms_enterprise_20181101_models.ListDatabasesRequest,
    ) -> dms_enterprise_20181101_models.ListDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_databases_with_options_async(request, runtime)

    def list_database_user_permssions_with_options(
        self,
        request: dms_enterprise_20181101_models.ListDatabaseUserPermssionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDatabaseUserPermssionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListDatabaseUserPermssionsResponse().from_map(
            self.do_rpcrequest('ListDatabaseUserPermssions', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_database_user_permssions_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListDatabaseUserPermssionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDatabaseUserPermssionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListDatabaseUserPermssionsResponse().from_map(
            await self.do_rpcrequest_async('ListDatabaseUserPermssions', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_database_user_permssions(
        self,
        request: dms_enterprise_20181101_models.ListDatabaseUserPermssionsRequest,
    ) -> dms_enterprise_20181101_models.ListDatabaseUserPermssionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_database_user_permssions_with_options(request, runtime)

    async def list_database_user_permssions_async(
        self,
        request: dms_enterprise_20181101_models.ListDatabaseUserPermssionsRequest,
    ) -> dms_enterprise_20181101_models.ListDatabaseUserPermssionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_database_user_permssions_with_options_async(request, runtime)

    def list_indexes_with_options(
        self,
        request: dms_enterprise_20181101_models.ListIndexesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListIndexesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListIndexesResponse().from_map(
            self.do_rpcrequest('ListIndexes', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_indexes_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListIndexesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListIndexesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListIndexesResponse().from_map(
            await self.do_rpcrequest_async('ListIndexes', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_indexes(
        self,
        request: dms_enterprise_20181101_models.ListIndexesRequest,
    ) -> dms_enterprise_20181101_models.ListIndexesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_indexes_with_options(request, runtime)

    async def list_indexes_async(
        self,
        request: dms_enterprise_20181101_models.ListIndexesRequest,
    ) -> dms_enterprise_20181101_models.ListIndexesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_indexes_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: dms_enterprise_20181101_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListInstancesResponse().from_map(
            self.do_rpcrequest('ListInstances', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListInstancesResponse().from_map(
            await self.do_rpcrequest_async('ListInstances', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instances(
        self,
        request: dms_enterprise_20181101_models.ListInstancesRequest,
    ) -> dms_enterprise_20181101_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: dms_enterprise_20181101_models.ListInstancesRequest,
    ) -> dms_enterprise_20181101_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_logic_databases_with_options(
        self,
        request: dms_enterprise_20181101_models.ListLogicDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListLogicDatabasesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListLogicDatabasesResponse().from_map(
            self.do_rpcrequest('ListLogicDatabases', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_logic_databases_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListLogicDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListLogicDatabasesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListLogicDatabasesResponse().from_map(
            await self.do_rpcrequest_async('ListLogicDatabases', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_logic_databases(
        self,
        request: dms_enterprise_20181101_models.ListLogicDatabasesRequest,
    ) -> dms_enterprise_20181101_models.ListLogicDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_logic_databases_with_options(request, runtime)

    async def list_logic_databases_async(
        self,
        request: dms_enterprise_20181101_models.ListLogicDatabasesRequest,
    ) -> dms_enterprise_20181101_models.ListLogicDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_logic_databases_with_options_async(request, runtime)

    def list_logic_tables_with_options(
        self,
        request: dms_enterprise_20181101_models.ListLogicTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListLogicTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListLogicTablesResponse().from_map(
            self.do_rpcrequest('ListLogicTables', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_logic_tables_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListLogicTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListLogicTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListLogicTablesResponse().from_map(
            await self.do_rpcrequest_async('ListLogicTables', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_logic_tables(
        self,
        request: dms_enterprise_20181101_models.ListLogicTablesRequest,
    ) -> dms_enterprise_20181101_models.ListLogicTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_logic_tables_with_options(request, runtime)

    async def list_logic_tables_async(
        self,
        request: dms_enterprise_20181101_models.ListLogicTablesRequest,
    ) -> dms_enterprise_20181101_models.ListLogicTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_logic_tables_with_options_async(request, runtime)

    def list_orders_with_options(
        self,
        request: dms_enterprise_20181101_models.ListOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListOrdersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListOrdersResponse().from_map(
            self.do_rpcrequest('ListOrders', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_orders_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListOrdersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListOrdersResponse().from_map(
            await self.do_rpcrequest_async('ListOrders', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_orders(
        self,
        request: dms_enterprise_20181101_models.ListOrdersRequest,
    ) -> dms_enterprise_20181101_models.ListOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_orders_with_options(request, runtime)

    async def list_orders_async(
        self,
        request: dms_enterprise_20181101_models.ListOrdersRequest,
    ) -> dms_enterprise_20181101_models.ListOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_orders_with_options_async(request, runtime)

    def list_sensitive_columns_with_options(
        self,
        request: dms_enterprise_20181101_models.ListSensitiveColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListSensitiveColumnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListSensitiveColumnsResponse().from_map(
            self.do_rpcrequest('ListSensitiveColumns', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_sensitive_columns_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListSensitiveColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListSensitiveColumnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListSensitiveColumnsResponse().from_map(
            await self.do_rpcrequest_async('ListSensitiveColumns', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_sensitive_columns(
        self,
        request: dms_enterprise_20181101_models.ListSensitiveColumnsRequest,
    ) -> dms_enterprise_20181101_models.ListSensitiveColumnsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sensitive_columns_with_options(request, runtime)

    async def list_sensitive_columns_async(
        self,
        request: dms_enterprise_20181101_models.ListSensitiveColumnsRequest,
    ) -> dms_enterprise_20181101_models.ListSensitiveColumnsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sensitive_columns_with_options_async(request, runtime)

    def list_sensitive_columns_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.ListSensitiveColumnsDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListSensitiveColumnsDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListSensitiveColumnsDetailResponse().from_map(
            self.do_rpcrequest('ListSensitiveColumnsDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_sensitive_columns_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListSensitiveColumnsDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListSensitiveColumnsDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListSensitiveColumnsDetailResponse().from_map(
            await self.do_rpcrequest_async('ListSensitiveColumnsDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_sensitive_columns_detail(
        self,
        request: dms_enterprise_20181101_models.ListSensitiveColumnsDetailRequest,
    ) -> dms_enterprise_20181101_models.ListSensitiveColumnsDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sensitive_columns_detail_with_options(request, runtime)

    async def list_sensitive_columns_detail_async(
        self,
        request: dms_enterprise_20181101_models.ListSensitiveColumnsDetailRequest,
    ) -> dms_enterprise_20181101_models.ListSensitiveColumnsDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sensitive_columns_detail_with_options_async(request, runtime)

    def list_tables_with_options(
        self,
        request: dms_enterprise_20181101_models.ListTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListTablesResponse().from_map(
            self.do_rpcrequest('ListTables', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tables_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListTablesResponse().from_map(
            await self.do_rpcrequest_async('ListTables', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tables(
        self,
        request: dms_enterprise_20181101_models.ListTablesRequest,
    ) -> dms_enterprise_20181101_models.ListTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tables_with_options(request, runtime)

    async def list_tables_async(
        self,
        request: dms_enterprise_20181101_models.ListTablesRequest,
    ) -> dms_enterprise_20181101_models.ListTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tables_with_options_async(request, runtime)

    def list_user_permissions_with_options(
        self,
        request: dms_enterprise_20181101_models.ListUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListUserPermissionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListUserPermissionsResponse().from_map(
            self.do_rpcrequest('ListUserPermissions', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_permissions_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListUserPermissionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListUserPermissionsResponse().from_map(
            await self.do_rpcrequest_async('ListUserPermissions', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_permissions(
        self,
        request: dms_enterprise_20181101_models.ListUserPermissionsRequest,
    ) -> dms_enterprise_20181101_models.ListUserPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_permissions_with_options(request, runtime)

    async def list_user_permissions_async(
        self,
        request: dms_enterprise_20181101_models.ListUserPermissionsRequest,
    ) -> dms_enterprise_20181101_models.ListUserPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_permissions_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: dms_enterprise_20181101_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListUsersResponse().from_map(
            self.do_rpcrequest('ListUsers', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListUsersResponse().from_map(
            await self.do_rpcrequest_async('ListUsers', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users(
        self,
        request: dms_enterprise_20181101_models.ListUsersRequest,
    ) -> dms_enterprise_20181101_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: dms_enterprise_20181101_models.ListUsersRequest,
    ) -> dms_enterprise_20181101_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_user_tenants_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListUserTenantsResponse:
        req = open_api_models.OpenApiRequest()
        return dms_enterprise_20181101_models.ListUserTenantsResponse().from_map(
            self.do_rpcrequest('ListUserTenants', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_tenants_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListUserTenantsResponse:
        req = open_api_models.OpenApiRequest()
        return dms_enterprise_20181101_models.ListUserTenantsResponse().from_map(
            await self.do_rpcrequest_async('ListUserTenants', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_tenants(self) -> dms_enterprise_20181101_models.ListUserTenantsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_tenants_with_options(runtime)

    async def list_user_tenants_async(self) -> dms_enterprise_20181101_models.ListUserTenantsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_tenants_with_options_async(runtime)

    def list_work_flow_nodes_with_options(
        self,
        request: dms_enterprise_20181101_models.ListWorkFlowNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListWorkFlowNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListWorkFlowNodesResponse().from_map(
            self.do_rpcrequest('ListWorkFlowNodes', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_work_flow_nodes_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListWorkFlowNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListWorkFlowNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListWorkFlowNodesResponse().from_map(
            await self.do_rpcrequest_async('ListWorkFlowNodes', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_work_flow_nodes(
        self,
        request: dms_enterprise_20181101_models.ListWorkFlowNodesRequest,
    ) -> dms_enterprise_20181101_models.ListWorkFlowNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_work_flow_nodes_with_options(request, runtime)

    async def list_work_flow_nodes_async(
        self,
        request: dms_enterprise_20181101_models.ListWorkFlowNodesRequest,
    ) -> dms_enterprise_20181101_models.ListWorkFlowNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_work_flow_nodes_with_options_async(request, runtime)

    def list_work_flow_templates_with_options(
        self,
        request: dms_enterprise_20181101_models.ListWorkFlowTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListWorkFlowTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListWorkFlowTemplatesResponse().from_map(
            self.do_rpcrequest('ListWorkFlowTemplates', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_work_flow_templates_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListWorkFlowTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListWorkFlowTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.ListWorkFlowTemplatesResponse().from_map(
            await self.do_rpcrequest_async('ListWorkFlowTemplates', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_work_flow_templates(
        self,
        request: dms_enterprise_20181101_models.ListWorkFlowTemplatesRequest,
    ) -> dms_enterprise_20181101_models.ListWorkFlowTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_work_flow_templates_with_options(request, runtime)

    async def list_work_flow_templates_async(
        self,
        request: dms_enterprise_20181101_models.ListWorkFlowTemplatesRequest,
    ) -> dms_enterprise_20181101_models.ListWorkFlowTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_work_flow_templates_with_options_async(request, runtime)

    def register_instance_with_options(
        self,
        request: dms_enterprise_20181101_models.RegisterInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RegisterInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.RegisterInstanceResponse().from_map(
            self.do_rpcrequest('RegisterInstance', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_instance_with_options_async(
        self,
        request: dms_enterprise_20181101_models.RegisterInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RegisterInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.RegisterInstanceResponse().from_map(
            await self.do_rpcrequest_async('RegisterInstance', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_instance(
        self,
        request: dms_enterprise_20181101_models.RegisterInstanceRequest,
    ) -> dms_enterprise_20181101_models.RegisterInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_instance_with_options(request, runtime)

    async def register_instance_async(
        self,
        request: dms_enterprise_20181101_models.RegisterInstanceRequest,
    ) -> dms_enterprise_20181101_models.RegisterInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_instance_with_options_async(request, runtime)

    def register_user_with_options(
        self,
        request: dms_enterprise_20181101_models.RegisterUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RegisterUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.RegisterUserResponse().from_map(
            self.do_rpcrequest('RegisterUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_user_with_options_async(
        self,
        request: dms_enterprise_20181101_models.RegisterUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RegisterUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.RegisterUserResponse().from_map(
            await self.do_rpcrequest_async('RegisterUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_user(
        self,
        request: dms_enterprise_20181101_models.RegisterUserRequest,
    ) -> dms_enterprise_20181101_models.RegisterUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_user_with_options(request, runtime)

    async def register_user_async(
        self,
        request: dms_enterprise_20181101_models.RegisterUserRequest,
    ) -> dms_enterprise_20181101_models.RegisterUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_user_with_options_async(request, runtime)

    def revoke_user_permission_with_options(
        self,
        request: dms_enterprise_20181101_models.RevokeUserPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RevokeUserPermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.RevokeUserPermissionResponse().from_map(
            self.do_rpcrequest('RevokeUserPermission', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def revoke_user_permission_with_options_async(
        self,
        request: dms_enterprise_20181101_models.RevokeUserPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RevokeUserPermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.RevokeUserPermissionResponse().from_map(
            await self.do_rpcrequest_async('RevokeUserPermission', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_user_permission(
        self,
        request: dms_enterprise_20181101_models.RevokeUserPermissionRequest,
    ) -> dms_enterprise_20181101_models.RevokeUserPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_user_permission_with_options(request, runtime)

    async def revoke_user_permission_async(
        self,
        request: dms_enterprise_20181101_models.RevokeUserPermissionRequest,
    ) -> dms_enterprise_20181101_models.RevokeUserPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_user_permission_with_options_async(request, runtime)

    def search_database_with_options(
        self,
        request: dms_enterprise_20181101_models.SearchDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SearchDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SearchDatabaseResponse().from_map(
            self.do_rpcrequest('SearchDatabase', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_database_with_options_async(
        self,
        request: dms_enterprise_20181101_models.SearchDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SearchDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SearchDatabaseResponse().from_map(
            await self.do_rpcrequest_async('SearchDatabase', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_database(
        self,
        request: dms_enterprise_20181101_models.SearchDatabaseRequest,
    ) -> dms_enterprise_20181101_models.SearchDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_database_with_options(request, runtime)

    async def search_database_async(
        self,
        request: dms_enterprise_20181101_models.SearchDatabaseRequest,
    ) -> dms_enterprise_20181101_models.SearchDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_database_with_options_async(request, runtime)

    def search_table_with_options(
        self,
        request: dms_enterprise_20181101_models.SearchTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SearchTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SearchTableResponse().from_map(
            self.do_rpcrequest('SearchTable', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_table_with_options_async(
        self,
        request: dms_enterprise_20181101_models.SearchTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SearchTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SearchTableResponse().from_map(
            await self.do_rpcrequest_async('SearchTable', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_table(
        self,
        request: dms_enterprise_20181101_models.SearchTableRequest,
    ) -> dms_enterprise_20181101_models.SearchTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_table_with_options(request, runtime)

    async def search_table_async(
        self,
        request: dms_enterprise_20181101_models.SearchTableRequest,
    ) -> dms_enterprise_20181101_models.SearchTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_table_with_options_async(request, runtime)

    def set_owners_with_options(
        self,
        request: dms_enterprise_20181101_models.SetOwnersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SetOwnersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SetOwnersResponse().from_map(
            self.do_rpcrequest('SetOwners', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_owners_with_options_async(
        self,
        request: dms_enterprise_20181101_models.SetOwnersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SetOwnersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SetOwnersResponse().from_map(
            await self.do_rpcrequest_async('SetOwners', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_owners(
        self,
        request: dms_enterprise_20181101_models.SetOwnersRequest,
    ) -> dms_enterprise_20181101_models.SetOwnersResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_owners_with_options(request, runtime)

    async def set_owners_async(
        self,
        request: dms_enterprise_20181101_models.SetOwnersRequest,
    ) -> dms_enterprise_20181101_models.SetOwnersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_owners_with_options_async(request, runtime)

    def submit_order_approval_with_options(
        self,
        request: dms_enterprise_20181101_models.SubmitOrderApprovalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SubmitOrderApprovalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SubmitOrderApprovalResponse().from_map(
            self.do_rpcrequest('SubmitOrderApproval', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_order_approval_with_options_async(
        self,
        request: dms_enterprise_20181101_models.SubmitOrderApprovalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SubmitOrderApprovalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SubmitOrderApprovalResponse().from_map(
            await self.do_rpcrequest_async('SubmitOrderApproval', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_order_approval(
        self,
        request: dms_enterprise_20181101_models.SubmitOrderApprovalRequest,
    ) -> dms_enterprise_20181101_models.SubmitOrderApprovalResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_order_approval_with_options(request, runtime)

    async def submit_order_approval_async(
        self,
        request: dms_enterprise_20181101_models.SubmitOrderApprovalRequest,
    ) -> dms_enterprise_20181101_models.SubmitOrderApprovalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_order_approval_with_options_async(request, runtime)

    def sync_database_meta_with_options(
        self,
        request: dms_enterprise_20181101_models.SyncDatabaseMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SyncDatabaseMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SyncDatabaseMetaResponse().from_map(
            self.do_rpcrequest('SyncDatabaseMeta', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sync_database_meta_with_options_async(
        self,
        request: dms_enterprise_20181101_models.SyncDatabaseMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SyncDatabaseMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SyncDatabaseMetaResponse().from_map(
            await self.do_rpcrequest_async('SyncDatabaseMeta', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_database_meta(
        self,
        request: dms_enterprise_20181101_models.SyncDatabaseMetaRequest,
    ) -> dms_enterprise_20181101_models.SyncDatabaseMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.sync_database_meta_with_options(request, runtime)

    async def sync_database_meta_async(
        self,
        request: dms_enterprise_20181101_models.SyncDatabaseMetaRequest,
    ) -> dms_enterprise_20181101_models.SyncDatabaseMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sync_database_meta_with_options_async(request, runtime)

    def sync_instance_meta_with_options(
        self,
        request: dms_enterprise_20181101_models.SyncInstanceMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SyncInstanceMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SyncInstanceMetaResponse().from_map(
            self.do_rpcrequest('SyncInstanceMeta', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sync_instance_meta_with_options_async(
        self,
        request: dms_enterprise_20181101_models.SyncInstanceMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SyncInstanceMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.SyncInstanceMetaResponse().from_map(
            await self.do_rpcrequest_async('SyncInstanceMeta', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_instance_meta(
        self,
        request: dms_enterprise_20181101_models.SyncInstanceMetaRequest,
    ) -> dms_enterprise_20181101_models.SyncInstanceMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.sync_instance_meta_with_options(request, runtime)

    async def sync_instance_meta_async(
        self,
        request: dms_enterprise_20181101_models.SyncInstanceMetaRequest,
    ) -> dms_enterprise_20181101_models.SyncInstanceMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sync_instance_meta_with_options_async(request, runtime)

    def update_instance_with_options(
        self,
        request: dms_enterprise_20181101_models.UpdateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.UpdateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.UpdateInstanceResponse().from_map(
            self.do_rpcrequest('UpdateInstance', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        request: dms_enterprise_20181101_models.UpdateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.UpdateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.UpdateInstanceResponse().from_map(
            await self.do_rpcrequest_async('UpdateInstance', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_instance(
        self,
        request: dms_enterprise_20181101_models.UpdateInstanceRequest,
    ) -> dms_enterprise_20181101_models.UpdateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_instance_with_options(request, runtime)

    async def update_instance_async(
        self,
        request: dms_enterprise_20181101_models.UpdateInstanceRequest,
    ) -> dms_enterprise_20181101_models.UpdateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: dms_enterprise_20181101_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.UpdateUserResponse().from_map(
            self.do_rpcrequest('UpdateUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: dms_enterprise_20181101_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return dms_enterprise_20181101_models.UpdateUserResponse().from_map(
            await self.do_rpcrequest_async('UpdateUser', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_user(
        self,
        request: dms_enterprise_20181101_models.UpdateUserRequest,
    ) -> dms_enterprise_20181101_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: dms_enterprise_20181101_models.UpdateUserRequest,
    ) -> dms_enterprise_20181101_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)
