# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_edas20170801 import models as edas_20170801_models
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
        self._endpoint_map = {
            'ap-northeast-2-pop': 'edas.ap-northeast-1.aliyuncs.com',
            'ap-south-1': 'edas.ap-northeast-1.aliyuncs.com',
            'ap-southeast-3': 'edas.ap-northeast-1.aliyuncs.com',
            'ap-southeast-5': 'edas.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'edas.aliyuncs.com',
            'cn-beijing-finance-pop': 'edas.aliyuncs.com',
            'cn-beijing-gov-1': 'edas.aliyuncs.com',
            'cn-beijing-nu16-b01': 'edas.aliyuncs.com',
            'cn-chengdu': 'edas.aliyuncs.com',
            'cn-edge-1': 'edas.aliyuncs.com',
            'cn-fujian': 'edas.aliyuncs.com',
            'cn-haidian-cm12-c01': 'edas.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'edas.aliyuncs.com',
            'cn-hangzhou-finance': 'edas.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'edas.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'edas.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'edas.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'edas.aliyuncs.com',
            'cn-hangzhou-test-306': 'edas.aliyuncs.com',
            'cn-hongkong-finance-pop': 'edas.aliyuncs.com',
            'cn-huhehaote': 'edas.aliyuncs.com',
            'cn-qingdao-nebula': 'edas.aliyuncs.com',
            'cn-shanghai-et15-b01': 'edas.aliyuncs.com',
            'cn-shanghai-et2-b01': 'edas.aliyuncs.com',
            'cn-shanghai-finance-1': 'edas.aliyuncs.com',
            'cn-shanghai-inner': 'edas.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'edas.aliyuncs.com',
            'cn-shenzhen-finance-1': 'edas.aliyuncs.com',
            'cn-shenzhen-inner': 'edas.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'edas.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'edas.aliyuncs.com',
            'cn-wuhan': 'edas.aliyuncs.com',
            'cn-yushanfang': 'edas.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'edas.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'edas.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'edas.aliyuncs.com',
            'eu-west-1': 'edas.ap-northeast-1.aliyuncs.com',
            'eu-west-1-oxs': 'edas.ap-northeast-1.aliyuncs.com',
            'me-east-1': 'edas.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'edas.ap-northeast-1.aliyuncs.com',
            'us-west-1': 'edas.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('edas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abort_and_rollback_change_order_with_options(
        self,
        request: edas_20170801_models.AbortAndRollbackChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.AbortAndRollbackChangeOrderResponse:
        """
        @summary Terminates a change process and rolls back the application. This operation is applicable to applications that are deployed in Container Service for Kubernetes (ACK) clusters.
        
        @param request: AbortAndRollbackChangeOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbortAndRollbackChangeOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortAndRollbackChangeOrder',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/change_order_abort_and_rollback',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.AbortAndRollbackChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def abort_and_rollback_change_order_with_options_async(
        self,
        request: edas_20170801_models.AbortAndRollbackChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.AbortAndRollbackChangeOrderResponse:
        """
        @summary Terminates a change process and rolls back the application. This operation is applicable to applications that are deployed in Container Service for Kubernetes (ACK) clusters.
        
        @param request: AbortAndRollbackChangeOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbortAndRollbackChangeOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortAndRollbackChangeOrder',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/change_order_abort_and_rollback',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.AbortAndRollbackChangeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abort_and_rollback_change_order(
        self,
        request: edas_20170801_models.AbortAndRollbackChangeOrderRequest,
    ) -> edas_20170801_models.AbortAndRollbackChangeOrderResponse:
        """
        @summary Terminates a change process and rolls back the application. This operation is applicable to applications that are deployed in Container Service for Kubernetes (ACK) clusters.
        
        @param request: AbortAndRollbackChangeOrderRequest
        @return: AbortAndRollbackChangeOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.abort_and_rollback_change_order_with_options(request, headers, runtime)

    async def abort_and_rollback_change_order_async(
        self,
        request: edas_20170801_models.AbortAndRollbackChangeOrderRequest,
    ) -> edas_20170801_models.AbortAndRollbackChangeOrderResponse:
        """
        @summary Terminates a change process and rolls back the application. This operation is applicable to applications that are deployed in Container Service for Kubernetes (ACK) clusters.
        
        @param request: AbortAndRollbackChangeOrderRequest
        @return: AbortAndRollbackChangeOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.abort_and_rollback_change_order_with_options_async(request, headers, runtime)

    def abort_change_order_with_options(
        self,
        request: edas_20170801_models.AbortChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.AbortChangeOrderResponse:
        """
        @summary Terminates a change process.
        
        @param request: AbortChangeOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbortChangeOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortChangeOrder',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/change_order_abort',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.AbortChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def abort_change_order_with_options_async(
        self,
        request: edas_20170801_models.AbortChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.AbortChangeOrderResponse:
        """
        @summary Terminates a change process.
        
        @param request: AbortChangeOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AbortChangeOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AbortChangeOrder',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/change_order_abort',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.AbortChangeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abort_change_order(
        self,
        request: edas_20170801_models.AbortChangeOrderRequest,
    ) -> edas_20170801_models.AbortChangeOrderResponse:
        """
        @summary Terminates a change process.
        
        @param request: AbortChangeOrderRequest
        @return: AbortChangeOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.abort_change_order_with_options(request, headers, runtime)

    async def abort_change_order_async(
        self,
        request: edas_20170801_models.AbortChangeOrderRequest,
    ) -> edas_20170801_models.AbortChangeOrderResponse:
        """
        @summary Terminates a change process.
        
        @param request: AbortChangeOrderRequest
        @return: AbortChangeOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.abort_change_order_with_options_async(request, headers, runtime)

    def add_log_path_with_options(
        self,
        request: edas_20170801_models.AddLogPathRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.AddLogPathResponse:
        """
        @summary Adds a log directory to an application. This operation is applicable to applications that are deployed in Alibaba Cloud Elastic Compute Service (ECS) clusters and hybrid cloud ECS clusters.
        
        @param request: AddLogPathRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddLogPathResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddLogPath',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/log/popListLogDirs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.AddLogPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_log_path_with_options_async(
        self,
        request: edas_20170801_models.AddLogPathRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.AddLogPathResponse:
        """
        @summary Adds a log directory to an application. This operation is applicable to applications that are deployed in Alibaba Cloud Elastic Compute Service (ECS) clusters and hybrid cloud ECS clusters.
        
        @param request: AddLogPathRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddLogPathResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddLogPath',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/log/popListLogDirs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.AddLogPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_log_path(
        self,
        request: edas_20170801_models.AddLogPathRequest,
    ) -> edas_20170801_models.AddLogPathResponse:
        """
        @summary Adds a log directory to an application. This operation is applicable to applications that are deployed in Alibaba Cloud Elastic Compute Service (ECS) clusters and hybrid cloud ECS clusters.
        
        @param request: AddLogPathRequest
        @return: AddLogPathResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_log_path_with_options(request, headers, runtime)

    async def add_log_path_async(
        self,
        request: edas_20170801_models.AddLogPathRequest,
    ) -> edas_20170801_models.AddLogPathResponse:
        """
        @summary Adds a log directory to an application. This operation is applicable to applications that are deployed in Alibaba Cloud Elastic Compute Service (ECS) clusters and hybrid cloud ECS clusters.
        
        @param request: AddLogPathRequest
        @return: AddLogPathResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_log_path_with_options_async(request, headers, runtime)

    def authorize_application_with_options(
        self,
        request: edas_20170801_models.AuthorizeApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.AuthorizeApplicationResponse:
        """
        @summary Grants a Resource Access Management (RAM) user the permissions on a specified application.
        
        @param request: AuthorizeApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/authorize_app',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.AuthorizeApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_application_with_options_async(
        self,
        request: edas_20170801_models.AuthorizeApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.AuthorizeApplicationResponse:
        """
        @summary Grants a Resource Access Management (RAM) user the permissions on a specified application.
        
        @param request: AuthorizeApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/authorize_app',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.AuthorizeApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_application(
        self,
        request: edas_20170801_models.AuthorizeApplicationRequest,
    ) -> edas_20170801_models.AuthorizeApplicationResponse:
        """
        @summary Grants a Resource Access Management (RAM) user the permissions on a specified application.
        
        @param request: AuthorizeApplicationRequest
        @return: AuthorizeApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.authorize_application_with_options(request, headers, runtime)

    async def authorize_application_async(
        self,
        request: edas_20170801_models.AuthorizeApplicationRequest,
    ) -> edas_20170801_models.AuthorizeApplicationResponse:
        """
        @summary Grants a Resource Access Management (RAM) user the permissions on a specified application.
        
        @param request: AuthorizeApplicationRequest
        @return: AuthorizeApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.authorize_application_with_options_async(request, headers, runtime)

    def authorize_resource_group_with_options(
        self,
        request: edas_20170801_models.AuthorizeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.AuthorizeResourceGroupResponse:
        """
        @summary Grants a Resource Access Management (RAM) user the permissions on a resource group.
        
        @param request: AuthorizeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeResourceGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/authorize_res_group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.AuthorizeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_resource_group_with_options_async(
        self,
        request: edas_20170801_models.AuthorizeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.AuthorizeResourceGroupResponse:
        """
        @summary Grants a Resource Access Management (RAM) user the permissions on a resource group.
        
        @param request: AuthorizeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeResourceGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/authorize_res_group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.AuthorizeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_resource_group(
        self,
        request: edas_20170801_models.AuthorizeResourceGroupRequest,
    ) -> edas_20170801_models.AuthorizeResourceGroupResponse:
        """
        @summary Grants a Resource Access Management (RAM) user the permissions on a resource group.
        
        @param request: AuthorizeResourceGroupRequest
        @return: AuthorizeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.authorize_resource_group_with_options(request, headers, runtime)

    async def authorize_resource_group_async(
        self,
        request: edas_20170801_models.AuthorizeResourceGroupRequest,
    ) -> edas_20170801_models.AuthorizeResourceGroupResponse:
        """
        @summary Grants a Resource Access Management (RAM) user the permissions on a resource group.
        
        @param request: AuthorizeResourceGroupRequest
        @return: AuthorizeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.authorize_resource_group_with_options_async(request, headers, runtime)

    def authorize_role_with_options(
        self,
        request: edas_20170801_models.AuthorizeRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.AuthorizeRoleResponse:
        """
        @summary Assigns one or more roles to a RAM user.
        
        @param request: AuthorizeRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_ids):
            query['RoleIds'] = request.role_ids
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeRole',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/authorize_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.AuthorizeRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_role_with_options_async(
        self,
        request: edas_20170801_models.AuthorizeRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.AuthorizeRoleResponse:
        """
        @summary Assigns one or more roles to a RAM user.
        
        @param request: AuthorizeRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_ids):
            query['RoleIds'] = request.role_ids
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeRole',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/authorize_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.AuthorizeRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_role(
        self,
        request: edas_20170801_models.AuthorizeRoleRequest,
    ) -> edas_20170801_models.AuthorizeRoleResponse:
        """
        @summary Assigns one or more roles to a RAM user.
        
        @param request: AuthorizeRoleRequest
        @return: AuthorizeRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.authorize_role_with_options(request, headers, runtime)

    async def authorize_role_async(
        self,
        request: edas_20170801_models.AuthorizeRoleRequest,
    ) -> edas_20170801_models.AuthorizeRoleResponse:
        """
        @summary Assigns one or more roles to a RAM user.
        
        @param request: AuthorizeRoleRequest
        @return: AuthorizeRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.authorize_role_with_options_async(request, headers, runtime)

    def bind_ecs_slb_with_options(
        self,
        request: edas_20170801_models.BindEcsSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.BindEcsSlbResponse:
        """
        @summary Binds a Server Load Balancer (SLB) instance to an application that is deployed in an Elastic Compute Service (ECS) cluster.
        
        @param request: BindEcsSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindEcsSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.deploy_group_id):
            query['DeployGroupId'] = request.deploy_group_id
        if not UtilClient.is_unset(request.listener_health_check_url):
            query['ListenerHealthCheckUrl'] = request.listener_health_check_url
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.slb_id):
            query['SlbId'] = request.slb_id
        if not UtilClient.is_unset(request.vforwarding_url_rule):
            query['VForwardingUrlRule'] = request.vforwarding_url_rule
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.vserver_group_name):
            query['VServerGroupName'] = request.vserver_group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindEcsSlb',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/slb/bind_slb',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.BindEcsSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_ecs_slb_with_options_async(
        self,
        request: edas_20170801_models.BindEcsSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.BindEcsSlbResponse:
        """
        @summary Binds a Server Load Balancer (SLB) instance to an application that is deployed in an Elastic Compute Service (ECS) cluster.
        
        @param request: BindEcsSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindEcsSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.deploy_group_id):
            query['DeployGroupId'] = request.deploy_group_id
        if not UtilClient.is_unset(request.listener_health_check_url):
            query['ListenerHealthCheckUrl'] = request.listener_health_check_url
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.slb_id):
            query['SlbId'] = request.slb_id
        if not UtilClient.is_unset(request.vforwarding_url_rule):
            query['VForwardingUrlRule'] = request.vforwarding_url_rule
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.vserver_group_name):
            query['VServerGroupName'] = request.vserver_group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindEcsSlb',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/slb/bind_slb',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.BindEcsSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_ecs_slb(
        self,
        request: edas_20170801_models.BindEcsSlbRequest,
    ) -> edas_20170801_models.BindEcsSlbResponse:
        """
        @summary Binds a Server Load Balancer (SLB) instance to an application that is deployed in an Elastic Compute Service (ECS) cluster.
        
        @param request: BindEcsSlbRequest
        @return: BindEcsSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.bind_ecs_slb_with_options(request, headers, runtime)

    async def bind_ecs_slb_async(
        self,
        request: edas_20170801_models.BindEcsSlbRequest,
    ) -> edas_20170801_models.BindEcsSlbResponse:
        """
        @summary Binds a Server Load Balancer (SLB) instance to an application that is deployed in an Elastic Compute Service (ECS) cluster.
        
        @param request: BindEcsSlbRequest
        @return: BindEcsSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.bind_ecs_slb_with_options_async(request, headers, runtime)

    def bind_k8s_slb_with_options(
        self,
        request: edas_20170801_models.BindK8sSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.BindK8sSlbResponse:
        """
        @summary Binds a Server Load Balancer (SLB) instance to an application that is deployed in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: BindK8sSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindK8sSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.service_port_infos):
            query['ServicePortInfos'] = request.service_port_infos
        if not UtilClient.is_unset(request.slb_id):
            query['SlbId'] = request.slb_id
        if not UtilClient.is_unset(request.slb_protocol):
            query['SlbProtocol'] = request.slb_protocol
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.target_port):
            query['TargetPort'] = request.target_port
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindK8sSlb',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_slb_binding',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.BindK8sSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_k8s_slb_with_options_async(
        self,
        request: edas_20170801_models.BindK8sSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.BindK8sSlbResponse:
        """
        @summary Binds a Server Load Balancer (SLB) instance to an application that is deployed in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: BindK8sSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindK8sSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.service_port_infos):
            query['ServicePortInfos'] = request.service_port_infos
        if not UtilClient.is_unset(request.slb_id):
            query['SlbId'] = request.slb_id
        if not UtilClient.is_unset(request.slb_protocol):
            query['SlbProtocol'] = request.slb_protocol
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.target_port):
            query['TargetPort'] = request.target_port
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindK8sSlb',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_slb_binding',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.BindK8sSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_k8s_slb(
        self,
        request: edas_20170801_models.BindK8sSlbRequest,
    ) -> edas_20170801_models.BindK8sSlbResponse:
        """
        @summary Binds a Server Load Balancer (SLB) instance to an application that is deployed in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: BindK8sSlbRequest
        @return: BindK8sSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.bind_k8s_slb_with_options(request, headers, runtime)

    async def bind_k8s_slb_async(
        self,
        request: edas_20170801_models.BindK8sSlbRequest,
    ) -> edas_20170801_models.BindK8sSlbResponse:
        """
        @summary Binds a Server Load Balancer (SLB) instance to an application that is deployed in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: BindK8sSlbRequest
        @return: BindK8sSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.bind_k8s_slb_with_options_async(request, headers, runtime)

    def bind_slb_with_options(
        self,
        request: edas_20170801_models.BindSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.BindSlbResponse:
        """
        @summary Binds a Server Load Balancer (SLB) instance to an application in Enterprise Distributed Application Service (EDAS).
        
        @param request: BindSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.slb_id):
            query['SlbId'] = request.slb_id
        if not UtilClient.is_unset(request.slb_ip):
            query['SlbIp'] = request.slb_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindSlb',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/app/bind_slb_json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.BindSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_slb_with_options_async(
        self,
        request: edas_20170801_models.BindSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.BindSlbResponse:
        """
        @summary Binds a Server Load Balancer (SLB) instance to an application in Enterprise Distributed Application Service (EDAS).
        
        @param request: BindSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.slb_id):
            query['SlbId'] = request.slb_id
        if not UtilClient.is_unset(request.slb_ip):
            query['SlbIp'] = request.slb_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindSlb',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/app/bind_slb_json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.BindSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_slb(
        self,
        request: edas_20170801_models.BindSlbRequest,
    ) -> edas_20170801_models.BindSlbResponse:
        """
        @summary Binds a Server Load Balancer (SLB) instance to an application in Enterprise Distributed Application Service (EDAS).
        
        @param request: BindSlbRequest
        @return: BindSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.bind_slb_with_options(request, headers, runtime)

    async def bind_slb_async(
        self,
        request: edas_20170801_models.BindSlbRequest,
    ) -> edas_20170801_models.BindSlbResponse:
        """
        @summary Binds a Server Load Balancer (SLB) instance to an application in Enterprise Distributed Application Service (EDAS).
        
        @param request: BindSlbRequest
        @return: BindSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.bind_slb_with_options_async(request, headers, runtime)

    def change_deploy_group_with_options(
        self,
        request: edas_20170801_models.ChangeDeployGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ChangeDeployGroupResponse:
        """
        @summary Changes the application instance group for an Elastic Compute Service (ECS) instance in an ECS cluster.
        
        @param request: ChangeDeployGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeDeployGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        if not UtilClient.is_unset(request.force_status):
            query['ForceStatus'] = request.force_status
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeDeployGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_change_group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ChangeDeployGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_deploy_group_with_options_async(
        self,
        request: edas_20170801_models.ChangeDeployGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ChangeDeployGroupResponse:
        """
        @summary Changes the application instance group for an Elastic Compute Service (ECS) instance in an ECS cluster.
        
        @param request: ChangeDeployGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeDeployGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        if not UtilClient.is_unset(request.force_status):
            query['ForceStatus'] = request.force_status
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeDeployGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_change_group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ChangeDeployGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_deploy_group(
        self,
        request: edas_20170801_models.ChangeDeployGroupRequest,
    ) -> edas_20170801_models.ChangeDeployGroupResponse:
        """
        @summary Changes the application instance group for an Elastic Compute Service (ECS) instance in an ECS cluster.
        
        @param request: ChangeDeployGroupRequest
        @return: ChangeDeployGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.change_deploy_group_with_options(request, headers, runtime)

    async def change_deploy_group_async(
        self,
        request: edas_20170801_models.ChangeDeployGroupRequest,
    ) -> edas_20170801_models.ChangeDeployGroupResponse:
        """
        @summary Changes the application instance group for an Elastic Compute Service (ECS) instance in an ECS cluster.
        
        @param request: ChangeDeployGroupRequest
        @return: ChangeDeployGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.change_deploy_group_with_options_async(request, headers, runtime)

    def continue_pipeline_with_options(
        self,
        request: edas_20170801_models.ContinuePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ContinuePipelineResponse:
        """
        @summary Manually confirms the release of the next batch.
        
        @param request: ContinuePipelineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContinuePipelineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.confirm):
            query['Confirm'] = request.confirm
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinuePipeline',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/pipeline_batch_confirm',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ContinuePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def continue_pipeline_with_options_async(
        self,
        request: edas_20170801_models.ContinuePipelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ContinuePipelineResponse:
        """
        @summary Manually confirms the release of the next batch.
        
        @param request: ContinuePipelineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContinuePipelineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.confirm):
            query['Confirm'] = request.confirm
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinuePipeline',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/pipeline_batch_confirm',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ContinuePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continue_pipeline(
        self,
        request: edas_20170801_models.ContinuePipelineRequest,
    ) -> edas_20170801_models.ContinuePipelineResponse:
        """
        @summary Manually confirms the release of the next batch.
        
        @param request: ContinuePipelineRequest
        @return: ContinuePipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.continue_pipeline_with_options(request, headers, runtime)

    async def continue_pipeline_async(
        self,
        request: edas_20170801_models.ContinuePipelineRequest,
    ) -> edas_20170801_models.ContinuePipelineResponse:
        """
        @summary Manually confirms the release of the next batch.
        
        @param request: ContinuePipelineRequest
        @return: ContinuePipelineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.continue_pipeline_with_options_async(request, headers, runtime)

    def convert_k8s_resource_with_options(
        self,
        request: edas_20170801_models.ConvertK8sResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ConvertK8sResourceResponse:
        """
        @summary Converts a Deployment into an application.
        
        @param request: ConvertK8sResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertK8sResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConvertK8sResource',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/oam/k8s_resource_convert',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ConvertK8sResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_k8s_resource_with_options_async(
        self,
        request: edas_20170801_models.ConvertK8sResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ConvertK8sResourceResponse:
        """
        @summary Converts a Deployment into an application.
        
        @param request: ConvertK8sResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConvertK8sResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConvertK8sResource',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/oam/k8s_resource_convert',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ConvertK8sResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_k8s_resource(
        self,
        request: edas_20170801_models.ConvertK8sResourceRequest,
    ) -> edas_20170801_models.ConvertK8sResourceResponse:
        """
        @summary Converts a Deployment into an application.
        
        @param request: ConvertK8sResourceRequest
        @return: ConvertK8sResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.convert_k8s_resource_with_options(request, headers, runtime)

    async def convert_k8s_resource_async(
        self,
        request: edas_20170801_models.ConvertK8sResourceRequest,
    ) -> edas_20170801_models.ConvertK8sResourceResponse:
        """
        @summary Converts a Deployment into an application.
        
        @param request: ConvertK8sResourceRequest
        @return: ConvertK8sResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.convert_k8s_resource_with_options_async(request, headers, runtime)

    def create_application_scaling_rule_with_options(
        self,
        request: edas_20170801_models.CreateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.CreateApplicationScalingRuleResponse:
        """
        @summary Creates an auto scaling policy for an application.
        
        @param request: CreateApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_behaviour):
            query['ScalingBehaviour'] = request.scaling_behaviour
        if not UtilClient.is_unset(request.scaling_rule_enable):
            query['ScalingRuleEnable'] = request.scaling_rule_enable
        if not UtilClient.is_unset(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        if not UtilClient.is_unset(request.scaling_rule_trigger):
            query['ScalingRuleTrigger'] = request.scaling_rule_trigger
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationScalingRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v1/eam/scale/application_scaling_rule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.CreateApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_scaling_rule_with_options_async(
        self,
        request: edas_20170801_models.CreateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.CreateApplicationScalingRuleResponse:
        """
        @summary Creates an auto scaling policy for an application.
        
        @param request: CreateApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_behaviour):
            query['ScalingBehaviour'] = request.scaling_behaviour
        if not UtilClient.is_unset(request.scaling_rule_enable):
            query['ScalingRuleEnable'] = request.scaling_rule_enable
        if not UtilClient.is_unset(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        if not UtilClient.is_unset(request.scaling_rule_trigger):
            query['ScalingRuleTrigger'] = request.scaling_rule_trigger
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationScalingRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v1/eam/scale/application_scaling_rule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.CreateApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_scaling_rule(
        self,
        request: edas_20170801_models.CreateApplicationScalingRuleRequest,
    ) -> edas_20170801_models.CreateApplicationScalingRuleResponse:
        """
        @summary Creates an auto scaling policy for an application.
        
        @param request: CreateApplicationScalingRuleRequest
        @return: CreateApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_application_scaling_rule_with_options(request, headers, runtime)

    async def create_application_scaling_rule_async(
        self,
        request: edas_20170801_models.CreateApplicationScalingRuleRequest,
    ) -> edas_20170801_models.CreateApplicationScalingRuleResponse:
        """
        @summary Creates an auto scaling policy for an application.
        
        @param request: CreateApplicationScalingRuleRequest
        @return: CreateApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_application_scaling_rule_with_options_async(request, headers, runtime)

    def create_config_template_with_options(
        self,
        request: edas_20170801_models.CreateConfigTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.CreateConfigTemplateResponse:
        """
        @summary Creates a configuration template.
        
        @param request: CreateConfigTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConfigTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.format):
            body['Format'] = request.format
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigTemplate',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/config_template',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.CreateConfigTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_config_template_with_options_async(
        self,
        request: edas_20170801_models.CreateConfigTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.CreateConfigTemplateResponse:
        """
        @summary Creates a configuration template.
        
        @param request: CreateConfigTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConfigTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.format):
            body['Format'] = request.format
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigTemplate',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/config_template',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.CreateConfigTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_config_template(
        self,
        request: edas_20170801_models.CreateConfigTemplateRequest,
    ) -> edas_20170801_models.CreateConfigTemplateResponse:
        """
        @summary Creates a configuration template.
        
        @param request: CreateConfigTemplateRequest
        @return: CreateConfigTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_config_template_with_options(request, headers, runtime)

    async def create_config_template_async(
        self,
        request: edas_20170801_models.CreateConfigTemplateRequest,
    ) -> edas_20170801_models.CreateConfigTemplateResponse:
        """
        @summary Creates a configuration template.
        
        @param request: CreateConfigTemplateRequest
        @return: CreateConfigTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_config_template_with_options_async(request, headers, runtime)

    def create_idcimport_command_with_options(
        self,
        request: edas_20170801_models.CreateIDCImportCommandRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.CreateIDCImportCommandResponse:
        """
        @summary Generates a command that is used to import instances to a hybrid cloud Elastic Compute Service (ECS) cluster.
        
        @description ## Description
        You must call the CreateIDCImportCommand operation first to generate a command used to import hybrid cloud ECS instances to a hybrid cloud ECS cluster. Then, run this command on the instances to import the instances to the cluster.
        
        @param request: CreateIDCImportCommandRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIDCImportCommandResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIDCImportCommand',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/create_idc_import_command',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.CreateIDCImportCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_idcimport_command_with_options_async(
        self,
        request: edas_20170801_models.CreateIDCImportCommandRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.CreateIDCImportCommandResponse:
        """
        @summary Generates a command that is used to import instances to a hybrid cloud Elastic Compute Service (ECS) cluster.
        
        @description ## Description
        You must call the CreateIDCImportCommand operation first to generate a command used to import hybrid cloud ECS instances to a hybrid cloud ECS cluster. Then, run this command on the instances to import the instances to the cluster.
        
        @param request: CreateIDCImportCommandRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIDCImportCommandResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIDCImportCommand',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/create_idc_import_command',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.CreateIDCImportCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_idcimport_command(
        self,
        request: edas_20170801_models.CreateIDCImportCommandRequest,
    ) -> edas_20170801_models.CreateIDCImportCommandResponse:
        """
        @summary Generates a command that is used to import instances to a hybrid cloud Elastic Compute Service (ECS) cluster.
        
        @description ## Description
        You must call the CreateIDCImportCommand operation first to generate a command used to import hybrid cloud ECS instances to a hybrid cloud ECS cluster. Then, run this command on the instances to import the instances to the cluster.
        
        @param request: CreateIDCImportCommandRequest
        @return: CreateIDCImportCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_idcimport_command_with_options(request, headers, runtime)

    async def create_idcimport_command_async(
        self,
        request: edas_20170801_models.CreateIDCImportCommandRequest,
    ) -> edas_20170801_models.CreateIDCImportCommandResponse:
        """
        @summary Generates a command that is used to import instances to a hybrid cloud Elastic Compute Service (ECS) cluster.
        
        @description ## Description
        You must call the CreateIDCImportCommand operation first to generate a command used to import hybrid cloud ECS instances to a hybrid cloud ECS cluster. Then, run this command on the instances to import the instances to the cluster.
        
        @param request: CreateIDCImportCommandRequest
        @return: CreateIDCImportCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_idcimport_command_with_options_async(request, headers, runtime)

    def create_k8s_config_map_with_options(
        self,
        request: edas_20170801_models.CreateK8sConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.CreateK8sConfigMapResponse:
        """
        @summary Creates a Kubernetes ConfigMap.
        
        @param request: CreateK8sConfigMapRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateK8sConfigMapResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateK8sConfigMap',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_config_map',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.CreateK8sConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_k8s_config_map_with_options_async(
        self,
        request: edas_20170801_models.CreateK8sConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.CreateK8sConfigMapResponse:
        """
        @summary Creates a Kubernetes ConfigMap.
        
        @param request: CreateK8sConfigMapRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateK8sConfigMapResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateK8sConfigMap',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_config_map',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.CreateK8sConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_k8s_config_map(
        self,
        request: edas_20170801_models.CreateK8sConfigMapRequest,
    ) -> edas_20170801_models.CreateK8sConfigMapResponse:
        """
        @summary Creates a Kubernetes ConfigMap.
        
        @param request: CreateK8sConfigMapRequest
        @return: CreateK8sConfigMapResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_k8s_config_map_with_options(request, headers, runtime)

    async def create_k8s_config_map_async(
        self,
        request: edas_20170801_models.CreateK8sConfigMapRequest,
    ) -> edas_20170801_models.CreateK8sConfigMapResponse:
        """
        @summary Creates a Kubernetes ConfigMap.
        
        @param request: CreateK8sConfigMapRequest
        @return: CreateK8sConfigMapResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_k8s_config_map_with_options_async(request, headers, runtime)

    def create_k8s_ingress_rule_with_options(
        self,
        request: edas_20170801_models.CreateK8sIngressRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.CreateK8sIngressRuleResponse:
        """
        @summary Creates an Ingress.
        
        @param request: CreateK8sIngressRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateK8sIngressRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ingress_conf):
            query['IngressConf'] = request.ingress_conf
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateK8sIngressRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_ingress',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.CreateK8sIngressRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_k8s_ingress_rule_with_options_async(
        self,
        request: edas_20170801_models.CreateK8sIngressRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.CreateK8sIngressRuleResponse:
        """
        @summary Creates an Ingress.
        
        @param request: CreateK8sIngressRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateK8sIngressRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ingress_conf):
            query['IngressConf'] = request.ingress_conf
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateK8sIngressRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_ingress',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.CreateK8sIngressRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_k8s_ingress_rule(
        self,
        request: edas_20170801_models.CreateK8sIngressRuleRequest,
    ) -> edas_20170801_models.CreateK8sIngressRuleResponse:
        """
        @summary Creates an Ingress.
        
        @param request: CreateK8sIngressRuleRequest
        @return: CreateK8sIngressRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_k8s_ingress_rule_with_options(request, headers, runtime)

    async def create_k8s_ingress_rule_async(
        self,
        request: edas_20170801_models.CreateK8sIngressRuleRequest,
    ) -> edas_20170801_models.CreateK8sIngressRuleResponse:
        """
        @summary Creates an Ingress.
        
        @param request: CreateK8sIngressRuleRequest
        @return: CreateK8sIngressRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_k8s_ingress_rule_with_options_async(request, headers, runtime)

    def create_k8s_secret_with_options(
        self,
        request: edas_20170801_models.CreateK8sSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.CreateK8sSecretResponse:
        """
        @summary Creates a Kubernetes Secret.
        
        @param request: CreateK8sSecretRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateK8sSecretResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_64encoded):
            body['Base64Encoded'] = request.base_64encoded
        if not UtilClient.is_unset(request.cert_id):
            body['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_region_id):
            body['CertRegionId'] = request.cert_region_id
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateK8sSecret',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_secret',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.CreateK8sSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_k8s_secret_with_options_async(
        self,
        request: edas_20170801_models.CreateK8sSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.CreateK8sSecretResponse:
        """
        @summary Creates a Kubernetes Secret.
        
        @param request: CreateK8sSecretRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateK8sSecretResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_64encoded):
            body['Base64Encoded'] = request.base_64encoded
        if not UtilClient.is_unset(request.cert_id):
            body['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_region_id):
            body['CertRegionId'] = request.cert_region_id
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateK8sSecret',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_secret',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.CreateK8sSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_k8s_secret(
        self,
        request: edas_20170801_models.CreateK8sSecretRequest,
    ) -> edas_20170801_models.CreateK8sSecretResponse:
        """
        @summary Creates a Kubernetes Secret.
        
        @param request: CreateK8sSecretRequest
        @return: CreateK8sSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_k8s_secret_with_options(request, headers, runtime)

    async def create_k8s_secret_async(
        self,
        request: edas_20170801_models.CreateK8sSecretRequest,
    ) -> edas_20170801_models.CreateK8sSecretResponse:
        """
        @summary Creates a Kubernetes Secret.
        
        @param request: CreateK8sSecretRequest
        @return: CreateK8sSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_k8s_secret_with_options_async(request, headers, runtime)

    def create_k8s_service_with_options(
        self,
        request: edas_20170801_models.CreateK8sServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.CreateK8sServiceResponse:
        """
        @summary Creates an application service in a Kubernetes cluster.
        
        @param request: CreateK8sServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateK8sServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.external_traffic_policy):
            query['ExternalTrafficPolicy'] = request.external_traffic_policy
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.service_ports):
            query['ServicePorts'] = request.service_ports
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateK8sService',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_service',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.CreateK8sServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_k8s_service_with_options_async(
        self,
        request: edas_20170801_models.CreateK8sServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.CreateK8sServiceResponse:
        """
        @summary Creates an application service in a Kubernetes cluster.
        
        @param request: CreateK8sServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateK8sServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.external_traffic_policy):
            query['ExternalTrafficPolicy'] = request.external_traffic_policy
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.service_ports):
            query['ServicePorts'] = request.service_ports
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateK8sService',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_service',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.CreateK8sServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_k8s_service(
        self,
        request: edas_20170801_models.CreateK8sServiceRequest,
    ) -> edas_20170801_models.CreateK8sServiceResponse:
        """
        @summary Creates an application service in a Kubernetes cluster.
        
        @param request: CreateK8sServiceRequest
        @return: CreateK8sServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_k8s_service_with_options(request, headers, runtime)

    async def create_k8s_service_async(
        self,
        request: edas_20170801_models.CreateK8sServiceRequest,
    ) -> edas_20170801_models.CreateK8sServiceResponse:
        """
        @summary Creates an application service in a Kubernetes cluster.
        
        @param request: CreateK8sServiceRequest
        @return: CreateK8sServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_k8s_service_with_options_async(request, headers, runtime)

    def delete_application_with_options(
        self,
        request: edas_20170801_models.DeleteApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteApplicationResponse:
        """
        @summary Deletes an application.
        
        @param request: DeleteApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_delete_app',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: edas_20170801_models.DeleteApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteApplicationResponse:
        """
        @summary Deletes an application.
        
        @param request: DeleteApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_delete_app',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application(
        self,
        request: edas_20170801_models.DeleteApplicationRequest,
    ) -> edas_20170801_models.DeleteApplicationResponse:
        """
        @summary Deletes an application.
        
        @param request: DeleteApplicationRequest
        @return: DeleteApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_application_with_options(request, headers, runtime)

    async def delete_application_async(
        self,
        request: edas_20170801_models.DeleteApplicationRequest,
    ) -> edas_20170801_models.DeleteApplicationResponse:
        """
        @summary Deletes an application.
        
        @param request: DeleteApplicationRequest
        @return: DeleteApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_application_with_options_async(request, headers, runtime)

    def delete_application_scaling_rule_with_options(
        self,
        request: edas_20170801_models.DeleteApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteApplicationScalingRuleResponse:
        """
        @summary Deletes an auto scaling policy for an application.
        
        @param request: DeleteApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationScalingRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v1/eam/scale/application_scaling_rule',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_scaling_rule_with_options_async(
        self,
        request: edas_20170801_models.DeleteApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteApplicationScalingRuleResponse:
        """
        @summary Deletes an auto scaling policy for an application.
        
        @param request: DeleteApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationScalingRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v1/eam/scale/application_scaling_rule',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application_scaling_rule(
        self,
        request: edas_20170801_models.DeleteApplicationScalingRuleRequest,
    ) -> edas_20170801_models.DeleteApplicationScalingRuleResponse:
        """
        @summary Deletes an auto scaling policy for an application.
        
        @param request: DeleteApplicationScalingRuleRequest
        @return: DeleteApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_application_scaling_rule_with_options(request, headers, runtime)

    async def delete_application_scaling_rule_async(
        self,
        request: edas_20170801_models.DeleteApplicationScalingRuleRequest,
    ) -> edas_20170801_models.DeleteApplicationScalingRuleResponse:
        """
        @summary Deletes an auto scaling policy for an application.
        
        @param request: DeleteApplicationScalingRuleRequest
        @return: DeleteApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_application_scaling_rule_with_options_async(request, headers, runtime)

    def delete_cluster_with_options(
        self,
        request: edas_20170801_models.DeleteClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteClusterResponse:
        """
        @summary Deletes an Elastic Compute Service (ECS) cluster or cancels the import of a Container Service for Kubernetes (ACK) cluster.
        
        @param request: DeleteClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/cluster',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: edas_20170801_models.DeleteClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteClusterResponse:
        """
        @summary Deletes an Elastic Compute Service (ECS) cluster or cancels the import of a Container Service for Kubernetes (ACK) cluster.
        
        @param request: DeleteClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/cluster',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        request: edas_20170801_models.DeleteClusterRequest,
    ) -> edas_20170801_models.DeleteClusterResponse:
        """
        @summary Deletes an Elastic Compute Service (ECS) cluster or cancels the import of a Container Service for Kubernetes (ACK) cluster.
        
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_cluster_with_options(request, headers, runtime)

    async def delete_cluster_async(
        self,
        request: edas_20170801_models.DeleteClusterRequest,
    ) -> edas_20170801_models.DeleteClusterResponse:
        """
        @summary Deletes an Elastic Compute Service (ECS) cluster or cancels the import of a Container Service for Kubernetes (ACK) cluster.
        
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_cluster_with_options_async(request, headers, runtime)

    def delete_cluster_member_with_options(
        self,
        request: edas_20170801_models.DeleteClusterMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteClusterMemberResponse:
        """
        @summary Removes an Elastic Compute Service (ECS) instance from a cluster.
        
        @param request: DeleteClusterMemberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_member_id):
            query['ClusterMemberId'] = request.cluster_member_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClusterMember',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/cluster_member',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteClusterMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_member_with_options_async(
        self,
        request: edas_20170801_models.DeleteClusterMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteClusterMemberResponse:
        """
        @summary Removes an Elastic Compute Service (ECS) instance from a cluster.
        
        @param request: DeleteClusterMemberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_member_id):
            query['ClusterMemberId'] = request.cluster_member_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClusterMember',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/cluster_member',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteClusterMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster_member(
        self,
        request: edas_20170801_models.DeleteClusterMemberRequest,
    ) -> edas_20170801_models.DeleteClusterMemberResponse:
        """
        @summary Removes an Elastic Compute Service (ECS) instance from a cluster.
        
        @param request: DeleteClusterMemberRequest
        @return: DeleteClusterMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_cluster_member_with_options(request, headers, runtime)

    async def delete_cluster_member_async(
        self,
        request: edas_20170801_models.DeleteClusterMemberRequest,
    ) -> edas_20170801_models.DeleteClusterMemberResponse:
        """
        @summary Removes an Elastic Compute Service (ECS) instance from a cluster.
        
        @param request: DeleteClusterMemberRequest
        @return: DeleteClusterMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_cluster_member_with_options_async(request, headers, runtime)

    def delete_config_template_with_options(
        self,
        request: edas_20170801_models.DeleteConfigTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteConfigTemplateResponse:
        """
        @summary Deletes a configuration template.
        
        @param request: DeleteConfigTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfigTemplate',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/config_template',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteConfigTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_config_template_with_options_async(
        self,
        request: edas_20170801_models.DeleteConfigTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteConfigTemplateResponse:
        """
        @summary Deletes a configuration template.
        
        @param request: DeleteConfigTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfigTemplate',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/config_template',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteConfigTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_config_template(
        self,
        request: edas_20170801_models.DeleteConfigTemplateRequest,
    ) -> edas_20170801_models.DeleteConfigTemplateResponse:
        """
        @summary Deletes a configuration template.
        
        @param request: DeleteConfigTemplateRequest
        @return: DeleteConfigTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_config_template_with_options(request, headers, runtime)

    async def delete_config_template_async(
        self,
        request: edas_20170801_models.DeleteConfigTemplateRequest,
    ) -> edas_20170801_models.DeleteConfigTemplateResponse:
        """
        @summary Deletes a configuration template.
        
        @param request: DeleteConfigTemplateRequest
        @return: DeleteConfigTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_config_template_with_options_async(request, headers, runtime)

    def delete_deploy_group_with_options(
        self,
        request: edas_20170801_models.DeleteDeployGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteDeployGroupResponse:
        """
        @summary Deletes an instance group for an application.
        
        @param request: DeleteDeployGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeployGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeployGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/deploy_group',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteDeployGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_deploy_group_with_options_async(
        self,
        request: edas_20170801_models.DeleteDeployGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteDeployGroupResponse:
        """
        @summary Deletes an instance group for an application.
        
        @param request: DeleteDeployGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeployGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeployGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/deploy_group',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteDeployGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_deploy_group(
        self,
        request: edas_20170801_models.DeleteDeployGroupRequest,
    ) -> edas_20170801_models.DeleteDeployGroupResponse:
        """
        @summary Deletes an instance group for an application.
        
        @param request: DeleteDeployGroupRequest
        @return: DeleteDeployGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_deploy_group_with_options(request, headers, runtime)

    async def delete_deploy_group_async(
        self,
        request: edas_20170801_models.DeleteDeployGroupRequest,
    ) -> edas_20170801_models.DeleteDeployGroupResponse:
        """
        @summary Deletes an instance group for an application.
        
        @param request: DeleteDeployGroupRequest
        @return: DeleteDeployGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_deploy_group_with_options_async(request, headers, runtime)

    def delete_ecu_with_options(
        self,
        request: edas_20170801_models.DeleteEcuRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteEcuResponse:
        """
        @summary Deletes an Elastic Compute Unit (ECU).
        
        @param request: DeleteEcuRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEcuResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecu_id):
            query['EcuId'] = request.ecu_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEcu',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/delete_ecu',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteEcuResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ecu_with_options_async(
        self,
        request: edas_20170801_models.DeleteEcuRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteEcuResponse:
        """
        @summary Deletes an Elastic Compute Unit (ECU).
        
        @param request: DeleteEcuRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEcuResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecu_id):
            query['EcuId'] = request.ecu_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEcu',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/delete_ecu',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteEcuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ecu(
        self,
        request: edas_20170801_models.DeleteEcuRequest,
    ) -> edas_20170801_models.DeleteEcuResponse:
        """
        @summary Deletes an Elastic Compute Unit (ECU).
        
        @param request: DeleteEcuRequest
        @return: DeleteEcuResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_ecu_with_options(request, headers, runtime)

    async def delete_ecu_async(
        self,
        request: edas_20170801_models.DeleteEcuRequest,
    ) -> edas_20170801_models.DeleteEcuResponse:
        """
        @summary Deletes an Elastic Compute Unit (ECU).
        
        @param request: DeleteEcuRequest
        @return: DeleteEcuResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_ecu_with_options_async(request, headers, runtime)

    def delete_k8s_application_with_options(
        self,
        request: edas_20170801_models.DeleteK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteK8sApplicationResponse:
        """
        @summary Deletes an application from a Container Service for Kubernetes (ACK) cluster.
        
        @param request: DeleteK8sApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteK8sApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteK8sApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_apps',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteK8sApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_k8s_application_with_options_async(
        self,
        request: edas_20170801_models.DeleteK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteK8sApplicationResponse:
        """
        @summary Deletes an application from a Container Service for Kubernetes (ACK) cluster.
        
        @param request: DeleteK8sApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteK8sApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteK8sApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_apps',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteK8sApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_k8s_application(
        self,
        request: edas_20170801_models.DeleteK8sApplicationRequest,
    ) -> edas_20170801_models.DeleteK8sApplicationResponse:
        """
        @summary Deletes an application from a Container Service for Kubernetes (ACK) cluster.
        
        @param request: DeleteK8sApplicationRequest
        @return: DeleteK8sApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_k8s_application_with_options(request, headers, runtime)

    async def delete_k8s_application_async(
        self,
        request: edas_20170801_models.DeleteK8sApplicationRequest,
    ) -> edas_20170801_models.DeleteK8sApplicationResponse:
        """
        @summary Deletes an application from a Container Service for Kubernetes (ACK) cluster.
        
        @param request: DeleteK8sApplicationRequest
        @return: DeleteK8sApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_k8s_application_with_options_async(request, headers, runtime)

    def delete_k8s_config_map_with_options(
        self,
        request: edas_20170801_models.DeleteK8sConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteK8sConfigMapResponse:
        """
        @summary Deletes a Kubernetes ConfigMap.
        
        @param request: DeleteK8sConfigMapRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteK8sConfigMapResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteK8sConfigMap',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_config_map',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteK8sConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_k8s_config_map_with_options_async(
        self,
        request: edas_20170801_models.DeleteK8sConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteK8sConfigMapResponse:
        """
        @summary Deletes a Kubernetes ConfigMap.
        
        @param request: DeleteK8sConfigMapRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteK8sConfigMapResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteK8sConfigMap',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_config_map',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteK8sConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_k8s_config_map(
        self,
        request: edas_20170801_models.DeleteK8sConfigMapRequest,
    ) -> edas_20170801_models.DeleteK8sConfigMapResponse:
        """
        @summary Deletes a Kubernetes ConfigMap.
        
        @param request: DeleteK8sConfigMapRequest
        @return: DeleteK8sConfigMapResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_k8s_config_map_with_options(request, headers, runtime)

    async def delete_k8s_config_map_async(
        self,
        request: edas_20170801_models.DeleteK8sConfigMapRequest,
    ) -> edas_20170801_models.DeleteK8sConfigMapResponse:
        """
        @summary Deletes a Kubernetes ConfigMap.
        
        @param request: DeleteK8sConfigMapRequest
        @return: DeleteK8sConfigMapResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_k8s_config_map_with_options_async(request, headers, runtime)

    def delete_k8s_ingress_rule_with_options(
        self,
        request: edas_20170801_models.DeleteK8sIngressRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteK8sIngressRuleResponse:
        """
        @summary Deletes an ingress.
        
        @param request: DeleteK8sIngressRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteK8sIngressRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteK8sIngressRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_ingress',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteK8sIngressRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_k8s_ingress_rule_with_options_async(
        self,
        request: edas_20170801_models.DeleteK8sIngressRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteK8sIngressRuleResponse:
        """
        @summary Deletes an ingress.
        
        @param request: DeleteK8sIngressRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteK8sIngressRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteK8sIngressRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_ingress',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteK8sIngressRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_k8s_ingress_rule(
        self,
        request: edas_20170801_models.DeleteK8sIngressRuleRequest,
    ) -> edas_20170801_models.DeleteK8sIngressRuleResponse:
        """
        @summary Deletes an ingress.
        
        @param request: DeleteK8sIngressRuleRequest
        @return: DeleteK8sIngressRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_k8s_ingress_rule_with_options(request, headers, runtime)

    async def delete_k8s_ingress_rule_async(
        self,
        request: edas_20170801_models.DeleteK8sIngressRuleRequest,
    ) -> edas_20170801_models.DeleteK8sIngressRuleResponse:
        """
        @summary Deletes an ingress.
        
        @param request: DeleteK8sIngressRuleRequest
        @return: DeleteK8sIngressRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_k8s_ingress_rule_with_options_async(request, headers, runtime)

    def delete_k8s_secret_with_options(
        self,
        request: edas_20170801_models.DeleteK8sSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteK8sSecretResponse:
        """
        @summary Deletes a Kubernetes Secret.
        
        @param request: DeleteK8sSecretRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteK8sSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteK8sSecret',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_secret',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteK8sSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_k8s_secret_with_options_async(
        self,
        request: edas_20170801_models.DeleteK8sSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteK8sSecretResponse:
        """
        @summary Deletes a Kubernetes Secret.
        
        @param request: DeleteK8sSecretRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteK8sSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteK8sSecret',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_secret',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteK8sSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_k8s_secret(
        self,
        request: edas_20170801_models.DeleteK8sSecretRequest,
    ) -> edas_20170801_models.DeleteK8sSecretResponse:
        """
        @summary Deletes a Kubernetes Secret.
        
        @param request: DeleteK8sSecretRequest
        @return: DeleteK8sSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_k8s_secret_with_options(request, headers, runtime)

    async def delete_k8s_secret_async(
        self,
        request: edas_20170801_models.DeleteK8sSecretRequest,
    ) -> edas_20170801_models.DeleteK8sSecretResponse:
        """
        @summary Deletes a Kubernetes Secret.
        
        @param request: DeleteK8sSecretRequest
        @return: DeleteK8sSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_k8s_secret_with_options_async(request, headers, runtime)

    def delete_k8s_service_with_options(
        self,
        request: edas_20170801_models.DeleteK8sServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteK8sServiceResponse:
        """
        @summary Deletes an application service from a Kubernetes cluster.
        
        @param request: DeleteK8sServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteK8sServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteK8sService',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_service',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteK8sServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_k8s_service_with_options_async(
        self,
        request: edas_20170801_models.DeleteK8sServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteK8sServiceResponse:
        """
        @summary Deletes an application service from a Kubernetes cluster.
        
        @param request: DeleteK8sServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteK8sServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteK8sService',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_service',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteK8sServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_k8s_service(
        self,
        request: edas_20170801_models.DeleteK8sServiceRequest,
    ) -> edas_20170801_models.DeleteK8sServiceResponse:
        """
        @summary Deletes an application service from a Kubernetes cluster.
        
        @param request: DeleteK8sServiceRequest
        @return: DeleteK8sServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_k8s_service_with_options(request, headers, runtime)

    async def delete_k8s_service_async(
        self,
        request: edas_20170801_models.DeleteK8sServiceRequest,
    ) -> edas_20170801_models.DeleteK8sServiceResponse:
        """
        @summary Deletes an application service from a Kubernetes cluster.
        
        @param request: DeleteK8sServiceRequest
        @return: DeleteK8sServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_k8s_service_with_options_async(request, headers, runtime)

    def delete_log_path_with_options(
        self,
        request: edas_20170801_models.DeleteLogPathRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteLogPathResponse:
        """
        @summary Removes a log directory from an application. This operation is applicable to applications that are deployed in Alibaba Cloud Elastic Compute Service (ECS) clusters and hybrid cloud ECS clusters.
        
        @param request: DeleteLogPathRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLogPathResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLogPath',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/log/popListLogDirs',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteLogPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_log_path_with_options_async(
        self,
        request: edas_20170801_models.DeleteLogPathRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteLogPathResponse:
        """
        @summary Removes a log directory from an application. This operation is applicable to applications that are deployed in Alibaba Cloud Elastic Compute Service (ECS) clusters and hybrid cloud ECS clusters.
        
        @param request: DeleteLogPathRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLogPathResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLogPath',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/log/popListLogDirs',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteLogPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_log_path(
        self,
        request: edas_20170801_models.DeleteLogPathRequest,
    ) -> edas_20170801_models.DeleteLogPathResponse:
        """
        @summary Removes a log directory from an application. This operation is applicable to applications that are deployed in Alibaba Cloud Elastic Compute Service (ECS) clusters and hybrid cloud ECS clusters.
        
        @param request: DeleteLogPathRequest
        @return: DeleteLogPathResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_log_path_with_options(request, headers, runtime)

    async def delete_log_path_async(
        self,
        request: edas_20170801_models.DeleteLogPathRequest,
    ) -> edas_20170801_models.DeleteLogPathResponse:
        """
        @summary Removes a log directory from an application. This operation is applicable to applications that are deployed in Alibaba Cloud Elastic Compute Service (ECS) clusters and hybrid cloud ECS clusters.
        
        @param request: DeleteLogPathRequest
        @return: DeleteLogPathResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_log_path_with_options_async(request, headers, runtime)

    def delete_role_with_options(
        self,
        request: edas_20170801_models.DeleteRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteRoleResponse:
        """
        @summary Deletes a Resource Access Management (RAM) role.
        
        @param request: DeleteRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRole',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/delete_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_role_with_options_async(
        self,
        request: edas_20170801_models.DeleteRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteRoleResponse:
        """
        @summary Deletes a Resource Access Management (RAM) role.
        
        @param request: DeleteRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRole',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/delete_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_role(
        self,
        request: edas_20170801_models.DeleteRoleRequest,
    ) -> edas_20170801_models.DeleteRoleResponse:
        """
        @summary Deletes a Resource Access Management (RAM) role.
        
        @param request: DeleteRoleRequest
        @return: DeleteRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_role_with_options(request, headers, runtime)

    async def delete_role_async(
        self,
        request: edas_20170801_models.DeleteRoleRequest,
    ) -> edas_20170801_models.DeleteRoleResponse:
        """
        @summary Deletes a Resource Access Management (RAM) role.
        
        @param request: DeleteRoleRequest
        @return: DeleteRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_role_with_options_async(request, headers, runtime)

    def delete_service_group_with_options(
        self,
        request: edas_20170801_models.DeleteServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteServiceGroupResponse:
        """
        @summary Deletes a service group.
        
        @param request: DeleteServiceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/service/serviceGroups',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_group_with_options_async(
        self,
        request: edas_20170801_models.DeleteServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteServiceGroupResponse:
        """
        @summary Deletes a service group.
        
        @param request: DeleteServiceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/service/serviceGroups',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_group(
        self,
        request: edas_20170801_models.DeleteServiceGroupRequest,
    ) -> edas_20170801_models.DeleteServiceGroupResponse:
        """
        @summary Deletes a service group.
        
        @param request: DeleteServiceGroupRequest
        @return: DeleteServiceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_group_with_options(request, headers, runtime)

    async def delete_service_group_async(
        self,
        request: edas_20170801_models.DeleteServiceGroupRequest,
    ) -> edas_20170801_models.DeleteServiceGroupResponse:
        """
        @summary Deletes a service group.
        
        @param request: DeleteServiceGroupRequest
        @return: DeleteServiceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_group_with_options_async(request, headers, runtime)

    def delete_swimming_lane_with_options(
        self,
        request: edas_20170801_models.DeleteSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteSwimmingLaneResponse:
        """
        @summary Deletes a lane.
        
        @param request: DeleteSwimmingLaneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSwimmingLaneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lane_id):
            query['LaneId'] = request.lane_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSwimmingLane',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/trafficmgnt/swimming_lanes',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteSwimmingLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_swimming_lane_with_options_async(
        self,
        request: edas_20170801_models.DeleteSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteSwimmingLaneResponse:
        """
        @summary Deletes a lane.
        
        @param request: DeleteSwimmingLaneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSwimmingLaneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lane_id):
            query['LaneId'] = request.lane_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSwimmingLane',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/trafficmgnt/swimming_lanes',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteSwimmingLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_swimming_lane(
        self,
        request: edas_20170801_models.DeleteSwimmingLaneRequest,
    ) -> edas_20170801_models.DeleteSwimmingLaneResponse:
        """
        @summary Deletes a lane.
        
        @param request: DeleteSwimmingLaneRequest
        @return: DeleteSwimmingLaneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_swimming_lane_with_options(request, headers, runtime)

    async def delete_swimming_lane_async(
        self,
        request: edas_20170801_models.DeleteSwimmingLaneRequest,
    ) -> edas_20170801_models.DeleteSwimmingLaneResponse:
        """
        @summary Deletes a lane.
        
        @param request: DeleteSwimmingLaneRequest
        @return: DeleteSwimmingLaneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_swimming_lane_with_options_async(request, headers, runtime)

    def delete_user_define_region_with_options(
        self,
        request: edas_20170801_models.DeleteUserDefineRegionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteUserDefineRegionResponse:
        """
        @summary Deletes a specified custom namespace.
        
        @param request: DeleteUserDefineRegionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserDefineRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_tag):
            query['RegionTag'] = request.region_tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserDefineRegion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/user_region_def',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteUserDefineRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_define_region_with_options_async(
        self,
        request: edas_20170801_models.DeleteUserDefineRegionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeleteUserDefineRegionResponse:
        """
        @summary Deletes a specified custom namespace.
        
        @param request: DeleteUserDefineRegionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserDefineRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_tag):
            query['RegionTag'] = request.region_tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserDefineRegion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/user_region_def',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeleteUserDefineRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_define_region(
        self,
        request: edas_20170801_models.DeleteUserDefineRegionRequest,
    ) -> edas_20170801_models.DeleteUserDefineRegionResponse:
        """
        @summary Deletes a specified custom namespace.
        
        @param request: DeleteUserDefineRegionRequest
        @return: DeleteUserDefineRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_user_define_region_with_options(request, headers, runtime)

    async def delete_user_define_region_async(
        self,
        request: edas_20170801_models.DeleteUserDefineRegionRequest,
    ) -> edas_20170801_models.DeleteUserDefineRegionResponse:
        """
        @summary Deletes a specified custom namespace.
        
        @param request: DeleteUserDefineRegionRequest
        @return: DeleteUserDefineRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_user_define_region_with_options_async(request, headers, runtime)

    def deploy_application_with_options(
        self,
        request: edas_20170801_models.DeployApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeployApplicationResponse:
        """
        @summary Deploys an application in an Elastic Compute Service (ECS) cluster.
        
        @description > To deploy an application in a Container Service for Kubernetes (ACK) cluster that is imported into Enterprise Distributed Application Service (EDAS), call the DeployK8sApplication operation provided by EDAS. For more information, see [](~~149420~~)DeployK8sApplication.
        
        @param request: DeployApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_env):
            query['AppEnv'] = request.app_env
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.batch):
            query['Batch'] = request.batch
        if not UtilClient.is_unset(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not UtilClient.is_unset(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        if not UtilClient.is_unset(request.component_ids):
            query['ComponentIds'] = request.component_ids
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.gray):
            query['Gray'] = request.gray
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.release_type):
            query['ReleaseType'] = request.release_type
        if not UtilClient.is_unset(request.traffic_control_strategy):
            query['TrafficControlStrategy'] = request.traffic_control_strategy
        if not UtilClient.is_unset(request.war_url):
            query['WarUrl'] = request.war_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_deploy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeployApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_application_with_options_async(
        self,
        request: edas_20170801_models.DeployApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeployApplicationResponse:
        """
        @summary Deploys an application in an Elastic Compute Service (ECS) cluster.
        
        @description > To deploy an application in a Container Service for Kubernetes (ACK) cluster that is imported into Enterprise Distributed Application Service (EDAS), call the DeployK8sApplication operation provided by EDAS. For more information, see [](~~149420~~)DeployK8sApplication.
        
        @param request: DeployApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_env):
            query['AppEnv'] = request.app_env
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.batch):
            query['Batch'] = request.batch
        if not UtilClient.is_unset(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not UtilClient.is_unset(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        if not UtilClient.is_unset(request.component_ids):
            query['ComponentIds'] = request.component_ids
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.gray):
            query['Gray'] = request.gray
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.release_type):
            query['ReleaseType'] = request.release_type
        if not UtilClient.is_unset(request.traffic_control_strategy):
            query['TrafficControlStrategy'] = request.traffic_control_strategy
        if not UtilClient.is_unset(request.war_url):
            query['WarUrl'] = request.war_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_deploy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeployApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_application(
        self,
        request: edas_20170801_models.DeployApplicationRequest,
    ) -> edas_20170801_models.DeployApplicationResponse:
        """
        @summary Deploys an application in an Elastic Compute Service (ECS) cluster.
        
        @description > To deploy an application in a Container Service for Kubernetes (ACK) cluster that is imported into Enterprise Distributed Application Service (EDAS), call the DeployK8sApplication operation provided by EDAS. For more information, see [](~~149420~~)DeployK8sApplication.
        
        @param request: DeployApplicationRequest
        @return: DeployApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deploy_application_with_options(request, headers, runtime)

    async def deploy_application_async(
        self,
        request: edas_20170801_models.DeployApplicationRequest,
    ) -> edas_20170801_models.DeployApplicationResponse:
        """
        @summary Deploys an application in an Elastic Compute Service (ECS) cluster.
        
        @description > To deploy an application in a Container Service for Kubernetes (ACK) cluster that is imported into Enterprise Distributed Application Service (EDAS), call the DeployK8sApplication operation provided by EDAS. For more information, see [](~~149420~~)DeployK8sApplication.
        
        @param request: DeployApplicationRequest
        @return: DeployApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.deploy_application_with_options_async(request, headers, runtime)

    def deploy_k8s_application_with_options(
        self,
        request: edas_20170801_models.DeployK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeployK8sApplicationResponse:
        """
        @summary Deploys an application in a Container Service for Kubernetes (ACK) cluster or a serverless Kubernetes cluster.
        
        @param request: DeployK8sApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployK8sApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.args):
            query['Args'] = request.args
        if not UtilClient.is_unset(request.batch_timeout):
            query['BatchTimeout'] = request.batch_timeout
        if not UtilClient.is_unset(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not UtilClient.is_unset(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        if not UtilClient.is_unset(request.canary_rule_id):
            query['CanaryRuleId'] = request.canary_rule_id
        if not UtilClient.is_unset(request.change_order_desc):
            query['ChangeOrderDesc'] = request.change_order_desc
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.config_mount_descs):
            query['ConfigMountDescs'] = request.config_mount_descs
        if not UtilClient.is_unset(request.cpu_limit):
            query['CpuLimit'] = request.cpu_limit
        if not UtilClient.is_unset(request.cpu_request):
            query['CpuRequest'] = request.cpu_request
        if not UtilClient.is_unset(request.custom_affinity):
            query['CustomAffinity'] = request.custom_affinity
        if not UtilClient.is_unset(request.custom_agent_version):
            query['CustomAgentVersion'] = request.custom_agent_version
        if not UtilClient.is_unset(request.custom_tolerations):
            query['CustomTolerations'] = request.custom_tolerations
        if not UtilClient.is_unset(request.deploy_across_nodes):
            query['DeployAcrossNodes'] = request.deploy_across_nodes
        if not UtilClient.is_unset(request.deploy_across_zones):
            query['DeployAcrossZones'] = request.deploy_across_zones
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.empty_dirs):
            query['EmptyDirs'] = request.empty_dirs
        if not UtilClient.is_unset(request.enable_ahas):
            query['EnableAhas'] = request.enable_ahas
        if not UtilClient.is_unset(request.enable_empty_push_reject):
            query['EnableEmptyPushReject'] = request.enable_empty_push_reject
        if not UtilClient.is_unset(request.enable_lossless_rule):
            query['EnableLosslessRule'] = request.enable_lossless_rule
        if not UtilClient.is_unset(request.env_froms):
            query['EnvFroms'] = request.env_froms
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.image_platforms):
            query['ImagePlatforms'] = request.image_platforms
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not UtilClient.is_unset(request.jdk):
            query['JDK'] = request.jdk
        if not UtilClient.is_unset(request.java_start_up_config):
            query['JavaStartUpConfig'] = request.java_start_up_config
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.limit_ephemeral_storage):
            query['LimitEphemeralStorage'] = request.limit_ephemeral_storage
        if not UtilClient.is_unset(request.liveness):
            query['Liveness'] = request.liveness
        if not UtilClient.is_unset(request.local_volume):
            query['LocalVolume'] = request.local_volume
        if not UtilClient.is_unset(request.lossless_rule_aligned):
            query['LosslessRuleAligned'] = request.lossless_rule_aligned
        if not UtilClient.is_unset(request.lossless_rule_delay_time):
            query['LosslessRuleDelayTime'] = request.lossless_rule_delay_time
        if not UtilClient.is_unset(request.lossless_rule_func_type):
            query['LosslessRuleFuncType'] = request.lossless_rule_func_type
        if not UtilClient.is_unset(request.lossless_rule_related):
            query['LosslessRuleRelated'] = request.lossless_rule_related
        if not UtilClient.is_unset(request.lossless_rule_warmup_time):
            query['LosslessRuleWarmupTime'] = request.lossless_rule_warmup_time
        if not UtilClient.is_unset(request.mcpu_limit):
            query['McpuLimit'] = request.mcpu_limit
        if not UtilClient.is_unset(request.mcpu_request):
            query['McpuRequest'] = request.mcpu_request
        if not UtilClient.is_unset(request.memory_limit):
            query['MemoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.memory_request):
            query['MemoryRequest'] = request.memory_request
        if not UtilClient.is_unset(request.mount_descs):
            query['MountDescs'] = request.mount_descs
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.package_version_id):
            query['PackageVersionId'] = request.package_version_id
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.pvc_mount_descs):
            query['PvcMountDescs'] = request.pvc_mount_descs
        if not UtilClient.is_unset(request.readiness):
            query['Readiness'] = request.readiness
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.requests_ephemeral_storage):
            query['RequestsEphemeralStorage'] = request.requests_ephemeral_storage
        if not UtilClient.is_unset(request.runtime_class_name):
            query['RuntimeClassName'] = request.runtime_class_name
        if not UtilClient.is_unset(request.security_context):
            query['SecurityContext'] = request.security_context
        if not UtilClient.is_unset(request.sidecars):
            query['Sidecars'] = request.sidecars
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.startup):
            query['Startup'] = request.startup
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.terminate_grace_period):
            query['TerminateGracePeriod'] = request.terminate_grace_period
        if not UtilClient.is_unset(request.traffic_control_strategy):
            query['TrafficControlStrategy'] = request.traffic_control_strategy
        if not UtilClient.is_unset(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not UtilClient.is_unset(request.uri_encoding):
            query['UriEncoding'] = request.uri_encoding
        if not UtilClient.is_unset(request.use_body_encoding):
            query['UseBodyEncoding'] = request.use_body_encoding
        if not UtilClient.is_unset(request.user_base_image_url):
            query['UserBaseImageUrl'] = request.user_base_image_url
        if not UtilClient.is_unset(request.volumes_str):
            query['VolumesStr'] = request.volumes_str
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        if not UtilClient.is_unset(request.web_container_config):
            query['WebContainerConfig'] = request.web_container_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployK8sApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_apps',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeployK8sApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_k8s_application_with_options_async(
        self,
        request: edas_20170801_models.DeployK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DeployK8sApplicationResponse:
        """
        @summary Deploys an application in a Container Service for Kubernetes (ACK) cluster or a serverless Kubernetes cluster.
        
        @param request: DeployK8sApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployK8sApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.args):
            query['Args'] = request.args
        if not UtilClient.is_unset(request.batch_timeout):
            query['BatchTimeout'] = request.batch_timeout
        if not UtilClient.is_unset(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not UtilClient.is_unset(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        if not UtilClient.is_unset(request.canary_rule_id):
            query['CanaryRuleId'] = request.canary_rule_id
        if not UtilClient.is_unset(request.change_order_desc):
            query['ChangeOrderDesc'] = request.change_order_desc
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.config_mount_descs):
            query['ConfigMountDescs'] = request.config_mount_descs
        if not UtilClient.is_unset(request.cpu_limit):
            query['CpuLimit'] = request.cpu_limit
        if not UtilClient.is_unset(request.cpu_request):
            query['CpuRequest'] = request.cpu_request
        if not UtilClient.is_unset(request.custom_affinity):
            query['CustomAffinity'] = request.custom_affinity
        if not UtilClient.is_unset(request.custom_agent_version):
            query['CustomAgentVersion'] = request.custom_agent_version
        if not UtilClient.is_unset(request.custom_tolerations):
            query['CustomTolerations'] = request.custom_tolerations
        if not UtilClient.is_unset(request.deploy_across_nodes):
            query['DeployAcrossNodes'] = request.deploy_across_nodes
        if not UtilClient.is_unset(request.deploy_across_zones):
            query['DeployAcrossZones'] = request.deploy_across_zones
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.empty_dirs):
            query['EmptyDirs'] = request.empty_dirs
        if not UtilClient.is_unset(request.enable_ahas):
            query['EnableAhas'] = request.enable_ahas
        if not UtilClient.is_unset(request.enable_empty_push_reject):
            query['EnableEmptyPushReject'] = request.enable_empty_push_reject
        if not UtilClient.is_unset(request.enable_lossless_rule):
            query['EnableLosslessRule'] = request.enable_lossless_rule
        if not UtilClient.is_unset(request.env_froms):
            query['EnvFroms'] = request.env_froms
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.image_platforms):
            query['ImagePlatforms'] = request.image_platforms
        if not UtilClient.is_unset(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not UtilClient.is_unset(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not UtilClient.is_unset(request.jdk):
            query['JDK'] = request.jdk
        if not UtilClient.is_unset(request.java_start_up_config):
            query['JavaStartUpConfig'] = request.java_start_up_config
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.limit_ephemeral_storage):
            query['LimitEphemeralStorage'] = request.limit_ephemeral_storage
        if not UtilClient.is_unset(request.liveness):
            query['Liveness'] = request.liveness
        if not UtilClient.is_unset(request.local_volume):
            query['LocalVolume'] = request.local_volume
        if not UtilClient.is_unset(request.lossless_rule_aligned):
            query['LosslessRuleAligned'] = request.lossless_rule_aligned
        if not UtilClient.is_unset(request.lossless_rule_delay_time):
            query['LosslessRuleDelayTime'] = request.lossless_rule_delay_time
        if not UtilClient.is_unset(request.lossless_rule_func_type):
            query['LosslessRuleFuncType'] = request.lossless_rule_func_type
        if not UtilClient.is_unset(request.lossless_rule_related):
            query['LosslessRuleRelated'] = request.lossless_rule_related
        if not UtilClient.is_unset(request.lossless_rule_warmup_time):
            query['LosslessRuleWarmupTime'] = request.lossless_rule_warmup_time
        if not UtilClient.is_unset(request.mcpu_limit):
            query['McpuLimit'] = request.mcpu_limit
        if not UtilClient.is_unset(request.mcpu_request):
            query['McpuRequest'] = request.mcpu_request
        if not UtilClient.is_unset(request.memory_limit):
            query['MemoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.memory_request):
            query['MemoryRequest'] = request.memory_request
        if not UtilClient.is_unset(request.mount_descs):
            query['MountDescs'] = request.mount_descs
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.package_version_id):
            query['PackageVersionId'] = request.package_version_id
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.pvc_mount_descs):
            query['PvcMountDescs'] = request.pvc_mount_descs
        if not UtilClient.is_unset(request.readiness):
            query['Readiness'] = request.readiness
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.requests_ephemeral_storage):
            query['RequestsEphemeralStorage'] = request.requests_ephemeral_storage
        if not UtilClient.is_unset(request.runtime_class_name):
            query['RuntimeClassName'] = request.runtime_class_name
        if not UtilClient.is_unset(request.security_context):
            query['SecurityContext'] = request.security_context
        if not UtilClient.is_unset(request.sidecars):
            query['Sidecars'] = request.sidecars
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.startup):
            query['Startup'] = request.startup
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.terminate_grace_period):
            query['TerminateGracePeriod'] = request.terminate_grace_period
        if not UtilClient.is_unset(request.traffic_control_strategy):
            query['TrafficControlStrategy'] = request.traffic_control_strategy
        if not UtilClient.is_unset(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not UtilClient.is_unset(request.uri_encoding):
            query['UriEncoding'] = request.uri_encoding
        if not UtilClient.is_unset(request.use_body_encoding):
            query['UseBodyEncoding'] = request.use_body_encoding
        if not UtilClient.is_unset(request.user_base_image_url):
            query['UserBaseImageUrl'] = request.user_base_image_url
        if not UtilClient.is_unset(request.volumes_str):
            query['VolumesStr'] = request.volumes_str
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        if not UtilClient.is_unset(request.web_container_config):
            query['WebContainerConfig'] = request.web_container_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployK8sApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_apps',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DeployK8sApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_k8s_application(
        self,
        request: edas_20170801_models.DeployK8sApplicationRequest,
    ) -> edas_20170801_models.DeployK8sApplicationResponse:
        """
        @summary Deploys an application in a Container Service for Kubernetes (ACK) cluster or a serverless Kubernetes cluster.
        
        @param request: DeployK8sApplicationRequest
        @return: DeployK8sApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deploy_k8s_application_with_options(request, headers, runtime)

    async def deploy_k8s_application_async(
        self,
        request: edas_20170801_models.DeployK8sApplicationRequest,
    ) -> edas_20170801_models.DeployK8sApplicationResponse:
        """
        @summary Deploys an application in a Container Service for Kubernetes (ACK) cluster or a serverless Kubernetes cluster.
        
        @param request: DeployK8sApplicationRequest
        @return: DeployK8sApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.deploy_k8s_application_with_options_async(request, headers, runtime)

    def describe_app_instance_list_with_options(
        self,
        request: edas_20170801_models.DescribeAppInstanceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DescribeAppInstanceListResponse:
        """
        @summary Queries Kubernetes application instances.
        
        @param request: DescribeAppInstanceListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppInstanceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.with_node_info):
            query['WithNodeInfo'] = request.with_node_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppInstanceList',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/oam/app_instance_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DescribeAppInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_instance_list_with_options_async(
        self,
        request: edas_20170801_models.DescribeAppInstanceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DescribeAppInstanceListResponse:
        """
        @summary Queries Kubernetes application instances.
        
        @param request: DescribeAppInstanceListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppInstanceListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.with_node_info):
            query['WithNodeInfo'] = request.with_node_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppInstanceList',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/oam/app_instance_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DescribeAppInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_instance_list(
        self,
        request: edas_20170801_models.DescribeAppInstanceListRequest,
    ) -> edas_20170801_models.DescribeAppInstanceListResponse:
        """
        @summary Queries Kubernetes application instances.
        
        @param request: DescribeAppInstanceListRequest
        @return: DescribeAppInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_app_instance_list_with_options(request, headers, runtime)

    async def describe_app_instance_list_async(
        self,
        request: edas_20170801_models.DescribeAppInstanceListRequest,
    ) -> edas_20170801_models.DescribeAppInstanceListResponse:
        """
        @summary Queries Kubernetes application instances.
        
        @param request: DescribeAppInstanceListRequest
        @return: DescribeAppInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_app_instance_list_with_options_async(request, headers, runtime)

    def describe_application_scaling_rules_with_options(
        self,
        request: edas_20170801_models.DescribeApplicationScalingRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DescribeApplicationScalingRulesResponse:
        """
        @summary Queries the auto scaling policies of an application.
        
        @param request: DescribeApplicationScalingRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationScalingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationScalingRules',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v1/eam/scale/application_scaling_rules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DescribeApplicationScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_scaling_rules_with_options_async(
        self,
        request: edas_20170801_models.DescribeApplicationScalingRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DescribeApplicationScalingRulesResponse:
        """
        @summary Queries the auto scaling policies of an application.
        
        @param request: DescribeApplicationScalingRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeApplicationScalingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApplicationScalingRules',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v1/eam/scale/application_scaling_rules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DescribeApplicationScalingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_scaling_rules(
        self,
        request: edas_20170801_models.DescribeApplicationScalingRulesRequest,
    ) -> edas_20170801_models.DescribeApplicationScalingRulesResponse:
        """
        @summary Queries the auto scaling policies of an application.
        
        @param request: DescribeApplicationScalingRulesRequest
        @return: DescribeApplicationScalingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_application_scaling_rules_with_options(request, headers, runtime)

    async def describe_application_scaling_rules_async(
        self,
        request: edas_20170801_models.DescribeApplicationScalingRulesRequest,
    ) -> edas_20170801_models.DescribeApplicationScalingRulesResponse:
        """
        @summary Queries the auto scaling policies of an application.
        
        @param request: DescribeApplicationScalingRulesRequest
        @return: DescribeApplicationScalingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_application_scaling_rules_with_options_async(request, headers, runtime)

    def describe_locality_setting_with_options(
        self,
        request: edas_20170801_models.DescribeLocalitySettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DescribeLocalitySettingResponse:
        """
        @param request: DescribeLocalitySettingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLocalitySettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLocalitySetting',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/sp/applications/locality/setting',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DescribeLocalitySettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_locality_setting_with_options_async(
        self,
        request: edas_20170801_models.DescribeLocalitySettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DescribeLocalitySettingResponse:
        """
        @param request: DescribeLocalitySettingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLocalitySettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLocalitySetting',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/sp/applications/locality/setting',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DescribeLocalitySettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_locality_setting(
        self,
        request: edas_20170801_models.DescribeLocalitySettingRequest,
    ) -> edas_20170801_models.DescribeLocalitySettingResponse:
        """
        @param request: DescribeLocalitySettingRequest
        @return: DescribeLocalitySettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_locality_setting_with_options(request, headers, runtime)

    async def describe_locality_setting_async(
        self,
        request: edas_20170801_models.DescribeLocalitySettingRequest,
    ) -> edas_20170801_models.DescribeLocalitySettingResponse:
        """
        @param request: DescribeLocalitySettingRequest
        @return: DescribeLocalitySettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_locality_setting_with_options_async(request, headers, runtime)

    def disable_application_scaling_rule_with_options(
        self,
        request: edas_20170801_models.DisableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DisableApplicationScalingRuleResponse:
        """
        @summary Disables an auto scaling policy for an application.
        
        @param request: DisableApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationScalingRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v1/eam/scale/disable_application_scaling_rule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DisableApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_scaling_rule_with_options_async(
        self,
        request: edas_20170801_models.DisableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.DisableApplicationScalingRuleResponse:
        """
        @summary Disables an auto scaling policy for an application.
        
        @param request: DisableApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationScalingRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v1/eam/scale/disable_application_scaling_rule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.DisableApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_scaling_rule(
        self,
        request: edas_20170801_models.DisableApplicationScalingRuleRequest,
    ) -> edas_20170801_models.DisableApplicationScalingRuleResponse:
        """
        @summary Disables an auto scaling policy for an application.
        
        @param request: DisableApplicationScalingRuleRequest
        @return: DisableApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_application_scaling_rule_with_options(request, headers, runtime)

    async def disable_application_scaling_rule_async(
        self,
        request: edas_20170801_models.DisableApplicationScalingRuleRequest,
    ) -> edas_20170801_models.DisableApplicationScalingRuleResponse:
        """
        @summary Disables an auto scaling policy for an application.
        
        @param request: DisableApplicationScalingRuleRequest
        @return: DisableApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.disable_application_scaling_rule_with_options_async(request, headers, runtime)

    def enable_application_scaling_rule_with_options(
        self,
        request: edas_20170801_models.EnableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.EnableApplicationScalingRuleResponse:
        """
        @summary Enables an auto scaling policy for an application.
        
        @param request: EnableApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationScalingRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v1/eam/scale/enable_application_scaling_rule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.EnableApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_scaling_rule_with_options_async(
        self,
        request: edas_20170801_models.EnableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.EnableApplicationScalingRuleResponse:
        """
        @summary Enables an auto scaling policy for an application.
        
        @param request: EnableApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationScalingRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v1/eam/scale/enable_application_scaling_rule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.EnableApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_scaling_rule(
        self,
        request: edas_20170801_models.EnableApplicationScalingRuleRequest,
    ) -> edas_20170801_models.EnableApplicationScalingRuleResponse:
        """
        @summary Enables an auto scaling policy for an application.
        
        @param request: EnableApplicationScalingRuleRequest
        @return: EnableApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_application_scaling_rule_with_options(request, headers, runtime)

    async def enable_application_scaling_rule_async(
        self,
        request: edas_20170801_models.EnableApplicationScalingRuleRequest,
    ) -> edas_20170801_models.EnableApplicationScalingRuleResponse:
        """
        @summary Enables an auto scaling policy for an application.
        
        @param request: EnableApplicationScalingRuleRequest
        @return: EnableApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.enable_application_scaling_rule_with_options_async(request, headers, runtime)

    def get_app_deployment_with_options(
        self,
        request: edas_20170801_models.GetAppDeploymentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetAppDeploymentResponse:
        """
        @summary Queries the information about the Deployment of a Kubernetes application.
        
        @param request: GetAppDeploymentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppDeploymentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppDeployment',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/oam/app_deployment',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetAppDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_deployment_with_options_async(
        self,
        request: edas_20170801_models.GetAppDeploymentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetAppDeploymentResponse:
        """
        @summary Queries the information about the Deployment of a Kubernetes application.
        
        @param request: GetAppDeploymentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppDeploymentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppDeployment',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/oam/app_deployment',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetAppDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_deployment(
        self,
        request: edas_20170801_models.GetAppDeploymentRequest,
    ) -> edas_20170801_models.GetAppDeploymentResponse:
        """
        @summary Queries the information about the Deployment of a Kubernetes application.
        
        @param request: GetAppDeploymentRequest
        @return: GetAppDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_app_deployment_with_options(request, headers, runtime)

    async def get_app_deployment_async(
        self,
        request: edas_20170801_models.GetAppDeploymentRequest,
    ) -> edas_20170801_models.GetAppDeploymentResponse:
        """
        @summary Queries the information about the Deployment of a Kubernetes application.
        
        @param request: GetAppDeploymentRequest
        @return: GetAppDeploymentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_app_deployment_with_options_async(request, headers, runtime)

    def get_application_with_options(
        self,
        request: edas_20170801_models.GetApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetApplicationResponse:
        """
        @summary Queries the details about a specified application in an Elastic Compute Service (ECS) cluster.
        
        @param request: GetApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/app_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_with_options_async(
        self,
        request: edas_20170801_models.GetApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetApplicationResponse:
        """
        @summary Queries the details about a specified application in an Elastic Compute Service (ECS) cluster.
        
        @param request: GetApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/app_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application(
        self,
        request: edas_20170801_models.GetApplicationRequest,
    ) -> edas_20170801_models.GetApplicationResponse:
        """
        @summary Queries the details about a specified application in an Elastic Compute Service (ECS) cluster.
        
        @param request: GetApplicationRequest
        @return: GetApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_application_with_options(request, headers, runtime)

    async def get_application_async(
        self,
        request: edas_20170801_models.GetApplicationRequest,
    ) -> edas_20170801_models.GetApplicationResponse:
        """
        @summary Queries the details about a specified application in an Elastic Compute Service (ECS) cluster.
        
        @param request: GetApplicationRequest
        @return: GetApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_application_with_options_async(request, headers, runtime)

    def get_change_order_info_with_options(
        self,
        request: edas_20170801_models.GetChangeOrderInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetChangeOrderInfoResponse:
        """
        @summary Queries the details about a change process.
        
        @param request: GetChangeOrderInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChangeOrderInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChangeOrderInfo',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/change_order_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetChangeOrderInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_change_order_info_with_options_async(
        self,
        request: edas_20170801_models.GetChangeOrderInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetChangeOrderInfoResponse:
        """
        @summary Queries the details about a change process.
        
        @param request: GetChangeOrderInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChangeOrderInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChangeOrderInfo',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/change_order_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetChangeOrderInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_change_order_info(
        self,
        request: edas_20170801_models.GetChangeOrderInfoRequest,
    ) -> edas_20170801_models.GetChangeOrderInfoResponse:
        """
        @summary Queries the details about a change process.
        
        @param request: GetChangeOrderInfoRequest
        @return: GetChangeOrderInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_change_order_info_with_options(request, headers, runtime)

    async def get_change_order_info_async(
        self,
        request: edas_20170801_models.GetChangeOrderInfoRequest,
    ) -> edas_20170801_models.GetChangeOrderInfoResponse:
        """
        @summary Queries the details about a change process.
        
        @param request: GetChangeOrderInfoRequest
        @return: GetChangeOrderInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_change_order_info_with_options_async(request, headers, runtime)

    def get_cluster_with_options(
        self,
        request: edas_20170801_models.GetClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetClusterResponse:
        """
        @summary Queries a specific cluster.
        
        @param request: GetClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/cluster',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_with_options_async(
        self,
        request: edas_20170801_models.GetClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetClusterResponse:
        """
        @summary Queries a specific cluster.
        
        @param request: GetClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/cluster',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster(
        self,
        request: edas_20170801_models.GetClusterRequest,
    ) -> edas_20170801_models.GetClusterResponse:
        """
        @summary Queries a specific cluster.
        
        @param request: GetClusterRequest
        @return: GetClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_with_options(request, headers, runtime)

    async def get_cluster_async(
        self,
        request: edas_20170801_models.GetClusterRequest,
    ) -> edas_20170801_models.GetClusterResponse:
        """
        @summary Queries a specific cluster.
        
        @param request: GetClusterRequest
        @return: GetClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cluster_with_options_async(request, headers, runtime)

    def get_container_configuration_with_options(
        self,
        request: edas_20170801_models.GetContainerConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetContainerConfigurationResponse:
        """
        @summary Queries the Tomcat configuration of an application or an instance group in which an application is deployed.
        
        @param request: GetContainerConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetContainerConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetContainerConfiguration',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/container_config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetContainerConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_container_configuration_with_options_async(
        self,
        request: edas_20170801_models.GetContainerConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetContainerConfigurationResponse:
        """
        @summary Queries the Tomcat configuration of an application or an instance group in which an application is deployed.
        
        @param request: GetContainerConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetContainerConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetContainerConfiguration',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/container_config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetContainerConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_container_configuration(
        self,
        request: edas_20170801_models.GetContainerConfigurationRequest,
    ) -> edas_20170801_models.GetContainerConfigurationResponse:
        """
        @summary Queries the Tomcat configuration of an application or an instance group in which an application is deployed.
        
        @param request: GetContainerConfigurationRequest
        @return: GetContainerConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_container_configuration_with_options(request, headers, runtime)

    async def get_container_configuration_async(
        self,
        request: edas_20170801_models.GetContainerConfigurationRequest,
    ) -> edas_20170801_models.GetContainerConfigurationResponse:
        """
        @summary Queries the Tomcat configuration of an application or an instance group in which an application is deployed.
        
        @param request: GetContainerConfigurationRequest
        @return: GetContainerConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_container_configuration_with_options_async(request, headers, runtime)

    def get_java_start_up_config_with_options(
        self,
        request: edas_20170801_models.GetJavaStartUpConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetJavaStartUpConfigResponse:
        """
        @summary Queries the configuration of Java startup parameters for an application.
        
        @param request: GetJavaStartUpConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJavaStartUpConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJavaStartUpConfig',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/oam/java_start_up_config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetJavaStartUpConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_java_start_up_config_with_options_async(
        self,
        request: edas_20170801_models.GetJavaStartUpConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetJavaStartUpConfigResponse:
        """
        @summary Queries the configuration of Java startup parameters for an application.
        
        @param request: GetJavaStartUpConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJavaStartUpConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJavaStartUpConfig',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/oam/java_start_up_config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetJavaStartUpConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_java_start_up_config(
        self,
        request: edas_20170801_models.GetJavaStartUpConfigRequest,
    ) -> edas_20170801_models.GetJavaStartUpConfigResponse:
        """
        @summary Queries the configuration of Java startup parameters for an application.
        
        @param request: GetJavaStartUpConfigRequest
        @return: GetJavaStartUpConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_java_start_up_config_with_options(request, headers, runtime)

    async def get_java_start_up_config_async(
        self,
        request: edas_20170801_models.GetJavaStartUpConfigRequest,
    ) -> edas_20170801_models.GetJavaStartUpConfigResponse:
        """
        @summary Queries the configuration of Java startup parameters for an application.
        
        @param request: GetJavaStartUpConfigRequest
        @return: GetJavaStartUpConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_java_start_up_config_with_options_async(request, headers, runtime)

    def get_jvm_configuration_with_options(
        self,
        request: edas_20170801_models.GetJvmConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetJvmConfigurationResponse:
        """
        @summary Queries the Java Virtual Machine (JVM) configuration of an application or an instance group in which an application is deployed.
        
        @param request: GetJvmConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJvmConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJvmConfiguration',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/app_jvm_config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetJvmConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_jvm_configuration_with_options_async(
        self,
        request: edas_20170801_models.GetJvmConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetJvmConfigurationResponse:
        """
        @summary Queries the Java Virtual Machine (JVM) configuration of an application or an instance group in which an application is deployed.
        
        @param request: GetJvmConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJvmConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJvmConfiguration',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/app_jvm_config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetJvmConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_jvm_configuration(
        self,
        request: edas_20170801_models.GetJvmConfigurationRequest,
    ) -> edas_20170801_models.GetJvmConfigurationResponse:
        """
        @summary Queries the Java Virtual Machine (JVM) configuration of an application or an instance group in which an application is deployed.
        
        @param request: GetJvmConfigurationRequest
        @return: GetJvmConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_jvm_configuration_with_options(request, headers, runtime)

    async def get_jvm_configuration_async(
        self,
        request: edas_20170801_models.GetJvmConfigurationRequest,
    ) -> edas_20170801_models.GetJvmConfigurationResponse:
        """
        @summary Queries the Java Virtual Machine (JVM) configuration of an application or an instance group in which an application is deployed.
        
        @param request: GetJvmConfigurationRequest
        @return: GetJvmConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_jvm_configuration_with_options_async(request, headers, runtime)

    def get_k8s_app_precheck_result_with_options(
        self,
        request: edas_20170801_models.GetK8sAppPrecheckResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetK8sAppPrecheckResultResponse:
        """
        @summary Queries the precheck result of a Kubernetes application.
        
        @param request: GetK8sAppPrecheckResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetK8sAppPrecheckResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetK8sAppPrecheckResult',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/app_precheck',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetK8sAppPrecheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_k8s_app_precheck_result_with_options_async(
        self,
        request: edas_20170801_models.GetK8sAppPrecheckResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetK8sAppPrecheckResultResponse:
        """
        @summary Queries the precheck result of a Kubernetes application.
        
        @param request: GetK8sAppPrecheckResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetK8sAppPrecheckResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetK8sAppPrecheckResult',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/app_precheck',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetK8sAppPrecheckResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_k8s_app_precheck_result(
        self,
        request: edas_20170801_models.GetK8sAppPrecheckResultRequest,
    ) -> edas_20170801_models.GetK8sAppPrecheckResultResponse:
        """
        @summary Queries the precheck result of a Kubernetes application.
        
        @param request: GetK8sAppPrecheckResultRequest
        @return: GetK8sAppPrecheckResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_k8s_app_precheck_result_with_options(request, headers, runtime)

    async def get_k8s_app_precheck_result_async(
        self,
        request: edas_20170801_models.GetK8sAppPrecheckResultRequest,
    ) -> edas_20170801_models.GetK8sAppPrecheckResultResponse:
        """
        @summary Queries the precheck result of a Kubernetes application.
        
        @param request: GetK8sAppPrecheckResultRequest
        @return: GetK8sAppPrecheckResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_k8s_app_precheck_result_with_options_async(request, headers, runtime)

    def get_k8s_application_with_options(
        self,
        request: edas_20170801_models.GetK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetK8sApplicationResponse:
        """
        @summary Queries the information about applications deployed in a Container Service for Kubernetes (ACK) cluster or a serverless Kubernetes cluster.
        
        @param request: GetK8sApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetK8sApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetK8sApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_application',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetK8sApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_k8s_application_with_options_async(
        self,
        request: edas_20170801_models.GetK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetK8sApplicationResponse:
        """
        @summary Queries the information about applications deployed in a Container Service for Kubernetes (ACK) cluster or a serverless Kubernetes cluster.
        
        @param request: GetK8sApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetK8sApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetK8sApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_application',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetK8sApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_k8s_application(
        self,
        request: edas_20170801_models.GetK8sApplicationRequest,
    ) -> edas_20170801_models.GetK8sApplicationResponse:
        """
        @summary Queries the information about applications deployed in a Container Service for Kubernetes (ACK) cluster or a serverless Kubernetes cluster.
        
        @param request: GetK8sApplicationRequest
        @return: GetK8sApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_k8s_application_with_options(request, headers, runtime)

    async def get_k8s_application_async(
        self,
        request: edas_20170801_models.GetK8sApplicationRequest,
    ) -> edas_20170801_models.GetK8sApplicationResponse:
        """
        @summary Queries the information about applications deployed in a Container Service for Kubernetes (ACK) cluster or a serverless Kubernetes cluster.
        
        @param request: GetK8sApplicationRequest
        @return: GetK8sApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_k8s_application_with_options_async(request, headers, runtime)

    def get_k8s_cluster_with_options(
        self,
        request: edas_20170801_models.GetK8sClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetK8sClusterResponse:
        """
        @summary Queries Container Service for Kubernetes (ACK) clusters or Serverless Kubernetes clusters in a specified region.
        
        @param request: GetK8sClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetK8sClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_tag):
            query['RegionTag'] = request.region_tag
        if not UtilClient.is_unset(request.sub_cluster_type):
            query['SubClusterType'] = request.sub_cluster_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetK8sCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s_clusters',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetK8sClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_k8s_cluster_with_options_async(
        self,
        request: edas_20170801_models.GetK8sClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetK8sClusterResponse:
        """
        @summary Queries Container Service for Kubernetes (ACK) clusters or Serverless Kubernetes clusters in a specified region.
        
        @param request: GetK8sClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetK8sClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_tag):
            query['RegionTag'] = request.region_tag
        if not UtilClient.is_unset(request.sub_cluster_type):
            query['SubClusterType'] = request.sub_cluster_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetK8sCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s_clusters',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetK8sClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_k8s_cluster(
        self,
        request: edas_20170801_models.GetK8sClusterRequest,
    ) -> edas_20170801_models.GetK8sClusterResponse:
        """
        @summary Queries Container Service for Kubernetes (ACK) clusters or Serverless Kubernetes clusters in a specified region.
        
        @param request: GetK8sClusterRequest
        @return: GetK8sClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_k8s_cluster_with_options(request, headers, runtime)

    async def get_k8s_cluster_async(
        self,
        request: edas_20170801_models.GetK8sClusterRequest,
    ) -> edas_20170801_models.GetK8sClusterResponse:
        """
        @summary Queries Container Service for Kubernetes (ACK) clusters or Serverless Kubernetes clusters in a specified region.
        
        @param request: GetK8sClusterRequest
        @return: GetK8sClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_k8s_cluster_with_options_async(request, headers, runtime)

    def get_k8s_services_with_options(
        self,
        request: edas_20170801_models.GetK8sServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetK8sServicesResponse:
        """
        @summary Queries application services that are deployed in a Kubernetes cluster.
        
        @param request: GetK8sServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetK8sServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetK8sServices',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_service',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetK8sServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_k8s_services_with_options_async(
        self,
        request: edas_20170801_models.GetK8sServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetK8sServicesResponse:
        """
        @summary Queries application services that are deployed in a Kubernetes cluster.
        
        @param request: GetK8sServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetK8sServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetK8sServices',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_service',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetK8sServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_k8s_services(
        self,
        request: edas_20170801_models.GetK8sServicesRequest,
    ) -> edas_20170801_models.GetK8sServicesResponse:
        """
        @summary Queries application services that are deployed in a Kubernetes cluster.
        
        @param request: GetK8sServicesRequest
        @return: GetK8sServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_k8s_services_with_options(request, headers, runtime)

    async def get_k8s_services_async(
        self,
        request: edas_20170801_models.GetK8sServicesRequest,
    ) -> edas_20170801_models.GetK8sServicesResponse:
        """
        @summary Queries application services that are deployed in a Kubernetes cluster.
        
        @param request: GetK8sServicesRequest
        @return: GetK8sServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_k8s_services_with_options_async(request, headers, runtime)

    def get_package_storage_credential_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetPackageStorageCredentialResponse:
        """
        @summary Queries the Security Token Service (STS) tokens that are required for temporary storage.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPackageStorageCredentialResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPackageStorageCredential',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/package_storage_credential',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetPackageStorageCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_package_storage_credential_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetPackageStorageCredentialResponse:
        """
        @summary Queries the Security Token Service (STS) tokens that are required for temporary storage.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPackageStorageCredentialResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPackageStorageCredential',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/package_storage_credential',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetPackageStorageCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_package_storage_credential(self) -> edas_20170801_models.GetPackageStorageCredentialResponse:
        """
        @summary Queries the Security Token Service (STS) tokens that are required for temporary storage.
        
        @return: GetPackageStorageCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_package_storage_credential_with_options(headers, runtime)

    async def get_package_storage_credential_async(self) -> edas_20170801_models.GetPackageStorageCredentialResponse:
        """
        @summary Queries the Security Token Service (STS) tokens that are required for temporary storage.
        
        @return: GetPackageStorageCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_package_storage_credential_with_options_async(headers, runtime)

    def get_scaling_rules_with_options(
        self,
        request: edas_20170801_models.GetScalingRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetScalingRulesResponse:
        """
        @summary Queries scaling rules.
        
        @param request: GetScalingRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScalingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScalingRules',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/scalingRules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scaling_rules_with_options_async(
        self,
        request: edas_20170801_models.GetScalingRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetScalingRulesResponse:
        """
        @summary Queries scaling rules.
        
        @param request: GetScalingRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScalingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScalingRules',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/scalingRules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetScalingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scaling_rules(
        self,
        request: edas_20170801_models.GetScalingRulesRequest,
    ) -> edas_20170801_models.GetScalingRulesResponse:
        """
        @summary Queries scaling rules.
        
        @param request: GetScalingRulesRequest
        @return: GetScalingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_scaling_rules_with_options(request, headers, runtime)

    async def get_scaling_rules_async(
        self,
        request: edas_20170801_models.GetScalingRulesRequest,
    ) -> edas_20170801_models.GetScalingRulesResponse:
        """
        @summary Queries scaling rules.
        
        @param request: GetScalingRulesRequest
        @return: GetScalingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_scaling_rules_with_options_async(request, headers, runtime)

    def get_secure_token_with_options(
        self,
        request: edas_20170801_models.GetSecureTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetSecureTokenResponse:
        """
        @summary Queries the security token information of a namespace. You can call this operation to query information, such as the AccessKey ID, AccessKey secret, tenant ID, and the domain name of Address Server, for the specified namespace.
        
        @param request: GetSecureTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSecureTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecureToken',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/secure_token',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetSecureTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secure_token_with_options_async(
        self,
        request: edas_20170801_models.GetSecureTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetSecureTokenResponse:
        """
        @summary Queries the security token information of a namespace. You can call this operation to query information, such as the AccessKey ID, AccessKey secret, tenant ID, and the domain name of Address Server, for the specified namespace.
        
        @param request: GetSecureTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSecureTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSecureToken',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/secure_token',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetSecureTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secure_token(
        self,
        request: edas_20170801_models.GetSecureTokenRequest,
    ) -> edas_20170801_models.GetSecureTokenResponse:
        """
        @summary Queries the security token information of a namespace. You can call this operation to query information, such as the AccessKey ID, AccessKey secret, tenant ID, and the domain name of Address Server, for the specified namespace.
        
        @param request: GetSecureTokenRequest
        @return: GetSecureTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_secure_token_with_options(request, headers, runtime)

    async def get_secure_token_async(
        self,
        request: edas_20170801_models.GetSecureTokenRequest,
    ) -> edas_20170801_models.GetSecureTokenResponse:
        """
        @summary Queries the security token information of a namespace. You can call this operation to query information, such as the AccessKey ID, AccessKey secret, tenant ID, and the domain name of Address Server, for the specified namespace.
        
        @param request: GetSecureTokenRequest
        @return: GetSecureTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_secure_token_with_options_async(request, headers, runtime)

    def get_service_consumers_page_with_options(
        self,
        request: edas_20170801_models.GetServiceConsumersPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetServiceConsumersPageResponse:
        """
        @summary Queries service consumers.
        
        @param request: GetServiceConsumersPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceConsumersPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        if not UtilClient.is_unset(request.group):
            query['group'] = request.group
        if not UtilClient.is_unset(request.ip):
            query['ip'] = request.ip
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.origin):
            query['origin'] = request.origin
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.registry_type):
            query['registryType'] = request.registry_type
        if not UtilClient.is_unset(request.service_id):
            query['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        if not UtilClient.is_unset(request.service_type):
            query['serviceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['serviceVersion'] = request.service_version
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceConsumersPage',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/sp/api/mseForOam/getServiceConsumersPage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetServiceConsumersPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_consumers_page_with_options_async(
        self,
        request: edas_20170801_models.GetServiceConsumersPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetServiceConsumersPageResponse:
        """
        @summary Queries service consumers.
        
        @param request: GetServiceConsumersPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceConsumersPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        if not UtilClient.is_unset(request.group):
            query['group'] = request.group
        if not UtilClient.is_unset(request.ip):
            query['ip'] = request.ip
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.origin):
            query['origin'] = request.origin
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.registry_type):
            query['registryType'] = request.registry_type
        if not UtilClient.is_unset(request.service_id):
            query['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        if not UtilClient.is_unset(request.service_type):
            query['serviceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['serviceVersion'] = request.service_version
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceConsumersPage',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/sp/api/mseForOam/getServiceConsumersPage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetServiceConsumersPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_consumers_page(
        self,
        request: edas_20170801_models.GetServiceConsumersPageRequest,
    ) -> edas_20170801_models.GetServiceConsumersPageResponse:
        """
        @summary Queries service consumers.
        
        @param request: GetServiceConsumersPageRequest
        @return: GetServiceConsumersPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_consumers_page_with_options(request, headers, runtime)

    async def get_service_consumers_page_async(
        self,
        request: edas_20170801_models.GetServiceConsumersPageRequest,
    ) -> edas_20170801_models.GetServiceConsumersPageResponse:
        """
        @summary Queries service consumers.
        
        @param request: GetServiceConsumersPageRequest
        @return: GetServiceConsumersPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_consumers_page_with_options_async(request, headers, runtime)

    def get_service_detail_with_options(
        self,
        request: edas_20170801_models.GetServiceDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetServiceDetailResponse:
        """
        @summary Queries service details.
        
        @param request: GetServiceDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        if not UtilClient.is_unset(request.group):
            query['group'] = request.group
        if not UtilClient.is_unset(request.ip):
            query['ip'] = request.ip
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.origin):
            query['origin'] = request.origin
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.registry_type):
            query['registryType'] = request.registry_type
        if not UtilClient.is_unset(request.service_id):
            query['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        if not UtilClient.is_unset(request.service_type):
            query['serviceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['serviceVersion'] = request.service_version
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceDetail',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/sp/api/mseForOam/getServiceDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetServiceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_detail_with_options_async(
        self,
        request: edas_20170801_models.GetServiceDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetServiceDetailResponse:
        """
        @summary Queries service details.
        
        @param request: GetServiceDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        if not UtilClient.is_unset(request.group):
            query['group'] = request.group
        if not UtilClient.is_unset(request.ip):
            query['ip'] = request.ip
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.origin):
            query['origin'] = request.origin
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.registry_type):
            query['registryType'] = request.registry_type
        if not UtilClient.is_unset(request.service_id):
            query['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        if not UtilClient.is_unset(request.service_type):
            query['serviceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['serviceVersion'] = request.service_version
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceDetail',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/sp/api/mseForOam/getServiceDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetServiceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_detail(
        self,
        request: edas_20170801_models.GetServiceDetailRequest,
    ) -> edas_20170801_models.GetServiceDetailResponse:
        """
        @summary Queries service details.
        
        @param request: GetServiceDetailRequest
        @return: GetServiceDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_detail_with_options(request, headers, runtime)

    async def get_service_detail_async(
        self,
        request: edas_20170801_models.GetServiceDetailRequest,
    ) -> edas_20170801_models.GetServiceDetailResponse:
        """
        @summary Queries service details.
        
        @param request: GetServiceDetailRequest
        @return: GetServiceDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_detail_with_options_async(request, headers, runtime)

    def get_service_list_page_with_options(
        self,
        request: edas_20170801_models.GetServiceListPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetServiceListPageResponse:
        """
        @summary Queries services.
        
        @param request: GetServiceListPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceListPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.origin):
            query['origin'] = request.origin
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.search_type):
            query['searchType'] = request.search_type
        if not UtilClient.is_unset(request.search_value):
            query['searchValue'] = request.search_value
        if not UtilClient.is_unset(request.service_type):
            query['serviceType'] = request.service_type
        if not UtilClient.is_unset(request.side):
            query['side'] = request.side
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceListPage',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/sp/api/mseForOam/getServiceListPage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetServiceListPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_list_page_with_options_async(
        self,
        request: edas_20170801_models.GetServiceListPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetServiceListPageResponse:
        """
        @summary Queries services.
        
        @param request: GetServiceListPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceListPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.origin):
            query['origin'] = request.origin
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.search_type):
            query['searchType'] = request.search_type
        if not UtilClient.is_unset(request.search_value):
            query['searchValue'] = request.search_value
        if not UtilClient.is_unset(request.service_type):
            query['serviceType'] = request.service_type
        if not UtilClient.is_unset(request.side):
            query['side'] = request.side
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceListPage',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/sp/api/mseForOam/getServiceListPage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetServiceListPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_list_page(
        self,
        request: edas_20170801_models.GetServiceListPageRequest,
    ) -> edas_20170801_models.GetServiceListPageResponse:
        """
        @summary Queries services.
        
        @param request: GetServiceListPageRequest
        @return: GetServiceListPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_list_page_with_options(request, headers, runtime)

    async def get_service_list_page_async(
        self,
        request: edas_20170801_models.GetServiceListPageRequest,
    ) -> edas_20170801_models.GetServiceListPageResponse:
        """
        @summary Queries services.
        
        @param request: GetServiceListPageRequest
        @return: GetServiceListPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_list_page_with_options_async(request, headers, runtime)

    def get_service_method_page_with_options(
        self,
        request: edas_20170801_models.GetServiceMethodPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetServiceMethodPageResponse:
        """
        @summary Queries service methods.
        
        @param request: GetServiceMethodPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceMethodPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        if not UtilClient.is_unset(request.group):
            query['group'] = request.group
        if not UtilClient.is_unset(request.ip):
            query['ip'] = request.ip
        if not UtilClient.is_unset(request.method_controller):
            query['methodController'] = request.method_controller
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.origin):
            query['origin'] = request.origin
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['path'] = request.path
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.registry_type):
            query['registryType'] = request.registry_type
        if not UtilClient.is_unset(request.service_id):
            query['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        if not UtilClient.is_unset(request.service_type):
            query['serviceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['serviceVersion'] = request.service_version
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceMethodPage',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/sp/api/mseForOam/getServiceMethodPage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetServiceMethodPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_method_page_with_options_async(
        self,
        request: edas_20170801_models.GetServiceMethodPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetServiceMethodPageResponse:
        """
        @summary Queries service methods.
        
        @param request: GetServiceMethodPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceMethodPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        if not UtilClient.is_unset(request.group):
            query['group'] = request.group
        if not UtilClient.is_unset(request.ip):
            query['ip'] = request.ip
        if not UtilClient.is_unset(request.method_controller):
            query['methodController'] = request.method_controller
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.origin):
            query['origin'] = request.origin
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['path'] = request.path
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.registry_type):
            query['registryType'] = request.registry_type
        if not UtilClient.is_unset(request.service_id):
            query['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        if not UtilClient.is_unset(request.service_type):
            query['serviceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['serviceVersion'] = request.service_version
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceMethodPage',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/sp/api/mseForOam/getServiceMethodPage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetServiceMethodPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_method_page(
        self,
        request: edas_20170801_models.GetServiceMethodPageRequest,
    ) -> edas_20170801_models.GetServiceMethodPageResponse:
        """
        @summary Queries service methods.
        
        @param request: GetServiceMethodPageRequest
        @return: GetServiceMethodPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_method_page_with_options(request, headers, runtime)

    async def get_service_method_page_async(
        self,
        request: edas_20170801_models.GetServiceMethodPageRequest,
    ) -> edas_20170801_models.GetServiceMethodPageResponse:
        """
        @summary Queries service methods.
        
        @param request: GetServiceMethodPageRequest
        @return: GetServiceMethodPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_method_page_with_options_async(request, headers, runtime)

    def get_service_providers_page_with_options(
        self,
        request: edas_20170801_models.GetServiceProvidersPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetServiceProvidersPageResponse:
        """
        @summary Queries service providers.
        
        @param request: GetServiceProvidersPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceProvidersPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        if not UtilClient.is_unset(request.group):
            query['group'] = request.group
        if not UtilClient.is_unset(request.ip):
            query['ip'] = request.ip
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.origin):
            query['origin'] = request.origin
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.registry_type):
            query['registryType'] = request.registry_type
        if not UtilClient.is_unset(request.service_id):
            query['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        if not UtilClient.is_unset(request.service_type):
            query['serviceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['serviceVersion'] = request.service_version
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceProvidersPage',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/sp/api/mseForOam/getServiceProvidersPage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetServiceProvidersPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_providers_page_with_options_async(
        self,
        request: edas_20170801_models.GetServiceProvidersPageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetServiceProvidersPageResponse:
        """
        @summary Queries service providers.
        
        @param request: GetServiceProvidersPageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceProvidersPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        if not UtilClient.is_unset(request.group):
            query['group'] = request.group
        if not UtilClient.is_unset(request.ip):
            query['ip'] = request.ip
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.origin):
            query['origin'] = request.origin
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.registry_type):
            query['registryType'] = request.registry_type
        if not UtilClient.is_unset(request.service_id):
            query['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        if not UtilClient.is_unset(request.service_type):
            query['serviceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['serviceVersion'] = request.service_version
        if not UtilClient.is_unset(request.size):
            query['size'] = request.size
        if not UtilClient.is_unset(request.source):
            query['source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceProvidersPage',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/sp/api/mseForOam/getServiceProvidersPage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetServiceProvidersPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_providers_page(
        self,
        request: edas_20170801_models.GetServiceProvidersPageRequest,
    ) -> edas_20170801_models.GetServiceProvidersPageResponse:
        """
        @summary Queries service providers.
        
        @param request: GetServiceProvidersPageRequest
        @return: GetServiceProvidersPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_providers_page_with_options(request, headers, runtime)

    async def get_service_providers_page_async(
        self,
        request: edas_20170801_models.GetServiceProvidersPageRequest,
    ) -> edas_20170801_models.GetServiceProvidersPageResponse:
        """
        @summary Queries service providers.
        
        @param request: GetServiceProvidersPageRequest
        @return: GetServiceProvidersPageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_providers_page_with_options_async(request, headers, runtime)

    def get_web_container_config_with_options(
        self,
        request: edas_20170801_models.GetWebContainerConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetWebContainerConfigResponse:
        """
        @summary Queries the Tomcat configurations of an application.
        
        @description **\
        
        @param request: GetWebContainerConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWebContainerConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWebContainerConfig',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/oam/web_container_config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetWebContainerConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_web_container_config_with_options_async(
        self,
        request: edas_20170801_models.GetWebContainerConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.GetWebContainerConfigResponse:
        """
        @summary Queries the Tomcat configurations of an application.
        
        @description **\
        
        @param request: GetWebContainerConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWebContainerConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWebContainerConfig',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/oam/web_container_config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.GetWebContainerConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_web_container_config(
        self,
        request: edas_20170801_models.GetWebContainerConfigRequest,
    ) -> edas_20170801_models.GetWebContainerConfigResponse:
        """
        @summary Queries the Tomcat configurations of an application.
        
        @description **\
        
        @param request: GetWebContainerConfigRequest
        @return: GetWebContainerConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_web_container_config_with_options(request, headers, runtime)

    async def get_web_container_config_async(
        self,
        request: edas_20170801_models.GetWebContainerConfigRequest,
    ) -> edas_20170801_models.GetWebContainerConfigResponse:
        """
        @summary Queries the Tomcat configurations of an application.
        
        @description **\
        
        @param request: GetWebContainerConfigRequest
        @return: GetWebContainerConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_web_container_config_with_options_async(request, headers, runtime)

    def import_k8s_cluster_with_options(
        self,
        request: edas_20170801_models.ImportK8sClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ImportK8sClusterResponse:
        """
        @summary Imports a Container Service for Kubernetes (ACK) cluster or a serverless Kubernetes cluster to Enterprise Distributed Application Service (EDAS).
        
        @param request: ImportK8sClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportK8sClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.enable_asm):
            query['EnableAsm'] = request.enable_asm
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportK8sCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/import_k8s_cluster',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ImportK8sClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_k8s_cluster_with_options_async(
        self,
        request: edas_20170801_models.ImportK8sClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ImportK8sClusterResponse:
        """
        @summary Imports a Container Service for Kubernetes (ACK) cluster or a serverless Kubernetes cluster to Enterprise Distributed Application Service (EDAS).
        
        @param request: ImportK8sClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportK8sClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.enable_asm):
            query['EnableAsm'] = request.enable_asm
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportK8sCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/import_k8s_cluster',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ImportK8sClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_k8s_cluster(
        self,
        request: edas_20170801_models.ImportK8sClusterRequest,
    ) -> edas_20170801_models.ImportK8sClusterResponse:
        """
        @summary Imports a Container Service for Kubernetes (ACK) cluster or a serverless Kubernetes cluster to Enterprise Distributed Application Service (EDAS).
        
        @param request: ImportK8sClusterRequest
        @return: ImportK8sClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.import_k8s_cluster_with_options(request, headers, runtime)

    async def import_k8s_cluster_async(
        self,
        request: edas_20170801_models.ImportK8sClusterRequest,
    ) -> edas_20170801_models.ImportK8sClusterResponse:
        """
        @summary Imports a Container Service for Kubernetes (ACK) cluster or a serverless Kubernetes cluster to Enterprise Distributed Application Service (EDAS).
        
        @param request: ImportK8sClusterRequest
        @return: ImportK8sClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.import_k8s_cluster_with_options_async(request, headers, runtime)

    def insert_application_with_options(
        self,
        request: edas_20170801_models.InsertApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertApplicationResponse:
        """
        @summary Creates an application in an Elastic Compute Service (ECS) cluster.
        
        @description > To create an application in a Kubernetes cluster, call the InsertK8sApplication operation provided by Enterprise Distributed Application Service (EDAS).
        
        @param request: InsertApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_ids):
            query['ComponentIds'] = request.component_ids
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ecu_info):
            query['EcuInfo'] = request.ecu_info
        if not UtilClient.is_unset(request.enable_port_check):
            query['EnablePortCheck'] = request.enable_port_check
        if not UtilClient.is_unset(request.enable_url_check):
            query['EnableUrlCheck'] = request.enable_url_check
        if not UtilClient.is_unset(request.health_check_url):
            query['HealthCheckUrl'] = request.health_check_url
        if not UtilClient.is_unset(request.hooks):
            query['Hooks'] = request.hooks
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.jvm_options):
            query['JvmOptions'] = request.jvm_options
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not UtilClient.is_unset(request.max_heap_size):
            query['MaxHeapSize'] = request.max_heap_size
        if not UtilClient.is_unset(request.max_perm_size):
            query['MaxPermSize'] = request.max_perm_size
        if not UtilClient.is_unset(request.mem):
            query['Mem'] = request.mem
        if not UtilClient.is_unset(request.min_heap_size):
            query['MinHeapSize'] = request.min_heap_size
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.reserved_port_str):
            query['ReservedPortStr'] = request.reserved_port_str
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_create_app',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_application_with_options_async(
        self,
        request: edas_20170801_models.InsertApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertApplicationResponse:
        """
        @summary Creates an application in an Elastic Compute Service (ECS) cluster.
        
        @description > To create an application in a Kubernetes cluster, call the InsertK8sApplication operation provided by Enterprise Distributed Application Service (EDAS).
        
        @param request: InsertApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_ids):
            query['ComponentIds'] = request.component_ids
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ecu_info):
            query['EcuInfo'] = request.ecu_info
        if not UtilClient.is_unset(request.enable_port_check):
            query['EnablePortCheck'] = request.enable_port_check
        if not UtilClient.is_unset(request.enable_url_check):
            query['EnableUrlCheck'] = request.enable_url_check
        if not UtilClient.is_unset(request.health_check_url):
            query['HealthCheckUrl'] = request.health_check_url
        if not UtilClient.is_unset(request.hooks):
            query['Hooks'] = request.hooks
        if not UtilClient.is_unset(request.jdk):
            query['Jdk'] = request.jdk
        if not UtilClient.is_unset(request.jvm_options):
            query['JvmOptions'] = request.jvm_options
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not UtilClient.is_unset(request.max_heap_size):
            query['MaxHeapSize'] = request.max_heap_size
        if not UtilClient.is_unset(request.max_perm_size):
            query['MaxPermSize'] = request.max_perm_size
        if not UtilClient.is_unset(request.mem):
            query['Mem'] = request.mem
        if not UtilClient.is_unset(request.min_heap_size):
            query['MinHeapSize'] = request.min_heap_size
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.reserved_port_str):
            query['ReservedPortStr'] = request.reserved_port_str
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_create_app',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_application(
        self,
        request: edas_20170801_models.InsertApplicationRequest,
    ) -> edas_20170801_models.InsertApplicationResponse:
        """
        @summary Creates an application in an Elastic Compute Service (ECS) cluster.
        
        @description > To create an application in a Kubernetes cluster, call the InsertK8sApplication operation provided by Enterprise Distributed Application Service (EDAS).
        
        @param request: InsertApplicationRequest
        @return: InsertApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.insert_application_with_options(request, headers, runtime)

    async def insert_application_async(
        self,
        request: edas_20170801_models.InsertApplicationRequest,
    ) -> edas_20170801_models.InsertApplicationResponse:
        """
        @summary Creates an application in an Elastic Compute Service (ECS) cluster.
        
        @description > To create an application in a Kubernetes cluster, call the InsertK8sApplication operation provided by Enterprise Distributed Application Service (EDAS).
        
        @param request: InsertApplicationRequest
        @return: InsertApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.insert_application_with_options_async(request, headers, runtime)

    def insert_cluster_with_options(
        self,
        request: edas_20170801_models.InsertClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertClusterResponse:
        """
        @summary Creates a cluster.
        
        @param request: InsertClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.iaas_provider):
            query['IaasProvider'] = request.iaas_provider
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not UtilClient.is_unset(request.network_mode):
            query['NetworkMode'] = request.network_mode
        if not UtilClient.is_unset(request.oversold_factor):
            query['OversoldFactor'] = request.oversold_factor
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/cluster',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_cluster_with_options_async(
        self,
        request: edas_20170801_models.InsertClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertClusterResponse:
        """
        @summary Creates a cluster.
        
        @param request: InsertClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.iaas_provider):
            query['IaasProvider'] = request.iaas_provider
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not UtilClient.is_unset(request.network_mode):
            query['NetworkMode'] = request.network_mode
        if not UtilClient.is_unset(request.oversold_factor):
            query['OversoldFactor'] = request.oversold_factor
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/cluster',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_cluster(
        self,
        request: edas_20170801_models.InsertClusterRequest,
    ) -> edas_20170801_models.InsertClusterResponse:
        """
        @summary Creates a cluster.
        
        @param request: InsertClusterRequest
        @return: InsertClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.insert_cluster_with_options(request, headers, runtime)

    async def insert_cluster_async(
        self,
        request: edas_20170801_models.InsertClusterRequest,
    ) -> edas_20170801_models.InsertClusterResponse:
        """
        @summary Creates a cluster.
        
        @param request: InsertClusterRequest
        @return: InsertClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.insert_cluster_with_options_async(request, headers, runtime)

    def insert_cluster_member_with_options(
        self,
        request: edas_20170801_models.InsertClusterMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertClusterMemberResponse:
        """
        @summary Imports Elastic Compute Service (ECS) instances into an ECS cluster.
        
        @description ##
        If you call this operation to import an ECS instance, the operating system of the ECS instance is reinstalled. After the operating system is reinstalled, all original data of the ECS instance is deleted. In addition, you must set a logon password for the ECS instance. Make sure that no important data exists on the ECS instance that you want to import or data has been backed up for the ECS instance.
        > We recommend that you call the InstallAgent operation instead of this operation. For more information, see [InstallAgent](https://help.aliyun.com/document_detail/127023.html).
        
        @param request: InsertClusterMemberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertClusterMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['clusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_ids):
            query['instanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.password):
            query['password'] = request.password
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertClusterMember',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/cluster_member',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertClusterMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_cluster_member_with_options_async(
        self,
        request: edas_20170801_models.InsertClusterMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertClusterMemberResponse:
        """
        @summary Imports Elastic Compute Service (ECS) instances into an ECS cluster.
        
        @description ##
        If you call this operation to import an ECS instance, the operating system of the ECS instance is reinstalled. After the operating system is reinstalled, all original data of the ECS instance is deleted. In addition, you must set a logon password for the ECS instance. Make sure that no important data exists on the ECS instance that you want to import or data has been backed up for the ECS instance.
        > We recommend that you call the InstallAgent operation instead of this operation. For more information, see [InstallAgent](https://help.aliyun.com/document_detail/127023.html).
        
        @param request: InsertClusterMemberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertClusterMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['clusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_ids):
            query['instanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.password):
            query['password'] = request.password
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertClusterMember',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/cluster_member',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertClusterMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_cluster_member(
        self,
        request: edas_20170801_models.InsertClusterMemberRequest,
    ) -> edas_20170801_models.InsertClusterMemberResponse:
        """
        @summary Imports Elastic Compute Service (ECS) instances into an ECS cluster.
        
        @description ##
        If you call this operation to import an ECS instance, the operating system of the ECS instance is reinstalled. After the operating system is reinstalled, all original data of the ECS instance is deleted. In addition, you must set a logon password for the ECS instance. Make sure that no important data exists on the ECS instance that you want to import or data has been backed up for the ECS instance.
        > We recommend that you call the InstallAgent operation instead of this operation. For more information, see [InstallAgent](https://help.aliyun.com/document_detail/127023.html).
        
        @param request: InsertClusterMemberRequest
        @return: InsertClusterMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.insert_cluster_member_with_options(request, headers, runtime)

    async def insert_cluster_member_async(
        self,
        request: edas_20170801_models.InsertClusterMemberRequest,
    ) -> edas_20170801_models.InsertClusterMemberResponse:
        """
        @summary Imports Elastic Compute Service (ECS) instances into an ECS cluster.
        
        @description ##
        If you call this operation to import an ECS instance, the operating system of the ECS instance is reinstalled. After the operating system is reinstalled, all original data of the ECS instance is deleted. In addition, you must set a logon password for the ECS instance. Make sure that no important data exists on the ECS instance that you want to import or data has been backed up for the ECS instance.
        > We recommend that you call the InstallAgent operation instead of this operation. For more information, see [InstallAgent](https://help.aliyun.com/document_detail/127023.html).
        
        @param request: InsertClusterMemberRequest
        @return: InsertClusterMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.insert_cluster_member_with_options_async(request, headers, runtime)

    def insert_deploy_group_with_options(
        self,
        request: edas_20170801_models.InsertDeployGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertDeployGroupResponse:
        """
        @summary Creates an instance group for a specified application.
        
        @param request: InsertDeployGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertDeployGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.init_package_version_id):
            query['InitPackageVersionId'] = request.init_package_version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertDeployGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/deploy_group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertDeployGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_deploy_group_with_options_async(
        self,
        request: edas_20170801_models.InsertDeployGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertDeployGroupResponse:
        """
        @summary Creates an instance group for a specified application.
        
        @param request: InsertDeployGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertDeployGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.init_package_version_id):
            query['InitPackageVersionId'] = request.init_package_version_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertDeployGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/deploy_group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertDeployGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_deploy_group(
        self,
        request: edas_20170801_models.InsertDeployGroupRequest,
    ) -> edas_20170801_models.InsertDeployGroupResponse:
        """
        @summary Creates an instance group for a specified application.
        
        @param request: InsertDeployGroupRequest
        @return: InsertDeployGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.insert_deploy_group_with_options(request, headers, runtime)

    async def insert_deploy_group_async(
        self,
        request: edas_20170801_models.InsertDeployGroupRequest,
    ) -> edas_20170801_models.InsertDeployGroupResponse:
        """
        @summary Creates an instance group for a specified application.
        
        @param request: InsertDeployGroupRequest
        @return: InsertDeployGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.insert_deploy_group_with_options_async(request, headers, runtime)

    def insert_k8s_application_with_options(
        self,
        request: edas_20170801_models.InsertK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertK8sApplicationResponse:
        """
        @summary Creates an application in a Container Service for Kubernetes (ACK) cluster or serverless Kubernetes cluster.
        
        @param request: InsertK8sApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertK8sApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.app_config):
            query['AppConfig'] = request.app_config
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_template_name):
            query['AppTemplateName'] = request.app_template_name
        if not UtilClient.is_unset(request.application_description):
            query['ApplicationDescription'] = request.application_description
        if not UtilClient.is_unset(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.config_mount_descs):
            query['ConfigMountDescs'] = request.config_mount_descs
        if not UtilClient.is_unset(request.container_registry_id):
            query['ContainerRegistryId'] = request.container_registry_id
        if not UtilClient.is_unset(request.cs_cluster_id):
            query['CsClusterId'] = request.cs_cluster_id
        if not UtilClient.is_unset(request.custom_affinity):
            query['CustomAffinity'] = request.custom_affinity
        if not UtilClient.is_unset(request.custom_agent_version):
            query['CustomAgentVersion'] = request.custom_agent_version
        if not UtilClient.is_unset(request.custom_tolerations):
            query['CustomTolerations'] = request.custom_tolerations
        if not UtilClient.is_unset(request.deploy_across_nodes):
            query['DeployAcrossNodes'] = request.deploy_across_nodes
        if not UtilClient.is_unset(request.deploy_across_zones):
            query['DeployAcrossZones'] = request.deploy_across_zones
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.empty_dirs):
            query['EmptyDirs'] = request.empty_dirs
        if not UtilClient.is_unset(request.enable_ahas):
            query['EnableAhas'] = request.enable_ahas
        if not UtilClient.is_unset(request.enable_asm):
            query['EnableAsm'] = request.enable_asm
        if not UtilClient.is_unset(request.enable_empty_push_reject):
            query['EnableEmptyPushReject'] = request.enable_empty_push_reject
        if not UtilClient.is_unset(request.enable_lossless_rule):
            query['EnableLosslessRule'] = request.enable_lossless_rule
        if not UtilClient.is_unset(request.env_froms):
            query['EnvFroms'] = request.env_froms
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.feature_config):
            query['FeatureConfig'] = request.feature_config
        if not UtilClient.is_unset(request.image_platforms):
            query['ImagePlatforms'] = request.image_platforms
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not UtilClient.is_unset(request.internet_slb_id):
            query['InternetSlbId'] = request.internet_slb_id
        if not UtilClient.is_unset(request.internet_slb_port):
            query['InternetSlbPort'] = request.internet_slb_port
        if not UtilClient.is_unset(request.internet_slb_protocol):
            query['InternetSlbProtocol'] = request.internet_slb_protocol
        if not UtilClient.is_unset(request.internet_target_port):
            query['InternetTargetPort'] = request.internet_target_port
        if not UtilClient.is_unset(request.intranet_slb_id):
            query['IntranetSlbId'] = request.intranet_slb_id
        if not UtilClient.is_unset(request.intranet_slb_port):
            query['IntranetSlbPort'] = request.intranet_slb_port
        if not UtilClient.is_unset(request.intranet_slb_protocol):
            query['IntranetSlbProtocol'] = request.intranet_slb_protocol
        if not UtilClient.is_unset(request.intranet_target_port):
            query['IntranetTargetPort'] = request.intranet_target_port
        if not UtilClient.is_unset(request.is_multilingual_app):
            query['IsMultilingualApp'] = request.is_multilingual_app
        if not UtilClient.is_unset(request.jdk):
            query['JDK'] = request.jdk
        if not UtilClient.is_unset(request.java_start_up_config):
            query['JavaStartUpConfig'] = request.java_start_up_config
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.limit_cpu):
            query['LimitCpu'] = request.limit_cpu
        if not UtilClient.is_unset(request.limit_ephemeral_storage):
            query['LimitEphemeralStorage'] = request.limit_ephemeral_storage
        if not UtilClient.is_unset(request.limit_mem):
            query['LimitMem'] = request.limit_mem
        if not UtilClient.is_unset(request.limitm_cpu):
            query['LimitmCpu'] = request.limitm_cpu
        if not UtilClient.is_unset(request.liveness):
            query['Liveness'] = request.liveness
        if not UtilClient.is_unset(request.local_volume):
            query['LocalVolume'] = request.local_volume
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not UtilClient.is_unset(request.lossless_rule_aligned):
            query['LosslessRuleAligned'] = request.lossless_rule_aligned
        if not UtilClient.is_unset(request.lossless_rule_delay_time):
            query['LosslessRuleDelayTime'] = request.lossless_rule_delay_time
        if not UtilClient.is_unset(request.lossless_rule_func_type):
            query['LosslessRuleFuncType'] = request.lossless_rule_func_type
        if not UtilClient.is_unset(request.lossless_rule_related):
            query['LosslessRuleRelated'] = request.lossless_rule_related
        if not UtilClient.is_unset(request.lossless_rule_warmup_time):
            query['LosslessRuleWarmupTime'] = request.lossless_rule_warmup_time
        if not UtilClient.is_unset(request.mount_descs):
            query['MountDescs'] = request.mount_descs
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.pvc_mount_descs):
            query['PvcMountDescs'] = request.pvc_mount_descs
        if not UtilClient.is_unset(request.readiness):
            query['Readiness'] = request.readiness
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.requests_cpu):
            query['RequestsCpu'] = request.requests_cpu
        if not UtilClient.is_unset(request.requests_ephemeral_storage):
            query['RequestsEphemeralStorage'] = request.requests_ephemeral_storage
        if not UtilClient.is_unset(request.requests_mem):
            query['RequestsMem'] = request.requests_mem
        if not UtilClient.is_unset(request.requestsm_cpu):
            query['RequestsmCpu'] = request.requestsm_cpu
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.runtime_class_name):
            query['RuntimeClassName'] = request.runtime_class_name
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.security_context):
            query['SecurityContext'] = request.security_context
        if not UtilClient.is_unset(request.service_configs):
            query['ServiceConfigs'] = request.service_configs
        if not UtilClient.is_unset(request.sidecars):
            query['Sidecars'] = request.sidecars
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.startup):
            query['Startup'] = request.startup
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.terminate_grace_period):
            query['TerminateGracePeriod'] = request.terminate_grace_period
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.uri_encoding):
            query['UriEncoding'] = request.uri_encoding
        if not UtilClient.is_unset(request.use_body_encoding):
            query['UseBodyEncoding'] = request.use_body_encoding
        if not UtilClient.is_unset(request.user_base_image_url):
            query['UserBaseImageUrl'] = request.user_base_image_url
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        if not UtilClient.is_unset(request.web_container_config):
            query['WebContainerConfig'] = request.web_container_config
        if not UtilClient.is_unset(request.workload_type):
            query['WorkloadType'] = request.workload_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertK8sApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/create_k8s_app',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertK8sApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_k8s_application_with_options_async(
        self,
        request: edas_20170801_models.InsertK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertK8sApplicationResponse:
        """
        @summary Creates an application in a Container Service for Kubernetes (ACK) cluster or serverless Kubernetes cluster.
        
        @param request: InsertK8sApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertK8sApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.app_config):
            query['AppConfig'] = request.app_config
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_template_name):
            query['AppTemplateName'] = request.app_template_name
        if not UtilClient.is_unset(request.application_description):
            query['ApplicationDescription'] = request.application_description
        if not UtilClient.is_unset(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.command_args):
            query['CommandArgs'] = request.command_args
        if not UtilClient.is_unset(request.config_mount_descs):
            query['ConfigMountDescs'] = request.config_mount_descs
        if not UtilClient.is_unset(request.container_registry_id):
            query['ContainerRegistryId'] = request.container_registry_id
        if not UtilClient.is_unset(request.cs_cluster_id):
            query['CsClusterId'] = request.cs_cluster_id
        if not UtilClient.is_unset(request.custom_affinity):
            query['CustomAffinity'] = request.custom_affinity
        if not UtilClient.is_unset(request.custom_agent_version):
            query['CustomAgentVersion'] = request.custom_agent_version
        if not UtilClient.is_unset(request.custom_tolerations):
            query['CustomTolerations'] = request.custom_tolerations
        if not UtilClient.is_unset(request.deploy_across_nodes):
            query['DeployAcrossNodes'] = request.deploy_across_nodes
        if not UtilClient.is_unset(request.deploy_across_zones):
            query['DeployAcrossZones'] = request.deploy_across_zones
        if not UtilClient.is_unset(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not UtilClient.is_unset(request.empty_dirs):
            query['EmptyDirs'] = request.empty_dirs
        if not UtilClient.is_unset(request.enable_ahas):
            query['EnableAhas'] = request.enable_ahas
        if not UtilClient.is_unset(request.enable_asm):
            query['EnableAsm'] = request.enable_asm
        if not UtilClient.is_unset(request.enable_empty_push_reject):
            query['EnableEmptyPushReject'] = request.enable_empty_push_reject
        if not UtilClient.is_unset(request.enable_lossless_rule):
            query['EnableLosslessRule'] = request.enable_lossless_rule
        if not UtilClient.is_unset(request.env_froms):
            query['EnvFroms'] = request.env_froms
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.feature_config):
            query['FeatureConfig'] = request.feature_config
        if not UtilClient.is_unset(request.image_platforms):
            query['ImagePlatforms'] = request.image_platforms
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not UtilClient.is_unset(request.internet_slb_id):
            query['InternetSlbId'] = request.internet_slb_id
        if not UtilClient.is_unset(request.internet_slb_port):
            query['InternetSlbPort'] = request.internet_slb_port
        if not UtilClient.is_unset(request.internet_slb_protocol):
            query['InternetSlbProtocol'] = request.internet_slb_protocol
        if not UtilClient.is_unset(request.internet_target_port):
            query['InternetTargetPort'] = request.internet_target_port
        if not UtilClient.is_unset(request.intranet_slb_id):
            query['IntranetSlbId'] = request.intranet_slb_id
        if not UtilClient.is_unset(request.intranet_slb_port):
            query['IntranetSlbPort'] = request.intranet_slb_port
        if not UtilClient.is_unset(request.intranet_slb_protocol):
            query['IntranetSlbProtocol'] = request.intranet_slb_protocol
        if not UtilClient.is_unset(request.intranet_target_port):
            query['IntranetTargetPort'] = request.intranet_target_port
        if not UtilClient.is_unset(request.is_multilingual_app):
            query['IsMultilingualApp'] = request.is_multilingual_app
        if not UtilClient.is_unset(request.jdk):
            query['JDK'] = request.jdk
        if not UtilClient.is_unset(request.java_start_up_config):
            query['JavaStartUpConfig'] = request.java_start_up_config
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.limit_cpu):
            query['LimitCpu'] = request.limit_cpu
        if not UtilClient.is_unset(request.limit_ephemeral_storage):
            query['LimitEphemeralStorage'] = request.limit_ephemeral_storage
        if not UtilClient.is_unset(request.limit_mem):
            query['LimitMem'] = request.limit_mem
        if not UtilClient.is_unset(request.limitm_cpu):
            query['LimitmCpu'] = request.limitm_cpu
        if not UtilClient.is_unset(request.liveness):
            query['Liveness'] = request.liveness
        if not UtilClient.is_unset(request.local_volume):
            query['LocalVolume'] = request.local_volume
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not UtilClient.is_unset(request.lossless_rule_aligned):
            query['LosslessRuleAligned'] = request.lossless_rule_aligned
        if not UtilClient.is_unset(request.lossless_rule_delay_time):
            query['LosslessRuleDelayTime'] = request.lossless_rule_delay_time
        if not UtilClient.is_unset(request.lossless_rule_func_type):
            query['LosslessRuleFuncType'] = request.lossless_rule_func_type
        if not UtilClient.is_unset(request.lossless_rule_related):
            query['LosslessRuleRelated'] = request.lossless_rule_related
        if not UtilClient.is_unset(request.lossless_rule_warmup_time):
            query['LosslessRuleWarmupTime'] = request.lossless_rule_warmup_time
        if not UtilClient.is_unset(request.mount_descs):
            query['MountDescs'] = request.mount_descs
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.nas_id):
            query['NasId'] = request.nas_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.package_version):
            query['PackageVersion'] = request.package_version
        if not UtilClient.is_unset(request.post_start):
            query['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.pvc_mount_descs):
            query['PvcMountDescs'] = request.pvc_mount_descs
        if not UtilClient.is_unset(request.readiness):
            query['Readiness'] = request.readiness
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        if not UtilClient.is_unset(request.requests_cpu):
            query['RequestsCpu'] = request.requests_cpu
        if not UtilClient.is_unset(request.requests_ephemeral_storage):
            query['RequestsEphemeralStorage'] = request.requests_ephemeral_storage
        if not UtilClient.is_unset(request.requests_mem):
            query['RequestsMem'] = request.requests_mem
        if not UtilClient.is_unset(request.requestsm_cpu):
            query['RequestsmCpu'] = request.requestsm_cpu
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.runtime_class_name):
            query['RuntimeClassName'] = request.runtime_class_name
        if not UtilClient.is_unset(request.secret_name):
            query['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.security_context):
            query['SecurityContext'] = request.security_context
        if not UtilClient.is_unset(request.service_configs):
            query['ServiceConfigs'] = request.service_configs
        if not UtilClient.is_unset(request.sidecars):
            query['Sidecars'] = request.sidecars
        if not UtilClient.is_unset(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not UtilClient.is_unset(request.startup):
            query['Startup'] = request.startup
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.terminate_grace_period):
            query['TerminateGracePeriod'] = request.terminate_grace_period
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.uri_encoding):
            query['UriEncoding'] = request.uri_encoding
        if not UtilClient.is_unset(request.use_body_encoding):
            query['UseBodyEncoding'] = request.use_body_encoding
        if not UtilClient.is_unset(request.user_base_image_url):
            query['UserBaseImageUrl'] = request.user_base_image_url
        if not UtilClient.is_unset(request.web_container):
            query['WebContainer'] = request.web_container
        if not UtilClient.is_unset(request.web_container_config):
            query['WebContainerConfig'] = request.web_container_config
        if not UtilClient.is_unset(request.workload_type):
            query['WorkloadType'] = request.workload_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertK8sApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/create_k8s_app',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertK8sApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_k8s_application(
        self,
        request: edas_20170801_models.InsertK8sApplicationRequest,
    ) -> edas_20170801_models.InsertK8sApplicationResponse:
        """
        @summary Creates an application in a Container Service for Kubernetes (ACK) cluster or serverless Kubernetes cluster.
        
        @param request: InsertK8sApplicationRequest
        @return: InsertK8sApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.insert_k8s_application_with_options(request, headers, runtime)

    async def insert_k8s_application_async(
        self,
        request: edas_20170801_models.InsertK8sApplicationRequest,
    ) -> edas_20170801_models.InsertK8sApplicationResponse:
        """
        @summary Creates an application in a Container Service for Kubernetes (ACK) cluster or serverless Kubernetes cluster.
        
        @param request: InsertK8sApplicationRequest
        @return: InsertK8sApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.insert_k8s_application_with_options_async(request, headers, runtime)

    def insert_or_update_region_with_options(
        self,
        request: edas_20170801_models.InsertOrUpdateRegionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertOrUpdateRegionResponse:
        """
        @summary Creates or edits a custom namespace.
        
        @param request: InsertOrUpdateRegionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertOrUpdateRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.debug_enable):
            query['DebugEnable'] = request.debug_enable
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.mse_instance_id):
            query['MseInstanceId'] = request.mse_instance_id
        if not UtilClient.is_unset(request.region_name):
            query['RegionName'] = request.region_name
        if not UtilClient.is_unset(request.region_tag):
            query['RegionTag'] = request.region_tag
        if not UtilClient.is_unset(request.registry_type):
            query['RegistryType'] = request.registry_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertOrUpdateRegion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/user_region_def',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertOrUpdateRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_or_update_region_with_options_async(
        self,
        request: edas_20170801_models.InsertOrUpdateRegionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertOrUpdateRegionResponse:
        """
        @summary Creates or edits a custom namespace.
        
        @param request: InsertOrUpdateRegionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertOrUpdateRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.debug_enable):
            query['DebugEnable'] = request.debug_enable
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.mse_instance_id):
            query['MseInstanceId'] = request.mse_instance_id
        if not UtilClient.is_unset(request.region_name):
            query['RegionName'] = request.region_name
        if not UtilClient.is_unset(request.region_tag):
            query['RegionTag'] = request.region_tag
        if not UtilClient.is_unset(request.registry_type):
            query['RegistryType'] = request.registry_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertOrUpdateRegion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/user_region_def',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertOrUpdateRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_or_update_region(
        self,
        request: edas_20170801_models.InsertOrUpdateRegionRequest,
    ) -> edas_20170801_models.InsertOrUpdateRegionResponse:
        """
        @summary Creates or edits a custom namespace.
        
        @param request: InsertOrUpdateRegionRequest
        @return: InsertOrUpdateRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.insert_or_update_region_with_options(request, headers, runtime)

    async def insert_or_update_region_async(
        self,
        request: edas_20170801_models.InsertOrUpdateRegionRequest,
    ) -> edas_20170801_models.InsertOrUpdateRegionResponse:
        """
        @summary Creates or edits a custom namespace.
        
        @param request: InsertOrUpdateRegionRequest
        @return: InsertOrUpdateRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.insert_or_update_region_with_options_async(request, headers, runtime)

    def insert_role_with_options(
        self,
        request: edas_20170801_models.InsertRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertRoleResponse:
        """
        @summary Creates a role.
        
        @param request: InsertRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_data):
            query['ActionData'] = request.action_data
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertRole',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/create_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_role_with_options_async(
        self,
        request: edas_20170801_models.InsertRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertRoleResponse:
        """
        @summary Creates a role.
        
        @param request: InsertRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_data):
            query['ActionData'] = request.action_data
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertRole',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/create_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_role(
        self,
        request: edas_20170801_models.InsertRoleRequest,
    ) -> edas_20170801_models.InsertRoleResponse:
        """
        @summary Creates a role.
        
        @param request: InsertRoleRequest
        @return: InsertRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.insert_role_with_options(request, headers, runtime)

    async def insert_role_async(
        self,
        request: edas_20170801_models.InsertRoleRequest,
    ) -> edas_20170801_models.InsertRoleResponse:
        """
        @summary Creates a role.
        
        @param request: InsertRoleRequest
        @return: InsertRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.insert_role_with_options_async(request, headers, runtime)

    def insert_service_group_with_options(
        self,
        request: edas_20170801_models.InsertServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertServiceGroupResponse:
        """
        @summary Creates a service group.
        
        @param request: InsertServiceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertServiceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertServiceGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/service/serviceGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_service_group_with_options_async(
        self,
        request: edas_20170801_models.InsertServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertServiceGroupResponse:
        """
        @summary Creates a service group.
        
        @param request: InsertServiceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertServiceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertServiceGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/service/serviceGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_service_group(
        self,
        request: edas_20170801_models.InsertServiceGroupRequest,
    ) -> edas_20170801_models.InsertServiceGroupResponse:
        """
        @summary Creates a service group.
        
        @param request: InsertServiceGroupRequest
        @return: InsertServiceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.insert_service_group_with_options(request, headers, runtime)

    async def insert_service_group_async(
        self,
        request: edas_20170801_models.InsertServiceGroupRequest,
    ) -> edas_20170801_models.InsertServiceGroupResponse:
        """
        @summary Creates a service group.
        
        @param request: InsertServiceGroupRequest
        @return: InsertServiceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.insert_service_group_with_options_async(request, headers, runtime)

    def insert_swimming_lane_with_options(
        self,
        request: edas_20170801_models.InsertSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertSwimmingLaneResponse:
        """
        @summary Creates a lane.
        
        @param request: InsertSwimmingLaneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertSwimmingLaneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_infos):
            query['AppInfos'] = request.app_infos
        if not UtilClient.is_unset(request.enable_rules):
            query['EnableRules'] = request.enable_rules
        if not UtilClient.is_unset(request.entry_rules):
            query['EntryRules'] = request.entry_rules
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertSwimmingLane',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/trafficmgnt/swimming_lanes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertSwimmingLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_swimming_lane_with_options_async(
        self,
        request: edas_20170801_models.InsertSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertSwimmingLaneResponse:
        """
        @summary Creates a lane.
        
        @param request: InsertSwimmingLaneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertSwimmingLaneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_infos):
            query['AppInfos'] = request.app_infos
        if not UtilClient.is_unset(request.enable_rules):
            query['EnableRules'] = request.enable_rules
        if not UtilClient.is_unset(request.entry_rules):
            query['EntryRules'] = request.entry_rules
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertSwimmingLane',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/trafficmgnt/swimming_lanes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertSwimmingLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_swimming_lane(
        self,
        request: edas_20170801_models.InsertSwimmingLaneRequest,
    ) -> edas_20170801_models.InsertSwimmingLaneResponse:
        """
        @summary Creates a lane.
        
        @param request: InsertSwimmingLaneRequest
        @return: InsertSwimmingLaneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.insert_swimming_lane_with_options(request, headers, runtime)

    async def insert_swimming_lane_async(
        self,
        request: edas_20170801_models.InsertSwimmingLaneRequest,
    ) -> edas_20170801_models.InsertSwimmingLaneResponse:
        """
        @summary Creates a lane.
        
        @param request: InsertSwimmingLaneRequest
        @return: InsertSwimmingLaneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.insert_swimming_lane_with_options_async(request, headers, runtime)

    def insert_swimming_lane_group_with_options(
        self,
        request: edas_20170801_models.InsertSwimmingLaneGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertSwimmingLaneGroupResponse:
        """
        @summary Creates a lane group.
        
        @param request: InsertSwimmingLaneGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertSwimmingLaneGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.entry_app):
            query['EntryApp'] = request.entry_app
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertSwimmingLaneGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/trafficmgnt/swimming_lane_groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertSwimmingLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_swimming_lane_group_with_options_async(
        self,
        request: edas_20170801_models.InsertSwimmingLaneGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InsertSwimmingLaneGroupResponse:
        """
        @summary Creates a lane group.
        
        @param request: InsertSwimmingLaneGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertSwimmingLaneGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.entry_app):
            query['EntryApp'] = request.entry_app
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertSwimmingLaneGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/trafficmgnt/swimming_lane_groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InsertSwimmingLaneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_swimming_lane_group(
        self,
        request: edas_20170801_models.InsertSwimmingLaneGroupRequest,
    ) -> edas_20170801_models.InsertSwimmingLaneGroupResponse:
        """
        @summary Creates a lane group.
        
        @param request: InsertSwimmingLaneGroupRequest
        @return: InsertSwimmingLaneGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.insert_swimming_lane_group_with_options(request, headers, runtime)

    async def insert_swimming_lane_group_async(
        self,
        request: edas_20170801_models.InsertSwimmingLaneGroupRequest,
    ) -> edas_20170801_models.InsertSwimmingLaneGroupResponse:
        """
        @summary Creates a lane group.
        
        @param request: InsertSwimmingLaneGroupRequest
        @return: InsertSwimmingLaneGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.insert_swimming_lane_group_with_options_async(request, headers, runtime)

    def install_agent_with_options(
        self,
        request: edas_20170801_models.InstallAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InstallAgentResponse:
        """
        @summary Uses the Cloud Assistant provided by Elastic Compute Service (ECS) to install Enterprise Distributed Application Service (EDAS) Agent and imports ECS instances to EDAS.
        
        @description If you call this operation to import an ECS instance into EDAS, the operating system of the ECS instance is not reinstalled. We recommend that you call this operation to import ECS instances into EDAS.
        
        @param request: InstallAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.do_async):
            query['DoAsync'] = request.do_async
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallAgent',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/ecss/install_agent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InstallAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_agent_with_options_async(
        self,
        request: edas_20170801_models.InstallAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.InstallAgentResponse:
        """
        @summary Uses the Cloud Assistant provided by Elastic Compute Service (ECS) to install Enterprise Distributed Application Service (EDAS) Agent and imports ECS instances to EDAS.
        
        @description If you call this operation to import an ECS instance into EDAS, the operating system of the ECS instance is not reinstalled. We recommend that you call this operation to import ECS instances into EDAS.
        
        @param request: InstallAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.do_async):
            query['DoAsync'] = request.do_async
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallAgent',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/ecss/install_agent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.InstallAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_agent(
        self,
        request: edas_20170801_models.InstallAgentRequest,
    ) -> edas_20170801_models.InstallAgentResponse:
        """
        @summary Uses the Cloud Assistant provided by Elastic Compute Service (ECS) to install Enterprise Distributed Application Service (EDAS) Agent and imports ECS instances to EDAS.
        
        @description If you call this operation to import an ECS instance into EDAS, the operating system of the ECS instance is not reinstalled. We recommend that you call this operation to import ECS instances into EDAS.
        
        @param request: InstallAgentRequest
        @return: InstallAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_agent_with_options(request, headers, runtime)

    async def install_agent_async(
        self,
        request: edas_20170801_models.InstallAgentRequest,
    ) -> edas_20170801_models.InstallAgentResponse:
        """
        @summary Uses the Cloud Assistant provided by Elastic Compute Service (ECS) to install Enterprise Distributed Application Service (EDAS) Agent and imports ECS instances to EDAS.
        
        @description If you call this operation to import an ECS instance into EDAS, the operating system of the ECS instance is not reinstalled. We recommend that you call this operation to import ECS instances into EDAS.
        
        @param request: InstallAgentRequest
        @return: InstallAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.install_agent_with_options_async(request, headers, runtime)

    def list_aliyun_region_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListAliyunRegionResponse:
        """
        @summary Queries Alibaba Cloud regions supported by Enterprise Distributed Application Service (EDAS).
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAliyunRegionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListAliyunRegion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/region_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListAliyunRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aliyun_region_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListAliyunRegionResponse:
        """
        @summary Queries Alibaba Cloud regions supported by Enterprise Distributed Application Service (EDAS).
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAliyunRegionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListAliyunRegion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/region_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListAliyunRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aliyun_region(self) -> edas_20170801_models.ListAliyunRegionResponse:
        """
        @summary Queries Alibaba Cloud regions supported by Enterprise Distributed Application Service (EDAS).
        
        @return: ListAliyunRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_aliyun_region_with_options(headers, runtime)

    async def list_aliyun_region_async(self) -> edas_20170801_models.ListAliyunRegionResponse:
        """
        @summary Queries Alibaba Cloud regions supported by Enterprise Distributed Application Service (EDAS).
        
        @return: ListAliyunRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_aliyun_region_with_options_async(headers, runtime)

    def list_application_with_options(
        self,
        request: edas_20170801_models.ListApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListApplicationResponse:
        """
        @summary Queries a list of applications.
        
        @param request: ListApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not UtilClient.is_unset(request.logical_region_id_filter):
            query['LogicalRegionIdFilter'] = request.logical_region_id_filter
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/app_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_with_options_async(
        self,
        request: edas_20170801_models.ListApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListApplicationResponse:
        """
        @summary Queries a list of applications.
        
        @param request: ListApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not UtilClient.is_unset(request.logical_region_id_filter):
            query['LogicalRegionIdFilter'] = request.logical_region_id_filter
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/app_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application(
        self,
        request: edas_20170801_models.ListApplicationRequest,
    ) -> edas_20170801_models.ListApplicationResponse:
        """
        @summary Queries a list of applications.
        
        @param request: ListApplicationRequest
        @return: ListApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_application_with_options(request, headers, runtime)

    async def list_application_async(
        self,
        request: edas_20170801_models.ListApplicationRequest,
    ) -> edas_20170801_models.ListApplicationResponse:
        """
        @summary Queries a list of applications.
        
        @param request: ListApplicationRequest
        @return: ListApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_application_with_options_async(request, headers, runtime)

    def list_application_ecu_with_options(
        self,
        request: edas_20170801_models.ListApplicationEcuRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListApplicationEcuResponse:
        """
        @summary Queries elastic compute units (ECUs).
        
        @param request: ListApplicationEcuRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationEcuResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationEcu',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/ecu_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListApplicationEcuResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_ecu_with_options_async(
        self,
        request: edas_20170801_models.ListApplicationEcuRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListApplicationEcuResponse:
        """
        @summary Queries elastic compute units (ECUs).
        
        @param request: ListApplicationEcuRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationEcuResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationEcu',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/ecu_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListApplicationEcuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_ecu(
        self,
        request: edas_20170801_models.ListApplicationEcuRequest,
    ) -> edas_20170801_models.ListApplicationEcuResponse:
        """
        @summary Queries elastic compute units (ECUs).
        
        @param request: ListApplicationEcuRequest
        @return: ListApplicationEcuResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_application_ecu_with_options(request, headers, runtime)

    async def list_application_ecu_async(
        self,
        request: edas_20170801_models.ListApplicationEcuRequest,
    ) -> edas_20170801_models.ListApplicationEcuResponse:
        """
        @summary Queries elastic compute units (ECUs).
        
        @param request: ListApplicationEcuRequest
        @return: ListApplicationEcuResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_application_ecu_with_options_async(request, headers, runtime)

    def list_authority_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListAuthorityResponse:
        """
        @summary Queries all permissions.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAuthorityResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListAuthority',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/authority_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_authority_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListAuthorityResponse:
        """
        @summary Queries all permissions.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAuthorityResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListAuthority',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/authority_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_authority(self) -> edas_20170801_models.ListAuthorityResponse:
        """
        @summary Queries all permissions.
        
        @return: ListAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_authority_with_options(headers, runtime)

    async def list_authority_async(self) -> edas_20170801_models.ListAuthorityResponse:
        """
        @summary Queries all permissions.
        
        @return: ListAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_authority_with_options_async(headers, runtime)

    def list_build_pack_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListBuildPackResponse:
        """
        @summary Queries Enterprise Distributed Application Service (EDAS) Container versions.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBuildPackResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListBuildPack',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/build_pack_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListBuildPackResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_build_pack_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListBuildPackResponse:
        """
        @summary Queries Enterprise Distributed Application Service (EDAS) Container versions.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBuildPackResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListBuildPack',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/build_pack_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListBuildPackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_build_pack(self) -> edas_20170801_models.ListBuildPackResponse:
        """
        @summary Queries Enterprise Distributed Application Service (EDAS) Container versions.
        
        @return: ListBuildPackResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_build_pack_with_options(headers, runtime)

    async def list_build_pack_async(self) -> edas_20170801_models.ListBuildPackResponse:
        """
        @summary Queries Enterprise Distributed Application Service (EDAS) Container versions.
        
        @return: ListBuildPackResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_build_pack_with_options_async(headers, runtime)

    def list_cluster_with_options(
        self,
        request: edas_20170801_models.ListClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListClusterResponse:
        """
        @summary Queries clusters.
        
        @param request: ListClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/cluster_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_with_options_async(
        self,
        request: edas_20170801_models.ListClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListClusterResponse:
        """
        @summary Queries clusters.
        
        @param request: ListClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/cluster_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster(
        self,
        request: edas_20170801_models.ListClusterRequest,
    ) -> edas_20170801_models.ListClusterResponse:
        """
        @summary Queries clusters.
        
        @param request: ListClusterRequest
        @return: ListClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_cluster_with_options(request, headers, runtime)

    async def list_cluster_async(
        self,
        request: edas_20170801_models.ListClusterRequest,
    ) -> edas_20170801_models.ListClusterResponse:
        """
        @summary Queries clusters.
        
        @param request: ListClusterRequest
        @return: ListClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_cluster_with_options_async(request, headers, runtime)

    def list_cluster_members_with_options(
        self,
        request: edas_20170801_models.ListClusterMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListClusterMembersResponse:
        """
        @summary Queries Elastic Compute Service (ECS) instances in a cluster.
        
        @param request: ListClusterMembersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ecs_list):
            query['EcsList'] = request.ecs_list
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterMembers',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/cluster_member_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListClusterMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_members_with_options_async(
        self,
        request: edas_20170801_models.ListClusterMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListClusterMembersResponse:
        """
        @summary Queries Elastic Compute Service (ECS) instances in a cluster.
        
        @param request: ListClusterMembersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ecs_list):
            query['EcsList'] = request.ecs_list
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterMembers',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/cluster_member_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListClusterMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_members(
        self,
        request: edas_20170801_models.ListClusterMembersRequest,
    ) -> edas_20170801_models.ListClusterMembersResponse:
        """
        @summary Queries Elastic Compute Service (ECS) instances in a cluster.
        
        @param request: ListClusterMembersRequest
        @return: ListClusterMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_cluster_members_with_options(request, headers, runtime)

    async def list_cluster_members_async(
        self,
        request: edas_20170801_models.ListClusterMembersRequest,
    ) -> edas_20170801_models.ListClusterMembersResponse:
        """
        @summary Queries Elastic Compute Service (ECS) instances in a cluster.
        
        @param request: ListClusterMembersRequest
        @return: ListClusterMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_cluster_members_with_options_async(request, headers, runtime)

    def list_components_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListComponentsResponse:
        """
        @summary Queries the components that are related to applications in Elastic Compute Service (ECS) clusters.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComponentsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListComponents',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/components',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_components_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListComponentsResponse:
        """
        @summary Queries the components that are related to applications in Elastic Compute Service (ECS) clusters.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComponentsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListComponents',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/components',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_components(self) -> edas_20170801_models.ListComponentsResponse:
        """
        @summary Queries the components that are related to applications in Elastic Compute Service (ECS) clusters.
        
        @return: ListComponentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_components_with_options(headers, runtime)

    async def list_components_async(self) -> edas_20170801_models.ListComponentsResponse:
        """
        @summary Queries the components that are related to applications in Elastic Compute Service (ECS) clusters.
        
        @return: ListComponentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_components_with_options_async(headers, runtime)

    def list_config_templates_with_options(
        self,
        request: edas_20170801_models.ListConfigTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListConfigTemplatesResponse:
        """
        @summary Queries configuration templates.
        
        @param request: ListConfigTemplatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigTemplates',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/config_template',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListConfigTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_templates_with_options_async(
        self,
        request: edas_20170801_models.ListConfigTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListConfigTemplatesResponse:
        """
        @summary Queries configuration templates.
        
        @param request: ListConfigTemplatesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConfigTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigTemplates',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/config_template',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListConfigTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_templates(
        self,
        request: edas_20170801_models.ListConfigTemplatesRequest,
    ) -> edas_20170801_models.ListConfigTemplatesResponse:
        """
        @summary Queries configuration templates.
        
        @param request: ListConfigTemplatesRequest
        @return: ListConfigTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_config_templates_with_options(request, headers, runtime)

    async def list_config_templates_async(
        self,
        request: edas_20170801_models.ListConfigTemplatesRequest,
    ) -> edas_20170801_models.ListConfigTemplatesResponse:
        """
        @summary Queries configuration templates.
        
        @param request: ListConfigTemplatesRequest
        @return: ListConfigTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_config_templates_with_options_async(request, headers, runtime)

    def list_consumed_services_with_options(
        self,
        request: edas_20170801_models.ListConsumedServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListConsumedServicesResponse:
        """
        @summary Queries the services that are consumed by an application.
        
        @param request: ListConsumedServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConsumedServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConsumedServices',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/service/listConsumedServices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListConsumedServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumed_services_with_options_async(
        self,
        request: edas_20170801_models.ListConsumedServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListConsumedServicesResponse:
        """
        @summary Queries the services that are consumed by an application.
        
        @param request: ListConsumedServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConsumedServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConsumedServices',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/service/listConsumedServices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListConsumedServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumed_services(
        self,
        request: edas_20170801_models.ListConsumedServicesRequest,
    ) -> edas_20170801_models.ListConsumedServicesResponse:
        """
        @summary Queries the services that are consumed by an application.
        
        @param request: ListConsumedServicesRequest
        @return: ListConsumedServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_consumed_services_with_options(request, headers, runtime)

    async def list_consumed_services_async(
        self,
        request: edas_20170801_models.ListConsumedServicesRequest,
    ) -> edas_20170801_models.ListConsumedServicesResponse:
        """
        @summary Queries the services that are consumed by an application.
        
        @param request: ListConsumedServicesRequest
        @return: ListConsumedServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_consumed_services_with_options_async(request, headers, runtime)

    def list_convertable_ecu_with_options(
        self,
        request: edas_20170801_models.ListConvertableEcuRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListConvertableEcuResponse:
        """
        @summary Queries the Elastic Compute Service (ECS) instances that can be imported to a specified cluster. This operation is applicable to ECS clusters.
        
        @param request: ListConvertableEcuRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConvertableEcuResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['clusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConvertableEcu',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/convertable_ecu_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListConvertableEcuResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_convertable_ecu_with_options_async(
        self,
        request: edas_20170801_models.ListConvertableEcuRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListConvertableEcuResponse:
        """
        @summary Queries the Elastic Compute Service (ECS) instances that can be imported to a specified cluster. This operation is applicable to ECS clusters.
        
        @param request: ListConvertableEcuRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConvertableEcuResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['clusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConvertableEcu',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/convertable_ecu_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListConvertableEcuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_convertable_ecu(
        self,
        request: edas_20170801_models.ListConvertableEcuRequest,
    ) -> edas_20170801_models.ListConvertableEcuResponse:
        """
        @summary Queries the Elastic Compute Service (ECS) instances that can be imported to a specified cluster. This operation is applicable to ECS clusters.
        
        @param request: ListConvertableEcuRequest
        @return: ListConvertableEcuResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_convertable_ecu_with_options(request, headers, runtime)

    async def list_convertable_ecu_async(
        self,
        request: edas_20170801_models.ListConvertableEcuRequest,
    ) -> edas_20170801_models.ListConvertableEcuResponse:
        """
        @summary Queries the Elastic Compute Service (ECS) instances that can be imported to a specified cluster. This operation is applicable to ECS clusters.
        
        @param request: ListConvertableEcuRequest
        @return: ListConvertableEcuResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_convertable_ecu_with_options_async(request, headers, runtime)

    def list_deploy_group_with_options(
        self,
        request: edas_20170801_models.ListDeployGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListDeployGroupResponse:
        """
        @summary Queries the instance groups to which an application is deployed.
        
        @param request: ListDeployGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeployGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeployGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/deploy_group_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListDeployGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deploy_group_with_options_async(
        self,
        request: edas_20170801_models.ListDeployGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListDeployGroupResponse:
        """
        @summary Queries the instance groups to which an application is deployed.
        
        @param request: ListDeployGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeployGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeployGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/deploy_group_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListDeployGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deploy_group(
        self,
        request: edas_20170801_models.ListDeployGroupRequest,
    ) -> edas_20170801_models.ListDeployGroupResponse:
        """
        @summary Queries the instance groups to which an application is deployed.
        
        @param request: ListDeployGroupRequest
        @return: ListDeployGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_deploy_group_with_options(request, headers, runtime)

    async def list_deploy_group_async(
        self,
        request: edas_20170801_models.ListDeployGroupRequest,
    ) -> edas_20170801_models.ListDeployGroupResponse:
        """
        @summary Queries the instance groups to which an application is deployed.
        
        @param request: ListDeployGroupRequest
        @return: ListDeployGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_deploy_group_with_options_async(request, headers, runtime)

    def list_ecs_not_in_cluster_with_options(
        self,
        request: edas_20170801_models.ListEcsNotInClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListEcsNotInClusterResponse:
        """
        @summary Queries all Elastic Compute Service (ECS) instances that have not been imported to clusters.
        
        @param request: ListEcsNotInClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEcsNotInClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_mode):
            query['NetworkMode'] = request.network_mode
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEcsNotInCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/ecs_not_in_cluster',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListEcsNotInClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ecs_not_in_cluster_with_options_async(
        self,
        request: edas_20170801_models.ListEcsNotInClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListEcsNotInClusterResponse:
        """
        @summary Queries all Elastic Compute Service (ECS) instances that have not been imported to clusters.
        
        @param request: ListEcsNotInClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEcsNotInClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_mode):
            query['NetworkMode'] = request.network_mode
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEcsNotInCluster',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/ecs_not_in_cluster',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListEcsNotInClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ecs_not_in_cluster(
        self,
        request: edas_20170801_models.ListEcsNotInClusterRequest,
    ) -> edas_20170801_models.ListEcsNotInClusterResponse:
        """
        @summary Queries all Elastic Compute Service (ECS) instances that have not been imported to clusters.
        
        @param request: ListEcsNotInClusterRequest
        @return: ListEcsNotInClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ecs_not_in_cluster_with_options(request, headers, runtime)

    async def list_ecs_not_in_cluster_async(
        self,
        request: edas_20170801_models.ListEcsNotInClusterRequest,
    ) -> edas_20170801_models.ListEcsNotInClusterResponse:
        """
        @summary Queries all Elastic Compute Service (ECS) instances that have not been imported to clusters.
        
        @param request: ListEcsNotInClusterRequest
        @return: ListEcsNotInClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ecs_not_in_cluster_with_options_async(request, headers, runtime)

    def list_ecu_by_region_with_options(
        self,
        request: edas_20170801_models.ListEcuByRegionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListEcuByRegionResponse:
        """
        @summary Queries the available elastic compute units (ECUs) in a specified namespace.
        
        @description ## Terms
        **Namespace**: the logical concept that is used to isolate resources such as clusters, ECS instances, and applications, and microservices published in EDAS. This concept involves the default namespace and custom namespaces. Each region has a default namespace and supports multiple custom namespaces. By default, only the default namespace is available. You do not need to create a custom namespace if you do not want to isolate resources and microservices.
        **Elastic compute unit (ECU)**: After an ECS instance is imported to a cluster, the instance becomes an ECU.
        **Elastic compute container (ECC)**: After you deploy an application to an ECU in a cluster, the ECU becomes an ECC.
        
        @param request: ListEcuByRegionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEcuByRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.act):
            query['Act'] = request.act
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEcuByRegion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/ecu_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListEcuByRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ecu_by_region_with_options_async(
        self,
        request: edas_20170801_models.ListEcuByRegionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListEcuByRegionResponse:
        """
        @summary Queries the available elastic compute units (ECUs) in a specified namespace.
        
        @description ## Terms
        **Namespace**: the logical concept that is used to isolate resources such as clusters, ECS instances, and applications, and microservices published in EDAS. This concept involves the default namespace and custom namespaces. Each region has a default namespace and supports multiple custom namespaces. By default, only the default namespace is available. You do not need to create a custom namespace if you do not want to isolate resources and microservices.
        **Elastic compute unit (ECU)**: After an ECS instance is imported to a cluster, the instance becomes an ECU.
        **Elastic compute container (ECC)**: After you deploy an application to an ECU in a cluster, the ECU becomes an ECC.
        
        @param request: ListEcuByRegionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEcuByRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.act):
            query['Act'] = request.act
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEcuByRegion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/ecu_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListEcuByRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ecu_by_region(
        self,
        request: edas_20170801_models.ListEcuByRegionRequest,
    ) -> edas_20170801_models.ListEcuByRegionResponse:
        """
        @summary Queries the available elastic compute units (ECUs) in a specified namespace.
        
        @description ## Terms
        **Namespace**: the logical concept that is used to isolate resources such as clusters, ECS instances, and applications, and microservices published in EDAS. This concept involves the default namespace and custom namespaces. Each region has a default namespace and supports multiple custom namespaces. By default, only the default namespace is available. You do not need to create a custom namespace if you do not want to isolate resources and microservices.
        **Elastic compute unit (ECU)**: After an ECS instance is imported to a cluster, the instance becomes an ECU.
        **Elastic compute container (ECC)**: After you deploy an application to an ECU in a cluster, the ECU becomes an ECC.
        
        @param request: ListEcuByRegionRequest
        @return: ListEcuByRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_ecu_by_region_with_options(request, headers, runtime)

    async def list_ecu_by_region_async(
        self,
        request: edas_20170801_models.ListEcuByRegionRequest,
    ) -> edas_20170801_models.ListEcuByRegionResponse:
        """
        @summary Queries the available elastic compute units (ECUs) in a specified namespace.
        
        @description ## Terms
        **Namespace**: the logical concept that is used to isolate resources such as clusters, ECS instances, and applications, and microservices published in EDAS. This concept involves the default namespace and custom namespaces. Each region has a default namespace and supports multiple custom namespaces. By default, only the default namespace is available. You do not need to create a custom namespace if you do not want to isolate resources and microservices.
        **Elastic compute unit (ECU)**: After an ECS instance is imported to a cluster, the instance becomes an ECU.
        **Elastic compute container (ECC)**: After you deploy an application to an ECU in a cluster, the ECU becomes an ECC.
        
        @param request: ListEcuByRegionRequest
        @return: ListEcuByRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_ecu_by_region_with_options_async(request, headers, runtime)

    def list_history_deploy_version_with_options(
        self,
        request: edas_20170801_models.ListHistoryDeployVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListHistoryDeployVersionResponse:
        """
        @summary Queries historical deployment packages of an application.
        
        @param request: ListHistoryDeployVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHistoryDeployVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHistoryDeployVersion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/deploy_history_version_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListHistoryDeployVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_history_deploy_version_with_options_async(
        self,
        request: edas_20170801_models.ListHistoryDeployVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListHistoryDeployVersionResponse:
        """
        @summary Queries historical deployment packages of an application.
        
        @param request: ListHistoryDeployVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListHistoryDeployVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHistoryDeployVersion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/deploy_history_version_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListHistoryDeployVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_history_deploy_version(
        self,
        request: edas_20170801_models.ListHistoryDeployVersionRequest,
    ) -> edas_20170801_models.ListHistoryDeployVersionResponse:
        """
        @summary Queries historical deployment packages of an application.
        
        @param request: ListHistoryDeployVersionRequest
        @return: ListHistoryDeployVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_history_deploy_version_with_options(request, headers, runtime)

    async def list_history_deploy_version_async(
        self,
        request: edas_20170801_models.ListHistoryDeployVersionRequest,
    ) -> edas_20170801_models.ListHistoryDeployVersionResponse:
        """
        @summary Queries historical deployment packages of an application.
        
        @param request: ListHistoryDeployVersionRequest
        @return: ListHistoryDeployVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_history_deploy_version_with_options_async(request, headers, runtime)

    def list_k8s_config_maps_with_options(
        self,
        request: edas_20170801_models.ListK8sConfigMapsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListK8sConfigMapsResponse:
        """
        @summary Queries Kubernetes ConfigMaps.
        
        @param request: ListK8sConfigMapsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListK8sConfigMapsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.condition):
            query['Condition'] = request.condition
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.show_related_apps):
            query['ShowRelatedApps'] = request.show_related_apps
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListK8sConfigMaps',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_config_map',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListK8sConfigMapsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_k8s_config_maps_with_options_async(
        self,
        request: edas_20170801_models.ListK8sConfigMapsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListK8sConfigMapsResponse:
        """
        @summary Queries Kubernetes ConfigMaps.
        
        @param request: ListK8sConfigMapsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListK8sConfigMapsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.condition):
            query['Condition'] = request.condition
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.show_related_apps):
            query['ShowRelatedApps'] = request.show_related_apps
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListK8sConfigMaps',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_config_map',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListK8sConfigMapsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_k8s_config_maps(
        self,
        request: edas_20170801_models.ListK8sConfigMapsRequest,
    ) -> edas_20170801_models.ListK8sConfigMapsResponse:
        """
        @summary Queries Kubernetes ConfigMaps.
        
        @param request: ListK8sConfigMapsRequest
        @return: ListK8sConfigMapsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_k8s_config_maps_with_options(request, headers, runtime)

    async def list_k8s_config_maps_async(
        self,
        request: edas_20170801_models.ListK8sConfigMapsRequest,
    ) -> edas_20170801_models.ListK8sConfigMapsResponse:
        """
        @summary Queries Kubernetes ConfigMaps.
        
        @param request: ListK8sConfigMapsRequest
        @return: ListK8sConfigMapsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_k8s_config_maps_with_options_async(request, headers, runtime)

    def list_k8s_ingress_rules_with_options(
        self,
        request: edas_20170801_models.ListK8sIngressRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListK8sIngressRulesResponse:
        """
        @summary Queries ingresses.
        
        @param request: ListK8sIngressRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListK8sIngressRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.condition):
            query['Condition'] = request.condition
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListK8sIngressRules',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_ingress',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListK8sIngressRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_k8s_ingress_rules_with_options_async(
        self,
        request: edas_20170801_models.ListK8sIngressRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListK8sIngressRulesResponse:
        """
        @summary Queries ingresses.
        
        @param request: ListK8sIngressRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListK8sIngressRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.condition):
            query['Condition'] = request.condition
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListK8sIngressRules',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_ingress',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListK8sIngressRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_k8s_ingress_rules(
        self,
        request: edas_20170801_models.ListK8sIngressRulesRequest,
    ) -> edas_20170801_models.ListK8sIngressRulesResponse:
        """
        @summary Queries ingresses.
        
        @param request: ListK8sIngressRulesRequest
        @return: ListK8sIngressRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_k8s_ingress_rules_with_options(request, headers, runtime)

    async def list_k8s_ingress_rules_async(
        self,
        request: edas_20170801_models.ListK8sIngressRulesRequest,
    ) -> edas_20170801_models.ListK8sIngressRulesResponse:
        """
        @summary Queries ingresses.
        
        @param request: ListK8sIngressRulesRequest
        @return: ListK8sIngressRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_k8s_ingress_rules_with_options_async(request, headers, runtime)

    def list_k8s_namespaces_with_options(
        self,
        request: edas_20170801_models.ListK8sNamespacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListK8sNamespacesResponse:
        """
        @summary Queries namespaces for a Kubernetes cluster.
        
        @param request: ListK8sNamespacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListK8sNamespacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListK8sNamespaces',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_namespace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListK8sNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_k8s_namespaces_with_options_async(
        self,
        request: edas_20170801_models.ListK8sNamespacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListK8sNamespacesResponse:
        """
        @summary Queries namespaces for a Kubernetes cluster.
        
        @param request: ListK8sNamespacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListK8sNamespacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListK8sNamespaces',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_namespace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListK8sNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_k8s_namespaces(
        self,
        request: edas_20170801_models.ListK8sNamespacesRequest,
    ) -> edas_20170801_models.ListK8sNamespacesResponse:
        """
        @summary Queries namespaces for a Kubernetes cluster.
        
        @param request: ListK8sNamespacesRequest
        @return: ListK8sNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_k8s_namespaces_with_options(request, headers, runtime)

    async def list_k8s_namespaces_async(
        self,
        request: edas_20170801_models.ListK8sNamespacesRequest,
    ) -> edas_20170801_models.ListK8sNamespacesResponse:
        """
        @summary Queries namespaces for a Kubernetes cluster.
        
        @param request: ListK8sNamespacesRequest
        @return: ListK8sNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_k8s_namespaces_with_options_async(request, headers, runtime)

    def list_k8s_secrets_with_options(
        self,
        request: edas_20170801_models.ListK8sSecretsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListK8sSecretsResponse:
        """
        @summary Queries Kubernetes Secrets.
        
        @param request: ListK8sSecretsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListK8sSecretsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.condition):
            query['Condition'] = request.condition
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.show_related_apps):
            query['ShowRelatedApps'] = request.show_related_apps
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListK8sSecrets',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_secret',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListK8sSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_k8s_secrets_with_options_async(
        self,
        request: edas_20170801_models.ListK8sSecretsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListK8sSecretsResponse:
        """
        @summary Queries Kubernetes Secrets.
        
        @param request: ListK8sSecretsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListK8sSecretsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.condition):
            query['Condition'] = request.condition
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.show_related_apps):
            query['ShowRelatedApps'] = request.show_related_apps
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListK8sSecrets',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_secret',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListK8sSecretsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_k8s_secrets(
        self,
        request: edas_20170801_models.ListK8sSecretsRequest,
    ) -> edas_20170801_models.ListK8sSecretsResponse:
        """
        @summary Queries Kubernetes Secrets.
        
        @param request: ListK8sSecretsRequest
        @return: ListK8sSecretsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_k8s_secrets_with_options(request, headers, runtime)

    async def list_k8s_secrets_async(
        self,
        request: edas_20170801_models.ListK8sSecretsRequest,
    ) -> edas_20170801_models.ListK8sSecretsResponse:
        """
        @summary Queries Kubernetes Secrets.
        
        @param request: ListK8sSecretsRequest
        @return: ListK8sSecretsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_k8s_secrets_with_options_async(request, headers, runtime)

    def list_methods_with_options(
        self,
        request: edas_20170801_models.ListMethodsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListMethodsResponse:
        """
        @summary Queries service methods.
        
        @param request: ListMethodsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMethodsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMethods',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/service/list_methods',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListMethodsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_methods_with_options_async(
        self,
        request: edas_20170801_models.ListMethodsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListMethodsResponse:
        """
        @summary Queries service methods.
        
        @param request: ListMethodsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMethodsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMethods',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/service/list_methods',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListMethodsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_methods(
        self,
        request: edas_20170801_models.ListMethodsRequest,
    ) -> edas_20170801_models.ListMethodsResponse:
        """
        @summary Queries service methods.
        
        @param request: ListMethodsRequest
        @return: ListMethodsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_methods_with_options(request, headers, runtime)

    async def list_methods_async(
        self,
        request: edas_20170801_models.ListMethodsRequest,
    ) -> edas_20170801_models.ListMethodsResponse:
        """
        @summary Queries service methods.
        
        @param request: ListMethodsRequest
        @return: ListMethodsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_methods_with_options_async(request, headers, runtime)

    def list_published_services_with_options(
        self,
        request: edas_20170801_models.ListPublishedServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListPublishedServicesResponse:
        """
        @summary Queries the services that are published by an application.
        
        @param request: ListPublishedServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublishedServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishedServices',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/service/listPublishedServices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListPublishedServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_published_services_with_options_async(
        self,
        request: edas_20170801_models.ListPublishedServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListPublishedServicesResponse:
        """
        @summary Queries the services that are published by an application.
        
        @param request: ListPublishedServicesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublishedServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishedServices',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/service/listPublishedServices',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListPublishedServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_published_services(
        self,
        request: edas_20170801_models.ListPublishedServicesRequest,
    ) -> edas_20170801_models.ListPublishedServicesResponse:
        """
        @summary Queries the services that are published by an application.
        
        @param request: ListPublishedServicesRequest
        @return: ListPublishedServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_published_services_with_options(request, headers, runtime)

    async def list_published_services_async(
        self,
        request: edas_20170801_models.ListPublishedServicesRequest,
    ) -> edas_20170801_models.ListPublishedServicesResponse:
        """
        @summary Queries the services that are published by an application.
        
        @param request: ListPublishedServicesRequest
        @return: ListPublishedServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_published_services_with_options_async(request, headers, runtime)

    def list_recent_change_order_with_options(
        self,
        request: edas_20170801_models.ListRecentChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListRecentChangeOrderResponse:
        """
        @summary Queries the change processes of an application.
        
        @param request: ListRecentChangeOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecentChangeOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecentChangeOrder',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/change_order_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListRecentChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recent_change_order_with_options_async(
        self,
        request: edas_20170801_models.ListRecentChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListRecentChangeOrderResponse:
        """
        @summary Queries the change processes of an application.
        
        @param request: ListRecentChangeOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecentChangeOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecentChangeOrder',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/change_order_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListRecentChangeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recent_change_order(
        self,
        request: edas_20170801_models.ListRecentChangeOrderRequest,
    ) -> edas_20170801_models.ListRecentChangeOrderResponse:
        """
        @summary Queries the change processes of an application.
        
        @param request: ListRecentChangeOrderRequest
        @return: ListRecentChangeOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_recent_change_order_with_options(request, headers, runtime)

    async def list_recent_change_order_async(
        self,
        request: edas_20170801_models.ListRecentChangeOrderRequest,
    ) -> edas_20170801_models.ListRecentChangeOrderResponse:
        """
        @summary Queries the change processes of an application.
        
        @param request: ListRecentChangeOrderRequest
        @return: ListRecentChangeOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_recent_change_order_with_options_async(request, headers, runtime)

    def list_resource_group_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListResourceGroupResponse:
        """
        @summary Queries resource groups.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListResourceGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/reg_group_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_group_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListResourceGroupResponse:
        """
        @summary Queries resource groups.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListResourceGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/reg_group_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_group(self) -> edas_20170801_models.ListResourceGroupResponse:
        """
        @summary Queries resource groups.
        
        @return: ListResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_group_with_options(headers, runtime)

    async def list_resource_group_async(self) -> edas_20170801_models.ListResourceGroupResponse:
        """
        @summary Queries resource groups.
        
        @return: ListResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_group_with_options_async(headers, runtime)

    def list_role_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListRoleResponse:
        """
        @summary Queries roles.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRole',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/role_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_role_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListRoleResponse:
        """
        @summary Queries roles.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRole',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/role_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_role(self) -> edas_20170801_models.ListRoleResponse:
        """
        @summary Queries roles.
        
        @return: ListRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_role_with_options(headers, runtime)

    async def list_role_async(self) -> edas_20170801_models.ListRoleResponse:
        """
        @summary Queries roles.
        
        @return: ListRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_role_with_options_async(headers, runtime)

    def list_scale_out_ecu_with_options(
        self,
        request: edas_20170801_models.ListScaleOutEcuRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListScaleOutEcuResponse:
        """
        @summary Queries elastic compute units (ECUs) available for scaling out an application in a specified cluster or the cluster where the application is deployed. This operation is applicable to Elastic Compute Service (ECS) clusters.
        
        @description ## Terms
        **Namespace**: the logical concept that is used to isolate resources such as clusters, ECS instances, and applications, and microservices published in EDAS. This concept involves the default namespace and custom namespaces. Each region has a default namespace and supports multiple custom namespaces. By default, only the default namespace is available. You do not need to create a custom namespace if you do not want to isolate resources and microservices.
        **Elastic compute unit (ECU)**: After an ECS instance is imported to a cluster, the instance becomes an ECU.
        **Elastic compute container (ECC)**: After you deploy an application to an ECU in a cluster, the ECU becomes an ECC.
        
        @param request: ListScaleOutEcuRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScaleOutEcuResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_num):
            query['InstanceNum'] = request.instance_num
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not UtilClient.is_unset(request.mem):
            query['Mem'] = request.mem
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScaleOutEcu',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/scale_out_ecu_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListScaleOutEcuResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scale_out_ecu_with_options_async(
        self,
        request: edas_20170801_models.ListScaleOutEcuRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListScaleOutEcuResponse:
        """
        @summary Queries elastic compute units (ECUs) available for scaling out an application in a specified cluster or the cluster where the application is deployed. This operation is applicable to Elastic Compute Service (ECS) clusters.
        
        @description ## Terms
        **Namespace**: the logical concept that is used to isolate resources such as clusters, ECS instances, and applications, and microservices published in EDAS. This concept involves the default namespace and custom namespaces. Each region has a default namespace and supports multiple custom namespaces. By default, only the default namespace is available. You do not need to create a custom namespace if you do not want to isolate resources and microservices.
        **Elastic compute unit (ECU)**: After an ECS instance is imported to a cluster, the instance becomes an ECU.
        **Elastic compute container (ECC)**: After you deploy an application to an ECU in a cluster, the ECU becomes an ECC.
        
        @param request: ListScaleOutEcuRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScaleOutEcuResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_num):
            query['InstanceNum'] = request.instance_num
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not UtilClient.is_unset(request.mem):
            query['Mem'] = request.mem
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScaleOutEcu',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/scale_out_ecu_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListScaleOutEcuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scale_out_ecu(
        self,
        request: edas_20170801_models.ListScaleOutEcuRequest,
    ) -> edas_20170801_models.ListScaleOutEcuResponse:
        """
        @summary Queries elastic compute units (ECUs) available for scaling out an application in a specified cluster or the cluster where the application is deployed. This operation is applicable to Elastic Compute Service (ECS) clusters.
        
        @description ## Terms
        **Namespace**: the logical concept that is used to isolate resources such as clusters, ECS instances, and applications, and microservices published in EDAS. This concept involves the default namespace and custom namespaces. Each region has a default namespace and supports multiple custom namespaces. By default, only the default namespace is available. You do not need to create a custom namespace if you do not want to isolate resources and microservices.
        **Elastic compute unit (ECU)**: After an ECS instance is imported to a cluster, the instance becomes an ECU.
        **Elastic compute container (ECC)**: After you deploy an application to an ECU in a cluster, the ECU becomes an ECC.
        
        @param request: ListScaleOutEcuRequest
        @return: ListScaleOutEcuResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_scale_out_ecu_with_options(request, headers, runtime)

    async def list_scale_out_ecu_async(
        self,
        request: edas_20170801_models.ListScaleOutEcuRequest,
    ) -> edas_20170801_models.ListScaleOutEcuResponse:
        """
        @summary Queries elastic compute units (ECUs) available for scaling out an application in a specified cluster or the cluster where the application is deployed. This operation is applicable to Elastic Compute Service (ECS) clusters.
        
        @description ## Terms
        **Namespace**: the logical concept that is used to isolate resources such as clusters, ECS instances, and applications, and microservices published in EDAS. This concept involves the default namespace and custom namespaces. Each region has a default namespace and supports multiple custom namespaces. By default, only the default namespace is available. You do not need to create a custom namespace if you do not want to isolate resources and microservices.
        **Elastic compute unit (ECU)**: After an ECS instance is imported to a cluster, the instance becomes an ECU.
        **Elastic compute container (ECC)**: After you deploy an application to an ECU in a cluster, the ECU becomes an ECC.
        
        @param request: ListScaleOutEcuRequest
        @return: ListScaleOutEcuResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_scale_out_ecu_with_options_async(request, headers, runtime)

    def list_service_groups_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListServiceGroupsResponse:
        """
        @summary Queries the service groups of a High-Speed Service Framework (HSF) application.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceGroupsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListServiceGroups',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/service/serviceGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListServiceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_groups_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListServiceGroupsResponse:
        """
        @summary Queries the service groups of a High-Speed Service Framework (HSF) application.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceGroupsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListServiceGroups',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/service/serviceGroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListServiceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_groups(self) -> edas_20170801_models.ListServiceGroupsResponse:
        """
        @summary Queries the service groups of a High-Speed Service Framework (HSF) application.
        
        @return: ListServiceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_groups_with_options(headers, runtime)

    async def list_service_groups_async(self) -> edas_20170801_models.ListServiceGroupsResponse:
        """
        @summary Queries the service groups of a High-Speed Service Framework (HSF) application.
        
        @return: ListServiceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_service_groups_with_options_async(headers, runtime)

    def list_slb_with_options(
        self,
        request: edas_20170801_models.ListSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListSlbResponse:
        """
        @summary Queries Server Load Balancer (SLB) instances.
        
        @param request: ListSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.slb_type):
            query['SlbType'] = request.slb_type
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSlb',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/slb_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_slb_with_options_async(
        self,
        request: edas_20170801_models.ListSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListSlbResponse:
        """
        @summary Queries Server Load Balancer (SLB) instances.
        
        @param request: ListSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.slb_type):
            query['SlbType'] = request.slb_type
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSlb',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/slb_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_slb(
        self,
        request: edas_20170801_models.ListSlbRequest,
    ) -> edas_20170801_models.ListSlbResponse:
        """
        @summary Queries Server Load Balancer (SLB) instances.
        
        @param request: ListSlbRequest
        @return: ListSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_slb_with_options(request, headers, runtime)

    async def list_slb_async(
        self,
        request: edas_20170801_models.ListSlbRequest,
    ) -> edas_20170801_models.ListSlbResponse:
        """
        @summary Queries Server Load Balancer (SLB) instances.
        
        @param request: ListSlbRequest
        @return: ListSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_slb_with_options_async(request, headers, runtime)

    def list_sub_account_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListSubAccountResponse:
        """
        @summary Queries the Resource Access Management (RAM) users.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSubAccountResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSubAccount',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/sub_account_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListSubAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sub_account_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListSubAccountResponse:
        """
        @summary Queries the Resource Access Management (RAM) users.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSubAccountResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListSubAccount',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/sub_account_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListSubAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sub_account(self) -> edas_20170801_models.ListSubAccountResponse:
        """
        @summary Queries the Resource Access Management (RAM) users.
        
        @return: ListSubAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sub_account_with_options(headers, runtime)

    async def list_sub_account_async(self) -> edas_20170801_models.ListSubAccountResponse:
        """
        @summary Queries the Resource Access Management (RAM) users.
        
        @return: ListSubAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_sub_account_with_options_async(headers, runtime)

    def list_swimming_lane_with_options(
        self,
        request: edas_20170801_models.ListSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListSwimmingLaneResponse:
        """
        @summary Queries lanes in a lane group.
        
        @param request: ListSwimmingLaneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSwimmingLaneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSwimmingLane',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/trafficmgnt/swimming_lanes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListSwimmingLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_swimming_lane_with_options_async(
        self,
        request: edas_20170801_models.ListSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListSwimmingLaneResponse:
        """
        @summary Queries lanes in a lane group.
        
        @param request: ListSwimmingLaneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSwimmingLaneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSwimmingLane',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/trafficmgnt/swimming_lanes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListSwimmingLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_swimming_lane(
        self,
        request: edas_20170801_models.ListSwimmingLaneRequest,
    ) -> edas_20170801_models.ListSwimmingLaneResponse:
        """
        @summary Queries lanes in a lane group.
        
        @param request: ListSwimmingLaneRequest
        @return: ListSwimmingLaneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_swimming_lane_with_options(request, headers, runtime)

    async def list_swimming_lane_async(
        self,
        request: edas_20170801_models.ListSwimmingLaneRequest,
    ) -> edas_20170801_models.ListSwimmingLaneResponse:
        """
        @summary Queries lanes in a lane group.
        
        @param request: ListSwimmingLaneRequest
        @return: ListSwimmingLaneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_swimming_lane_with_options_async(request, headers, runtime)

    def list_swimming_lane_group_with_options(
        self,
        request: edas_20170801_models.ListSwimmingLaneGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListSwimmingLaneGroupResponse:
        """
        @summary Queries lane groups.
        
        @param request: ListSwimmingLaneGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSwimmingLaneGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSwimmingLaneGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/trafficmgnt/swimming_lane_groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListSwimmingLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_swimming_lane_group_with_options_async(
        self,
        request: edas_20170801_models.ListSwimmingLaneGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListSwimmingLaneGroupResponse:
        """
        @summary Queries lane groups.
        
        @param request: ListSwimmingLaneGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSwimmingLaneGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSwimmingLaneGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/trafficmgnt/swimming_lane_groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListSwimmingLaneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_swimming_lane_group(
        self,
        request: edas_20170801_models.ListSwimmingLaneGroupRequest,
    ) -> edas_20170801_models.ListSwimmingLaneGroupResponse:
        """
        @summary Queries lane groups.
        
        @param request: ListSwimmingLaneGroupRequest
        @return: ListSwimmingLaneGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_swimming_lane_group_with_options(request, headers, runtime)

    async def list_swimming_lane_group_async(
        self,
        request: edas_20170801_models.ListSwimmingLaneGroupRequest,
    ) -> edas_20170801_models.ListSwimmingLaneGroupResponse:
        """
        @summary Queries lane groups.
        
        @param request: ListSwimmingLaneGroupRequest
        @return: ListSwimmingLaneGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_swimming_lane_group_with_options_async(request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        request: edas_20170801_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to resources.
        
        @param request: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/tag/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: edas_20170801_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to resources.
        
        @param request: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/tag/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: edas_20170801_models.ListTagResourcesRequest,
    ) -> edas_20170801_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: edas_20170801_models.ListTagResourcesRequest,
    ) -> edas_20170801_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are added to resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def list_user_define_region_with_options(
        self,
        request: edas_20170801_models.ListUserDefineRegionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListUserDefineRegionResponse:
        """
        @summary Queries custom namespaces.
        
        @param request: ListUserDefineRegionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserDefineRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.debug_enable):
            query['DebugEnable'] = request.debug_enable
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserDefineRegion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/user_region_defs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListUserDefineRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_define_region_with_options_async(
        self,
        request: edas_20170801_models.ListUserDefineRegionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListUserDefineRegionResponse:
        """
        @summary Queries custom namespaces.
        
        @param request: ListUserDefineRegionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserDefineRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.debug_enable):
            query['DebugEnable'] = request.debug_enable
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserDefineRegion',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/user_region_defs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListUserDefineRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_define_region(
        self,
        request: edas_20170801_models.ListUserDefineRegionRequest,
    ) -> edas_20170801_models.ListUserDefineRegionResponse:
        """
        @summary Queries custom namespaces.
        
        @param request: ListUserDefineRegionRequest
        @return: ListUserDefineRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_define_region_with_options(request, headers, runtime)

    async def list_user_define_region_async(
        self,
        request: edas_20170801_models.ListUserDefineRegionRequest,
    ) -> edas_20170801_models.ListUserDefineRegionResponse:
        """
        @summary Queries custom namespaces.
        
        @param request: ListUserDefineRegionRequest
        @return: ListUserDefineRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_define_region_with_options_async(request, headers, runtime)

    def list_vpc_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListVpcResponse:
        """
        @summary The HTTP status code returned.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVpcResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListVpc',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/vpc_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ListVpcResponse:
        """
        @summary The HTTP status code returned.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVpcResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListVpc',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/vpc_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ListVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc(self) -> edas_20170801_models.ListVpcResponse:
        """
        @summary The HTTP status code returned.
        
        @return: ListVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_vpc_with_options(headers, runtime)

    async def list_vpc_async(self) -> edas_20170801_models.ListVpcResponse:
        """
        @summary The HTTP status code returned.
        
        @return: ListVpcResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_vpc_with_options_async(headers, runtime)

    def migrate_ecu_with_options(
        self,
        request: edas_20170801_models.MigrateEcuRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.MigrateEcuResponse:
        """
        @summary Migrates an elastic compute unit (ECU) to the default cluster in a specified namespace.
        
        @description ## Limits
        We recommend that you do not call this operation. Instead, we recommend that you call the TransformClusterMember operation. For more information, see [TransformClusterMember](https://help.aliyun.com/document_detail/71514.html).
        When you call this operation to import an Elastic Compute Service (ECS) instance, the operating system of the ECS instance is reinstalled. After the operating system is reinstalled, all data of the ECS instance is deleted. You must set a logon password for the ECS instance. Make sure that no important data exists on or data has been backed up for the ECS instance that you want to import.
        ## Terms
        **Namespace**: the logical concept that is used to isolate resources and microservices in Enterprise Distributed Application Service (EDAS). The resources include clusters, ECS instances, and applications. You can use a default or custom namespace. Each region has a default namespace and supports multiple custom namespaces. By default, only the default namespace is available. You do not need to create a custom namespace if you do not want to isolate resources or microservices.
        **ECU**: After an ECS instance is imported to a cluster, the instance becomes an ECU.
        **Elastic compute container (ECC)**: After you deploy an application to an ECU in a cluster, the ECU becomes an ECC.
        
        @param request: MigrateEcuRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: MigrateEcuResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateEcu',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/migrate_ecu',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.MigrateEcuResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_ecu_with_options_async(
        self,
        request: edas_20170801_models.MigrateEcuRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.MigrateEcuResponse:
        """
        @summary Migrates an elastic compute unit (ECU) to the default cluster in a specified namespace.
        
        @description ## Limits
        We recommend that you do not call this operation. Instead, we recommend that you call the TransformClusterMember operation. For more information, see [TransformClusterMember](https://help.aliyun.com/document_detail/71514.html).
        When you call this operation to import an Elastic Compute Service (ECS) instance, the operating system of the ECS instance is reinstalled. After the operating system is reinstalled, all data of the ECS instance is deleted. You must set a logon password for the ECS instance. Make sure that no important data exists on or data has been backed up for the ECS instance that you want to import.
        ## Terms
        **Namespace**: the logical concept that is used to isolate resources and microservices in Enterprise Distributed Application Service (EDAS). The resources include clusters, ECS instances, and applications. You can use a default or custom namespace. Each region has a default namespace and supports multiple custom namespaces. By default, only the default namespace is available. You do not need to create a custom namespace if you do not want to isolate resources or microservices.
        **ECU**: After an ECS instance is imported to a cluster, the instance becomes an ECU.
        **Elastic compute container (ECC)**: After you deploy an application to an ECU in a cluster, the ECU becomes an ECC.
        
        @param request: MigrateEcuRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: MigrateEcuResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MigrateEcu',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/migrate_ecu',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.MigrateEcuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_ecu(
        self,
        request: edas_20170801_models.MigrateEcuRequest,
    ) -> edas_20170801_models.MigrateEcuResponse:
        """
        @summary Migrates an elastic compute unit (ECU) to the default cluster in a specified namespace.
        
        @description ## Limits
        We recommend that you do not call this operation. Instead, we recommend that you call the TransformClusterMember operation. For more information, see [TransformClusterMember](https://help.aliyun.com/document_detail/71514.html).
        When you call this operation to import an Elastic Compute Service (ECS) instance, the operating system of the ECS instance is reinstalled. After the operating system is reinstalled, all data of the ECS instance is deleted. You must set a logon password for the ECS instance. Make sure that no important data exists on or data has been backed up for the ECS instance that you want to import.
        ## Terms
        **Namespace**: the logical concept that is used to isolate resources and microservices in Enterprise Distributed Application Service (EDAS). The resources include clusters, ECS instances, and applications. You can use a default or custom namespace. Each region has a default namespace and supports multiple custom namespaces. By default, only the default namespace is available. You do not need to create a custom namespace if you do not want to isolate resources or microservices.
        **ECU**: After an ECS instance is imported to a cluster, the instance becomes an ECU.
        **Elastic compute container (ECC)**: After you deploy an application to an ECU in a cluster, the ECU becomes an ECC.
        
        @param request: MigrateEcuRequest
        @return: MigrateEcuResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.migrate_ecu_with_options(request, headers, runtime)

    async def migrate_ecu_async(
        self,
        request: edas_20170801_models.MigrateEcuRequest,
    ) -> edas_20170801_models.MigrateEcuResponse:
        """
        @summary Migrates an elastic compute unit (ECU) to the default cluster in a specified namespace.
        
        @description ## Limits
        We recommend that you do not call this operation. Instead, we recommend that you call the TransformClusterMember operation. For more information, see [TransformClusterMember](https://help.aliyun.com/document_detail/71514.html).
        When you call this operation to import an Elastic Compute Service (ECS) instance, the operating system of the ECS instance is reinstalled. After the operating system is reinstalled, all data of the ECS instance is deleted. You must set a logon password for the ECS instance. Make sure that no important data exists on or data has been backed up for the ECS instance that you want to import.
        ## Terms
        **Namespace**: the logical concept that is used to isolate resources and microservices in Enterprise Distributed Application Service (EDAS). The resources include clusters, ECS instances, and applications. You can use a default or custom namespace. Each region has a default namespace and supports multiple custom namespaces. By default, only the default namespace is available. You do not need to create a custom namespace if you do not want to isolate resources or microservices.
        **ECU**: After an ECS instance is imported to a cluster, the instance becomes an ECU.
        **Elastic compute container (ECC)**: After you deploy an application to an ECU in a cluster, the ECU becomes an ECC.
        
        @param request: MigrateEcuRequest
        @return: MigrateEcuResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.migrate_ecu_with_options_async(request, headers, runtime)

    def modify_scaling_rule_with_options(
        self,
        request: edas_20170801_models.ModifyScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ModifyScalingRuleResponse:
        """
        @summary Modifies the scaling rule for an application.
        
        @param request: ModifyScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_eula):
            query['AcceptEULA'] = request.accept_eula
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.in_condition):
            query['InCondition'] = request.in_condition
        if not UtilClient.is_unset(request.in_cpu):
            query['InCpu'] = request.in_cpu
        if not UtilClient.is_unset(request.in_duration):
            query['InDuration'] = request.in_duration
        if not UtilClient.is_unset(request.in_enable):
            query['InEnable'] = request.in_enable
        if not UtilClient.is_unset(request.in_instance_num):
            query['InInstanceNum'] = request.in_instance_num
        if not UtilClient.is_unset(request.in_load):
            query['InLoad'] = request.in_load
        if not UtilClient.is_unset(request.in_rt):
            query['InRT'] = request.in_rt
        if not UtilClient.is_unset(request.in_step):
            query['InStep'] = request.in_step
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.multi_az_policy):
            query['MultiAzPolicy'] = request.multi_az_policy
        if not UtilClient.is_unset(request.out_cpu):
            query['OutCPU'] = request.out_cpu
        if not UtilClient.is_unset(request.out_condition):
            query['OutCondition'] = request.out_condition
        if not UtilClient.is_unset(request.out_duration):
            query['OutDuration'] = request.out_duration
        if not UtilClient.is_unset(request.out_enable):
            query['OutEnable'] = request.out_enable
        if not UtilClient.is_unset(request.out_instance_num):
            query['OutInstanceNum'] = request.out_instance_num
        if not UtilClient.is_unset(request.out_load):
            query['OutLoad'] = request.out_load
        if not UtilClient.is_unset(request.out_rt):
            query['OutRT'] = request.out_rt
        if not UtilClient.is_unset(request.out_step):
            query['OutStep'] = request.out_step
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.resource_from):
            query['ResourceFrom'] = request.resource_from
        if not UtilClient.is_unset(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_instance_id):
            query['TemplateInstanceId'] = request.template_instance_id
        if not UtilClient.is_unset(request.template_instance_name):
            query['TemplateInstanceName'] = request.template_instance_name
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/scaling_rules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ModifyScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_rule_with_options_async(
        self,
        request: edas_20170801_models.ModifyScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ModifyScalingRuleResponse:
        """
        @summary Modifies the scaling rule for an application.
        
        @param request: ModifyScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_eula):
            query['AcceptEULA'] = request.accept_eula
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.in_condition):
            query['InCondition'] = request.in_condition
        if not UtilClient.is_unset(request.in_cpu):
            query['InCpu'] = request.in_cpu
        if not UtilClient.is_unset(request.in_duration):
            query['InDuration'] = request.in_duration
        if not UtilClient.is_unset(request.in_enable):
            query['InEnable'] = request.in_enable
        if not UtilClient.is_unset(request.in_instance_num):
            query['InInstanceNum'] = request.in_instance_num
        if not UtilClient.is_unset(request.in_load):
            query['InLoad'] = request.in_load
        if not UtilClient.is_unset(request.in_rt):
            query['InRT'] = request.in_rt
        if not UtilClient.is_unset(request.in_step):
            query['InStep'] = request.in_step
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.multi_az_policy):
            query['MultiAzPolicy'] = request.multi_az_policy
        if not UtilClient.is_unset(request.out_cpu):
            query['OutCPU'] = request.out_cpu
        if not UtilClient.is_unset(request.out_condition):
            query['OutCondition'] = request.out_condition
        if not UtilClient.is_unset(request.out_duration):
            query['OutDuration'] = request.out_duration
        if not UtilClient.is_unset(request.out_enable):
            query['OutEnable'] = request.out_enable
        if not UtilClient.is_unset(request.out_instance_num):
            query['OutInstanceNum'] = request.out_instance_num
        if not UtilClient.is_unset(request.out_load):
            query['OutLoad'] = request.out_load
        if not UtilClient.is_unset(request.out_rt):
            query['OutRT'] = request.out_rt
        if not UtilClient.is_unset(request.out_step):
            query['OutStep'] = request.out_step
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.resource_from):
            query['ResourceFrom'] = request.resource_from
        if not UtilClient.is_unset(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_instance_id):
            query['TemplateInstanceId'] = request.template_instance_id
        if not UtilClient.is_unset(request.template_instance_name):
            query['TemplateInstanceName'] = request.template_instance_name
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/scaling_rules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ModifyScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scaling_rule(
        self,
        request: edas_20170801_models.ModifyScalingRuleRequest,
    ) -> edas_20170801_models.ModifyScalingRuleResponse:
        """
        @summary Modifies the scaling rule for an application.
        
        @param request: ModifyScalingRuleRequest
        @return: ModifyScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_scaling_rule_with_options(request, headers, runtime)

    async def modify_scaling_rule_async(
        self,
        request: edas_20170801_models.ModifyScalingRuleRequest,
    ) -> edas_20170801_models.ModifyScalingRuleResponse:
        """
        @summary Modifies the scaling rule for an application.
        
        @param request: ModifyScalingRuleRequest
        @return: ModifyScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_scaling_rule_with_options_async(request, headers, runtime)

    def query_application_status_with_options(
        self,
        request: edas_20170801_models.QueryApplicationStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.QueryApplicationStatusResponse:
        """
        @summary Queries the status of an application.
        
        @param request: QueryApplicationStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryApplicationStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryApplicationStatus',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/app_status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.QueryApplicationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_application_status_with_options_async(
        self,
        request: edas_20170801_models.QueryApplicationStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.QueryApplicationStatusResponse:
        """
        @summary Queries the status of an application.
        
        @param request: QueryApplicationStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryApplicationStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryApplicationStatus',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/app_status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.QueryApplicationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_application_status(
        self,
        request: edas_20170801_models.QueryApplicationStatusRequest,
    ) -> edas_20170801_models.QueryApplicationStatusResponse:
        """
        @summary Queries the status of an application.
        
        @param request: QueryApplicationStatusRequest
        @return: QueryApplicationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_application_status_with_options(request, headers, runtime)

    async def query_application_status_async(
        self,
        request: edas_20170801_models.QueryApplicationStatusRequest,
    ) -> edas_20170801_models.QueryApplicationStatusResponse:
        """
        @summary Queries the status of an application.
        
        @param request: QueryApplicationStatusRequest
        @return: QueryApplicationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_application_status_with_options_async(request, headers, runtime)

    def query_ecc_info_with_options(
        self,
        request: edas_20170801_models.QueryEccInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.QueryEccInfoResponse:
        """
        @summary Queries details about an elastic compute container (ECC). This operation is applicable to Container Service for Kubernetes (ACK) clusters.
        
        @param request: QueryEccInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryEccInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecc_id):
            query['EccId'] = request.ecc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEccInfo',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/ecc',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.QueryEccInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ecc_info_with_options_async(
        self,
        request: edas_20170801_models.QueryEccInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.QueryEccInfoResponse:
        """
        @summary Queries details about an elastic compute container (ECC). This operation is applicable to Container Service for Kubernetes (ACK) clusters.
        
        @param request: QueryEccInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryEccInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecc_id):
            query['EccId'] = request.ecc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEccInfo',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/ecc',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.QueryEccInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ecc_info(
        self,
        request: edas_20170801_models.QueryEccInfoRequest,
    ) -> edas_20170801_models.QueryEccInfoResponse:
        """
        @summary Queries details about an elastic compute container (ECC). This operation is applicable to Container Service for Kubernetes (ACK) clusters.
        
        @param request: QueryEccInfoRequest
        @return: QueryEccInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_ecc_info_with_options(request, headers, runtime)

    async def query_ecc_info_async(
        self,
        request: edas_20170801_models.QueryEccInfoRequest,
    ) -> edas_20170801_models.QueryEccInfoResponse:
        """
        @summary Queries details about an elastic compute container (ECC). This operation is applicable to Container Service for Kubernetes (ACK) clusters.
        
        @param request: QueryEccInfoRequest
        @return: QueryEccInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_ecc_info_with_options_async(request, headers, runtime)

    def query_migrate_ecu_list_with_options(
        self,
        request: edas_20170801_models.QueryMigrateEcuListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.QueryMigrateEcuListResponse:
        """
        @summary Queries the elastic compute units (ECUs) that can be migrated.
        
        @param request: QueryMigrateEcuListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMigrateEcuListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMigrateEcuList',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/migrate_ecu_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.QueryMigrateEcuListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_migrate_ecu_list_with_options_async(
        self,
        request: edas_20170801_models.QueryMigrateEcuListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.QueryMigrateEcuListResponse:
        """
        @summary Queries the elastic compute units (ECUs) that can be migrated.
        
        @param request: QueryMigrateEcuListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMigrateEcuListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMigrateEcuList',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/migrate_ecu_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.QueryMigrateEcuListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_migrate_ecu_list(
        self,
        request: edas_20170801_models.QueryMigrateEcuListRequest,
    ) -> edas_20170801_models.QueryMigrateEcuListResponse:
        """
        @summary Queries the elastic compute units (ECUs) that can be migrated.
        
        @param request: QueryMigrateEcuListRequest
        @return: QueryMigrateEcuListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_migrate_ecu_list_with_options(request, headers, runtime)

    async def query_migrate_ecu_list_async(
        self,
        request: edas_20170801_models.QueryMigrateEcuListRequest,
    ) -> edas_20170801_models.QueryMigrateEcuListResponse:
        """
        @summary Queries the elastic compute units (ECUs) that can be migrated.
        
        @param request: QueryMigrateEcuListRequest
        @return: QueryMigrateEcuListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_migrate_ecu_list_with_options_async(request, headers, runtime)

    def query_migrate_region_list_with_options(
        self,
        request: edas_20170801_models.QueryMigrateRegionListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.QueryMigrateRegionListResponse:
        """
        @summary Queries the namespaces to which an instance can be migrated.
        
        @param request: QueryMigrateRegionListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMigrateRegionListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMigrateRegionList',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/migrate_region_select',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.QueryMigrateRegionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_migrate_region_list_with_options_async(
        self,
        request: edas_20170801_models.QueryMigrateRegionListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.QueryMigrateRegionListResponse:
        """
        @summary Queries the namespaces to which an instance can be migrated.
        
        @param request: QueryMigrateRegionListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryMigrateRegionListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMigrateRegionList',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/migrate_region_select',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.QueryMigrateRegionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_migrate_region_list(
        self,
        request: edas_20170801_models.QueryMigrateRegionListRequest,
    ) -> edas_20170801_models.QueryMigrateRegionListResponse:
        """
        @summary Queries the namespaces to which an instance can be migrated.
        
        @param request: QueryMigrateRegionListRequest
        @return: QueryMigrateRegionListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_migrate_region_list_with_options(request, headers, runtime)

    async def query_migrate_region_list_async(
        self,
        request: edas_20170801_models.QueryMigrateRegionListRequest,
    ) -> edas_20170801_models.QueryMigrateRegionListResponse:
        """
        @summary Queries the namespaces to which an instance can be migrated.
        
        @param request: QueryMigrateRegionListRequest
        @return: QueryMigrateRegionListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_migrate_region_list_with_options_async(request, headers, runtime)

    def query_region_config_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.QueryRegionConfigResponse:
        """
        @summary Queries the configurations of different regions that are supported by Enterprise Distributed Application Service (EDAS).
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRegionConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='QueryRegionConfig',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/region_config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.QueryRegionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_region_config_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.QueryRegionConfigResponse:
        """
        @summary Queries the configurations of different regions that are supported by Enterprise Distributed Application Service (EDAS).
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryRegionConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='QueryRegionConfig',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/region_config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.QueryRegionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_region_config(self) -> edas_20170801_models.QueryRegionConfigResponse:
        """
        @summary Queries the configurations of different regions that are supported by Enterprise Distributed Application Service (EDAS).
        
        @return: QueryRegionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_region_config_with_options(headers, runtime)

    async def query_region_config_async(self) -> edas_20170801_models.QueryRegionConfigResponse:
        """
        @summary Queries the configurations of different regions that are supported by Enterprise Distributed Application Service (EDAS).
        
        @return: QueryRegionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_region_config_with_options_async(headers, runtime)

    def query_sls_log_store_list_with_options(
        self,
        request: edas_20170801_models.QuerySlsLogStoreListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.QuerySlsLogStoreListResponse:
        """
        @summary Queries the configuration details of Log Service for an application.
        
        @param request: QuerySlsLogStoreListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySlsLogStoreListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySlsLogStoreList',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/sls/query_sls_log_store_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.QuerySlsLogStoreListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sls_log_store_list_with_options_async(
        self,
        request: edas_20170801_models.QuerySlsLogStoreListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.QuerySlsLogStoreListResponse:
        """
        @summary Queries the configuration details of Log Service for an application.
        
        @param request: QuerySlsLogStoreListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySlsLogStoreListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySlsLogStoreList',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/sls/query_sls_log_store_list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.QuerySlsLogStoreListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sls_log_store_list(
        self,
        request: edas_20170801_models.QuerySlsLogStoreListRequest,
    ) -> edas_20170801_models.QuerySlsLogStoreListResponse:
        """
        @summary Queries the configuration details of Log Service for an application.
        
        @param request: QuerySlsLogStoreListRequest
        @return: QuerySlsLogStoreListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_sls_log_store_list_with_options(request, headers, runtime)

    async def query_sls_log_store_list_async(
        self,
        request: edas_20170801_models.QuerySlsLogStoreListRequest,
    ) -> edas_20170801_models.QuerySlsLogStoreListResponse:
        """
        @summary Queries the configuration details of Log Service for an application.
        
        @param request: QuerySlsLogStoreListRequest
        @return: QuerySlsLogStoreListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_sls_log_store_list_with_options_async(request, headers, runtime)

    def reset_application_with_options(
        self,
        request: edas_20170801_models.ResetApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ResetApplicationResponse:
        """
        @summary Resets an application.
        
        @param request: ResetApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_reset',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ResetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_application_with_options_async(
        self,
        request: edas_20170801_models.ResetApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ResetApplicationResponse:
        """
        @summary Resets an application.
        
        @param request: ResetApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_reset',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ResetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_application(
        self,
        request: edas_20170801_models.ResetApplicationRequest,
    ) -> edas_20170801_models.ResetApplicationResponse:
        """
        @summary Resets an application.
        
        @param request: ResetApplicationRequest
        @return: ResetApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reset_application_with_options(request, headers, runtime)

    async def reset_application_async(
        self,
        request: edas_20170801_models.ResetApplicationRequest,
    ) -> edas_20170801_models.ResetApplicationResponse:
        """
        @summary Resets an application.
        
        @param request: ResetApplicationRequest
        @return: ResetApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.reset_application_with_options_async(request, headers, runtime)

    def restart_application_with_options(
        self,
        request: edas_20170801_models.RestartApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.RestartApplicationResponse:
        """
        @summary Restarts an application. This operation is applicable to applications that are deployed in Elastic Compute Service (ECS) clusters.
        
        @param request: RestartApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_restart',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.RestartApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_application_with_options_async(
        self,
        request: edas_20170801_models.RestartApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.RestartApplicationResponse:
        """
        @summary Restarts an application. This operation is applicable to applications that are deployed in Elastic Compute Service (ECS) clusters.
        
        @param request: RestartApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_restart',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.RestartApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_application(
        self,
        request: edas_20170801_models.RestartApplicationRequest,
    ) -> edas_20170801_models.RestartApplicationResponse:
        """
        @summary Restarts an application. This operation is applicable to applications that are deployed in Elastic Compute Service (ECS) clusters.
        
        @param request: RestartApplicationRequest
        @return: RestartApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_application_with_options(request, headers, runtime)

    async def restart_application_async(
        self,
        request: edas_20170801_models.RestartApplicationRequest,
    ) -> edas_20170801_models.RestartApplicationResponse:
        """
        @summary Restarts an application. This operation is applicable to applications that are deployed in Elastic Compute Service (ECS) clusters.
        
        @param request: RestartApplicationRequest
        @return: RestartApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restart_application_with_options_async(request, headers, runtime)

    def restart_k8s_application_with_options(
        self,
        request: edas_20170801_models.RestartK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.RestartK8sApplicationResponse:
        """
        @summary Restarts an application that is deployed in a Container Service for Kubernetes (ACK) cluster or a serverless Kubernetes cluster.
        
        @param request: RestartK8sApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartK8sApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartK8sApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/restart_k8s_app',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.RestartK8sApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_k8s_application_with_options_async(
        self,
        request: edas_20170801_models.RestartK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.RestartK8sApplicationResponse:
        """
        @summary Restarts an application that is deployed in a Container Service for Kubernetes (ACK) cluster or a serverless Kubernetes cluster.
        
        @param request: RestartK8sApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartK8sApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartK8sApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/restart_k8s_app',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.RestartK8sApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_k8s_application(
        self,
        request: edas_20170801_models.RestartK8sApplicationRequest,
    ) -> edas_20170801_models.RestartK8sApplicationResponse:
        """
        @summary Restarts an application that is deployed in a Container Service for Kubernetes (ACK) cluster or a serverless Kubernetes cluster.
        
        @param request: RestartK8sApplicationRequest
        @return: RestartK8sApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.restart_k8s_application_with_options(request, headers, runtime)

    async def restart_k8s_application_async(
        self,
        request: edas_20170801_models.RestartK8sApplicationRequest,
    ) -> edas_20170801_models.RestartK8sApplicationResponse:
        """
        @summary Restarts an application that is deployed in a Container Service for Kubernetes (ACK) cluster or a serverless Kubernetes cluster.
        
        @param request: RestartK8sApplicationRequest
        @return: RestartK8sApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.restart_k8s_application_with_options_async(request, headers, runtime)

    def retry_change_order_task_with_options(
        self,
        request: edas_20170801_models.RetryChangeOrderTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.RetryChangeOrderTaskResponse:
        """
        @summary Retries a failed process.
        
        @param request: RetryChangeOrderTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryChangeOrderTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.retry_status):
            query['RetryStatus'] = request.retry_status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryChangeOrderTask',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/task_retry',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.RetryChangeOrderTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_change_order_task_with_options_async(
        self,
        request: edas_20170801_models.RetryChangeOrderTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.RetryChangeOrderTaskResponse:
        """
        @summary Retries a failed process.
        
        @param request: RetryChangeOrderTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryChangeOrderTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.retry_status):
            query['RetryStatus'] = request.retry_status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryChangeOrderTask',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/task_retry',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.RetryChangeOrderTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_change_order_task(
        self,
        request: edas_20170801_models.RetryChangeOrderTaskRequest,
    ) -> edas_20170801_models.RetryChangeOrderTaskResponse:
        """
        @summary Retries a failed process.
        
        @param request: RetryChangeOrderTaskRequest
        @return: RetryChangeOrderTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.retry_change_order_task_with_options(request, headers, runtime)

    async def retry_change_order_task_async(
        self,
        request: edas_20170801_models.RetryChangeOrderTaskRequest,
    ) -> edas_20170801_models.RetryChangeOrderTaskResponse:
        """
        @summary Retries a failed process.
        
        @param request: RetryChangeOrderTaskRequest
        @return: RetryChangeOrderTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.retry_change_order_task_with_options_async(request, headers, runtime)

    def rollback_application_with_options(
        self,
        request: edas_20170801_models.RollbackApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.RollbackApplicationResponse:
        """
        @summary Rolls back an application.
        
        @param request: RollbackApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.batch):
            query['Batch'] = request.batch
        if not UtilClient.is_unset(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_rollback',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.RollbackApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_application_with_options_async(
        self,
        request: edas_20170801_models.RollbackApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.RollbackApplicationResponse:
        """
        @summary Rolls back an application.
        
        @param request: RollbackApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.batch):
            query['Batch'] = request.batch
        if not UtilClient.is_unset(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.history_version):
            query['HistoryVersion'] = request.history_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_rollback',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.RollbackApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_application(
        self,
        request: edas_20170801_models.RollbackApplicationRequest,
    ) -> edas_20170801_models.RollbackApplicationResponse:
        """
        @summary Rolls back an application.
        
        @param request: RollbackApplicationRequest
        @return: RollbackApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rollback_application_with_options(request, headers, runtime)

    async def rollback_application_async(
        self,
        request: edas_20170801_models.RollbackApplicationRequest,
    ) -> edas_20170801_models.RollbackApplicationResponse:
        """
        @summary Rolls back an application.
        
        @param request: RollbackApplicationRequest
        @return: RollbackApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rollback_application_with_options_async(request, headers, runtime)

    def rollback_change_order_with_options(
        self,
        request: edas_20170801_models.RollbackChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.RollbackChangeOrderResponse:
        """
        @summary Terminates an application change process and rolls back the application. This operation is applicable to applications that are deployed in Elastic Compute Service (ECS) clusters.
        
        @param request: RollbackChangeOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackChangeOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackChangeOrder',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/oam/changeorder/rollback',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.RollbackChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_change_order_with_options_async(
        self,
        request: edas_20170801_models.RollbackChangeOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.RollbackChangeOrderResponse:
        """
        @summary Terminates an application change process and rolls back the application. This operation is applicable to applications that are deployed in Elastic Compute Service (ECS) clusters.
        
        @param request: RollbackChangeOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackChangeOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackChangeOrder',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/oam/changeorder/rollback',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.RollbackChangeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_change_order(
        self,
        request: edas_20170801_models.RollbackChangeOrderRequest,
    ) -> edas_20170801_models.RollbackChangeOrderResponse:
        """
        @summary Terminates an application change process and rolls back the application. This operation is applicable to applications that are deployed in Elastic Compute Service (ECS) clusters.
        
        @param request: RollbackChangeOrderRequest
        @return: RollbackChangeOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rollback_change_order_with_options(request, headers, runtime)

    async def rollback_change_order_async(
        self,
        request: edas_20170801_models.RollbackChangeOrderRequest,
    ) -> edas_20170801_models.RollbackChangeOrderResponse:
        """
        @summary Terminates an application change process and rolls back the application. This operation is applicable to applications that are deployed in Elastic Compute Service (ECS) clusters.
        
        @param request: RollbackChangeOrderRequest
        @return: RollbackChangeOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rollback_change_order_with_options_async(request, headers, runtime)

    def scale_in_application_with_options(
        self,
        request: edas_20170801_models.ScaleInApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ScaleInApplicationResponse:
        """
        @summary Scales in an application.
        
        @param request: ScaleInApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleInApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        if not UtilClient.is_unset(request.force_status):
            query['ForceStatus'] = request.force_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleInApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_scale_in',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ScaleInApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_in_application_with_options_async(
        self,
        request: edas_20170801_models.ScaleInApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ScaleInApplicationResponse:
        """
        @summary Scales in an application.
        
        @param request: ScaleInApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleInApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        if not UtilClient.is_unset(request.force_status):
            query['ForceStatus'] = request.force_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleInApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_scale_in',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ScaleInApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_in_application(
        self,
        request: edas_20170801_models.ScaleInApplicationRequest,
    ) -> edas_20170801_models.ScaleInApplicationResponse:
        """
        @summary Scales in an application.
        
        @param request: ScaleInApplicationRequest
        @return: ScaleInApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_in_application_with_options(request, headers, runtime)

    async def scale_in_application_async(
        self,
        request: edas_20170801_models.ScaleInApplicationRequest,
    ) -> edas_20170801_models.ScaleInApplicationResponse:
        """
        @summary Scales in an application.
        
        @param request: ScaleInApplicationRequest
        @return: ScaleInApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scale_in_application_with_options_async(request, headers, runtime)

    def scale_k8s_application_with_options(
        self,
        request: edas_20170801_models.ScaleK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ScaleK8sApplicationResponse:
        """
        @summary Scales out or in an application that is deployed in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: ScaleK8sApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleK8sApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleK8sApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_apps',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ScaleK8sApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_k8s_application_with_options_async(
        self,
        request: edas_20170801_models.ScaleK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ScaleK8sApplicationResponse:
        """
        @summary Scales out or in an application that is deployed in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: ScaleK8sApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleK8sApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleK8sApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_apps',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ScaleK8sApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_k8s_application(
        self,
        request: edas_20170801_models.ScaleK8sApplicationRequest,
    ) -> edas_20170801_models.ScaleK8sApplicationResponse:
        """
        @summary Scales out or in an application that is deployed in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: ScaleK8sApplicationRequest
        @return: ScaleK8sApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_k8s_application_with_options(request, headers, runtime)

    async def scale_k8s_application_async(
        self,
        request: edas_20170801_models.ScaleK8sApplicationRequest,
    ) -> edas_20170801_models.ScaleK8sApplicationResponse:
        """
        @summary Scales out or in an application that is deployed in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: ScaleK8sApplicationRequest
        @return: ScaleK8sApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scale_k8s_application_with_options_async(request, headers, runtime)

    def scale_out_application_with_options(
        self,
        request: edas_20170801_models.ScaleOutApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ScaleOutApplicationResponse:
        """
        @summary Scales out an application.
        
        @param request: ScaleOutApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleOutApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.deploy_group):
            query['DeployGroup'] = request.deploy_group
        if not UtilClient.is_unset(request.ecu_info):
            query['EcuInfo'] = request.ecu_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleOutApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_scale_out',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ScaleOutApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_out_application_with_options_async(
        self,
        request: edas_20170801_models.ScaleOutApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ScaleOutApplicationResponse:
        """
        @summary Scales out an application.
        
        @param request: ScaleOutApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleOutApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.deploy_group):
            query['DeployGroup'] = request.deploy_group
        if not UtilClient.is_unset(request.ecu_info):
            query['EcuInfo'] = request.ecu_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleOutApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_scale_out',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ScaleOutApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_out_application(
        self,
        request: edas_20170801_models.ScaleOutApplicationRequest,
    ) -> edas_20170801_models.ScaleOutApplicationResponse:
        """
        @summary Scales out an application.
        
        @param request: ScaleOutApplicationRequest
        @return: ScaleOutApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_out_application_with_options(request, headers, runtime)

    async def scale_out_application_async(
        self,
        request: edas_20170801_models.ScaleOutApplicationRequest,
    ) -> edas_20170801_models.ScaleOutApplicationResponse:
        """
        @summary Scales out an application.
        
        @param request: ScaleOutApplicationRequest
        @return: ScaleOutApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scale_out_application_with_options_async(request, headers, runtime)

    def scaleout_application_with_new_instances_with_options(
        self,
        request: edas_20170801_models.ScaleoutApplicationWithNewInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ScaleoutApplicationWithNewInstancesResponse:
        """
        @summary Purchases Elastic Compute Service (ECS) instances in the Enterprise Distributed Application Service (EDAS) console and adds the purchased ECS instances to the specified instance group of an application.
        
        @description ## Limits
        Assume that the auto scaling feature is configured and enabled for an application. When an auto scale-in is triggered for the application, the ECS instances that are purchased by calling this operation are removed first.
        
        @param request: ScaleoutApplicationWithNewInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleoutApplicationWithNewInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_charge_period):
            query['InstanceChargePeriod'] = request.instance_charge_period
        if not UtilClient.is_unset(request.instance_charge_period_unit):
            query['InstanceChargePeriodUnit'] = request.instance_charge_period_unit
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.scaling_num):
            query['ScalingNum'] = request.scaling_num
        if not UtilClient.is_unset(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_instance_id):
            query['TemplateInstanceId'] = request.template_instance_id
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleoutApplicationWithNewInstances',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/scaling/scale_out',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ScaleoutApplicationWithNewInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def scaleout_application_with_new_instances_with_options_async(
        self,
        request: edas_20170801_models.ScaleoutApplicationWithNewInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.ScaleoutApplicationWithNewInstancesResponse:
        """
        @summary Purchases Elastic Compute Service (ECS) instances in the Enterprise Distributed Application Service (EDAS) console and adds the purchased ECS instances to the specified instance group of an application.
        
        @description ## Limits
        Assume that the auto scaling feature is configured and enabled for an application. When an auto scale-in is triggered for the application, the ECS instances that are purchased by calling this operation are removed first.
        
        @param request: ScaleoutApplicationWithNewInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleoutApplicationWithNewInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_charge_period):
            query['InstanceChargePeriod'] = request.instance_charge_period
        if not UtilClient.is_unset(request.instance_charge_period_unit):
            query['InstanceChargePeriodUnit'] = request.instance_charge_period_unit
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.scaling_num):
            query['ScalingNum'] = request.scaling_num
        if not UtilClient.is_unset(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_instance_id):
            query['TemplateInstanceId'] = request.template_instance_id
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleoutApplicationWithNewInstances',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/scaling/scale_out',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.ScaleoutApplicationWithNewInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scaleout_application_with_new_instances(
        self,
        request: edas_20170801_models.ScaleoutApplicationWithNewInstancesRequest,
    ) -> edas_20170801_models.ScaleoutApplicationWithNewInstancesResponse:
        """
        @summary Purchases Elastic Compute Service (ECS) instances in the Enterprise Distributed Application Service (EDAS) console and adds the purchased ECS instances to the specified instance group of an application.
        
        @description ## Limits
        Assume that the auto scaling feature is configured and enabled for an application. When an auto scale-in is triggered for the application, the ECS instances that are purchased by calling this operation are removed first.
        
        @param request: ScaleoutApplicationWithNewInstancesRequest
        @return: ScaleoutApplicationWithNewInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scaleout_application_with_new_instances_with_options(request, headers, runtime)

    async def scaleout_application_with_new_instances_async(
        self,
        request: edas_20170801_models.ScaleoutApplicationWithNewInstancesRequest,
    ) -> edas_20170801_models.ScaleoutApplicationWithNewInstancesResponse:
        """
        @summary Purchases Elastic Compute Service (ECS) instances in the Enterprise Distributed Application Service (EDAS) console and adds the purchased ECS instances to the specified instance group of an application.
        
        @description ## Limits
        Assume that the auto scaling feature is configured and enabled for an application. When an auto scale-in is triggered for the application, the ECS instances that are purchased by calling this operation are removed first.
        
        @param request: ScaleoutApplicationWithNewInstancesRequest
        @return: ScaleoutApplicationWithNewInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scaleout_application_with_new_instances_with_options_async(request, headers, runtime)

    def start_application_with_options(
        self,
        request: edas_20170801_models.StartApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.StartApplicationResponse:
        """
        @summary Starts an application.
        
        @param request: StartApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.StartApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_application_with_options_async(
        self,
        request: edas_20170801_models.StartApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.StartApplicationResponse:
        """
        @summary Starts an application.
        
        @param request: StartApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.StartApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_application(
        self,
        request: edas_20170801_models.StartApplicationRequest,
    ) -> edas_20170801_models.StartApplicationResponse:
        """
        @summary Starts an application.
        
        @param request: StartApplicationRequest
        @return: StartApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_application_with_options(request, headers, runtime)

    async def start_application_async(
        self,
        request: edas_20170801_models.StartApplicationRequest,
    ) -> edas_20170801_models.StartApplicationResponse:
        """
        @summary Starts an application.
        
        @param request: StartApplicationRequest
        @return: StartApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_application_with_options_async(request, headers, runtime)

    def start_k8s_app_precheck_with_options(
        self,
        request: edas_20170801_models.StartK8sAppPrecheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.StartK8sAppPrecheckResponse:
        """
        @summary Starts precheck for Kubernetes application changes.
        
        @param request: StartK8sAppPrecheckRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartK8sAppPrecheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_ids):
            query['ComponentIds'] = request.component_ids
        if not UtilClient.is_unset(request.config_mount_descs):
            query['ConfigMountDescs'] = request.config_mount_descs
        if not UtilClient.is_unset(request.empty_dirs):
            query['EmptyDirs'] = request.empty_dirs
        if not UtilClient.is_unset(request.env_froms):
            query['EnvFroms'] = request.env_froms
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.java_start_up_config):
            query['JavaStartUpConfig'] = request.java_start_up_config
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.limit_ephemeral_storage):
            query['LimitEphemeralStorage'] = request.limit_ephemeral_storage
        if not UtilClient.is_unset(request.limit_mem):
            query['LimitMem'] = request.limit_mem
        if not UtilClient.is_unset(request.limitm_cpu):
            query['LimitmCpu'] = request.limitm_cpu
        if not UtilClient.is_unset(request.local_volume):
            query['LocalVolume'] = request.local_volume
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.pvc_mount_descs):
            query['PvcMountDescs'] = request.pvc_mount_descs
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.requests_ephemeral_storage):
            query['RequestsEphemeralStorage'] = request.requests_ephemeral_storage
        if not UtilClient.is_unset(request.requests_mem):
            query['RequestsMem'] = request.requests_mem
        if not UtilClient.is_unset(request.requestsm_cpu):
            query['RequestsmCpu'] = request.requestsm_cpu
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartK8sAppPrecheck',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/app_precheck',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.StartK8sAppPrecheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_k8s_app_precheck_with_options_async(
        self,
        request: edas_20170801_models.StartK8sAppPrecheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.StartK8sAppPrecheckResponse:
        """
        @summary Starts precheck for Kubernetes application changes.
        
        @param request: StartK8sAppPrecheckRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartK8sAppPrecheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_ids):
            query['ComponentIds'] = request.component_ids
        if not UtilClient.is_unset(request.config_mount_descs):
            query['ConfigMountDescs'] = request.config_mount_descs
        if not UtilClient.is_unset(request.empty_dirs):
            query['EmptyDirs'] = request.empty_dirs
        if not UtilClient.is_unset(request.env_froms):
            query['EnvFroms'] = request.env_froms
        if not UtilClient.is_unset(request.envs):
            query['Envs'] = request.envs
        if not UtilClient.is_unset(request.image_url):
            query['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.java_start_up_config):
            query['JavaStartUpConfig'] = request.java_start_up_config
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.limit_ephemeral_storage):
            query['LimitEphemeralStorage'] = request.limit_ephemeral_storage
        if not UtilClient.is_unset(request.limit_mem):
            query['LimitMem'] = request.limit_mem
        if not UtilClient.is_unset(request.limitm_cpu):
            query['LimitmCpu'] = request.limitm_cpu
        if not UtilClient.is_unset(request.local_volume):
            query['LocalVolume'] = request.local_volume
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.package_url):
            query['PackageUrl'] = request.package_url
        if not UtilClient.is_unset(request.pvc_mount_descs):
            query['PvcMountDescs'] = request.pvc_mount_descs
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.requests_ephemeral_storage):
            query['RequestsEphemeralStorage'] = request.requests_ephemeral_storage
        if not UtilClient.is_unset(request.requests_mem):
            query['RequestsMem'] = request.requests_mem
        if not UtilClient.is_unset(request.requestsm_cpu):
            query['RequestsmCpu'] = request.requestsm_cpu
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartK8sAppPrecheck',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/app_precheck',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.StartK8sAppPrecheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_k8s_app_precheck(
        self,
        request: edas_20170801_models.StartK8sAppPrecheckRequest,
    ) -> edas_20170801_models.StartK8sAppPrecheckResponse:
        """
        @summary Starts precheck for Kubernetes application changes.
        
        @param request: StartK8sAppPrecheckRequest
        @return: StartK8sAppPrecheckResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_k8s_app_precheck_with_options(request, headers, runtime)

    async def start_k8s_app_precheck_async(
        self,
        request: edas_20170801_models.StartK8sAppPrecheckRequest,
    ) -> edas_20170801_models.StartK8sAppPrecheckResponse:
        """
        @summary Starts precheck for Kubernetes application changes.
        
        @param request: StartK8sAppPrecheckRequest
        @return: StartK8sAppPrecheckResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_k8s_app_precheck_with_options_async(request, headers, runtime)

    def start_k8s_application_with_options(
        self,
        request: edas_20170801_models.StartK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.StartK8sApplicationResponse:
        """
        @summary Starts an application in a Container Service for Kubernetes (ACK) cluster or Serverless Kubernetes cluster.
        
        @param request: StartK8sApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartK8sApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartK8sApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/start_k8s_app',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.StartK8sApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_k8s_application_with_options_async(
        self,
        request: edas_20170801_models.StartK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.StartK8sApplicationResponse:
        """
        @summary Starts an application in a Container Service for Kubernetes (ACK) cluster or Serverless Kubernetes cluster.
        
        @param request: StartK8sApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartK8sApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartK8sApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/start_k8s_app',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.StartK8sApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_k8s_application(
        self,
        request: edas_20170801_models.StartK8sApplicationRequest,
    ) -> edas_20170801_models.StartK8sApplicationResponse:
        """
        @summary Starts an application in a Container Service for Kubernetes (ACK) cluster or Serverless Kubernetes cluster.
        
        @param request: StartK8sApplicationRequest
        @return: StartK8sApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_k8s_application_with_options(request, headers, runtime)

    async def start_k8s_application_async(
        self,
        request: edas_20170801_models.StartK8sApplicationRequest,
    ) -> edas_20170801_models.StartK8sApplicationResponse:
        """
        @summary Starts an application in a Container Service for Kubernetes (ACK) cluster or Serverless Kubernetes cluster.
        
        @param request: StartK8sApplicationRequest
        @return: StartK8sApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_k8s_application_with_options_async(request, headers, runtime)

    def stop_application_with_options(
        self,
        request: edas_20170801_models.StopApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.StopApplicationResponse:
        """
        @summary Stops an application.
        
        @param request: StopApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.StopApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_application_with_options_async(
        self,
        request: edas_20170801_models.StopApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.StopApplicationResponse:
        """
        @summary Stops an application.
        
        @param request: StopApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.StopApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_application(
        self,
        request: edas_20170801_models.StopApplicationRequest,
    ) -> edas_20170801_models.StopApplicationResponse:
        """
        @summary Stops an application.
        
        @param request: StopApplicationRequest
        @return: StopApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_application_with_options(request, headers, runtime)

    async def stop_application_async(
        self,
        request: edas_20170801_models.StopApplicationRequest,
    ) -> edas_20170801_models.StopApplicationResponse:
        """
        @summary Stops an application.
        
        @param request: StopApplicationRequest
        @return: StopApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_application_with_options_async(request, headers, runtime)

    def stop_k8s_application_with_options(
        self,
        request: edas_20170801_models.StopK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.StopK8sApplicationResponse:
        """
        @summary Stops an application in a Container Service for Kubernetes (ACK) cluster or a Serverless Kubernetes cluster.
        
        @param request: StopK8sApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopK8sApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopK8sApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/stop_k8s_app',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.StopK8sApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_k8s_application_with_options_async(
        self,
        request: edas_20170801_models.StopK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.StopK8sApplicationResponse:
        """
        @summary Stops an application in a Container Service for Kubernetes (ACK) cluster or a Serverless Kubernetes cluster.
        
        @param request: StopK8sApplicationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopK8sApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopK8sApplication',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/stop_k8s_app',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.StopK8sApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_k8s_application(
        self,
        request: edas_20170801_models.StopK8sApplicationRequest,
    ) -> edas_20170801_models.StopK8sApplicationResponse:
        """
        @summary Stops an application in a Container Service for Kubernetes (ACK) cluster or a Serverless Kubernetes cluster.
        
        @param request: StopK8sApplicationRequest
        @return: StopK8sApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_k8s_application_with_options(request, headers, runtime)

    async def stop_k8s_application_async(
        self,
        request: edas_20170801_models.StopK8sApplicationRequest,
    ) -> edas_20170801_models.StopK8sApplicationResponse:
        """
        @summary Stops an application in a Container Service for Kubernetes (ACK) cluster or a Serverless Kubernetes cluster.
        
        @param request: StopK8sApplicationRequest
        @return: StopK8sApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_k8s_application_with_options_async(request, headers, runtime)

    def switch_advanced_monitoring_with_options(
        self,
        request: edas_20170801_models.SwitchAdvancedMonitoringRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.SwitchAdvancedMonitoringResponse:
        """
        @summary Queries the status of the advanced application monitoring feature or configures this feature for an application that is deployed in an Elastic Compute Service (ECS) or Kubernetes cluster.
        
        @description To call the SwitchAdvancedMonitoring operation, you must make sure that the version of Enterprise Distributed Application Service (EDAS) SDK for Java or Python is 3.15.2 or later.
        
        @param request: SwitchAdvancedMonitoringRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchAdvancedMonitoringResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.enable_advanced_monitoring):
            query['EnableAdvancedMonitoring'] = request.enable_advanced_monitoring
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchAdvancedMonitoring',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/monitor/advancedMonitorInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.SwitchAdvancedMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_advanced_monitoring_with_options_async(
        self,
        request: edas_20170801_models.SwitchAdvancedMonitoringRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.SwitchAdvancedMonitoringResponse:
        """
        @summary Queries the status of the advanced application monitoring feature or configures this feature for an application that is deployed in an Elastic Compute Service (ECS) or Kubernetes cluster.
        
        @description To call the SwitchAdvancedMonitoring operation, you must make sure that the version of Enterprise Distributed Application Service (EDAS) SDK for Java or Python is 3.15.2 or later.
        
        @param request: SwitchAdvancedMonitoringRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SwitchAdvancedMonitoringResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.enable_advanced_monitoring):
            query['EnableAdvancedMonitoring'] = request.enable_advanced_monitoring
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchAdvancedMonitoring',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/monitor/advancedMonitorInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.SwitchAdvancedMonitoringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_advanced_monitoring(
        self,
        request: edas_20170801_models.SwitchAdvancedMonitoringRequest,
    ) -> edas_20170801_models.SwitchAdvancedMonitoringResponse:
        """
        @summary Queries the status of the advanced application monitoring feature or configures this feature for an application that is deployed in an Elastic Compute Service (ECS) or Kubernetes cluster.
        
        @description To call the SwitchAdvancedMonitoring operation, you must make sure that the version of Enterprise Distributed Application Service (EDAS) SDK for Java or Python is 3.15.2 or later.
        
        @param request: SwitchAdvancedMonitoringRequest
        @return: SwitchAdvancedMonitoringResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.switch_advanced_monitoring_with_options(request, headers, runtime)

    async def switch_advanced_monitoring_async(
        self,
        request: edas_20170801_models.SwitchAdvancedMonitoringRequest,
    ) -> edas_20170801_models.SwitchAdvancedMonitoringResponse:
        """
        @summary Queries the status of the advanced application monitoring feature or configures this feature for an application that is deployed in an Elastic Compute Service (ECS) or Kubernetes cluster.
        
        @description To call the SwitchAdvancedMonitoring operation, you must make sure that the version of Enterprise Distributed Application Service (EDAS) SDK for Java or Python is 3.15.2 or later.
        
        @param request: SwitchAdvancedMonitoringRequest
        @return: SwitchAdvancedMonitoringResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.switch_advanced_monitoring_with_options_async(request, headers, runtime)

    def synchronize_resource_with_options(
        self,
        request: edas_20170801_models.SynchronizeResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.SynchronizeResourceResponse:
        """
        @summary Synchronizes the basic Alibaba Cloud resources that belong to your account to Enterprise Distributed Application Service (EDAS). This operation is applicable to Elastic Compute Service (ECS) clusters.
        
        @description If you call this operation to synchronize ECS resource information, all instance data is synchronized from ECS. If you have more than 100 ECS instances, we recommend that you do not frequently call this operation.
        
        @param request: SynchronizeResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SynchronizeResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SynchronizeResource',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/pop_sync_resource',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.SynchronizeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def synchronize_resource_with_options_async(
        self,
        request: edas_20170801_models.SynchronizeResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.SynchronizeResourceResponse:
        """
        @summary Synchronizes the basic Alibaba Cloud resources that belong to your account to Enterprise Distributed Application Service (EDAS). This operation is applicable to Elastic Compute Service (ECS) clusters.
        
        @description If you call this operation to synchronize ECS resource information, all instance data is synchronized from ECS. If you have more than 100 ECS instances, we recommend that you do not frequently call this operation.
        
        @param request: SynchronizeResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SynchronizeResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SynchronizeResource',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/pop_sync_resource',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.SynchronizeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def synchronize_resource(
        self,
        request: edas_20170801_models.SynchronizeResourceRequest,
    ) -> edas_20170801_models.SynchronizeResourceResponse:
        """
        @summary Synchronizes the basic Alibaba Cloud resources that belong to your account to Enterprise Distributed Application Service (EDAS). This operation is applicable to Elastic Compute Service (ECS) clusters.
        
        @description If you call this operation to synchronize ECS resource information, all instance data is synchronized from ECS. If you have more than 100 ECS instances, we recommend that you do not frequently call this operation.
        
        @param request: SynchronizeResourceRequest
        @return: SynchronizeResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.synchronize_resource_with_options(request, headers, runtime)

    async def synchronize_resource_async(
        self,
        request: edas_20170801_models.SynchronizeResourceRequest,
    ) -> edas_20170801_models.SynchronizeResourceResponse:
        """
        @summary Synchronizes the basic Alibaba Cloud resources that belong to your account to Enterprise Distributed Application Service (EDAS). This operation is applicable to Elastic Compute Service (ECS) clusters.
        
        @description If you call this operation to synchronize ECS resource information, all instance data is synchronized from ECS. If you have more than 100 ECS instances, we recommend that you do not frequently call this operation.
        
        @param request: SynchronizeResourceRequest
        @return: SynchronizeResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.synchronize_resource_with_options_async(request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: edas_20170801_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.TagResourcesResponse:
        """
        @summary Creates tags and adds the tags to resources at a time.
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/tag/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: edas_20170801_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.TagResourcesResponse:
        """
        @summary Creates tags and adds the tags to resources at a time.
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/tag/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: edas_20170801_models.TagResourcesRequest,
    ) -> edas_20170801_models.TagResourcesResponse:
        """
        @summary Creates tags and adds the tags to resources at a time.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: edas_20170801_models.TagResourcesRequest,
    ) -> edas_20170801_models.TagResourcesResponse:
        """
        @summary Creates tags and adds the tags to resources at a time.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def transform_cluster_member_with_options(
        self,
        request: edas_20170801_models.TransformClusterMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.TransformClusterMemberResponse:
        """
        @summary Imports or migrates one or more Elastic Compute Service (ECS) instances to a cluster.
        
        @description ## Limits
        When you call this operation to import an ECS instance, the operating system of the ECS instance is reinstalled. After the operating system is reinstalled, all data of the ECS instance is deleted. You must set a logon password for the ECS instance. Make sure that no important data exists on or data has been backed up for the ECS instance that you want to import.
        
        @param request: TransformClusterMemberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransformClusterMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.target_cluster_id):
            query['TargetClusterId'] = request.target_cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransformClusterMember',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/transform_cluster_member',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.TransformClusterMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def transform_cluster_member_with_options_async(
        self,
        request: edas_20170801_models.TransformClusterMemberRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.TransformClusterMemberResponse:
        """
        @summary Imports or migrates one or more Elastic Compute Service (ECS) instances to a cluster.
        
        @description ## Limits
        When you call this operation to import an ECS instance, the operating system of the ECS instance is reinstalled. After the operating system is reinstalled, all data of the ECS instance is deleted. You must set a logon password for the ECS instance. Make sure that no important data exists on or data has been backed up for the ECS instance that you want to import.
        
        @param request: TransformClusterMemberRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TransformClusterMemberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.target_cluster_id):
            query['TargetClusterId'] = request.target_cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransformClusterMember',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/resource/transform_cluster_member',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.TransformClusterMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transform_cluster_member(
        self,
        request: edas_20170801_models.TransformClusterMemberRequest,
    ) -> edas_20170801_models.TransformClusterMemberResponse:
        """
        @summary Imports or migrates one or more Elastic Compute Service (ECS) instances to a cluster.
        
        @description ## Limits
        When you call this operation to import an ECS instance, the operating system of the ECS instance is reinstalled. After the operating system is reinstalled, all data of the ECS instance is deleted. You must set a logon password for the ECS instance. Make sure that no important data exists on or data has been backed up for the ECS instance that you want to import.
        
        @param request: TransformClusterMemberRequest
        @return: TransformClusterMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.transform_cluster_member_with_options(request, headers, runtime)

    async def transform_cluster_member_async(
        self,
        request: edas_20170801_models.TransformClusterMemberRequest,
    ) -> edas_20170801_models.TransformClusterMemberResponse:
        """
        @summary Imports or migrates one or more Elastic Compute Service (ECS) instances to a cluster.
        
        @description ## Limits
        When you call this operation to import an ECS instance, the operating system of the ECS instance is reinstalled. After the operating system is reinstalled, all data of the ECS instance is deleted. You must set a logon password for the ECS instance. Make sure that no important data exists on or data has been backed up for the ECS instance that you want to import.
        
        @param request: TransformClusterMemberRequest
        @return: TransformClusterMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.transform_cluster_member_with_options_async(request, headers, runtime)

    def unbind_k8s_slb_with_options(
        self,
        request: edas_20170801_models.UnbindK8sSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UnbindK8sSlbResponse:
        """
        @summary Unbinds a Server Load Balancer (SLB) instance from an application that is deployed in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: UnbindK8sSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindK8sSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.slb_name):
            query['SlbName'] = request.slb_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindK8sSlb',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_slb_binding',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UnbindK8sSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_k8s_slb_with_options_async(
        self,
        request: edas_20170801_models.UnbindK8sSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UnbindK8sSlbResponse:
        """
        @summary Unbinds a Server Load Balancer (SLB) instance from an application that is deployed in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: UnbindK8sSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindK8sSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.slb_name):
            query['SlbName'] = request.slb_name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindK8sSlb',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_slb_binding',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UnbindK8sSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_k8s_slb(
        self,
        request: edas_20170801_models.UnbindK8sSlbRequest,
    ) -> edas_20170801_models.UnbindK8sSlbResponse:
        """
        @summary Unbinds a Server Load Balancer (SLB) instance from an application that is deployed in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: UnbindK8sSlbRequest
        @return: UnbindK8sSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.unbind_k8s_slb_with_options(request, headers, runtime)

    async def unbind_k8s_slb_async(
        self,
        request: edas_20170801_models.UnbindK8sSlbRequest,
    ) -> edas_20170801_models.UnbindK8sSlbResponse:
        """
        @summary Unbinds a Server Load Balancer (SLB) instance from an application that is deployed in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: UnbindK8sSlbRequest
        @return: UnbindK8sSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.unbind_k8s_slb_with_options_async(request, headers, runtime)

    def unbind_slb_with_options(
        self,
        request: edas_20170801_models.UnbindSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UnbindSlbResponse:
        """
        @summary Unbinds a Server Load Balancer (SLB) instance from an application.
        
        @param request: UnbindSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.delete_listener):
            query['DeleteListener'] = request.delete_listener
        if not UtilClient.is_unset(request.slb_id):
            query['SlbId'] = request.slb_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindSlb',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/app/unbind_slb_json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UnbindSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_slb_with_options_async(
        self,
        request: edas_20170801_models.UnbindSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UnbindSlbResponse:
        """
        @summary Unbinds a Server Load Balancer (SLB) instance from an application.
        
        @param request: UnbindSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.delete_listener):
            query['DeleteListener'] = request.delete_listener
        if not UtilClient.is_unset(request.slb_id):
            query['SlbId'] = request.slb_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindSlb',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/app/unbind_slb_json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UnbindSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_slb(
        self,
        request: edas_20170801_models.UnbindSlbRequest,
    ) -> edas_20170801_models.UnbindSlbResponse:
        """
        @summary Unbinds a Server Load Balancer (SLB) instance from an application.
        
        @param request: UnbindSlbRequest
        @return: UnbindSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.unbind_slb_with_options(request, headers, runtime)

    async def unbind_slb_async(
        self,
        request: edas_20170801_models.UnbindSlbRequest,
    ) -> edas_20170801_models.UnbindSlbResponse:
        """
        @summary Unbinds a Server Load Balancer (SLB) instance from an application.
        
        @param request: UnbindSlbRequest
        @return: UnbindSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.unbind_slb_with_options_async(request, headers, runtime)

    def untag_resources_with_options(
        self,
        request: edas_20170801_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UntagResourcesResponse:
        """
        @summary Removes one or more tags from one or more resources.
        
        @param request: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_all):
            query['DeleteAll'] = request.delete_all
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/tag/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: edas_20170801_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UntagResourcesResponse:
        """
        @summary Removes one or more tags from one or more resources.
        
        @param request: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_all):
            query['DeleteAll'] = request.delete_all
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/tag/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: edas_20170801_models.UntagResourcesRequest,
    ) -> edas_20170801_models.UntagResourcesResponse:
        """
        @summary Removes one or more tags from one or more resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: edas_20170801_models.UntagResourcesRequest,
    ) -> edas_20170801_models.UntagResourcesResponse:
        """
        @summary Removes one or more tags from one or more resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_account_info_with_options(
        self,
        request: edas_20170801_models.UpdateAccountInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateAccountInfoResponse:
        """
        @summary Modifies the information about an account.
        
        @param request: UpdateAccountInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAccountInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccountInfo',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/edit_account_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_account_info_with_options_async(
        self,
        request: edas_20170801_models.UpdateAccountInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateAccountInfoResponse:
        """
        @summary Modifies the information about an account.
        
        @param request: UpdateAccountInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAccountInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.telephone):
            query['Telephone'] = request.telephone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccountInfo',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/edit_account_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateAccountInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_account_info(
        self,
        request: edas_20170801_models.UpdateAccountInfoRequest,
    ) -> edas_20170801_models.UpdateAccountInfoResponse:
        """
        @summary Modifies the information about an account.
        
        @param request: UpdateAccountInfoRequest
        @return: UpdateAccountInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_account_info_with_options(request, headers, runtime)

    async def update_account_info_async(
        self,
        request: edas_20170801_models.UpdateAccountInfoRequest,
    ) -> edas_20170801_models.UpdateAccountInfoResponse:
        """
        @summary Modifies the information about an account.
        
        @param request: UpdateAccountInfoRequest
        @return: UpdateAccountInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_account_info_with_options_async(request, headers, runtime)

    def update_application_base_info_with_options(
        self,
        request: edas_20170801_models.UpdateApplicationBaseInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateApplicationBaseInfoResponse:
        """
        @summary Modifies the name, description, and owner of an application.
        
        @param request: UpdateApplicationBaseInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationBaseInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationBaseInfo',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/update_app_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateApplicationBaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_base_info_with_options_async(
        self,
        request: edas_20170801_models.UpdateApplicationBaseInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateApplicationBaseInfoResponse:
        """
        @summary Modifies the name, description, and owner of an application.
        
        @param request: UpdateApplicationBaseInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationBaseInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationBaseInfo',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/update_app_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateApplicationBaseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_base_info(
        self,
        request: edas_20170801_models.UpdateApplicationBaseInfoRequest,
    ) -> edas_20170801_models.UpdateApplicationBaseInfoResponse:
        """
        @summary Modifies the name, description, and owner of an application.
        
        @param request: UpdateApplicationBaseInfoRequest
        @return: UpdateApplicationBaseInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_application_base_info_with_options(request, headers, runtime)

    async def update_application_base_info_async(
        self,
        request: edas_20170801_models.UpdateApplicationBaseInfoRequest,
    ) -> edas_20170801_models.UpdateApplicationBaseInfoResponse:
        """
        @summary Modifies the name, description, and owner of an application.
        
        @param request: UpdateApplicationBaseInfoRequest
        @return: UpdateApplicationBaseInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_application_base_info_with_options_async(request, headers, runtime)

    def update_application_scaling_rule_with_options(
        self,
        request: edas_20170801_models.UpdateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateApplicationScalingRuleResponse:
        """
        @summary Modifies an auto scaling policy for an application.
        
        @param request: UpdateApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_behaviour):
            query['ScalingBehaviour'] = request.scaling_behaviour
        if not UtilClient.is_unset(request.scaling_rule_enable):
            query['ScalingRuleEnable'] = request.scaling_rule_enable
        if not UtilClient.is_unset(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        if not UtilClient.is_unset(request.scaling_rule_trigger):
            query['ScalingRuleTrigger'] = request.scaling_rule_trigger
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationScalingRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v1/eam/scale/application_scaling_rule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_scaling_rule_with_options_async(
        self,
        request: edas_20170801_models.UpdateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateApplicationScalingRuleResponse:
        """
        @summary Modifies an auto scaling policy for an application.
        
        @param request: UpdateApplicationScalingRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.scaling_behaviour):
            query['ScalingBehaviour'] = request.scaling_behaviour
        if not UtilClient.is_unset(request.scaling_rule_enable):
            query['ScalingRuleEnable'] = request.scaling_rule_enable
        if not UtilClient.is_unset(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        if not UtilClient.is_unset(request.scaling_rule_trigger):
            query['ScalingRuleTrigger'] = request.scaling_rule_trigger
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationScalingRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v1/eam/scale/application_scaling_rule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_scaling_rule(
        self,
        request: edas_20170801_models.UpdateApplicationScalingRuleRequest,
    ) -> edas_20170801_models.UpdateApplicationScalingRuleResponse:
        """
        @summary Modifies an auto scaling policy for an application.
        
        @param request: UpdateApplicationScalingRuleRequest
        @return: UpdateApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_application_scaling_rule_with_options(request, headers, runtime)

    async def update_application_scaling_rule_async(
        self,
        request: edas_20170801_models.UpdateApplicationScalingRuleRequest,
    ) -> edas_20170801_models.UpdateApplicationScalingRuleResponse:
        """
        @summary Modifies an auto scaling policy for an application.
        
        @param request: UpdateApplicationScalingRuleRequest
        @return: UpdateApplicationScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_application_scaling_rule_with_options_async(request, headers, runtime)

    def update_config_template_with_options(
        self,
        request: edas_20170801_models.UpdateConfigTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateConfigTemplateResponse:
        """
        @summary Modifies a configuration template.
        
        @param request: UpdateConfigTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.format):
            body['Format'] = request.format
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigTemplate',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/config_template',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateConfigTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_template_with_options_async(
        self,
        request: edas_20170801_models.UpdateConfigTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateConfigTemplateResponse:
        """
        @summary Modifies a configuration template.
        
        @param request: UpdateConfigTemplateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConfigTemplateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.format):
            body['Format'] = request.format
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfigTemplate',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/config_template',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateConfigTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config_template(
        self,
        request: edas_20170801_models.UpdateConfigTemplateRequest,
    ) -> edas_20170801_models.UpdateConfigTemplateResponse:
        """
        @summary Modifies a configuration template.
        
        @param request: UpdateConfigTemplateRequest
        @return: UpdateConfigTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_config_template_with_options(request, headers, runtime)

    async def update_config_template_async(
        self,
        request: edas_20170801_models.UpdateConfigTemplateRequest,
    ) -> edas_20170801_models.UpdateConfigTemplateResponse:
        """
        @summary Modifies a configuration template.
        
        @param request: UpdateConfigTemplateRequest
        @return: UpdateConfigTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_config_template_with_options_async(request, headers, runtime)

    def update_container_with_options(
        self,
        request: edas_20170801_models.UpdateContainerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateContainerResponse:
        """
        @summary Updates the Enterprise Distributed Application Service (EDAS) Container version of a High-Speed Service Framework (HSF) application. EDAS Container includes Ali-Tomcat and Pandora.
        
        @param request: UpdateContainerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateContainerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateContainer',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_update_container',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateContainerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_container_with_options_async(
        self,
        request: edas_20170801_models.UpdateContainerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateContainerResponse:
        """
        @summary Updates the Enterprise Distributed Application Service (EDAS) Container version of a High-Speed Service Framework (HSF) application. EDAS Container includes Ali-Tomcat and Pandora.
        
        @param request: UpdateContainerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateContainerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateContainer',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/changeorder/co_update_container',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateContainerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_container(
        self,
        request: edas_20170801_models.UpdateContainerRequest,
    ) -> edas_20170801_models.UpdateContainerResponse:
        """
        @summary Updates the Enterprise Distributed Application Service (EDAS) Container version of a High-Speed Service Framework (HSF) application. EDAS Container includes Ali-Tomcat and Pandora.
        
        @param request: UpdateContainerRequest
        @return: UpdateContainerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_container_with_options(request, headers, runtime)

    async def update_container_async(
        self,
        request: edas_20170801_models.UpdateContainerRequest,
    ) -> edas_20170801_models.UpdateContainerResponse:
        """
        @summary Updates the Enterprise Distributed Application Service (EDAS) Container version of a High-Speed Service Framework (HSF) application. EDAS Container includes Ali-Tomcat and Pandora.
        
        @param request: UpdateContainerRequest
        @return: UpdateContainerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_container_with_options_async(request, headers, runtime)

    def update_container_configuration_with_options(
        self,
        request: edas_20170801_models.UpdateContainerConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateContainerConfigurationResponse:
        """
        @summary Configures the Tomcat container for an application or application instance group in an Elastic Compute Service (ECS) cluster.
        
        @param request: UpdateContainerConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateContainerConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.context_path):
            query['ContextPath'] = request.context_path
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.http_port):
            query['HttpPort'] = request.http_port
        if not UtilClient.is_unset(request.max_threads):
            query['MaxThreads'] = request.max_threads
        if not UtilClient.is_unset(request.uriencoding):
            query['URIEncoding'] = request.uriencoding
        if not UtilClient.is_unset(request.use_body_encoding):
            query['UseBodyEncoding'] = request.use_body_encoding
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateContainerConfiguration',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/container_config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateContainerConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_container_configuration_with_options_async(
        self,
        request: edas_20170801_models.UpdateContainerConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateContainerConfigurationResponse:
        """
        @summary Configures the Tomcat container for an application or application instance group in an Elastic Compute Service (ECS) cluster.
        
        @param request: UpdateContainerConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateContainerConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.context_path):
            query['ContextPath'] = request.context_path
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.http_port):
            query['HttpPort'] = request.http_port
        if not UtilClient.is_unset(request.max_threads):
            query['MaxThreads'] = request.max_threads
        if not UtilClient.is_unset(request.uriencoding):
            query['URIEncoding'] = request.uriencoding
        if not UtilClient.is_unset(request.use_body_encoding):
            query['UseBodyEncoding'] = request.use_body_encoding
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateContainerConfiguration',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/container_config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateContainerConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_container_configuration(
        self,
        request: edas_20170801_models.UpdateContainerConfigurationRequest,
    ) -> edas_20170801_models.UpdateContainerConfigurationResponse:
        """
        @summary Configures the Tomcat container for an application or application instance group in an Elastic Compute Service (ECS) cluster.
        
        @param request: UpdateContainerConfigurationRequest
        @return: UpdateContainerConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_container_configuration_with_options(request, headers, runtime)

    async def update_container_configuration_async(
        self,
        request: edas_20170801_models.UpdateContainerConfigurationRequest,
    ) -> edas_20170801_models.UpdateContainerConfigurationResponse:
        """
        @summary Configures the Tomcat container for an application or application instance group in an Elastic Compute Service (ECS) cluster.
        
        @param request: UpdateContainerConfigurationRequest
        @return: UpdateContainerConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_container_configuration_with_options_async(request, headers, runtime)

    def update_health_check_url_with_options(
        self,
        request: edas_20170801_models.UpdateHealthCheckUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateHealthCheckUrlResponse:
        """
        @summary Changes the health check URL for an application.
        
        @param request: UpdateHealthCheckUrlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHealthCheckUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.hc_url):
            query['hcURL'] = request.hc_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHealthCheckUrl',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/modify_hc_url',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateHealthCheckUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_health_check_url_with_options_async(
        self,
        request: edas_20170801_models.UpdateHealthCheckUrlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateHealthCheckUrlResponse:
        """
        @summary Changes the health check URL for an application.
        
        @param request: UpdateHealthCheckUrlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHealthCheckUrlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.hc_url):
            query['hcURL'] = request.hc_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHealthCheckUrl',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/modify_hc_url',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateHealthCheckUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_health_check_url(
        self,
        request: edas_20170801_models.UpdateHealthCheckUrlRequest,
    ) -> edas_20170801_models.UpdateHealthCheckUrlResponse:
        """
        @summary Changes the health check URL for an application.
        
        @param request: UpdateHealthCheckUrlRequest
        @return: UpdateHealthCheckUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_health_check_url_with_options(request, headers, runtime)

    async def update_health_check_url_async(
        self,
        request: edas_20170801_models.UpdateHealthCheckUrlRequest,
    ) -> edas_20170801_models.UpdateHealthCheckUrlResponse:
        """
        @summary Changes the health check URL for an application.
        
        @param request: UpdateHealthCheckUrlRequest
        @return: UpdateHealthCheckUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_health_check_url_with_options_async(request, headers, runtime)

    def update_hook_configuration_with_options(
        self,
        request: edas_20170801_models.UpdateHookConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateHookConfigurationResponse:
        """
        @summary Mounts a script to an application or application instance group.
        
        @param request: UpdateHookConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHookConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.hooks):
            query['Hooks'] = request.hooks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHookConfiguration',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/app/config_app_hook_json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateHookConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hook_configuration_with_options_async(
        self,
        request: edas_20170801_models.UpdateHookConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateHookConfigurationResponse:
        """
        @summary Mounts a script to an application or application instance group.
        
        @param request: UpdateHookConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHookConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.hooks):
            query['Hooks'] = request.hooks
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHookConfiguration',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/app/config_app_hook_json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateHookConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_hook_configuration(
        self,
        request: edas_20170801_models.UpdateHookConfigurationRequest,
    ) -> edas_20170801_models.UpdateHookConfigurationResponse:
        """
        @summary Mounts a script to an application or application instance group.
        
        @param request: UpdateHookConfigurationRequest
        @return: UpdateHookConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_hook_configuration_with_options(request, headers, runtime)

    async def update_hook_configuration_async(
        self,
        request: edas_20170801_models.UpdateHookConfigurationRequest,
    ) -> edas_20170801_models.UpdateHookConfigurationResponse:
        """
        @summary Mounts a script to an application or application instance group.
        
        @param request: UpdateHookConfigurationRequest
        @return: UpdateHookConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_hook_configuration_with_options_async(request, headers, runtime)

    def update_jvm_configuration_with_options(
        self,
        request: edas_20170801_models.UpdateJvmConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateJvmConfigurationResponse:
        """
        @summary Configures the Java virtual machine (JVM) parameters for an application or an instance group where the application is deployed.
        
        @param request: UpdateJvmConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateJvmConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.max_heap_size):
            query['MaxHeapSize'] = request.max_heap_size
        if not UtilClient.is_unset(request.max_perm_size):
            query['MaxPermSize'] = request.max_perm_size
        if not UtilClient.is_unset(request.min_heap_size):
            query['MinHeapSize'] = request.min_heap_size
        if not UtilClient.is_unset(request.options):
            query['Options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateJvmConfiguration',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/app_jvm_config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateJvmConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_jvm_configuration_with_options_async(
        self,
        request: edas_20170801_models.UpdateJvmConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateJvmConfigurationResponse:
        """
        @summary Configures the Java virtual machine (JVM) parameters for an application or an instance group where the application is deployed.
        
        @param request: UpdateJvmConfigurationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateJvmConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.max_heap_size):
            query['MaxHeapSize'] = request.max_heap_size
        if not UtilClient.is_unset(request.max_perm_size):
            query['MaxPermSize'] = request.max_perm_size
        if not UtilClient.is_unset(request.min_heap_size):
            query['MinHeapSize'] = request.min_heap_size
        if not UtilClient.is_unset(request.options):
            query['Options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateJvmConfiguration',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/app/app_jvm_config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateJvmConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_jvm_configuration(
        self,
        request: edas_20170801_models.UpdateJvmConfigurationRequest,
    ) -> edas_20170801_models.UpdateJvmConfigurationResponse:
        """
        @summary Configures the Java virtual machine (JVM) parameters for an application or an instance group where the application is deployed.
        
        @param request: UpdateJvmConfigurationRequest
        @return: UpdateJvmConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_jvm_configuration_with_options(request, headers, runtime)

    async def update_jvm_configuration_async(
        self,
        request: edas_20170801_models.UpdateJvmConfigurationRequest,
    ) -> edas_20170801_models.UpdateJvmConfigurationResponse:
        """
        @summary Configures the Java virtual machine (JVM) parameters for an application or an instance group where the application is deployed.
        
        @param request: UpdateJvmConfigurationRequest
        @return: UpdateJvmConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_jvm_configuration_with_options_async(request, headers, runtime)

    def update_k8s_application_base_info_with_options(
        self,
        request: edas_20170801_models.UpdateK8sApplicationBaseInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateK8sApplicationBaseInfoResponse:
        """
        @summary Modifies basic information about an application that is deployed in a Kubernetes cluster.
        
        @param request: UpdateK8sApplicationBaseInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sApplicationBaseInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateK8sApplicationBaseInfo',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/oam/update_app_basic_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateK8sApplicationBaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_application_base_info_with_options_async(
        self,
        request: edas_20170801_models.UpdateK8sApplicationBaseInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateK8sApplicationBaseInfoResponse:
        """
        @summary Modifies basic information about an application that is deployed in a Kubernetes cluster.
        
        @param request: UpdateK8sApplicationBaseInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sApplicationBaseInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateK8sApplicationBaseInfo',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/oam/update_app_basic_info',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateK8sApplicationBaseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_application_base_info(
        self,
        request: edas_20170801_models.UpdateK8sApplicationBaseInfoRequest,
    ) -> edas_20170801_models.UpdateK8sApplicationBaseInfoResponse:
        """
        @summary Modifies basic information about an application that is deployed in a Kubernetes cluster.
        
        @param request: UpdateK8sApplicationBaseInfoRequest
        @return: UpdateK8sApplicationBaseInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_k8s_application_base_info_with_options(request, headers, runtime)

    async def update_k8s_application_base_info_async(
        self,
        request: edas_20170801_models.UpdateK8sApplicationBaseInfoRequest,
    ) -> edas_20170801_models.UpdateK8sApplicationBaseInfoResponse:
        """
        @summary Modifies basic information about an application that is deployed in a Kubernetes cluster.
        
        @param request: UpdateK8sApplicationBaseInfoRequest
        @return: UpdateK8sApplicationBaseInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_k8s_application_base_info_with_options_async(request, headers, runtime)

    def update_k8s_application_config_with_options(
        self,
        request: edas_20170801_models.UpdateK8sApplicationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateK8sApplicationConfigResponse:
        """
        @summary Updates the configuration of an application in a Container Service for Kubernetes (ACK) or Serverless Kubernetes cluster.
        
        @param request: UpdateK8sApplicationConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sApplicationConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cpu_limit):
            query['CpuLimit'] = request.cpu_limit
        if not UtilClient.is_unset(request.cpu_request):
            query['CpuRequest'] = request.cpu_request
        if not UtilClient.is_unset(request.ephemeral_storage_limit):
            query['EphemeralStorageLimit'] = request.ephemeral_storage_limit
        if not UtilClient.is_unset(request.ephemeral_storage_request):
            query['EphemeralStorageRequest'] = request.ephemeral_storage_request
        if not UtilClient.is_unset(request.mcpu_limit):
            query['McpuLimit'] = request.mcpu_limit
        if not UtilClient.is_unset(request.mcpu_request):
            query['McpuRequest'] = request.mcpu_request
        if not UtilClient.is_unset(request.memory_limit):
            query['MemoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.memory_request):
            query['MemoryRequest'] = request.memory_request
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateK8sApplicationConfig',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_app_configuration',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateK8sApplicationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_application_config_with_options_async(
        self,
        request: edas_20170801_models.UpdateK8sApplicationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateK8sApplicationConfigResponse:
        """
        @summary Updates the configuration of an application in a Container Service for Kubernetes (ACK) or Serverless Kubernetes cluster.
        
        @param request: UpdateK8sApplicationConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sApplicationConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cpu_limit):
            query['CpuLimit'] = request.cpu_limit
        if not UtilClient.is_unset(request.cpu_request):
            query['CpuRequest'] = request.cpu_request
        if not UtilClient.is_unset(request.ephemeral_storage_limit):
            query['EphemeralStorageLimit'] = request.ephemeral_storage_limit
        if not UtilClient.is_unset(request.ephemeral_storage_request):
            query['EphemeralStorageRequest'] = request.ephemeral_storage_request
        if not UtilClient.is_unset(request.mcpu_limit):
            query['McpuLimit'] = request.mcpu_limit
        if not UtilClient.is_unset(request.mcpu_request):
            query['McpuRequest'] = request.mcpu_request
        if not UtilClient.is_unset(request.memory_limit):
            query['MemoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.memory_request):
            query['MemoryRequest'] = request.memory_request
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateK8sApplicationConfig',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_app_configuration',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateK8sApplicationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_application_config(
        self,
        request: edas_20170801_models.UpdateK8sApplicationConfigRequest,
    ) -> edas_20170801_models.UpdateK8sApplicationConfigResponse:
        """
        @summary Updates the configuration of an application in a Container Service for Kubernetes (ACK) or Serverless Kubernetes cluster.
        
        @param request: UpdateK8sApplicationConfigRequest
        @return: UpdateK8sApplicationConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_k8s_application_config_with_options(request, headers, runtime)

    async def update_k8s_application_config_async(
        self,
        request: edas_20170801_models.UpdateK8sApplicationConfigRequest,
    ) -> edas_20170801_models.UpdateK8sApplicationConfigResponse:
        """
        @summary Updates the configuration of an application in a Container Service for Kubernetes (ACK) or Serverless Kubernetes cluster.
        
        @param request: UpdateK8sApplicationConfigRequest
        @return: UpdateK8sApplicationConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_k8s_application_config_with_options_async(request, headers, runtime)

    def update_k8s_config_map_with_options(
        self,
        request: edas_20170801_models.UpdateK8sConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateK8sConfigMapResponse:
        """
        @summary Modifies a Kubernetes ConfigMap.
        
        @param request: UpdateK8sConfigMapRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sConfigMapResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateK8sConfigMap',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_config_map',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateK8sConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_config_map_with_options_async(
        self,
        request: edas_20170801_models.UpdateK8sConfigMapRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateK8sConfigMapResponse:
        """
        @summary Modifies a Kubernetes ConfigMap.
        
        @param request: UpdateK8sConfigMapRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sConfigMapResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateK8sConfigMap',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_config_map',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateK8sConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_config_map(
        self,
        request: edas_20170801_models.UpdateK8sConfigMapRequest,
    ) -> edas_20170801_models.UpdateK8sConfigMapResponse:
        """
        @summary Modifies a Kubernetes ConfigMap.
        
        @param request: UpdateK8sConfigMapRequest
        @return: UpdateK8sConfigMapResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_k8s_config_map_with_options(request, headers, runtime)

    async def update_k8s_config_map_async(
        self,
        request: edas_20170801_models.UpdateK8sConfigMapRequest,
    ) -> edas_20170801_models.UpdateK8sConfigMapResponse:
        """
        @summary Modifies a Kubernetes ConfigMap.
        
        @param request: UpdateK8sConfigMapRequest
        @return: UpdateK8sConfigMapResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_k8s_config_map_with_options_async(request, headers, runtime)

    def update_k8s_ingress_rule_with_options(
        self,
        request: edas_20170801_models.UpdateK8sIngressRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateK8sIngressRuleResponse:
        """
        @summary Updates an ingress.
        
        @param request: UpdateK8sIngressRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sIngressRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ingress_conf):
            query['IngressConf'] = request.ingress_conf
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateK8sIngressRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_ingress',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateK8sIngressRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_ingress_rule_with_options_async(
        self,
        request: edas_20170801_models.UpdateK8sIngressRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateK8sIngressRuleResponse:
        """
        @summary Updates an ingress.
        
        @param request: UpdateK8sIngressRuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sIngressRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ingress_conf):
            query['IngressConf'] = request.ingress_conf
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateK8sIngressRule',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_ingress',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateK8sIngressRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_ingress_rule(
        self,
        request: edas_20170801_models.UpdateK8sIngressRuleRequest,
    ) -> edas_20170801_models.UpdateK8sIngressRuleResponse:
        """
        @summary Updates an ingress.
        
        @param request: UpdateK8sIngressRuleRequest
        @return: UpdateK8sIngressRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_k8s_ingress_rule_with_options(request, headers, runtime)

    async def update_k8s_ingress_rule_async(
        self,
        request: edas_20170801_models.UpdateK8sIngressRuleRequest,
    ) -> edas_20170801_models.UpdateK8sIngressRuleResponse:
        """
        @summary Updates an ingress.
        
        @param request: UpdateK8sIngressRuleRequest
        @return: UpdateK8sIngressRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_k8s_ingress_rule_with_options_async(request, headers, runtime)

    def update_k8s_resource_with_options(
        self,
        request: edas_20170801_models.UpdateK8sResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateK8sResourceResponse:
        """
        @summary Updates a specified resource in a Kubernetes cluster.
        
        @description > You can update only Deployments.
        
        @param request: UpdateK8sResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.resource_content):
            body['ResourceContent'] = request.resource_content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateK8sResource',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/oam/update_k8s_resource_config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateK8sResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_resource_with_options_async(
        self,
        request: edas_20170801_models.UpdateK8sResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateK8sResourceResponse:
        """
        @summary Updates a specified resource in a Kubernetes cluster.
        
        @description > You can update only Deployments.
        
        @param request: UpdateK8sResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.resource_content):
            body['ResourceContent'] = request.resource_content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateK8sResource',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/oam/update_k8s_resource_config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateK8sResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_resource(
        self,
        request: edas_20170801_models.UpdateK8sResourceRequest,
    ) -> edas_20170801_models.UpdateK8sResourceResponse:
        """
        @summary Updates a specified resource in a Kubernetes cluster.
        
        @description > You can update only Deployments.
        
        @param request: UpdateK8sResourceRequest
        @return: UpdateK8sResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_k8s_resource_with_options(request, headers, runtime)

    async def update_k8s_resource_async(
        self,
        request: edas_20170801_models.UpdateK8sResourceRequest,
    ) -> edas_20170801_models.UpdateK8sResourceResponse:
        """
        @summary Updates a specified resource in a Kubernetes cluster.
        
        @description > You can update only Deployments.
        
        @param request: UpdateK8sResourceRequest
        @return: UpdateK8sResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_k8s_resource_with_options_async(request, headers, runtime)

    def update_k8s_secret_with_options(
        self,
        request: edas_20170801_models.UpdateK8sSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateK8sSecretResponse:
        """
        @summary Modifies a Kubernetes Secret.
        
        @param request: UpdateK8sSecretRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sSecretResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_64encoded):
            body['Base64Encoded'] = request.base_64encoded
        if not UtilClient.is_unset(request.cert_id):
            body['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_region_id):
            body['CertRegionId'] = request.cert_region_id
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateK8sSecret',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_secret',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateK8sSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_secret_with_options_async(
        self,
        request: edas_20170801_models.UpdateK8sSecretRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateK8sSecretResponse:
        """
        @summary Modifies a Kubernetes Secret.
        
        @param request: UpdateK8sSecretRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sSecretResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_64encoded):
            body['Base64Encoded'] = request.base_64encoded
        if not UtilClient.is_unset(request.cert_id):
            body['CertId'] = request.cert_id
        if not UtilClient.is_unset(request.cert_region_id):
            body['CertRegionId'] = request.cert_region_id
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateK8sSecret',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_secret',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateK8sSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_secret(
        self,
        request: edas_20170801_models.UpdateK8sSecretRequest,
    ) -> edas_20170801_models.UpdateK8sSecretResponse:
        """
        @summary Modifies a Kubernetes Secret.
        
        @param request: UpdateK8sSecretRequest
        @return: UpdateK8sSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_k8s_secret_with_options(request, headers, runtime)

    async def update_k8s_secret_async(
        self,
        request: edas_20170801_models.UpdateK8sSecretRequest,
    ) -> edas_20170801_models.UpdateK8sSecretResponse:
        """
        @summary Modifies a Kubernetes Secret.
        
        @param request: UpdateK8sSecretRequest
        @return: UpdateK8sSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_k8s_secret_with_options_async(request, headers, runtime)

    def update_k8s_service_with_options(
        self,
        request: edas_20170801_models.UpdateK8sServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateK8sServiceResponse:
        """
        @summary Updates an application service in a Kubernetes cluster.
        
        @param request: UpdateK8sServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.external_traffic_policy):
            query['ExternalTrafficPolicy'] = request.external_traffic_policy
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.service_ports):
            query['ServicePorts'] = request.service_ports
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateK8sService',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_service',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateK8sServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_service_with_options_async(
        self,
        request: edas_20170801_models.UpdateK8sServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateK8sServiceResponse:
        """
        @summary Updates an application service in a Kubernetes cluster.
        
        @param request: UpdateK8sServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.external_traffic_policy):
            query['ExternalTrafficPolicy'] = request.external_traffic_policy
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.service_ports):
            query['ServicePorts'] = request.service_ports
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateK8sService',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_service',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateK8sServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_service(
        self,
        request: edas_20170801_models.UpdateK8sServiceRequest,
    ) -> edas_20170801_models.UpdateK8sServiceResponse:
        """
        @summary Updates an application service in a Kubernetes cluster.
        
        @param request: UpdateK8sServiceRequest
        @return: UpdateK8sServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_k8s_service_with_options(request, headers, runtime)

    async def update_k8s_service_async(
        self,
        request: edas_20170801_models.UpdateK8sServiceRequest,
    ) -> edas_20170801_models.UpdateK8sServiceResponse:
        """
        @summary Updates an application service in a Kubernetes cluster.
        
        @param request: UpdateK8sServiceRequest
        @return: UpdateK8sServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_k8s_service_with_options_async(request, headers, runtime)

    def update_k8s_slb_with_options(
        self,
        request: edas_20170801_models.UpdateK8sSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateK8sSlbResponse:
        """
        @summary Updates the Server Load Balancer (SLB) instance bound to an application that is deployed in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: UpdateK8sSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.disable_force_override):
            query['DisableForceOverride'] = request.disable_force_override
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.service_port_infos):
            query['ServicePortInfos'] = request.service_port_infos
        if not UtilClient.is_unset(request.slb_name):
            query['SlbName'] = request.slb_name
        if not UtilClient.is_unset(request.slb_protocol):
            query['SlbProtocol'] = request.slb_protocol
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.target_port):
            query['TargetPort'] = request.target_port
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateK8sSlb',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_slb_binding',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateK8sSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_slb_with_options_async(
        self,
        request: edas_20170801_models.UpdateK8sSlbRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateK8sSlbResponse:
        """
        @summary Updates the Server Load Balancer (SLB) instance bound to an application that is deployed in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: UpdateK8sSlbRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sSlbResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.disable_force_override):
            query['DisableForceOverride'] = request.disable_force_override
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.service_port_infos):
            query['ServicePortInfos'] = request.service_port_infos
        if not UtilClient.is_unset(request.slb_name):
            query['SlbName'] = request.slb_name
        if not UtilClient.is_unset(request.slb_protocol):
            query['SlbProtocol'] = request.slb_protocol
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.target_port):
            query['TargetPort'] = request.target_port
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateK8sSlb',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/acs/k8s_slb_binding',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateK8sSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_slb(
        self,
        request: edas_20170801_models.UpdateK8sSlbRequest,
    ) -> edas_20170801_models.UpdateK8sSlbResponse:
        """
        @summary Updates the Server Load Balancer (SLB) instance bound to an application that is deployed in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: UpdateK8sSlbRequest
        @return: UpdateK8sSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_k8s_slb_with_options(request, headers, runtime)

    async def update_k8s_slb_async(
        self,
        request: edas_20170801_models.UpdateK8sSlbRequest,
    ) -> edas_20170801_models.UpdateK8sSlbResponse:
        """
        @summary Updates the Server Load Balancer (SLB) instance bound to an application that is deployed in a Container Service for Kubernetes (ACK) cluster.
        
        @param request: UpdateK8sSlbRequest
        @return: UpdateK8sSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_k8s_slb_with_options_async(request, headers, runtime)

    def update_locality_setting_with_options(
        self,
        request: edas_20170801_models.UpdateLocalitySettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateLocalitySettingResponse:
        """
        @summary 更新本地设置
        
        @param request: UpdateLocalitySettingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLocalitySettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLocalitySetting',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/sp/applications/locality/setting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateLocalitySettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_locality_setting_with_options_async(
        self,
        request: edas_20170801_models.UpdateLocalitySettingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateLocalitySettingResponse:
        """
        @summary 更新本地设置
        
        @param request: UpdateLocalitySettingRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLocalitySettingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLocalitySetting',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/sp/applications/locality/setting',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateLocalitySettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_locality_setting(
        self,
        request: edas_20170801_models.UpdateLocalitySettingRequest,
    ) -> edas_20170801_models.UpdateLocalitySettingResponse:
        """
        @summary 更新本地设置
        
        @param request: UpdateLocalitySettingRequest
        @return: UpdateLocalitySettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_locality_setting_with_options(request, headers, runtime)

    async def update_locality_setting_async(
        self,
        request: edas_20170801_models.UpdateLocalitySettingRequest,
    ) -> edas_20170801_models.UpdateLocalitySettingResponse:
        """
        @summary 更新本地设置
        
        @param request: UpdateLocalitySettingRequest
        @return: UpdateLocalitySettingResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_locality_setting_with_options_async(request, headers, runtime)

    def update_role_with_options(
        self,
        request: edas_20170801_models.UpdateRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateRoleResponse:
        """
        @summary Modifies a role.
        
        @param request: UpdateRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_data):
            query['ActionData'] = request.action_data
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRole',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/edit_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_role_with_options_async(
        self,
        request: edas_20170801_models.UpdateRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateRoleResponse:
        """
        @summary Modifies a role.
        
        @param request: UpdateRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_data):
            query['ActionData'] = request.action_data
        if not UtilClient.is_unset(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRole',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/account/edit_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_role(
        self,
        request: edas_20170801_models.UpdateRoleRequest,
    ) -> edas_20170801_models.UpdateRoleResponse:
        """
        @summary Modifies a role.
        
        @param request: UpdateRoleRequest
        @return: UpdateRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_role_with_options(request, headers, runtime)

    async def update_role_async(
        self,
        request: edas_20170801_models.UpdateRoleRequest,
    ) -> edas_20170801_models.UpdateRoleResponse:
        """
        @summary Modifies a role.
        
        @param request: UpdateRoleRequest
        @return: UpdateRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_role_with_options_async(request, headers, runtime)

    def update_sls_log_store_with_options(
        self,
        request: edas_20170801_models.UpdateSlsLogStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateSlsLogStoreResponse:
        """
        @summary Configures a Logstore for an application.
        
        @param request: UpdateSlsLogStoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSlsLogStoreResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.configs):
            body['Configs'] = request.configs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSlsLogStore',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/sls/update_sls_log_store',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateSlsLogStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sls_log_store_with_options_async(
        self,
        request: edas_20170801_models.UpdateSlsLogStoreRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateSlsLogStoreResponse:
        """
        @summary Configures a Logstore for an application.
        
        @param request: UpdateSlsLogStoreRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSlsLogStoreResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.configs):
            body['Configs'] = request.configs
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSlsLogStore',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/k8s/sls/update_sls_log_store',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateSlsLogStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sls_log_store(
        self,
        request: edas_20170801_models.UpdateSlsLogStoreRequest,
    ) -> edas_20170801_models.UpdateSlsLogStoreResponse:
        """
        @summary Configures a Logstore for an application.
        
        @param request: UpdateSlsLogStoreRequest
        @return: UpdateSlsLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_sls_log_store_with_options(request, headers, runtime)

    async def update_sls_log_store_async(
        self,
        request: edas_20170801_models.UpdateSlsLogStoreRequest,
    ) -> edas_20170801_models.UpdateSlsLogStoreResponse:
        """
        @summary Configures a Logstore for an application.
        
        @param request: UpdateSlsLogStoreRequest
        @return: UpdateSlsLogStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_sls_log_store_with_options_async(request, headers, runtime)

    def update_swimming_lane_with_options(
        self,
        request: edas_20170801_models.UpdateSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateSwimmingLaneResponse:
        """
        @summary 更新泳道
        
        @param request: UpdateSwimmingLaneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSwimmingLaneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_infos):
            query['AppInfos'] = request.app_infos
        if not UtilClient.is_unset(request.enable_rules):
            query['EnableRules'] = request.enable_rules
        if not UtilClient.is_unset(request.entry_rules):
            query['EntryRules'] = request.entry_rules
        if not UtilClient.is_unset(request.lane_id):
            query['LaneId'] = request.lane_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSwimmingLane',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/trafficmgnt/swimming_lanes',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateSwimmingLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_swimming_lane_with_options_async(
        self,
        request: edas_20170801_models.UpdateSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateSwimmingLaneResponse:
        """
        @summary 更新泳道
        
        @param request: UpdateSwimmingLaneRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSwimmingLaneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_infos):
            query['AppInfos'] = request.app_infos
        if not UtilClient.is_unset(request.enable_rules):
            query['EnableRules'] = request.enable_rules
        if not UtilClient.is_unset(request.entry_rules):
            query['EntryRules'] = request.entry_rules
        if not UtilClient.is_unset(request.lane_id):
            query['LaneId'] = request.lane_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSwimmingLane',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/trafficmgnt/swimming_lanes',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateSwimmingLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_swimming_lane(
        self,
        request: edas_20170801_models.UpdateSwimmingLaneRequest,
    ) -> edas_20170801_models.UpdateSwimmingLaneResponse:
        """
        @summary 更新泳道
        
        @param request: UpdateSwimmingLaneRequest
        @return: UpdateSwimmingLaneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_swimming_lane_with_options(request, headers, runtime)

    async def update_swimming_lane_async(
        self,
        request: edas_20170801_models.UpdateSwimmingLaneRequest,
    ) -> edas_20170801_models.UpdateSwimmingLaneResponse:
        """
        @summary 更新泳道
        
        @param request: UpdateSwimmingLaneRequest
        @return: UpdateSwimmingLaneResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_swimming_lane_with_options_async(request, headers, runtime)

    def update_swimming_lane_group_with_options(
        self,
        request: edas_20170801_models.UpdateSwimmingLaneGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateSwimmingLaneGroupResponse:
        """
        @summary Updates a lane group.
        
        @param request: UpdateSwimmingLaneGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSwimmingLaneGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.entry_app):
            query['EntryApp'] = request.entry_app
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSwimmingLaneGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/trafficmgnt/swimming_lane_groups',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateSwimmingLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_swimming_lane_group_with_options_async(
        self,
        request: edas_20170801_models.UpdateSwimmingLaneGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> edas_20170801_models.UpdateSwimmingLaneGroupResponse:
        """
        @summary Updates a lane group.
        
        @param request: UpdateSwimmingLaneGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSwimmingLaneGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.entry_app):
            query['EntryApp'] = request.entry_app
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSwimmingLaneGroup',
            version='2017-08-01',
            protocol='HTTPS',
            pathname=f'/pop/v5/trafficmgnt/swimming_lane_groups',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            edas_20170801_models.UpdateSwimmingLaneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_swimming_lane_group(
        self,
        request: edas_20170801_models.UpdateSwimmingLaneGroupRequest,
    ) -> edas_20170801_models.UpdateSwimmingLaneGroupResponse:
        """
        @summary Updates a lane group.
        
        @param request: UpdateSwimmingLaneGroupRequest
        @return: UpdateSwimmingLaneGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_swimming_lane_group_with_options(request, headers, runtime)

    async def update_swimming_lane_group_async(
        self,
        request: edas_20170801_models.UpdateSwimmingLaneGroupRequest,
    ) -> edas_20170801_models.UpdateSwimmingLaneGroupResponse:
        """
        @summary Updates a lane group.
        
        @param request: UpdateSwimmingLaneGroupRequest
        @return: UpdateSwimmingLaneGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_swimming_lane_group_with_options_async(request, headers, runtime)
