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

    def submit_struct_sync_order_approval_with_options(
        self,
        request: dms_enterprise_20181101_models.SubmitStructSyncOrderApprovalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SubmitStructSyncOrderApprovalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SubmitStructSyncOrderApprovalResponse(),
            self.do_rpcrequest('SubmitStructSyncOrderApproval', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_struct_sync_order_approval_with_options_async(
        self,
        request: dms_enterprise_20181101_models.SubmitStructSyncOrderApprovalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SubmitStructSyncOrderApprovalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SubmitStructSyncOrderApprovalResponse(),
            await self.do_rpcrequest_async('SubmitStructSyncOrderApproval', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_database_user_permssions_with_options(
        self,
        request: dms_enterprise_20181101_models.ListDatabaseUserPermssionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDatabaseUserPermssionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDatabaseUserPermssionsResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDatabaseUserPermssionsResponse(),
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

    def list_sensitive_columns_with_options(
        self,
        request: dms_enterprise_20181101_models.ListSensitiveColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListSensitiveColumnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListSensitiveColumnsResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListSensitiveColumnsResponse(),
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

    def list_users_with_options(
        self,
        request: dms_enterprise_20181101_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListUsersResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListUsersResponse(),
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

    def submit_order_approval_with_options(
        self,
        request: dms_enterprise_20181101_models.SubmitOrderApprovalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SubmitOrderApprovalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SubmitOrderApprovalResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SubmitOrderApprovalResponse(),
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

    def grant_user_permission_with_options(
        self,
        request: dms_enterprise_20181101_models.GrantUserPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GrantUserPermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GrantUserPermissionResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GrantUserPermissionResponse(),
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

    def get_meta_table_detail_info_with_options(
        self,
        request: dms_enterprise_20181101_models.GetMetaTableDetailInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetMetaTableDetailInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetMetaTableDetailInfoResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetMetaTableDetailInfoResponse(),
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

    def create_free_lock_correct_order_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateFreeLockCorrectOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateFreeLockCorrectOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateFreeLockCorrectOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateFreeLockCorrectOrderResponse(),
            self.do_rpcrequest('CreateFreeLockCorrectOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_free_lock_correct_order_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateFreeLockCorrectOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateFreeLockCorrectOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateFreeLockCorrectOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateFreeLockCorrectOrderResponse(),
            await self.do_rpcrequest_async('CreateFreeLockCorrectOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_user_permissions_with_options(
        self,
        request: dms_enterprise_20181101_models.ListUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListUserPermissionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListUserPermissionsResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListUserPermissionsResponse(),
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

    def get_proxy_with_options(
        self,
        request: dms_enterprise_20181101_models.GetProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetProxyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetProxyResponse(),
            self.do_rpcrequest('GetProxy', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_proxy_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetProxyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetProxyResponse(),
            await self.do_rpcrequest_async('GetProxy', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_logic_database_with_options(
        self,
        request: dms_enterprise_20181101_models.DeleteLogicDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteLogicDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteLogicDatabaseResponse(),
            self.do_rpcrequest('DeleteLogicDatabase', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_logic_database_with_options_async(
        self,
        request: dms_enterprise_20181101_models.DeleteLogicDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteLogicDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteLogicDatabaseResponse(),
            await self.do_rpcrequest_async('DeleteLogicDatabase', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_ddlpublish_records_with_options(
        self,
        request: dms_enterprise_20181101_models.ListDDLPublishRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDDLPublishRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDDLPublishRecordsResponse(),
            self.do_rpcrequest('ListDDLPublishRecords', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_ddlpublish_records_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListDDLPublishRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDDLPublishRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDDLPublishRecordsResponse(),
            await self.do_rpcrequest_async('ListDDLPublishRecords', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_struct_sync_job_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetStructSyncJobDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetStructSyncJobDetailResponse(),
            self.do_rpcrequest('GetStructSyncJobDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_struct_sync_job_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetStructSyncJobDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetStructSyncJobDetailResponse(),
            await self.do_rpcrequest_async('GetStructSyncJobDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def search_database_with_options(
        self,
        request: dms_enterprise_20181101_models.SearchDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SearchDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SearchDatabaseResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SearchDatabaseResponse(),
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

    def sync_database_meta_with_options(
        self,
        request: dms_enterprise_20181101_models.SyncDatabaseMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SyncDatabaseMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SyncDatabaseMetaResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SyncDatabaseMetaResponse(),
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

    def get_meta_table_column_with_options(
        self,
        request: dms_enterprise_20181101_models.GetMetaTableColumnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetMetaTableColumnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetMetaTableColumnResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetMetaTableColumnResponse(),
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

    def change_column_sec_level_with_options(
        self,
        request: dms_enterprise_20181101_models.ChangeColumnSecLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ChangeColumnSecLevelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ChangeColumnSecLevelResponse(),
            self.do_rpcrequest('ChangeColumnSecLevel', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_column_sec_level_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ChangeColumnSecLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ChangeColumnSecLevelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ChangeColumnSecLevelResponse(),
            await self.do_rpcrequest_async('ChangeColumnSecLevel', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def execute_script_with_options(
        self,
        request: dms_enterprise_20181101_models.ExecuteScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ExecuteScriptResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ExecuteScriptResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ExecuteScriptResponse(),
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

    def list_dbtask_sqljob_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.ListDBTaskSQLJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDBTaskSQLJobDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDBTaskSQLJobDetailResponse(),
            self.do_rpcrequest('ListDBTaskSQLJobDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_dbtask_sqljob_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListDBTaskSQLJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDBTaskSQLJobDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDBTaskSQLJobDetailResponse(),
            await self.do_rpcrequest_async('ListDBTaskSQLJobDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_user_active_tenant_with_options(
        self,
        request: dms_enterprise_20181101_models.GetUserActiveTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetUserActiveTenantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetUserActiveTenantResponse(),
            self.do_rpcrequest('GetUserActiveTenant', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_active_tenant_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetUserActiveTenantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetUserActiveTenantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetUserActiveTenantResponse(),
            await self.do_rpcrequest_async('GetUserActiveTenant', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def register_user_with_options(
        self,
        request: dms_enterprise_20181101_models.RegisterUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RegisterUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.RegisterUserResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.RegisterUserResponse(),
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

    def get_perm_apply_order_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetPermApplyOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetPermApplyOrderDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetPermApplyOrderDetailResponse(),
            self.do_rpcrequest('GetPermApplyOrderDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_perm_apply_order_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetPermApplyOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetPermApplyOrderDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetPermApplyOrderDetailResponse(),
            await self.do_rpcrequest_async('GetPermApplyOrderDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_logic_tables_with_options(
        self,
        request: dms_enterprise_20181101_models.ListLogicTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListLogicTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListLogicTablesResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListLogicTablesResponse(),
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

    def get_data_export_download_urlwith_options(
        self,
        request: dms_enterprise_20181101_models.GetDataExportDownloadURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataExportDownloadURLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataExportDownloadURLResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataExportDownloadURLResponse(),
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

    def get_database_with_options(
        self,
        request: dms_enterprise_20181101_models.GetDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDatabaseResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDatabaseResponse(),
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

    def search_table_with_options(
        self,
        request: dms_enterprise_20181101_models.SearchTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SearchTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SearchTableResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SearchTableResponse(),
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

    def approve_order_with_options(
        self,
        request: dms_enterprise_20181101_models.ApproveOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ApproveOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ApproveOrderResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ApproveOrderResponse(),
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

    def delete_proxy_access_with_options(
        self,
        request: dms_enterprise_20181101_models.DeleteProxyAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteProxyAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteProxyAccessResponse(),
            self.do_rpcrequest('DeleteProxyAccess', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_proxy_access_with_options_async(
        self,
        request: dms_enterprise_20181101_models.DeleteProxyAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteProxyAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteProxyAccessResponse(),
            await self.do_rpcrequest_async('DeleteProxyAccess', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_data_correct_task_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCorrectTaskDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCorrectTaskDetailResponse(),
            self.do_rpcrequest('GetDataCorrectTaskDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_data_correct_task_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCorrectTaskDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCorrectTaskDetailResponse(),
            await self.do_rpcrequest_async('GetDataCorrectTaskDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def close_order_with_options(
        self,
        request: dms_enterprise_20181101_models.CloseOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CloseOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CloseOrderResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CloseOrderResponse(),
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

    def sync_instance_meta_with_options(
        self,
        request: dms_enterprise_20181101_models.SyncInstanceMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SyncInstanceMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SyncInstanceMetaResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SyncInstanceMetaResponse(),
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

    def get_sqlreview_optimize_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetSQLReviewOptimizeDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetSQLReviewOptimizeDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetSQLReviewOptimizeDetailResponse(),
            self.do_rpcrequest('GetSQLReviewOptimizeDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_sqlreview_optimize_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetSQLReviewOptimizeDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetSQLReviewOptimizeDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetSQLReviewOptimizeDetailResponse(),
            await self.do_rpcrequest_async('GetSQLReviewOptimizeDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def register_instance_with_options(
        self,
        request: dms_enterprise_20181101_models.RegisterInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RegisterInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.RegisterInstanceResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.RegisterInstanceResponse(),
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

    def create_struct_sync_order_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateStructSyncOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateStructSyncOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateStructSyncOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateStructSyncOrderResponse(),
            self.do_rpcrequest('CreateStructSyncOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_struct_sync_order_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateStructSyncOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateStructSyncOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateStructSyncOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateStructSyncOrderResponse(),
            await self.do_rpcrequest_async('CreateStructSyncOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ExecuteDataExportResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ExecuteDataExportResponse(),
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

    def list_work_flow_nodes_with_options(
        self,
        request: dms_enterprise_20181101_models.ListWorkFlowNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListWorkFlowNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListWorkFlowNodesResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListWorkFlowNodesResponse(),
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

    def list_proxies_with_options(
        self,
        request: dms_enterprise_20181101_models.ListProxiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListProxiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListProxiesResponse(),
            self.do_rpcrequest('ListProxies', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_proxies_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListProxiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListProxiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListProxiesResponse(),
            await self.do_rpcrequest_async('ListProxies', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_struct_sync_order_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetStructSyncOrderDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetStructSyncOrderDetailResponse(),
            self.do_rpcrequest('GetStructSyncOrderDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_struct_sync_order_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetStructSyncOrderDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetStructSyncOrderDetailResponse(),
            await self.do_rpcrequest_async('GetStructSyncOrderDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_user_with_options(
        self,
        request: dms_enterprise_20181101_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.UpdateUserResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.UpdateUserResponse(),
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

    def get_physical_database_with_options(
        self,
        request: dms_enterprise_20181101_models.GetPhysicalDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetPhysicalDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetPhysicalDatabaseResponse(),
            self.do_rpcrequest('GetPhysicalDatabase', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_physical_database_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetPhysicalDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetPhysicalDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetPhysicalDatabaseResponse(),
            await self.do_rpcrequest_async('GetPhysicalDatabase', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_struct_sync_exec_sql_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncExecSqlDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetStructSyncExecSqlDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetStructSyncExecSqlDetailResponse(),
            self.do_rpcrequest('GetStructSyncExecSqlDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_struct_sync_exec_sql_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncExecSqlDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetStructSyncExecSqlDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetStructSyncExecSqlDetailResponse(),
            await self.do_rpcrequest_async('GetStructSyncExecSqlDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_instance_with_options(
        self,
        request: dms_enterprise_20181101_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteInstanceResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteInstanceResponse(),
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

    def get_table_dbtopology_with_options(
        self,
        request: dms_enterprise_20181101_models.GetTableDBTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetTableDBTopologyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetTableDBTopologyResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetTableDBTopologyResponse(),
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

    def get_data_correct_sqlfile_with_options(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectSQLFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCorrectSQLFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCorrectSQLFileResponse(),
            self.do_rpcrequest('GetDataCorrectSQLFile', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_data_correct_sqlfile_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectSQLFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCorrectSQLFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCorrectSQLFileResponse(),
            await self.do_rpcrequest_async('GetDataCorrectSQLFile', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateOrderResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateOrderResponse(),
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

    def list_databases_with_options(
        self,
        request: dms_enterprise_20181101_models.ListDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDatabasesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDatabasesResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDatabasesResponse(),
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

    def create_proxy_access_with_options(
        self,
        request: dms_enterprise_20181101_models.CreateProxyAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateProxyAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateProxyAccessResponse(),
            self.do_rpcrequest('CreateProxyAccess', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_proxy_access_with_options_async(
        self,
        request: dms_enterprise_20181101_models.CreateProxyAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateProxyAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateProxyAccessResponse(),
            await self.do_rpcrequest_async('CreateProxyAccess', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_work_flow_templates_with_options(
        self,
        request: dms_enterprise_20181101_models.ListWorkFlowTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListWorkFlowTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListWorkFlowTemplatesResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListWorkFlowTemplatesResponse(),
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

    def get_data_export_order_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetDataExportOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataExportOrderDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataExportOrderDetailResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataExportOrderDetailResponse(),
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

    def list_instances_with_options(
        self,
        request: dms_enterprise_20181101_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListInstancesResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListInstancesResponse(),
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

    def get_user_upload_file_job_with_options(
        self,
        request: dms_enterprise_20181101_models.GetUserUploadFileJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetUserUploadFileJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetUserUploadFileJobResponse(),
            self.do_rpcrequest('GetUserUploadFileJob', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_upload_file_job_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetUserUploadFileJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetUserUploadFileJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetUserUploadFileJobResponse(),
            await self.do_rpcrequest_async('GetUserUploadFileJob', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_proxy_with_options(
        self,
        request: dms_enterprise_20181101_models.CreateProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateProxyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateProxyResponse(),
            self.do_rpcrequest('CreateProxy', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_proxy_with_options_async(
        self,
        request: dms_enterprise_20181101_models.CreateProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateProxyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateProxyResponse(),
            await self.do_rpcrequest_async('CreateProxy', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateUploadOSSFileJobResponse(),
            self.do_rpcrequest('CreateUploadOSSFileJob', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateUploadOSSFileJobResponse(),
            await self.do_rpcrequest_async('CreateUploadOSSFileJob', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_dbtopology_with_options(
        self,
        request: dms_enterprise_20181101_models.GetDBTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDBTopologyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDBTopologyResponse(),
            self.do_rpcrequest('GetDBTopology', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_dbtopology_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetDBTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDBTopologyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDBTopologyResponse(),
            await self.do_rpcrequest_async('GetDBTopology', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_sqlreview_check_result_status_with_options(
        self,
        request: dms_enterprise_20181101_models.GetSQLReviewCheckResultStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetSQLReviewCheckResultStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetSQLReviewCheckResultStatusResponse(),
            self.do_rpcrequest('GetSQLReviewCheckResultStatus', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_sqlreview_check_result_status_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetSQLReviewCheckResultStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetSQLReviewCheckResultStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetSQLReviewCheckResultStatusResponse(),
            await self.do_rpcrequest_async('GetSQLReviewCheckResultStatus', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_user_with_options(
        self,
        request: dms_enterprise_20181101_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetUserResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetUserResponse(),
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

    def execute_struct_sync_with_options(
        self,
        request: dms_enterprise_20181101_models.ExecuteStructSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ExecuteStructSyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ExecuteStructSyncResponse(),
            self.do_rpcrequest('ExecuteStructSync', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def execute_struct_sync_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ExecuteStructSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ExecuteStructSyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ExecuteStructSyncResponse(),
            await self.do_rpcrequest_async('ExecuteStructSync', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_data_correct_order_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetDataCorrectOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCorrectOrderDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCorrectOrderDetailResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCorrectOrderDetailResponse(),
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

    def list_columns_with_options(
        self,
        request: dms_enterprise_20181101_models.ListColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListColumnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListColumnsResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListColumnsResponse(),
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

    def revoke_user_permission_with_options(
        self,
        request: dms_enterprise_20181101_models.RevokeUserPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.RevokeUserPermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.RevokeUserPermissionResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.RevokeUserPermissionResponse(),
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

    def enable_user_with_options(
        self,
        request: dms_enterprise_20181101_models.EnableUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.EnableUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.EnableUserResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.EnableUserResponse(),
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.EditLogicDatabaseResponse(),
            self.do_rpcrequest('EditLogicDatabase', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.EditLogicDatabaseResponse(),
            await self.do_rpcrequest_async('EditLogicDatabase', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_instance_with_options(
        self,
        request: dms_enterprise_20181101_models.UpdateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.UpdateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.UpdateInstanceResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.UpdateInstanceResponse(),
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

    def disable_user_with_options(
        self,
        request: dms_enterprise_20181101_models.DisableUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DisableUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DisableUserResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DisableUserResponse(),
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

    def get_approval_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetApprovalDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetApprovalDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetApprovalDetailResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetApprovalDetailResponse(),
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListSQLReviewOriginSQLResponse(),
            self.do_rpcrequest('ListSQLReviewOriginSQL', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListSQLReviewOriginSQLResponse(),
            await self.do_rpcrequest_async('ListSQLReviewOriginSQL', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_instance_with_options(
        self,
        request: dms_enterprise_20181101_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetInstanceResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetInstanceResponse(),
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

    def list_indexes_with_options(
        self,
        request: dms_enterprise_20181101_models.ListIndexesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListIndexesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListIndexesResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListIndexesResponse(),
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

    def get_table_topology_with_options(
        self,
        request: dms_enterprise_20181101_models.GetTableTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetTableTopologyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetTableTopologyResponse(),
            self.do_rpcrequest('GetTableTopology', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_table_topology_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetTableTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetTableTopologyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetTableTopologyResponse(),
            await self.do_rpcrequest_async('GetTableTopology', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_data_cron_clear_order_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateDataCronClearOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateDataCronClearOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateDataCronClearOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateDataCronClearOrderResponse(),
            self.do_rpcrequest('CreateDataCronClearOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_data_cron_clear_order_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateDataCronClearOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateDataCronClearOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateDataCronClearOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateDataCronClearOrderResponse(),
            await self.do_rpcrequest_async('CreateDataCronClearOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_proxy_accesses_with_options(
        self,
        request: dms_enterprise_20181101_models.ListProxyAccessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListProxyAccessesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListProxyAccessesResponse(),
            self.do_rpcrequest('ListProxyAccesses', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_proxy_accesses_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListProxyAccessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListProxyAccessesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListProxyAccessesResponse(),
            await self.do_rpcrequest_async('ListProxyAccesses', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_publish_group_task_with_options(
        self,
        request: dms_enterprise_20181101_models.CreatePublishGroupTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreatePublishGroupTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreatePublishGroupTaskResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreatePublishGroupTaskResponse(),
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

    def inspect_proxy_access_secret_with_options(
        self,
        request: dms_enterprise_20181101_models.InspectProxyAccessSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.InspectProxyAccessSecretResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.InspectProxyAccessSecretResponse(),
            self.do_rpcrequest('InspectProxyAccessSecret', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def inspect_proxy_access_secret_with_options_async(
        self,
        request: dms_enterprise_20181101_models.InspectProxyAccessSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.InspectProxyAccessSecretResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.InspectProxyAccessSecretResponse(),
            await self.do_rpcrequest_async('InspectProxyAccessSecret', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_owner_apply_order_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.GetOwnerApplyOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetOwnerApplyOrderDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetOwnerApplyOrderDetailResponse(),
            self.do_rpcrequest('GetOwnerApplyOrderDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_owner_apply_order_detail_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetOwnerApplyOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetOwnerApplyOrderDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetOwnerApplyOrderDetailResponse(),
            await self.do_rpcrequest_async('GetOwnerApplyOrderDetail', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_instance_user_permissions_with_options(
        self,
        request: dms_enterprise_20181101_models.ListInstanceUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListInstanceUserPermissionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListInstanceUserPermissionsResponse(),
            self.do_rpcrequest('ListInstanceUserPermissions', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_instance_user_permissions_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListInstanceUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListInstanceUserPermissionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListInstanceUserPermissionsResponse(),
            await self.do_rpcrequest_async('ListInstanceUserPermissions', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_op_log_with_options(
        self,
        request: dms_enterprise_20181101_models.GetOpLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetOpLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetOpLogResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetOpLogResponse(),
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

    def list_dbtask_sqljob_with_options(
        self,
        request: dms_enterprise_20181101_models.ListDBTaskSQLJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDBTaskSQLJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDBTaskSQLJobResponse(),
            self.do_rpcrequest('ListDBTaskSQLJob', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_dbtask_sqljob_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListDBTaskSQLJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDBTaskSQLJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDBTaskSQLJobResponse(),
            await self.do_rpcrequest_async('ListDBTaskSQLJob', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_user_with_options(
        self,
        request: dms_enterprise_20181101_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteUserResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteUserResponse(),
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

    def get_data_cron_clear_task_detail_list_with_options(
        self,
        request: dms_enterprise_20181101_models.GetDataCronClearTaskDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCronClearTaskDetailListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCronClearTaskDetailListResponse(),
            self.do_rpcrequest('GetDataCronClearTaskDetailList', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_data_cron_clear_task_detail_list_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetDataCronClearTaskDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetDataCronClearTaskDetailListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCronClearTaskDetailListResponse(),
            await self.do_rpcrequest_async('GetDataCronClearTaskDetailList', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_struct_sync_job_analyze_result_with_options(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncJobAnalyzeResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetStructSyncJobAnalyzeResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetStructSyncJobAnalyzeResultResponse(),
            self.do_rpcrequest('GetStructSyncJobAnalyzeResult', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_struct_sync_job_analyze_result_with_options_async(
        self,
        request: dms_enterprise_20181101_models.GetStructSyncJobAnalyzeResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetStructSyncJobAnalyzeResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetStructSyncJobAnalyzeResultResponse(),
            await self.do_rpcrequest_async('GetStructSyncJobAnalyzeResult', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_upload_file_job_with_options(
        self,
        request: dms_enterprise_20181101_models.CreateUploadFileJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateUploadFileJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateUploadFileJobResponse(),
            self.do_rpcrequest('CreateUploadFileJob', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_upload_file_job_with_options_async(
        self,
        request: dms_enterprise_20181101_models.CreateUploadFileJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateUploadFileJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateUploadFileJobResponse(),
            await self.do_rpcrequest_async('CreateUploadFileJob', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_proxy_with_options(
        self,
        request: dms_enterprise_20181101_models.DeleteProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteProxyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteProxyResponse(),
            self.do_rpcrequest('DeleteProxy', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_proxy_with_options_async(
        self,
        request: dms_enterprise_20181101_models.DeleteProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.DeleteProxyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.DeleteProxyResponse(),
            await self.do_rpcrequest_async('DeleteProxy', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_logic_databases_with_options(
        self,
        request: dms_enterprise_20181101_models.ListLogicDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListLogicDatabasesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListLogicDatabasesResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListLogicDatabasesResponse(),
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

    def create_data_import_order_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateDataImportOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateDataImportOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateDataImportOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateDataImportOrderResponse(),
            self.do_rpcrequest('CreateDataImportOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_data_import_order_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateDataImportOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateDataImportOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateDataImportOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateDataImportOrderResponse(),
            await self.do_rpcrequest_async('CreateDataImportOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_orders_with_options(
        self,
        request: dms_enterprise_20181101_models.ListOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListOrdersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListOrdersResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListOrdersResponse(),
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

    def create_sqlreview_order_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateSQLReviewOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateSQLReviewOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateSQLReviewOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateSQLReviewOrderResponse(),
            self.do_rpcrequest('CreateSQLReviewOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_sqlreview_order_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateSQLReviewOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateSQLReviewOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateSQLReviewOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateSQLReviewOrderResponse(),
            await self.do_rpcrequest_async('CreateSQLReviewOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_order_base_info_with_options(
        self,
        request: dms_enterprise_20181101_models.GetOrderBaseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetOrderBaseInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetOrderBaseInfoResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetOrderBaseInfoResponse(),
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

    def list_user_tenants_with_options(
        self,
        request: dms_enterprise_20181101_models.ListUserTenantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListUserTenantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListUserTenantsResponse(),
            self.do_rpcrequest('ListUserTenants', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_tenants_with_options_async(
        self,
        request: dms_enterprise_20181101_models.ListUserTenantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListUserTenantsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListUserTenantsResponse(),
            await self.do_rpcrequest_async('ListUserTenants', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def set_owners_with_options(
        self,
        request: dms_enterprise_20181101_models.SetOwnersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.SetOwnersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SetOwnersResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.SetOwnersResponse(),
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

    def create_data_correct_order_with_options(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateDataCorrectOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateDataCorrectOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateDataCorrectOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateDataCorrectOrderResponse(),
            self.do_rpcrequest('CreateDataCorrectOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_data_correct_order_with_options_async(
        self,
        tmp_req: dms_enterprise_20181101_models.CreateDataCorrectOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.CreateDataCorrectOrderResponse:
        UtilClient.validate_model(tmp_req)
        request = dms_enterprise_20181101_models.CreateDataCorrectOrderShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.related_user_list):
            request.related_user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.related_user_list, 'RelatedUserList', 'json')
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'Param', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateDataCorrectOrderResponse(),
            await self.do_rpcrequest_async('CreateDataCorrectOrder', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_logic_database_with_options(
        self,
        request: dms_enterprise_20181101_models.GetLogicDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.GetLogicDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetLogicDatabaseResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetLogicDatabaseResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCorrectBackupFilesResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.GetDataCorrectBackupFilesResponse(),
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

    def list_data_correct_pre_check_sqlwith_options(
        self,
        request: dms_enterprise_20181101_models.ListDataCorrectPreCheckSQLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDataCorrectPreCheckSQLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDataCorrectPreCheckSQLResponse(),
            self.do_rpcrequest('ListDataCorrectPreCheckSQL', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_data_correct_pre_check_sqlwith_options_async(
        self,
        request: dms_enterprise_20181101_models.ListDataCorrectPreCheckSQLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDataCorrectPreCheckSQLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDataCorrectPreCheckSQLResponse(),
            await self.do_rpcrequest_async('ListDataCorrectPreCheckSQL', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ExecuteDataCorrectResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ExecuteDataCorrectResponse(),
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

    def list_data_correct_pre_check_dbwith_options(
        self,
        request: dms_enterprise_20181101_models.ListDataCorrectPreCheckDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDataCorrectPreCheckDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDataCorrectPreCheckDBResponse(),
            self.do_rpcrequest('ListDataCorrectPreCheckDB', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_data_correct_pre_check_dbwith_options_async(
        self,
        request: dms_enterprise_20181101_models.ListDataCorrectPreCheckDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListDataCorrectPreCheckDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListDataCorrectPreCheckDBResponse(),
            await self.do_rpcrequest_async('ListDataCorrectPreCheckDB', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateLogicDatabaseResponse(),
            self.do_rpcrequest('CreateLogicDatabase', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.CreateLogicDatabaseResponse(),
            await self.do_rpcrequest_async('CreateLogicDatabase', '2018-11-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_tables_with_options(
        self,
        request: dms_enterprise_20181101_models.ListTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListTablesResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListTablesResponse(),
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

    def list_sensitive_columns_detail_with_options(
        self,
        request: dms_enterprise_20181101_models.ListSensitiveColumnsDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_enterprise_20181101_models.ListSensitiveColumnsDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListSensitiveColumnsDetailResponse(),
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
        return TeaCore.from_map(
            dms_enterprise_20181101_models.ListSensitiveColumnsDetailResponse(),
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
