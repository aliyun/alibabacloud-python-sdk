# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

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

    def add_lh_members_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.AddLhMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.AddLhMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.AddLhMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        query = {}
        if not UtilClient.is_unset(request.members_shrink):
            query['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLhMembers',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.AddLhMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_lh_members_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.AddLhMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.AddLhMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.AddLhMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        query = {}
        if not UtilClient.is_unset(request.members_shrink):
            query['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLhMembers',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.AddLhMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_lh_members(
        self,
        request: dms_enterprise_20181101_models.AddLhMembersRequest,
    ) -> dms_enterprise_20181101_models.AddLhMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_lh_members_with_options(request, runtime)

    async def add_lh_members_async(
        self,
        request: dms_enterprise_20181101_models.AddLhMembersRequest,
    ) -> dms_enterprise_20181101_models.AddLhMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_lh_members_with_options_async(request, runtime)

    def add_logic_table_route_config_with_options(
        self,
        request: dms_enterprise_20181101_models.AddLogicTableRouteConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.AddLogicTableRouteConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.route_expr):
            query['RouteExpr'] = request.route_expr
        if not UtilClient.is_unset(request.route_key):
            query['RouteKey'] = request.route_key
        if not UtilClient.is_unset(request.table_id):
            query['TableId'] = request.table_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLogicTableRouteConfig',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.AddLogicTableRouteConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_logic_table_route_config_with_options_async(
        self,
        request: dms_enterprise_20181101_models.AddLogicTableRouteConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.AddLogicTableRouteConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.route_expr):
            query['RouteExpr'] = request.route_expr
        if not UtilClient.is_unset(request.route_key):
            query['RouteKey'] = request.route_key
        if not UtilClient.is_unset(request.table_id):
            query['TableId'] = request.table_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLogicTableRouteConfig',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.AddLogicTableRouteConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_logic_table_route_config(
        self,
        request: dms_enterprise_20181101_models.AddLogicTableRouteConfigRequest,
    ) -> dms_enterprise_20181101_models.AddLogicTableRouteConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_logic_table_route_config_with_options(request, runtime)

    async def add_logic_table_route_config_async(
        self,
        request: dms_enterprise_20181101_models.AddLogicTableRouteConfigRequest,
    ) -> dms_enterprise_20181101_models.AddLogicTableRouteConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_logic_table_route_config_with_options_async(request, runtime)

    def approve_order_with_options(
        self,
        request: dms_enterprise_20181101_models.ApproveOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ApproveOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.approval_type):
            query['ApprovalType'] = request.approval_type
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workflow_instance_id):
            query['WorkflowInstanceId'] = request.workflow_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApproveOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ApproveOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def approve_order_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ApproveOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ApproveOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.approval_type):
            query['ApprovalType'] = request.approval_type
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workflow_instance_id):
            query['WorkflowInstanceId'] = request.workflow_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApproveOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ApproveOrderResponse(),
            await self.call_api_async(params, req, runtime)
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

    def change_column_sec_level_with_options(
        self,
        request: dms_enterprise_20181101_models.ChangeColumnSecLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ChangeColumnSecLevelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.column_name):
            query['ColumnName'] = request.column_name
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.is_logic):
            query['IsLogic'] = request.is_logic
        if not UtilClient.is_unset(request.new_level):
            query['NewLevel'] = request.new_level
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeColumnSecLevel',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ChangeColumnSecLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_column_sec_level_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ChangeColumnSecLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ChangeColumnSecLevelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.column_name):
            query['ColumnName'] = request.column_name
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.is_logic):
            query['IsLogic'] = request.is_logic
        if not UtilClient.is_unset(request.new_level):
            query['NewLevel'] = request.new_level
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeColumnSecLevel',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ChangeColumnSecLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_column_sec_level(
        self,
        request: dms_enterprise_20181101_models.ChangeColumnSecLevelRequest,
    ) -> dms_enterprise_20181101_models.ChangeColumnSecLevelResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_column_sec_level_with_options(request, runtime)

    async def change_column_sec_level_async(
        self,
        request: dms_enterprise_20181101_models.ChangeColumnSecLevelRequest,
    ) -> dms_enterprise_20181101_models.ChangeColumnSecLevelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_column_sec_level_with_options_async(request, runtime)

    def change_lh_dag_owner_with_options(
        self,
        request: dms_enterprise_20181101_models.ChangeLhDagOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ChangeLhDagOwnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dag_id):
            query['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeLhDagOwner',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ChangeLhDagOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_lh_dag_owner_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ChangeLhDagOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ChangeLhDagOwnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dag_id):
            query['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeLhDagOwner',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ChangeLhDagOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_lh_dag_owner(
        self,
        request: dms_enterprise_20181101_models.ChangeLhDagOwnerRequest,
    ) -> dms_enterprise_20181101_models.ChangeLhDagOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_lh_dag_owner_with_options(request, runtime)

    async def change_lh_dag_owner_async(
        self,
        request: dms_enterprise_20181101_models.ChangeLhDagOwnerRequest,
    ) -> dms_enterprise_20181101_models.ChangeLhDagOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_lh_dag_owner_with_options_async(request, runtime)

    def close_order_with_options(
        self,
        request: dms_enterprise_20181101_models.CloseOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CloseOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.close_reason):
            query['CloseReason'] = request.close_reason
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CloseOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_order_with_options_async(
        self,
        request: dms_enterprise_20181101_models.CloseOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CloseOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.close_reason):
            query['CloseReason'] = request.close_reason
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CloseOrderResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_data_correct_order_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateDataCorrectOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateDataCorrectOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateDataCorrectOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.attachment_key):
            query['AttachmentKey'] = request.attachment_key
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.param_shrink):
            query['Param'] = request.param_shrink
        if not UtilClient.is_unset(request.related_user_list_shrink):
            query['RelatedUserList'] = request.related_user_list_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataCorrectOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateDataCorrectOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_correct_order_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateDataCorrectOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateDataCorrectOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateDataCorrectOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.attachment_key):
            query['AttachmentKey'] = request.attachment_key
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.param_shrink):
            query['Param'] = request.param_shrink
        if not UtilClient.is_unset(request.related_user_list_shrink):
            query['RelatedUserList'] = request.related_user_list_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataCorrectOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateDataCorrectOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_correct_order(
        self,
        request: dms_enterprise_20181101_models.CreateDataCorrectOrderRequest,
    ) -> dms_enterprise_20181101_models.CreateDataCorrectOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_data_correct_order_with_options(request, runtime)

    async def create_data_correct_order_async(
        self,
        request: dms_enterprise_20181101_models.CreateDataCorrectOrderRequest,
    ) -> dms_enterprise_20181101_models.CreateDataCorrectOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_data_correct_order_with_options_async(request, runtime)

    def create_data_cron_clear_order_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateDataCronClearOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateDataCronClearOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateDataCronClearOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.attachment_key):
            query['AttachmentKey'] = request.attachment_key
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.param_shrink):
            query['Param'] = request.param_shrink
        if not UtilClient.is_unset(request.related_user_list_shrink):
            query['RelatedUserList'] = request.related_user_list_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataCronClearOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateDataCronClearOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_cron_clear_order_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateDataCronClearOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateDataCronClearOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateDataCronClearOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.attachment_key):
            query['AttachmentKey'] = request.attachment_key
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.param_shrink):
            query['Param'] = request.param_shrink
        if not UtilClient.is_unset(request.related_user_list_shrink):
            query['RelatedUserList'] = request.related_user_list_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataCronClearOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateDataCronClearOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_cron_clear_order(
        self,
        request: dms_enterprise_20181101_models.CreateDataCronClearOrderRequest,
    ) -> dms_enterprise_20181101_models.CreateDataCronClearOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_data_cron_clear_order_with_options(request, runtime)

    async def create_data_cron_clear_order_async(
        self,
        request: dms_enterprise_20181101_models.CreateDataCronClearOrderRequest,
    ) -> dms_enterprise_20181101_models.CreateDataCronClearOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_data_cron_clear_order_with_options_async(request, runtime)

    def create_data_import_order_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateDataImportOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateDataImportOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateDataImportOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.attachment_key):
            query['AttachmentKey'] = request.attachment_key
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.param_shrink):
            query['Param'] = request.param_shrink
        if not UtilClient.is_unset(request.related_user_list_shrink):
            query['RelatedUserList'] = request.related_user_list_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataImportOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateDataImportOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_import_order_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateDataImportOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateDataImportOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateDataImportOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.attachment_key):
            query['AttachmentKey'] = request.attachment_key
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.param_shrink):
            query['Param'] = request.param_shrink
        if not UtilClient.is_unset(request.related_user_list_shrink):
            query['RelatedUserList'] = request.related_user_list_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataImportOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateDataImportOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_import_order(
        self,
        request: dms_enterprise_20181101_models.CreateDataImportOrderRequest,
    ) -> dms_enterprise_20181101_models.CreateDataImportOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_data_import_order_with_options(request, runtime)

    async def create_data_import_order_async(
        self,
        request: dms_enterprise_20181101_models.CreateDataImportOrderRequest,
    ) -> dms_enterprise_20181101_models.CreateDataImportOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_data_import_order_with_options_async(request, runtime)

    def create_free_lock_correct_order_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateFreeLockCorrectOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateFreeLockCorrectOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateFreeLockCorrectOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.attachment_key):
            query['AttachmentKey'] = request.attachment_key
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.param_shrink):
            query['Param'] = request.param_shrink
        if not UtilClient.is_unset(request.related_user_list_shrink):
            query['RelatedUserList'] = request.related_user_list_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFreeLockCorrectOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateFreeLockCorrectOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_free_lock_correct_order_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateFreeLockCorrectOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateFreeLockCorrectOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateFreeLockCorrectOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.attachment_key):
            query['AttachmentKey'] = request.attachment_key
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.param_shrink):
            query['Param'] = request.param_shrink
        if not UtilClient.is_unset(request.related_user_list_shrink):
            query['RelatedUserList'] = request.related_user_list_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFreeLockCorrectOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateFreeLockCorrectOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_free_lock_correct_order(
        self,
        request: dms_enterprise_20181101_models.CreateFreeLockCorrectOrderRequest,
    ) -> dms_enterprise_20181101_models.CreateFreeLockCorrectOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_free_lock_correct_order_with_options(request, runtime)

    async def create_free_lock_correct_order_async(
        self,
        request: dms_enterprise_20181101_models.CreateFreeLockCorrectOrderRequest,
    ) -> dms_enterprise_20181101_models.CreateFreeLockCorrectOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_free_lock_correct_order_with_options_async(request, runtime)

    def create_lake_house_space_with_options(
        self,
        request: dms_enterprise_20181101_models.CreateLakeHouseSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateLakeHouseSpaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dev_db_id):
            query['DevDbId'] = request.dev_db_id
        if not UtilClient.is_unset(request.dw_db_type):
            query['DwDbType'] = request.dw_db_type
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.prod_db_id):
            query['ProdDbId'] = request.prod_db_id
        if not UtilClient.is_unset(request.space_config):
            query['SpaceConfig'] = request.space_config
        if not UtilClient.is_unset(request.space_name):
            query['SpaceName'] = request.space_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLakeHouseSpace',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateLakeHouseSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lake_house_space_with_options_async(
        self,
        request: dms_enterprise_20181101_models.CreateLakeHouseSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateLakeHouseSpaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dev_db_id):
            query['DevDbId'] = request.dev_db_id
        if not UtilClient.is_unset(request.dw_db_type):
            query['DwDbType'] = request.dw_db_type
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.prod_db_id):
            query['ProdDbId'] = request.prod_db_id
        if not UtilClient.is_unset(request.space_config):
            query['SpaceConfig'] = request.space_config
        if not UtilClient.is_unset(request.space_name):
            query['SpaceName'] = request.space_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLakeHouseSpace',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateLakeHouseSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lake_house_space(
        self,
        request: dms_enterprise_20181101_models.CreateLakeHouseSpaceRequest,
    ) -> dms_enterprise_20181101_models.CreateLakeHouseSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_lake_house_space_with_options(request, runtime)

    async def create_lake_house_space_async(
        self,
        request: dms_enterprise_20181101_models.CreateLakeHouseSpaceRequest,
    ) -> dms_enterprise_20181101_models.CreateLakeHouseSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_lake_house_space_with_options_async(request, runtime)

    def create_logic_database_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateLogicDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateLogicDatabaseResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateLogicDatabaseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.database_ids):
            request.database_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.database_ids, 'DatabaseIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.alias):
            query['Alias'] = request.alias
        if not UtilClient.is_unset(request.database_ids_shrink):
            query['DatabaseIds'] = request.database_ids_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLogicDatabase',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateLogicDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_logic_database_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateLogicDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateLogicDatabaseResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateLogicDatabaseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.database_ids):
            request.database_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.database_ids, 'DatabaseIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.alias):
            query['Alias'] = request.alias
        if not UtilClient.is_unset(request.database_ids_shrink):
            query['DatabaseIds'] = request.database_ids_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLogicDatabase',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateLogicDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_logic_database(
        self,
        request: dms_enterprise_20181101_models.CreateLogicDatabaseRequest,
    ) -> dms_enterprise_20181101_models.CreateLogicDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_logic_database_with_options(request, runtime)

    async def create_logic_database_async(
        self,
        request: dms_enterprise_20181101_models.CreateLogicDatabaseRequest,
    ) -> dms_enterprise_20181101_models.CreateLogicDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_logic_database_with_options_async(request, runtime)

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
        query = {}
        if not UtilClient.is_unset(request.attachment_key):
            query['AttachmentKey'] = request.attachment_key
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.plugin_type):
            query['PluginType'] = request.plugin_type
        if not UtilClient.is_unset(request.related_user_list):
            query['RelatedUserList'] = request.related_user_list
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        body = {}
        if not UtilClient.is_unset(request.plugin_param_shrink):
            body['PluginParam'] = request.plugin_param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateOrderResponse(),
            self.call_api(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.attachment_key):
            query['AttachmentKey'] = request.attachment_key
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.plugin_type):
            query['PluginType'] = request.plugin_type
        if not UtilClient.is_unset(request.related_user_list):
            query['RelatedUserList'] = request.related_user_list
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        body = {}
        if not UtilClient.is_unset(request.plugin_param_shrink):
            body['PluginParam'] = request.plugin_param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateOrderResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_proxy_with_options(
        self,
        request: dms_enterprise_20181101_models.CreateProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProxy',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_proxy_with_options_async(
        self,
        request: dms_enterprise_20181101_models.CreateProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProxy',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_proxy(
        self,
        request: dms_enterprise_20181101_models.CreateProxyRequest,
    ) -> dms_enterprise_20181101_models.CreateProxyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_proxy_with_options(request, runtime)

    async def create_proxy_async(
        self,
        request: dms_enterprise_20181101_models.CreateProxyRequest,
    ) -> dms_enterprise_20181101_models.CreateProxyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_proxy_with_options_async(request, runtime)

    def create_proxy_access_with_options(
        self,
        request: dms_enterprise_20181101_models.CreateProxyAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateProxyAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.indep_account):
            query['IndepAccount'] = request.indep_account
        if not UtilClient.is_unset(request.indep_password):
            query['IndepPassword'] = request.indep_password
        if not UtilClient.is_unset(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProxyAccess',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateProxyAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_proxy_access_with_options_async(
        self,
        request: dms_enterprise_20181101_models.CreateProxyAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateProxyAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.indep_account):
            query['IndepAccount'] = request.indep_account
        if not UtilClient.is_unset(request.indep_password):
            query['IndepPassword'] = request.indep_password
        if not UtilClient.is_unset(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProxyAccess',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateProxyAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_proxy_access(
        self,
        request: dms_enterprise_20181101_models.CreateProxyAccessRequest,
    ) -> dms_enterprise_20181101_models.CreateProxyAccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_proxy_access_with_options(request, runtime)

    async def create_proxy_access_async(
        self,
        request: dms_enterprise_20181101_models.CreateProxyAccessRequest,
    ) -> dms_enterprise_20181101_models.CreateProxyAccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_proxy_access_with_options_async(request, runtime)

    def create_publish_group_task_with_options(
        self,
        request: dms_enterprise_20181101_models.CreatePublishGroupTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreatePublishGroupTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.plan_time):
            query['PlanTime'] = request.plan_time
        if not UtilClient.is_unset(request.publish_strategy):
            query['PublishStrategy'] = request.publish_strategy
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePublishGroupTask',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreatePublishGroupTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_publish_group_task_with_options_async(
        self,
        request: dms_enterprise_20181101_models.CreatePublishGroupTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreatePublishGroupTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.plan_time):
            query['PlanTime'] = request.plan_time
        if not UtilClient.is_unset(request.publish_strategy):
            query['PublishStrategy'] = request.publish_strategy
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePublishGroupTask',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreatePublishGroupTaskResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_sqlreview_order_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateSQLReviewOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateSQLReviewOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateSQLReviewOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.param_shrink):
            query['Param'] = request.param_shrink
        if not UtilClient.is_unset(request.related_user_list_shrink):
            query['RelatedUserList'] = request.related_user_list_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSQLReviewOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateSQLReviewOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sqlreview_order_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateSQLReviewOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateSQLReviewOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateSQLReviewOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.param_shrink):
            query['Param'] = request.param_shrink
        if not UtilClient.is_unset(request.related_user_list_shrink):
            query['RelatedUserList'] = request.related_user_list_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSQLReviewOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateSQLReviewOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sqlreview_order(
        self,
        request: dms_enterprise_20181101_models.CreateSQLReviewOrderRequest,
    ) -> dms_enterprise_20181101_models.CreateSQLReviewOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sqlreview_order_with_options(request, runtime)

    async def create_sqlreview_order_async(
        self,
        request: dms_enterprise_20181101_models.CreateSQLReviewOrderRequest,
    ) -> dms_enterprise_20181101_models.CreateSQLReviewOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sqlreview_order_with_options_async(request, runtime)

    def create_standard_group_with_options(
        self,
        request: dms_enterprise_20181101_models.CreateStandardGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateStandardGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStandardGroup',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateStandardGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_standard_group_with_options_async(
        self,
        request: dms_enterprise_20181101_models.CreateStandardGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateStandardGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStandardGroup',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateStandardGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_standard_group(
        self,
        request: dms_enterprise_20181101_models.CreateStandardGroupRequest,
    ) -> dms_enterprise_20181101_models.CreateStandardGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_standard_group_with_options(request, runtime)

    async def create_standard_group_async(
        self,
        request: dms_enterprise_20181101_models.CreateStandardGroupRequest,
    ) -> dms_enterprise_20181101_models.CreateStandardGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_standard_group_with_options_async(request, runtime)

    def create_struct_sync_order_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateStructSyncOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateStructSyncOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateStructSyncOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.attachment_key):
            query['AttachmentKey'] = request.attachment_key
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.param_shrink):
            query['Param'] = request.param_shrink
        if not UtilClient.is_unset(request.related_user_list_shrink):
            query['RelatedUserList'] = request.related_user_list_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStructSyncOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateStructSyncOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_struct_sync_order_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateStructSyncOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateStructSyncOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateStructSyncOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        query = {}
        if not UtilClient.is_unset(request.attachment_key):
            query['AttachmentKey'] = request.attachment_key
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.param_shrink):
            query['Param'] = request.param_shrink
        if not UtilClient.is_unset(request.related_user_list_shrink):
            query['RelatedUserList'] = request.related_user_list_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStructSyncOrder',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateStructSyncOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_struct_sync_order(
        self,
        request: dms_enterprise_20181101_models.CreateStructSyncOrderRequest,
    ) -> dms_enterprise_20181101_models.CreateStructSyncOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_struct_sync_order_with_options(request, runtime)

    async def create_struct_sync_order_async(
        self,
        request: dms_enterprise_20181101_models.CreateStructSyncOrderRequest,
    ) -> dms_enterprise_20181101_models.CreateStructSyncOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_struct_sync_order_with_options_async(request, runtime)

    def create_upload_file_job_with_options(
        self,
        request: dms_enterprise_20181101_models.CreateUploadFileJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateUploadFileJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_source):
            query['FileSource'] = request.file_source
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.upload_url):
            query['UploadURL'] = request.upload_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUploadFileJob',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateUploadFileJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_upload_file_job_with_options_async(
        self,
        request: dms_enterprise_20181101_models.CreateUploadFileJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateUploadFileJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_source):
            query['FileSource'] = request.file_source
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.upload_url):
            query['UploadURL'] = request.upload_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUploadFileJob',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateUploadFileJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_upload_file_job(
        self,
        request: dms_enterprise_20181101_models.CreateUploadFileJobRequest,
    ) -> dms_enterprise_20181101_models.CreateUploadFileJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_upload_file_job_with_options(request, runtime)

    async def create_upload_file_job_async(
        self,
        request: dms_enterprise_20181101_models.CreateUploadFileJobRequest,
    ) -> dms_enterprise_20181101_models.CreateUploadFileJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_upload_file_job_with_options_async(request, runtime)

    def create_upload_ossfile_job_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateUploadOSSFileJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateUploadOSSFileJobResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateUploadOSSFileJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.upload_target):
            request.upload_target_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.upload_target), 'UploadTarget', 'json')
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_source):
            query['FileSource'] = request.file_source
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.upload_target_shrink):
            query['UploadTarget'] = request.upload_target_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUploadOSSFileJob',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateUploadOSSFileJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_upload_ossfile_job_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateUploadOSSFileJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateUploadOSSFileJobResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateUploadOSSFileJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.upload_target):
            request.upload_target_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.upload_target), 'UploadTarget', 'json')
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_source):
            query['FileSource'] = request.file_source
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.upload_target_shrink):
            query['UploadTarget'] = request.upload_target_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUploadOSSFileJob',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateUploadOSSFileJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_upload_ossfile_job(
        self,
        request: dms_enterprise_20181101_models.CreateUploadOSSFileJobRequest,
    ) -> dms_enterprise_20181101_models.CreateUploadOSSFileJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_upload_ossfile_job_with_options(request, runtime)

    async def create_upload_ossfile_job_async(
        self,
        request: dms_enterprise_20181101_models.CreateUploadOSSFileJobRequest,
    ) -> dms_enterprise_20181101_models.CreateUploadOSSFileJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_upload_ossfile_job_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: dms_enterprise_20181101_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: dms_enterprise_20181101_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_lake_house_space_with_options(
        self,
        request: dms_enterprise_20181101_models.DeleteLakeHouseSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteLakeHouseSpaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_id):
            query['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLakeHouseSpace',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteLakeHouseSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_lake_house_space_with_options_async(
        self,
        request: dms_enterprise_20181101_models.DeleteLakeHouseSpaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteLakeHouseSpaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_id):
            query['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLakeHouseSpace',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteLakeHouseSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_lake_house_space(
        self,
        request: dms_enterprise_20181101_models.DeleteLakeHouseSpaceRequest,
    ) -> dms_enterprise_20181101_models.DeleteLakeHouseSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_lake_house_space_with_options(request, runtime)

    async def delete_lake_house_space_async(
        self,
        request: dms_enterprise_20181101_models.DeleteLakeHouseSpaceRequest,
    ) -> dms_enterprise_20181101_models.DeleteLakeHouseSpaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_lake_house_space_with_options_async(request, runtime)

    def delete_lh_members_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.DeleteLhMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteLhMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.DeleteLhMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.member_ids):
            request.member_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.member_ids, 'MemberIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.member_ids_shrink):
            query['MemberIds'] = request.member_ids_shrink
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLhMembers',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteLhMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_lh_members_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.DeleteLhMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteLhMembersResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.DeleteLhMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.member_ids):
            request.member_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.member_ids, 'MemberIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.member_ids_shrink):
            query['MemberIds'] = request.member_ids_shrink
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLhMembers',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteLhMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_lh_members(
        self,
        request: dms_enterprise_20181101_models.DeleteLhMembersRequest,
    ) -> dms_enterprise_20181101_models.DeleteLhMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_lh_members_with_options(request, runtime)

    async def delete_lh_members_async(
        self,
        request: dms_enterprise_20181101_models.DeleteLhMembersRequest,
    ) -> dms_enterprise_20181101_models.DeleteLhMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_lh_members_with_options_async(request, runtime)

    def delete_logic_database_with_options(
        self,
        request: dms_enterprise_20181101_models.DeleteLogicDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteLogicDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logic_db_id):
            query['LogicDbId'] = request.logic_db_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLogicDatabase',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteLogicDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_logic_database_with_options_async(
        self,
        request: dms_enterprise_20181101_models.DeleteLogicDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteLogicDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logic_db_id):
            query['LogicDbId'] = request.logic_db_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLogicDatabase',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteLogicDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_logic_database(
        self,
        request: dms_enterprise_20181101_models.DeleteLogicDatabaseRequest,
    ) -> dms_enterprise_20181101_models.DeleteLogicDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_logic_database_with_options(request, runtime)

    async def delete_logic_database_async(
        self,
        request: dms_enterprise_20181101_models.DeleteLogicDatabaseRequest,
    ) -> dms_enterprise_20181101_models.DeleteLogicDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_logic_database_with_options_async(request, runtime)

    def delete_logic_table_route_config_with_options(
        self,
        request: dms_enterprise_20181101_models.DeleteLogicTableRouteConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteLogicTableRouteConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.route_key):
            query['RouteKey'] = request.route_key
        if not UtilClient.is_unset(request.table_id):
            query['TableId'] = request.table_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLogicTableRouteConfig',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteLogicTableRouteConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_logic_table_route_config_with_options_async(
        self,
        request: dms_enterprise_20181101_models.DeleteLogicTableRouteConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteLogicTableRouteConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.route_key):
            query['RouteKey'] = request.route_key
        if not UtilClient.is_unset(request.table_id):
            query['TableId'] = request.table_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLogicTableRouteConfig',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteLogicTableRouteConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_logic_table_route_config(
        self,
        request: dms_enterprise_20181101_models.DeleteLogicTableRouteConfigRequest,
    ) -> dms_enterprise_20181101_models.DeleteLogicTableRouteConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_logic_table_route_config_with_options(request, runtime)

    async def delete_logic_table_route_config_async(
        self,
        request: dms_enterprise_20181101_models.DeleteLogicTableRouteConfigRequest,
    ) -> dms_enterprise_20181101_models.DeleteLogicTableRouteConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_logic_table_route_config_with_options_async(request, runtime)

    def delete_proxy_with_options(
        self,
        request: dms_enterprise_20181101_models.DeleteProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProxy',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_proxy_with_options_async(
        self,
        request: dms_enterprise_20181101_models.DeleteProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProxy',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_proxy(
        self,
        request: dms_enterprise_20181101_models.DeleteProxyRequest,
    ) -> dms_enterprise_20181101_models.DeleteProxyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_proxy_with_options(request, runtime)

    async def delete_proxy_async(
        self,
        request: dms_enterprise_20181101_models.DeleteProxyRequest,
    ) -> dms_enterprise_20181101_models.DeleteProxyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_proxy_with_options_async(request, runtime)

    def delete_proxy_access_with_options(
        self,
        request: dms_enterprise_20181101_models.DeleteProxyAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteProxyAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.proxy_access_id):
            query['ProxyAccessId'] = request.proxy_access_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProxyAccess',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteProxyAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_proxy_access_with_options_async(
        self,
        request: dms_enterprise_20181101_models.DeleteProxyAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteProxyAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.proxy_access_id):
            query['ProxyAccessId'] = request.proxy_access_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProxyAccess',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteProxyAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_proxy_access(
        self,
        request: dms_enterprise_20181101_models.DeleteProxyAccessRequest,
    ) -> dms_enterprise_20181101_models.DeleteProxyAccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_proxy_access_with_options(request, runtime)

    async def delete_proxy_access_async(
        self,
        request: dms_enterprise_20181101_models.DeleteProxyAccessRequest,
    ) -> dms_enterprise_20181101_models.DeleteProxyAccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_proxy_access_with_options_async(request, runtime)

    def delete_task_flow_with_options(
        self,
        request: dms_enterprise_20181101_models.DeleteTaskFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteTaskFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dag_id):
            query['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTaskFlow',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteTaskFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_task_flow_with_options_async(
        self,
        request: dms_enterprise_20181101_models.DeleteTaskFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteTaskFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dag_id):
            query['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTaskFlow',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteTaskFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_task_flow(
        self,
        request: dms_enterprise_20181101_models.DeleteTaskFlowRequest,
    ) -> dms_enterprise_20181101_models.DeleteTaskFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_task_flow_with_options(request, runtime)

    async def delete_task_flow_async(
        self,
        request: dms_enterprise_20181101_models.DeleteTaskFlowRequest,
    ) -> dms_enterprise_20181101_models.DeleteTaskFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_task_flow_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: dms_enterprise_20181101_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: dms_enterprise_20181101_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableUser',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DisableUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_user_with_options_async(
        self,
        request: dms_enterprise_20181101_models.DisableUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DisableUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableUser',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DisableUserResponse(),
            await self.call_api_async(params, req, runtime)
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

    def edit_logic_database_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.EditLogicDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.EditLogicDatabaseResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.EditLogicDatabaseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.database_ids):
            request.database_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.database_ids, 'DatabaseIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.alias):
            query['Alias'] = request.alias
        if not UtilClient.is_unset(request.database_ids_shrink):
            query['DatabaseIds'] = request.database_ids_shrink
        if not UtilClient.is_unset(request.logic_db_id):
            query['LogicDbId'] = request.logic_db_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditLogicDatabase',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.EditLogicDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_logic_database_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.EditLogicDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.EditLogicDatabaseResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.EditLogicDatabaseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.database_ids):
            request.database_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.database_ids, 'DatabaseIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.alias):
            query['Alias'] = request.alias
        if not UtilClient.is_unset(request.database_ids_shrink):
            query['DatabaseIds'] = request.database_ids_shrink
        if not UtilClient.is_unset(request.logic_db_id):
            query['LogicDbId'] = request.logic_db_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditLogicDatabase',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.EditLogicDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_logic_database(
        self,
        request: dms_enterprise_20181101_models.EditLogicDatabaseRequest,
    ) -> dms_enterprise_20181101_models.EditLogicDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_logic_database_with_options(request, runtime)

    async def edit_logic_database_async(
        self,
        request: dms_enterprise_20181101_models.EditLogicDatabaseRequest,
    ) -> dms_enterprise_20181101_models.EditLogicDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_logic_database_with_options_async(request, runtime)

    def enable_user_with_options(
        self,
        request: dms_enterprise_20181101_models.EnableUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.EnableUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableUser',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.EnableUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_user_with_options_async(
        self,
        request: dms_enterprise_20181101_models.EnableUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.EnableUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableUser',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.EnableUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.action_detail_shrink):
            query['ActionDetail'] = request.action_detail_shrink
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteDataCorrect',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ExecuteDataCorrectResponse(),
            self.call_api(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.action_detail_shrink):
            query['ActionDetail'] = request.action_detail_shrink
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteDataCorrect',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ExecuteDataCorrectResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.action_detail_shrink):
            query['ActionDetail'] = request.action_detail_shrink
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteDataExport',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ExecuteDataExportResponse(),
            self.call_api(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.action_detail_shrink):
            query['ActionDetail'] = request.action_detail_shrink
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteDataExport',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ExecuteDataExportResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.script):
            query['Script'] = request.script
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteScript',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ExecuteScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_script_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ExecuteScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ExecuteScriptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.script):
            query['Script'] = request.script
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteScript',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ExecuteScriptResponse(),
            await self.call_api_async(params, req, runtime)
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

    def execute_struct_sync_with_options(
        self,
        request: dms_enterprise_20181101_models.ExecuteStructSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ExecuteStructSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteStructSync',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ExecuteStructSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_struct_sync_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ExecuteStructSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ExecuteStructSyncResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteStructSync',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ExecuteStructSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_struct_sync(
        self,
        request: dms_enterprise_20181101_models.ExecuteStructSyncRequest,
    ) -> dms_enterprise_20181101_models.ExecuteStructSyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_struct_sync_with_options(request, runtime)

    async def execute_struct_sync_async(
        self,
        request: dms_enterprise_20181101_models.ExecuteStructSyncRequest,
    ) -> dms_enterprise_20181101_models.ExecuteStructSyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_struct_sync_with_options_async(request, runtime)

    def get_approval_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetApprovalDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetApprovalDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workflow_instance_id):
            query['WorkflowInstanceId'] = request.workflow_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApprovalDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetApprovalDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_approval_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetApprovalDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetApprovalDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workflow_instance_id):
            query['WorkflowInstanceId'] = request.workflow_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApprovalDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetApprovalDetailResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_dbtask_sqljob_log_with_options(
        self,
        request: dms_enterprise_20181101_models.GetDBTaskSQLJobLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDBTaskSQLJobLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDBTaskSQLJobLog',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDBTaskSQLJobLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dbtask_sqljob_log_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetDBTaskSQLJobLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDBTaskSQLJobLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDBTaskSQLJobLog',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDBTaskSQLJobLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dbtask_sqljob_log(
        self,
        request: dms_enterprise_20181101_models.GetDBTaskSQLJobLogRequest,
    ) -> dms_enterprise_20181101_models.GetDBTaskSQLJobLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dbtask_sqljob_log_with_options(request, runtime)

    async def get_dbtask_sqljob_log_async(
        self,
        request: dms_enterprise_20181101_models.GetDBTaskSQLJobLogRequest,
    ) -> dms_enterprise_20181101_models.GetDBTaskSQLJobLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dbtask_sqljob_log_with_options_async(request, runtime)

    def get_dbtopology_with_options(
        self,
        request: dms_enterprise_20181101_models.GetDBTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDBTopologyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logic_db_id):
            query['LogicDbId'] = request.logic_db_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDBTopology',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDBTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dbtopology_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetDBTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDBTopologyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logic_db_id):
            query['LogicDbId'] = request.logic_db_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDBTopology',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDBTopologyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dbtopology(
        self,
        request: dms_enterprise_20181101_models.GetDBTopologyRequest,
    ) -> dms_enterprise_20181101_models.GetDBTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dbtopology_with_options(request, runtime)

    async def get_dbtopology_async(
        self,
        request: dms_enterprise_20181101_models.GetDBTopologyRequest,
    ) -> dms_enterprise_20181101_models.GetDBTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dbtopology_with_options_async(request, runtime)

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
        query = {}
        if not UtilClient.is_unset(request.action_detail_shrink):
            query['ActionDetail'] = request.action_detail_shrink
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataCorrectBackupFiles',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCorrectBackupFilesResponse(),
            self.call_api(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.action_detail_shrink):
            query['ActionDetail'] = request.action_detail_shrink
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataCorrectBackupFiles',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCorrectBackupFilesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataCorrectOrderDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCorrectOrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_correct_order_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCorrectOrderDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataCorrectOrderDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCorrectOrderDetailResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_data_correct_sqlfile_with_options(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectSQLFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCorrectSQLFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataCorrectSQLFile',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCorrectSQLFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_correct_sqlfile_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectSQLFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCorrectSQLFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataCorrectSQLFile',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCorrectSQLFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_correct_sqlfile(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectSQLFileRequest,
    ) -> dms_enterprise_20181101_models.GetDataCorrectSQLFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_correct_sqlfile_with_options(request, runtime)

    async def get_data_correct_sqlfile_async(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectSQLFileRequest,
    ) -> dms_enterprise_20181101_models.GetDataCorrectSQLFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_correct_sqlfile_with_options_async(request, runtime)

    def get_data_correct_task_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCorrectTaskDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataCorrectTaskDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCorrectTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_correct_task_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCorrectTaskDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataCorrectTaskDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCorrectTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_correct_task_detail(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectTaskDetailRequest,
    ) -> dms_enterprise_20181101_models.GetDataCorrectTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_correct_task_detail_with_options(request, runtime)

    async def get_data_correct_task_detail_async(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectTaskDetailRequest,
    ) -> dms_enterprise_20181101_models.GetDataCorrectTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_correct_task_detail_with_options_async(request, runtime)

    def get_data_cron_clear_task_detail_list_with_options(
        self,
        request: dms_enterprise_20181101_models.GetDataCronClearTaskDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCronClearTaskDetailListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataCronClearTaskDetailList',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCronClearTaskDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_cron_clear_task_detail_list_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetDataCronClearTaskDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCronClearTaskDetailListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataCronClearTaskDetailList',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCronClearTaskDetailListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_cron_clear_task_detail_list(
        self,
        request: dms_enterprise_20181101_models.GetDataCronClearTaskDetailListRequest,
    ) -> dms_enterprise_20181101_models.GetDataCronClearTaskDetailListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_cron_clear_task_detail_list_with_options(request, runtime)

    async def get_data_cron_clear_task_detail_list_async(
        self,
        request: dms_enterprise_20181101_models.GetDataCronClearTaskDetailListRequest,
    ) -> dms_enterprise_20181101_models.GetDataCronClearTaskDetailListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_cron_clear_task_detail_list_with_options_async(request, runtime)

    def get_data_export_download_urlwith_options(
        self,
        request: dms_enterprise_20181101_models.GetDataExportDownloadURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataExportDownloadURLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataExportDownloadURL',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataExportDownloadURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_export_download_urlwith_options_async(
        self,
        request: dms_enterprise_20181101_models.GetDataExportDownloadURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataExportDownloadURLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataExportDownloadURL',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataExportDownloadURLResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        body = {}
        if not UtilClient.is_unset(request.order_id):
            body['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataExportOrderDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataExportOrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_export_order_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetDataExportOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataExportOrderDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        body = {}
        if not UtilClient.is_unset(request.order_id):
            body['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataExportOrderDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataExportOrderDetailResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_database_with_options(
        self,
        request: dms_enterprise_20181101_models.GetDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatabase',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_database_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDatabase',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_instance_with_options(
        self,
        request: dms_enterprise_20181101_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_lh_space_by_name_with_options(
        self,
        request: dms_enterprise_20181101_models.GetLhSpaceByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetLhSpaceByNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_name):
            query['SpaceName'] = request.space_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLhSpaceByName',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetLhSpaceByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lh_space_by_name_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetLhSpaceByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetLhSpaceByNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_name):
            query['SpaceName'] = request.space_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLhSpaceByName',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetLhSpaceByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lh_space_by_name(
        self,
        request: dms_enterprise_20181101_models.GetLhSpaceByNameRequest,
    ) -> dms_enterprise_20181101_models.GetLhSpaceByNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_lh_space_by_name_with_options(request, runtime)

    async def get_lh_space_by_name_async(
        self,
        request: dms_enterprise_20181101_models.GetLhSpaceByNameRequest,
    ) -> dms_enterprise_20181101_models.GetLhSpaceByNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_lh_space_by_name_with_options_async(request, runtime)

    def get_logic_database_with_options(
        self,
        request: dms_enterprise_20181101_models.GetLogicDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetLogicDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLogicDatabase',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetLogicDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_logic_database_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetLogicDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetLogicDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLogicDatabase',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetLogicDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaTableColumn',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetMetaTableColumnResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_meta_table_column_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetMetaTableColumnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetMetaTableColumnResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaTableColumn',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetMetaTableColumnResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaTableDetailInfo',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetMetaTableDetailInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_meta_table_detail_info_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetMetaTableDetailInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetMetaTableDetailInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMetaTableDetailInfo',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetMetaTableDetailInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.module):
            query['Module'] = request.module
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOpLog',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetOpLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_op_log_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetOpLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetOpLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.module):
            query['Module'] = request.module
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOpLog',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetOpLogResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrderBaseInfo',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetOrderBaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_order_base_info_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetOrderBaseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetOrderBaseInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrderBaseInfo',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetOrderBaseInfoResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_owner_apply_order_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetOwnerApplyOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetOwnerApplyOrderDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOwnerApplyOrderDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetOwnerApplyOrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_owner_apply_order_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetOwnerApplyOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetOwnerApplyOrderDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOwnerApplyOrderDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetOwnerApplyOrderDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_owner_apply_order_detail(
        self,
        request: dms_enterprise_20181101_models.GetOwnerApplyOrderDetailRequest,
    ) -> dms_enterprise_20181101_models.GetOwnerApplyOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_owner_apply_order_detail_with_options(request, runtime)

    async def get_owner_apply_order_detail_async(
        self,
        request: dms_enterprise_20181101_models.GetOwnerApplyOrderDetailRequest,
    ) -> dms_enterprise_20181101_models.GetOwnerApplyOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_owner_apply_order_detail_with_options_async(request, runtime)

    def get_perm_apply_order_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetPermApplyOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetPermApplyOrderDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPermApplyOrderDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetPermApplyOrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_perm_apply_order_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetPermApplyOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetPermApplyOrderDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPermApplyOrderDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetPermApplyOrderDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_perm_apply_order_detail(
        self,
        request: dms_enterprise_20181101_models.GetPermApplyOrderDetailRequest,
    ) -> dms_enterprise_20181101_models.GetPermApplyOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_perm_apply_order_detail_with_options(request, runtime)

    async def get_perm_apply_order_detail_async(
        self,
        request: dms_enterprise_20181101_models.GetPermApplyOrderDetailRequest,
    ) -> dms_enterprise_20181101_models.GetPermApplyOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_perm_apply_order_detail_with_options_async(request, runtime)

    def get_physical_database_with_options(
        self,
        request: dms_enterprise_20181101_models.GetPhysicalDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetPhysicalDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalDatabase',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetPhysicalDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_physical_database_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetPhysicalDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetPhysicalDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalDatabase',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetPhysicalDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_physical_database(
        self,
        request: dms_enterprise_20181101_models.GetPhysicalDatabaseRequest,
    ) -> dms_enterprise_20181101_models.GetPhysicalDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_physical_database_with_options(request, runtime)

    async def get_physical_database_async(
        self,
        request: dms_enterprise_20181101_models.GetPhysicalDatabaseRequest,
    ) -> dms_enterprise_20181101_models.GetPhysicalDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_physical_database_with_options_async(request, runtime)

    def get_proxy_with_options(
        self,
        request: dms_enterprise_20181101_models.GetProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProxy',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_proxy_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProxy',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_proxy(
        self,
        request: dms_enterprise_20181101_models.GetProxyRequest,
    ) -> dms_enterprise_20181101_models.GetProxyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_proxy_with_options(request, runtime)

    async def get_proxy_async(
        self,
        request: dms_enterprise_20181101_models.GetProxyRequest,
    ) -> dms_enterprise_20181101_models.GetProxyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_proxy_with_options_async(request, runtime)

    def get_sqlreview_check_result_status_with_options(
        self,
        request: dms_enterprise_20181101_models.GetSQLReviewCheckResultStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetSQLReviewCheckResultStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSQLReviewCheckResultStatus',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetSQLReviewCheckResultStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sqlreview_check_result_status_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetSQLReviewCheckResultStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetSQLReviewCheckResultStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSQLReviewCheckResultStatus',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetSQLReviewCheckResultStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sqlreview_check_result_status(
        self,
        request: dms_enterprise_20181101_models.GetSQLReviewCheckResultStatusRequest,
    ) -> dms_enterprise_20181101_models.GetSQLReviewCheckResultStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sqlreview_check_result_status_with_options(request, runtime)

    async def get_sqlreview_check_result_status_async(
        self,
        request: dms_enterprise_20181101_models.GetSQLReviewCheckResultStatusRequest,
    ) -> dms_enterprise_20181101_models.GetSQLReviewCheckResultStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sqlreview_check_result_status_with_options_async(request, runtime)

    def get_sqlreview_optimize_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetSQLReviewOptimizeDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetSQLReviewOptimizeDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sqlreview_query_key):
            query['SQLReviewQueryKey'] = request.sqlreview_query_key
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSQLReviewOptimizeDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetSQLReviewOptimizeDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sqlreview_optimize_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetSQLReviewOptimizeDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetSQLReviewOptimizeDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sqlreview_query_key):
            query['SQLReviewQueryKey'] = request.sqlreview_query_key
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSQLReviewOptimizeDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetSQLReviewOptimizeDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sqlreview_optimize_detail(
        self,
        request: dms_enterprise_20181101_models.GetSQLReviewOptimizeDetailRequest,
    ) -> dms_enterprise_20181101_models.GetSQLReviewOptimizeDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sqlreview_optimize_detail_with_options(request, runtime)

    async def get_sqlreview_optimize_detail_async(
        self,
        request: dms_enterprise_20181101_models.GetSQLReviewOptimizeDetailRequest,
    ) -> dms_enterprise_20181101_models.GetSQLReviewOptimizeDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sqlreview_optimize_detail_with_options_async(request, runtime)

    def get_struct_sync_exec_sql_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncExecSqlDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetStructSyncExecSqlDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStructSyncExecSqlDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetStructSyncExecSqlDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_struct_sync_exec_sql_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncExecSqlDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetStructSyncExecSqlDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStructSyncExecSqlDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetStructSyncExecSqlDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_struct_sync_exec_sql_detail(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncExecSqlDetailRequest,
    ) -> dms_enterprise_20181101_models.GetStructSyncExecSqlDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_struct_sync_exec_sql_detail_with_options(request, runtime)

    async def get_struct_sync_exec_sql_detail_async(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncExecSqlDetailRequest,
    ) -> dms_enterprise_20181101_models.GetStructSyncExecSqlDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_struct_sync_exec_sql_detail_with_options_async(request, runtime)

    def get_struct_sync_job_analyze_result_with_options(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncJobAnalyzeResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetStructSyncJobAnalyzeResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compare_type):
            query['CompareType'] = request.compare_type
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStructSyncJobAnalyzeResult',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetStructSyncJobAnalyzeResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_struct_sync_job_analyze_result_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncJobAnalyzeResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetStructSyncJobAnalyzeResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compare_type):
            query['CompareType'] = request.compare_type
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStructSyncJobAnalyzeResult',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetStructSyncJobAnalyzeResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_struct_sync_job_analyze_result(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncJobAnalyzeResultRequest,
    ) -> dms_enterprise_20181101_models.GetStructSyncJobAnalyzeResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_struct_sync_job_analyze_result_with_options(request, runtime)

    async def get_struct_sync_job_analyze_result_async(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncJobAnalyzeResultRequest,
    ) -> dms_enterprise_20181101_models.GetStructSyncJobAnalyzeResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_struct_sync_job_analyze_result_with_options_async(request, runtime)

    def get_struct_sync_job_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetStructSyncJobDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStructSyncJobDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetStructSyncJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_struct_sync_job_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetStructSyncJobDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStructSyncJobDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetStructSyncJobDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_struct_sync_job_detail(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncJobDetailRequest,
    ) -> dms_enterprise_20181101_models.GetStructSyncJobDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_struct_sync_job_detail_with_options(request, runtime)

    async def get_struct_sync_job_detail_async(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncJobDetailRequest,
    ) -> dms_enterprise_20181101_models.GetStructSyncJobDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_struct_sync_job_detail_with_options_async(request, runtime)

    def get_struct_sync_order_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetStructSyncOrderDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStructSyncOrderDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetStructSyncOrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_struct_sync_order_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetStructSyncOrderDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStructSyncOrderDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetStructSyncOrderDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_struct_sync_order_detail(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncOrderDetailRequest,
    ) -> dms_enterprise_20181101_models.GetStructSyncOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_struct_sync_order_detail_with_options(request, runtime)

    async def get_struct_sync_order_detail_async(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncOrderDetailRequest,
    ) -> dms_enterprise_20181101_models.GetStructSyncOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_struct_sync_order_detail_with_options_async(request, runtime)

    def get_table_dbtopology_with_options(
        self,
        request: dms_enterprise_20181101_models.GetTableDBTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetTableDBTopologyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableDBTopology',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetTableDBTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_dbtopology_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetTableDBTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetTableDBTopologyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableDBTopology',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetTableDBTopologyResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_table_topology_with_options(
        self,
        request: dms_enterprise_20181101_models.GetTableTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetTableTopologyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableTopology',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetTableTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_topology_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetTableTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetTableTopologyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_guid):
            query['TableGuid'] = request.table_guid
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableTopology',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetTableTopologyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_topology(
        self,
        request: dms_enterprise_20181101_models.GetTableTopologyRequest,
    ) -> dms_enterprise_20181101_models.GetTableTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_table_topology_with_options(request, runtime)

    async def get_table_topology_async(
        self,
        request: dms_enterprise_20181101_models.GetTableTopologyRequest,
    ) -> dms_enterprise_20181101_models.GetTableTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_table_topology_with_options_async(request, runtime)

    def get_task_instance_relation_with_options(
        self,
        request: dms_enterprise_20181101_models.GetTaskInstanceRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetTaskInstanceRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dag_id):
            query['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.dag_instance_id):
            query['DagInstanceId'] = request.dag_instance_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskInstanceRelation',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetTaskInstanceRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_instance_relation_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetTaskInstanceRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetTaskInstanceRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dag_id):
            query['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.dag_instance_id):
            query['DagInstanceId'] = request.dag_instance_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskInstanceRelation',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetTaskInstanceRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_instance_relation(
        self,
        request: dms_enterprise_20181101_models.GetTaskInstanceRelationRequest,
    ) -> dms_enterprise_20181101_models.GetTaskInstanceRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_instance_relation_with_options(request, runtime)

    async def get_task_instance_relation_async(
        self,
        request: dms_enterprise_20181101_models.GetTaskInstanceRelationRequest,
    ) -> dms_enterprise_20181101_models.GetTaskInstanceRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_instance_relation_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: dms_enterprise_20181101_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        request: dms_enterprise_20181101_models.GetUserActiveTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetUserActiveTenantResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserActiveTenant',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetUserActiveTenantResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_active_tenant_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetUserActiveTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetUserActiveTenantResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserActiveTenant',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetUserActiveTenantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_active_tenant(
        self,
        request: dms_enterprise_20181101_models.GetUserActiveTenantRequest,
    ) -> dms_enterprise_20181101_models.GetUserActiveTenantResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_active_tenant_with_options(request, runtime)

    async def get_user_active_tenant_async(
        self,
        request: dms_enterprise_20181101_models.GetUserActiveTenantRequest,
    ) -> dms_enterprise_20181101_models.GetUserActiveTenantResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_active_tenant_with_options_async(request, runtime)

    def get_user_upload_file_job_with_options(
        self,
        request: dms_enterprise_20181101_models.GetUserUploadFileJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetUserUploadFileJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_key):
            query['JobKey'] = request.job_key
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserUploadFileJob',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetUserUploadFileJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_upload_file_job_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetUserUploadFileJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetUserUploadFileJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_key):
            query['JobKey'] = request.job_key
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserUploadFileJob',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetUserUploadFileJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_upload_file_job(
        self,
        request: dms_enterprise_20181101_models.GetUserUploadFileJobRequest,
    ) -> dms_enterprise_20181101_models.GetUserUploadFileJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_upload_file_job_with_options(request, runtime)

    async def get_user_upload_file_job_async(
        self,
        request: dms_enterprise_20181101_models.GetUserUploadFileJobRequest,
    ) -> dms_enterprise_20181101_models.GetUserUploadFileJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_upload_file_job_with_options_async(request, runtime)

    def grant_user_permission_with_options(
        self,
        request: dms_enterprise_20181101_models.GrantUserPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GrantUserPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.ds_type):
            query['DsType'] = request.ds_type
        if not UtilClient.is_unset(request.expire_date):
            query['ExpireDate'] = request.expire_date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.perm_types):
            query['PermTypes'] = request.perm_types
        if not UtilClient.is_unset(request.table_id):
            query['TableId'] = request.table_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantUserPermission',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GrantUserPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_user_permission_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GrantUserPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GrantUserPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.ds_type):
            query['DsType'] = request.ds_type
        if not UtilClient.is_unset(request.expire_date):
            query['ExpireDate'] = request.expire_date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.perm_types):
            query['PermTypes'] = request.perm_types
        if not UtilClient.is_unset(request.table_id):
            query['TableId'] = request.table_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantUserPermission',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GrantUserPermissionResponse(),
            await self.call_api_async(params, req, runtime)
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

    def inspect_proxy_access_secret_with_options(
        self,
        request: dms_enterprise_20181101_models.InspectProxyAccessSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.InspectProxyAccessSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.proxy_access_id):
            query['ProxyAccessId'] = request.proxy_access_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InspectProxyAccessSecret',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.InspectProxyAccessSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def inspect_proxy_access_secret_with_options_async(
        self,
        request: dms_enterprise_20181101_models.InspectProxyAccessSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.InspectProxyAccessSecretResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.proxy_access_id):
            query['ProxyAccessId'] = request.proxy_access_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InspectProxyAccessSecret',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.InspectProxyAccessSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def inspect_proxy_access_secret(
        self,
        request: dms_enterprise_20181101_models.InspectProxyAccessSecretRequest,
    ) -> dms_enterprise_20181101_models.InspectProxyAccessSecretResponse:
        runtime = util_models.RuntimeOptions()
        return self.inspect_proxy_access_secret_with_options(request, runtime)

    async def inspect_proxy_access_secret_async(
        self,
        request: dms_enterprise_20181101_models.InspectProxyAccessSecretRequest,
    ) -> dms_enterprise_20181101_models.InspectProxyAccessSecretResponse:
        runtime = util_models.RuntimeOptions()
        return await self.inspect_proxy_access_secret_with_options_async(request, runtime)

    def list_columns_with_options(
        self,
        request: dms_enterprise_20181101_models.ListColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListColumnsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.table_id):
            query['TableId'] = request.table_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListColumns',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_columns_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListColumnsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.table_id):
            query['TableId'] = request.table_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListColumns',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListColumnsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_dbtask_sqljob_with_options(
        self,
        request: dms_enterprise_20181101_models.ListDBTaskSQLJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDBTaskSQLJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbtask_group_id):
            query['DBTaskGroupId'] = request.dbtask_group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDBTaskSQLJob',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDBTaskSQLJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dbtask_sqljob_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListDBTaskSQLJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDBTaskSQLJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbtask_group_id):
            query['DBTaskGroupId'] = request.dbtask_group_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDBTaskSQLJob',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDBTaskSQLJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dbtask_sqljob(
        self,
        request: dms_enterprise_20181101_models.ListDBTaskSQLJobRequest,
    ) -> dms_enterprise_20181101_models.ListDBTaskSQLJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dbtask_sqljob_with_options(request, runtime)

    async def list_dbtask_sqljob_async(
        self,
        request: dms_enterprise_20181101_models.ListDBTaskSQLJobRequest,
    ) -> dms_enterprise_20181101_models.ListDBTaskSQLJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dbtask_sqljob_with_options_async(request, runtime)

    def list_dbtask_sqljob_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.ListDBTaskSQLJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDBTaskSQLJobDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDBTaskSQLJobDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDBTaskSQLJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dbtask_sqljob_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListDBTaskSQLJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDBTaskSQLJobDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDBTaskSQLJobDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDBTaskSQLJobDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dbtask_sqljob_detail(
        self,
        request: dms_enterprise_20181101_models.ListDBTaskSQLJobDetailRequest,
    ) -> dms_enterprise_20181101_models.ListDBTaskSQLJobDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dbtask_sqljob_detail_with_options(request, runtime)

    async def list_dbtask_sqljob_detail_async(
        self,
        request: dms_enterprise_20181101_models.ListDBTaskSQLJobDetailRequest,
    ) -> dms_enterprise_20181101_models.ListDBTaskSQLJobDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dbtask_sqljob_detail_with_options_async(request, runtime)

    def list_ddlpublish_records_with_options(
        self,
        request: dms_enterprise_20181101_models.ListDDLPublishRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDDLPublishRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDDLPublishRecords',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDDLPublishRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ddlpublish_records_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListDDLPublishRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDDLPublishRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDDLPublishRecords',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDDLPublishRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ddlpublish_records(
        self,
        request: dms_enterprise_20181101_models.ListDDLPublishRecordsRequest,
    ) -> dms_enterprise_20181101_models.ListDDLPublishRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ddlpublish_records_with_options(request, runtime)

    async def list_ddlpublish_records_async(
        self,
        request: dms_enterprise_20181101_models.ListDDLPublishRecordsRequest,
    ) -> dms_enterprise_20181101_models.ListDDLPublishRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ddlpublish_records_with_options_async(request, runtime)

    def list_data_correct_pre_check_dbwith_options(
        self,
        request: dms_enterprise_20181101_models.ListDataCorrectPreCheckDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDataCorrectPreCheckDBResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataCorrectPreCheckDB',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDataCorrectPreCheckDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_correct_pre_check_dbwith_options_async(
        self,
        request: dms_enterprise_20181101_models.ListDataCorrectPreCheckDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDataCorrectPreCheckDBResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataCorrectPreCheckDB',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDataCorrectPreCheckDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_correct_pre_check_db(
        self,
        request: dms_enterprise_20181101_models.ListDataCorrectPreCheckDBRequest,
    ) -> dms_enterprise_20181101_models.ListDataCorrectPreCheckDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_correct_pre_check_dbwith_options(request, runtime)

    async def list_data_correct_pre_check_db_async(
        self,
        request: dms_enterprise_20181101_models.ListDataCorrectPreCheckDBRequest,
    ) -> dms_enterprise_20181101_models.ListDataCorrectPreCheckDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_correct_pre_check_dbwith_options_async(request, runtime)

    def list_data_correct_pre_check_sqlwith_options(
        self,
        request: dms_enterprise_20181101_models.ListDataCorrectPreCheckSQLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDataCorrectPreCheckSQLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataCorrectPreCheckSQL',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDataCorrectPreCheckSQLResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_correct_pre_check_sqlwith_options_async(
        self,
        request: dms_enterprise_20181101_models.ListDataCorrectPreCheckSQLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDataCorrectPreCheckSQLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataCorrectPreCheckSQL',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDataCorrectPreCheckSQLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_correct_pre_check_sql(
        self,
        request: dms_enterprise_20181101_models.ListDataCorrectPreCheckSQLRequest,
    ) -> dms_enterprise_20181101_models.ListDataCorrectPreCheckSQLResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_correct_pre_check_sqlwith_options(request, runtime)

    async def list_data_correct_pre_check_sql_async(
        self,
        request: dms_enterprise_20181101_models.ListDataCorrectPreCheckSQLRequest,
    ) -> dms_enterprise_20181101_models.ListDataCorrectPreCheckSQLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_correct_pre_check_sqlwith_options_async(request, runtime)

    def list_database_user_permssions_with_options(
        self,
        request: dms_enterprise_20181101_models.ListDatabaseUserPermssionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDatabaseUserPermssionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.perm_type):
            query['PermType'] = request.perm_type
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabaseUserPermssions',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDatabaseUserPermssionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_database_user_permssions_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListDatabaseUserPermssionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDatabaseUserPermssionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.perm_type):
            query['PermType'] = request.perm_type
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabaseUserPermssions',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDatabaseUserPermssionsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_databases_with_options(
        self,
        request: dms_enterprise_20181101_models.ListDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDatabasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabases',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_databases_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDatabasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatabases',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_indexes_with_options(
        self,
        request: dms_enterprise_20181101_models.ListIndexesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListIndexesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.table_id):
            query['TableId'] = request.table_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIndexes',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListIndexesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_indexes_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListIndexesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListIndexesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.table_id):
            query['TableId'] = request.table_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIndexes',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListIndexesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_instance_login_audit_log_with_options(
        self,
        request: dms_enterprise_20181101_models.ListInstanceLoginAuditLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListInstanceLoginAuditLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.op_user_name):
            query['OpUserName'] = request.op_user_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceLoginAuditLog',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListInstanceLoginAuditLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_login_audit_log_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListInstanceLoginAuditLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListInstanceLoginAuditLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.op_user_name):
            query['OpUserName'] = request.op_user_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceLoginAuditLog',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListInstanceLoginAuditLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_login_audit_log(
        self,
        request: dms_enterprise_20181101_models.ListInstanceLoginAuditLogRequest,
    ) -> dms_enterprise_20181101_models.ListInstanceLoginAuditLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instance_login_audit_log_with_options(request, runtime)

    async def list_instance_login_audit_log_async(
        self,
        request: dms_enterprise_20181101_models.ListInstanceLoginAuditLogRequest,
    ) -> dms_enterprise_20181101_models.ListInstanceLoginAuditLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_login_audit_log_with_options_async(request, runtime)

    def list_instance_user_permissions_with_options(
        self,
        request: dms_enterprise_20181101_models.ListInstanceUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListInstanceUserPermissionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceUserPermissions',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListInstanceUserPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_user_permissions_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListInstanceUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListInstanceUserPermissionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceUserPermissions',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListInstanceUserPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_user_permissions(
        self,
        request: dms_enterprise_20181101_models.ListInstanceUserPermissionsRequest,
    ) -> dms_enterprise_20181101_models.ListInstanceUserPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instance_user_permissions_with_options(request, runtime)

    async def list_instance_user_permissions_async(
        self,
        request: dms_enterprise_20181101_models.ListInstanceUserPermissionsRequest,
    ) -> dms_enterprise_20181101_models.ListInstanceUserPermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_user_permissions_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: dms_enterprise_20181101_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.instance_source):
            query['InstanceSource'] = request.instance_source
        if not UtilClient.is_unset(request.instance_state):
            query['InstanceState'] = request.instance_state
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.instance_source):
            query['InstanceSource'] = request.instance_source
        if not UtilClient.is_unset(request.instance_state):
            query['InstanceState'] = request.instance_state
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_lh_task_flow_and_scenario_with_options(
        self,
        request: dms_enterprise_20181101_models.ListLhTaskFlowAndScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListLhTaskFlowAndScenarioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_id):
            query['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLhTaskFlowAndScenario',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListLhTaskFlowAndScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_lh_task_flow_and_scenario_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListLhTaskFlowAndScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListLhTaskFlowAndScenarioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.space_id):
            query['SpaceId'] = request.space_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLhTaskFlowAndScenario',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListLhTaskFlowAndScenarioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_lh_task_flow_and_scenario(
        self,
        request: dms_enterprise_20181101_models.ListLhTaskFlowAndScenarioRequest,
    ) -> dms_enterprise_20181101_models.ListLhTaskFlowAndScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_lh_task_flow_and_scenario_with_options(request, runtime)

    async def list_lh_task_flow_and_scenario_async(
        self,
        request: dms_enterprise_20181101_models.ListLhTaskFlowAndScenarioRequest,
    ) -> dms_enterprise_20181101_models.ListLhTaskFlowAndScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_lh_task_flow_and_scenario_with_options_async(request, runtime)

    def list_logic_databases_with_options(
        self,
        request: dms_enterprise_20181101_models.ListLogicDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListLogicDatabasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogicDatabases',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListLogicDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_logic_databases_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListLogicDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListLogicDatabasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogicDatabases',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListLogicDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_logic_table_route_config_with_options(
        self,
        request: dms_enterprise_20181101_models.ListLogicTableRouteConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListLogicTableRouteConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_id):
            query['TableId'] = request.table_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogicTableRouteConfig',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListLogicTableRouteConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_logic_table_route_config_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListLogicTableRouteConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListLogicTableRouteConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_id):
            query['TableId'] = request.table_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogicTableRouteConfig',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListLogicTableRouteConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_logic_table_route_config(
        self,
        request: dms_enterprise_20181101_models.ListLogicTableRouteConfigRequest,
    ) -> dms_enterprise_20181101_models.ListLogicTableRouteConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_logic_table_route_config_with_options(request, runtime)

    async def list_logic_table_route_config_async(
        self,
        request: dms_enterprise_20181101_models.ListLogicTableRouteConfigRequest,
    ) -> dms_enterprise_20181101_models.ListLogicTableRouteConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_logic_table_route_config_with_options_async(request, runtime)

    def list_logic_tables_with_options(
        self,
        request: dms_enterprise_20181101_models.ListLogicTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListLogicTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.return_guid):
            query['ReturnGuid'] = request.return_guid
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogicTables',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListLogicTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_logic_tables_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListLogicTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListLogicTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.return_guid):
            query['ReturnGuid'] = request.return_guid
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogicTables',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListLogicTablesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order_result_type):
            query['OrderResultType'] = request.order_result_type
        if not UtilClient.is_unset(request.order_status):
            query['OrderStatus'] = request.order_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.plugin_type):
            query['PluginType'] = request.plugin_type
        if not UtilClient.is_unset(request.search_content):
            query['SearchContent'] = request.search_content
        if not UtilClient.is_unset(request.search_date_type):
            query['SearchDateType'] = request.search_date_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrders',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_orders_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order_result_type):
            query['OrderResultType'] = request.order_result_type
        if not UtilClient.is_unset(request.order_status):
            query['OrderStatus'] = request.order_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.plugin_type):
            query['PluginType'] = request.plugin_type
        if not UtilClient.is_unset(request.search_content):
            query['SearchContent'] = request.search_content
        if not UtilClient.is_unset(request.search_date_type):
            query['SearchDateType'] = request.search_date_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrders',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListOrdersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_proxies_with_options(
        self,
        request: dms_enterprise_20181101_models.ListProxiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListProxiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProxies',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListProxiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_proxies_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListProxiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListProxiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProxies',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListProxiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_proxies(
        self,
        request: dms_enterprise_20181101_models.ListProxiesRequest,
    ) -> dms_enterprise_20181101_models.ListProxiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_proxies_with_options(request, runtime)

    async def list_proxies_async(
        self,
        request: dms_enterprise_20181101_models.ListProxiesRequest,
    ) -> dms_enterprise_20181101_models.ListProxiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_proxies_with_options_async(request, runtime)

    def list_proxy_accesses_with_options(
        self,
        request: dms_enterprise_20181101_models.ListProxyAccessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListProxyAccessesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProxyAccesses',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListProxyAccessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_proxy_accesses_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListProxyAccessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListProxyAccessesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.proxy_id):
            query['ProxyId'] = request.proxy_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProxyAccesses',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListProxyAccessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_proxy_accesses(
        self,
        request: dms_enterprise_20181101_models.ListProxyAccessesRequest,
    ) -> dms_enterprise_20181101_models.ListProxyAccessesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_proxy_accesses_with_options(request, runtime)

    async def list_proxy_accesses_async(
        self,
        request: dms_enterprise_20181101_models.ListProxyAccessesRequest,
    ) -> dms_enterprise_20181101_models.ListProxyAccessesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_proxy_accesses_with_options_async(request, runtime)

    def list_proxy_sqlexec_audit_log_with_options(
        self,
        request: dms_enterprise_20181101_models.ListProxySQLExecAuditLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListProxySQLExecAuditLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.exec_state):
            query['ExecState'] = request.exec_state
        if not UtilClient.is_unset(request.op_user_name):
            query['OpUserName'] = request.op_user_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqltype):
            query['SQLType'] = request.sqltype
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProxySQLExecAuditLog',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListProxySQLExecAuditLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_proxy_sqlexec_audit_log_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListProxySQLExecAuditLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListProxySQLExecAuditLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.exec_state):
            query['ExecState'] = request.exec_state
        if not UtilClient.is_unset(request.op_user_name):
            query['OpUserName'] = request.op_user_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sqltype):
            query['SQLType'] = request.sqltype
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProxySQLExecAuditLog',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListProxySQLExecAuditLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_proxy_sqlexec_audit_log(
        self,
        request: dms_enterprise_20181101_models.ListProxySQLExecAuditLogRequest,
    ) -> dms_enterprise_20181101_models.ListProxySQLExecAuditLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_proxy_sqlexec_audit_log_with_options(request, runtime)

    async def list_proxy_sqlexec_audit_log_async(
        self,
        request: dms_enterprise_20181101_models.ListProxySQLExecAuditLogRequest,
    ) -> dms_enterprise_20181101_models.ListProxySQLExecAuditLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_proxy_sqlexec_audit_log_with_options_async(request, runtime)

    def list_sqlexec_audit_log_with_options(
        self,
        request: dms_enterprise_20181101_models.ListSQLExecAuditLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListSQLExecAuditLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.exec_state):
            query['ExecState'] = request.exec_state
        if not UtilClient.is_unset(request.op_user_name):
            query['OpUserName'] = request.op_user_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.sql_type):
            query['SqlType'] = request.sql_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSQLExecAuditLog',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListSQLExecAuditLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sqlexec_audit_log_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListSQLExecAuditLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListSQLExecAuditLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.exec_state):
            query['ExecState'] = request.exec_state
        if not UtilClient.is_unset(request.op_user_name):
            query['OpUserName'] = request.op_user_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.sql_type):
            query['SqlType'] = request.sql_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSQLExecAuditLog',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListSQLExecAuditLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sqlexec_audit_log(
        self,
        request: dms_enterprise_20181101_models.ListSQLExecAuditLogRequest,
    ) -> dms_enterprise_20181101_models.ListSQLExecAuditLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sqlexec_audit_log_with_options(request, runtime)

    async def list_sqlexec_audit_log_async(
        self,
        request: dms_enterprise_20181101_models.ListSQLExecAuditLogRequest,
    ) -> dms_enterprise_20181101_models.ListSQLExecAuditLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sqlexec_audit_log_with_options_async(request, runtime)

    def list_sqlreview_origin_sqlwith_options(
        self,
        tmp_req: dms_enterprise_20181101_models.ListSQLReviewOriginSQLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListSQLReviewOriginSQLResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.ListSQLReviewOriginSQLShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_action_detail):
            request.order_action_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.order_action_detail), 'OrderActionDetail', 'json')
        query = {}
        if not UtilClient.is_unset(request.order_action_detail_shrink):
            query['OrderActionDetail'] = request.order_action_detail_shrink
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSQLReviewOriginSQL',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListSQLReviewOriginSQLResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sqlreview_origin_sqlwith_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.ListSQLReviewOriginSQLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListSQLReviewOriginSQLResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.ListSQLReviewOriginSQLShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_action_detail):
            request.order_action_detail_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.order_action_detail), 'OrderActionDetail', 'json')
        query = {}
        if not UtilClient.is_unset(request.order_action_detail_shrink):
            query['OrderActionDetail'] = request.order_action_detail_shrink
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSQLReviewOriginSQL',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListSQLReviewOriginSQLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sqlreview_origin_sql(
        self,
        request: dms_enterprise_20181101_models.ListSQLReviewOriginSQLRequest,
    ) -> dms_enterprise_20181101_models.ListSQLReviewOriginSQLResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sqlreview_origin_sqlwith_options(request, runtime)

    async def list_sqlreview_origin_sql_async(
        self,
        request: dms_enterprise_20181101_models.ListSQLReviewOriginSQLRequest,
    ) -> dms_enterprise_20181101_models.ListSQLReviewOriginSQLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sqlreview_origin_sqlwith_options_async(request, runtime)

    def list_sensitive_columns_with_options(
        self,
        request: dms_enterprise_20181101_models.ListSensitiveColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListSensitiveColumnsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.column_name):
            query['ColumnName'] = request.column_name
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.security_level):
            query['SecurityLevel'] = request.security_level
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSensitiveColumns',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListSensitiveColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sensitive_columns_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListSensitiveColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListSensitiveColumnsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.column_name):
            query['ColumnName'] = request.column_name
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.security_level):
            query['SecurityLevel'] = request.security_level
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSensitiveColumns',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListSensitiveColumnsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.column_name):
            query['ColumnName'] = request.column_name
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSensitiveColumnsDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListSensitiveColumnsDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sensitive_columns_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListSensitiveColumnsDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListSensitiveColumnsDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.column_name):
            query['ColumnName'] = request.column_name
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSensitiveColumnsDetail',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListSensitiveColumnsDetailResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_standard_groups_with_options(
        self,
        request: dms_enterprise_20181101_models.ListStandardGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListStandardGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStandardGroups',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListStandardGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_standard_groups_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListStandardGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListStandardGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStandardGroups',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListStandardGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_standard_groups(
        self,
        request: dms_enterprise_20181101_models.ListStandardGroupsRequest,
    ) -> dms_enterprise_20181101_models.ListStandardGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_standard_groups_with_options(request, runtime)

    async def list_standard_groups_async(
        self,
        request: dms_enterprise_20181101_models.ListStandardGroupsRequest,
    ) -> dms_enterprise_20181101_models.ListStandardGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_standard_groups_with_options_async(request, runtime)

    def list_tables_with_options(
        self,
        request: dms_enterprise_20181101_models.ListTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.return_guid):
            query['ReturnGuid'] = request.return_guid
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTables',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tables_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_id):
            query['DatabaseId'] = request.database_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.return_guid):
            query['ReturnGuid'] = request.return_guid
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTables',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListTablesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_task_flow_with_options(
        self,
        request: dms_enterprise_20181101_models.ListTaskFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListTaskFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dag_id):
            query['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.dag_instance_id):
            query['DagInstanceId'] = request.dag_instance_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskFlow',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListTaskFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_flow_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListTaskFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListTaskFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dag_id):
            query['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.dag_instance_id):
            query['DagInstanceId'] = request.dag_instance_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskFlow',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListTaskFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_flow(
        self,
        request: dms_enterprise_20181101_models.ListTaskFlowRequest,
    ) -> dms_enterprise_20181101_models.ListTaskFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_task_flow_with_options(request, runtime)

    async def list_task_flow_async(
        self,
        request: dms_enterprise_20181101_models.ListTaskFlowRequest,
    ) -> dms_enterprise_20181101_models.ListTaskFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_task_flow_with_options_async(request, runtime)

    def list_task_flow_instance_with_options(
        self,
        request: dms_enterprise_20181101_models.ListTaskFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListTaskFlowInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dag_id):
            query['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time_begin):
            query['StartTimeBegin'] = request.start_time_begin
        if not UtilClient.is_unset(request.start_time_end):
            query['StartTimeEnd'] = request.start_time_end
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskFlowInstance',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListTaskFlowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_flow_instance_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListTaskFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListTaskFlowInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dag_id):
            query['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time_begin):
            query['StartTimeBegin'] = request.start_time_begin
        if not UtilClient.is_unset(request.start_time_end):
            query['StartTimeEnd'] = request.start_time_end
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskFlowInstance',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListTaskFlowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_flow_instance(
        self,
        request: dms_enterprise_20181101_models.ListTaskFlowInstanceRequest,
    ) -> dms_enterprise_20181101_models.ListTaskFlowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_task_flow_instance_with_options(request, runtime)

    async def list_task_flow_instance_async(
        self,
        request: dms_enterprise_20181101_models.ListTaskFlowInstanceRequest,
    ) -> dms_enterprise_20181101_models.ListTaskFlowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_task_flow_instance_with_options_async(request, runtime)

    def list_user_permissions_with_options(
        self,
        request: dms_enterprise_20181101_models.ListUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListUserPermissionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.perm_type):
            query['PermType'] = request.perm_type
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserPermissions',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListUserPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_permissions_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListUserPermissionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.perm_type):
            query['PermType'] = request.perm_type
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserPermissions',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListUserPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_user_tenants_with_options(
        self,
        request: dms_enterprise_20181101_models.ListUserTenantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListUserTenantsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserTenants',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListUserTenantsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_tenants_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListUserTenantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListUserTenantsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserTenants',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListUserTenantsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_tenants(
        self,
        request: dms_enterprise_20181101_models.ListUserTenantsRequest,
    ) -> dms_enterprise_20181101_models.ListUserTenantsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_tenants_with_options(request, runtime)

    async def list_user_tenants_async(
        self,
        request: dms_enterprise_20181101_models.ListUserTenantsRequest,
    ) -> dms_enterprise_20181101_models.ListUserTenantsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_tenants_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: dms_enterprise_20181101_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.user_state):
            query['UserState'] = request.user_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.user_state):
            query['UserState'] = request.user_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_work_flow_nodes_with_options(
        self,
        request: dms_enterprise_20181101_models.ListWorkFlowNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListWorkFlowNodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkFlowNodes',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListWorkFlowNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_work_flow_nodes_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListWorkFlowNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListWorkFlowNodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkFlowNodes',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListWorkFlowNodesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkFlowTemplates',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListWorkFlowTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_work_flow_templates_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListWorkFlowTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListWorkFlowTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkFlowTemplates',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListWorkFlowTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_data_correct_exec_sqlwith_options(
        self,
        request: dms_enterprise_20181101_models.ModifyDataCorrectExecSQLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ModifyDataCorrectExecSQLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.exec_sql):
            query['ExecSQL'] = request.exec_sql
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDataCorrectExecSQL',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ModifyDataCorrectExecSQLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_data_correct_exec_sqlwith_options_async(
        self,
        request: dms_enterprise_20181101_models.ModifyDataCorrectExecSQLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ModifyDataCorrectExecSQLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.exec_sql):
            query['ExecSQL'] = request.exec_sql
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDataCorrectExecSQL',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ModifyDataCorrectExecSQLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_data_correct_exec_sql(
        self,
        request: dms_enterprise_20181101_models.ModifyDataCorrectExecSQLRequest,
    ) -> dms_enterprise_20181101_models.ModifyDataCorrectExecSQLResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_data_correct_exec_sqlwith_options(request, runtime)

    async def modify_data_correct_exec_sql_async(
        self,
        request: dms_enterprise_20181101_models.ModifyDataCorrectExecSQLRequest,
    ) -> dms_enterprise_20181101_models.ModifyDataCorrectExecSQLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_data_correct_exec_sqlwith_options_async(request, runtime)

    def pause_data_correct_sqljob_with_options(
        self,
        request: dms_enterprise_20181101_models.PauseDataCorrectSQLJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.PauseDataCorrectSQLJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PauseDataCorrectSQLJob',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.PauseDataCorrectSQLJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_data_correct_sqljob_with_options_async(
        self,
        request: dms_enterprise_20181101_models.PauseDataCorrectSQLJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.PauseDataCorrectSQLJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PauseDataCorrectSQLJob',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.PauseDataCorrectSQLJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_data_correct_sqljob(
        self,
        request: dms_enterprise_20181101_models.PauseDataCorrectSQLJobRequest,
    ) -> dms_enterprise_20181101_models.PauseDataCorrectSQLJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.pause_data_correct_sqljob_with_options(request, runtime)

    async def pause_data_correct_sqljob_async(
        self,
        request: dms_enterprise_20181101_models.PauseDataCorrectSQLJobRequest,
    ) -> dms_enterprise_20181101_models.PauseDataCorrectSQLJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pause_data_correct_sqljob_with_options_async(request, runtime)

    def re_deploy_lh_dag_version_with_options(
        self,
        request: dms_enterprise_20181101_models.ReDeployLhDagVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ReDeployLhDagVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dag_id):
            query['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.dag_version):
            query['DagVersion'] = request.dag_version
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReDeployLhDagVersion',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ReDeployLhDagVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def re_deploy_lh_dag_version_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ReDeployLhDagVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ReDeployLhDagVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dag_id):
            query['DagId'] = request.dag_id
        if not UtilClient.is_unset(request.dag_version):
            query['DagVersion'] = request.dag_version
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReDeployLhDagVersion',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ReDeployLhDagVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def re_deploy_lh_dag_version(
        self,
        request: dms_enterprise_20181101_models.ReDeployLhDagVersionRequest,
    ) -> dms_enterprise_20181101_models.ReDeployLhDagVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.re_deploy_lh_dag_version_with_options(request, runtime)

    async def re_deploy_lh_dag_version_async(
        self,
        request: dms_enterprise_20181101_models.ReDeployLhDagVersionRequest,
    ) -> dms_enterprise_20181101_models.ReDeployLhDagVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.re_deploy_lh_dag_version_with_options_async(request, runtime)

    def register_instance_with_options(
        self,
        request: dms_enterprise_20181101_models.RegisterInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RegisterInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_link_name):
            query['DataLinkName'] = request.data_link_name
        if not UtilClient.is_unset(request.database_password):
            query['DatabasePassword'] = request.database_password
        if not UtilClient.is_unset(request.database_user):
            query['DatabaseUser'] = request.database_user
        if not UtilClient.is_unset(request.dba_uid):
            query['DbaUid'] = request.dba_uid
        if not UtilClient.is_unset(request.ddl_online):
            query['DdlOnline'] = request.ddl_online
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.ecs_region):
            query['EcsRegion'] = request.ecs_region
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.export_timeout):
            query['ExportTimeout'] = request.export_timeout
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not UtilClient.is_unset(request.instance_source):
            query['InstanceSource'] = request.instance_source
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.query_timeout):
            query['QueryTimeout'] = request.query_timeout
        if not UtilClient.is_unset(request.safe_rule):
            query['SafeRule'] = request.safe_rule
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.skip_test):
            query['SkipTest'] = request.skip_test
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.use_dsql):
            query['UseDsql'] = request.use_dsql
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterInstance',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.RegisterInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_instance_with_options_async(
        self,
        request: dms_enterprise_20181101_models.RegisterInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RegisterInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_link_name):
            query['DataLinkName'] = request.data_link_name
        if not UtilClient.is_unset(request.database_password):
            query['DatabasePassword'] = request.database_password
        if not UtilClient.is_unset(request.database_user):
            query['DatabaseUser'] = request.database_user
        if not UtilClient.is_unset(request.dba_uid):
            query['DbaUid'] = request.dba_uid
        if not UtilClient.is_unset(request.ddl_online):
            query['DdlOnline'] = request.ddl_online
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.ecs_region):
            query['EcsRegion'] = request.ecs_region
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.export_timeout):
            query['ExportTimeout'] = request.export_timeout
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not UtilClient.is_unset(request.instance_source):
            query['InstanceSource'] = request.instance_source
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.query_timeout):
            query['QueryTimeout'] = request.query_timeout
        if not UtilClient.is_unset(request.safe_rule):
            query['SafeRule'] = request.safe_rule
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.skip_test):
            query['SkipTest'] = request.skip_test
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.use_dsql):
            query['UseDsql'] = request.use_dsql
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterInstance',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.RegisterInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.role_names):
            query['RoleNames'] = request.role_names
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_nick):
            query['UserNick'] = request.user_nick
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterUser',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.RegisterUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_user_with_options_async(
        self,
        request: dms_enterprise_20181101_models.RegisterUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RegisterUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.role_names):
            query['RoleNames'] = request.role_names
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_nick):
            query['UserNick'] = request.user_nick
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterUser',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.RegisterUserResponse(),
            await self.call_api_async(params, req, runtime)
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

    def restart_data_correct_sqljob_with_options(
        self,
        request: dms_enterprise_20181101_models.RestartDataCorrectSQLJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RestartDataCorrectSQLJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDataCorrectSQLJob',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.RestartDataCorrectSQLJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_data_correct_sqljob_with_options_async(
        self,
        request: dms_enterprise_20181101_models.RestartDataCorrectSQLJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RestartDataCorrectSQLJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDataCorrectSQLJob',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.RestartDataCorrectSQLJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_data_correct_sqljob(
        self,
        request: dms_enterprise_20181101_models.RestartDataCorrectSQLJobRequest,
    ) -> dms_enterprise_20181101_models.RestartDataCorrectSQLJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_data_correct_sqljob_with_options(request, runtime)

    async def restart_data_correct_sqljob_async(
        self,
        request: dms_enterprise_20181101_models.RestartDataCorrectSQLJobRequest,
    ) -> dms_enterprise_20181101_models.RestartDataCorrectSQLJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_data_correct_sqljob_with_options_async(request, runtime)

    def retry_data_correct_pre_check_with_options(
        self,
        request: dms_enterprise_20181101_models.RetryDataCorrectPreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RetryDataCorrectPreCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryDataCorrectPreCheck',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.RetryDataCorrectPreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_data_correct_pre_check_with_options_async(
        self,
        request: dms_enterprise_20181101_models.RetryDataCorrectPreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RetryDataCorrectPreCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryDataCorrectPreCheck',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.RetryDataCorrectPreCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_data_correct_pre_check(
        self,
        request: dms_enterprise_20181101_models.RetryDataCorrectPreCheckRequest,
    ) -> dms_enterprise_20181101_models.RetryDataCorrectPreCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_data_correct_pre_check_with_options(request, runtime)

    async def retry_data_correct_pre_check_async(
        self,
        request: dms_enterprise_20181101_models.RetryDataCorrectPreCheckRequest,
    ) -> dms_enterprise_20181101_models.RetryDataCorrectPreCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_data_correct_pre_check_with_options_async(request, runtime)

    def revoke_user_permission_with_options(
        self,
        request: dms_enterprise_20181101_models.RevokeUserPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RevokeUserPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.ds_type):
            query['DsType'] = request.ds_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.perm_types):
            query['PermTypes'] = request.perm_types
        if not UtilClient.is_unset(request.table_id):
            query['TableId'] = request.table_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.user_access_id):
            query['UserAccessId'] = request.user_access_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeUserPermission',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.RevokeUserPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_user_permission_with_options_async(
        self,
        request: dms_enterprise_20181101_models.RevokeUserPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RevokeUserPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.ds_type):
            query['DsType'] = request.ds_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.perm_types):
            query['PermTypes'] = request.perm_types
        if not UtilClient.is_unset(request.table_id):
            query['TableId'] = request.table_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.user_access_id):
            query['UserAccessId'] = request.user_access_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeUserPermission',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.RevokeUserPermissionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.search_range):
            query['SearchRange'] = request.search_range
        if not UtilClient.is_unset(request.search_target):
            query['SearchTarget'] = request.search_target
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchDatabase',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SearchDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_database_with_options_async(
        self,
        request: dms_enterprise_20181101_models.SearchDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SearchDatabaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.search_range):
            query['SearchRange'] = request.search_range
        if not UtilClient.is_unset(request.search_target):
            query['SearchTarget'] = request.search_target
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchDatabase',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SearchDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.return_guid):
            query['ReturnGuid'] = request.return_guid
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.search_range):
            query['SearchRange'] = request.search_range
        if not UtilClient.is_unset(request.search_target):
            query['SearchTarget'] = request.search_target
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTable',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SearchTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_table_with_options_async(
        self,
        request: dms_enterprise_20181101_models.SearchTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SearchTableResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_type):
            query['DbType'] = request.db_type
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.return_guid):
            query['ReturnGuid'] = request.return_guid
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.search_range):
            query['SearchRange'] = request.search_range
        if not UtilClient.is_unset(request.search_target):
            query['SearchTarget'] = request.search_target
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTable',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SearchTableResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.owner_ids):
            query['OwnerIds'] = request.owner_ids
        if not UtilClient.is_unset(request.owner_type):
            query['OwnerType'] = request.owner_type
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetOwners',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SetOwnersResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_owners_with_options_async(
        self,
        request: dms_enterprise_20181101_models.SetOwnersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SetOwnersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_ids):
            query['OwnerIds'] = request.owner_ids
        if not UtilClient.is_unset(request.owner_type):
            query['OwnerType'] = request.owner_type
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetOwners',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SetOwnersResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitOrderApproval',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SubmitOrderApprovalResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_order_approval_with_options_async(
        self,
        request: dms_enterprise_20181101_models.SubmitOrderApprovalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SubmitOrderApprovalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitOrderApproval',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SubmitOrderApprovalResponse(),
            await self.call_api_async(params, req, runtime)
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

    def submit_struct_sync_order_approval_with_options(
        self,
        request: dms_enterprise_20181101_models.SubmitStructSyncOrderApprovalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SubmitStructSyncOrderApprovalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitStructSyncOrderApproval',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SubmitStructSyncOrderApprovalResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_struct_sync_order_approval_with_options_async(
        self,
        request: dms_enterprise_20181101_models.SubmitStructSyncOrderApprovalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SubmitStructSyncOrderApprovalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitStructSyncOrderApproval',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SubmitStructSyncOrderApprovalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_struct_sync_order_approval(
        self,
        request: dms_enterprise_20181101_models.SubmitStructSyncOrderApprovalRequest,
    ) -> dms_enterprise_20181101_models.SubmitStructSyncOrderApprovalResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_struct_sync_order_approval_with_options(request, runtime)

    async def submit_struct_sync_order_approval_async(
        self,
        request: dms_enterprise_20181101_models.SubmitStructSyncOrderApprovalRequest,
    ) -> dms_enterprise_20181101_models.SubmitStructSyncOrderApprovalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_struct_sync_order_approval_with_options_async(request, runtime)

    def sync_database_meta_with_options(
        self,
        request: dms_enterprise_20181101_models.SyncDatabaseMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SyncDatabaseMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncDatabaseMeta',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SyncDatabaseMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_database_meta_with_options_async(
        self,
        request: dms_enterprise_20181101_models.SyncDatabaseMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SyncDatabaseMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['DbId'] = request.db_id
        if not UtilClient.is_unset(request.logic):
            query['Logic'] = request.logic
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncDatabaseMeta',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SyncDatabaseMetaResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.ignore_table):
            query['IgnoreTable'] = request.ignore_table
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncInstanceMeta',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SyncInstanceMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_instance_meta_with_options_async(
        self,
        request: dms_enterprise_20181101_models.SyncInstanceMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SyncInstanceMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ignore_table):
            query['IgnoreTable'] = request.ignore_table
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncInstanceMeta',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SyncInstanceMetaResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.data_link_name):
            query['DataLinkName'] = request.data_link_name
        if not UtilClient.is_unset(request.database_password):
            query['DatabasePassword'] = request.database_password
        if not UtilClient.is_unset(request.database_user):
            query['DatabaseUser'] = request.database_user
        if not UtilClient.is_unset(request.dba_id):
            query['DbaId'] = request.dba_id
        if not UtilClient.is_unset(request.ddl_online):
            query['DdlOnline'] = request.ddl_online
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.ecs_region):
            query['EcsRegion'] = request.ecs_region
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.export_timeout):
            query['ExportTimeout'] = request.export_timeout
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_source):
            query['InstanceSource'] = request.instance_source
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.query_timeout):
            query['QueryTimeout'] = request.query_timeout
        if not UtilClient.is_unset(request.safe_rule_id):
            query['SafeRuleId'] = request.safe_rule_id
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.skip_test):
            query['SkipTest'] = request.skip_test
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.use_dsql):
            query['UseDsql'] = request.use_dsql
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        request: dms_enterprise_20181101_models.UpdateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.UpdateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_link_name):
            query['DataLinkName'] = request.data_link_name
        if not UtilClient.is_unset(request.database_password):
            query['DatabasePassword'] = request.database_password
        if not UtilClient.is_unset(request.database_user):
            query['DatabaseUser'] = request.database_user
        if not UtilClient.is_unset(request.dba_id):
            query['DbaId'] = request.dba_id
        if not UtilClient.is_unset(request.ddl_online):
            query['DdlOnline'] = request.ddl_online
        if not UtilClient.is_unset(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not UtilClient.is_unset(request.ecs_region):
            query['EcsRegion'] = request.ecs_region
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.export_timeout):
            query['ExportTimeout'] = request.export_timeout
        if not UtilClient.is_unset(request.host):
            query['Host'] = request.host
        if not UtilClient.is_unset(request.instance_alias):
            query['InstanceAlias'] = request.instance_alias
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_source):
            query['InstanceSource'] = request.instance_source
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.query_timeout):
            query['QueryTimeout'] = request.query_timeout
        if not UtilClient.is_unset(request.safe_rule_id):
            query['SafeRuleId'] = request.safe_rule_id
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.skip_test):
            query['SkipTest'] = request.skip_test
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.use_dsql):
            query['UseDsql'] = request.use_dsql
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        if not UtilClient.is_unset(request.max_execute_count):
            query['MaxExecuteCount'] = request.max_execute_count
        if not UtilClient.is_unset(request.max_result_count):
            query['MaxResultCount'] = request.max_result_count
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.role_names):
            query['RoleNames'] = request.role_names
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_nick):
            query['UserNick'] = request.user_nick
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: dms_enterprise_20181101_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_execute_count):
            query['MaxExecuteCount'] = request.max_execute_count
        if not UtilClient.is_unset(request.max_result_count):
            query['MaxResultCount'] = request.max_result_count
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.role_names):
            query['RoleNames'] = request.role_names
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.user_nick):
            query['UserNick'] = request.user_nick
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2018-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
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
