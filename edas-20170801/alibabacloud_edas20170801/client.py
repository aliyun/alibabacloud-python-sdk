# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_edas20170801 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def abort_and_rollback_change_order_with_options(
        self,
        request: main_models.AbortAndRollbackChangeOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AbortAndRollbackChangeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AbortAndRollbackChangeOrder',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/change_order_abort_and_rollback',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AbortAndRollbackChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def abort_and_rollback_change_order_with_options_async(
        self,
        request: main_models.AbortAndRollbackChangeOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AbortAndRollbackChangeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AbortAndRollbackChangeOrder',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/change_order_abort_and_rollback',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AbortAndRollbackChangeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abort_and_rollback_change_order(
        self,
        request: main_models.AbortAndRollbackChangeOrderRequest,
    ) -> main_models.AbortAndRollbackChangeOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.abort_and_rollback_change_order_with_options(request, headers, runtime)

    async def abort_and_rollback_change_order_async(
        self,
        request: main_models.AbortAndRollbackChangeOrderRequest,
    ) -> main_models.AbortAndRollbackChangeOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.abort_and_rollback_change_order_with_options_async(request, headers, runtime)

    def abort_change_order_with_options(
        self,
        request: main_models.AbortChangeOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AbortChangeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AbortChangeOrder',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/change_order_abort',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AbortChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def abort_change_order_with_options_async(
        self,
        request: main_models.AbortChangeOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AbortChangeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AbortChangeOrder',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/change_order_abort',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AbortChangeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def abort_change_order(
        self,
        request: main_models.AbortChangeOrderRequest,
    ) -> main_models.AbortChangeOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.abort_change_order_with_options(request, headers, runtime)

    async def abort_change_order_async(
        self,
        request: main_models.AbortChangeOrderRequest,
    ) -> main_models.AbortChangeOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.abort_change_order_with_options_async(request, headers, runtime)

    def add_log_path_with_options(
        self,
        request: main_models.AddLogPathRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddLogPathResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddLogPath',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/log/popListLogDirs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddLogPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_log_path_with_options_async(
        self,
        request: main_models.AddLogPathRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddLogPathResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddLogPath',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/log/popListLogDirs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddLogPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_log_path(
        self,
        request: main_models.AddLogPathRequest,
    ) -> main_models.AddLogPathResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_log_path_with_options(request, headers, runtime)

    async def add_log_path_async(
        self,
        request: main_models.AddLogPathRequest,
    ) -> main_models.AddLogPathResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_log_path_with_options_async(request, headers, runtime)

    def authorize_application_with_options(
        self,
        request: main_models.AuthorizeApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/authorize_app',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_application_with_options_async(
        self,
        request: main_models.AuthorizeApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/authorize_app',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_application(
        self,
        request: main_models.AuthorizeApplicationRequest,
    ) -> main_models.AuthorizeApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.authorize_application_with_options(request, headers, runtime)

    async def authorize_application_async(
        self,
        request: main_models.AuthorizeApplicationRequest,
    ) -> main_models.AuthorizeApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.authorize_application_with_options_async(request, headers, runtime)

    def authorize_resource_group_with_options(
        self,
        request: main_models.AuthorizeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeResourceGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/authorize_res_group',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_resource_group_with_options_async(
        self,
        request: main_models.AuthorizeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeResourceGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/authorize_res_group',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_resource_group(
        self,
        request: main_models.AuthorizeResourceGroupRequest,
    ) -> main_models.AuthorizeResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.authorize_resource_group_with_options(request, headers, runtime)

    async def authorize_resource_group_async(
        self,
        request: main_models.AuthorizeResourceGroupRequest,
    ) -> main_models.AuthorizeResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.authorize_resource_group_with_options_async(request, headers, runtime)

    def authorize_role_with_options(
        self,
        request: main_models.AuthorizeRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_ids):
            query['RoleIds'] = request.role_ids
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeRole',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/authorize_role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_role_with_options_async(
        self,
        request: main_models.AuthorizeRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_ids):
            query['RoleIds'] = request.role_ids
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeRole',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/authorize_role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_role(
        self,
        request: main_models.AuthorizeRoleRequest,
    ) -> main_models.AuthorizeRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.authorize_role_with_options(request, headers, runtime)

    async def authorize_role_async(
        self,
        request: main_models.AuthorizeRoleRequest,
    ) -> main_models.AuthorizeRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.authorize_role_with_options_async(request, headers, runtime)

    def bind_ecs_slb_with_options(
        self,
        request: main_models.BindEcsSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindEcsSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.deploy_group_id):
            query['DeployGroupId'] = request.deploy_group_id
        if not DaraCore.is_null(request.listener_health_check_url):
            query['ListenerHealthCheckUrl'] = request.listener_health_check_url
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not DaraCore.is_null(request.slb_id):
            query['SlbId'] = request.slb_id
        if not DaraCore.is_null(request.vforwarding_url_rule):
            query['VForwardingUrlRule'] = request.vforwarding_url_rule
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.vserver_group_name):
            query['VServerGroupName'] = request.vserver_group_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindEcsSlb',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/slb/bind_slb',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindEcsSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_ecs_slb_with_options_async(
        self,
        request: main_models.BindEcsSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindEcsSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.deploy_group_id):
            query['DeployGroupId'] = request.deploy_group_id
        if not DaraCore.is_null(request.listener_health_check_url):
            query['ListenerHealthCheckUrl'] = request.listener_health_check_url
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not DaraCore.is_null(request.slb_id):
            query['SlbId'] = request.slb_id
        if not DaraCore.is_null(request.vforwarding_url_rule):
            query['VForwardingUrlRule'] = request.vforwarding_url_rule
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not DaraCore.is_null(request.vserver_group_name):
            query['VServerGroupName'] = request.vserver_group_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindEcsSlb',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/slb/bind_slb',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindEcsSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_ecs_slb(
        self,
        request: main_models.BindEcsSlbRequest,
    ) -> main_models.BindEcsSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.bind_ecs_slb_with_options(request, headers, runtime)

    async def bind_ecs_slb_async(
        self,
        request: main_models.BindEcsSlbRequest,
    ) -> main_models.BindEcsSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.bind_ecs_slb_with_options_async(request, headers, runtime)

    def bind_k8s_slb_with_options(
        self,
        request: main_models.BindK8sSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindK8sSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.service_port_infos):
            query['ServicePortInfos'] = request.service_port_infos
        if not DaraCore.is_null(request.slb_id):
            query['SlbId'] = request.slb_id
        if not DaraCore.is_null(request.slb_protocol):
            query['SlbProtocol'] = request.slb_protocol
        if not DaraCore.is_null(request.specification):
            query['Specification'] = request.specification
        if not DaraCore.is_null(request.target_port):
            query['TargetPort'] = request.target_port
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindK8sSlb',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_slb_binding',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindK8sSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_k8s_slb_with_options_async(
        self,
        request: main_models.BindK8sSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindK8sSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.service_port_infos):
            query['ServicePortInfos'] = request.service_port_infos
        if not DaraCore.is_null(request.slb_id):
            query['SlbId'] = request.slb_id
        if not DaraCore.is_null(request.slb_protocol):
            query['SlbProtocol'] = request.slb_protocol
        if not DaraCore.is_null(request.specification):
            query['Specification'] = request.specification
        if not DaraCore.is_null(request.target_port):
            query['TargetPort'] = request.target_port
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindK8sSlb',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_slb_binding',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindK8sSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_k8s_slb(
        self,
        request: main_models.BindK8sSlbRequest,
    ) -> main_models.BindK8sSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.bind_k8s_slb_with_options(request, headers, runtime)

    async def bind_k8s_slb_async(
        self,
        request: main_models.BindK8sSlbRequest,
    ) -> main_models.BindK8sSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.bind_k8s_slb_with_options_async(request, headers, runtime)

    def bind_slb_with_options(
        self,
        request: main_models.BindSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.slb_id):
            query['SlbId'] = request.slb_id
        if not DaraCore.is_null(request.slb_ip):
            query['SlbIp'] = request.slb_ip
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindSlb',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/app/bind_slb_json',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_slb_with_options_async(
        self,
        request: main_models.BindSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BindSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not DaraCore.is_null(request.slb_id):
            query['SlbId'] = request.slb_id
        if not DaraCore.is_null(request.slb_ip):
            query['SlbIp'] = request.slb_ip
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindSlb',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/app/bind_slb_json',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_slb(
        self,
        request: main_models.BindSlbRequest,
    ) -> main_models.BindSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.bind_slb_with_options(request, headers, runtime)

    async def bind_slb_async(
        self,
        request: main_models.BindSlbRequest,
    ) -> main_models.BindSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.bind_slb_with_options_async(request, headers, runtime)

    def change_deploy_group_with_options(
        self,
        request: main_models.ChangeDeployGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeDeployGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        if not DaraCore.is_null(request.force_status):
            query['ForceStatus'] = request.force_status
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeDeployGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_change_group',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeDeployGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_deploy_group_with_options_async(
        self,
        request: main_models.ChangeDeployGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeDeployGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        if not DaraCore.is_null(request.force_status):
            query['ForceStatus'] = request.force_status
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeDeployGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_change_group',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeDeployGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_deploy_group(
        self,
        request: main_models.ChangeDeployGroupRequest,
    ) -> main_models.ChangeDeployGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.change_deploy_group_with_options(request, headers, runtime)

    async def change_deploy_group_async(
        self,
        request: main_models.ChangeDeployGroupRequest,
    ) -> main_models.ChangeDeployGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.change_deploy_group_with_options_async(request, headers, runtime)

    def continue_pipeline_with_options(
        self,
        request: main_models.ContinuePipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ContinuePipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.confirm):
            query['Confirm'] = request.confirm
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ContinuePipeline',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/pipeline_batch_confirm',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinuePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def continue_pipeline_with_options_async(
        self,
        request: main_models.ContinuePipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ContinuePipelineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.confirm):
            query['Confirm'] = request.confirm
        if not DaraCore.is_null(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ContinuePipeline',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/pipeline_batch_confirm',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinuePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continue_pipeline(
        self,
        request: main_models.ContinuePipelineRequest,
    ) -> main_models.ContinuePipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.continue_pipeline_with_options(request, headers, runtime)

    async def continue_pipeline_async(
        self,
        request: main_models.ContinuePipelineRequest,
    ) -> main_models.ContinuePipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.continue_pipeline_with_options_async(request, headers, runtime)

    def convert_k8s_resource_with_options(
        self,
        request: main_models.ConvertK8sResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ConvertK8sResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConvertK8sResource',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/oam/k8s_resource_convert',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConvertK8sResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_k8s_resource_with_options_async(
        self,
        request: main_models.ConvertK8sResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ConvertK8sResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConvertK8sResource',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/oam/k8s_resource_convert',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConvertK8sResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_k8s_resource(
        self,
        request: main_models.ConvertK8sResourceRequest,
    ) -> main_models.ConvertK8sResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.convert_k8s_resource_with_options(request, headers, runtime)

    async def convert_k8s_resource_async(
        self,
        request: main_models.ConvertK8sResourceRequest,
    ) -> main_models.ConvertK8sResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.convert_k8s_resource_with_options_async(request, headers, runtime)

    def create_application_scaling_rule_with_options(
        self,
        request: main_models.CreateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_behaviour):
            query['ScalingBehaviour'] = request.scaling_behaviour
        if not DaraCore.is_null(request.scaling_rule_enable):
            query['ScalingRuleEnable'] = request.scaling_rule_enable
        if not DaraCore.is_null(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not DaraCore.is_null(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        if not DaraCore.is_null(request.scaling_rule_trigger):
            query['ScalingRuleTrigger'] = request.scaling_rule_trigger
        if not DaraCore.is_null(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationScalingRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/eam/scale/application_scaling_rule',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_scaling_rule_with_options_async(
        self,
        request: main_models.CreateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_behaviour):
            query['ScalingBehaviour'] = request.scaling_behaviour
        if not DaraCore.is_null(request.scaling_rule_enable):
            query['ScalingRuleEnable'] = request.scaling_rule_enable
        if not DaraCore.is_null(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not DaraCore.is_null(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        if not DaraCore.is_null(request.scaling_rule_trigger):
            query['ScalingRuleTrigger'] = request.scaling_rule_trigger
        if not DaraCore.is_null(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationScalingRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/eam/scale/application_scaling_rule',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_scaling_rule(
        self,
        request: main_models.CreateApplicationScalingRuleRequest,
    ) -> main_models.CreateApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_application_scaling_rule_with_options(request, headers, runtime)

    async def create_application_scaling_rule_async(
        self,
        request: main_models.CreateApplicationScalingRuleRequest,
    ) -> main_models.CreateApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_application_scaling_rule_with_options_async(request, headers, runtime)

    def create_config_template_with_options(
        self,
        request: main_models.CreateConfigTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConfigTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.format):
            body['Format'] = request.format
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConfigTemplate',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/config_template',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConfigTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_config_template_with_options_async(
        self,
        request: main_models.CreateConfigTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConfigTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.format):
            body['Format'] = request.format
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConfigTemplate',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/config_template',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConfigTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_config_template(
        self,
        request: main_models.CreateConfigTemplateRequest,
    ) -> main_models.CreateConfigTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_config_template_with_options(request, headers, runtime)

    async def create_config_template_async(
        self,
        request: main_models.CreateConfigTemplateRequest,
    ) -> main_models.CreateConfigTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_config_template_with_options_async(request, headers, runtime)

    def create_idcimport_command_with_options(
        self,
        request: main_models.CreateIDCImportCommandRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIDCImportCommandResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIDCImportCommand',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/create_idc_import_command',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIDCImportCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_idcimport_command_with_options_async(
        self,
        request: main_models.CreateIDCImportCommandRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIDCImportCommandResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIDCImportCommand',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/create_idc_import_command',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIDCImportCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_idcimport_command(
        self,
        request: main_models.CreateIDCImportCommandRequest,
    ) -> main_models.CreateIDCImportCommandResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_idcimport_command_with_options(request, headers, runtime)

    async def create_idcimport_command_async(
        self,
        request: main_models.CreateIDCImportCommandRequest,
    ) -> main_models.CreateIDCImportCommandResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_idcimport_command_with_options_async(request, headers, runtime)

    def create_k8s_config_map_with_options(
        self,
        request: main_models.CreateK8sConfigMapRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateK8sConfigMapResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateK8sConfigMap',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_config_map',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateK8sConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_k8s_config_map_with_options_async(
        self,
        request: main_models.CreateK8sConfigMapRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateK8sConfigMapResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateK8sConfigMap',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_config_map',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateK8sConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_k8s_config_map(
        self,
        request: main_models.CreateK8sConfigMapRequest,
    ) -> main_models.CreateK8sConfigMapResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_k8s_config_map_with_options(request, headers, runtime)

    async def create_k8s_config_map_async(
        self,
        request: main_models.CreateK8sConfigMapRequest,
    ) -> main_models.CreateK8sConfigMapResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_k8s_config_map_with_options_async(request, headers, runtime)

    def create_k8s_ingress_rule_with_options(
        self,
        request: main_models.CreateK8sIngressRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateK8sIngressRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ingress_conf):
            query['IngressConf'] = request.ingress_conf
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateK8sIngressRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_ingress',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateK8sIngressRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_k8s_ingress_rule_with_options_async(
        self,
        request: main_models.CreateK8sIngressRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateK8sIngressRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ingress_conf):
            query['IngressConf'] = request.ingress_conf
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateK8sIngressRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_ingress',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateK8sIngressRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_k8s_ingress_rule(
        self,
        request: main_models.CreateK8sIngressRuleRequest,
    ) -> main_models.CreateK8sIngressRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_k8s_ingress_rule_with_options(request, headers, runtime)

    async def create_k8s_ingress_rule_async(
        self,
        request: main_models.CreateK8sIngressRuleRequest,
    ) -> main_models.CreateK8sIngressRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_k8s_ingress_rule_with_options_async(request, headers, runtime)

    def create_k8s_secret_with_options(
        self,
        request: main_models.CreateK8sSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateK8sSecretResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.base_64encoded):
            body['Base64Encoded'] = request.base_64encoded
        if not DaraCore.is_null(request.cert_id):
            body['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_region_id):
            body['CertRegionId'] = request.cert_region_id
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateK8sSecret',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_secret',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateK8sSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_k8s_secret_with_options_async(
        self,
        request: main_models.CreateK8sSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateK8sSecretResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.base_64encoded):
            body['Base64Encoded'] = request.base_64encoded
        if not DaraCore.is_null(request.cert_id):
            body['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_region_id):
            body['CertRegionId'] = request.cert_region_id
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateK8sSecret',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_secret',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateK8sSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_k8s_secret(
        self,
        request: main_models.CreateK8sSecretRequest,
    ) -> main_models.CreateK8sSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_k8s_secret_with_options(request, headers, runtime)

    async def create_k8s_secret_async(
        self,
        request: main_models.CreateK8sSecretRequest,
    ) -> main_models.CreateK8sSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_k8s_secret_with_options_async(request, headers, runtime)

    def create_k8s_service_with_options(
        self,
        request: main_models.CreateK8sServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateK8sServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.external_traffic_policy):
            query['ExternalTrafficPolicy'] = request.external_traffic_policy
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.service_ports):
            query['ServicePorts'] = request.service_ports
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateK8sService',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_service',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateK8sServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_k8s_service_with_options_async(
        self,
        request: main_models.CreateK8sServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateK8sServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.external_traffic_policy):
            query['ExternalTrafficPolicy'] = request.external_traffic_policy
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.service_ports):
            query['ServicePorts'] = request.service_ports
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateK8sService',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_service',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateK8sServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_k8s_service(
        self,
        request: main_models.CreateK8sServiceRequest,
    ) -> main_models.CreateK8sServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_k8s_service_with_options(request, headers, runtime)

    async def create_k8s_service_async(
        self,
        request: main_models.CreateK8sServiceRequest,
    ) -> main_models.CreateK8sServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_k8s_service_with_options_async(request, headers, runtime)

    def delete_application_with_options(
        self,
        request: main_models.DeleteApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_delete_app',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: main_models.DeleteApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_delete_app',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application(
        self,
        request: main_models.DeleteApplicationRequest,
    ) -> main_models.DeleteApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_application_with_options(request, headers, runtime)

    async def delete_application_async(
        self,
        request: main_models.DeleteApplicationRequest,
    ) -> main_models.DeleteApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_application_with_options_async(request, headers, runtime)

    def delete_application_scaling_rule_with_options(
        self,
        request: main_models.DeleteApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationScalingRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/eam/scale/application_scaling_rule',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_scaling_rule_with_options_async(
        self,
        request: main_models.DeleteApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationScalingRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/eam/scale/application_scaling_rule',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application_scaling_rule(
        self,
        request: main_models.DeleteApplicationScalingRuleRequest,
    ) -> main_models.DeleteApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_application_scaling_rule_with_options(request, headers, runtime)

    async def delete_application_scaling_rule_async(
        self,
        request: main_models.DeleteApplicationScalingRuleRequest,
    ) -> main_models.DeleteApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_application_scaling_rule_with_options_async(request, headers, runtime)

    def delete_cluster_with_options(
        self,
        request: main_models.DeleteClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCluster',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/cluster',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: main_models.DeleteClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCluster',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/cluster',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        request: main_models.DeleteClusterRequest,
    ) -> main_models.DeleteClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_cluster_with_options(request, headers, runtime)

    async def delete_cluster_async(
        self,
        request: main_models.DeleteClusterRequest,
    ) -> main_models.DeleteClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_cluster_with_options_async(request, headers, runtime)

    def delete_cluster_member_with_options(
        self,
        request: main_models.DeleteClusterMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_member_id):
            query['ClusterMemberId'] = request.cluster_member_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClusterMember',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/cluster_member',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClusterMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_member_with_options_async(
        self,
        request: main_models.DeleteClusterMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_member_id):
            query['ClusterMemberId'] = request.cluster_member_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClusterMember',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/cluster_member',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClusterMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster_member(
        self,
        request: main_models.DeleteClusterMemberRequest,
    ) -> main_models.DeleteClusterMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_cluster_member_with_options(request, headers, runtime)

    async def delete_cluster_member_async(
        self,
        request: main_models.DeleteClusterMemberRequest,
    ) -> main_models.DeleteClusterMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_cluster_member_with_options_async(request, headers, runtime)

    def delete_config_template_with_options(
        self,
        request: main_models.DeleteConfigTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConfigTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConfigTemplate',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/config_template',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConfigTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_config_template_with_options_async(
        self,
        request: main_models.DeleteConfigTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConfigTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConfigTemplate',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/config_template',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConfigTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_config_template(
        self,
        request: main_models.DeleteConfigTemplateRequest,
    ) -> main_models.DeleteConfigTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_config_template_with_options(request, headers, runtime)

    async def delete_config_template_async(
        self,
        request: main_models.DeleteConfigTemplateRequest,
    ) -> main_models.DeleteConfigTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_config_template_with_options_async(request, headers, runtime)

    def delete_deploy_group_with_options(
        self,
        request: main_models.DeleteDeployGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeployGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeployGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/deploy_group',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeployGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_deploy_group_with_options_async(
        self,
        request: main_models.DeleteDeployGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeployGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeployGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/deploy_group',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeployGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_deploy_group(
        self,
        request: main_models.DeleteDeployGroupRequest,
    ) -> main_models.DeleteDeployGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_deploy_group_with_options(request, headers, runtime)

    async def delete_deploy_group_async(
        self,
        request: main_models.DeleteDeployGroupRequest,
    ) -> main_models.DeleteDeployGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_deploy_group_with_options_async(request, headers, runtime)

    def delete_ecu_with_options(
        self,
        request: main_models.DeleteEcuRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEcuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ecu_id):
            query['EcuId'] = request.ecu_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEcu',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/delete_ecu',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEcuResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ecu_with_options_async(
        self,
        request: main_models.DeleteEcuRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEcuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ecu_id):
            query['EcuId'] = request.ecu_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEcu',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/delete_ecu',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEcuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ecu(
        self,
        request: main_models.DeleteEcuRequest,
    ) -> main_models.DeleteEcuResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_ecu_with_options(request, headers, runtime)

    async def delete_ecu_async(
        self,
        request: main_models.DeleteEcuRequest,
    ) -> main_models.DeleteEcuResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_ecu_with_options_async(request, headers, runtime)

    def delete_k8s_application_with_options(
        self,
        request: main_models.DeleteK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteK8sApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteK8sApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_apps',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteK8sApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_k8s_application_with_options_async(
        self,
        request: main_models.DeleteK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteK8sApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteK8sApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_apps',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteK8sApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_k8s_application(
        self,
        request: main_models.DeleteK8sApplicationRequest,
    ) -> main_models.DeleteK8sApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_k8s_application_with_options(request, headers, runtime)

    async def delete_k8s_application_async(
        self,
        request: main_models.DeleteK8sApplicationRequest,
    ) -> main_models.DeleteK8sApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_k8s_application_with_options_async(request, headers, runtime)

    def delete_k8s_config_map_with_options(
        self,
        request: main_models.DeleteK8sConfigMapRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteK8sConfigMapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteK8sConfigMap',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_config_map',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteK8sConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_k8s_config_map_with_options_async(
        self,
        request: main_models.DeleteK8sConfigMapRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteK8sConfigMapResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteK8sConfigMap',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_config_map',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteK8sConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_k8s_config_map(
        self,
        request: main_models.DeleteK8sConfigMapRequest,
    ) -> main_models.DeleteK8sConfigMapResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_k8s_config_map_with_options(request, headers, runtime)

    async def delete_k8s_config_map_async(
        self,
        request: main_models.DeleteK8sConfigMapRequest,
    ) -> main_models.DeleteK8sConfigMapResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_k8s_config_map_with_options_async(request, headers, runtime)

    def delete_k8s_ingress_rule_with_options(
        self,
        request: main_models.DeleteK8sIngressRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteK8sIngressRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteK8sIngressRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_ingress',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteK8sIngressRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_k8s_ingress_rule_with_options_async(
        self,
        request: main_models.DeleteK8sIngressRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteK8sIngressRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteK8sIngressRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_ingress',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteK8sIngressRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_k8s_ingress_rule(
        self,
        request: main_models.DeleteK8sIngressRuleRequest,
    ) -> main_models.DeleteK8sIngressRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_k8s_ingress_rule_with_options(request, headers, runtime)

    async def delete_k8s_ingress_rule_async(
        self,
        request: main_models.DeleteK8sIngressRuleRequest,
    ) -> main_models.DeleteK8sIngressRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_k8s_ingress_rule_with_options_async(request, headers, runtime)

    def delete_k8s_secret_with_options(
        self,
        request: main_models.DeleteK8sSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteK8sSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteK8sSecret',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_secret',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteK8sSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_k8s_secret_with_options_async(
        self,
        request: main_models.DeleteK8sSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteK8sSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteK8sSecret',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_secret',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteK8sSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_k8s_secret(
        self,
        request: main_models.DeleteK8sSecretRequest,
    ) -> main_models.DeleteK8sSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_k8s_secret_with_options(request, headers, runtime)

    async def delete_k8s_secret_async(
        self,
        request: main_models.DeleteK8sSecretRequest,
    ) -> main_models.DeleteK8sSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_k8s_secret_with_options_async(request, headers, runtime)

    def delete_k8s_service_with_options(
        self,
        request: main_models.DeleteK8sServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteK8sServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteK8sService',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_service',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteK8sServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_k8s_service_with_options_async(
        self,
        request: main_models.DeleteK8sServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteK8sServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteK8sService',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_service',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteK8sServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_k8s_service(
        self,
        request: main_models.DeleteK8sServiceRequest,
    ) -> main_models.DeleteK8sServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_k8s_service_with_options(request, headers, runtime)

    async def delete_k8s_service_async(
        self,
        request: main_models.DeleteK8sServiceRequest,
    ) -> main_models.DeleteK8sServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_k8s_service_with_options_async(request, headers, runtime)

    def delete_log_path_with_options(
        self,
        request: main_models.DeleteLogPathRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogPathResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogPath',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/log/popListLogDirs',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLogPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_log_path_with_options_async(
        self,
        request: main_models.DeleteLogPathRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogPathResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogPath',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/log/popListLogDirs',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLogPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_log_path(
        self,
        request: main_models.DeleteLogPathRequest,
    ) -> main_models.DeleteLogPathResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_log_path_with_options(request, headers, runtime)

    async def delete_log_path_async(
        self,
        request: main_models.DeleteLogPathRequest,
    ) -> main_models.DeleteLogPathResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_log_path_with_options_async(request, headers, runtime)

    def delete_role_with_options(
        self,
        request: main_models.DeleteRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRole',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/delete_role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_role_with_options_async(
        self,
        request: main_models.DeleteRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRole',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/delete_role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_role(
        self,
        request: main_models.DeleteRoleRequest,
    ) -> main_models.DeleteRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_role_with_options(request, headers, runtime)

    async def delete_role_async(
        self,
        request: main_models.DeleteRoleRequest,
    ) -> main_models.DeleteRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_role_with_options_async(request, headers, runtime)

    def delete_service_group_with_options(
        self,
        request: main_models.DeleteServiceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/service/serviceGroups',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_group_with_options_async(
        self,
        request: main_models.DeleteServiceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/service/serviceGroups',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_group(
        self,
        request: main_models.DeleteServiceGroupRequest,
    ) -> main_models.DeleteServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_service_group_with_options(request, headers, runtime)

    async def delete_service_group_async(
        self,
        request: main_models.DeleteServiceGroupRequest,
    ) -> main_models.DeleteServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_service_group_with_options_async(request, headers, runtime)

    def delete_swimming_lane_with_options(
        self,
        request: main_models.DeleteSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSwimmingLaneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lane_id):
            query['LaneId'] = request.lane_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSwimmingLane',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/trafficmgnt/swimming_lanes',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSwimmingLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_swimming_lane_with_options_async(
        self,
        request: main_models.DeleteSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSwimmingLaneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lane_id):
            query['LaneId'] = request.lane_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSwimmingLane',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/trafficmgnt/swimming_lanes',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSwimmingLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_swimming_lane(
        self,
        request: main_models.DeleteSwimmingLaneRequest,
    ) -> main_models.DeleteSwimmingLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_swimming_lane_with_options(request, headers, runtime)

    async def delete_swimming_lane_async(
        self,
        request: main_models.DeleteSwimmingLaneRequest,
    ) -> main_models.DeleteSwimmingLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_swimming_lane_with_options_async(request, headers, runtime)

    def delete_user_define_region_with_options(
        self,
        request: main_models.DeleteUserDefineRegionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserDefineRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.region_tag):
            query['RegionTag'] = request.region_tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserDefineRegion',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/user_region_def',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserDefineRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_define_region_with_options_async(
        self,
        request: main_models.DeleteUserDefineRegionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserDefineRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.region_tag):
            query['RegionTag'] = request.region_tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserDefineRegion',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/user_region_def',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserDefineRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_define_region(
        self,
        request: main_models.DeleteUserDefineRegionRequest,
    ) -> main_models.DeleteUserDefineRegionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_user_define_region_with_options(request, headers, runtime)

    async def delete_user_define_region_async(
        self,
        request: main_models.DeleteUserDefineRegionRequest,
    ) -> main_models.DeleteUserDefineRegionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_user_define_region_with_options_async(request, headers, runtime)

    def deploy_application_with_options(
        self,
        request: main_models.DeployApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeployApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_env):
            query['AppEnv'] = request.app_env
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.batch):
            query['Batch'] = request.batch
        if not DaraCore.is_null(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not DaraCore.is_null(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        if not DaraCore.is_null(request.component_ids):
            query['ComponentIds'] = request.component_ids
        if not DaraCore.is_null(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.gray):
            query['Gray'] = request.gray
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.package_version):
            query['PackageVersion'] = request.package_version
        if not DaraCore.is_null(request.release_type):
            query['ReleaseType'] = request.release_type
        if not DaraCore.is_null(request.traffic_control_strategy):
            query['TrafficControlStrategy'] = request.traffic_control_strategy
        if not DaraCore.is_null(request.war_url):
            query['WarUrl'] = request.war_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeployApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_deploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_application_with_options_async(
        self,
        request: main_models.DeployApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeployApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_env):
            query['AppEnv'] = request.app_env
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.batch):
            query['Batch'] = request.batch
        if not DaraCore.is_null(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not DaraCore.is_null(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        if not DaraCore.is_null(request.component_ids):
            query['ComponentIds'] = request.component_ids
        if not DaraCore.is_null(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.gray):
            query['Gray'] = request.gray
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.package_version):
            query['PackageVersion'] = request.package_version
        if not DaraCore.is_null(request.release_type):
            query['ReleaseType'] = request.release_type
        if not DaraCore.is_null(request.traffic_control_strategy):
            query['TrafficControlStrategy'] = request.traffic_control_strategy
        if not DaraCore.is_null(request.war_url):
            query['WarUrl'] = request.war_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeployApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_deploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_application(
        self,
        request: main_models.DeployApplicationRequest,
    ) -> main_models.DeployApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.deploy_application_with_options(request, headers, runtime)

    async def deploy_application_async(
        self,
        request: main_models.DeployApplicationRequest,
    ) -> main_models.DeployApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.deploy_application_with_options_async(request, headers, runtime)

    def deploy_k8s_application_with_options(
        self,
        request: main_models.DeployK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeployK8sApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.args):
            query['Args'] = request.args
        if not DaraCore.is_null(request.batch_timeout):
            query['BatchTimeout'] = request.batch_timeout
        if not DaraCore.is_null(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not DaraCore.is_null(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        if not DaraCore.is_null(request.canary_rule_id):
            query['CanaryRuleId'] = request.canary_rule_id
        if not DaraCore.is_null(request.change_order_desc):
            query['ChangeOrderDesc'] = request.change_order_desc
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.config_mount_descs):
            query['ConfigMountDescs'] = request.config_mount_descs
        if not DaraCore.is_null(request.cpu_limit):
            query['CpuLimit'] = request.cpu_limit
        if not DaraCore.is_null(request.cpu_request):
            query['CpuRequest'] = request.cpu_request
        if not DaraCore.is_null(request.custom_affinity):
            query['CustomAffinity'] = request.custom_affinity
        if not DaraCore.is_null(request.custom_agent_version):
            query['CustomAgentVersion'] = request.custom_agent_version
        if not DaraCore.is_null(request.custom_tolerations):
            query['CustomTolerations'] = request.custom_tolerations
        if not DaraCore.is_null(request.deploy_across_nodes):
            query['DeployAcrossNodes'] = request.deploy_across_nodes
        if not DaraCore.is_null(request.deploy_across_zones):
            query['DeployAcrossZones'] = request.deploy_across_zones
        if not DaraCore.is_null(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not DaraCore.is_null(request.empty_dirs):
            query['EmptyDirs'] = request.empty_dirs
        if not DaraCore.is_null(request.enable_ahas):
            query['EnableAhas'] = request.enable_ahas
        if not DaraCore.is_null(request.enable_empty_push_reject):
            query['EnableEmptyPushReject'] = request.enable_empty_push_reject
        if not DaraCore.is_null(request.enable_lossless_rule):
            query['EnableLosslessRule'] = request.enable_lossless_rule
        if not DaraCore.is_null(request.env_froms):
            query['EnvFroms'] = request.env_froms
        if not DaraCore.is_null(request.envs):
            query['Envs'] = request.envs
        if not DaraCore.is_null(request.image):
            query['Image'] = request.image
        if not DaraCore.is_null(request.image_platforms):
            query['ImagePlatforms'] = request.image_platforms
        if not DaraCore.is_null(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not DaraCore.is_null(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not DaraCore.is_null(request.jdk):
            query['JDK'] = request.jdk
        if not DaraCore.is_null(request.java_start_up_config):
            query['JavaStartUpConfig'] = request.java_start_up_config
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.limit_ephemeral_storage):
            query['LimitEphemeralStorage'] = request.limit_ephemeral_storage
        if not DaraCore.is_null(request.liveness):
            query['Liveness'] = request.liveness
        if not DaraCore.is_null(request.local_volume):
            query['LocalVolume'] = request.local_volume
        if not DaraCore.is_null(request.lossless_rule_aligned):
            query['LosslessRuleAligned'] = request.lossless_rule_aligned
        if not DaraCore.is_null(request.lossless_rule_delay_time):
            query['LosslessRuleDelayTime'] = request.lossless_rule_delay_time
        if not DaraCore.is_null(request.lossless_rule_func_type):
            query['LosslessRuleFuncType'] = request.lossless_rule_func_type
        if not DaraCore.is_null(request.lossless_rule_related):
            query['LosslessRuleRelated'] = request.lossless_rule_related
        if not DaraCore.is_null(request.lossless_rule_warmup_time):
            query['LosslessRuleWarmupTime'] = request.lossless_rule_warmup_time
        if not DaraCore.is_null(request.mcpu_limit):
            query['McpuLimit'] = request.mcpu_limit
        if not DaraCore.is_null(request.mcpu_request):
            query['McpuRequest'] = request.mcpu_request
        if not DaraCore.is_null(request.memory_limit):
            query['MemoryLimit'] = request.memory_limit
        if not DaraCore.is_null(request.memory_request):
            query['MemoryRequest'] = request.memory_request
        if not DaraCore.is_null(request.mount_descs):
            query['MountDescs'] = request.mount_descs
        if not DaraCore.is_null(request.nas_id):
            query['NasId'] = request.nas_id
        if not DaraCore.is_null(request.package_url):
            query['PackageUrl'] = request.package_url
        if not DaraCore.is_null(request.package_version):
            query['PackageVersion'] = request.package_version
        if not DaraCore.is_null(request.package_version_id):
            query['PackageVersionId'] = request.package_version_id
        if not DaraCore.is_null(request.post_start):
            query['PostStart'] = request.post_start
        if not DaraCore.is_null(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not DaraCore.is_null(request.pvc_mount_descs):
            query['PvcMountDescs'] = request.pvc_mount_descs
        if not DaraCore.is_null(request.readiness):
            query['Readiness'] = request.readiness
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.requests_ephemeral_storage):
            query['RequestsEphemeralStorage'] = request.requests_ephemeral_storage
        if not DaraCore.is_null(request.runtime_class_name):
            query['RuntimeClassName'] = request.runtime_class_name
        if not DaraCore.is_null(request.security_context):
            query['SecurityContext'] = request.security_context
        if not DaraCore.is_null(request.sidecars):
            query['Sidecars'] = request.sidecars
        if not DaraCore.is_null(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not DaraCore.is_null(request.startup):
            query['Startup'] = request.startup
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.terminate_grace_period):
            query['TerminateGracePeriod'] = request.terminate_grace_period
        if not DaraCore.is_null(request.traffic_control_strategy):
            query['TrafficControlStrategy'] = request.traffic_control_strategy
        if not DaraCore.is_null(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not DaraCore.is_null(request.uri_encoding):
            query['UriEncoding'] = request.uri_encoding
        if not DaraCore.is_null(request.use_body_encoding):
            query['UseBodyEncoding'] = request.use_body_encoding
        if not DaraCore.is_null(request.user_base_image_url):
            query['UserBaseImageUrl'] = request.user_base_image_url
        if not DaraCore.is_null(request.volumes_str):
            query['VolumesStr'] = request.volumes_str
        if not DaraCore.is_null(request.web_container):
            query['WebContainer'] = request.web_container
        if not DaraCore.is_null(request.web_container_config):
            query['WebContainerConfig'] = request.web_container_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeployK8sApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_apps',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployK8sApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_k8s_application_with_options_async(
        self,
        request: main_models.DeployK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeployK8sApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.args):
            query['Args'] = request.args
        if not DaraCore.is_null(request.batch_timeout):
            query['BatchTimeout'] = request.batch_timeout
        if not DaraCore.is_null(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not DaraCore.is_null(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        if not DaraCore.is_null(request.canary_rule_id):
            query['CanaryRuleId'] = request.canary_rule_id
        if not DaraCore.is_null(request.change_order_desc):
            query['ChangeOrderDesc'] = request.change_order_desc
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.config_mount_descs):
            query['ConfigMountDescs'] = request.config_mount_descs
        if not DaraCore.is_null(request.cpu_limit):
            query['CpuLimit'] = request.cpu_limit
        if not DaraCore.is_null(request.cpu_request):
            query['CpuRequest'] = request.cpu_request
        if not DaraCore.is_null(request.custom_affinity):
            query['CustomAffinity'] = request.custom_affinity
        if not DaraCore.is_null(request.custom_agent_version):
            query['CustomAgentVersion'] = request.custom_agent_version
        if not DaraCore.is_null(request.custom_tolerations):
            query['CustomTolerations'] = request.custom_tolerations
        if not DaraCore.is_null(request.deploy_across_nodes):
            query['DeployAcrossNodes'] = request.deploy_across_nodes
        if not DaraCore.is_null(request.deploy_across_zones):
            query['DeployAcrossZones'] = request.deploy_across_zones
        if not DaraCore.is_null(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not DaraCore.is_null(request.empty_dirs):
            query['EmptyDirs'] = request.empty_dirs
        if not DaraCore.is_null(request.enable_ahas):
            query['EnableAhas'] = request.enable_ahas
        if not DaraCore.is_null(request.enable_empty_push_reject):
            query['EnableEmptyPushReject'] = request.enable_empty_push_reject
        if not DaraCore.is_null(request.enable_lossless_rule):
            query['EnableLosslessRule'] = request.enable_lossless_rule
        if not DaraCore.is_null(request.env_froms):
            query['EnvFroms'] = request.env_froms
        if not DaraCore.is_null(request.envs):
            query['Envs'] = request.envs
        if not DaraCore.is_null(request.image):
            query['Image'] = request.image
        if not DaraCore.is_null(request.image_platforms):
            query['ImagePlatforms'] = request.image_platforms
        if not DaraCore.is_null(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not DaraCore.is_null(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not DaraCore.is_null(request.jdk):
            query['JDK'] = request.jdk
        if not DaraCore.is_null(request.java_start_up_config):
            query['JavaStartUpConfig'] = request.java_start_up_config
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.limit_ephemeral_storage):
            query['LimitEphemeralStorage'] = request.limit_ephemeral_storage
        if not DaraCore.is_null(request.liveness):
            query['Liveness'] = request.liveness
        if not DaraCore.is_null(request.local_volume):
            query['LocalVolume'] = request.local_volume
        if not DaraCore.is_null(request.lossless_rule_aligned):
            query['LosslessRuleAligned'] = request.lossless_rule_aligned
        if not DaraCore.is_null(request.lossless_rule_delay_time):
            query['LosslessRuleDelayTime'] = request.lossless_rule_delay_time
        if not DaraCore.is_null(request.lossless_rule_func_type):
            query['LosslessRuleFuncType'] = request.lossless_rule_func_type
        if not DaraCore.is_null(request.lossless_rule_related):
            query['LosslessRuleRelated'] = request.lossless_rule_related
        if not DaraCore.is_null(request.lossless_rule_warmup_time):
            query['LosslessRuleWarmupTime'] = request.lossless_rule_warmup_time
        if not DaraCore.is_null(request.mcpu_limit):
            query['McpuLimit'] = request.mcpu_limit
        if not DaraCore.is_null(request.mcpu_request):
            query['McpuRequest'] = request.mcpu_request
        if not DaraCore.is_null(request.memory_limit):
            query['MemoryLimit'] = request.memory_limit
        if not DaraCore.is_null(request.memory_request):
            query['MemoryRequest'] = request.memory_request
        if not DaraCore.is_null(request.mount_descs):
            query['MountDescs'] = request.mount_descs
        if not DaraCore.is_null(request.nas_id):
            query['NasId'] = request.nas_id
        if not DaraCore.is_null(request.package_url):
            query['PackageUrl'] = request.package_url
        if not DaraCore.is_null(request.package_version):
            query['PackageVersion'] = request.package_version
        if not DaraCore.is_null(request.package_version_id):
            query['PackageVersionId'] = request.package_version_id
        if not DaraCore.is_null(request.post_start):
            query['PostStart'] = request.post_start
        if not DaraCore.is_null(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not DaraCore.is_null(request.pvc_mount_descs):
            query['PvcMountDescs'] = request.pvc_mount_descs
        if not DaraCore.is_null(request.readiness):
            query['Readiness'] = request.readiness
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.requests_ephemeral_storage):
            query['RequestsEphemeralStorage'] = request.requests_ephemeral_storage
        if not DaraCore.is_null(request.runtime_class_name):
            query['RuntimeClassName'] = request.runtime_class_name
        if not DaraCore.is_null(request.security_context):
            query['SecurityContext'] = request.security_context
        if not DaraCore.is_null(request.sidecars):
            query['Sidecars'] = request.sidecars
        if not DaraCore.is_null(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not DaraCore.is_null(request.startup):
            query['Startup'] = request.startup
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.terminate_grace_period):
            query['TerminateGracePeriod'] = request.terminate_grace_period
        if not DaraCore.is_null(request.traffic_control_strategy):
            query['TrafficControlStrategy'] = request.traffic_control_strategy
        if not DaraCore.is_null(request.update_strategy):
            query['UpdateStrategy'] = request.update_strategy
        if not DaraCore.is_null(request.uri_encoding):
            query['UriEncoding'] = request.uri_encoding
        if not DaraCore.is_null(request.use_body_encoding):
            query['UseBodyEncoding'] = request.use_body_encoding
        if not DaraCore.is_null(request.user_base_image_url):
            query['UserBaseImageUrl'] = request.user_base_image_url
        if not DaraCore.is_null(request.volumes_str):
            query['VolumesStr'] = request.volumes_str
        if not DaraCore.is_null(request.web_container):
            query['WebContainer'] = request.web_container
        if not DaraCore.is_null(request.web_container_config):
            query['WebContainerConfig'] = request.web_container_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeployK8sApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_apps',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployK8sApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_k8s_application(
        self,
        request: main_models.DeployK8sApplicationRequest,
    ) -> main_models.DeployK8sApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.deploy_k8s_application_with_options(request, headers, runtime)

    async def deploy_k8s_application_async(
        self,
        request: main_models.DeployK8sApplicationRequest,
    ) -> main_models.DeployK8sApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.deploy_k8s_application_with_options_async(request, headers, runtime)

    def describe_app_instance_list_with_options(
        self,
        request: main_models.DescribeAppInstanceListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppInstanceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.with_node_info):
            query['WithNodeInfo'] = request.with_node_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppInstanceList',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/oam/app_instance_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_instance_list_with_options_async(
        self,
        request: main_models.DescribeAppInstanceListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppInstanceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.with_node_info):
            query['WithNodeInfo'] = request.with_node_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppInstanceList',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/oam/app_instance_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_instance_list(
        self,
        request: main_models.DescribeAppInstanceListRequest,
    ) -> main_models.DescribeAppInstanceListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_app_instance_list_with_options(request, headers, runtime)

    async def describe_app_instance_list_async(
        self,
        request: main_models.DescribeAppInstanceListRequest,
    ) -> main_models.DescribeAppInstanceListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_app_instance_list_with_options_async(request, headers, runtime)

    def describe_application_scaling_rules_with_options(
        self,
        request: main_models.DescribeApplicationScalingRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationScalingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationScalingRules',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/eam/scale/application_scaling_rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_scaling_rules_with_options_async(
        self,
        request: main_models.DescribeApplicationScalingRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationScalingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationScalingRules',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/eam/scale/application_scaling_rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationScalingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_scaling_rules(
        self,
        request: main_models.DescribeApplicationScalingRulesRequest,
    ) -> main_models.DescribeApplicationScalingRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_application_scaling_rules_with_options(request, headers, runtime)

    async def describe_application_scaling_rules_async(
        self,
        request: main_models.DescribeApplicationScalingRulesRequest,
    ) -> main_models.DescribeApplicationScalingRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_application_scaling_rules_with_options_async(request, headers, runtime)

    def describe_locality_setting_with_options(
        self,
        request: main_models.DescribeLocalitySettingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLocalitySettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLocalitySetting',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/sp/applications/locality/setting',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLocalitySettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_locality_setting_with_options_async(
        self,
        request: main_models.DescribeLocalitySettingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLocalitySettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLocalitySetting',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/sp/applications/locality/setting',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLocalitySettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_locality_setting(
        self,
        request: main_models.DescribeLocalitySettingRequest,
    ) -> main_models.DescribeLocalitySettingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_locality_setting_with_options(request, headers, runtime)

    async def describe_locality_setting_async(
        self,
        request: main_models.DescribeLocalitySettingRequest,
    ) -> main_models.DescribeLocalitySettingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_locality_setting_with_options_async(request, headers, runtime)

    def disable_application_scaling_rule_with_options(
        self,
        request: main_models.DisableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationScalingRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/eam/scale/disable_application_scaling_rule',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_scaling_rule_with_options_async(
        self,
        request: main_models.DisableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationScalingRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/eam/scale/disable_application_scaling_rule',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_scaling_rule(
        self,
        request: main_models.DisableApplicationScalingRuleRequest,
    ) -> main_models.DisableApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.disable_application_scaling_rule_with_options(request, headers, runtime)

    async def disable_application_scaling_rule_async(
        self,
        request: main_models.DisableApplicationScalingRuleRequest,
    ) -> main_models.DisableApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.disable_application_scaling_rule_with_options_async(request, headers, runtime)

    def enable_application_scaling_rule_with_options(
        self,
        request: main_models.EnableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationScalingRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/eam/scale/enable_application_scaling_rule',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_scaling_rule_with_options_async(
        self,
        request: main_models.EnableApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationScalingRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/eam/scale/enable_application_scaling_rule',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_scaling_rule(
        self,
        request: main_models.EnableApplicationScalingRuleRequest,
    ) -> main_models.EnableApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.enable_application_scaling_rule_with_options(request, headers, runtime)

    async def enable_application_scaling_rule_async(
        self,
        request: main_models.EnableApplicationScalingRuleRequest,
    ) -> main_models.EnableApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.enable_application_scaling_rule_with_options_async(request, headers, runtime)

    def get_app_deployment_with_options(
        self,
        request: main_models.GetAppDeploymentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAppDeploymentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppDeployment',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/oam/app_deployment',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_deployment_with_options_async(
        self,
        request: main_models.GetAppDeploymentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAppDeploymentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppDeployment',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/oam/app_deployment',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_deployment(
        self,
        request: main_models.GetAppDeploymentRequest,
    ) -> main_models.GetAppDeploymentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_app_deployment_with_options(request, headers, runtime)

    async def get_app_deployment_async(
        self,
        request: main_models.GetAppDeploymentRequest,
    ) -> main_models.GetAppDeploymentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_app_deployment_with_options_async(request, headers, runtime)

    def get_application_with_options(
        self,
        request: main_models.GetApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/app_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_with_options_async(
        self,
        request: main_models.GetApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/app_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application(
        self,
        request: main_models.GetApplicationRequest,
    ) -> main_models.GetApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_application_with_options(request, headers, runtime)

    async def get_application_async(
        self,
        request: main_models.GetApplicationRequest,
    ) -> main_models.GetApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_application_with_options_async(request, headers, runtime)

    def get_change_order_info_with_options(
        self,
        request: main_models.GetChangeOrderInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetChangeOrderInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChangeOrderInfo',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/change_order_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChangeOrderInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_change_order_info_with_options_async(
        self,
        request: main_models.GetChangeOrderInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetChangeOrderInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChangeOrderInfo',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/change_order_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChangeOrderInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_change_order_info(
        self,
        request: main_models.GetChangeOrderInfoRequest,
    ) -> main_models.GetChangeOrderInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_change_order_info_with_options(request, headers, runtime)

    async def get_change_order_info_async(
        self,
        request: main_models.GetChangeOrderInfoRequest,
    ) -> main_models.GetChangeOrderInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_change_order_info_with_options_async(request, headers, runtime)

    def get_cluster_with_options(
        self,
        request: main_models.GetClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCluster',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/cluster',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_with_options_async(
        self,
        request: main_models.GetClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCluster',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/cluster',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster(
        self,
        request: main_models.GetClusterRequest,
    ) -> main_models.GetClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_cluster_with_options(request, headers, runtime)

    async def get_cluster_async(
        self,
        request: main_models.GetClusterRequest,
    ) -> main_models.GetClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_cluster_with_options_async(request, headers, runtime)

    def get_container_configuration_with_options(
        self,
        request: main_models.GetContainerConfigurationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetContainerConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetContainerConfiguration',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/container_config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContainerConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_container_configuration_with_options_async(
        self,
        request: main_models.GetContainerConfigurationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetContainerConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetContainerConfiguration',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/container_config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetContainerConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_container_configuration(
        self,
        request: main_models.GetContainerConfigurationRequest,
    ) -> main_models.GetContainerConfigurationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_container_configuration_with_options(request, headers, runtime)

    async def get_container_configuration_async(
        self,
        request: main_models.GetContainerConfigurationRequest,
    ) -> main_models.GetContainerConfigurationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_container_configuration_with_options_async(request, headers, runtime)

    def get_java_start_up_config_with_options(
        self,
        request: main_models.GetJavaStartUpConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJavaStartUpConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJavaStartUpConfig',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/oam/java_start_up_config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJavaStartUpConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_java_start_up_config_with_options_async(
        self,
        request: main_models.GetJavaStartUpConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJavaStartUpConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJavaStartUpConfig',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/oam/java_start_up_config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJavaStartUpConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_java_start_up_config(
        self,
        request: main_models.GetJavaStartUpConfigRequest,
    ) -> main_models.GetJavaStartUpConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_java_start_up_config_with_options(request, headers, runtime)

    async def get_java_start_up_config_async(
        self,
        request: main_models.GetJavaStartUpConfigRequest,
    ) -> main_models.GetJavaStartUpConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_java_start_up_config_with_options_async(request, headers, runtime)

    def get_jvm_configuration_with_options(
        self,
        request: main_models.GetJvmConfigurationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJvmConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJvmConfiguration',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/app_jvm_config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJvmConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_jvm_configuration_with_options_async(
        self,
        request: main_models.GetJvmConfigurationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJvmConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJvmConfiguration',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/app_jvm_config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJvmConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_jvm_configuration(
        self,
        request: main_models.GetJvmConfigurationRequest,
    ) -> main_models.GetJvmConfigurationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_jvm_configuration_with_options(request, headers, runtime)

    async def get_jvm_configuration_async(
        self,
        request: main_models.GetJvmConfigurationRequest,
    ) -> main_models.GetJvmConfigurationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_jvm_configuration_with_options_async(request, headers, runtime)

    def get_k8s_app_precheck_result_with_options(
        self,
        request: main_models.GetK8sAppPrecheckResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetK8sAppPrecheckResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetK8sAppPrecheckResult',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/app_precheck',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetK8sAppPrecheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_k8s_app_precheck_result_with_options_async(
        self,
        request: main_models.GetK8sAppPrecheckResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetK8sAppPrecheckResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetK8sAppPrecheckResult',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/app_precheck',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetK8sAppPrecheckResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_k8s_app_precheck_result(
        self,
        request: main_models.GetK8sAppPrecheckResultRequest,
    ) -> main_models.GetK8sAppPrecheckResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_k8s_app_precheck_result_with_options(request, headers, runtime)

    async def get_k8s_app_precheck_result_async(
        self,
        request: main_models.GetK8sAppPrecheckResultRequest,
    ) -> main_models.GetK8sAppPrecheckResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_k8s_app_precheck_result_with_options_async(request, headers, runtime)

    def get_k8s_application_with_options(
        self,
        request: main_models.GetK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetK8sApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetK8sApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_application',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetK8sApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_k8s_application_with_options_async(
        self,
        request: main_models.GetK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetK8sApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetK8sApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_application',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetK8sApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_k8s_application(
        self,
        request: main_models.GetK8sApplicationRequest,
    ) -> main_models.GetK8sApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_k8s_application_with_options(request, headers, runtime)

    async def get_k8s_application_async(
        self,
        request: main_models.GetK8sApplicationRequest,
    ) -> main_models.GetK8sApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_k8s_application_with_options_async(request, headers, runtime)

    def get_k8s_cluster_with_options(
        self,
        request: main_models.GetK8sClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetK8sClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_tag):
            query['RegionTag'] = request.region_tag
        if not DaraCore.is_null(request.sub_cluster_type):
            query['SubClusterType'] = request.sub_cluster_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetK8sCluster',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s_clusters',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetK8sClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_k8s_cluster_with_options_async(
        self,
        request: main_models.GetK8sClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetK8sClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_tag):
            query['RegionTag'] = request.region_tag
        if not DaraCore.is_null(request.sub_cluster_type):
            query['SubClusterType'] = request.sub_cluster_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetK8sCluster',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s_clusters',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetK8sClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_k8s_cluster(
        self,
        request: main_models.GetK8sClusterRequest,
    ) -> main_models.GetK8sClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_k8s_cluster_with_options(request, headers, runtime)

    async def get_k8s_cluster_async(
        self,
        request: main_models.GetK8sClusterRequest,
    ) -> main_models.GetK8sClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_k8s_cluster_with_options_async(request, headers, runtime)

    def get_k8s_services_with_options(
        self,
        request: main_models.GetK8sServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetK8sServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetK8sServices',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_service',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetK8sServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_k8s_services_with_options_async(
        self,
        request: main_models.GetK8sServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetK8sServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetK8sServices',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_service',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetK8sServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_k8s_services(
        self,
        request: main_models.GetK8sServicesRequest,
    ) -> main_models.GetK8sServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_k8s_services_with_options(request, headers, runtime)

    async def get_k8s_services_async(
        self,
        request: main_models.GetK8sServicesRequest,
    ) -> main_models.GetK8sServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_k8s_services_with_options_async(request, headers, runtime)

    def get_package_storage_credential_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPackageStorageCredentialResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPackageStorageCredential',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/package_storage_credential',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPackageStorageCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_package_storage_credential_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPackageStorageCredentialResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPackageStorageCredential',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/package_storage_credential',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPackageStorageCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_package_storage_credential(self) -> main_models.GetPackageStorageCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_package_storage_credential_with_options(headers, runtime)

    async def get_package_storage_credential_async(self) -> main_models.GetPackageStorageCredentialResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_package_storage_credential_with_options_async(headers, runtime)

    def get_scaling_rules_with_options(
        self,
        request: main_models.GetScalingRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetScalingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScalingRules',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/scalingRules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scaling_rules_with_options_async(
        self,
        request: main_models.GetScalingRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetScalingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScalingRules',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/scalingRules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScalingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scaling_rules(
        self,
        request: main_models.GetScalingRulesRequest,
    ) -> main_models.GetScalingRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_scaling_rules_with_options(request, headers, runtime)

    async def get_scaling_rules_async(
        self,
        request: main_models.GetScalingRulesRequest,
    ) -> main_models.GetScalingRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_scaling_rules_with_options_async(request, headers, runtime)

    def get_secure_token_with_options(
        self,
        request: main_models.GetSecureTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSecureTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecureToken',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/secure_token',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecureTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secure_token_with_options_async(
        self,
        request: main_models.GetSecureTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSecureTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecureToken',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/secure_token',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecureTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secure_token(
        self,
        request: main_models.GetSecureTokenRequest,
    ) -> main_models.GetSecureTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_secure_token_with_options(request, headers, runtime)

    async def get_secure_token_async(
        self,
        request: main_models.GetSecureTokenRequest,
    ) -> main_models.GetSecureTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_secure_token_with_options_async(request, headers, runtime)

    def get_service_consumers_page_with_options(
        self,
        request: main_models.GetServiceConsumersPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceConsumersPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['appId'] = request.app_id
        if not DaraCore.is_null(request.group):
            query['group'] = request.group
        if not DaraCore.is_null(request.ip):
            query['ip'] = request.ip
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.origin):
            query['origin'] = request.origin
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.registry_type):
            query['registryType'] = request.registry_type
        if not DaraCore.is_null(request.service_id):
            query['serviceId'] = request.service_id
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        if not DaraCore.is_null(request.service_version):
            query['serviceVersion'] = request.service_version
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceConsumersPage',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/sp/api/mseForOam/getServiceConsumersPage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceConsumersPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_consumers_page_with_options_async(
        self,
        request: main_models.GetServiceConsumersPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceConsumersPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['appId'] = request.app_id
        if not DaraCore.is_null(request.group):
            query['group'] = request.group
        if not DaraCore.is_null(request.ip):
            query['ip'] = request.ip
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.origin):
            query['origin'] = request.origin
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.registry_type):
            query['registryType'] = request.registry_type
        if not DaraCore.is_null(request.service_id):
            query['serviceId'] = request.service_id
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        if not DaraCore.is_null(request.service_version):
            query['serviceVersion'] = request.service_version
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceConsumersPage',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/sp/api/mseForOam/getServiceConsumersPage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceConsumersPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_consumers_page(
        self,
        request: main_models.GetServiceConsumersPageRequest,
    ) -> main_models.GetServiceConsumersPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_service_consumers_page_with_options(request, headers, runtime)

    async def get_service_consumers_page_async(
        self,
        request: main_models.GetServiceConsumersPageRequest,
    ) -> main_models.GetServiceConsumersPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_service_consumers_page_with_options_async(request, headers, runtime)

    def get_service_detail_with_options(
        self,
        request: main_models.GetServiceDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['appId'] = request.app_id
        if not DaraCore.is_null(request.group):
            query['group'] = request.group
        if not DaraCore.is_null(request.ip):
            query['ip'] = request.ip
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.origin):
            query['origin'] = request.origin
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.registry_type):
            query['registryType'] = request.registry_type
        if not DaraCore.is_null(request.service_id):
            query['serviceId'] = request.service_id
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        if not DaraCore.is_null(request.service_version):
            query['serviceVersion'] = request.service_version
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceDetail',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/sp/api/mseForOam/getServiceDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_detail_with_options_async(
        self,
        request: main_models.GetServiceDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['appId'] = request.app_id
        if not DaraCore.is_null(request.group):
            query['group'] = request.group
        if not DaraCore.is_null(request.ip):
            query['ip'] = request.ip
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.origin):
            query['origin'] = request.origin
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.registry_type):
            query['registryType'] = request.registry_type
        if not DaraCore.is_null(request.service_id):
            query['serviceId'] = request.service_id
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        if not DaraCore.is_null(request.service_version):
            query['serviceVersion'] = request.service_version
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceDetail',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/sp/api/mseForOam/getServiceDetail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_detail(
        self,
        request: main_models.GetServiceDetailRequest,
    ) -> main_models.GetServiceDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_service_detail_with_options(request, headers, runtime)

    async def get_service_detail_async(
        self,
        request: main_models.GetServiceDetailRequest,
    ) -> main_models.GetServiceDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_service_detail_with_options_async(request, headers, runtime)

    def get_service_list_page_with_options(
        self,
        request: main_models.GetServiceListPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceListPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.origin):
            query['origin'] = request.origin
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.search_type):
            query['searchType'] = request.search_type
        if not DaraCore.is_null(request.search_value):
            query['searchValue'] = request.search_value
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        if not DaraCore.is_null(request.side):
            query['side'] = request.side
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceListPage',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/sp/api/mseForOam/getServiceListPage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceListPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_list_page_with_options_async(
        self,
        request: main_models.GetServiceListPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceListPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.origin):
            query['origin'] = request.origin
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.search_type):
            query['searchType'] = request.search_type
        if not DaraCore.is_null(request.search_value):
            query['searchValue'] = request.search_value
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        if not DaraCore.is_null(request.side):
            query['side'] = request.side
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceListPage',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/sp/api/mseForOam/getServiceListPage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceListPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_list_page(
        self,
        request: main_models.GetServiceListPageRequest,
    ) -> main_models.GetServiceListPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_service_list_page_with_options(request, headers, runtime)

    async def get_service_list_page_async(
        self,
        request: main_models.GetServiceListPageRequest,
    ) -> main_models.GetServiceListPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_service_list_page_with_options_async(request, headers, runtime)

    def get_service_method_page_with_options(
        self,
        request: main_models.GetServiceMethodPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceMethodPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['appId'] = request.app_id
        if not DaraCore.is_null(request.group):
            query['group'] = request.group
        if not DaraCore.is_null(request.ip):
            query['ip'] = request.ip
        if not DaraCore.is_null(request.method_controller):
            query['methodController'] = request.method_controller
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.origin):
            query['origin'] = request.origin
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.path):
            query['path'] = request.path
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.registry_type):
            query['registryType'] = request.registry_type
        if not DaraCore.is_null(request.service_id):
            query['serviceId'] = request.service_id
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        if not DaraCore.is_null(request.service_version):
            query['serviceVersion'] = request.service_version
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceMethodPage',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/sp/api/mseForOam/getServiceMethodPage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceMethodPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_method_page_with_options_async(
        self,
        request: main_models.GetServiceMethodPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceMethodPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['appId'] = request.app_id
        if not DaraCore.is_null(request.group):
            query['group'] = request.group
        if not DaraCore.is_null(request.ip):
            query['ip'] = request.ip
        if not DaraCore.is_null(request.method_controller):
            query['methodController'] = request.method_controller
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.origin):
            query['origin'] = request.origin
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.path):
            query['path'] = request.path
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.registry_type):
            query['registryType'] = request.registry_type
        if not DaraCore.is_null(request.service_id):
            query['serviceId'] = request.service_id
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        if not DaraCore.is_null(request.service_version):
            query['serviceVersion'] = request.service_version
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceMethodPage',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/sp/api/mseForOam/getServiceMethodPage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceMethodPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_method_page(
        self,
        request: main_models.GetServiceMethodPageRequest,
    ) -> main_models.GetServiceMethodPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_service_method_page_with_options(request, headers, runtime)

    async def get_service_method_page_async(
        self,
        request: main_models.GetServiceMethodPageRequest,
    ) -> main_models.GetServiceMethodPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_service_method_page_with_options_async(request, headers, runtime)

    def get_service_providers_page_with_options(
        self,
        request: main_models.GetServiceProvidersPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceProvidersPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['appId'] = request.app_id
        if not DaraCore.is_null(request.group):
            query['group'] = request.group
        if not DaraCore.is_null(request.ip):
            query['ip'] = request.ip
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.origin):
            query['origin'] = request.origin
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.registry_type):
            query['registryType'] = request.registry_type
        if not DaraCore.is_null(request.service_id):
            query['serviceId'] = request.service_id
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        if not DaraCore.is_null(request.service_version):
            query['serviceVersion'] = request.service_version
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceProvidersPage',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/sp/api/mseForOam/getServiceProvidersPage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceProvidersPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_providers_page_with_options_async(
        self,
        request: main_models.GetServiceProvidersPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceProvidersPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['appId'] = request.app_id
        if not DaraCore.is_null(request.group):
            query['group'] = request.group
        if not DaraCore.is_null(request.ip):
            query['ip'] = request.ip
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.origin):
            query['origin'] = request.origin
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.registry_type):
            query['registryType'] = request.registry_type
        if not DaraCore.is_null(request.service_id):
            query['serviceId'] = request.service_id
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        if not DaraCore.is_null(request.service_type):
            query['serviceType'] = request.service_type
        if not DaraCore.is_null(request.service_version):
            query['serviceVersion'] = request.service_version
        if not DaraCore.is_null(request.size):
            query['size'] = request.size
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceProvidersPage',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/sp/api/mseForOam/getServiceProvidersPage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceProvidersPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_providers_page(
        self,
        request: main_models.GetServiceProvidersPageRequest,
    ) -> main_models.GetServiceProvidersPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_service_providers_page_with_options(request, headers, runtime)

    async def get_service_providers_page_async(
        self,
        request: main_models.GetServiceProvidersPageRequest,
    ) -> main_models.GetServiceProvidersPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_service_providers_page_with_options_async(request, headers, runtime)

    def get_web_container_config_with_options(
        self,
        request: main_models.GetWebContainerConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWebContainerConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWebContainerConfig',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/oam/web_container_config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWebContainerConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_web_container_config_with_options_async(
        self,
        request: main_models.GetWebContainerConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWebContainerConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWebContainerConfig',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/oam/web_container_config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWebContainerConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_web_container_config(
        self,
        request: main_models.GetWebContainerConfigRequest,
    ) -> main_models.GetWebContainerConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_web_container_config_with_options(request, headers, runtime)

    async def get_web_container_config_async(
        self,
        request: main_models.GetWebContainerConfigRequest,
    ) -> main_models.GetWebContainerConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_web_container_config_with_options_async(request, headers, runtime)

    def import_k8s_cluster_with_options(
        self,
        request: main_models.ImportK8sClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ImportK8sClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.enable_asm):
            query['EnableAsm'] = request.enable_asm
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportK8sCluster',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/import_k8s_cluster',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportK8sClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_k8s_cluster_with_options_async(
        self,
        request: main_models.ImportK8sClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ImportK8sClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.enable_asm):
            query['EnableAsm'] = request.enable_asm
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportK8sCluster',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/import_k8s_cluster',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportK8sClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_k8s_cluster(
        self,
        request: main_models.ImportK8sClusterRequest,
    ) -> main_models.ImportK8sClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.import_k8s_cluster_with_options(request, headers, runtime)

    async def import_k8s_cluster_async(
        self,
        request: main_models.ImportK8sClusterRequest,
    ) -> main_models.ImportK8sClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.import_k8s_cluster_with_options_async(request, headers, runtime)

    def insert_application_with_options(
        self,
        request: main_models.InsertApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.component_ids):
            query['ComponentIds'] = request.component_ids
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ecu_info):
            query['EcuInfo'] = request.ecu_info
        if not DaraCore.is_null(request.enable_port_check):
            query['EnablePortCheck'] = request.enable_port_check
        if not DaraCore.is_null(request.enable_url_check):
            query['EnableUrlCheck'] = request.enable_url_check
        if not DaraCore.is_null(request.health_check_url):
            query['HealthCheckUrl'] = request.health_check_url
        if not DaraCore.is_null(request.hooks):
            query['Hooks'] = request.hooks
        if not DaraCore.is_null(request.jdk):
            query['Jdk'] = request.jdk
        if not DaraCore.is_null(request.jvm_options):
            query['JvmOptions'] = request.jvm_options
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not DaraCore.is_null(request.max_heap_size):
            query['MaxHeapSize'] = request.max_heap_size
        if not DaraCore.is_null(request.max_perm_size):
            query['MaxPermSize'] = request.max_perm_size
        if not DaraCore.is_null(request.mem):
            query['Mem'] = request.mem
        if not DaraCore.is_null(request.min_heap_size):
            query['MinHeapSize'] = request.min_heap_size
        if not DaraCore.is_null(request.package_type):
            query['PackageType'] = request.package_type
        if not DaraCore.is_null(request.reserved_port_str):
            query['ReservedPortStr'] = request.reserved_port_str
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.web_container):
            query['WebContainer'] = request.web_container
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_create_app',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_application_with_options_async(
        self,
        request: main_models.InsertApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.component_ids):
            query['ComponentIds'] = request.component_ids
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ecu_info):
            query['EcuInfo'] = request.ecu_info
        if not DaraCore.is_null(request.enable_port_check):
            query['EnablePortCheck'] = request.enable_port_check
        if not DaraCore.is_null(request.enable_url_check):
            query['EnableUrlCheck'] = request.enable_url_check
        if not DaraCore.is_null(request.health_check_url):
            query['HealthCheckUrl'] = request.health_check_url
        if not DaraCore.is_null(request.hooks):
            query['Hooks'] = request.hooks
        if not DaraCore.is_null(request.jdk):
            query['Jdk'] = request.jdk
        if not DaraCore.is_null(request.jvm_options):
            query['JvmOptions'] = request.jvm_options
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not DaraCore.is_null(request.max_heap_size):
            query['MaxHeapSize'] = request.max_heap_size
        if not DaraCore.is_null(request.max_perm_size):
            query['MaxPermSize'] = request.max_perm_size
        if not DaraCore.is_null(request.mem):
            query['Mem'] = request.mem
        if not DaraCore.is_null(request.min_heap_size):
            query['MinHeapSize'] = request.min_heap_size
        if not DaraCore.is_null(request.package_type):
            query['PackageType'] = request.package_type
        if not DaraCore.is_null(request.reserved_port_str):
            query['ReservedPortStr'] = request.reserved_port_str
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.web_container):
            query['WebContainer'] = request.web_container
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_create_app',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_application(
        self,
        request: main_models.InsertApplicationRequest,
    ) -> main_models.InsertApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.insert_application_with_options(request, headers, runtime)

    async def insert_application_async(
        self,
        request: main_models.InsertApplicationRequest,
    ) -> main_models.InsertApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.insert_application_with_options_async(request, headers, runtime)

    def insert_cluster_with_options(
        self,
        request: main_models.InsertClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.iaas_provider):
            query['IaasProvider'] = request.iaas_provider
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not DaraCore.is_null(request.network_mode):
            query['NetworkMode'] = request.network_mode
        if not DaraCore.is_null(request.oversold_factor):
            query['OversoldFactor'] = request.oversold_factor
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertCluster',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/cluster',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_cluster_with_options_async(
        self,
        request: main_models.InsertClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.iaas_provider):
            query['IaasProvider'] = request.iaas_provider
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not DaraCore.is_null(request.network_mode):
            query['NetworkMode'] = request.network_mode
        if not DaraCore.is_null(request.oversold_factor):
            query['OversoldFactor'] = request.oversold_factor
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertCluster',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/cluster',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_cluster(
        self,
        request: main_models.InsertClusterRequest,
    ) -> main_models.InsertClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.insert_cluster_with_options(request, headers, runtime)

    async def insert_cluster_async(
        self,
        request: main_models.InsertClusterRequest,
    ) -> main_models.InsertClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.insert_cluster_with_options_async(request, headers, runtime)

    def insert_cluster_member_with_options(
        self,
        request: main_models.InsertClusterMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertClusterMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['clusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_ids):
            query['instanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.password):
            query['password'] = request.password
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertClusterMember',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/cluster_member',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertClusterMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_cluster_member_with_options_async(
        self,
        request: main_models.InsertClusterMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertClusterMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['clusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_ids):
            query['instanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.password):
            query['password'] = request.password
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertClusterMember',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/cluster_member',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertClusterMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_cluster_member(
        self,
        request: main_models.InsertClusterMemberRequest,
    ) -> main_models.InsertClusterMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.insert_cluster_member_with_options(request, headers, runtime)

    async def insert_cluster_member_async(
        self,
        request: main_models.InsertClusterMemberRequest,
    ) -> main_models.InsertClusterMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.insert_cluster_member_with_options_async(request, headers, runtime)

    def insert_deploy_group_with_options(
        self,
        request: main_models.InsertDeployGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertDeployGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.init_package_version_id):
            query['InitPackageVersionId'] = request.init_package_version_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertDeployGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/deploy_group',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertDeployGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_deploy_group_with_options_async(
        self,
        request: main_models.InsertDeployGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertDeployGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.init_package_version_id):
            query['InitPackageVersionId'] = request.init_package_version_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertDeployGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/deploy_group',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertDeployGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_deploy_group(
        self,
        request: main_models.InsertDeployGroupRequest,
    ) -> main_models.InsertDeployGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.insert_deploy_group_with_options(request, headers, runtime)

    async def insert_deploy_group_async(
        self,
        request: main_models.InsertDeployGroupRequest,
    ) -> main_models.InsertDeployGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.insert_deploy_group_with_options_async(request, headers, runtime)

    def insert_k8s_application_with_options(
        self,
        request: main_models.InsertK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertK8sApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.app_config):
            query['AppConfig'] = request.app_config
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_template_name):
            query['AppTemplateName'] = request.app_template_name
        if not DaraCore.is_null(request.application_description):
            query['ApplicationDescription'] = request.application_description
        if not DaraCore.is_null(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.command_args):
            query['CommandArgs'] = request.command_args
        if not DaraCore.is_null(request.config_mount_descs):
            query['ConfigMountDescs'] = request.config_mount_descs
        if not DaraCore.is_null(request.container_registry_id):
            query['ContainerRegistryId'] = request.container_registry_id
        if not DaraCore.is_null(request.cs_cluster_id):
            query['CsClusterId'] = request.cs_cluster_id
        if not DaraCore.is_null(request.custom_affinity):
            query['CustomAffinity'] = request.custom_affinity
        if not DaraCore.is_null(request.custom_agent_version):
            query['CustomAgentVersion'] = request.custom_agent_version
        if not DaraCore.is_null(request.custom_tolerations):
            query['CustomTolerations'] = request.custom_tolerations
        if not DaraCore.is_null(request.deploy_across_nodes):
            query['DeployAcrossNodes'] = request.deploy_across_nodes
        if not DaraCore.is_null(request.deploy_across_zones):
            query['DeployAcrossZones'] = request.deploy_across_zones
        if not DaraCore.is_null(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not DaraCore.is_null(request.empty_dirs):
            query['EmptyDirs'] = request.empty_dirs
        if not DaraCore.is_null(request.enable_ahas):
            query['EnableAhas'] = request.enable_ahas
        if not DaraCore.is_null(request.enable_asm):
            query['EnableAsm'] = request.enable_asm
        if not DaraCore.is_null(request.enable_empty_push_reject):
            query['EnableEmptyPushReject'] = request.enable_empty_push_reject
        if not DaraCore.is_null(request.enable_lossless_rule):
            query['EnableLosslessRule'] = request.enable_lossless_rule
        if not DaraCore.is_null(request.env_froms):
            query['EnvFroms'] = request.env_froms
        if not DaraCore.is_null(request.envs):
            query['Envs'] = request.envs
        if not DaraCore.is_null(request.feature_config):
            query['FeatureConfig'] = request.feature_config
        if not DaraCore.is_null(request.image_platforms):
            query['ImagePlatforms'] = request.image_platforms
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not DaraCore.is_null(request.internet_slb_id):
            query['InternetSlbId'] = request.internet_slb_id
        if not DaraCore.is_null(request.internet_slb_port):
            query['InternetSlbPort'] = request.internet_slb_port
        if not DaraCore.is_null(request.internet_slb_protocol):
            query['InternetSlbProtocol'] = request.internet_slb_protocol
        if not DaraCore.is_null(request.internet_target_port):
            query['InternetTargetPort'] = request.internet_target_port
        if not DaraCore.is_null(request.intranet_slb_id):
            query['IntranetSlbId'] = request.intranet_slb_id
        if not DaraCore.is_null(request.intranet_slb_port):
            query['IntranetSlbPort'] = request.intranet_slb_port
        if not DaraCore.is_null(request.intranet_slb_protocol):
            query['IntranetSlbProtocol'] = request.intranet_slb_protocol
        if not DaraCore.is_null(request.intranet_target_port):
            query['IntranetTargetPort'] = request.intranet_target_port
        if not DaraCore.is_null(request.is_multilingual_app):
            query['IsMultilingualApp'] = request.is_multilingual_app
        if not DaraCore.is_null(request.jdk):
            query['JDK'] = request.jdk
        if not DaraCore.is_null(request.java_start_up_config):
            query['JavaStartUpConfig'] = request.java_start_up_config
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.limit_cpu):
            query['LimitCpu'] = request.limit_cpu
        if not DaraCore.is_null(request.limit_ephemeral_storage):
            query['LimitEphemeralStorage'] = request.limit_ephemeral_storage
        if not DaraCore.is_null(request.limit_mem):
            query['LimitMem'] = request.limit_mem
        if not DaraCore.is_null(request.limitm_cpu):
            query['LimitmCpu'] = request.limitm_cpu
        if not DaraCore.is_null(request.liveness):
            query['Liveness'] = request.liveness
        if not DaraCore.is_null(request.local_volume):
            query['LocalVolume'] = request.local_volume
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not DaraCore.is_null(request.lossless_rule_aligned):
            query['LosslessRuleAligned'] = request.lossless_rule_aligned
        if not DaraCore.is_null(request.lossless_rule_delay_time):
            query['LosslessRuleDelayTime'] = request.lossless_rule_delay_time
        if not DaraCore.is_null(request.lossless_rule_func_type):
            query['LosslessRuleFuncType'] = request.lossless_rule_func_type
        if not DaraCore.is_null(request.lossless_rule_related):
            query['LosslessRuleRelated'] = request.lossless_rule_related
        if not DaraCore.is_null(request.lossless_rule_warmup_time):
            query['LosslessRuleWarmupTime'] = request.lossless_rule_warmup_time
        if not DaraCore.is_null(request.mount_descs):
            query['MountDescs'] = request.mount_descs
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.nas_id):
            query['NasId'] = request.nas_id
        if not DaraCore.is_null(request.package_type):
            query['PackageType'] = request.package_type
        if not DaraCore.is_null(request.package_url):
            query['PackageUrl'] = request.package_url
        if not DaraCore.is_null(request.package_version):
            query['PackageVersion'] = request.package_version
        if not DaraCore.is_null(request.post_start):
            query['PostStart'] = request.post_start
        if not DaraCore.is_null(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not DaraCore.is_null(request.pvc_mount_descs):
            query['PvcMountDescs'] = request.pvc_mount_descs
        if not DaraCore.is_null(request.readiness):
            query['Readiness'] = request.readiness
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.requests_cpu):
            query['RequestsCpu'] = request.requests_cpu
        if not DaraCore.is_null(request.requests_ephemeral_storage):
            query['RequestsEphemeralStorage'] = request.requests_ephemeral_storage
        if not DaraCore.is_null(request.requests_mem):
            query['RequestsMem'] = request.requests_mem
        if not DaraCore.is_null(request.requestsm_cpu):
            query['RequestsmCpu'] = request.requestsm_cpu
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.runtime_class_name):
            query['RuntimeClassName'] = request.runtime_class_name
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.security_context):
            query['SecurityContext'] = request.security_context
        if not DaraCore.is_null(request.service_configs):
            query['ServiceConfigs'] = request.service_configs
        if not DaraCore.is_null(request.sidecars):
            query['Sidecars'] = request.sidecars
        if not DaraCore.is_null(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not DaraCore.is_null(request.startup):
            query['Startup'] = request.startup
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.terminate_grace_period):
            query['TerminateGracePeriod'] = request.terminate_grace_period
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.uri_encoding):
            query['UriEncoding'] = request.uri_encoding
        if not DaraCore.is_null(request.use_body_encoding):
            query['UseBodyEncoding'] = request.use_body_encoding
        if not DaraCore.is_null(request.user_base_image_url):
            query['UserBaseImageUrl'] = request.user_base_image_url
        if not DaraCore.is_null(request.web_container):
            query['WebContainer'] = request.web_container
        if not DaraCore.is_null(request.web_container_config):
            query['WebContainerConfig'] = request.web_container_config
        if not DaraCore.is_null(request.workload_type):
            query['WorkloadType'] = request.workload_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertK8sApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/create_k8s_app',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertK8sApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_k8s_application_with_options_async(
        self,
        request: main_models.InsertK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertK8sApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.app_config):
            query['AppConfig'] = request.app_config
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_template_name):
            query['AppTemplateName'] = request.app_template_name
        if not DaraCore.is_null(request.application_description):
            query['ApplicationDescription'] = request.application_description
        if not DaraCore.is_null(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.command):
            query['Command'] = request.command
        if not DaraCore.is_null(request.command_args):
            query['CommandArgs'] = request.command_args
        if not DaraCore.is_null(request.config_mount_descs):
            query['ConfigMountDescs'] = request.config_mount_descs
        if not DaraCore.is_null(request.container_registry_id):
            query['ContainerRegistryId'] = request.container_registry_id
        if not DaraCore.is_null(request.cs_cluster_id):
            query['CsClusterId'] = request.cs_cluster_id
        if not DaraCore.is_null(request.custom_affinity):
            query['CustomAffinity'] = request.custom_affinity
        if not DaraCore.is_null(request.custom_agent_version):
            query['CustomAgentVersion'] = request.custom_agent_version
        if not DaraCore.is_null(request.custom_tolerations):
            query['CustomTolerations'] = request.custom_tolerations
        if not DaraCore.is_null(request.deploy_across_nodes):
            query['DeployAcrossNodes'] = request.deploy_across_nodes
        if not DaraCore.is_null(request.deploy_across_zones):
            query['DeployAcrossZones'] = request.deploy_across_zones
        if not DaraCore.is_null(request.edas_container_version):
            query['EdasContainerVersion'] = request.edas_container_version
        if not DaraCore.is_null(request.empty_dirs):
            query['EmptyDirs'] = request.empty_dirs
        if not DaraCore.is_null(request.enable_ahas):
            query['EnableAhas'] = request.enable_ahas
        if not DaraCore.is_null(request.enable_asm):
            query['EnableAsm'] = request.enable_asm
        if not DaraCore.is_null(request.enable_empty_push_reject):
            query['EnableEmptyPushReject'] = request.enable_empty_push_reject
        if not DaraCore.is_null(request.enable_lossless_rule):
            query['EnableLosslessRule'] = request.enable_lossless_rule
        if not DaraCore.is_null(request.env_froms):
            query['EnvFroms'] = request.env_froms
        if not DaraCore.is_null(request.envs):
            query['Envs'] = request.envs
        if not DaraCore.is_null(request.feature_config):
            query['FeatureConfig'] = request.feature_config
        if not DaraCore.is_null(request.image_platforms):
            query['ImagePlatforms'] = request.image_platforms
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not DaraCore.is_null(request.internet_slb_id):
            query['InternetSlbId'] = request.internet_slb_id
        if not DaraCore.is_null(request.internet_slb_port):
            query['InternetSlbPort'] = request.internet_slb_port
        if not DaraCore.is_null(request.internet_slb_protocol):
            query['InternetSlbProtocol'] = request.internet_slb_protocol
        if not DaraCore.is_null(request.internet_target_port):
            query['InternetTargetPort'] = request.internet_target_port
        if not DaraCore.is_null(request.intranet_slb_id):
            query['IntranetSlbId'] = request.intranet_slb_id
        if not DaraCore.is_null(request.intranet_slb_port):
            query['IntranetSlbPort'] = request.intranet_slb_port
        if not DaraCore.is_null(request.intranet_slb_protocol):
            query['IntranetSlbProtocol'] = request.intranet_slb_protocol
        if not DaraCore.is_null(request.intranet_target_port):
            query['IntranetTargetPort'] = request.intranet_target_port
        if not DaraCore.is_null(request.is_multilingual_app):
            query['IsMultilingualApp'] = request.is_multilingual_app
        if not DaraCore.is_null(request.jdk):
            query['JDK'] = request.jdk
        if not DaraCore.is_null(request.java_start_up_config):
            query['JavaStartUpConfig'] = request.java_start_up_config
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.limit_cpu):
            query['LimitCpu'] = request.limit_cpu
        if not DaraCore.is_null(request.limit_ephemeral_storage):
            query['LimitEphemeralStorage'] = request.limit_ephemeral_storage
        if not DaraCore.is_null(request.limit_mem):
            query['LimitMem'] = request.limit_mem
        if not DaraCore.is_null(request.limitm_cpu):
            query['LimitmCpu'] = request.limitm_cpu
        if not DaraCore.is_null(request.liveness):
            query['Liveness'] = request.liveness
        if not DaraCore.is_null(request.local_volume):
            query['LocalVolume'] = request.local_volume
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not DaraCore.is_null(request.lossless_rule_aligned):
            query['LosslessRuleAligned'] = request.lossless_rule_aligned
        if not DaraCore.is_null(request.lossless_rule_delay_time):
            query['LosslessRuleDelayTime'] = request.lossless_rule_delay_time
        if not DaraCore.is_null(request.lossless_rule_func_type):
            query['LosslessRuleFuncType'] = request.lossless_rule_func_type
        if not DaraCore.is_null(request.lossless_rule_related):
            query['LosslessRuleRelated'] = request.lossless_rule_related
        if not DaraCore.is_null(request.lossless_rule_warmup_time):
            query['LosslessRuleWarmupTime'] = request.lossless_rule_warmup_time
        if not DaraCore.is_null(request.mount_descs):
            query['MountDescs'] = request.mount_descs
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.nas_id):
            query['NasId'] = request.nas_id
        if not DaraCore.is_null(request.package_type):
            query['PackageType'] = request.package_type
        if not DaraCore.is_null(request.package_url):
            query['PackageUrl'] = request.package_url
        if not DaraCore.is_null(request.package_version):
            query['PackageVersion'] = request.package_version
        if not DaraCore.is_null(request.post_start):
            query['PostStart'] = request.post_start
        if not DaraCore.is_null(request.pre_stop):
            query['PreStop'] = request.pre_stop
        if not DaraCore.is_null(request.pvc_mount_descs):
            query['PvcMountDescs'] = request.pvc_mount_descs
        if not DaraCore.is_null(request.readiness):
            query['Readiness'] = request.readiness
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.requests_cpu):
            query['RequestsCpu'] = request.requests_cpu
        if not DaraCore.is_null(request.requests_ephemeral_storage):
            query['RequestsEphemeralStorage'] = request.requests_ephemeral_storage
        if not DaraCore.is_null(request.requests_mem):
            query['RequestsMem'] = request.requests_mem
        if not DaraCore.is_null(request.requestsm_cpu):
            query['RequestsmCpu'] = request.requestsm_cpu
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.runtime_class_name):
            query['RuntimeClassName'] = request.runtime_class_name
        if not DaraCore.is_null(request.secret_name):
            query['SecretName'] = request.secret_name
        if not DaraCore.is_null(request.security_context):
            query['SecurityContext'] = request.security_context
        if not DaraCore.is_null(request.service_configs):
            query['ServiceConfigs'] = request.service_configs
        if not DaraCore.is_null(request.sidecars):
            query['Sidecars'] = request.sidecars
        if not DaraCore.is_null(request.sls_configs):
            query['SlsConfigs'] = request.sls_configs
        if not DaraCore.is_null(request.startup):
            query['Startup'] = request.startup
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.terminate_grace_period):
            query['TerminateGracePeriod'] = request.terminate_grace_period
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        if not DaraCore.is_null(request.uri_encoding):
            query['UriEncoding'] = request.uri_encoding
        if not DaraCore.is_null(request.use_body_encoding):
            query['UseBodyEncoding'] = request.use_body_encoding
        if not DaraCore.is_null(request.user_base_image_url):
            query['UserBaseImageUrl'] = request.user_base_image_url
        if not DaraCore.is_null(request.web_container):
            query['WebContainer'] = request.web_container
        if not DaraCore.is_null(request.web_container_config):
            query['WebContainerConfig'] = request.web_container_config
        if not DaraCore.is_null(request.workload_type):
            query['WorkloadType'] = request.workload_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertK8sApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/create_k8s_app',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertK8sApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_k8s_application(
        self,
        request: main_models.InsertK8sApplicationRequest,
    ) -> main_models.InsertK8sApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.insert_k8s_application_with_options(request, headers, runtime)

    async def insert_k8s_application_async(
        self,
        request: main_models.InsertK8sApplicationRequest,
    ) -> main_models.InsertK8sApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.insert_k8s_application_with_options_async(request, headers, runtime)

    def insert_or_update_region_with_options(
        self,
        request: main_models.InsertOrUpdateRegionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertOrUpdateRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.debug_enable):
            query['DebugEnable'] = request.debug_enable
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.mse_instance_id):
            query['MseInstanceId'] = request.mse_instance_id
        if not DaraCore.is_null(request.region_name):
            query['RegionName'] = request.region_name
        if not DaraCore.is_null(request.region_tag):
            query['RegionTag'] = request.region_tag
        if not DaraCore.is_null(request.registry_type):
            query['RegistryType'] = request.registry_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertOrUpdateRegion',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/user_region_def',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertOrUpdateRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_or_update_region_with_options_async(
        self,
        request: main_models.InsertOrUpdateRegionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertOrUpdateRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.debug_enable):
            query['DebugEnable'] = request.debug_enable
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.mse_instance_id):
            query['MseInstanceId'] = request.mse_instance_id
        if not DaraCore.is_null(request.region_name):
            query['RegionName'] = request.region_name
        if not DaraCore.is_null(request.region_tag):
            query['RegionTag'] = request.region_tag
        if not DaraCore.is_null(request.registry_type):
            query['RegistryType'] = request.registry_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertOrUpdateRegion',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/user_region_def',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertOrUpdateRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_or_update_region(
        self,
        request: main_models.InsertOrUpdateRegionRequest,
    ) -> main_models.InsertOrUpdateRegionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.insert_or_update_region_with_options(request, headers, runtime)

    async def insert_or_update_region_async(
        self,
        request: main_models.InsertOrUpdateRegionRequest,
    ) -> main_models.InsertOrUpdateRegionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.insert_or_update_region_with_options_async(request, headers, runtime)

    def insert_role_with_options(
        self,
        request: main_models.InsertRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_data):
            query['ActionData'] = request.action_data
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertRole',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/create_role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_role_with_options_async(
        self,
        request: main_models.InsertRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_data):
            query['ActionData'] = request.action_data
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertRole',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/create_role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_role(
        self,
        request: main_models.InsertRoleRequest,
    ) -> main_models.InsertRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.insert_role_with_options(request, headers, runtime)

    async def insert_role_async(
        self,
        request: main_models.InsertRoleRequest,
    ) -> main_models.InsertRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.insert_role_with_options_async(request, headers, runtime)

    def insert_service_group_with_options(
        self,
        request: main_models.InsertServiceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertServiceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertServiceGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/service/serviceGroups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_service_group_with_options_async(
        self,
        request: main_models.InsertServiceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertServiceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertServiceGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/service/serviceGroups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_service_group(
        self,
        request: main_models.InsertServiceGroupRequest,
    ) -> main_models.InsertServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.insert_service_group_with_options(request, headers, runtime)

    async def insert_service_group_async(
        self,
        request: main_models.InsertServiceGroupRequest,
    ) -> main_models.InsertServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.insert_service_group_with_options_async(request, headers, runtime)

    def insert_swimming_lane_with_options(
        self,
        request: main_models.InsertSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertSwimmingLaneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_infos):
            query['AppInfos'] = request.app_infos
        if not DaraCore.is_null(request.enable_rules):
            query['EnableRules'] = request.enable_rules
        if not DaraCore.is_null(request.entry_rules):
            query['EntryRules'] = request.entry_rules
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertSwimmingLane',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/trafficmgnt/swimming_lanes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertSwimmingLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_swimming_lane_with_options_async(
        self,
        request: main_models.InsertSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertSwimmingLaneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_infos):
            query['AppInfos'] = request.app_infos
        if not DaraCore.is_null(request.enable_rules):
            query['EnableRules'] = request.enable_rules
        if not DaraCore.is_null(request.entry_rules):
            query['EntryRules'] = request.entry_rules
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertSwimmingLane',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/trafficmgnt/swimming_lanes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertSwimmingLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_swimming_lane(
        self,
        request: main_models.InsertSwimmingLaneRequest,
    ) -> main_models.InsertSwimmingLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.insert_swimming_lane_with_options(request, headers, runtime)

    async def insert_swimming_lane_async(
        self,
        request: main_models.InsertSwimmingLaneRequest,
    ) -> main_models.InsertSwimmingLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.insert_swimming_lane_with_options_async(request, headers, runtime)

    def insert_swimming_lane_group_with_options(
        self,
        request: main_models.InsertSwimmingLaneGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertSwimmingLaneGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.entry_app):
            query['EntryApp'] = request.entry_app
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertSwimmingLaneGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/trafficmgnt/swimming_lane_groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertSwimmingLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_swimming_lane_group_with_options_async(
        self,
        request: main_models.InsertSwimmingLaneGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InsertSwimmingLaneGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.entry_app):
            query['EntryApp'] = request.entry_app
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InsertSwimmingLaneGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/trafficmgnt/swimming_lane_groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InsertSwimmingLaneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_swimming_lane_group(
        self,
        request: main_models.InsertSwimmingLaneGroupRequest,
    ) -> main_models.InsertSwimmingLaneGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.insert_swimming_lane_group_with_options(request, headers, runtime)

    async def insert_swimming_lane_group_async(
        self,
        request: main_models.InsertSwimmingLaneGroupRequest,
    ) -> main_models.InsertSwimmingLaneGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.insert_swimming_lane_group_with_options_async(request, headers, runtime)

    def install_agent_with_options(
        self,
        request: main_models.InstallAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.do_async):
            query['DoAsync'] = request.do_async
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallAgent',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/ecss/install_agent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_agent_with_options_async(
        self,
        request: main_models.InstallAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.do_async):
            query['DoAsync'] = request.do_async
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallAgent',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/ecss/install_agent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_agent(
        self,
        request: main_models.InstallAgentRequest,
    ) -> main_models.InstallAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.install_agent_with_options(request, headers, runtime)

    async def install_agent_async(
        self,
        request: main_models.InstallAgentRequest,
    ) -> main_models.InstallAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.install_agent_with_options_async(request, headers, runtime)

    def list_aliyun_region_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAliyunRegionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListAliyunRegion',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/region_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAliyunRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aliyun_region_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAliyunRegionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListAliyunRegion',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/region_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAliyunRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aliyun_region(self) -> main_models.ListAliyunRegionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_aliyun_region_with_options(headers, runtime)

    async def list_aliyun_region_async(self) -> main_models.ListAliyunRegionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_aliyun_region_with_options_async(headers, runtime)

    def list_application_with_options(
        self,
        request: main_models.ListApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not DaraCore.is_null(request.logical_region_id_filter):
            query['LogicalRegionIdFilter'] = request.logical_region_id_filter
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/app_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_with_options_async(
        self,
        request: main_models.ListApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not DaraCore.is_null(request.logical_region_id_filter):
            query['LogicalRegionIdFilter'] = request.logical_region_id_filter
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/app_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application(
        self,
        request: main_models.ListApplicationRequest,
    ) -> main_models.ListApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_application_with_options(request, headers, runtime)

    async def list_application_async(
        self,
        request: main_models.ListApplicationRequest,
    ) -> main_models.ListApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_application_with_options_async(request, headers, runtime)

    def list_application_ecu_with_options(
        self,
        request: main_models.ListApplicationEcuRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationEcuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationEcu',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/ecu_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationEcuResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_ecu_with_options_async(
        self,
        request: main_models.ListApplicationEcuRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationEcuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationEcu',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/ecu_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationEcuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_ecu(
        self,
        request: main_models.ListApplicationEcuRequest,
    ) -> main_models.ListApplicationEcuResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_application_ecu_with_options(request, headers, runtime)

    async def list_application_ecu_async(
        self,
        request: main_models.ListApplicationEcuRequest,
    ) -> main_models.ListApplicationEcuResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_application_ecu_with_options_async(request, headers, runtime)

    def list_authority_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthorityResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListAuthority',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/authority_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_authority_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthorityResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListAuthority',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/authority_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_authority(self) -> main_models.ListAuthorityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_authority_with_options(headers, runtime)

    async def list_authority_async(self) -> main_models.ListAuthorityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_authority_with_options_async(headers, runtime)

    def list_build_pack_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBuildPackResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListBuildPack',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/build_pack_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBuildPackResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_build_pack_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBuildPackResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListBuildPack',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/build_pack_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBuildPackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_build_pack(self) -> main_models.ListBuildPackResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_build_pack_with_options(headers, runtime)

    async def list_build_pack_async(self) -> main_models.ListBuildPackResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_build_pack_with_options_async(headers, runtime)

    def list_cluster_with_options(
        self,
        request: main_models.ListClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCluster',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/cluster_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_with_options_async(
        self,
        request: main_models.ListClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCluster',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/cluster_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster(
        self,
        request: main_models.ListClusterRequest,
    ) -> main_models.ListClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_cluster_with_options(request, headers, runtime)

    async def list_cluster_async(
        self,
        request: main_models.ListClusterRequest,
    ) -> main_models.ListClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_cluster_with_options_async(request, headers, runtime)

    def list_cluster_members_with_options(
        self,
        request: main_models.ListClusterMembersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ecs_list):
            query['EcsList'] = request.ecs_list
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterMembers',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/cluster_member_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_members_with_options_async(
        self,
        request: main_models.ListClusterMembersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ecs_list):
            query['EcsList'] = request.ecs_list
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterMembers',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/cluster_member_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_members(
        self,
        request: main_models.ListClusterMembersRequest,
    ) -> main_models.ListClusterMembersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_cluster_members_with_options(request, headers, runtime)

    async def list_cluster_members_async(
        self,
        request: main_models.ListClusterMembersRequest,
    ) -> main_models.ListClusterMembersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_cluster_members_with_options_async(request, headers, runtime)

    def list_components_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListComponents',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/components',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_components_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListComponents',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/components',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_components(self) -> main_models.ListComponentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_components_with_options(headers, runtime)

    async def list_components_async(self) -> main_models.ListComponentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_components_with_options_async(headers, runtime)

    def list_config_templates_with_options(
        self,
        request: main_models.ListConfigTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigTemplates',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/config_template',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_templates_with_options_async(
        self,
        request: main_models.ListConfigTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConfigTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConfigTemplates',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/config_template',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConfigTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_templates(
        self,
        request: main_models.ListConfigTemplatesRequest,
    ) -> main_models.ListConfigTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_config_templates_with_options(request, headers, runtime)

    async def list_config_templates_async(
        self,
        request: main_models.ListConfigTemplatesRequest,
    ) -> main_models.ListConfigTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_config_templates_with_options_async(request, headers, runtime)

    def list_consumed_services_with_options(
        self,
        request: main_models.ListConsumedServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumedServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumedServices',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/service/listConsumedServices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumedServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumed_services_with_options_async(
        self,
        request: main_models.ListConsumedServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumedServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumedServices',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/service/listConsumedServices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumedServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumed_services(
        self,
        request: main_models.ListConsumedServicesRequest,
    ) -> main_models.ListConsumedServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_consumed_services_with_options(request, headers, runtime)

    async def list_consumed_services_async(
        self,
        request: main_models.ListConsumedServicesRequest,
    ) -> main_models.ListConsumedServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_consumed_services_with_options_async(request, headers, runtime)

    def list_convertable_ecu_with_options(
        self,
        request: main_models.ListConvertableEcuRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConvertableEcuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['clusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConvertableEcu',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/convertable_ecu_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConvertableEcuResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_convertable_ecu_with_options_async(
        self,
        request: main_models.ListConvertableEcuRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConvertableEcuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['clusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConvertableEcu',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/convertable_ecu_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConvertableEcuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_convertable_ecu(
        self,
        request: main_models.ListConvertableEcuRequest,
    ) -> main_models.ListConvertableEcuResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_convertable_ecu_with_options(request, headers, runtime)

    async def list_convertable_ecu_async(
        self,
        request: main_models.ListConvertableEcuRequest,
    ) -> main_models.ListConvertableEcuResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_convertable_ecu_with_options_async(request, headers, runtime)

    def list_deploy_group_with_options(
        self,
        request: main_models.ListDeployGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDeployGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeployGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/deploy_group_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeployGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deploy_group_with_options_async(
        self,
        request: main_models.ListDeployGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDeployGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeployGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/deploy_group_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeployGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deploy_group(
        self,
        request: main_models.ListDeployGroupRequest,
    ) -> main_models.ListDeployGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_deploy_group_with_options(request, headers, runtime)

    async def list_deploy_group_async(
        self,
        request: main_models.ListDeployGroupRequest,
    ) -> main_models.ListDeployGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_deploy_group_with_options_async(request, headers, runtime)

    def list_ecs_not_in_cluster_with_options(
        self,
        request: main_models.ListEcsNotInClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEcsNotInClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_mode):
            query['NetworkMode'] = request.network_mode
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEcsNotInCluster',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/ecs_not_in_cluster',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEcsNotInClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ecs_not_in_cluster_with_options_async(
        self,
        request: main_models.ListEcsNotInClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEcsNotInClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_mode):
            query['NetworkMode'] = request.network_mode
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEcsNotInCluster',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/ecs_not_in_cluster',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEcsNotInClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ecs_not_in_cluster(
        self,
        request: main_models.ListEcsNotInClusterRequest,
    ) -> main_models.ListEcsNotInClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_ecs_not_in_cluster_with_options(request, headers, runtime)

    async def list_ecs_not_in_cluster_async(
        self,
        request: main_models.ListEcsNotInClusterRequest,
    ) -> main_models.ListEcsNotInClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ecs_not_in_cluster_with_options_async(request, headers, runtime)

    def list_ecu_by_region_with_options(
        self,
        request: main_models.ListEcuByRegionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEcuByRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.act):
            query['Act'] = request.act
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEcuByRegion',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/ecu_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEcuByRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ecu_by_region_with_options_async(
        self,
        request: main_models.ListEcuByRegionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEcuByRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.act):
            query['Act'] = request.act
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEcuByRegion',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/ecu_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEcuByRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ecu_by_region(
        self,
        request: main_models.ListEcuByRegionRequest,
    ) -> main_models.ListEcuByRegionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_ecu_by_region_with_options(request, headers, runtime)

    async def list_ecu_by_region_async(
        self,
        request: main_models.ListEcuByRegionRequest,
    ) -> main_models.ListEcuByRegionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ecu_by_region_with_options_async(request, headers, runtime)

    def list_history_deploy_version_with_options(
        self,
        request: main_models.ListHistoryDeployVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListHistoryDeployVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHistoryDeployVersion',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/deploy_history_version_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHistoryDeployVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_history_deploy_version_with_options_async(
        self,
        request: main_models.ListHistoryDeployVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListHistoryDeployVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHistoryDeployVersion',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/deploy_history_version_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHistoryDeployVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_history_deploy_version(
        self,
        request: main_models.ListHistoryDeployVersionRequest,
    ) -> main_models.ListHistoryDeployVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_history_deploy_version_with_options(request, headers, runtime)

    async def list_history_deploy_version_async(
        self,
        request: main_models.ListHistoryDeployVersionRequest,
    ) -> main_models.ListHistoryDeployVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_history_deploy_version_with_options_async(request, headers, runtime)

    def list_k8s_config_maps_with_options(
        self,
        request: main_models.ListK8sConfigMapsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListK8sConfigMapsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.condition):
            query['Condition'] = request.condition
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.show_related_apps):
            query['ShowRelatedApps'] = request.show_related_apps
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListK8sConfigMaps',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_config_map',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListK8sConfigMapsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_k8s_config_maps_with_options_async(
        self,
        request: main_models.ListK8sConfigMapsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListK8sConfigMapsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.condition):
            query['Condition'] = request.condition
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.show_related_apps):
            query['ShowRelatedApps'] = request.show_related_apps
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListK8sConfigMaps',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_config_map',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListK8sConfigMapsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_k8s_config_maps(
        self,
        request: main_models.ListK8sConfigMapsRequest,
    ) -> main_models.ListK8sConfigMapsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_k8s_config_maps_with_options(request, headers, runtime)

    async def list_k8s_config_maps_async(
        self,
        request: main_models.ListK8sConfigMapsRequest,
    ) -> main_models.ListK8sConfigMapsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_k8s_config_maps_with_options_async(request, headers, runtime)

    def list_k8s_ingress_rules_with_options(
        self,
        request: main_models.ListK8sIngressRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListK8sIngressRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.condition):
            query['Condition'] = request.condition
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListK8sIngressRules',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_ingress',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListK8sIngressRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_k8s_ingress_rules_with_options_async(
        self,
        request: main_models.ListK8sIngressRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListK8sIngressRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.condition):
            query['Condition'] = request.condition
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListK8sIngressRules',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_ingress',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListK8sIngressRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_k8s_ingress_rules(
        self,
        request: main_models.ListK8sIngressRulesRequest,
    ) -> main_models.ListK8sIngressRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_k8s_ingress_rules_with_options(request, headers, runtime)

    async def list_k8s_ingress_rules_async(
        self,
        request: main_models.ListK8sIngressRulesRequest,
    ) -> main_models.ListK8sIngressRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_k8s_ingress_rules_with_options_async(request, headers, runtime)

    def list_k8s_namespaces_with_options(
        self,
        request: main_models.ListK8sNamespacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListK8sNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListK8sNamespaces',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_namespace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListK8sNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_k8s_namespaces_with_options_async(
        self,
        request: main_models.ListK8sNamespacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListK8sNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListK8sNamespaces',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_namespace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListK8sNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_k8s_namespaces(
        self,
        request: main_models.ListK8sNamespacesRequest,
    ) -> main_models.ListK8sNamespacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_k8s_namespaces_with_options(request, headers, runtime)

    async def list_k8s_namespaces_async(
        self,
        request: main_models.ListK8sNamespacesRequest,
    ) -> main_models.ListK8sNamespacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_k8s_namespaces_with_options_async(request, headers, runtime)

    def list_k8s_secrets_with_options(
        self,
        request: main_models.ListK8sSecretsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListK8sSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.condition):
            query['Condition'] = request.condition
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.show_related_apps):
            query['ShowRelatedApps'] = request.show_related_apps
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListK8sSecrets',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_secret',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListK8sSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_k8s_secrets_with_options_async(
        self,
        request: main_models.ListK8sSecretsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListK8sSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.condition):
            query['Condition'] = request.condition
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.show_related_apps):
            query['ShowRelatedApps'] = request.show_related_apps
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListK8sSecrets',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_secret',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListK8sSecretsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_k8s_secrets(
        self,
        request: main_models.ListK8sSecretsRequest,
    ) -> main_models.ListK8sSecretsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_k8s_secrets_with_options(request, headers, runtime)

    async def list_k8s_secrets_async(
        self,
        request: main_models.ListK8sSecretsRequest,
    ) -> main_models.ListK8sSecretsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_k8s_secrets_with_options_async(request, headers, runtime)

    def list_methods_with_options(
        self,
        request: main_models.ListMethodsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMethodsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMethods',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/service/list_methods',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMethodsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_methods_with_options_async(
        self,
        request: main_models.ListMethodsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMethodsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMethods',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/service/list_methods',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMethodsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_methods(
        self,
        request: main_models.ListMethodsRequest,
    ) -> main_models.ListMethodsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_methods_with_options(request, headers, runtime)

    async def list_methods_async(
        self,
        request: main_models.ListMethodsRequest,
    ) -> main_models.ListMethodsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_methods_with_options_async(request, headers, runtime)

    def list_published_services_with_options(
        self,
        request: main_models.ListPublishedServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPublishedServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPublishedServices',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/service/listPublishedServices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPublishedServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_published_services_with_options_async(
        self,
        request: main_models.ListPublishedServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPublishedServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPublishedServices',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/service/listPublishedServices',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPublishedServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_published_services(
        self,
        request: main_models.ListPublishedServicesRequest,
    ) -> main_models.ListPublishedServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_published_services_with_options(request, headers, runtime)

    async def list_published_services_async(
        self,
        request: main_models.ListPublishedServicesRequest,
    ) -> main_models.ListPublishedServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_published_services_with_options_async(request, headers, runtime)

    def list_recent_change_order_with_options(
        self,
        request: main_models.ListRecentChangeOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRecentChangeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecentChangeOrder',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/change_order_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecentChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recent_change_order_with_options_async(
        self,
        request: main_models.ListRecentChangeOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRecentChangeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecentChangeOrder',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/change_order_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecentChangeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recent_change_order(
        self,
        request: main_models.ListRecentChangeOrderRequest,
    ) -> main_models.ListRecentChangeOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_recent_change_order_with_options(request, headers, runtime)

    async def list_recent_change_order_async(
        self,
        request: main_models.ListRecentChangeOrderRequest,
    ) -> main_models.ListRecentChangeOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_recent_change_order_with_options_async(request, headers, runtime)

    def list_resource_group_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/reg_group_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_group_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/reg_group_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_group(self) -> main_models.ListResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_resource_group_with_options(headers, runtime)

    async def list_resource_group_async(self) -> main_models.ListResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_resource_group_with_options_async(headers, runtime)

    def list_role_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListRole',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/role_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_role_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListRole',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/role_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_role(self) -> main_models.ListRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_role_with_options(headers, runtime)

    async def list_role_async(self) -> main_models.ListRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_role_with_options_async(headers, runtime)

    def list_scale_out_ecu_with_options(
        self,
        request: main_models.ListScaleOutEcuRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListScaleOutEcuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_num):
            query['InstanceNum'] = request.instance_num
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not DaraCore.is_null(request.mem):
            query['Mem'] = request.mem
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScaleOutEcu',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/scale_out_ecu_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScaleOutEcuResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scale_out_ecu_with_options_async(
        self,
        request: main_models.ListScaleOutEcuRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListScaleOutEcuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cpu):
            query['Cpu'] = request.cpu
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_num):
            query['InstanceNum'] = request.instance_num
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        if not DaraCore.is_null(request.mem):
            query['Mem'] = request.mem
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScaleOutEcu',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/scale_out_ecu_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScaleOutEcuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scale_out_ecu(
        self,
        request: main_models.ListScaleOutEcuRequest,
    ) -> main_models.ListScaleOutEcuResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_scale_out_ecu_with_options(request, headers, runtime)

    async def list_scale_out_ecu_async(
        self,
        request: main_models.ListScaleOutEcuRequest,
    ) -> main_models.ListScaleOutEcuResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_scale_out_ecu_with_options_async(request, headers, runtime)

    def list_service_groups_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceGroupsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListServiceGroups',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/service/serviceGroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_groups_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceGroupsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListServiceGroups',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/service/serviceGroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_groups(self) -> main_models.ListServiceGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_service_groups_with_options(headers, runtime)

    async def list_service_groups_async(self) -> main_models.ListServiceGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_service_groups_with_options_async(headers, runtime)

    def list_slb_with_options(
        self,
        request: main_models.ListSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.slb_type):
            query['SlbType'] = request.slb_type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSlb',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/slb_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_slb_with_options_async(
        self,
        request: main_models.ListSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_type):
            query['AddressType'] = request.address_type
        if not DaraCore.is_null(request.slb_type):
            query['SlbType'] = request.slb_type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSlb',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/slb_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_slb(
        self,
        request: main_models.ListSlbRequest,
    ) -> main_models.ListSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_slb_with_options(request, headers, runtime)

    async def list_slb_async(
        self,
        request: main_models.ListSlbRequest,
    ) -> main_models.ListSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_slb_with_options_async(request, headers, runtime)

    def list_sub_account_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSubAccountResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSubAccount',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/sub_account_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sub_account_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSubAccountResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSubAccount',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/sub_account_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sub_account(self) -> main_models.ListSubAccountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_sub_account_with_options(headers, runtime)

    async def list_sub_account_async(self) -> main_models.ListSubAccountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_sub_account_with_options_async(headers, runtime)

    def list_swimming_lane_with_options(
        self,
        request: main_models.ListSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSwimmingLaneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSwimmingLane',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/trafficmgnt/swimming_lanes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSwimmingLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_swimming_lane_with_options_async(
        self,
        request: main_models.ListSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSwimmingLaneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSwimmingLane',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/trafficmgnt/swimming_lanes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSwimmingLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_swimming_lane(
        self,
        request: main_models.ListSwimmingLaneRequest,
    ) -> main_models.ListSwimmingLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_swimming_lane_with_options(request, headers, runtime)

    async def list_swimming_lane_async(
        self,
        request: main_models.ListSwimmingLaneRequest,
    ) -> main_models.ListSwimmingLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_swimming_lane_with_options_async(request, headers, runtime)

    def list_swimming_lane_group_with_options(
        self,
        request: main_models.ListSwimmingLaneGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSwimmingLaneGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSwimmingLaneGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/trafficmgnt/swimming_lane_groups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSwimmingLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_swimming_lane_group_with_options_async(
        self,
        request: main_models.ListSwimmingLaneGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSwimmingLaneGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSwimmingLaneGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/trafficmgnt/swimming_lane_groups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSwimmingLaneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_swimming_lane_group(
        self,
        request: main_models.ListSwimmingLaneGroupRequest,
    ) -> main_models.ListSwimmingLaneGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_swimming_lane_group_with_options(request, headers, runtime)

    async def list_swimming_lane_group_async(
        self,
        request: main_models.ListSwimmingLaneGroupRequest,
    ) -> main_models.ListSwimmingLaneGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_swimming_lane_group_with_options_async(request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/tag/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/tag/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def list_user_define_region_with_options(
        self,
        request: main_models.ListUserDefineRegionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserDefineRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.debug_enable):
            query['DebugEnable'] = request.debug_enable
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserDefineRegion',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/user_region_defs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserDefineRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_define_region_with_options_async(
        self,
        request: main_models.ListUserDefineRegionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserDefineRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.debug_enable):
            query['DebugEnable'] = request.debug_enable
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserDefineRegion',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/user_region_defs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserDefineRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_define_region(
        self,
        request: main_models.ListUserDefineRegionRequest,
    ) -> main_models.ListUserDefineRegionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_user_define_region_with_options(request, headers, runtime)

    async def list_user_define_region_async(
        self,
        request: main_models.ListUserDefineRegionRequest,
    ) -> main_models.ListUserDefineRegionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_user_define_region_with_options_async(request, headers, runtime)

    def list_vpc_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListVpc',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/vpc_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vpc_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVpcResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListVpc',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/vpc_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vpc(self) -> main_models.ListVpcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_vpc_with_options(headers, runtime)

    async def list_vpc_async(self) -> main_models.ListVpcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_vpc_with_options_async(headers, runtime)

    def migrate_application_with_options(
        self,
        request: main_models.MigrateApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MigrateApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['appIds'] = request.app_ids
        if not DaraCore.is_null(request.cmd):
            query['cmd'] = request.cmd
        if not DaraCore.is_null(request.config):
            query['config'] = request.config
        if not DaraCore.is_null(request.raw_data):
            query['rawData'] = request.raw_data
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MigrateApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/migrateK8sApp',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_application_with_options_async(
        self,
        request: main_models.MigrateApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MigrateApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['appIds'] = request.app_ids
        if not DaraCore.is_null(request.cmd):
            query['cmd'] = request.cmd
        if not DaraCore.is_null(request.config):
            query['config'] = request.config
        if not DaraCore.is_null(request.raw_data):
            query['rawData'] = request.raw_data
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MigrateApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/migrateK8sApp',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_application(
        self,
        request: main_models.MigrateApplicationRequest,
    ) -> main_models.MigrateApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.migrate_application_with_options(request, headers, runtime)

    async def migrate_application_async(
        self,
        request: main_models.MigrateApplicationRequest,
    ) -> main_models.MigrateApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.migrate_application_with_options_async(request, headers, runtime)

    def migrate_ecu_with_options(
        self,
        request: main_models.MigrateEcuRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MigrateEcuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MigrateEcu',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/migrate_ecu',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateEcuResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_ecu_with_options_async(
        self,
        request: main_models.MigrateEcuRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MigrateEcuResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MigrateEcu',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/migrate_ecu',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateEcuResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_ecu(
        self,
        request: main_models.MigrateEcuRequest,
    ) -> main_models.MigrateEcuResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.migrate_ecu_with_options(request, headers, runtime)

    async def migrate_ecu_async(
        self,
        request: main_models.MigrateEcuRequest,
    ) -> main_models.MigrateEcuResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.migrate_ecu_with_options_async(request, headers, runtime)

    def modify_scaling_rule_with_options(
        self,
        request: main_models.ModifyScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_eula):
            query['AcceptEULA'] = request.accept_eula
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.in_condition):
            query['InCondition'] = request.in_condition
        if not DaraCore.is_null(request.in_cpu):
            query['InCpu'] = request.in_cpu
        if not DaraCore.is_null(request.in_duration):
            query['InDuration'] = request.in_duration
        if not DaraCore.is_null(request.in_enable):
            query['InEnable'] = request.in_enable
        if not DaraCore.is_null(request.in_instance_num):
            query['InInstanceNum'] = request.in_instance_num
        if not DaraCore.is_null(request.in_load):
            query['InLoad'] = request.in_load
        if not DaraCore.is_null(request.in_rt):
            query['InRT'] = request.in_rt
        if not DaraCore.is_null(request.in_step):
            query['InStep'] = request.in_step
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.multi_az_policy):
            query['MultiAzPolicy'] = request.multi_az_policy
        if not DaraCore.is_null(request.out_cpu):
            query['OutCPU'] = request.out_cpu
        if not DaraCore.is_null(request.out_condition):
            query['OutCondition'] = request.out_condition
        if not DaraCore.is_null(request.out_duration):
            query['OutDuration'] = request.out_duration
        if not DaraCore.is_null(request.out_enable):
            query['OutEnable'] = request.out_enable
        if not DaraCore.is_null(request.out_instance_num):
            query['OutInstanceNum'] = request.out_instance_num
        if not DaraCore.is_null(request.out_load):
            query['OutLoad'] = request.out_load
        if not DaraCore.is_null(request.out_rt):
            query['OutRT'] = request.out_rt
        if not DaraCore.is_null(request.out_step):
            query['OutStep'] = request.out_step
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.resource_from):
            query['ResourceFrom'] = request.resource_from
        if not DaraCore.is_null(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_instance_id):
            query['TemplateInstanceId'] = request.template_instance_id
        if not DaraCore.is_null(request.template_instance_name):
            query['TemplateInstanceName'] = request.template_instance_name
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScalingRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/scaling_rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_rule_with_options_async(
        self,
        request: main_models.ModifyScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_eula):
            query['AcceptEULA'] = request.accept_eula
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.in_condition):
            query['InCondition'] = request.in_condition
        if not DaraCore.is_null(request.in_cpu):
            query['InCpu'] = request.in_cpu
        if not DaraCore.is_null(request.in_duration):
            query['InDuration'] = request.in_duration
        if not DaraCore.is_null(request.in_enable):
            query['InEnable'] = request.in_enable
        if not DaraCore.is_null(request.in_instance_num):
            query['InInstanceNum'] = request.in_instance_num
        if not DaraCore.is_null(request.in_load):
            query['InLoad'] = request.in_load
        if not DaraCore.is_null(request.in_rt):
            query['InRT'] = request.in_rt
        if not DaraCore.is_null(request.in_step):
            query['InStep'] = request.in_step
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.multi_az_policy):
            query['MultiAzPolicy'] = request.multi_az_policy
        if not DaraCore.is_null(request.out_cpu):
            query['OutCPU'] = request.out_cpu
        if not DaraCore.is_null(request.out_condition):
            query['OutCondition'] = request.out_condition
        if not DaraCore.is_null(request.out_duration):
            query['OutDuration'] = request.out_duration
        if not DaraCore.is_null(request.out_enable):
            query['OutEnable'] = request.out_enable
        if not DaraCore.is_null(request.out_instance_num):
            query['OutInstanceNum'] = request.out_instance_num
        if not DaraCore.is_null(request.out_load):
            query['OutLoad'] = request.out_load
        if not DaraCore.is_null(request.out_rt):
            query['OutRT'] = request.out_rt
        if not DaraCore.is_null(request.out_step):
            query['OutStep'] = request.out_step
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.resource_from):
            query['ResourceFrom'] = request.resource_from
        if not DaraCore.is_null(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_instance_id):
            query['TemplateInstanceId'] = request.template_instance_id
        if not DaraCore.is_null(request.template_instance_name):
            query['TemplateInstanceName'] = request.template_instance_name
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyScalingRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/scaling_rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scaling_rule(
        self,
        request: main_models.ModifyScalingRuleRequest,
    ) -> main_models.ModifyScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_scaling_rule_with_options(request, headers, runtime)

    async def modify_scaling_rule_async(
        self,
        request: main_models.ModifyScalingRuleRequest,
    ) -> main_models.ModifyScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_scaling_rule_with_options_async(request, headers, runtime)

    def query_application_status_with_options(
        self,
        request: main_models.QueryApplicationStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryApplicationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryApplicationStatus',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/app_status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryApplicationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_application_status_with_options_async(
        self,
        request: main_models.QueryApplicationStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryApplicationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryApplicationStatus',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/app_status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryApplicationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_application_status(
        self,
        request: main_models.QueryApplicationStatusRequest,
    ) -> main_models.QueryApplicationStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_application_status_with_options(request, headers, runtime)

    async def query_application_status_async(
        self,
        request: main_models.QueryApplicationStatusRequest,
    ) -> main_models.QueryApplicationStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_application_status_with_options_async(request, headers, runtime)

    def query_ecc_info_with_options(
        self,
        request: main_models.QueryEccInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryEccInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ecc_id):
            query['EccId'] = request.ecc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEccInfo',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/ecc',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEccInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_ecc_info_with_options_async(
        self,
        request: main_models.QueryEccInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryEccInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ecc_id):
            query['EccId'] = request.ecc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEccInfo',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/ecc',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEccInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_ecc_info(
        self,
        request: main_models.QueryEccInfoRequest,
    ) -> main_models.QueryEccInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_ecc_info_with_options(request, headers, runtime)

    async def query_ecc_info_async(
        self,
        request: main_models.QueryEccInfoRequest,
    ) -> main_models.QueryEccInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_ecc_info_with_options_async(request, headers, runtime)

    def query_migrate_ecu_list_with_options(
        self,
        request: main_models.QueryMigrateEcuListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryMigrateEcuListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMigrateEcuList',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/migrate_ecu_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMigrateEcuListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_migrate_ecu_list_with_options_async(
        self,
        request: main_models.QueryMigrateEcuListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryMigrateEcuListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMigrateEcuList',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/migrate_ecu_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMigrateEcuListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_migrate_ecu_list(
        self,
        request: main_models.QueryMigrateEcuListRequest,
    ) -> main_models.QueryMigrateEcuListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_migrate_ecu_list_with_options(request, headers, runtime)

    async def query_migrate_ecu_list_async(
        self,
        request: main_models.QueryMigrateEcuListRequest,
    ) -> main_models.QueryMigrateEcuListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_migrate_ecu_list_with_options_async(request, headers, runtime)

    def query_migrate_region_list_with_options(
        self,
        request: main_models.QueryMigrateRegionListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryMigrateRegionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMigrateRegionList',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/migrate_region_select',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMigrateRegionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_migrate_region_list_with_options_async(
        self,
        request: main_models.QueryMigrateRegionListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryMigrateRegionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.logical_region_id):
            query['LogicalRegionId'] = request.logical_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMigrateRegionList',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/migrate_region_select',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMigrateRegionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_migrate_region_list(
        self,
        request: main_models.QueryMigrateRegionListRequest,
    ) -> main_models.QueryMigrateRegionListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_migrate_region_list_with_options(request, headers, runtime)

    async def query_migrate_region_list_async(
        self,
        request: main_models.QueryMigrateRegionListRequest,
    ) -> main_models.QueryMigrateRegionListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_migrate_region_list_with_options_async(request, headers, runtime)

    def query_region_config_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryRegionConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'QueryRegionConfig',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/region_config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRegionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_region_config_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryRegionConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'QueryRegionConfig',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/region_config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRegionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_region_config(self) -> main_models.QueryRegionConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_region_config_with_options(headers, runtime)

    async def query_region_config_async(self) -> main_models.QueryRegionConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_region_config_with_options_async(headers, runtime)

    def query_sls_log_store_list_with_options(
        self,
        request: main_models.QuerySlsLogStoreListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QuerySlsLogStoreListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySlsLogStoreList',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/sls/query_sls_log_store_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySlsLogStoreListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sls_log_store_list_with_options_async(
        self,
        request: main_models.QuerySlsLogStoreListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QuerySlsLogStoreListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySlsLogStoreList',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/sls/query_sls_log_store_list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySlsLogStoreListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sls_log_store_list(
        self,
        request: main_models.QuerySlsLogStoreListRequest,
    ) -> main_models.QuerySlsLogStoreListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_sls_log_store_list_with_options(request, headers, runtime)

    async def query_sls_log_store_list_async(
        self,
        request: main_models.QuerySlsLogStoreListRequest,
    ) -> main_models.QuerySlsLogStoreListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_sls_log_store_list_with_options_async(request, headers, runtime)

    def reset_application_with_options(
        self,
        request: main_models.ResetApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_reset',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_application_with_options_async(
        self,
        request: main_models.ResetApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_reset',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_application(
        self,
        request: main_models.ResetApplicationRequest,
    ) -> main_models.ResetApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.reset_application_with_options(request, headers, runtime)

    async def reset_application_async(
        self,
        request: main_models.ResetApplicationRequest,
    ) -> main_models.ResetApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.reset_application_with_options_async(request, headers, runtime)

    def restart_application_with_options(
        self,
        request: main_models.RestartApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_application_with_options_async(
        self,
        request: main_models.RestartApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_application(
        self,
        request: main_models.RestartApplicationRequest,
    ) -> main_models.RestartApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restart_application_with_options(request, headers, runtime)

    async def restart_application_async(
        self,
        request: main_models.RestartApplicationRequest,
    ) -> main_models.RestartApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restart_application_with_options_async(request, headers, runtime)

    def restart_k8s_application_with_options(
        self,
        request: main_models.RestartK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartK8sApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartK8sApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/restart_k8s_app',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartK8sApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_k8s_application_with_options_async(
        self,
        request: main_models.RestartK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartK8sApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartK8sApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/restart_k8s_app',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartK8sApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_k8s_application(
        self,
        request: main_models.RestartK8sApplicationRequest,
    ) -> main_models.RestartK8sApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restart_k8s_application_with_options(request, headers, runtime)

    async def restart_k8s_application_async(
        self,
        request: main_models.RestartK8sApplicationRequest,
    ) -> main_models.RestartK8sApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restart_k8s_application_with_options_async(request, headers, runtime)

    def retry_change_order_task_with_options(
        self,
        request: main_models.RetryChangeOrderTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RetryChangeOrderTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.retry_status):
            query['RetryStatus'] = request.retry_status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetryChangeOrderTask',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/task_retry',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryChangeOrderTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_change_order_task_with_options_async(
        self,
        request: main_models.RetryChangeOrderTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RetryChangeOrderTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.retry_status):
            query['RetryStatus'] = request.retry_status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetryChangeOrderTask',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/task_retry',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryChangeOrderTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_change_order_task(
        self,
        request: main_models.RetryChangeOrderTaskRequest,
    ) -> main_models.RetryChangeOrderTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.retry_change_order_task_with_options(request, headers, runtime)

    async def retry_change_order_task_async(
        self,
        request: main_models.RetryChangeOrderTaskRequest,
    ) -> main_models.RetryChangeOrderTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.retry_change_order_task_with_options_async(request, headers, runtime)

    def rollback_application_with_options(
        self,
        request: main_models.RollbackApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RollbackApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.batch):
            query['Batch'] = request.batch
        if not DaraCore.is_null(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.history_version):
            query['HistoryVersion'] = request.history_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_rollback',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_application_with_options_async(
        self,
        request: main_models.RollbackApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RollbackApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.batch):
            query['Batch'] = request.batch
        if not DaraCore.is_null(request.batch_wait_time):
            query['BatchWaitTime'] = request.batch_wait_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.history_version):
            query['HistoryVersion'] = request.history_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_rollback',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_application(
        self,
        request: main_models.RollbackApplicationRequest,
    ) -> main_models.RollbackApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.rollback_application_with_options(request, headers, runtime)

    async def rollback_application_async(
        self,
        request: main_models.RollbackApplicationRequest,
    ) -> main_models.RollbackApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.rollback_application_with_options_async(request, headers, runtime)

    def rollback_change_order_with_options(
        self,
        request: main_models.RollbackChangeOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RollbackChangeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackChangeOrder',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/oam/changeorder/rollback',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackChangeOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_change_order_with_options_async(
        self,
        request: main_models.RollbackChangeOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RollbackChangeOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackChangeOrder',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/oam/changeorder/rollback',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackChangeOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_change_order(
        self,
        request: main_models.RollbackChangeOrderRequest,
    ) -> main_models.RollbackChangeOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.rollback_change_order_with_options(request, headers, runtime)

    async def rollback_change_order_async(
        self,
        request: main_models.RollbackChangeOrderRequest,
    ) -> main_models.RollbackChangeOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.rollback_change_order_with_options_async(request, headers, runtime)

    def scale_in_application_with_options(
        self,
        request: main_models.ScaleInApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleInApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        if not DaraCore.is_null(request.force_status):
            query['ForceStatus'] = request.force_status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScaleInApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_scale_in',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleInApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_in_application_with_options_async(
        self,
        request: main_models.ScaleInApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleInApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        if not DaraCore.is_null(request.force_status):
            query['ForceStatus'] = request.force_status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScaleInApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_scale_in',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleInApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_in_application(
        self,
        request: main_models.ScaleInApplicationRequest,
    ) -> main_models.ScaleInApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.scale_in_application_with_options(request, headers, runtime)

    async def scale_in_application_async(
        self,
        request: main_models.ScaleInApplicationRequest,
    ) -> main_models.ScaleInApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.scale_in_application_with_options_async(request, headers, runtime)

    def scale_k8s_application_with_options(
        self,
        request: main_models.ScaleK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleK8sApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScaleK8sApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_apps',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleK8sApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_k8s_application_with_options_async(
        self,
        request: main_models.ScaleK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleK8sApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScaleK8sApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_apps',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleK8sApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_k8s_application(
        self,
        request: main_models.ScaleK8sApplicationRequest,
    ) -> main_models.ScaleK8sApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.scale_k8s_application_with_options(request, headers, runtime)

    async def scale_k8s_application_async(
        self,
        request: main_models.ScaleK8sApplicationRequest,
    ) -> main_models.ScaleK8sApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.scale_k8s_application_with_options_async(request, headers, runtime)

    def scale_out_application_with_options(
        self,
        request: main_models.ScaleOutApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleOutApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.deploy_group):
            query['DeployGroup'] = request.deploy_group
        if not DaraCore.is_null(request.ecu_info):
            query['EcuInfo'] = request.ecu_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScaleOutApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_scale_out',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleOutApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_out_application_with_options_async(
        self,
        request: main_models.ScaleOutApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleOutApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.deploy_group):
            query['DeployGroup'] = request.deploy_group
        if not DaraCore.is_null(request.ecu_info):
            query['EcuInfo'] = request.ecu_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScaleOutApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_scale_out',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleOutApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_out_application(
        self,
        request: main_models.ScaleOutApplicationRequest,
    ) -> main_models.ScaleOutApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.scale_out_application_with_options(request, headers, runtime)

    async def scale_out_application_async(
        self,
        request: main_models.ScaleOutApplicationRequest,
    ) -> main_models.ScaleOutApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.scale_out_application_with_options_async(request, headers, runtime)

    def scaleout_application_with_new_instances_with_options(
        self,
        request: main_models.ScaleoutApplicationWithNewInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleoutApplicationWithNewInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_charge_period):
            query['InstanceChargePeriod'] = request.instance_charge_period
        if not DaraCore.is_null(request.instance_charge_period_unit):
            query['InstanceChargePeriodUnit'] = request.instance_charge_period_unit
        if not DaraCore.is_null(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not DaraCore.is_null(request.scaling_num):
            query['ScalingNum'] = request.scaling_num
        if not DaraCore.is_null(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_instance_id):
            query['TemplateInstanceId'] = request.template_instance_id
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScaleoutApplicationWithNewInstances',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/scaling/scale_out',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleoutApplicationWithNewInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def scaleout_application_with_new_instances_with_options_async(
        self,
        request: main_models.ScaleoutApplicationWithNewInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleoutApplicationWithNewInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_charge_period):
            query['InstanceChargePeriod'] = request.instance_charge_period
        if not DaraCore.is_null(request.instance_charge_period_unit):
            query['InstanceChargePeriodUnit'] = request.instance_charge_period_unit
        if not DaraCore.is_null(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not DaraCore.is_null(request.scaling_num):
            query['ScalingNum'] = request.scaling_num
        if not DaraCore.is_null(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_instance_id):
            query['TemplateInstanceId'] = request.template_instance_id
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScaleoutApplicationWithNewInstances',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/scaling/scale_out',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleoutApplicationWithNewInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scaleout_application_with_new_instances(
        self,
        request: main_models.ScaleoutApplicationWithNewInstancesRequest,
    ) -> main_models.ScaleoutApplicationWithNewInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.scaleout_application_with_new_instances_with_options(request, headers, runtime)

    async def scaleout_application_with_new_instances_async(
        self,
        request: main_models.ScaleoutApplicationWithNewInstancesRequest,
    ) -> main_models.ScaleoutApplicationWithNewInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.scaleout_application_with_new_instances_with_options_async(request, headers, runtime)

    def start_application_with_options(
        self,
        request: main_models.StartApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_application_with_options_async(
        self,
        request: main_models.StartApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_application(
        self,
        request: main_models.StartApplicationRequest,
    ) -> main_models.StartApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_application_with_options(request, headers, runtime)

    async def start_application_async(
        self,
        request: main_models.StartApplicationRequest,
    ) -> main_models.StartApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_application_with_options_async(request, headers, runtime)

    def start_k8s_app_precheck_with_options(
        self,
        request: main_models.StartK8sAppPrecheckRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartK8sAppPrecheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.component_ids):
            query['ComponentIds'] = request.component_ids
        if not DaraCore.is_null(request.config_mount_descs):
            query['ConfigMountDescs'] = request.config_mount_descs
        if not DaraCore.is_null(request.empty_dirs):
            query['EmptyDirs'] = request.empty_dirs
        if not DaraCore.is_null(request.env_froms):
            query['EnvFroms'] = request.env_froms
        if not DaraCore.is_null(request.envs):
            query['Envs'] = request.envs
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.java_start_up_config):
            query['JavaStartUpConfig'] = request.java_start_up_config
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.limit_ephemeral_storage):
            query['LimitEphemeralStorage'] = request.limit_ephemeral_storage
        if not DaraCore.is_null(request.limit_mem):
            query['LimitMem'] = request.limit_mem
        if not DaraCore.is_null(request.limitm_cpu):
            query['LimitmCpu'] = request.limitm_cpu
        if not DaraCore.is_null(request.local_volume):
            query['LocalVolume'] = request.local_volume
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.package_url):
            query['PackageUrl'] = request.package_url
        if not DaraCore.is_null(request.pvc_mount_descs):
            query['PvcMountDescs'] = request.pvc_mount_descs
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.requests_ephemeral_storage):
            query['RequestsEphemeralStorage'] = request.requests_ephemeral_storage
        if not DaraCore.is_null(request.requests_mem):
            query['RequestsMem'] = request.requests_mem
        if not DaraCore.is_null(request.requestsm_cpu):
            query['RequestsmCpu'] = request.requestsm_cpu
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartK8sAppPrecheck',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/app_precheck',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartK8sAppPrecheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_k8s_app_precheck_with_options_async(
        self,
        request: main_models.StartK8sAppPrecheckRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartK8sAppPrecheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.component_ids):
            query['ComponentIds'] = request.component_ids
        if not DaraCore.is_null(request.config_mount_descs):
            query['ConfigMountDescs'] = request.config_mount_descs
        if not DaraCore.is_null(request.empty_dirs):
            query['EmptyDirs'] = request.empty_dirs
        if not DaraCore.is_null(request.env_froms):
            query['EnvFroms'] = request.env_froms
        if not DaraCore.is_null(request.envs):
            query['Envs'] = request.envs
        if not DaraCore.is_null(request.image_url):
            query['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.java_start_up_config):
            query['JavaStartUpConfig'] = request.java_start_up_config
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.limit_ephemeral_storage):
            query['LimitEphemeralStorage'] = request.limit_ephemeral_storage
        if not DaraCore.is_null(request.limit_mem):
            query['LimitMem'] = request.limit_mem
        if not DaraCore.is_null(request.limitm_cpu):
            query['LimitmCpu'] = request.limitm_cpu
        if not DaraCore.is_null(request.local_volume):
            query['LocalVolume'] = request.local_volume
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.package_url):
            query['PackageUrl'] = request.package_url
        if not DaraCore.is_null(request.pvc_mount_descs):
            query['PvcMountDescs'] = request.pvc_mount_descs
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.requests_ephemeral_storage):
            query['RequestsEphemeralStorage'] = request.requests_ephemeral_storage
        if not DaraCore.is_null(request.requests_mem):
            query['RequestsMem'] = request.requests_mem
        if not DaraCore.is_null(request.requestsm_cpu):
            query['RequestsmCpu'] = request.requestsm_cpu
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartK8sAppPrecheck',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/app_precheck',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartK8sAppPrecheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_k8s_app_precheck(
        self,
        request: main_models.StartK8sAppPrecheckRequest,
    ) -> main_models.StartK8sAppPrecheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_k8s_app_precheck_with_options(request, headers, runtime)

    async def start_k8s_app_precheck_async(
        self,
        request: main_models.StartK8sAppPrecheckRequest,
    ) -> main_models.StartK8sAppPrecheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_k8s_app_precheck_with_options_async(request, headers, runtime)

    def start_k8s_application_with_options(
        self,
        request: main_models.StartK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartK8sApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartK8sApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/start_k8s_app',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartK8sApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_k8s_application_with_options_async(
        self,
        request: main_models.StartK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartK8sApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.replicas):
            query['Replicas'] = request.replicas
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartK8sApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/start_k8s_app',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartK8sApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_k8s_application(
        self,
        request: main_models.StartK8sApplicationRequest,
    ) -> main_models.StartK8sApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_k8s_application_with_options(request, headers, runtime)

    async def start_k8s_application_async(
        self,
        request: main_models.StartK8sApplicationRequest,
    ) -> main_models.StartK8sApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_k8s_application_with_options_async(request, headers, runtime)

    def stop_application_with_options(
        self,
        request: main_models.StopApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_application_with_options_async(
        self,
        request: main_models.StopApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.ecc_info):
            query['EccInfo'] = request.ecc_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_application(
        self,
        request: main_models.StopApplicationRequest,
    ) -> main_models.StopApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_application_with_options(request, headers, runtime)

    async def stop_application_async(
        self,
        request: main_models.StopApplicationRequest,
    ) -> main_models.StopApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_application_with_options_async(request, headers, runtime)

    def stop_k8s_application_with_options(
        self,
        request: main_models.StopK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopK8sApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopK8sApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/stop_k8s_app',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopK8sApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_k8s_application_with_options_async(
        self,
        request: main_models.StopK8sApplicationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopK8sApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopK8sApplication',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/stop_k8s_app',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopK8sApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_k8s_application(
        self,
        request: main_models.StopK8sApplicationRequest,
    ) -> main_models.StopK8sApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_k8s_application_with_options(request, headers, runtime)

    async def stop_k8s_application_async(
        self,
        request: main_models.StopK8sApplicationRequest,
    ) -> main_models.StopK8sApplicationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_k8s_application_with_options_async(request, headers, runtime)

    def switch_advanced_monitoring_with_options(
        self,
        request: main_models.SwitchAdvancedMonitoringRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SwitchAdvancedMonitoringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.enable_advanced_monitoring):
            query['EnableAdvancedMonitoring'] = request.enable_advanced_monitoring
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchAdvancedMonitoring',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/monitor/advancedMonitorInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchAdvancedMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_advanced_monitoring_with_options_async(
        self,
        request: main_models.SwitchAdvancedMonitoringRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SwitchAdvancedMonitoringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.enable_advanced_monitoring):
            query['EnableAdvancedMonitoring'] = request.enable_advanced_monitoring
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchAdvancedMonitoring',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/monitor/advancedMonitorInfo',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchAdvancedMonitoringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_advanced_monitoring(
        self,
        request: main_models.SwitchAdvancedMonitoringRequest,
    ) -> main_models.SwitchAdvancedMonitoringResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.switch_advanced_monitoring_with_options(request, headers, runtime)

    async def switch_advanced_monitoring_async(
        self,
        request: main_models.SwitchAdvancedMonitoringRequest,
    ) -> main_models.SwitchAdvancedMonitoringResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.switch_advanced_monitoring_with_options_async(request, headers, runtime)

    def synchronize_resource_with_options(
        self,
        request: main_models.SynchronizeResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SynchronizeResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SynchronizeResource',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/pop_sync_resource',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SynchronizeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def synchronize_resource_with_options_async(
        self,
        request: main_models.SynchronizeResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SynchronizeResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SynchronizeResource',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/pop_sync_resource',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SynchronizeResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def synchronize_resource(
        self,
        request: main_models.SynchronizeResourceRequest,
    ) -> main_models.SynchronizeResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.synchronize_resource_with_options(request, headers, runtime)

    async def synchronize_resource_async(
        self,
        request: main_models.SynchronizeResourceRequest,
    ) -> main_models.SynchronizeResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.synchronize_resource_with_options_async(request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/tag/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/tag/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def transform_cluster_member_with_options(
        self,
        request: main_models.TransformClusterMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TransformClusterMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.target_cluster_id):
            query['TargetClusterId'] = request.target_cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransformClusterMember',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/transform_cluster_member',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransformClusterMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def transform_cluster_member_with_options_async(
        self,
        request: main_models.TransformClusterMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TransformClusterMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.target_cluster_id):
            query['TargetClusterId'] = request.target_cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransformClusterMember',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/resource/transform_cluster_member',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransformClusterMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transform_cluster_member(
        self,
        request: main_models.TransformClusterMemberRequest,
    ) -> main_models.TransformClusterMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.transform_cluster_member_with_options(request, headers, runtime)

    async def transform_cluster_member_async(
        self,
        request: main_models.TransformClusterMemberRequest,
    ) -> main_models.TransformClusterMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.transform_cluster_member_with_options_async(request, headers, runtime)

    def unbind_k8s_slb_with_options(
        self,
        request: main_models.UnbindK8sSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnbindK8sSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.slb_name):
            query['SlbName'] = request.slb_name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindK8sSlb',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_slb_binding',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindK8sSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_k8s_slb_with_options_async(
        self,
        request: main_models.UnbindK8sSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnbindK8sSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.slb_name):
            query['SlbName'] = request.slb_name
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindK8sSlb',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_slb_binding',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindK8sSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_k8s_slb(
        self,
        request: main_models.UnbindK8sSlbRequest,
    ) -> main_models.UnbindK8sSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.unbind_k8s_slb_with_options(request, headers, runtime)

    async def unbind_k8s_slb_async(
        self,
        request: main_models.UnbindK8sSlbRequest,
    ) -> main_models.UnbindK8sSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.unbind_k8s_slb_with_options_async(request, headers, runtime)

    def unbind_slb_with_options(
        self,
        request: main_models.UnbindSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnbindSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.delete_listener):
            query['DeleteListener'] = request.delete_listener
        if not DaraCore.is_null(request.slb_id):
            query['SlbId'] = request.slb_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindSlb',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/app/unbind_slb_json',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_slb_with_options_async(
        self,
        request: main_models.UnbindSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnbindSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.delete_listener):
            query['DeleteListener'] = request.delete_listener
        if not DaraCore.is_null(request.slb_id):
            query['SlbId'] = request.slb_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindSlb',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/app/unbind_slb_json',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_slb(
        self,
        request: main_models.UnbindSlbRequest,
    ) -> main_models.UnbindSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.unbind_slb_with_options(request, headers, runtime)

    async def unbind_slb_async(
        self,
        request: main_models.UnbindSlbRequest,
    ) -> main_models.UnbindSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.unbind_slb_with_options_async(request, headers, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_all):
            query['DeleteAll'] = request.delete_all
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/tag/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_all):
            query['DeleteAll'] = request.delete_all
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/tag/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_account_info_with_options(
        self,
        request: main_models.UpdateAccountInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccountInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.telephone):
            query['Telephone'] = request.telephone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccountInfo',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/edit_account_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_account_info_with_options_async(
        self,
        request: main_models.UpdateAccountInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccountInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.telephone):
            query['Telephone'] = request.telephone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccountInfo',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/edit_account_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccountInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_account_info(
        self,
        request: main_models.UpdateAccountInfoRequest,
    ) -> main_models.UpdateAccountInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_account_info_with_options(request, headers, runtime)

    async def update_account_info_async(
        self,
        request: main_models.UpdateAccountInfoRequest,
    ) -> main_models.UpdateAccountInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_account_info_with_options_async(request, headers, runtime)

    def update_application_base_info_with_options(
        self,
        request: main_models.UpdateApplicationBaseInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationBaseInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationBaseInfo',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/update_app_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationBaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_base_info_with_options_async(
        self,
        request: main_models.UpdateApplicationBaseInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationBaseInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationBaseInfo',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/update_app_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationBaseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_base_info(
        self,
        request: main_models.UpdateApplicationBaseInfoRequest,
    ) -> main_models.UpdateApplicationBaseInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_application_base_info_with_options(request, headers, runtime)

    async def update_application_base_info_async(
        self,
        request: main_models.UpdateApplicationBaseInfoRequest,
    ) -> main_models.UpdateApplicationBaseInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_application_base_info_with_options_async(request, headers, runtime)

    def update_application_scaling_rule_with_options(
        self,
        request: main_models.UpdateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_behaviour):
            query['ScalingBehaviour'] = request.scaling_behaviour
        if not DaraCore.is_null(request.scaling_rule_enable):
            query['ScalingRuleEnable'] = request.scaling_rule_enable
        if not DaraCore.is_null(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not DaraCore.is_null(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        if not DaraCore.is_null(request.scaling_rule_trigger):
            query['ScalingRuleTrigger'] = request.scaling_rule_trigger
        if not DaraCore.is_null(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationScalingRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/eam/scale/application_scaling_rule',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_scaling_rule_with_options_async(
        self,
        request: main_models.UpdateApplicationScalingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationScalingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.scaling_behaviour):
            query['ScalingBehaviour'] = request.scaling_behaviour
        if not DaraCore.is_null(request.scaling_rule_enable):
            query['ScalingRuleEnable'] = request.scaling_rule_enable
        if not DaraCore.is_null(request.scaling_rule_metric):
            query['ScalingRuleMetric'] = request.scaling_rule_metric
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not DaraCore.is_null(request.scaling_rule_timer):
            query['ScalingRuleTimer'] = request.scaling_rule_timer
        if not DaraCore.is_null(request.scaling_rule_trigger):
            query['ScalingRuleTrigger'] = request.scaling_rule_trigger
        if not DaraCore.is_null(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationScalingRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v1/eam/scale/application_scaling_rule',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_scaling_rule(
        self,
        request: main_models.UpdateApplicationScalingRuleRequest,
    ) -> main_models.UpdateApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_application_scaling_rule_with_options(request, headers, runtime)

    async def update_application_scaling_rule_async(
        self,
        request: main_models.UpdateApplicationScalingRuleRequest,
    ) -> main_models.UpdateApplicationScalingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_application_scaling_rule_with_options_async(request, headers, runtime)

    def update_config_template_with_options(
        self,
        request: main_models.UpdateConfigTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.format):
            body['Format'] = request.format
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfigTemplate',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/config_template',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_template_with_options_async(
        self,
        request: main_models.UpdateConfigTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConfigTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.format):
            body['Format'] = request.format
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConfigTemplate',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/config_template',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConfigTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config_template(
        self,
        request: main_models.UpdateConfigTemplateRequest,
    ) -> main_models.UpdateConfigTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_config_template_with_options(request, headers, runtime)

    async def update_config_template_async(
        self,
        request: main_models.UpdateConfigTemplateRequest,
    ) -> main_models.UpdateConfigTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_config_template_with_options_async(request, headers, runtime)

    def update_container_with_options(
        self,
        request: main_models.UpdateContainerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContainerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContainer',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_update_container',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContainerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_container_with_options_async(
        self,
        request: main_models.UpdateContainerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContainerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.build_pack_id):
            query['BuildPackId'] = request.build_pack_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContainer',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/changeorder/co_update_container',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContainerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_container(
        self,
        request: main_models.UpdateContainerRequest,
    ) -> main_models.UpdateContainerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_container_with_options(request, headers, runtime)

    async def update_container_async(
        self,
        request: main_models.UpdateContainerRequest,
    ) -> main_models.UpdateContainerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_container_with_options_async(request, headers, runtime)

    def update_container_configuration_with_options(
        self,
        request: main_models.UpdateContainerConfigurationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContainerConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.context_path):
            query['ContextPath'] = request.context_path
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.http_port):
            query['HttpPort'] = request.http_port
        if not DaraCore.is_null(request.max_threads):
            query['MaxThreads'] = request.max_threads
        if not DaraCore.is_null(request.uriencoding):
            query['URIEncoding'] = request.uriencoding
        if not DaraCore.is_null(request.use_body_encoding):
            query['UseBodyEncoding'] = request.use_body_encoding
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContainerConfiguration',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/container_config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContainerConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_container_configuration_with_options_async(
        self,
        request: main_models.UpdateContainerConfigurationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContainerConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.context_path):
            query['ContextPath'] = request.context_path
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.http_port):
            query['HttpPort'] = request.http_port
        if not DaraCore.is_null(request.max_threads):
            query['MaxThreads'] = request.max_threads
        if not DaraCore.is_null(request.uriencoding):
            query['URIEncoding'] = request.uriencoding
        if not DaraCore.is_null(request.use_body_encoding):
            query['UseBodyEncoding'] = request.use_body_encoding
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContainerConfiguration',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/container_config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContainerConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_container_configuration(
        self,
        request: main_models.UpdateContainerConfigurationRequest,
    ) -> main_models.UpdateContainerConfigurationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_container_configuration_with_options(request, headers, runtime)

    async def update_container_configuration_async(
        self,
        request: main_models.UpdateContainerConfigurationRequest,
    ) -> main_models.UpdateContainerConfigurationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_container_configuration_with_options_async(request, headers, runtime)

    def update_health_check_url_with_options(
        self,
        request: main_models.UpdateHealthCheckUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHealthCheckUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.hc_url):
            query['hcURL'] = request.hc_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHealthCheckUrl',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/modify_hc_url',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHealthCheckUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_health_check_url_with_options_async(
        self,
        request: main_models.UpdateHealthCheckUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHealthCheckUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.hc_url):
            query['hcURL'] = request.hc_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHealthCheckUrl',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/modify_hc_url',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHealthCheckUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_health_check_url(
        self,
        request: main_models.UpdateHealthCheckUrlRequest,
    ) -> main_models.UpdateHealthCheckUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_health_check_url_with_options(request, headers, runtime)

    async def update_health_check_url_async(
        self,
        request: main_models.UpdateHealthCheckUrlRequest,
    ) -> main_models.UpdateHealthCheckUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_health_check_url_with_options_async(request, headers, runtime)

    def update_hook_configuration_with_options(
        self,
        request: main_models.UpdateHookConfigurationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHookConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.hooks):
            query['Hooks'] = request.hooks
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHookConfiguration',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/app/config_app_hook_json',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHookConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hook_configuration_with_options_async(
        self,
        request: main_models.UpdateHookConfigurationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHookConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.hooks):
            query['Hooks'] = request.hooks
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHookConfiguration',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/app/config_app_hook_json',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHookConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_hook_configuration(
        self,
        request: main_models.UpdateHookConfigurationRequest,
    ) -> main_models.UpdateHookConfigurationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_hook_configuration_with_options(request, headers, runtime)

    async def update_hook_configuration_async(
        self,
        request: main_models.UpdateHookConfigurationRequest,
    ) -> main_models.UpdateHookConfigurationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_hook_configuration_with_options_async(request, headers, runtime)

    def update_jvm_configuration_with_options(
        self,
        request: main_models.UpdateJvmConfigurationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJvmConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.max_heap_size):
            query['MaxHeapSize'] = request.max_heap_size
        if not DaraCore.is_null(request.max_perm_size):
            query['MaxPermSize'] = request.max_perm_size
        if not DaraCore.is_null(request.min_heap_size):
            query['MinHeapSize'] = request.min_heap_size
        if not DaraCore.is_null(request.options):
            query['Options'] = request.options
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJvmConfiguration',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/app_jvm_config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateJvmConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_jvm_configuration_with_options_async(
        self,
        request: main_models.UpdateJvmConfigurationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJvmConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.max_heap_size):
            query['MaxHeapSize'] = request.max_heap_size
        if not DaraCore.is_null(request.max_perm_size):
            query['MaxPermSize'] = request.max_perm_size
        if not DaraCore.is_null(request.min_heap_size):
            query['MinHeapSize'] = request.min_heap_size
        if not DaraCore.is_null(request.options):
            query['Options'] = request.options
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJvmConfiguration',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/app/app_jvm_config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateJvmConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_jvm_configuration(
        self,
        request: main_models.UpdateJvmConfigurationRequest,
    ) -> main_models.UpdateJvmConfigurationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_jvm_configuration_with_options(request, headers, runtime)

    async def update_jvm_configuration_async(
        self,
        request: main_models.UpdateJvmConfigurationRequest,
    ) -> main_models.UpdateJvmConfigurationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_jvm_configuration_with_options_async(request, headers, runtime)

    def update_k8s_application_base_info_with_options(
        self,
        request: main_models.UpdateK8sApplicationBaseInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sApplicationBaseInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sApplicationBaseInfo',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/oam/update_app_basic_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sApplicationBaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_application_base_info_with_options_async(
        self,
        request: main_models.UpdateK8sApplicationBaseInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sApplicationBaseInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sApplicationBaseInfo',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/oam/update_app_basic_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sApplicationBaseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_application_base_info(
        self,
        request: main_models.UpdateK8sApplicationBaseInfoRequest,
    ) -> main_models.UpdateK8sApplicationBaseInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_k8s_application_base_info_with_options(request, headers, runtime)

    async def update_k8s_application_base_info_async(
        self,
        request: main_models.UpdateK8sApplicationBaseInfoRequest,
    ) -> main_models.UpdateK8sApplicationBaseInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_k8s_application_base_info_with_options_async(request, headers, runtime)

    def update_k8s_application_config_with_options(
        self,
        request: main_models.UpdateK8sApplicationConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sApplicationConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cpu_limit):
            query['CpuLimit'] = request.cpu_limit
        if not DaraCore.is_null(request.cpu_request):
            query['CpuRequest'] = request.cpu_request
        if not DaraCore.is_null(request.ephemeral_storage_limit):
            query['EphemeralStorageLimit'] = request.ephemeral_storage_limit
        if not DaraCore.is_null(request.ephemeral_storage_request):
            query['EphemeralStorageRequest'] = request.ephemeral_storage_request
        if not DaraCore.is_null(request.mcpu_limit):
            query['McpuLimit'] = request.mcpu_limit
        if not DaraCore.is_null(request.mcpu_request):
            query['McpuRequest'] = request.mcpu_request
        if not DaraCore.is_null(request.memory_limit):
            query['MemoryLimit'] = request.memory_limit
        if not DaraCore.is_null(request.memory_request):
            query['MemoryRequest'] = request.memory_request
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sApplicationConfig',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_app_configuration',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sApplicationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_application_config_with_options_async(
        self,
        request: main_models.UpdateK8sApplicationConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sApplicationConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cpu_limit):
            query['CpuLimit'] = request.cpu_limit
        if not DaraCore.is_null(request.cpu_request):
            query['CpuRequest'] = request.cpu_request
        if not DaraCore.is_null(request.ephemeral_storage_limit):
            query['EphemeralStorageLimit'] = request.ephemeral_storage_limit
        if not DaraCore.is_null(request.ephemeral_storage_request):
            query['EphemeralStorageRequest'] = request.ephemeral_storage_request
        if not DaraCore.is_null(request.mcpu_limit):
            query['McpuLimit'] = request.mcpu_limit
        if not DaraCore.is_null(request.mcpu_request):
            query['McpuRequest'] = request.mcpu_request
        if not DaraCore.is_null(request.memory_limit):
            query['MemoryLimit'] = request.memory_limit
        if not DaraCore.is_null(request.memory_request):
            query['MemoryRequest'] = request.memory_request
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sApplicationConfig',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_app_configuration',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sApplicationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_application_config(
        self,
        request: main_models.UpdateK8sApplicationConfigRequest,
    ) -> main_models.UpdateK8sApplicationConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_k8s_application_config_with_options(request, headers, runtime)

    async def update_k8s_application_config_async(
        self,
        request: main_models.UpdateK8sApplicationConfigRequest,
    ) -> main_models.UpdateK8sApplicationConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_k8s_application_config_with_options_async(request, headers, runtime)

    def update_k8s_config_map_with_options(
        self,
        request: main_models.UpdateK8sConfigMapRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sConfigMapResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sConfigMap',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_config_map',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sConfigMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_config_map_with_options_async(
        self,
        request: main_models.UpdateK8sConfigMapRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sConfigMapResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sConfigMap',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_config_map',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sConfigMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_config_map(
        self,
        request: main_models.UpdateK8sConfigMapRequest,
    ) -> main_models.UpdateK8sConfigMapResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_k8s_config_map_with_options(request, headers, runtime)

    async def update_k8s_config_map_async(
        self,
        request: main_models.UpdateK8sConfigMapRequest,
    ) -> main_models.UpdateK8sConfigMapResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_k8s_config_map_with_options_async(request, headers, runtime)

    def update_k8s_ingress_rule_with_options(
        self,
        request: main_models.UpdateK8sIngressRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sIngressRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ingress_conf):
            query['IngressConf'] = request.ingress_conf
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sIngressRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_ingress',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sIngressRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_ingress_rule_with_options_async(
        self,
        request: main_models.UpdateK8sIngressRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sIngressRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ingress_conf):
            query['IngressConf'] = request.ingress_conf
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sIngressRule',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_ingress',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sIngressRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_ingress_rule(
        self,
        request: main_models.UpdateK8sIngressRuleRequest,
    ) -> main_models.UpdateK8sIngressRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_k8s_ingress_rule_with_options(request, headers, runtime)

    async def update_k8s_ingress_rule_async(
        self,
        request: main_models.UpdateK8sIngressRuleRequest,
    ) -> main_models.UpdateK8sIngressRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_k8s_ingress_rule_with_options_async(request, headers, runtime)

    def update_k8s_resource_with_options(
        self,
        request: main_models.UpdateK8sResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.resource_content):
            body['ResourceContent'] = request.resource_content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sResource',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/oam/update_k8s_resource_config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_resource_with_options_async(
        self,
        request: main_models.UpdateK8sResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.resource_content):
            body['ResourceContent'] = request.resource_content
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sResource',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/oam/update_k8s_resource_config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_resource(
        self,
        request: main_models.UpdateK8sResourceRequest,
    ) -> main_models.UpdateK8sResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_k8s_resource_with_options(request, headers, runtime)

    async def update_k8s_resource_async(
        self,
        request: main_models.UpdateK8sResourceRequest,
    ) -> main_models.UpdateK8sResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_k8s_resource_with_options_async(request, headers, runtime)

    def update_k8s_secret_with_options(
        self,
        request: main_models.UpdateK8sSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sSecretResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.base_64encoded):
            body['Base64Encoded'] = request.base_64encoded
        if not DaraCore.is_null(request.cert_id):
            body['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_region_id):
            body['CertRegionId'] = request.cert_region_id
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sSecret',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_secret',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_secret_with_options_async(
        self,
        request: main_models.UpdateK8sSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sSecretResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.base_64encoded):
            body['Base64Encoded'] = request.base_64encoded
        if not DaraCore.is_null(request.cert_id):
            body['CertId'] = request.cert_id
        if not DaraCore.is_null(request.cert_region_id):
            body['CertRegionId'] = request.cert_region_id
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sSecret',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_secret',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_secret(
        self,
        request: main_models.UpdateK8sSecretRequest,
    ) -> main_models.UpdateK8sSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_k8s_secret_with_options(request, headers, runtime)

    async def update_k8s_secret_async(
        self,
        request: main_models.UpdateK8sSecretRequest,
    ) -> main_models.UpdateK8sSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_k8s_secret_with_options_async(request, headers, runtime)

    def update_k8s_service_with_options(
        self,
        request: main_models.UpdateK8sServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.external_traffic_policy):
            query['ExternalTrafficPolicy'] = request.external_traffic_policy
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.service_ports):
            query['ServicePorts'] = request.service_ports
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sService',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_service',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_service_with_options_async(
        self,
        request: main_models.UpdateK8sServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.external_traffic_policy):
            query['ExternalTrafficPolicy'] = request.external_traffic_policy
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.service_ports):
            query['ServicePorts'] = request.service_ports
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sService',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_service',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_service(
        self,
        request: main_models.UpdateK8sServiceRequest,
    ) -> main_models.UpdateK8sServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_k8s_service_with_options(request, headers, runtime)

    async def update_k8s_service_async(
        self,
        request: main_models.UpdateK8sServiceRequest,
    ) -> main_models.UpdateK8sServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_k8s_service_with_options_async(request, headers, runtime)

    def update_k8s_slb_with_options(
        self,
        request: main_models.UpdateK8sSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.disable_force_override):
            query['DisableForceOverride'] = request.disable_force_override
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.service_port_infos):
            query['ServicePortInfos'] = request.service_port_infos
        if not DaraCore.is_null(request.slb_name):
            query['SlbName'] = request.slb_name
        if not DaraCore.is_null(request.slb_protocol):
            query['SlbProtocol'] = request.slb_protocol
        if not DaraCore.is_null(request.specification):
            query['Specification'] = request.specification
        if not DaraCore.is_null(request.target_port):
            query['TargetPort'] = request.target_port
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sSlb',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_slb_binding',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_slb_with_options_async(
        self,
        request: main_models.UpdateK8sSlbRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.disable_force_override):
            query['DisableForceOverride'] = request.disable_force_override
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not DaraCore.is_null(request.service_port_infos):
            query['ServicePortInfos'] = request.service_port_infos
        if not DaraCore.is_null(request.slb_name):
            query['SlbName'] = request.slb_name
        if not DaraCore.is_null(request.slb_protocol):
            query['SlbProtocol'] = request.slb_protocol
        if not DaraCore.is_null(request.specification):
            query['Specification'] = request.specification
        if not DaraCore.is_null(request.target_port):
            query['TargetPort'] = request.target_port
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sSlb',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/acs/k8s_slb_binding',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_slb(
        self,
        request: main_models.UpdateK8sSlbRequest,
    ) -> main_models.UpdateK8sSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_k8s_slb_with_options(request, headers, runtime)

    async def update_k8s_slb_async(
        self,
        request: main_models.UpdateK8sSlbRequest,
    ) -> main_models.UpdateK8sSlbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_k8s_slb_with_options_async(request, headers, runtime)

    def update_locality_setting_with_options(
        self,
        request: main_models.UpdateLocalitySettingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLocalitySettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLocalitySetting',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/sp/applications/locality/setting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLocalitySettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_locality_setting_with_options_async(
        self,
        request: main_models.UpdateLocalitySettingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLocalitySettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLocalitySetting',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/sp/applications/locality/setting',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLocalitySettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_locality_setting(
        self,
        request: main_models.UpdateLocalitySettingRequest,
    ) -> main_models.UpdateLocalitySettingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_locality_setting_with_options(request, headers, runtime)

    async def update_locality_setting_async(
        self,
        request: main_models.UpdateLocalitySettingRequest,
    ) -> main_models.UpdateLocalitySettingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_locality_setting_with_options_async(request, headers, runtime)

    def update_role_with_options(
        self,
        request: main_models.UpdateRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_data):
            query['ActionData'] = request.action_data
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRole',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/edit_role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_role_with_options_async(
        self,
        request: main_models.UpdateRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_data):
            query['ActionData'] = request.action_data
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRole',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/account/edit_role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_role(
        self,
        request: main_models.UpdateRoleRequest,
    ) -> main_models.UpdateRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_role_with_options(request, headers, runtime)

    async def update_role_async(
        self,
        request: main_models.UpdateRoleRequest,
    ) -> main_models.UpdateRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_role_with_options_async(request, headers, runtime)

    def update_sls_log_store_with_options(
        self,
        request: main_models.UpdateSlsLogStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSlsLogStoreResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.configs):
            body['Configs'] = request.configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSlsLogStore',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/sls/update_sls_log_store',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSlsLogStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sls_log_store_with_options_async(
        self,
        request: main_models.UpdateSlsLogStoreRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSlsLogStoreResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.configs):
            body['Configs'] = request.configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSlsLogStore',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/k8s/sls/update_sls_log_store',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSlsLogStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sls_log_store(
        self,
        request: main_models.UpdateSlsLogStoreRequest,
    ) -> main_models.UpdateSlsLogStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_sls_log_store_with_options(request, headers, runtime)

    async def update_sls_log_store_async(
        self,
        request: main_models.UpdateSlsLogStoreRequest,
    ) -> main_models.UpdateSlsLogStoreResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_sls_log_store_with_options_async(request, headers, runtime)

    def update_swimming_lane_with_options(
        self,
        request: main_models.UpdateSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSwimmingLaneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_infos):
            query['AppInfos'] = request.app_infos
        if not DaraCore.is_null(request.enable_rules):
            query['EnableRules'] = request.enable_rules
        if not DaraCore.is_null(request.entry_rules):
            query['EntryRules'] = request.entry_rules
        if not DaraCore.is_null(request.lane_id):
            query['LaneId'] = request.lane_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSwimmingLane',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/trafficmgnt/swimming_lanes',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSwimmingLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_swimming_lane_with_options_async(
        self,
        request: main_models.UpdateSwimmingLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSwimmingLaneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_infos):
            query['AppInfos'] = request.app_infos
        if not DaraCore.is_null(request.enable_rules):
            query['EnableRules'] = request.enable_rules
        if not DaraCore.is_null(request.entry_rules):
            query['EntryRules'] = request.entry_rules
        if not DaraCore.is_null(request.lane_id):
            query['LaneId'] = request.lane_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSwimmingLane',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/trafficmgnt/swimming_lanes',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSwimmingLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_swimming_lane(
        self,
        request: main_models.UpdateSwimmingLaneRequest,
    ) -> main_models.UpdateSwimmingLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_swimming_lane_with_options(request, headers, runtime)

    async def update_swimming_lane_async(
        self,
        request: main_models.UpdateSwimmingLaneRequest,
    ) -> main_models.UpdateSwimmingLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_swimming_lane_with_options_async(request, headers, runtime)

    def update_swimming_lane_group_with_options(
        self,
        request: main_models.UpdateSwimmingLaneGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSwimmingLaneGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.entry_app):
            query['EntryApp'] = request.entry_app
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSwimmingLaneGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/trafficmgnt/swimming_lane_groups',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSwimmingLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_swimming_lane_group_with_options_async(
        self,
        request: main_models.UpdateSwimmingLaneGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSwimmingLaneGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.entry_app):
            query['EntryApp'] = request.entry_app
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSwimmingLaneGroup',
            version = '2017-08-01',
            protocol = 'HTTPS',
            pathname = f'/pop/v5/trafficmgnt/swimming_lane_groups',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSwimmingLaneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_swimming_lane_group(
        self,
        request: main_models.UpdateSwimmingLaneGroupRequest,
    ) -> main_models.UpdateSwimmingLaneGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_swimming_lane_group_with_options(request, headers, runtime)

    async def update_swimming_lane_group_async(
        self,
        request: main_models.UpdateSwimmingLaneGroupRequest,
    ) -> main_models.UpdateSwimmingLaneGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_swimming_lane_group_with_options_async(request, headers, runtime)
