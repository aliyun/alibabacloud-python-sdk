# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cs20151215 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

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
            'ap-northeast-2-pop': 'cs.aliyuncs.com',
            'cn-beijing-finance-pop': 'cs.aliyuncs.com',
            'cn-beijing-gov-1': 'cs.aliyuncs.com',
            'cn-beijing-nu16-b01': 'cs.aliyuncs.com',
            'cn-edge-1': 'cs.aliyuncs.com',
            'cn-fujian': 'cs.aliyuncs.com',
            'cn-haidian-cm12-c01': 'cs.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'cs.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'cs.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'cs.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'cs.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'cs.aliyuncs.com',
            'cn-hangzhou-test-306': 'cs.aliyuncs.com',
            'cn-hongkong-finance-pop': 'cs.aliyuncs.com',
            'cn-qingdao-nebula': 'cs.aliyuncs.com',
            'cn-shanghai-et15-b01': 'cs.aliyuncs.com',
            'cn-shanghai-et2-b01': 'cs.aliyuncs.com',
            'cn-shanghai-inner': 'cs.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'cs.aliyuncs.com',
            'cn-shenzhen-inner': 'cs.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'cs.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'cs.aliyuncs.com',
            'cn-wuhan': 'cs.aliyuncs.com',
            'cn-yushanfang': 'cs.aliyuncs.com',
            'cn-zhangbei': 'cs.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'cs.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'cs.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'cs.aliyuncs.com',
            'eu-west-1-oxs': 'cs.aliyuncs.com',
            'rus-west-1-pop': 'cs.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def attach_instances_with_options(
        self,
        cluster_id: str,
        request: main_models.AttachInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AttachInstancesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not DaraCore.is_null(request.format_disk):
            body['format_disk'] = request.format_disk
        if not DaraCore.is_null(request.image_id):
            body['image_id'] = request.image_id
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        if not DaraCore.is_null(request.is_edge_worker):
            body['is_edge_worker'] = request.is_edge_worker
        if not DaraCore.is_null(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not DaraCore.is_null(request.key_pair):
            body['key_pair'] = request.key_pair
        if not DaraCore.is_null(request.nodepool_id):
            body['nodepool_id'] = request.nodepool_id
        if not DaraCore.is_null(request.password):
            body['password'] = request.password
        if not DaraCore.is_null(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not DaraCore.is_null(request.runtime):
            body['runtime'] = request.runtime
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.user_data):
            body['user_data'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachInstances',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/attach',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_instances_with_options_async(
        self,
        cluster_id: str,
        request: main_models.AttachInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AttachInstancesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not DaraCore.is_null(request.format_disk):
            body['format_disk'] = request.format_disk
        if not DaraCore.is_null(request.image_id):
            body['image_id'] = request.image_id
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        if not DaraCore.is_null(request.is_edge_worker):
            body['is_edge_worker'] = request.is_edge_worker
        if not DaraCore.is_null(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not DaraCore.is_null(request.key_pair):
            body['key_pair'] = request.key_pair
        if not DaraCore.is_null(request.nodepool_id):
            body['nodepool_id'] = request.nodepool_id
        if not DaraCore.is_null(request.password):
            body['password'] = request.password
        if not DaraCore.is_null(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not DaraCore.is_null(request.runtime):
            body['runtime'] = request.runtime
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.user_data):
            body['user_data'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachInstances',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/attach',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_instances(
        self,
        cluster_id: str,
        request: main_models.AttachInstancesRequest,
    ) -> main_models.AttachInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.attach_instances_with_options(cluster_id, request, headers, runtime)

    async def attach_instances_async(
        self,
        cluster_id: str,
        request: main_models.AttachInstancesRequest,
    ) -> main_models.AttachInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.attach_instances_with_options_async(cluster_id, request, headers, runtime)

    def attach_instances_to_node_pool_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.AttachInstancesToNodePoolRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AttachInstancesToNodePoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.format_disk):
            body['format_disk'] = request.format_disk
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        if not DaraCore.is_null(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not DaraCore.is_null(request.password):
            body['password'] = request.password
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachInstancesToNodePool',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}/attach',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachInstancesToNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_instances_to_node_pool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.AttachInstancesToNodePoolRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AttachInstancesToNodePoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.format_disk):
            body['format_disk'] = request.format_disk
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        if not DaraCore.is_null(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not DaraCore.is_null(request.password):
            body['password'] = request.password
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachInstancesToNodePool',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}/attach',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachInstancesToNodePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_instances_to_node_pool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.AttachInstancesToNodePoolRequest,
    ) -> main_models.AttachInstancesToNodePoolResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.attach_instances_to_node_pool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def attach_instances_to_node_pool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.AttachInstancesToNodePoolRequest,
    ) -> main_models.AttachInstancesToNodePoolResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.attach_instances_to_node_pool_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def cancel_cluster_upgrade_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelClusterUpgradeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CancelClusterUpgrade',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/clusters/{DaraURL.percent_encode(cluster_id)}/upgrade/cancel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CancelClusterUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_cluster_upgrade_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelClusterUpgradeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CancelClusterUpgrade',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/clusters/{DaraURL.percent_encode(cluster_id)}/upgrade/cancel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CancelClusterUpgradeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_cluster_upgrade(
        self,
        cluster_id: str,
    ) -> main_models.CancelClusterUpgradeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_cluster_upgrade_with_options(cluster_id, headers, runtime)

    async def cancel_cluster_upgrade_async(
        self,
        cluster_id: str,
    ) -> main_models.CancelClusterUpgradeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_cluster_upgrade_with_options_async(cluster_id, headers, runtime)

    def cancel_component_upgrade_with_options(
        self,
        cluster_id: str,
        component_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelComponentUpgradeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CancelComponentUpgrade',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/{DaraURL.percent_encode(component_id)}/cancel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CancelComponentUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_component_upgrade_with_options_async(
        self,
        cluster_id: str,
        component_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelComponentUpgradeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CancelComponentUpgrade',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/{DaraURL.percent_encode(component_id)}/cancel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CancelComponentUpgradeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_component_upgrade(
        self,
        cluster_id: str,
        component_id: str,
    ) -> main_models.CancelComponentUpgradeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_component_upgrade_with_options(cluster_id, component_id, headers, runtime)

    async def cancel_component_upgrade_async(
        self,
        cluster_id: str,
        component_id: str,
    ) -> main_models.CancelComponentUpgradeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_component_upgrade_with_options_async(cluster_id, component_id, headers, runtime)

    def cancel_operation_plan_with_options(
        self,
        plan_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelOperationPlanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CancelOperationPlan',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/operation/plans/{DaraURL.percent_encode(plan_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelOperationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_operation_plan_with_options_async(
        self,
        plan_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelOperationPlanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CancelOperationPlan',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/operation/plans/{DaraURL.percent_encode(plan_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelOperationPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_operation_plan(
        self,
        plan_id: str,
    ) -> main_models.CancelOperationPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_operation_plan_with_options(plan_id, headers, runtime)

    async def cancel_operation_plan_async(
        self,
        plan_id: str,
    ) -> main_models.CancelOperationPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_operation_plan_with_options_async(plan_id, headers, runtime)

    def cancel_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CancelTask',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}/cancel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CancelTask',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}/cancel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CancelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_task(
        self,
        task_id: str,
    ) -> main_models.CancelTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_task_with_options(task_id, headers, runtime)

    async def cancel_task_async(
        self,
        task_id: str,
    ) -> main_models.CancelTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_task_with_options_async(task_id, headers, runtime)

    def check_control_plane_log_enable_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckControlPlaneLogEnableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CheckControlPlaneLogEnable',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/controlplanelog',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckControlPlaneLogEnableResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_control_plane_log_enable_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckControlPlaneLogEnableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CheckControlPlaneLogEnable',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/controlplanelog',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckControlPlaneLogEnableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_control_plane_log_enable(
        self,
        cluster_id: str,
    ) -> main_models.CheckControlPlaneLogEnableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.check_control_plane_log_enable_with_options(cluster_id, headers, runtime)

    async def check_control_plane_log_enable_async(
        self,
        cluster_id: str,
    ) -> main_models.CheckControlPlaneLogEnableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.check_control_plane_log_enable_with_options_async(cluster_id, headers, runtime)

    def check_service_role_with_options(
        self,
        request: main_models.CheckServiceRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckServiceRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.roles):
            body['roles'] = request.roles
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceRole',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/ram/check-service-role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckServiceRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_role_with_options_async(
        self,
        request: main_models.CheckServiceRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckServiceRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.roles):
            body['roles'] = request.roles
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceRole',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/ram/check-service-role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckServiceRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_role(
        self,
        request: main_models.CheckServiceRoleRequest,
    ) -> main_models.CheckServiceRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.check_service_role_with_options(request, headers, runtime)

    async def check_service_role_async(
        self,
        request: main_models.CheckServiceRoleRequest,
    ) -> main_models.CheckServiceRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.check_service_role_with_options_async(request, headers, runtime)

    def clean_cluster_user_permissions_with_options(
        self,
        cluster_id: str,
        uid: str,
        request: main_models.CleanClusterUserPermissionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CleanClusterUserPermissionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CleanClusterUserPermissions',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/cluster/{DaraURL.percent_encode(cluster_id)}/user/{DaraURL.percent_encode(uid)}/permissions',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CleanClusterUserPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def clean_cluster_user_permissions_with_options_async(
        self,
        cluster_id: str,
        uid: str,
        request: main_models.CleanClusterUserPermissionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CleanClusterUserPermissionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CleanClusterUserPermissions',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/cluster/{DaraURL.percent_encode(cluster_id)}/user/{DaraURL.percent_encode(uid)}/permissions',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CleanClusterUserPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clean_cluster_user_permissions(
        self,
        cluster_id: str,
        uid: str,
        request: main_models.CleanClusterUserPermissionsRequest,
    ) -> main_models.CleanClusterUserPermissionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.clean_cluster_user_permissions_with_options(cluster_id, uid, request, headers, runtime)

    async def clean_cluster_user_permissions_async(
        self,
        cluster_id: str,
        uid: str,
        request: main_models.CleanClusterUserPermissionsRequest,
    ) -> main_models.CleanClusterUserPermissionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.clean_cluster_user_permissions_with_options_async(cluster_id, uid, request, headers, runtime)

    def clean_user_permissions_with_options(
        self,
        uid: str,
        tmp_req: main_models.CleanUserPermissionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CleanUserPermissionsResponse:
        tmp_req.validate()
        request = main_models.CleanUserPermissionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cluster_ids):
            request.cluster_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.cluster_ids, 'ClusterIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.cluster_ids_shrink):
            query['ClusterIds'] = request.cluster_ids_shrink
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CleanUserPermissions',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/users/{DaraURL.percent_encode(uid)}/permissions',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CleanUserPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def clean_user_permissions_with_options_async(
        self,
        uid: str,
        tmp_req: main_models.CleanUserPermissionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CleanUserPermissionsResponse:
        tmp_req.validate()
        request = main_models.CleanUserPermissionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cluster_ids):
            request.cluster_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.cluster_ids, 'ClusterIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.cluster_ids_shrink):
            query['ClusterIds'] = request.cluster_ids_shrink
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CleanUserPermissions',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/users/{DaraURL.percent_encode(uid)}/permissions',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CleanUserPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clean_user_permissions(
        self,
        uid: str,
        request: main_models.CleanUserPermissionsRequest,
    ) -> main_models.CleanUserPermissionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.clean_user_permissions_with_options(uid, request, headers, runtime)

    async def clean_user_permissions_async(
        self,
        uid: str,
        request: main_models.CleanUserPermissionsRequest,
    ) -> main_models.CleanUserPermissionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.clean_user_permissions_with_options_async(uid, request, headers, runtime)

    def create_autoscaling_config_with_options(
        self,
        cluster_id: str,
        request: main_models.CreateAutoscalingConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAutoscalingConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cool_down_duration):
            body['cool_down_duration'] = request.cool_down_duration
        if not DaraCore.is_null(request.daemonset_eviction_for_nodes):
            body['daemonset_eviction_for_nodes'] = request.daemonset_eviction_for_nodes
        if not DaraCore.is_null(request.expander):
            body['expander'] = request.expander
        if not DaraCore.is_null(request.gpu_utilization_threshold):
            body['gpu_utilization_threshold'] = request.gpu_utilization_threshold
        if not DaraCore.is_null(request.max_graceful_termination_sec):
            body['max_graceful_termination_sec'] = request.max_graceful_termination_sec
        if not DaraCore.is_null(request.min_replica_count):
            body['min_replica_count'] = request.min_replica_count
        if not DaraCore.is_null(request.priorities):
            body['priorities'] = request.priorities
        if not DaraCore.is_null(request.recycle_node_deletion_enabled):
            body['recycle_node_deletion_enabled'] = request.recycle_node_deletion_enabled
        if not DaraCore.is_null(request.scale_down_enabled):
            body['scale_down_enabled'] = request.scale_down_enabled
        if not DaraCore.is_null(request.scale_up_from_zero):
            body['scale_up_from_zero'] = request.scale_up_from_zero
        if not DaraCore.is_null(request.scaler_type):
            body['scaler_type'] = request.scaler_type
        if not DaraCore.is_null(request.scan_interval):
            body['scan_interval'] = request.scan_interval
        if not DaraCore.is_null(request.skip_nodes_with_local_storage):
            body['skip_nodes_with_local_storage'] = request.skip_nodes_with_local_storage
        if not DaraCore.is_null(request.skip_nodes_with_system_pods):
            body['skip_nodes_with_system_pods'] = request.skip_nodes_with_system_pods
        if not DaraCore.is_null(request.unneeded_duration):
            body['unneeded_duration'] = request.unneeded_duration
        if not DaraCore.is_null(request.utilization_threshold):
            body['utilization_threshold'] = request.utilization_threshold
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAutoscalingConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/cluster/{DaraURL.percent_encode(cluster_id)}/autoscale/config/',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAutoscalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_autoscaling_config_with_options_async(
        self,
        cluster_id: str,
        request: main_models.CreateAutoscalingConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAutoscalingConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cool_down_duration):
            body['cool_down_duration'] = request.cool_down_duration
        if not DaraCore.is_null(request.daemonset_eviction_for_nodes):
            body['daemonset_eviction_for_nodes'] = request.daemonset_eviction_for_nodes
        if not DaraCore.is_null(request.expander):
            body['expander'] = request.expander
        if not DaraCore.is_null(request.gpu_utilization_threshold):
            body['gpu_utilization_threshold'] = request.gpu_utilization_threshold
        if not DaraCore.is_null(request.max_graceful_termination_sec):
            body['max_graceful_termination_sec'] = request.max_graceful_termination_sec
        if not DaraCore.is_null(request.min_replica_count):
            body['min_replica_count'] = request.min_replica_count
        if not DaraCore.is_null(request.priorities):
            body['priorities'] = request.priorities
        if not DaraCore.is_null(request.recycle_node_deletion_enabled):
            body['recycle_node_deletion_enabled'] = request.recycle_node_deletion_enabled
        if not DaraCore.is_null(request.scale_down_enabled):
            body['scale_down_enabled'] = request.scale_down_enabled
        if not DaraCore.is_null(request.scale_up_from_zero):
            body['scale_up_from_zero'] = request.scale_up_from_zero
        if not DaraCore.is_null(request.scaler_type):
            body['scaler_type'] = request.scaler_type
        if not DaraCore.is_null(request.scan_interval):
            body['scan_interval'] = request.scan_interval
        if not DaraCore.is_null(request.skip_nodes_with_local_storage):
            body['skip_nodes_with_local_storage'] = request.skip_nodes_with_local_storage
        if not DaraCore.is_null(request.skip_nodes_with_system_pods):
            body['skip_nodes_with_system_pods'] = request.skip_nodes_with_system_pods
        if not DaraCore.is_null(request.unneeded_duration):
            body['unneeded_duration'] = request.unneeded_duration
        if not DaraCore.is_null(request.utilization_threshold):
            body['utilization_threshold'] = request.utilization_threshold
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAutoscalingConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/cluster/{DaraURL.percent_encode(cluster_id)}/autoscale/config/',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAutoscalingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_autoscaling_config(
        self,
        cluster_id: str,
        request: main_models.CreateAutoscalingConfigRequest,
    ) -> main_models.CreateAutoscalingConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_autoscaling_config_with_options(cluster_id, request, headers, runtime)

    async def create_autoscaling_config_async(
        self,
        cluster_id: str,
        request: main_models.CreateAutoscalingConfigRequest,
    ) -> main_models.CreateAutoscalingConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_autoscaling_config_with_options_async(cluster_id, request, headers, runtime)

    def create_cluster_with_options(
        self,
        request: main_models.CreateClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_control_list):
            body['access_control_list'] = request.access_control_list
        if not DaraCore.is_null(request.addons):
            body['addons'] = request.addons
        if not DaraCore.is_null(request.api_audiences):
            body['api_audiences'] = request.api_audiences
        if not DaraCore.is_null(request.audit_log_config):
            body['audit_log_config'] = request.audit_log_config
        if not DaraCore.is_null(request.auto_mode):
            body['auto_mode'] = request.auto_mode
        if not DaraCore.is_null(request.auto_renew):
            body['auto_renew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_period):
            body['auto_renew_period'] = request.auto_renew_period
        if not DaraCore.is_null(request.charge_type):
            body['charge_type'] = request.charge_type
        if not DaraCore.is_null(request.cis_enabled):
            body['cis_enabled'] = request.cis_enabled
        if not DaraCore.is_null(request.cloud_monitor_flags):
            body['cloud_monitor_flags'] = request.cloud_monitor_flags
        if not DaraCore.is_null(request.cluster_domain):
            body['cluster_domain'] = request.cluster_domain
        if not DaraCore.is_null(request.cluster_spec):
            body['cluster_spec'] = request.cluster_spec
        if not DaraCore.is_null(request.cluster_type):
            body['cluster_type'] = request.cluster_type
        if not DaraCore.is_null(request.container_cidr):
            body['container_cidr'] = request.container_cidr
        if not DaraCore.is_null(request.control_plane_config):
            body['control_plane_config'] = request.control_plane_config
        if not DaraCore.is_null(request.controlplane_log_components):
            body['controlplane_log_components'] = request.controlplane_log_components
        if not DaraCore.is_null(request.controlplane_log_project):
            body['controlplane_log_project'] = request.controlplane_log_project
        if not DaraCore.is_null(request.controlplane_log_ttl):
            body['controlplane_log_ttl'] = request.controlplane_log_ttl
        if not DaraCore.is_null(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not DaraCore.is_null(request.custom_san):
            body['custom_san'] = request.custom_san
        if not DaraCore.is_null(request.deletion_protection):
            body['deletion_protection'] = request.deletion_protection
        if not DaraCore.is_null(request.disable_rollback):
            body['disable_rollback'] = request.disable_rollback
        if not DaraCore.is_null(request.enable_rrsa):
            body['enable_rrsa'] = request.enable_rrsa
        if not DaraCore.is_null(request.encryption_provider_key):
            body['encryption_provider_key'] = request.encryption_provider_key
        if not DaraCore.is_null(request.endpoint_public_access):
            body['endpoint_public_access'] = request.endpoint_public_access
        if not DaraCore.is_null(request.extra_sans):
            body['extra_sans'] = request.extra_sans
        if not DaraCore.is_null(request.format_disk):
            body['format_disk'] = request.format_disk
        if not DaraCore.is_null(request.image_id):
            body['image_id'] = request.image_id
        if not DaraCore.is_null(request.image_type):
            body['image_type'] = request.image_type
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        if not DaraCore.is_null(request.ip_stack):
            body['ip_stack'] = request.ip_stack
        if not DaraCore.is_null(request.is_enterprise_security_group):
            body['is_enterprise_security_group'] = request.is_enterprise_security_group
        if not DaraCore.is_null(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not DaraCore.is_null(request.key_pair):
            body['key_pair'] = request.key_pair
        if not DaraCore.is_null(request.kubernetes_version):
            body['kubernetes_version'] = request.kubernetes_version
        if not DaraCore.is_null(request.load_balancer_id):
            body['load_balancer_id'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_spec):
            body['load_balancer_spec'] = request.load_balancer_spec
        if not DaraCore.is_null(request.logging_type):
            body['logging_type'] = request.logging_type
        if not DaraCore.is_null(request.login_password):
            body['login_password'] = request.login_password
        if not DaraCore.is_null(request.maintenance_window):
            body['maintenance_window'] = request.maintenance_window
        if not DaraCore.is_null(request.master_auto_renew):
            body['master_auto_renew'] = request.master_auto_renew
        if not DaraCore.is_null(request.master_auto_renew_period):
            body['master_auto_renew_period'] = request.master_auto_renew_period
        if not DaraCore.is_null(request.master_count):
            body['master_count'] = request.master_count
        if not DaraCore.is_null(request.master_instance_charge_type):
            body['master_instance_charge_type'] = request.master_instance_charge_type
        if not DaraCore.is_null(request.master_instance_types):
            body['master_instance_types'] = request.master_instance_types
        if not DaraCore.is_null(request.master_period):
            body['master_period'] = request.master_period
        if not DaraCore.is_null(request.master_period_unit):
            body['master_period_unit'] = request.master_period_unit
        if not DaraCore.is_null(request.master_system_disk_category):
            body['master_system_disk_category'] = request.master_system_disk_category
        if not DaraCore.is_null(request.master_system_disk_performance_level):
            body['master_system_disk_performance_level'] = request.master_system_disk_performance_level
        if not DaraCore.is_null(request.master_system_disk_size):
            body['master_system_disk_size'] = request.master_system_disk_size
        if not DaraCore.is_null(request.master_system_disk_snapshot_policy_id):
            body['master_system_disk_snapshot_policy_id'] = request.master_system_disk_snapshot_policy_id
        if not DaraCore.is_null(request.master_vswitch_ids):
            body['master_vswitch_ids'] = request.master_vswitch_ids
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.nat_gateway):
            body['nat_gateway'] = request.nat_gateway
        if not DaraCore.is_null(request.node_cidr_mask):
            body['node_cidr_mask'] = request.node_cidr_mask
        if not DaraCore.is_null(request.node_name_mode):
            body['node_name_mode'] = request.node_name_mode
        if not DaraCore.is_null(request.node_port_range):
            body['node_port_range'] = request.node_port_range
        if not DaraCore.is_null(request.nodepools):
            body['nodepools'] = request.nodepools
        if not DaraCore.is_null(request.num_of_nodes):
            body['num_of_nodes'] = request.num_of_nodes
        if not DaraCore.is_null(request.operation_policy):
            body['operation_policy'] = request.operation_policy
        if not DaraCore.is_null(request.os_type):
            body['os_type'] = request.os_type
        if not DaraCore.is_null(request.period):
            body['period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            body['period_unit'] = request.period_unit
        if not DaraCore.is_null(request.platform):
            body['platform'] = request.platform
        if not DaraCore.is_null(request.pod_vswitch_ids):
            body['pod_vswitch_ids'] = request.pod_vswitch_ids
        if not DaraCore.is_null(request.profile):
            body['profile'] = request.profile
        if not DaraCore.is_null(request.proxy_mode):
            body['proxy_mode'] = request.proxy_mode
        if not DaraCore.is_null(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not DaraCore.is_null(request.region_id):
            body['region_id'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['resource_group_id'] = request.resource_group_id
        if not DaraCore.is_null(request.rrsa_config):
            body['rrsa_config'] = request.rrsa_config
        if not DaraCore.is_null(request.runtime):
            body['runtime'] = request.runtime
        if not DaraCore.is_null(request.security_group_id):
            body['security_group_id'] = request.security_group_id
        if not DaraCore.is_null(request.security_hardening_os):
            body['security_hardening_os'] = request.security_hardening_os
        if not DaraCore.is_null(request.service_account_issuer):
            body['service_account_issuer'] = request.service_account_issuer
        if not DaraCore.is_null(request.service_cidr):
            body['service_cidr'] = request.service_cidr
        if not DaraCore.is_null(request.service_discovery_types):
            body['service_discovery_types'] = request.service_discovery_types
        if not DaraCore.is_null(request.snat_entry):
            body['snat_entry'] = request.snat_entry
        if not DaraCore.is_null(request.soc_enabled):
            body['soc_enabled'] = request.soc_enabled
        if not DaraCore.is_null(request.ssh_flags):
            body['ssh_flags'] = request.ssh_flags
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.taints):
            body['taints'] = request.taints
        if not DaraCore.is_null(request.timeout_mins):
            body['timeout_mins'] = request.timeout_mins
        if not DaraCore.is_null(request.timezone):
            body['timezone'] = request.timezone
        if not DaraCore.is_null(request.user_ca):
            body['user_ca'] = request.user_ca
        if not DaraCore.is_null(request.user_data):
            body['user_data'] = request.user_data
        if not DaraCore.is_null(request.vpcid):
            body['vpcid'] = request.vpcid
        if not DaraCore.is_null(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        if not DaraCore.is_null(request.worker_auto_renew):
            body['worker_auto_renew'] = request.worker_auto_renew
        if not DaraCore.is_null(request.worker_auto_renew_period):
            body['worker_auto_renew_period'] = request.worker_auto_renew_period
        if not DaraCore.is_null(request.worker_data_disks):
            body['worker_data_disks'] = request.worker_data_disks
        if not DaraCore.is_null(request.worker_instance_charge_type):
            body['worker_instance_charge_type'] = request.worker_instance_charge_type
        if not DaraCore.is_null(request.worker_instance_types):
            body['worker_instance_types'] = request.worker_instance_types
        if not DaraCore.is_null(request.worker_period):
            body['worker_period'] = request.worker_period
        if not DaraCore.is_null(request.worker_period_unit):
            body['worker_period_unit'] = request.worker_period_unit
        if not DaraCore.is_null(request.worker_system_disk_category):
            body['worker_system_disk_category'] = request.worker_system_disk_category
        if not DaraCore.is_null(request.worker_system_disk_performance_level):
            body['worker_system_disk_performance_level'] = request.worker_system_disk_performance_level
        if not DaraCore.is_null(request.worker_system_disk_size):
            body['worker_system_disk_size'] = request.worker_system_disk_size
        if not DaraCore.is_null(request.worker_system_disk_snapshot_policy_id):
            body['worker_system_disk_snapshot_policy_id'] = request.worker_system_disk_snapshot_policy_id
        if not DaraCore.is_null(request.worker_vswitch_ids):
            body['worker_vswitch_ids'] = request.worker_vswitch_ids
        if not DaraCore.is_null(request.zone_id):
            body['zone_id'] = request.zone_id
        if not DaraCore.is_null(request.zone_ids):
            body['zone_ids'] = request.zone_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCluster',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: main_models.CreateClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_control_list):
            body['access_control_list'] = request.access_control_list
        if not DaraCore.is_null(request.addons):
            body['addons'] = request.addons
        if not DaraCore.is_null(request.api_audiences):
            body['api_audiences'] = request.api_audiences
        if not DaraCore.is_null(request.audit_log_config):
            body['audit_log_config'] = request.audit_log_config
        if not DaraCore.is_null(request.auto_mode):
            body['auto_mode'] = request.auto_mode
        if not DaraCore.is_null(request.auto_renew):
            body['auto_renew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_period):
            body['auto_renew_period'] = request.auto_renew_period
        if not DaraCore.is_null(request.charge_type):
            body['charge_type'] = request.charge_type
        if not DaraCore.is_null(request.cis_enabled):
            body['cis_enabled'] = request.cis_enabled
        if not DaraCore.is_null(request.cloud_monitor_flags):
            body['cloud_monitor_flags'] = request.cloud_monitor_flags
        if not DaraCore.is_null(request.cluster_domain):
            body['cluster_domain'] = request.cluster_domain
        if not DaraCore.is_null(request.cluster_spec):
            body['cluster_spec'] = request.cluster_spec
        if not DaraCore.is_null(request.cluster_type):
            body['cluster_type'] = request.cluster_type
        if not DaraCore.is_null(request.container_cidr):
            body['container_cidr'] = request.container_cidr
        if not DaraCore.is_null(request.control_plane_config):
            body['control_plane_config'] = request.control_plane_config
        if not DaraCore.is_null(request.controlplane_log_components):
            body['controlplane_log_components'] = request.controlplane_log_components
        if not DaraCore.is_null(request.controlplane_log_project):
            body['controlplane_log_project'] = request.controlplane_log_project
        if not DaraCore.is_null(request.controlplane_log_ttl):
            body['controlplane_log_ttl'] = request.controlplane_log_ttl
        if not DaraCore.is_null(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not DaraCore.is_null(request.custom_san):
            body['custom_san'] = request.custom_san
        if not DaraCore.is_null(request.deletion_protection):
            body['deletion_protection'] = request.deletion_protection
        if not DaraCore.is_null(request.disable_rollback):
            body['disable_rollback'] = request.disable_rollback
        if not DaraCore.is_null(request.enable_rrsa):
            body['enable_rrsa'] = request.enable_rrsa
        if not DaraCore.is_null(request.encryption_provider_key):
            body['encryption_provider_key'] = request.encryption_provider_key
        if not DaraCore.is_null(request.endpoint_public_access):
            body['endpoint_public_access'] = request.endpoint_public_access
        if not DaraCore.is_null(request.extra_sans):
            body['extra_sans'] = request.extra_sans
        if not DaraCore.is_null(request.format_disk):
            body['format_disk'] = request.format_disk
        if not DaraCore.is_null(request.image_id):
            body['image_id'] = request.image_id
        if not DaraCore.is_null(request.image_type):
            body['image_type'] = request.image_type
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        if not DaraCore.is_null(request.ip_stack):
            body['ip_stack'] = request.ip_stack
        if not DaraCore.is_null(request.is_enterprise_security_group):
            body['is_enterprise_security_group'] = request.is_enterprise_security_group
        if not DaraCore.is_null(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not DaraCore.is_null(request.key_pair):
            body['key_pair'] = request.key_pair
        if not DaraCore.is_null(request.kubernetes_version):
            body['kubernetes_version'] = request.kubernetes_version
        if not DaraCore.is_null(request.load_balancer_id):
            body['load_balancer_id'] = request.load_balancer_id
        if not DaraCore.is_null(request.load_balancer_spec):
            body['load_balancer_spec'] = request.load_balancer_spec
        if not DaraCore.is_null(request.logging_type):
            body['logging_type'] = request.logging_type
        if not DaraCore.is_null(request.login_password):
            body['login_password'] = request.login_password
        if not DaraCore.is_null(request.maintenance_window):
            body['maintenance_window'] = request.maintenance_window
        if not DaraCore.is_null(request.master_auto_renew):
            body['master_auto_renew'] = request.master_auto_renew
        if not DaraCore.is_null(request.master_auto_renew_period):
            body['master_auto_renew_period'] = request.master_auto_renew_period
        if not DaraCore.is_null(request.master_count):
            body['master_count'] = request.master_count
        if not DaraCore.is_null(request.master_instance_charge_type):
            body['master_instance_charge_type'] = request.master_instance_charge_type
        if not DaraCore.is_null(request.master_instance_types):
            body['master_instance_types'] = request.master_instance_types
        if not DaraCore.is_null(request.master_period):
            body['master_period'] = request.master_period
        if not DaraCore.is_null(request.master_period_unit):
            body['master_period_unit'] = request.master_period_unit
        if not DaraCore.is_null(request.master_system_disk_category):
            body['master_system_disk_category'] = request.master_system_disk_category
        if not DaraCore.is_null(request.master_system_disk_performance_level):
            body['master_system_disk_performance_level'] = request.master_system_disk_performance_level
        if not DaraCore.is_null(request.master_system_disk_size):
            body['master_system_disk_size'] = request.master_system_disk_size
        if not DaraCore.is_null(request.master_system_disk_snapshot_policy_id):
            body['master_system_disk_snapshot_policy_id'] = request.master_system_disk_snapshot_policy_id
        if not DaraCore.is_null(request.master_vswitch_ids):
            body['master_vswitch_ids'] = request.master_vswitch_ids
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.nat_gateway):
            body['nat_gateway'] = request.nat_gateway
        if not DaraCore.is_null(request.node_cidr_mask):
            body['node_cidr_mask'] = request.node_cidr_mask
        if not DaraCore.is_null(request.node_name_mode):
            body['node_name_mode'] = request.node_name_mode
        if not DaraCore.is_null(request.node_port_range):
            body['node_port_range'] = request.node_port_range
        if not DaraCore.is_null(request.nodepools):
            body['nodepools'] = request.nodepools
        if not DaraCore.is_null(request.num_of_nodes):
            body['num_of_nodes'] = request.num_of_nodes
        if not DaraCore.is_null(request.operation_policy):
            body['operation_policy'] = request.operation_policy
        if not DaraCore.is_null(request.os_type):
            body['os_type'] = request.os_type
        if not DaraCore.is_null(request.period):
            body['period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            body['period_unit'] = request.period_unit
        if not DaraCore.is_null(request.platform):
            body['platform'] = request.platform
        if not DaraCore.is_null(request.pod_vswitch_ids):
            body['pod_vswitch_ids'] = request.pod_vswitch_ids
        if not DaraCore.is_null(request.profile):
            body['profile'] = request.profile
        if not DaraCore.is_null(request.proxy_mode):
            body['proxy_mode'] = request.proxy_mode
        if not DaraCore.is_null(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not DaraCore.is_null(request.region_id):
            body['region_id'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['resource_group_id'] = request.resource_group_id
        if not DaraCore.is_null(request.rrsa_config):
            body['rrsa_config'] = request.rrsa_config
        if not DaraCore.is_null(request.runtime):
            body['runtime'] = request.runtime
        if not DaraCore.is_null(request.security_group_id):
            body['security_group_id'] = request.security_group_id
        if not DaraCore.is_null(request.security_hardening_os):
            body['security_hardening_os'] = request.security_hardening_os
        if not DaraCore.is_null(request.service_account_issuer):
            body['service_account_issuer'] = request.service_account_issuer
        if not DaraCore.is_null(request.service_cidr):
            body['service_cidr'] = request.service_cidr
        if not DaraCore.is_null(request.service_discovery_types):
            body['service_discovery_types'] = request.service_discovery_types
        if not DaraCore.is_null(request.snat_entry):
            body['snat_entry'] = request.snat_entry
        if not DaraCore.is_null(request.soc_enabled):
            body['soc_enabled'] = request.soc_enabled
        if not DaraCore.is_null(request.ssh_flags):
            body['ssh_flags'] = request.ssh_flags
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.taints):
            body['taints'] = request.taints
        if not DaraCore.is_null(request.timeout_mins):
            body['timeout_mins'] = request.timeout_mins
        if not DaraCore.is_null(request.timezone):
            body['timezone'] = request.timezone
        if not DaraCore.is_null(request.user_ca):
            body['user_ca'] = request.user_ca
        if not DaraCore.is_null(request.user_data):
            body['user_data'] = request.user_data
        if not DaraCore.is_null(request.vpcid):
            body['vpcid'] = request.vpcid
        if not DaraCore.is_null(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        if not DaraCore.is_null(request.worker_auto_renew):
            body['worker_auto_renew'] = request.worker_auto_renew
        if not DaraCore.is_null(request.worker_auto_renew_period):
            body['worker_auto_renew_period'] = request.worker_auto_renew_period
        if not DaraCore.is_null(request.worker_data_disks):
            body['worker_data_disks'] = request.worker_data_disks
        if not DaraCore.is_null(request.worker_instance_charge_type):
            body['worker_instance_charge_type'] = request.worker_instance_charge_type
        if not DaraCore.is_null(request.worker_instance_types):
            body['worker_instance_types'] = request.worker_instance_types
        if not DaraCore.is_null(request.worker_period):
            body['worker_period'] = request.worker_period
        if not DaraCore.is_null(request.worker_period_unit):
            body['worker_period_unit'] = request.worker_period_unit
        if not DaraCore.is_null(request.worker_system_disk_category):
            body['worker_system_disk_category'] = request.worker_system_disk_category
        if not DaraCore.is_null(request.worker_system_disk_performance_level):
            body['worker_system_disk_performance_level'] = request.worker_system_disk_performance_level
        if not DaraCore.is_null(request.worker_system_disk_size):
            body['worker_system_disk_size'] = request.worker_system_disk_size
        if not DaraCore.is_null(request.worker_system_disk_snapshot_policy_id):
            body['worker_system_disk_snapshot_policy_id'] = request.worker_system_disk_snapshot_policy_id
        if not DaraCore.is_null(request.worker_vswitch_ids):
            body['worker_vswitch_ids'] = request.worker_vswitch_ids
        if not DaraCore.is_null(request.zone_id):
            body['zone_id'] = request.zone_id
        if not DaraCore.is_null(request.zone_ids):
            body['zone_ids'] = request.zone_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCluster',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: main_models.CreateClusterRequest,
    ) -> main_models.CreateClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_cluster_with_options(request, headers, runtime)

    async def create_cluster_async(
        self,
        request: main_models.CreateClusterRequest,
    ) -> main_models.CreateClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_cluster_with_options_async(request, headers, runtime)

    def create_cluster_diagnosis_with_options(
        self,
        cluster_id: str,
        request: main_models.CreateClusterDiagnosisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterDiagnosisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.target):
            body['target'] = request.target
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateClusterDiagnosis',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/diagnosis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterDiagnosisResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_diagnosis_with_options_async(
        self,
        cluster_id: str,
        request: main_models.CreateClusterDiagnosisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterDiagnosisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.target):
            body['target'] = request.target
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateClusterDiagnosis',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/diagnosis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterDiagnosisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster_diagnosis(
        self,
        cluster_id: str,
        request: main_models.CreateClusterDiagnosisRequest,
    ) -> main_models.CreateClusterDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_cluster_diagnosis_with_options(cluster_id, request, headers, runtime)

    async def create_cluster_diagnosis_async(
        self,
        cluster_id: str,
        request: main_models.CreateClusterDiagnosisRequest,
    ) -> main_models.CreateClusterDiagnosisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_cluster_diagnosis_with_options_async(cluster_id, request, headers, runtime)

    def create_cluster_inspect_config_with_options(
        self,
        cluster_id: str,
        request: main_models.CreateClusterInspectConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterInspectConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.disabled_check_items):
            body['disabledCheckItems'] = request.disabled_check_items
        if not DaraCore.is_null(request.enabled):
            body['enabled'] = request.enabled
        if not DaraCore.is_null(request.recurrence):
            body['recurrence'] = request.recurrence
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateClusterInspectConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/inspectConfig',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterInspectConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_inspect_config_with_options_async(
        self,
        cluster_id: str,
        request: main_models.CreateClusterInspectConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterInspectConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.disabled_check_items):
            body['disabledCheckItems'] = request.disabled_check_items
        if not DaraCore.is_null(request.enabled):
            body['enabled'] = request.enabled
        if not DaraCore.is_null(request.recurrence):
            body['recurrence'] = request.recurrence
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateClusterInspectConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/inspectConfig',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterInspectConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster_inspect_config(
        self,
        cluster_id: str,
        request: main_models.CreateClusterInspectConfigRequest,
    ) -> main_models.CreateClusterInspectConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_cluster_inspect_config_with_options(cluster_id, request, headers, runtime)

    async def create_cluster_inspect_config_async(
        self,
        cluster_id: str,
        request: main_models.CreateClusterInspectConfigRequest,
    ) -> main_models.CreateClusterInspectConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_cluster_inspect_config_with_options_async(cluster_id, request, headers, runtime)

    def create_cluster_node_pool_with_options(
        self,
        cluster_id: str,
        request: main_models.CreateClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterNodePoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_mode):
            body['auto_mode'] = request.auto_mode
        if not DaraCore.is_null(request.auto_scaling):
            body['auto_scaling'] = request.auto_scaling
        if not DaraCore.is_null(request.count):
            body['count'] = request.count
        if not DaraCore.is_null(request.eflo_node_group):
            body['eflo_node_group'] = request.eflo_node_group
        if not DaraCore.is_null(request.host_network):
            body['host_network'] = request.host_network
        if not DaraCore.is_null(request.interconnect_config):
            body['interconnect_config'] = request.interconnect_config
        if not DaraCore.is_null(request.interconnect_mode):
            body['interconnect_mode'] = request.interconnect_mode
        if not DaraCore.is_null(request.intranet):
            body['intranet'] = request.intranet
        if not DaraCore.is_null(request.kubernetes_config):
            body['kubernetes_config'] = request.kubernetes_config
        if not DaraCore.is_null(request.management):
            body['management'] = request.management
        if not DaraCore.is_null(request.max_nodes):
            body['max_nodes'] = request.max_nodes
        if not DaraCore.is_null(request.node_components):
            body['node_components'] = request.node_components
        if not DaraCore.is_null(request.node_config):
            body['node_config'] = request.node_config
        if not DaraCore.is_null(request.nodepool_info):
            body['nodepool_info'] = request.nodepool_info
        if not DaraCore.is_null(request.scaling_group):
            body['scaling_group'] = request.scaling_group
        if not DaraCore.is_null(request.tee_config):
            body['tee_config'] = request.tee_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateClusterNodePool',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_node_pool_with_options_async(
        self,
        cluster_id: str,
        request: main_models.CreateClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterNodePoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_mode):
            body['auto_mode'] = request.auto_mode
        if not DaraCore.is_null(request.auto_scaling):
            body['auto_scaling'] = request.auto_scaling
        if not DaraCore.is_null(request.count):
            body['count'] = request.count
        if not DaraCore.is_null(request.eflo_node_group):
            body['eflo_node_group'] = request.eflo_node_group
        if not DaraCore.is_null(request.host_network):
            body['host_network'] = request.host_network
        if not DaraCore.is_null(request.interconnect_config):
            body['interconnect_config'] = request.interconnect_config
        if not DaraCore.is_null(request.interconnect_mode):
            body['interconnect_mode'] = request.interconnect_mode
        if not DaraCore.is_null(request.intranet):
            body['intranet'] = request.intranet
        if not DaraCore.is_null(request.kubernetes_config):
            body['kubernetes_config'] = request.kubernetes_config
        if not DaraCore.is_null(request.management):
            body['management'] = request.management
        if not DaraCore.is_null(request.max_nodes):
            body['max_nodes'] = request.max_nodes
        if not DaraCore.is_null(request.node_components):
            body['node_components'] = request.node_components
        if not DaraCore.is_null(request.node_config):
            body['node_config'] = request.node_config
        if not DaraCore.is_null(request.nodepool_info):
            body['nodepool_info'] = request.nodepool_info
        if not DaraCore.is_null(request.scaling_group):
            body['scaling_group'] = request.scaling_group
        if not DaraCore.is_null(request.tee_config):
            body['tee_config'] = request.tee_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateClusterNodePool',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterNodePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster_node_pool(
        self,
        cluster_id: str,
        request: main_models.CreateClusterNodePoolRequest,
    ) -> main_models.CreateClusterNodePoolResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_cluster_node_pool_with_options(cluster_id, request, headers, runtime)

    async def create_cluster_node_pool_async(
        self,
        cluster_id: str,
        request: main_models.CreateClusterNodePoolRequest,
    ) -> main_models.CreateClusterNodePoolResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_cluster_node_pool_with_options_async(cluster_id, request, headers, runtime)

    def create_kubernetes_trigger_with_options(
        self,
        request: main_models.CreateKubernetesTriggerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKubernetesTriggerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.project_id):
            body['project_id'] = request.project_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKubernetesTrigger',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/triggers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKubernetesTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_kubernetes_trigger_with_options_async(
        self,
        request: main_models.CreateKubernetesTriggerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateKubernetesTriggerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.project_id):
            body['project_id'] = request.project_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateKubernetesTrigger',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/triggers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKubernetesTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_kubernetes_trigger(
        self,
        request: main_models.CreateKubernetesTriggerRequest,
    ) -> main_models.CreateKubernetesTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_kubernetes_trigger_with_options(request, headers, runtime)

    async def create_kubernetes_trigger_async(
        self,
        request: main_models.CreateKubernetesTriggerRequest,
    ) -> main_models.CreateKubernetesTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_kubernetes_trigger_with_options_async(request, headers, runtime)

    def create_template_with_options(
        self,
        request: main_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.template):
            body['template'] = request.template
        if not DaraCore.is_null(request.template_type):
            body['template_type'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/templates',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: main_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.template):
            body['template'] = request.template
        if not DaraCore.is_null(request.template_type):
            body['template_type'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/templates',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_template_with_options(request, headers, runtime)

    async def create_template_async(
        self,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_template_with_options_async(request, headers, runtime)

    def create_trigger_with_options(
        self,
        cluster_id: str,
        request: main_models.CreateTriggerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTriggerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.project_id):
            body['project_id'] = request.project_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrigger',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/triggers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_trigger_with_options_async(
        self,
        cluster_id: str,
        request: main_models.CreateTriggerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTriggerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.project_id):
            body['project_id'] = request.project_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrigger',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/triggers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_trigger(
        self,
        cluster_id: str,
        request: main_models.CreateTriggerRequest,
    ) -> main_models.CreateTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_trigger_with_options(cluster_id, request, headers, runtime)

    async def create_trigger_async(
        self,
        cluster_id: str,
        request: main_models.CreateTriggerRequest,
    ) -> main_models.CreateTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_trigger_with_options_async(cluster_id, request, headers, runtime)

    def delete_alert_contact_with_options(
        self,
        tmp_req: main_models.DeleteAlertContactRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertContactResponse:
        tmp_req.validate()
        request = main_models.DeleteAlertContactShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact_ids):
            request.contact_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact_ids, 'contact_ids', 'json')
        query = {}
        if not DaraCore.is_null(request.contact_ids_shrink):
            query['contact_ids'] = request.contact_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertContact',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/alert/contacts',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_contact_with_options_async(
        self,
        tmp_req: main_models.DeleteAlertContactRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertContactResponse:
        tmp_req.validate()
        request = main_models.DeleteAlertContactShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact_ids):
            request.contact_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact_ids, 'contact_ids', 'json')
        query = {}
        if not DaraCore.is_null(request.contact_ids_shrink):
            query['contact_ids'] = request.contact_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertContact',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/alert/contacts',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_contact(
        self,
        request: main_models.DeleteAlertContactRequest,
    ) -> main_models.DeleteAlertContactResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_alert_contact_with_options(request, headers, runtime)

    async def delete_alert_contact_async(
        self,
        request: main_models.DeleteAlertContactRequest,
    ) -> main_models.DeleteAlertContactResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_alert_contact_with_options_async(request, headers, runtime)

    def delete_alert_contact_group_with_options(
        self,
        tmp_req: main_models.DeleteAlertContactGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertContactGroupResponse:
        tmp_req.validate()
        request = main_models.DeleteAlertContactGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact_group_ids):
            request.contact_group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact_group_ids, 'contact_group_ids', 'json')
        query = {}
        if not DaraCore.is_null(request.contact_group_ids_shrink):
            query['contact_group_ids'] = request.contact_group_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertContactGroup',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/alert/contact_groups',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_contact_group_with_options_async(
        self,
        tmp_req: main_models.DeleteAlertContactGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertContactGroupResponse:
        tmp_req.validate()
        request = main_models.DeleteAlertContactGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.contact_group_ids):
            request.contact_group_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.contact_group_ids, 'contact_group_ids', 'json')
        query = {}
        if not DaraCore.is_null(request.contact_group_ids_shrink):
            query['contact_group_ids'] = request.contact_group_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertContactGroup',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/alert/contact_groups',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_contact_group(
        self,
        request: main_models.DeleteAlertContactGroupRequest,
    ) -> main_models.DeleteAlertContactGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_alert_contact_group_with_options(request, headers, runtime)

    async def delete_alert_contact_group_async(
        self,
        request: main_models.DeleteAlertContactGroupRequest,
    ) -> main_models.DeleteAlertContactGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_alert_contact_group_with_options_async(request, headers, runtime)

    def delete_cluster_with_options(
        self,
        cluster_id: str,
        tmp_req: main_models.DeleteClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterResponse:
        tmp_req.validate()
        request = main_models.DeleteClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_options):
            request.delete_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_options, 'delete_options', 'json')
        if not DaraCore.is_null(tmp_req.retain_resources):
            request.retain_resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.retain_resources, 'retain_resources', 'json')
        query = {}
        if not DaraCore.is_null(request.delete_options_shrink):
            query['delete_options'] = request.delete_options_shrink
        if not DaraCore.is_null(request.keep_slb):
            query['keep_slb'] = request.keep_slb
        if not DaraCore.is_null(request.retain_all_resources):
            query['retain_all_resources'] = request.retain_all_resources
        if not DaraCore.is_null(request.retain_resources_shrink):
            query['retain_resources'] = request.retain_resources_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCluster',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}',
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
        cluster_id: str,
        tmp_req: main_models.DeleteClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterResponse:
        tmp_req.validate()
        request = main_models.DeleteClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_options):
            request.delete_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_options, 'delete_options', 'json')
        if not DaraCore.is_null(tmp_req.retain_resources):
            request.retain_resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.retain_resources, 'retain_resources', 'json')
        query = {}
        if not DaraCore.is_null(request.delete_options_shrink):
            query['delete_options'] = request.delete_options_shrink
        if not DaraCore.is_null(request.keep_slb):
            query['keep_slb'] = request.keep_slb
        if not DaraCore.is_null(request.retain_all_resources):
            query['retain_all_resources'] = request.retain_all_resources
        if not DaraCore.is_null(request.retain_resources_shrink):
            query['retain_resources'] = request.retain_resources_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCluster',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}',
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
        cluster_id: str,
        request: main_models.DeleteClusterRequest,
    ) -> main_models.DeleteClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_cluster_with_options(cluster_id, request, headers, runtime)

    async def delete_cluster_async(
        self,
        cluster_id: str,
        request: main_models.DeleteClusterRequest,
    ) -> main_models.DeleteClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_cluster_with_options_async(cluster_id, request, headers, runtime)

    def delete_cluster_inspect_config_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterInspectConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteClusterInspectConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/inspectConfig',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClusterInspectConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_inspect_config_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterInspectConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteClusterInspectConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/inspectConfig',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClusterInspectConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster_inspect_config(
        self,
        cluster_id: str,
    ) -> main_models.DeleteClusterInspectConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_cluster_inspect_config_with_options(cluster_id, headers, runtime)

    async def delete_cluster_inspect_config_async(
        self,
        cluster_id: str,
    ) -> main_models.DeleteClusterInspectConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_cluster_inspect_config_with_options_async(cluster_id, headers, runtime)

    def delete_cluster_nodepool_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.DeleteClusterNodepoolRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterNodepoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClusterNodepool',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClusterNodepoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_nodepool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.DeleteClusterNodepoolRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterNodepoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['force'] = request.force
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClusterNodepool',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClusterNodepoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster_nodepool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.DeleteClusterNodepoolRequest,
    ) -> main_models.DeleteClusterNodepoolResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_cluster_nodepool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def delete_cluster_nodepool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.DeleteClusterNodepoolRequest,
    ) -> main_models.DeleteClusterNodepoolResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_cluster_nodepool_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def delete_cluster_nodes_with_options(
        self,
        cluster_id: str,
        request: main_models.DeleteClusterNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterNodesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drain_node):
            body['drain_node'] = request.drain_node
        if not DaraCore.is_null(request.nodes):
            body['nodes'] = request.nodes
        if not DaraCore.is_null(request.release_node):
            body['release_node'] = request.release_node
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClusterNodes',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClusterNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_nodes_with_options_async(
        self,
        cluster_id: str,
        request: main_models.DeleteClusterNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterNodesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drain_node):
            body['drain_node'] = request.drain_node
        if not DaraCore.is_null(request.nodes):
            body['nodes'] = request.nodes
        if not DaraCore.is_null(request.release_node):
            body['release_node'] = request.release_node
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClusterNodes',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClusterNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster_nodes(
        self,
        cluster_id: str,
        request: main_models.DeleteClusterNodesRequest,
    ) -> main_models.DeleteClusterNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_cluster_nodes_with_options(cluster_id, request, headers, runtime)

    async def delete_cluster_nodes_async(
        self,
        cluster_id: str,
        request: main_models.DeleteClusterNodesRequest,
    ) -> main_models.DeleteClusterNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_cluster_nodes_with_options_async(cluster_id, request, headers, runtime)

    def delete_kubernetes_trigger_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKubernetesTriggerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteKubernetesTrigger',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/triggers/revoke/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteKubernetesTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_kubernetes_trigger_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKubernetesTriggerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteKubernetesTrigger',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/triggers/revoke/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteKubernetesTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_kubernetes_trigger(
        self,
        id: str,
    ) -> main_models.DeleteKubernetesTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_kubernetes_trigger_with_options(id, headers, runtime)

    async def delete_kubernetes_trigger_async(
        self,
        id: str,
    ) -> main_models.DeleteKubernetesTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_kubernetes_trigger_with_options_async(id, headers, runtime)

    def delete_policy_instance_with_options(
        self,
        cluster_id: str,
        policy_name: str,
        request: main_models.DeletePolicyInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['instance_name'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicyInstance',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/policies/{DaraURL.percent_encode(policy_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_instance_with_options_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: main_models.DeletePolicyInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['instance_name'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicyInstance',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/policies/{DaraURL.percent_encode(policy_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_instance(
        self,
        cluster_id: str,
        policy_name: str,
        request: main_models.DeletePolicyInstanceRequest,
    ) -> main_models.DeletePolicyInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_policy_instance_with_options(cluster_id, policy_name, request, headers, runtime)

    async def delete_policy_instance_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: main_models.DeletePolicyInstanceRequest,
    ) -> main_models.DeletePolicyInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_policy_instance_with_options_async(cluster_id, policy_name, request, headers, runtime)

    def delete_template_with_options(
        self,
        template_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/templates/{DaraURL.percent_encode(template_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        template_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/templates/{DaraURL.percent_encode(template_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        template_id: str,
    ) -> main_models.DeleteTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_template_with_options(template_id, headers, runtime)

    async def delete_template_async(
        self,
        template_id: str,
    ) -> main_models.DeleteTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_template_with_options_async(template_id, headers, runtime)

    def delete_trigger_with_options(
        self,
        cluster_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTriggerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrigger',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/triggers/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_trigger_with_options_async(
        self,
        cluster_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTriggerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrigger',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/triggers/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_trigger(
        self,
        cluster_id: str,
        id: str,
    ) -> main_models.DeleteTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_trigger_with_options(cluster_id, id, headers, runtime)

    async def delete_trigger_async(
        self,
        cluster_id: str,
        id: str,
    ) -> main_models.DeleteTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_trigger_with_options_async(cluster_id, id, headers, runtime)

    def deploy_policy_instance_with_options(
        self,
        cluster_id: str,
        policy_name: str,
        request: main_models.DeployPolicyInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeployPolicyInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.namespaces):
            body['namespaces'] = request.namespaces
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeployPolicyInstance',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/policies/{DaraURL.percent_encode(policy_name)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployPolicyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_policy_instance_with_options_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: main_models.DeployPolicyInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeployPolicyInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.namespaces):
            body['namespaces'] = request.namespaces
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeployPolicyInstance',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/policies/{DaraURL.percent_encode(policy_name)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployPolicyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_policy_instance(
        self,
        cluster_id: str,
        policy_name: str,
        request: main_models.DeployPolicyInstanceRequest,
    ) -> main_models.DeployPolicyInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.deploy_policy_instance_with_options(cluster_id, policy_name, request, headers, runtime)

    async def deploy_policy_instance_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: main_models.DeployPolicyInstanceRequest,
    ) -> main_models.DeployPolicyInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.deploy_policy_instance_with_options_async(cluster_id, policy_name, request, headers, runtime)

    def describe_addon_with_options(
        self,
        addon_name: str,
        request: main_models.DescribeAddonRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAddonResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not DaraCore.is_null(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not DaraCore.is_null(request.cluster_version):
            query['cluster_version'] = request.cluster_version
        if not DaraCore.is_null(request.profile):
            query['profile'] = request.profile
        if not DaraCore.is_null(request.region_id):
            query['region_id'] = request.region_id
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAddon',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/addons/{DaraURL.percent_encode(addon_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAddonResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_addon_with_options_async(
        self,
        addon_name: str,
        request: main_models.DescribeAddonRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAddonResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not DaraCore.is_null(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not DaraCore.is_null(request.cluster_version):
            query['cluster_version'] = request.cluster_version
        if not DaraCore.is_null(request.profile):
            query['profile'] = request.profile
        if not DaraCore.is_null(request.region_id):
            query['region_id'] = request.region_id
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAddon',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/addons/{DaraURL.percent_encode(addon_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAddonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_addon(
        self,
        addon_name: str,
        request: main_models.DescribeAddonRequest,
    ) -> main_models.DescribeAddonResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_addon_with_options(addon_name, request, headers, runtime)

    async def describe_addon_async(
        self,
        addon_name: str,
        request: main_models.DescribeAddonRequest,
    ) -> main_models.DescribeAddonResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_addon_with_options_async(addon_name, request, headers, runtime)

    def describe_addons_with_options(
        self,
        request: main_models.DescribeAddonsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAddonsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_profile):
            query['cluster_profile'] = request.cluster_profile
        if not DaraCore.is_null(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not DaraCore.is_null(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not DaraCore.is_null(request.cluster_version):
            query['cluster_version'] = request.cluster_version
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAddons',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/components/metadata',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_addons_with_options_async(
        self,
        request: main_models.DescribeAddonsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAddonsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_profile):
            query['cluster_profile'] = request.cluster_profile
        if not DaraCore.is_null(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not DaraCore.is_null(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not DaraCore.is_null(request.cluster_version):
            query['cluster_version'] = request.cluster_version
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAddons',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/components/metadata',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_addons(
        self,
        request: main_models.DescribeAddonsRequest,
    ) -> main_models.DescribeAddonsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_addons_with_options(request, headers, runtime)

    async def describe_addons_async(
        self,
        request: main_models.DescribeAddonsRequest,
    ) -> main_models.DescribeAddonsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_addons_with_options_async(request, headers, runtime)

    def describe_cluster_addon_instance_with_options(
        self,
        cluster_id: str,
        addon_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterAddonInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterAddonInstance',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/{DaraURL.percent_encode(addon_name)}/instance',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterAddonInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_addon_instance_with_options_async(
        self,
        cluster_id: str,
        addon_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterAddonInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterAddonInstance',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/{DaraURL.percent_encode(addon_name)}/instance',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterAddonInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_addon_instance(
        self,
        cluster_id: str,
        addon_name: str,
    ) -> main_models.DescribeClusterAddonInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_cluster_addon_instance_with_options(cluster_id, addon_name, headers, runtime)

    async def describe_cluster_addon_instance_async(
        self,
        cluster_id: str,
        addon_name: str,
    ) -> main_models.DescribeClusterAddonInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_cluster_addon_instance_with_options_async(cluster_id, addon_name, headers, runtime)

    def describe_cluster_addon_metadata_with_options(
        self,
        cluster_id: str,
        component_id: str,
        request: main_models.DescribeClusterAddonMetadataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterAddonMetadataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterAddonMetadata',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/{DaraURL.percent_encode(component_id)}/metadata',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterAddonMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_addon_metadata_with_options_async(
        self,
        cluster_id: str,
        component_id: str,
        request: main_models.DescribeClusterAddonMetadataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterAddonMetadataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterAddonMetadata',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/{DaraURL.percent_encode(component_id)}/metadata',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterAddonMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_addon_metadata(
        self,
        cluster_id: str,
        component_id: str,
        request: main_models.DescribeClusterAddonMetadataRequest,
    ) -> main_models.DescribeClusterAddonMetadataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_cluster_addon_metadata_with_options(cluster_id, component_id, request, headers, runtime)

    async def describe_cluster_addon_metadata_async(
        self,
        cluster_id: str,
        component_id: str,
        request: main_models.DescribeClusterAddonMetadataRequest,
    ) -> main_models.DescribeClusterAddonMetadataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_cluster_addon_metadata_with_options_async(cluster_id, component_id, request, headers, runtime)

    def describe_cluster_addon_upgrade_status_with_options(
        self,
        cluster_id: str,
        component_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterAddonUpgradeStatusResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterAddonUpgradeStatus',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/{DaraURL.percent_encode(component_id)}/upgradestatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterAddonUpgradeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_addon_upgrade_status_with_options_async(
        self,
        cluster_id: str,
        component_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterAddonUpgradeStatusResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterAddonUpgradeStatus',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/{DaraURL.percent_encode(component_id)}/upgradestatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterAddonUpgradeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_addon_upgrade_status(
        self,
        cluster_id: str,
        component_id: str,
    ) -> main_models.DescribeClusterAddonUpgradeStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_cluster_addon_upgrade_status_with_options(cluster_id, component_id, headers, runtime)

    async def describe_cluster_addon_upgrade_status_async(
        self,
        cluster_id: str,
        component_id: str,
    ) -> main_models.DescribeClusterAddonUpgradeStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_cluster_addon_upgrade_status_with_options_async(cluster_id, component_id, headers, runtime)

    def describe_cluster_addons_upgrade_status_with_options(
        self,
        cluster_id: str,
        tmp_req: main_models.DescribeClusterAddonsUpgradeStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterAddonsUpgradeStatusResponse:
        tmp_req.validate()
        request = main_models.DescribeClusterAddonsUpgradeStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.component_ids):
            request.component_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.component_ids, 'componentIds', 'json')
        query = {}
        if not DaraCore.is_null(request.component_ids_shrink):
            query['componentIds'] = request.component_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterAddonsUpgradeStatus',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/upgradestatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterAddonsUpgradeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_addons_upgrade_status_with_options_async(
        self,
        cluster_id: str,
        tmp_req: main_models.DescribeClusterAddonsUpgradeStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterAddonsUpgradeStatusResponse:
        tmp_req.validate()
        request = main_models.DescribeClusterAddonsUpgradeStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.component_ids):
            request.component_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.component_ids, 'componentIds', 'json')
        query = {}
        if not DaraCore.is_null(request.component_ids_shrink):
            query['componentIds'] = request.component_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterAddonsUpgradeStatus',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/upgradestatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterAddonsUpgradeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_addons_upgrade_status(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterAddonsUpgradeStatusRequest,
    ) -> main_models.DescribeClusterAddonsUpgradeStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_cluster_addons_upgrade_status_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_addons_upgrade_status_async(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterAddonsUpgradeStatusRequest,
    ) -> main_models.DescribeClusterAddonsUpgradeStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_cluster_addons_upgrade_status_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_addons_version_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterAddonsVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterAddonsVersion',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/version',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterAddonsVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_addons_version_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterAddonsVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterAddonsVersion',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/version',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterAddonsVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_addons_version(
        self,
        cluster_id: str,
    ) -> main_models.DescribeClusterAddonsVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_cluster_addons_version_with_options(cluster_id, headers, runtime)

    async def describe_cluster_addons_version_async(
        self,
        cluster_id: str,
    ) -> main_models.DescribeClusterAddonsVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_cluster_addons_version_with_options_async(cluster_id, headers, runtime)

    def describe_cluster_attach_scripts_with_options(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterAttachScriptsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterAttachScriptsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.arch):
            body['arch'] = request.arch
        if not DaraCore.is_null(request.expired):
            body['expired'] = request.expired
        if not DaraCore.is_null(request.format_disk):
            body['format_disk'] = request.format_disk
        if not DaraCore.is_null(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not DaraCore.is_null(request.nodepool_id):
            body['nodepool_id'] = request.nodepool_id
        if not DaraCore.is_null(request.one_time_token):
            body['one_time_token'] = request.one_time_token
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        if not DaraCore.is_null(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterAttachScripts',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/attachscript',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterAttachScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_attach_scripts_with_options_async(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterAttachScriptsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterAttachScriptsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.arch):
            body['arch'] = request.arch
        if not DaraCore.is_null(request.expired):
            body['expired'] = request.expired
        if not DaraCore.is_null(request.format_disk):
            body['format_disk'] = request.format_disk
        if not DaraCore.is_null(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not DaraCore.is_null(request.nodepool_id):
            body['nodepool_id'] = request.nodepool_id
        if not DaraCore.is_null(request.one_time_token):
            body['one_time_token'] = request.one_time_token
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        if not DaraCore.is_null(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterAttachScripts',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/attachscript',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'string'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterAttachScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_attach_scripts(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterAttachScriptsRequest,
    ) -> main_models.DescribeClusterAttachScriptsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_cluster_attach_scripts_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_attach_scripts_async(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterAttachScriptsRequest,
    ) -> main_models.DescribeClusterAttachScriptsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_cluster_attach_scripts_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_detail_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterDetailResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterDetail',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_detail_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterDetailResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterDetail',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_detail(
        self,
        cluster_id: str,
    ) -> main_models.DescribeClusterDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_cluster_detail_with_options(cluster_id, headers, runtime)

    async def describe_cluster_detail_async(
        self,
        cluster_id: str,
    ) -> main_models.DescribeClusterDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_cluster_detail_with_options_async(cluster_id, headers, runtime)

    def describe_cluster_events_with_options(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterEvents',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_events_with_options_async(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterEvents',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_events(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterEventsRequest,
    ) -> main_models.DescribeClusterEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_cluster_events_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_events_async(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterEventsRequest,
    ) -> main_models.DescribeClusterEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_cluster_events_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_logs_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterLogsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterLogs',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_logs_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterLogsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterLogs',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_logs(
        self,
        cluster_id: str,
    ) -> main_models.DescribeClusterLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_cluster_logs_with_options(cluster_id, headers, runtime)

    async def describe_cluster_logs_async(
        self,
        cluster_id: str,
    ) -> main_models.DescribeClusterLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_cluster_logs_with_options_async(cluster_id, headers, runtime)

    def describe_cluster_node_pool_detail_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterNodePoolDetailResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterNodePoolDetail',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterNodePoolDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_node_pool_detail_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterNodePoolDetailResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterNodePoolDetail',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterNodePoolDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_node_pool_detail(
        self,
        cluster_id: str,
        nodepool_id: str,
    ) -> main_models.DescribeClusterNodePoolDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_cluster_node_pool_detail_with_options(cluster_id, nodepool_id, headers, runtime)

    async def describe_cluster_node_pool_detail_async(
        self,
        cluster_id: str,
        nodepool_id: str,
    ) -> main_models.DescribeClusterNodePoolDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_cluster_node_pool_detail_with_options_async(cluster_id, nodepool_id, headers, runtime)

    def describe_cluster_node_pools_with_options(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterNodePoolsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterNodePoolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.nodepool_name):
            query['NodepoolName'] = request.nodepool_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterNodePools',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterNodePoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_node_pools_with_options_async(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterNodePoolsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterNodePoolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.nodepool_name):
            query['NodepoolName'] = request.nodepool_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterNodePools',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterNodePoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_node_pools(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterNodePoolsRequest,
    ) -> main_models.DescribeClusterNodePoolsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_cluster_node_pools_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_node_pools_async(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterNodePoolsRequest,
    ) -> main_models.DescribeClusterNodePoolsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_cluster_node_pools_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_nodes_with_options(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['instanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.nodepool_id):
            query['nodepool_id'] = request.nodepool_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.state):
            query['state'] = request.state
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterNodes',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_nodes_with_options_async(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['instanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.nodepool_id):
            query['nodepool_id'] = request.nodepool_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.state):
            query['state'] = request.state
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterNodes',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_nodes(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterNodesRequest,
    ) -> main_models.DescribeClusterNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_cluster_nodes_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_nodes_async(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterNodesRequest,
    ) -> main_models.DescribeClusterNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_cluster_nodes_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_resources_with_options(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.with_addon_resources):
            query['with_addon_resources'] = request.with_addon_resources
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterResources',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_resources_with_options_async(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.with_addon_resources):
            query['with_addon_resources'] = request.with_addon_resources
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterResources',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_resources(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterResourcesRequest,
    ) -> main_models.DescribeClusterResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_cluster_resources_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_resources_async(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterResourcesRequest,
    ) -> main_models.DescribeClusterResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_cluster_resources_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_tasks_with_options(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterTasks',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_tasks_with_options_async(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterTasks',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_tasks(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterTasksRequest,
    ) -> main_models.DescribeClusterTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_cluster_tasks_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_tasks_async(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterTasksRequest,
    ) -> main_models.DescribeClusterTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_cluster_tasks_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_user_kubeconfig_with_options(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterUserKubeconfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterUserKubeconfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.temporary_duration_minutes):
            query['TemporaryDurationMinutes'] = request.temporary_duration_minutes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterUserKubeconfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/k8s/{DaraURL.percent_encode(cluster_id)}/user_config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterUserKubeconfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_user_kubeconfig_with_options_async(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterUserKubeconfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterUserKubeconfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.temporary_duration_minutes):
            query['TemporaryDurationMinutes'] = request.temporary_duration_minutes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterUserKubeconfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/k8s/{DaraURL.percent_encode(cluster_id)}/user_config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterUserKubeconfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_user_kubeconfig(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterUserKubeconfigRequest,
    ) -> main_models.DescribeClusterUserKubeconfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_cluster_user_kubeconfig_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_user_kubeconfig_async(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterUserKubeconfigRequest,
    ) -> main_models.DescribeClusterUserKubeconfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_cluster_user_kubeconfig_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_v2user_kubeconfig_with_options(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterV2UserKubeconfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterV2UserKubeconfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.temporary_duration_minutes):
            query['TemporaryDurationMinutes'] = request.temporary_duration_minutes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterV2UserKubeconfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/k8s/{DaraURL.percent_encode(cluster_id)}/user_config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterV2UserKubeconfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_v2user_kubeconfig_with_options_async(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterV2UserKubeconfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterV2UserKubeconfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.temporary_duration_minutes):
            query['TemporaryDurationMinutes'] = request.temporary_duration_minutes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterV2UserKubeconfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/k8s/{DaraURL.percent_encode(cluster_id)}/user_config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterV2UserKubeconfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_v2user_kubeconfig(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterV2UserKubeconfigRequest,
    ) -> main_models.DescribeClusterV2UserKubeconfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_cluster_v2user_kubeconfig_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_v2user_kubeconfig_async(
        self,
        cluster_id: str,
        request: main_models.DescribeClusterV2UserKubeconfigRequest,
    ) -> main_models.DescribeClusterV2UserKubeconfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_cluster_v2user_kubeconfig_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_vuls_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterVulsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterVuls',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/vuls',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterVulsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_vuls_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterVulsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterVuls',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/vuls',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterVulsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_vuls(
        self,
        cluster_id: str,
    ) -> main_models.DescribeClusterVulsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_cluster_vuls_with_options(cluster_id, headers, runtime)

    async def describe_cluster_vuls_async(
        self,
        cluster_id: str,
    ) -> main_models.DescribeClusterVulsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_cluster_vuls_with_options_async(cluster_id, headers, runtime)

    def describe_clusters_with_options(
        self,
        request: main_models.DescribeClustersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_type):
            query['clusterType'] = request.cluster_type
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['resource_group_id'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusters',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_clusters_with_options_async(
        self,
        request: main_models.DescribeClustersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_type):
            query['clusterType'] = request.cluster_type
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['resource_group_id'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusters',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_clusters(
        self,
        request: main_models.DescribeClustersRequest,
    ) -> main_models.DescribeClustersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_clusters_with_options(request, headers, runtime)

    async def describe_clusters_async(
        self,
        request: main_models.DescribeClustersRequest,
    ) -> main_models.DescribeClustersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_clusters_with_options_async(request, headers, runtime)

    def describe_clusters_for_region_with_options(
        self,
        region_id: str,
        request: main_models.DescribeClustersForRegionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClustersForRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not DaraCore.is_null(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.profile):
            query['profile'] = request.profile
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClustersForRegion',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/regions/{DaraURL.percent_encode(region_id)}/clusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClustersForRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_clusters_for_region_with_options_async(
        self,
        region_id: str,
        request: main_models.DescribeClustersForRegionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClustersForRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not DaraCore.is_null(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.profile):
            query['profile'] = request.profile
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClustersForRegion',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/regions/{DaraURL.percent_encode(region_id)}/clusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClustersForRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_clusters_for_region(
        self,
        region_id: str,
        request: main_models.DescribeClustersForRegionRequest,
    ) -> main_models.DescribeClustersForRegionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_clusters_for_region_with_options(region_id, request, headers, runtime)

    async def describe_clusters_for_region_async(
        self,
        region_id: str,
        request: main_models.DescribeClustersForRegionRequest,
    ) -> main_models.DescribeClustersForRegionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_clusters_for_region_with_options_async(region_id, request, headers, runtime)

    def describe_clusters_v1with_options(
        self,
        request: main_models.DescribeClustersV1Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClustersV1Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not DaraCore.is_null(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.profile):
            query['profile'] = request.profile
        if not DaraCore.is_null(request.region_id):
            query['region_id'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClustersV1',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v1/clusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClustersV1Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_clusters_v1with_options_async(
        self,
        request: main_models.DescribeClustersV1Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClustersV1Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not DaraCore.is_null(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.profile):
            query['profile'] = request.profile
        if not DaraCore.is_null(request.region_id):
            query['region_id'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClustersV1',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v1/clusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClustersV1Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_clusters_v1(
        self,
        request: main_models.DescribeClustersV1Request,
    ) -> main_models.DescribeClustersV1Response:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_clusters_v1with_options(request, headers, runtime)

    async def describe_clusters_v1_async(
        self,
        request: main_models.DescribeClustersV1Request,
    ) -> main_models.DescribeClustersV1Response:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_clusters_v1with_options_async(request, headers, runtime)

    def describe_events_with_options(
        self,
        request: main_models.DescribeEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEvents',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_events_with_options_async(
        self,
        request: main_models.DescribeEventsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEvents',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_events(
        self,
        request: main_models.DescribeEventsRequest,
    ) -> main_models.DescribeEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_events_with_options(request, headers, runtime)

    async def describe_events_async(
        self,
        request: main_models.DescribeEventsRequest,
    ) -> main_models.DescribeEventsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_events_with_options_async(request, headers, runtime)

    def describe_events_for_region_with_options(
        self,
        region_id: str,
        request: main_models.DescribeEventsForRegionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventsForRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventsForRegion',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/regions/{DaraURL.percent_encode(region_id)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventsForRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_events_for_region_with_options_async(
        self,
        region_id: str,
        request: main_models.DescribeEventsForRegionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventsForRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventsForRegion',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/regions/{DaraURL.percent_encode(region_id)}/events',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventsForRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_events_for_region(
        self,
        region_id: str,
        request: main_models.DescribeEventsForRegionRequest,
    ) -> main_models.DescribeEventsForRegionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_events_for_region_with_options(region_id, request, headers, runtime)

    async def describe_events_for_region_async(
        self,
        region_id: str,
        request: main_models.DescribeEventsForRegionRequest,
    ) -> main_models.DescribeEventsForRegionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_events_for_region_with_options_async(region_id, request, headers, runtime)

    def describe_external_agent_with_options(
        self,
        cluster_id: str,
        request: main_models.DescribeExternalAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExternalAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_mode):
            query['AgentMode'] = request.agent_mode
        if not DaraCore.is_null(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExternalAgent',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/k8s/{DaraURL.percent_encode(cluster_id)}/external/agent/deployment',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExternalAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_external_agent_with_options_async(
        self,
        cluster_id: str,
        request: main_models.DescribeExternalAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExternalAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_mode):
            query['AgentMode'] = request.agent_mode
        if not DaraCore.is_null(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExternalAgent',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/k8s/{DaraURL.percent_encode(cluster_id)}/external/agent/deployment',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExternalAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_external_agent(
        self,
        cluster_id: str,
        request: main_models.DescribeExternalAgentRequest,
    ) -> main_models.DescribeExternalAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_external_agent_with_options(cluster_id, request, headers, runtime)

    async def describe_external_agent_async(
        self,
        cluster_id: str,
        request: main_models.DescribeExternalAgentRequest,
    ) -> main_models.DescribeExternalAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_external_agent_with_options_async(cluster_id, request, headers, runtime)

    def describe_kubernetes_version_metadata_with_options(
        self,
        request: main_models.DescribeKubernetesVersionMetadataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKubernetesVersionMetadataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.kubernetes_version):
            query['KubernetesVersion'] = request.kubernetes_version
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.profile):
            query['Profile'] = request.profile
        if not DaraCore.is_null(request.query_upgradable_version):
            query['QueryUpgradableVersion'] = request.query_upgradable_version
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.runtime):
            query['runtime'] = request.runtime
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKubernetesVersionMetadata',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v1/metadata/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeKubernetesVersionMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kubernetes_version_metadata_with_options_async(
        self,
        request: main_models.DescribeKubernetesVersionMetadataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKubernetesVersionMetadataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.kubernetes_version):
            query['KubernetesVersion'] = request.kubernetes_version
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.profile):
            query['Profile'] = request.profile
        if not DaraCore.is_null(request.query_upgradable_version):
            query['QueryUpgradableVersion'] = request.query_upgradable_version
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.runtime):
            query['runtime'] = request.runtime
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKubernetesVersionMetadata',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v1/metadata/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeKubernetesVersionMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kubernetes_version_metadata(
        self,
        request: main_models.DescribeKubernetesVersionMetadataRequest,
    ) -> main_models.DescribeKubernetesVersionMetadataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_kubernetes_version_metadata_with_options(request, headers, runtime)

    async def describe_kubernetes_version_metadata_async(
        self,
        request: main_models.DescribeKubernetesVersionMetadataRequest,
    ) -> main_models.DescribeKubernetesVersionMetadataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_kubernetes_version_metadata_with_options_async(request, headers, runtime)

    def describe_node_pool_vuls_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.DescribeNodePoolVulsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNodePoolVulsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.necessity):
            query['necessity'] = request.necessity
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNodePoolVuls',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}/vuls',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNodePoolVulsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_node_pool_vuls_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.DescribeNodePoolVulsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNodePoolVulsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.necessity):
            query['necessity'] = request.necessity
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNodePoolVuls',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}/vuls',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNodePoolVulsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_node_pool_vuls(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.DescribeNodePoolVulsRequest,
    ) -> main_models.DescribeNodePoolVulsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_node_pool_vuls_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def describe_node_pool_vuls_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.DescribeNodePoolVulsRequest,
    ) -> main_models.DescribeNodePoolVulsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_node_pool_vuls_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def describe_policies_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribePoliciesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicies',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/policies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policies_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribePoliciesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicies',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/policies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policies(self) -> main_models.DescribePoliciesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_policies_with_options(headers, runtime)

    async def describe_policies_async(self) -> main_models.DescribePoliciesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_policies_with_options_async(headers, runtime)

    def describe_policy_details_with_options(
        self,
        policy_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolicyDetailsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicyDetails',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/policies/{DaraURL.percent_encode(policy_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePolicyDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_details_with_options_async(
        self,
        policy_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolicyDetailsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicyDetails',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/policies/{DaraURL.percent_encode(policy_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePolicyDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy_details(
        self,
        policy_name: str,
    ) -> main_models.DescribePolicyDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_policy_details_with_options(policy_name, headers, runtime)

    async def describe_policy_details_async(
        self,
        policy_name: str,
    ) -> main_models.DescribePolicyDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_policy_details_with_options_async(policy_name, headers, runtime)

    def describe_policy_governance_in_cluster_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolicyGovernanceInClusterResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicyGovernanceInCluster',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/policygovernance',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePolicyGovernanceInClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_governance_in_cluster_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolicyGovernanceInClusterResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicyGovernanceInCluster',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/policygovernance',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePolicyGovernanceInClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy_governance_in_cluster(
        self,
        cluster_id: str,
    ) -> main_models.DescribePolicyGovernanceInClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_policy_governance_in_cluster_with_options(cluster_id, headers, runtime)

    async def describe_policy_governance_in_cluster_async(
        self,
        cluster_id: str,
    ) -> main_models.DescribePolicyGovernanceInClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_policy_governance_in_cluster_with_options_async(cluster_id, headers, runtime)

    def describe_policy_instances_with_options(
        self,
        cluster_id: str,
        request: main_models.DescribePolicyInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolicyInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['instance_name'] = request.instance_name
        if not DaraCore.is_null(request.policy_name):
            query['policy_name'] = request.policy_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicyInstances',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/policies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribePolicyInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_instances_with_options_async(
        self,
        cluster_id: str,
        request: main_models.DescribePolicyInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolicyInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['instance_name'] = request.instance_name
        if not DaraCore.is_null(request.policy_name):
            query['policy_name'] = request.policy_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicyInstances',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/policies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribePolicyInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy_instances(
        self,
        cluster_id: str,
        request: main_models.DescribePolicyInstancesRequest,
    ) -> main_models.DescribePolicyInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_policy_instances_with_options(cluster_id, request, headers, runtime)

    async def describe_policy_instances_async(
        self,
        cluster_id: str,
        request: main_models.DescribePolicyInstancesRequest,
    ) -> main_models.DescribePolicyInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_policy_instances_with_options_async(cluster_id, request, headers, runtime)

    def describe_policy_instances_status_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolicyInstancesStatusResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicyInstancesStatus',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/policies/status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePolicyInstancesStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_instances_status_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolicyInstancesStatusResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicyInstancesStatus',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/policies/status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePolicyInstancesStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy_instances_status(
        self,
        cluster_id: str,
    ) -> main_models.DescribePolicyInstancesStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_policy_instances_status_with_options(cluster_id, headers, runtime)

    async def describe_policy_instances_status_async(
        self,
        cluster_id: str,
    ) -> main_models.DescribePolicyInstancesStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_policy_instances_status_with_options_async(cluster_id, headers, runtime)

    def describe_resources_delete_protection_with_options(
        self,
        cluster_id: str,
        resource_type: str,
        request: main_models.DescribeResourcesDeleteProtectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourcesDeleteProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.resources):
            query['resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourcesDeleteProtection',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/resources/{DaraURL.percent_encode(resource_type)}/protection',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeResourcesDeleteProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resources_delete_protection_with_options_async(
        self,
        cluster_id: str,
        resource_type: str,
        request: main_models.DescribeResourcesDeleteProtectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourcesDeleteProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.resources):
            query['resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourcesDeleteProtection',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/resources/{DaraURL.percent_encode(resource_type)}/protection',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeResourcesDeleteProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resources_delete_protection(
        self,
        cluster_id: str,
        resource_type: str,
        request: main_models.DescribeResourcesDeleteProtectionRequest,
    ) -> main_models.DescribeResourcesDeleteProtectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_resources_delete_protection_with_options(cluster_id, resource_type, request, headers, runtime)

    async def describe_resources_delete_protection_async(
        self,
        cluster_id: str,
        resource_type: str,
        request: main_models.DescribeResourcesDeleteProtectionRequest,
    ) -> main_models.DescribeResourcesDeleteProtectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_resources_delete_protection_with_options_async(cluster_id, resource_type, request, headers, runtime)

    def describe_subaccount_k8s_cluster_user_config_with_options(
        self,
        cluster_id: str,
        uid: str,
        request: main_models.DescribeSubaccountK8sClusterUserConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSubaccountK8sClusterUserConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.temporary_duration_minutes):
            query['TemporaryDurationMinutes'] = request.temporary_duration_minutes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSubaccountK8sClusterUserConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/k8s/{DaraURL.percent_encode(cluster_id)}/users/{DaraURL.percent_encode(uid)}/user_config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSubaccountK8sClusterUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_subaccount_k8s_cluster_user_config_with_options_async(
        self,
        cluster_id: str,
        uid: str,
        request: main_models.DescribeSubaccountK8sClusterUserConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSubaccountK8sClusterUserConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not DaraCore.is_null(request.temporary_duration_minutes):
            query['TemporaryDurationMinutes'] = request.temporary_duration_minutes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSubaccountK8sClusterUserConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/k8s/{DaraURL.percent_encode(cluster_id)}/users/{DaraURL.percent_encode(uid)}/user_config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSubaccountK8sClusterUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_subaccount_k8s_cluster_user_config(
        self,
        cluster_id: str,
        uid: str,
        request: main_models.DescribeSubaccountK8sClusterUserConfigRequest,
    ) -> main_models.DescribeSubaccountK8sClusterUserConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_subaccount_k8s_cluster_user_config_with_options(cluster_id, uid, request, headers, runtime)

    async def describe_subaccount_k8s_cluster_user_config_async(
        self,
        cluster_id: str,
        uid: str,
        request: main_models.DescribeSubaccountK8sClusterUserConfigRequest,
    ) -> main_models.DescribeSubaccountK8sClusterUserConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_subaccount_k8s_cluster_user_config_with_options_async(cluster_id, uid, request, headers, runtime)

    def describe_task_info_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTaskInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeTaskInfo',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_task_info_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTaskInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeTaskInfo',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_task_info(
        self,
        task_id: str,
    ) -> main_models.DescribeTaskInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_task_info_with_options(task_id, headers, runtime)

    async def describe_task_info_async(
        self,
        task_id: str,
    ) -> main_models.DescribeTaskInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_task_info_with_options_async(task_id, headers, runtime)

    def describe_template_attribute_with_options(
        self,
        template_id: str,
        request: main_models.DescribeTemplateAttributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplateAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_type):
            query['template_type'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplateAttribute',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/templates/{DaraURL.percent_encode(template_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplateAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_template_attribute_with_options_async(
        self,
        template_id: str,
        request: main_models.DescribeTemplateAttributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplateAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_type):
            query['template_type'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplateAttribute',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/templates/{DaraURL.percent_encode(template_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplateAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_template_attribute(
        self,
        template_id: str,
        request: main_models.DescribeTemplateAttributeRequest,
    ) -> main_models.DescribeTemplateAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_template_attribute_with_options(template_id, request, headers, runtime)

    async def describe_template_attribute_async(
        self,
        template_id: str,
        request: main_models.DescribeTemplateAttributeRequest,
    ) -> main_models.DescribeTemplateAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_template_attribute_with_options_async(template_id, request, headers, runtime)

    def describe_templates_with_options(
        self,
        request: main_models.DescribeTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['page_num'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.template_type):
            query['template_type'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplates',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_templates_with_options_async(
        self,
        request: main_models.DescribeTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['page_num'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.template_type):
            query['template_type'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplates',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_templates(
        self,
        request: main_models.DescribeTemplatesRequest,
    ) -> main_models.DescribeTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_templates_with_options(request, headers, runtime)

    async def describe_templates_async(
        self,
        request: main_models.DescribeTemplatesRequest,
    ) -> main_models.DescribeTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_templates_with_options_async(request, headers, runtime)

    def describe_trigger_with_options(
        self,
        cluster_id: str,
        request: main_models.DescribeTriggerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.action):
            query['action'] = request.action
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrigger',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/triggers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_trigger_with_options_async(
        self,
        cluster_id: str,
        request: main_models.DescribeTriggerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.action):
            query['action'] = request.action
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTrigger',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/triggers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_trigger(
        self,
        cluster_id: str,
        request: main_models.DescribeTriggerRequest,
    ) -> main_models.DescribeTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_trigger_with_options(cluster_id, request, headers, runtime)

    async def describe_trigger_async(
        self,
        cluster_id: str,
        request: main_models.DescribeTriggerRequest,
    ) -> main_models.DescribeTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_trigger_with_options_async(cluster_id, request, headers, runtime)

    def describe_user_cluster_namespaces_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserClusterNamespacesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserClusterNamespaces',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/k8s/{DaraURL.percent_encode(cluster_id)}/namespaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeUserClusterNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_cluster_namespaces_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserClusterNamespacesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserClusterNamespaces',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/k8s/{DaraURL.percent_encode(cluster_id)}/namespaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeUserClusterNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_cluster_namespaces(
        self,
        cluster_id: str,
    ) -> main_models.DescribeUserClusterNamespacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_user_cluster_namespaces_with_options(cluster_id, headers, runtime)

    async def describe_user_cluster_namespaces_async(
        self,
        cluster_id: str,
    ) -> main_models.DescribeUserClusterNamespacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_user_cluster_namespaces_with_options_async(cluster_id, headers, runtime)

    def describe_user_permission_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserPermissionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserPermission',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/permissions/users/{DaraURL.percent_encode(uid)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeUserPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_permission_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserPermissionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserPermission',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/permissions/users/{DaraURL.percent_encode(uid)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.DescribeUserPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_permission(
        self,
        uid: str,
    ) -> main_models.DescribeUserPermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_user_permission_with_options(uid, headers, runtime)

    async def describe_user_permission_async(
        self,
        uid: str,
    ) -> main_models.DescribeUserPermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_user_permission_with_options_async(uid, headers, runtime)

    def describe_user_quota_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserQuotaResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserQuota',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/quota',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_quota_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserQuotaResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserQuota',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/quota',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_quota(self) -> main_models.DescribeUserQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_user_quota_with_options(headers, runtime)

    async def describe_user_quota_async(self) -> main_models.DescribeUserQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_user_quota_with_options_async(headers, runtime)

    def fix_node_pool_vuls_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.FixNodePoolVulsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FixNodePoolVulsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_restart):
            body['auto_restart'] = request.auto_restart
        if not DaraCore.is_null(request.nodes):
            body['nodes'] = request.nodes
        if not DaraCore.is_null(request.rollout_policy):
            body['rollout_policy'] = request.rollout_policy
        if not DaraCore.is_null(request.vuls):
            body['vuls'] = request.vuls
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FixNodePoolVuls',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}/vuls/fix',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FixNodePoolVulsResponse(),
            self.call_api(params, req, runtime)
        )

    async def fix_node_pool_vuls_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.FixNodePoolVulsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FixNodePoolVulsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_restart):
            body['auto_restart'] = request.auto_restart
        if not DaraCore.is_null(request.nodes):
            body['nodes'] = request.nodes
        if not DaraCore.is_null(request.rollout_policy):
            body['rollout_policy'] = request.rollout_policy
        if not DaraCore.is_null(request.vuls):
            body['vuls'] = request.vuls
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FixNodePoolVuls',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}/vuls/fix',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FixNodePoolVulsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fix_node_pool_vuls(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.FixNodePoolVulsRequest,
    ) -> main_models.FixNodePoolVulsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.fix_node_pool_vuls_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def fix_node_pool_vuls_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.FixNodePoolVulsRequest,
    ) -> main_models.FixNodePoolVulsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.fix_node_pool_vuls_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def get_cluster_addon_instance_with_options(
        self,
        cluster_id: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterAddonInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetClusterAddonInstance',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/addon_instances/{DaraURL.percent_encode(instance_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterAddonInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_addon_instance_with_options_async(
        self,
        cluster_id: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterAddonInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetClusterAddonInstance',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/addon_instances/{DaraURL.percent_encode(instance_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterAddonInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_addon_instance(
        self,
        cluster_id: str,
        instance_name: str,
    ) -> main_models.GetClusterAddonInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_cluster_addon_instance_with_options(cluster_id, instance_name, headers, runtime)

    async def get_cluster_addon_instance_async(
        self,
        cluster_id: str,
        instance_name: str,
    ) -> main_models.GetClusterAddonInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_cluster_addon_instance_with_options_async(cluster_id, instance_name, headers, runtime)

    def get_cluster_audit_project_with_options(
        self,
        clusterid: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterAuditProjectResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetClusterAuditProject',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(clusterid)}/audit',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterAuditProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_audit_project_with_options_async(
        self,
        clusterid: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterAuditProjectResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetClusterAuditProject',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(clusterid)}/audit',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterAuditProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_audit_project(
        self,
        clusterid: str,
    ) -> main_models.GetClusterAuditProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_cluster_audit_project_with_options(clusterid, headers, runtime)

    async def get_cluster_audit_project_async(
        self,
        clusterid: str,
    ) -> main_models.GetClusterAuditProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_cluster_audit_project_with_options_async(clusterid, headers, runtime)

    def get_cluster_check_with_options(
        self,
        cluster_id: str,
        check_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterCheckResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetClusterCheck',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/checks/{DaraURL.percent_encode(check_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_check_with_options_async(
        self,
        cluster_id: str,
        check_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterCheckResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetClusterCheck',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/checks/{DaraURL.percent_encode(check_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_check(
        self,
        cluster_id: str,
        check_id: str,
    ) -> main_models.GetClusterCheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_cluster_check_with_options(cluster_id, check_id, headers, runtime)

    async def get_cluster_check_async(
        self,
        cluster_id: str,
        check_id: str,
    ) -> main_models.GetClusterCheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_cluster_check_with_options_async(cluster_id, check_id, headers, runtime)

    def get_cluster_diagnosis_check_items_with_options(
        self,
        cluster_id: str,
        diagnosis_id: str,
        request: main_models.GetClusterDiagnosisCheckItemsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterDiagnosisCheckItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClusterDiagnosisCheckItems',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/diagnosis/{DaraURL.percent_encode(diagnosis_id)}/check_items',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterDiagnosisCheckItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_diagnosis_check_items_with_options_async(
        self,
        cluster_id: str,
        diagnosis_id: str,
        request: main_models.GetClusterDiagnosisCheckItemsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterDiagnosisCheckItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClusterDiagnosisCheckItems',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/diagnosis/{DaraURL.percent_encode(diagnosis_id)}/check_items',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterDiagnosisCheckItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_diagnosis_check_items(
        self,
        cluster_id: str,
        diagnosis_id: str,
        request: main_models.GetClusterDiagnosisCheckItemsRequest,
    ) -> main_models.GetClusterDiagnosisCheckItemsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_cluster_diagnosis_check_items_with_options(cluster_id, diagnosis_id, request, headers, runtime)

    async def get_cluster_diagnosis_check_items_async(
        self,
        cluster_id: str,
        diagnosis_id: str,
        request: main_models.GetClusterDiagnosisCheckItemsRequest,
    ) -> main_models.GetClusterDiagnosisCheckItemsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_cluster_diagnosis_check_items_with_options_async(cluster_id, diagnosis_id, request, headers, runtime)

    def get_cluster_diagnosis_result_with_options(
        self,
        cluster_id: str,
        diagnosis_id: str,
        request: main_models.GetClusterDiagnosisResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterDiagnosisResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClusterDiagnosisResult',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/diagnosis/{DaraURL.percent_encode(diagnosis_id)}/result',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterDiagnosisResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_diagnosis_result_with_options_async(
        self,
        cluster_id: str,
        diagnosis_id: str,
        request: main_models.GetClusterDiagnosisResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterDiagnosisResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClusterDiagnosisResult',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/diagnosis/{DaraURL.percent_encode(diagnosis_id)}/result',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterDiagnosisResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_diagnosis_result(
        self,
        cluster_id: str,
        diagnosis_id: str,
        request: main_models.GetClusterDiagnosisResultRequest,
    ) -> main_models.GetClusterDiagnosisResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_cluster_diagnosis_result_with_options(cluster_id, diagnosis_id, request, headers, runtime)

    async def get_cluster_diagnosis_result_async(
        self,
        cluster_id: str,
        diagnosis_id: str,
        request: main_models.GetClusterDiagnosisResultRequest,
    ) -> main_models.GetClusterDiagnosisResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_cluster_diagnosis_result_with_options_async(cluster_id, diagnosis_id, request, headers, runtime)

    def get_cluster_inspect_config_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterInspectConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetClusterInspectConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/inspectConfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterInspectConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_inspect_config_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterInspectConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetClusterInspectConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/inspectConfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterInspectConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_inspect_config(
        self,
        cluster_id: str,
    ) -> main_models.GetClusterInspectConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_cluster_inspect_config_with_options(cluster_id, headers, runtime)

    async def get_cluster_inspect_config_async(
        self,
        cluster_id: str,
    ) -> main_models.GetClusterInspectConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_cluster_inspect_config_with_options_async(cluster_id, headers, runtime)

    def get_cluster_inspect_report_detail_with_options(
        self,
        cluster_id: str,
        report_id: str,
        request: main_models.GetClusterInspectReportDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterInspectReportDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['category'] = request.category
        if not DaraCore.is_null(request.enable_filter):
            query['enableFilter'] = request.enable_filter
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        if not DaraCore.is_null(request.level):
            query['level'] = request.level
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.target_type):
            query['targetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClusterInspectReportDetail',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/inspectReports/{DaraURL.percent_encode(report_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterInspectReportDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_inspect_report_detail_with_options_async(
        self,
        cluster_id: str,
        report_id: str,
        request: main_models.GetClusterInspectReportDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterInspectReportDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['category'] = request.category
        if not DaraCore.is_null(request.enable_filter):
            query['enableFilter'] = request.enable_filter
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        if not DaraCore.is_null(request.level):
            query['level'] = request.level
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.target_type):
            query['targetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClusterInspectReportDetail',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/inspectReports/{DaraURL.percent_encode(report_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterInspectReportDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_inspect_report_detail(
        self,
        cluster_id: str,
        report_id: str,
        request: main_models.GetClusterInspectReportDetailRequest,
    ) -> main_models.GetClusterInspectReportDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_cluster_inspect_report_detail_with_options(cluster_id, report_id, request, headers, runtime)

    async def get_cluster_inspect_report_detail_async(
        self,
        cluster_id: str,
        report_id: str,
        request: main_models.GetClusterInspectReportDetailRequest,
    ) -> main_models.GetClusterInspectReportDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_cluster_inspect_report_detail_with_options_async(cluster_id, report_id, request, headers, runtime)

    def get_kubernetes_trigger_with_options(
        self,
        cluster_id: str,
        request: main_models.GetKubernetesTriggerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKubernetesTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.action):
            query['action'] = request.action
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKubernetesTrigger',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/triggers/{DaraURL.percent_encode(cluster_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.GetKubernetesTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_kubernetes_trigger_with_options_async(
        self,
        cluster_id: str,
        request: main_models.GetKubernetesTriggerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetKubernetesTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.action):
            query['action'] = request.action
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKubernetesTrigger',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/triggers/{DaraURL.percent_encode(cluster_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.GetKubernetesTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_kubernetes_trigger(
        self,
        cluster_id: str,
        request: main_models.GetKubernetesTriggerRequest,
    ) -> main_models.GetKubernetesTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_kubernetes_trigger_with_options(cluster_id, request, headers, runtime)

    async def get_kubernetes_trigger_async(
        self,
        cluster_id: str,
        request: main_models.GetKubernetesTriggerRequest,
    ) -> main_models.GetKubernetesTriggerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_kubernetes_trigger_with_options_async(cluster_id, request, headers, runtime)

    def get_upgrade_status_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUpgradeStatusResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetUpgradeStatus',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/clusters/{DaraURL.percent_encode(cluster_id)}/upgrade/status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUpgradeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upgrade_status_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUpgradeStatusResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetUpgradeStatus',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/clusters/{DaraURL.percent_encode(cluster_id)}/upgrade/status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUpgradeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upgrade_status(
        self,
        cluster_id: str,
    ) -> main_models.GetUpgradeStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_upgrade_status_with_options(cluster_id, headers, runtime)

    async def get_upgrade_status_async(
        self,
        cluster_id: str,
    ) -> main_models.GetUpgradeStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_upgrade_status_with_options_async(cluster_id, headers, runtime)

    def grant_permissions_with_options(
        self,
        uid: str,
        request: main_models.GrantPermissionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GrantPermissionsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'GrantPermissions',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/permissions/users/{DaraURL.percent_encode(uid)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.GrantPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_permissions_with_options_async(
        self,
        uid: str,
        request: main_models.GrantPermissionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GrantPermissionsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'GrantPermissions',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/permissions/users/{DaraURL.percent_encode(uid)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.GrantPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_permissions(
        self,
        uid: str,
        request: main_models.GrantPermissionsRequest,
    ) -> main_models.GrantPermissionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.grant_permissions_with_options(uid, request, headers, runtime)

    async def grant_permissions_async(
        self,
        uid: str,
        request: main_models.GrantPermissionsRequest,
    ) -> main_models.GrantPermissionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.grant_permissions_with_options_async(uid, request, headers, runtime)

    def install_cluster_addons_with_options(
        self,
        cluster_id: str,
        request: main_models.InstallClusterAddonsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallClusterAddonsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'InstallClusterAddons',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/install',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallClusterAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_cluster_addons_with_options_async(
        self,
        cluster_id: str,
        request: main_models.InstallClusterAddonsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallClusterAddonsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'InstallClusterAddons',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/install',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallClusterAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_cluster_addons(
        self,
        cluster_id: str,
        request: main_models.InstallClusterAddonsRequest,
    ) -> main_models.InstallClusterAddonsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.install_cluster_addons_with_options(cluster_id, request, headers, runtime)

    async def install_cluster_addons_async(
        self,
        cluster_id: str,
        request: main_models.InstallClusterAddonsRequest,
    ) -> main_models.InstallClusterAddonsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.install_cluster_addons_with_options_async(cluster_id, request, headers, runtime)

    def install_node_pool_components_with_options(
        self,
        cluster_id: str,
        node_pool_id: str,
        request: main_models.InstallNodePoolComponentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallNodePoolComponentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.components):
            body['components'] = request.components
        if not DaraCore.is_null(request.node_names):
            body['nodeNames'] = request.node_names
        if not DaraCore.is_null(request.rolling_policy):
            body['rollingPolicy'] = request.rolling_policy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallNodePoolComponents',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(node_pool_id)}/components',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallNodePoolComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_node_pool_components_with_options_async(
        self,
        cluster_id: str,
        node_pool_id: str,
        request: main_models.InstallNodePoolComponentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallNodePoolComponentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.components):
            body['components'] = request.components
        if not DaraCore.is_null(request.node_names):
            body['nodeNames'] = request.node_names
        if not DaraCore.is_null(request.rolling_policy):
            body['rollingPolicy'] = request.rolling_policy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallNodePoolComponents',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(node_pool_id)}/components',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallNodePoolComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_node_pool_components(
        self,
        cluster_id: str,
        node_pool_id: str,
        request: main_models.InstallNodePoolComponentsRequest,
    ) -> main_models.InstallNodePoolComponentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.install_node_pool_components_with_options(cluster_id, node_pool_id, request, headers, runtime)

    async def install_node_pool_components_async(
        self,
        cluster_id: str,
        node_pool_id: str,
        request: main_models.InstallNodePoolComponentsRequest,
    ) -> main_models.InstallNodePoolComponentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.install_node_pool_components_with_options_async(cluster_id, node_pool_id, request, headers, runtime)

    def list_addons_with_options(
        self,
        request: main_models.ListAddonsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAddonsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not DaraCore.is_null(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not DaraCore.is_null(request.cluster_version):
            query['cluster_version'] = request.cluster_version
        if not DaraCore.is_null(request.profile):
            query['profile'] = request.profile
        if not DaraCore.is_null(request.region_id):
            query['region_id'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddons',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/addons',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addons_with_options_async(
        self,
        request: main_models.ListAddonsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAddonsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not DaraCore.is_null(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not DaraCore.is_null(request.cluster_version):
            query['cluster_version'] = request.cluster_version
        if not DaraCore.is_null(request.profile):
            query['profile'] = request.profile
        if not DaraCore.is_null(request.region_id):
            query['region_id'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddons',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/addons',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_addons(
        self,
        request: main_models.ListAddonsRequest,
    ) -> main_models.ListAddonsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_addons_with_options(request, headers, runtime)

    async def list_addons_async(
        self,
        request: main_models.ListAddonsRequest,
    ) -> main_models.ListAddonsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_addons_with_options_async(request, headers, runtime)

    def list_cluster_addon_instance_resources_with_options(
        self,
        cluster_id: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterAddonInstanceResourcesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListClusterAddonInstanceResources',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/addon_instances/{DaraURL.percent_encode(instance_name)}/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterAddonInstanceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_addon_instance_resources_with_options_async(
        self,
        cluster_id: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterAddonInstanceResourcesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListClusterAddonInstanceResources',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/addon_instances/{DaraURL.percent_encode(instance_name)}/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterAddonInstanceResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_addon_instance_resources(
        self,
        cluster_id: str,
        instance_name: str,
    ) -> main_models.ListClusterAddonInstanceResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_cluster_addon_instance_resources_with_options(cluster_id, instance_name, headers, runtime)

    async def list_cluster_addon_instance_resources_async(
        self,
        cluster_id: str,
        instance_name: str,
    ) -> main_models.ListClusterAddonInstanceResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_cluster_addon_instance_resources_with_options_async(cluster_id, instance_name, headers, runtime)

    def list_cluster_addon_instances_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterAddonInstancesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListClusterAddonInstances',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/addon_instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterAddonInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_addon_instances_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterAddonInstancesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListClusterAddonInstances',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/addon_instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterAddonInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_addon_instances(
        self,
        cluster_id: str,
    ) -> main_models.ListClusterAddonInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_cluster_addon_instances_with_options(cluster_id, headers, runtime)

    async def list_cluster_addon_instances_async(
        self,
        cluster_id: str,
    ) -> main_models.ListClusterAddonInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_cluster_addon_instances_with_options_async(cluster_id, headers, runtime)

    def list_cluster_checks_with_options(
        self,
        cluster_id: str,
        request: main_models.ListClusterChecksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterChecksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.target):
            query['target'] = request.target
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterChecks',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/checks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterChecksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_checks_with_options_async(
        self,
        cluster_id: str,
        request: main_models.ListClusterChecksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterChecksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.target):
            query['target'] = request.target
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterChecks',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/checks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterChecksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_checks(
        self,
        cluster_id: str,
        request: main_models.ListClusterChecksRequest,
    ) -> main_models.ListClusterChecksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_cluster_checks_with_options(cluster_id, request, headers, runtime)

    async def list_cluster_checks_async(
        self,
        cluster_id: str,
        request: main_models.ListClusterChecksRequest,
    ) -> main_models.ListClusterChecksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_cluster_checks_with_options_async(cluster_id, request, headers, runtime)

    def list_cluster_inspect_reports_with_options(
        self,
        cluster_id: str,
        request: main_models.ListClusterInspectReportsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterInspectReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterInspectReports',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/inspectReports',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterInspectReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_inspect_reports_with_options_async(
        self,
        cluster_id: str,
        request: main_models.ListClusterInspectReportsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterInspectReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterInspectReports',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/inspectReports',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterInspectReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_inspect_reports(
        self,
        cluster_id: str,
        request: main_models.ListClusterInspectReportsRequest,
    ) -> main_models.ListClusterInspectReportsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_cluster_inspect_reports_with_options(cluster_id, request, headers, runtime)

    async def list_cluster_inspect_reports_async(
        self,
        cluster_id: str,
        request: main_models.ListClusterInspectReportsRequest,
    ) -> main_models.ListClusterInspectReportsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_cluster_inspect_reports_with_options_async(cluster_id, request, headers, runtime)

    def list_cluster_kubeconfig_states_with_options(
        self,
        cluster_id: str,
        request: main_models.ListClusterKubeconfigStatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterKubeconfigStatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterKubeconfigStates',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/kubeconfig/states',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterKubeconfigStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_kubeconfig_states_with_options_async(
        self,
        cluster_id: str,
        request: main_models.ListClusterKubeconfigStatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterKubeconfigStatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterKubeconfigStates',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/kubeconfig/states',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterKubeconfigStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_kubeconfig_states(
        self,
        cluster_id: str,
        request: main_models.ListClusterKubeconfigStatesRequest,
    ) -> main_models.ListClusterKubeconfigStatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_cluster_kubeconfig_states_with_options(cluster_id, request, headers, runtime)

    async def list_cluster_kubeconfig_states_async(
        self,
        cluster_id: str,
        request: main_models.ListClusterKubeconfigStatesRequest,
    ) -> main_models.ListClusterKubeconfigStatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_cluster_kubeconfig_states_with_options_async(cluster_id, request, headers, runtime)

    def list_operation_plans_with_options(
        self,
        request: main_models.ListOperationPlansRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationPlans',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/operation/plans',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_operation_plans_with_options_async(
        self,
        request: main_models.ListOperationPlansRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationPlans',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/operation/plans',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_operation_plans(
        self,
        request: main_models.ListOperationPlansRequest,
    ) -> main_models.ListOperationPlansResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_operation_plans_with_options(request, headers, runtime)

    async def list_operation_plans_async(
        self,
        request: main_models.ListOperationPlansRequest,
    ) -> main_models.ListOperationPlansResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_operation_plans_with_options_async(request, headers, runtime)

    def list_operation_plans_for_region_with_options(
        self,
        region_id: str,
        request: main_models.ListOperationPlansForRegionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationPlansForRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.state):
            query['state'] = request.state
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationPlansForRegion',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/regions/{DaraURL.percent_encode(region_id)}/operation/plans',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationPlansForRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_operation_plans_for_region_with_options_async(
        self,
        region_id: str,
        request: main_models.ListOperationPlansForRegionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOperationPlansForRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not DaraCore.is_null(request.state):
            query['state'] = request.state
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOperationPlansForRegion',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/regions/{DaraURL.percent_encode(region_id)}/operation/plans',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOperationPlansForRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_operation_plans_for_region(
        self,
        region_id: str,
        request: main_models.ListOperationPlansForRegionRequest,
    ) -> main_models.ListOperationPlansForRegionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_operation_plans_for_region_with_options(region_id, request, headers, runtime)

    async def list_operation_plans_for_region_async(
        self,
        region_id: str,
        request: main_models.ListOperationPlansForRegionRequest,
    ) -> main_models.ListOperationPlansForRegionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_operation_plans_for_region_with_options_async(region_id, request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'resource_ids', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['next_token'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['region_id'] = request.region_id
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['resource_ids'] = request.resource_ids_shrink
        if not DaraCore.is_null(request.resource_type):
            query['resource_type'] = request.resource_type
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/tags',
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
        tmp_req: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'resource_ids', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['next_token'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['region_id'] = request.region_id
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['resource_ids'] = request.resource_ids_shrink
        if not DaraCore.is_null(request.resource_type):
            query['resource_type'] = request.resource_type
        if not DaraCore.is_null(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/tags',
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

    def list_user_kube_config_states_with_options(
        self,
        uid: str,
        request: main_models.ListUserKubeConfigStatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserKubeConfigStatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserKubeConfigStates',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/users/{DaraURL.percent_encode(uid)}/kubeconfig/states',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserKubeConfigStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_kube_config_states_with_options_async(
        self,
        uid: str,
        request: main_models.ListUserKubeConfigStatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserKubeConfigStatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserKubeConfigStates',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/users/{DaraURL.percent_encode(uid)}/kubeconfig/states',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserKubeConfigStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_kube_config_states(
        self,
        uid: str,
        request: main_models.ListUserKubeConfigStatesRequest,
    ) -> main_models.ListUserKubeConfigStatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_user_kube_config_states_with_options(uid, request, headers, runtime)

    async def list_user_kube_config_states_async(
        self,
        uid: str,
        request: main_models.ListUserKubeConfigStatesRequest,
    ) -> main_models.ListUserKubeConfigStatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_user_kube_config_states_with_options_async(uid, request, headers, runtime)

    def migrate_cluster_with_options(
        self,
        cluster_id: str,
        request: main_models.MigrateClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MigrateClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.oss_bucket_endpoint):
            body['oss_bucket_endpoint'] = request.oss_bucket_endpoint
        if not DaraCore.is_null(request.oss_bucket_name):
            body['oss_bucket_name'] = request.oss_bucket_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MigrateCluster',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/migrate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_cluster_with_options_async(
        self,
        cluster_id: str,
        request: main_models.MigrateClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MigrateClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.oss_bucket_endpoint):
            body['oss_bucket_endpoint'] = request.oss_bucket_endpoint
        if not DaraCore.is_null(request.oss_bucket_name):
            body['oss_bucket_name'] = request.oss_bucket_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MigrateCluster',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/migrate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_cluster(
        self,
        cluster_id: str,
        request: main_models.MigrateClusterRequest,
    ) -> main_models.MigrateClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.migrate_cluster_with_options(cluster_id, request, headers, runtime)

    async def migrate_cluster_async(
        self,
        cluster_id: str,
        request: main_models.MigrateClusterRequest,
    ) -> main_models.MigrateClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.migrate_cluster_with_options_async(cluster_id, request, headers, runtime)

    def modify_cluster_with_options(
        self,
        cluster_id: str,
        request: main_models.ModifyClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_control_list):
            body['access_control_list'] = request.access_control_list
        if not DaraCore.is_null(request.api_server_custom_cert_sans):
            body['api_server_custom_cert_sans'] = request.api_server_custom_cert_sans
        if not DaraCore.is_null(request.api_server_eip):
            body['api_server_eip'] = request.api_server_eip
        if not DaraCore.is_null(request.api_server_eip_id):
            body['api_server_eip_id'] = request.api_server_eip_id
        if not DaraCore.is_null(request.cluster_name):
            body['cluster_name'] = request.cluster_name
        if not DaraCore.is_null(request.control_plane_config):
            body['control_plane_config'] = request.control_plane_config
        if not DaraCore.is_null(request.deletion_protection):
            body['deletion_protection'] = request.deletion_protection
        if not DaraCore.is_null(request.enable_rrsa):
            body['enable_rrsa'] = request.enable_rrsa
        if not DaraCore.is_null(request.ingress_domain_rebinding):
            body['ingress_domain_rebinding'] = request.ingress_domain_rebinding
        if not DaraCore.is_null(request.ingress_loadbalancer_id):
            body['ingress_loadbalancer_id'] = request.ingress_loadbalancer_id
        if not DaraCore.is_null(request.instance_deletion_protection):
            body['instance_deletion_protection'] = request.instance_deletion_protection
        if not DaraCore.is_null(request.maintenance_window):
            body['maintenance_window'] = request.maintenance_window
        if not DaraCore.is_null(request.operation_policy):
            body['operation_policy'] = request.operation_policy
        if not DaraCore.is_null(request.resource_group_id):
            body['resource_group_id'] = request.resource_group_id
        if not DaraCore.is_null(request.security_group_id):
            body['security_group_id'] = request.security_group_id
        if not DaraCore.is_null(request.system_events_logging):
            body['system_events_logging'] = request.system_events_logging
        if not DaraCore.is_null(request.timezone):
            body['timezone'] = request.timezone
        if not DaraCore.is_null(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCluster',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/clusters/{DaraURL.percent_encode(cluster_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_with_options_async(
        self,
        cluster_id: str,
        request: main_models.ModifyClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_control_list):
            body['access_control_list'] = request.access_control_list
        if not DaraCore.is_null(request.api_server_custom_cert_sans):
            body['api_server_custom_cert_sans'] = request.api_server_custom_cert_sans
        if not DaraCore.is_null(request.api_server_eip):
            body['api_server_eip'] = request.api_server_eip
        if not DaraCore.is_null(request.api_server_eip_id):
            body['api_server_eip_id'] = request.api_server_eip_id
        if not DaraCore.is_null(request.cluster_name):
            body['cluster_name'] = request.cluster_name
        if not DaraCore.is_null(request.control_plane_config):
            body['control_plane_config'] = request.control_plane_config
        if not DaraCore.is_null(request.deletion_protection):
            body['deletion_protection'] = request.deletion_protection
        if not DaraCore.is_null(request.enable_rrsa):
            body['enable_rrsa'] = request.enable_rrsa
        if not DaraCore.is_null(request.ingress_domain_rebinding):
            body['ingress_domain_rebinding'] = request.ingress_domain_rebinding
        if not DaraCore.is_null(request.ingress_loadbalancer_id):
            body['ingress_loadbalancer_id'] = request.ingress_loadbalancer_id
        if not DaraCore.is_null(request.instance_deletion_protection):
            body['instance_deletion_protection'] = request.instance_deletion_protection
        if not DaraCore.is_null(request.maintenance_window):
            body['maintenance_window'] = request.maintenance_window
        if not DaraCore.is_null(request.operation_policy):
            body['operation_policy'] = request.operation_policy
        if not DaraCore.is_null(request.resource_group_id):
            body['resource_group_id'] = request.resource_group_id
        if not DaraCore.is_null(request.security_group_id):
            body['security_group_id'] = request.security_group_id
        if not DaraCore.is_null(request.system_events_logging):
            body['system_events_logging'] = request.system_events_logging
        if not DaraCore.is_null(request.timezone):
            body['timezone'] = request.timezone
        if not DaraCore.is_null(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCluster',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/clusters/{DaraURL.percent_encode(cluster_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster(
        self,
        cluster_id: str,
        request: main_models.ModifyClusterRequest,
    ) -> main_models.ModifyClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_cluster_with_options(cluster_id, request, headers, runtime)

    async def modify_cluster_async(
        self,
        cluster_id: str,
        request: main_models.ModifyClusterRequest,
    ) -> main_models.ModifyClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_cluster_with_options_async(cluster_id, request, headers, runtime)

    def modify_cluster_addon_with_options(
        self,
        cluster_id: str,
        component_id: str,
        request: main_models.ModifyClusterAddonRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClusterAddonResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClusterAddon',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/{DaraURL.percent_encode(component_id)}/config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.ModifyClusterAddonResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_addon_with_options_async(
        self,
        cluster_id: str,
        component_id: str,
        request: main_models.ModifyClusterAddonRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClusterAddonResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClusterAddon',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/{DaraURL.percent_encode(component_id)}/config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.ModifyClusterAddonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_addon(
        self,
        cluster_id: str,
        component_id: str,
        request: main_models.ModifyClusterAddonRequest,
    ) -> main_models.ModifyClusterAddonResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_cluster_addon_with_options(cluster_id, component_id, request, headers, runtime)

    async def modify_cluster_addon_async(
        self,
        cluster_id: str,
        component_id: str,
        request: main_models.ModifyClusterAddonRequest,
    ) -> main_models.ModifyClusterAddonResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_cluster_addon_with_options_async(cluster_id, component_id, request, headers, runtime)

    def modify_cluster_node_pool_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.ModifyClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClusterNodePoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_scaling):
            body['auto_scaling'] = request.auto_scaling
        if not DaraCore.is_null(request.concurrency):
            body['concurrency'] = request.concurrency
        if not DaraCore.is_null(request.kubernetes_config):
            body['kubernetes_config'] = request.kubernetes_config
        if not DaraCore.is_null(request.management):
            body['management'] = request.management
        if not DaraCore.is_null(request.nodepool_info):
            body['nodepool_info'] = request.nodepool_info
        if not DaraCore.is_null(request.scaling_group):
            body['scaling_group'] = request.scaling_group
        if not DaraCore.is_null(request.tee_config):
            body['tee_config'] = request.tee_config
        if not DaraCore.is_null(request.update_nodes):
            body['update_nodes'] = request.update_nodes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClusterNodePool',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyClusterNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_node_pool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.ModifyClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClusterNodePoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_scaling):
            body['auto_scaling'] = request.auto_scaling
        if not DaraCore.is_null(request.concurrency):
            body['concurrency'] = request.concurrency
        if not DaraCore.is_null(request.kubernetes_config):
            body['kubernetes_config'] = request.kubernetes_config
        if not DaraCore.is_null(request.management):
            body['management'] = request.management
        if not DaraCore.is_null(request.nodepool_info):
            body['nodepool_info'] = request.nodepool_info
        if not DaraCore.is_null(request.scaling_group):
            body['scaling_group'] = request.scaling_group
        if not DaraCore.is_null(request.tee_config):
            body['tee_config'] = request.tee_config
        if not DaraCore.is_null(request.update_nodes):
            body['update_nodes'] = request.update_nodes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClusterNodePool',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyClusterNodePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_node_pool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.ModifyClusterNodePoolRequest,
    ) -> main_models.ModifyClusterNodePoolResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_cluster_node_pool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def modify_cluster_node_pool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.ModifyClusterNodePoolRequest,
    ) -> main_models.ModifyClusterNodePoolResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_cluster_node_pool_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def modify_cluster_tags_with_options(
        self,
        cluster_id: str,
        request: main_models.ModifyClusterTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClusterTagsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClusterTags',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.ModifyClusterTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_tags_with_options_async(
        self,
        cluster_id: str,
        request: main_models.ModifyClusterTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClusterTagsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClusterTags',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.ModifyClusterTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_tags(
        self,
        cluster_id: str,
        request: main_models.ModifyClusterTagsRequest,
    ) -> main_models.ModifyClusterTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_cluster_tags_with_options(cluster_id, request, headers, runtime)

    async def modify_cluster_tags_async(
        self,
        cluster_id: str,
        request: main_models.ModifyClusterTagsRequest,
    ) -> main_models.ModifyClusterTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_cluster_tags_with_options_async(cluster_id, request, headers, runtime)

    def modify_node_pool_node_config_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.ModifyNodePoolNodeConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNodePoolNodeConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.containerd_config):
            body['containerd_config'] = request.containerd_config
        if not DaraCore.is_null(request.kubelet_config):
            body['kubelet_config'] = request.kubelet_config
        if not DaraCore.is_null(request.os_config):
            body['os_config'] = request.os_config
        if not DaraCore.is_null(request.rolling_policy):
            body['rolling_policy'] = request.rolling_policy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNodePoolNodeConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}/node_config',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNodePoolNodeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_node_pool_node_config_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.ModifyNodePoolNodeConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNodePoolNodeConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.containerd_config):
            body['containerd_config'] = request.containerd_config
        if not DaraCore.is_null(request.kubelet_config):
            body['kubelet_config'] = request.kubelet_config
        if not DaraCore.is_null(request.os_config):
            body['os_config'] = request.os_config
        if not DaraCore.is_null(request.rolling_policy):
            body['rolling_policy'] = request.rolling_policy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNodePoolNodeConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}/node_config',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNodePoolNodeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_node_pool_node_config(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.ModifyNodePoolNodeConfigRequest,
    ) -> main_models.ModifyNodePoolNodeConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_node_pool_node_config_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def modify_node_pool_node_config_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.ModifyNodePoolNodeConfigRequest,
    ) -> main_models.ModifyNodePoolNodeConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_node_pool_node_config_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def modify_policy_instance_with_options(
        self,
        cluster_id: str,
        policy_name: str,
        request: main_models.ModifyPolicyInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPolicyInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.instance_name):
            body['instance_name'] = request.instance_name
        if not DaraCore.is_null(request.namespaces):
            body['namespaces'] = request.namespaces
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPolicyInstance',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/policies/{DaraURL.percent_encode(policy_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPolicyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_policy_instance_with_options_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: main_models.ModifyPolicyInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyPolicyInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.instance_name):
            body['instance_name'] = request.instance_name
        if not DaraCore.is_null(request.namespaces):
            body['namespaces'] = request.namespaces
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyPolicyInstance',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/policies/{DaraURL.percent_encode(policy_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyPolicyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_policy_instance(
        self,
        cluster_id: str,
        policy_name: str,
        request: main_models.ModifyPolicyInstanceRequest,
    ) -> main_models.ModifyPolicyInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_policy_instance_with_options(cluster_id, policy_name, request, headers, runtime)

    async def modify_policy_instance_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: main_models.ModifyPolicyInstanceRequest,
    ) -> main_models.ModifyPolicyInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_policy_instance_with_options_async(cluster_id, policy_name, request, headers, runtime)

    def open_ack_service_with_options(
        self,
        request: main_models.OpenAckServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenAckServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenAckService',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/service/open',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenAckServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_ack_service_with_options_async(
        self,
        request: main_models.OpenAckServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenAckServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenAckService',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/service/open',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenAckServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_ack_service(
        self,
        request: main_models.OpenAckServiceRequest,
    ) -> main_models.OpenAckServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.open_ack_service_with_options(request, headers, runtime)

    async def open_ack_service_async(
        self,
        request: main_models.OpenAckServiceRequest,
    ) -> main_models.OpenAckServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.open_ack_service_with_options_async(request, headers, runtime)

    def pause_cluster_upgrade_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PauseClusterUpgradeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'PauseClusterUpgrade',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/clusters/{DaraURL.percent_encode(cluster_id)}/upgrade/pause',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PauseClusterUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_cluster_upgrade_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PauseClusterUpgradeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'PauseClusterUpgrade',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/clusters/{DaraURL.percent_encode(cluster_id)}/upgrade/pause',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PauseClusterUpgradeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_cluster_upgrade(
        self,
        cluster_id: str,
    ) -> main_models.PauseClusterUpgradeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.pause_cluster_upgrade_with_options(cluster_id, headers, runtime)

    async def pause_cluster_upgrade_async(
        self,
        cluster_id: str,
    ) -> main_models.PauseClusterUpgradeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.pause_cluster_upgrade_with_options_async(cluster_id, headers, runtime)

    def pause_component_upgrade_with_options(
        self,
        clusterid: str,
        componentid: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PauseComponentUpgradeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'PauseComponentUpgrade',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(clusterid)}/components/{DaraURL.percent_encode(componentid)}/pause',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PauseComponentUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_component_upgrade_with_options_async(
        self,
        clusterid: str,
        componentid: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PauseComponentUpgradeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'PauseComponentUpgrade',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(clusterid)}/components/{DaraURL.percent_encode(componentid)}/pause',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PauseComponentUpgradeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_component_upgrade(
        self,
        clusterid: str,
        componentid: str,
    ) -> main_models.PauseComponentUpgradeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.pause_component_upgrade_with_options(clusterid, componentid, headers, runtime)

    async def pause_component_upgrade_async(
        self,
        clusterid: str,
        componentid: str,
    ) -> main_models.PauseComponentUpgradeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.pause_component_upgrade_with_options_async(clusterid, componentid, headers, runtime)

    def pause_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PauseTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'PauseTask',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}/pause',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PauseTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PauseTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'PauseTask',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}/pause',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PauseTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_task(
        self,
        task_id: str,
    ) -> main_models.PauseTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.pause_task_with_options(task_id, headers, runtime)

    async def pause_task_async(
        self,
        task_id: str,
    ) -> main_models.PauseTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.pause_task_with_options_async(task_id, headers, runtime)

    def remove_cluster_nodes_with_options(
        self,
        cluster_id: str,
        request: main_models.RemoveClusterNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveClusterNodesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drain_node):
            body['drain_node'] = request.drain_node
        if not DaraCore.is_null(request.nodes):
            body['nodes'] = request.nodes
        if not DaraCore.is_null(request.release_node):
            body['release_node'] = request.release_node
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveClusterNodes',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/clusters/{DaraURL.percent_encode(cluster_id)}/nodes/remove',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.RemoveClusterNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_cluster_nodes_with_options_async(
        self,
        cluster_id: str,
        request: main_models.RemoveClusterNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveClusterNodesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drain_node):
            body['drain_node'] = request.drain_node
        if not DaraCore.is_null(request.nodes):
            body['nodes'] = request.nodes
        if not DaraCore.is_null(request.release_node):
            body['release_node'] = request.release_node
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveClusterNodes',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/clusters/{DaraURL.percent_encode(cluster_id)}/nodes/remove',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.RemoveClusterNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_cluster_nodes(
        self,
        cluster_id: str,
        request: main_models.RemoveClusterNodesRequest,
    ) -> main_models.RemoveClusterNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_cluster_nodes_with_options(cluster_id, request, headers, runtime)

    async def remove_cluster_nodes_async(
        self,
        cluster_id: str,
        request: main_models.RemoveClusterNodesRequest,
    ) -> main_models.RemoveClusterNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_cluster_nodes_with_options_async(cluster_id, request, headers, runtime)

    def remove_node_pool_nodes_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        tmp_req: main_models.RemoveNodePoolNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveNodePoolNodesResponse:
        tmp_req.validate()
        request = main_models.RemoveNodePoolNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'instance_ids', 'json')
        if not DaraCore.is_null(tmp_req.nodes):
            request.nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.nodes, 'nodes', 'json')
        query = {}
        if not DaraCore.is_null(request.concurrency):
            query['concurrency'] = request.concurrency
        if not DaraCore.is_null(request.drain_node):
            query['drain_node'] = request.drain_node
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['instance_ids'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.nodes_shrink):
            query['nodes'] = request.nodes_shrink
        if not DaraCore.is_null(request.release_node):
            query['release_node'] = request.release_node
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveNodePoolNodes',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}/nodes',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveNodePoolNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_node_pool_nodes_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        tmp_req: main_models.RemoveNodePoolNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveNodePoolNodesResponse:
        tmp_req.validate()
        request = main_models.RemoveNodePoolNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'instance_ids', 'json')
        if not DaraCore.is_null(tmp_req.nodes):
            request.nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.nodes, 'nodes', 'json')
        query = {}
        if not DaraCore.is_null(request.concurrency):
            query['concurrency'] = request.concurrency
        if not DaraCore.is_null(request.drain_node):
            query['drain_node'] = request.drain_node
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['instance_ids'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.nodes_shrink):
            query['nodes'] = request.nodes_shrink
        if not DaraCore.is_null(request.release_node):
            query['release_node'] = request.release_node
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveNodePoolNodes',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}/nodes',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveNodePoolNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_node_pool_nodes(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.RemoveNodePoolNodesRequest,
    ) -> main_models.RemoveNodePoolNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_node_pool_nodes_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def remove_node_pool_nodes_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.RemoveNodePoolNodesRequest,
    ) -> main_models.RemoveNodePoolNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_node_pool_nodes_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def repair_cluster_node_pool_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.RepairClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RepairClusterNodePoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_restart):
            body['auto_restart'] = request.auto_restart
        if not DaraCore.is_null(request.nodes):
            body['nodes'] = request.nodes
        if not DaraCore.is_null(request.operations):
            body['operations'] = request.operations
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RepairClusterNodePool',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}/repair',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RepairClusterNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def repair_cluster_node_pool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.RepairClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RepairClusterNodePoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_restart):
            body['auto_restart'] = request.auto_restart
        if not DaraCore.is_null(request.nodes):
            body['nodes'] = request.nodes
        if not DaraCore.is_null(request.operations):
            body['operations'] = request.operations
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RepairClusterNodePool',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}/repair',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RepairClusterNodePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def repair_cluster_node_pool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.RepairClusterNodePoolRequest,
    ) -> main_models.RepairClusterNodePoolResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.repair_cluster_node_pool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def repair_cluster_node_pool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.RepairClusterNodePoolRequest,
    ) -> main_models.RepairClusterNodePoolResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.repair_cluster_node_pool_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def resume_component_upgrade_with_options(
        self,
        clusterid: str,
        componentid: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeComponentUpgradeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ResumeComponentUpgrade',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(clusterid)}/components/{DaraURL.percent_encode(componentid)}/resume',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.ResumeComponentUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_component_upgrade_with_options_async(
        self,
        clusterid: str,
        componentid: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeComponentUpgradeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ResumeComponentUpgrade',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(clusterid)}/components/{DaraURL.percent_encode(componentid)}/resume',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.ResumeComponentUpgradeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_component_upgrade(
        self,
        clusterid: str,
        componentid: str,
    ) -> main_models.ResumeComponentUpgradeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.resume_component_upgrade_with_options(clusterid, componentid, headers, runtime)

    async def resume_component_upgrade_async(
        self,
        clusterid: str,
        componentid: str,
    ) -> main_models.ResumeComponentUpgradeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.resume_component_upgrade_with_options_async(clusterid, componentid, headers, runtime)

    def resume_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ResumeTask',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}/resume',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.ResumeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ResumeTask',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}/resume',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.ResumeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_task(
        self,
        task_id: str,
    ) -> main_models.ResumeTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.resume_task_with_options(task_id, headers, runtime)

    async def resume_task_async(
        self,
        task_id: str,
    ) -> main_models.ResumeTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.resume_task_with_options_async(task_id, headers, runtime)

    def resume_upgrade_cluster_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeUpgradeClusterResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ResumeUpgradeCluster',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/clusters/{DaraURL.percent_encode(cluster_id)}/upgrade/resume',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.ResumeUpgradeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_upgrade_cluster_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeUpgradeClusterResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ResumeUpgradeCluster',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/clusters/{DaraURL.percent_encode(cluster_id)}/upgrade/resume',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.ResumeUpgradeClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_upgrade_cluster(
        self,
        cluster_id: str,
    ) -> main_models.ResumeUpgradeClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.resume_upgrade_cluster_with_options(cluster_id, headers, runtime)

    async def resume_upgrade_cluster_async(
        self,
        cluster_id: str,
    ) -> main_models.ResumeUpgradeClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.resume_upgrade_cluster_with_options_async(cluster_id, headers, runtime)

    def revoke_k8s_cluster_kube_config_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeK8sClusterKubeConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RevokeK8sClusterKubeConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/k8s/{DaraURL.percent_encode(cluster_id)}/certs',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeK8sClusterKubeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_k8s_cluster_kube_config_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeK8sClusterKubeConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RevokeK8sClusterKubeConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/k8s/{DaraURL.percent_encode(cluster_id)}/certs',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeK8sClusterKubeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_k8s_cluster_kube_config(
        self,
        cluster_id: str,
    ) -> main_models.RevokeK8sClusterKubeConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.revoke_k8s_cluster_kube_config_with_options(cluster_id, headers, runtime)

    async def revoke_k8s_cluster_kube_config_async(
        self,
        cluster_id: str,
    ) -> main_models.RevokeK8sClusterKubeConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.revoke_k8s_cluster_kube_config_with_options_async(cluster_id, headers, runtime)

    def run_cluster_check_with_options(
        self,
        cluster_id: str,
        request: main_models.RunClusterCheckRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunClusterCheckResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        if not DaraCore.is_null(request.target):
            body['target'] = request.target
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunClusterCheck',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/checks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunClusterCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_cluster_check_with_options_async(
        self,
        cluster_id: str,
        request: main_models.RunClusterCheckRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunClusterCheckResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        if not DaraCore.is_null(request.target):
            body['target'] = request.target
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunClusterCheck',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/checks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunClusterCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_cluster_check(
        self,
        cluster_id: str,
        request: main_models.RunClusterCheckRequest,
    ) -> main_models.RunClusterCheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_cluster_check_with_options(cluster_id, request, headers, runtime)

    async def run_cluster_check_async(
        self,
        cluster_id: str,
        request: main_models.RunClusterCheckRequest,
    ) -> main_models.RunClusterCheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_cluster_check_with_options_async(cluster_id, request, headers, runtime)

    def run_cluster_inspect_with_options(
        self,
        cluster_id: str,
        request: main_models.RunClusterInspectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunClusterInspectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunClusterInspect',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/inspectReports',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunClusterInspectResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_cluster_inspect_with_options_async(
        self,
        cluster_id: str,
        request: main_models.RunClusterInspectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunClusterInspectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunClusterInspect',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/inspectReports',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunClusterInspectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_cluster_inspect(
        self,
        cluster_id: str,
        request: main_models.RunClusterInspectRequest,
    ) -> main_models.RunClusterInspectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_cluster_inspect_with_options(cluster_id, request, headers, runtime)

    async def run_cluster_inspect_async(
        self,
        cluster_id: str,
        request: main_models.RunClusterInspectRequest,
    ) -> main_models.RunClusterInspectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_cluster_inspect_with_options_async(cluster_id, request, headers, runtime)

    def scale_cluster_node_pool_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.ScaleClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleClusterNodePoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.count):
            body['count'] = request.count
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ScaleClusterNodePool',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleClusterNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_cluster_node_pool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.ScaleClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleClusterNodePoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.count):
            body['count'] = request.count
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ScaleClusterNodePool',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleClusterNodePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_cluster_node_pool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.ScaleClusterNodePoolRequest,
    ) -> main_models.ScaleClusterNodePoolResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.scale_cluster_node_pool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def scale_cluster_node_pool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.ScaleClusterNodePoolRequest,
    ) -> main_models.ScaleClusterNodePoolResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.scale_cluster_node_pool_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def scale_out_cluster_with_options(
        self,
        cluster_id: str,
        request: main_models.ScaleOutClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleOutClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cloud_monitor_flags):
            body['cloud_monitor_flags'] = request.cloud_monitor_flags
        if not DaraCore.is_null(request.count):
            body['count'] = request.count
        if not DaraCore.is_null(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not DaraCore.is_null(request.image_id):
            body['image_id'] = request.image_id
        if not DaraCore.is_null(request.key_pair):
            body['key_pair'] = request.key_pair
        if not DaraCore.is_null(request.login_password):
            body['login_password'] = request.login_password
        if not DaraCore.is_null(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not DaraCore.is_null(request.runtime):
            body['runtime'] = request.runtime
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.taints):
            body['taints'] = request.taints
        if not DaraCore.is_null(request.user_data):
            body['user_data'] = request.user_data
        if not DaraCore.is_null(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        if not DaraCore.is_null(request.worker_auto_renew):
            body['worker_auto_renew'] = request.worker_auto_renew
        if not DaraCore.is_null(request.worker_auto_renew_period):
            body['worker_auto_renew_period'] = request.worker_auto_renew_period
        if not DaraCore.is_null(request.worker_data_disks):
            body['worker_data_disks'] = request.worker_data_disks
        if not DaraCore.is_null(request.worker_instance_charge_type):
            body['worker_instance_charge_type'] = request.worker_instance_charge_type
        if not DaraCore.is_null(request.worker_instance_types):
            body['worker_instance_types'] = request.worker_instance_types
        if not DaraCore.is_null(request.worker_period):
            body['worker_period'] = request.worker_period
        if not DaraCore.is_null(request.worker_period_unit):
            body['worker_period_unit'] = request.worker_period_unit
        if not DaraCore.is_null(request.worker_system_disk_category):
            body['worker_system_disk_category'] = request.worker_system_disk_category
        if not DaraCore.is_null(request.worker_system_disk_size):
            body['worker_system_disk_size'] = request.worker_system_disk_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ScaleOutCluster',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/clusters/{DaraURL.percent_encode(cluster_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleOutClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_out_cluster_with_options_async(
        self,
        cluster_id: str,
        request: main_models.ScaleOutClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleOutClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cloud_monitor_flags):
            body['cloud_monitor_flags'] = request.cloud_monitor_flags
        if not DaraCore.is_null(request.count):
            body['count'] = request.count
        if not DaraCore.is_null(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not DaraCore.is_null(request.image_id):
            body['image_id'] = request.image_id
        if not DaraCore.is_null(request.key_pair):
            body['key_pair'] = request.key_pair
        if not DaraCore.is_null(request.login_password):
            body['login_password'] = request.login_password
        if not DaraCore.is_null(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not DaraCore.is_null(request.runtime):
            body['runtime'] = request.runtime
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.taints):
            body['taints'] = request.taints
        if not DaraCore.is_null(request.user_data):
            body['user_data'] = request.user_data
        if not DaraCore.is_null(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        if not DaraCore.is_null(request.worker_auto_renew):
            body['worker_auto_renew'] = request.worker_auto_renew
        if not DaraCore.is_null(request.worker_auto_renew_period):
            body['worker_auto_renew_period'] = request.worker_auto_renew_period
        if not DaraCore.is_null(request.worker_data_disks):
            body['worker_data_disks'] = request.worker_data_disks
        if not DaraCore.is_null(request.worker_instance_charge_type):
            body['worker_instance_charge_type'] = request.worker_instance_charge_type
        if not DaraCore.is_null(request.worker_instance_types):
            body['worker_instance_types'] = request.worker_instance_types
        if not DaraCore.is_null(request.worker_period):
            body['worker_period'] = request.worker_period
        if not DaraCore.is_null(request.worker_period_unit):
            body['worker_period_unit'] = request.worker_period_unit
        if not DaraCore.is_null(request.worker_system_disk_category):
            body['worker_system_disk_category'] = request.worker_system_disk_category
        if not DaraCore.is_null(request.worker_system_disk_size):
            body['worker_system_disk_size'] = request.worker_system_disk_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ScaleOutCluster',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/clusters/{DaraURL.percent_encode(cluster_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleOutClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_out_cluster(
        self,
        cluster_id: str,
        request: main_models.ScaleOutClusterRequest,
    ) -> main_models.ScaleOutClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.scale_out_cluster_with_options(cluster_id, request, headers, runtime)

    async def scale_out_cluster_async(
        self,
        cluster_id: str,
        request: main_models.ScaleOutClusterRequest,
    ) -> main_models.ScaleOutClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.scale_out_cluster_with_options_async(cluster_id, request, headers, runtime)

    def scan_cluster_vuls_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScanClusterVulsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ScanClusterVuls',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/vuls/scan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScanClusterVulsResponse(),
            self.call_api(params, req, runtime)
        )

    async def scan_cluster_vuls_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScanClusterVulsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ScanClusterVuls',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/vuls/scan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScanClusterVulsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scan_cluster_vuls(
        self,
        cluster_id: str,
    ) -> main_models.ScanClusterVulsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.scan_cluster_vuls_with_options(cluster_id, headers, runtime)

    async def scan_cluster_vuls_async(
        self,
        cluster_id: str,
    ) -> main_models.ScanClusterVulsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.scan_cluster_vuls_with_options_async(cluster_id, headers, runtime)

    def start_alert_with_options(
        self,
        cluster_id: str,
        request: main_models.StartAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartAlertResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_rule_group_name):
            body['alert_rule_group_name'] = request.alert_rule_group_name
        if not DaraCore.is_null(request.alert_rule_name):
            body['alert_rule_name'] = request.alert_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartAlert',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/alert/{DaraURL.percent_encode(cluster_id)}/alert_rule/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_alert_with_options_async(
        self,
        cluster_id: str,
        request: main_models.StartAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartAlertResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_rule_group_name):
            body['alert_rule_group_name'] = request.alert_rule_group_name
        if not DaraCore.is_null(request.alert_rule_name):
            body['alert_rule_name'] = request.alert_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartAlert',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/alert/{DaraURL.percent_encode(cluster_id)}/alert_rule/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_alert(
        self,
        cluster_id: str,
        request: main_models.StartAlertRequest,
    ) -> main_models.StartAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_alert_with_options(cluster_id, request, headers, runtime)

    async def start_alert_async(
        self,
        cluster_id: str,
        request: main_models.StartAlertRequest,
    ) -> main_models.StartAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_alert_with_options_async(cluster_id, request, headers, runtime)

    def stop_alert_with_options(
        self,
        cluster_id: str,
        request: main_models.StopAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopAlertResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_rule_group_name):
            body['alert_rule_group_name'] = request.alert_rule_group_name
        if not DaraCore.is_null(request.alert_rule_name):
            body['alert_rule_name'] = request.alert_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopAlert',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/alert/{DaraURL.percent_encode(cluster_id)}/alert_rule/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_alert_with_options_async(
        self,
        cluster_id: str,
        request: main_models.StopAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopAlertResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_rule_group_name):
            body['alert_rule_group_name'] = request.alert_rule_group_name
        if not DaraCore.is_null(request.alert_rule_name):
            body['alert_rule_name'] = request.alert_rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopAlert',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/alert/{DaraURL.percent_encode(cluster_id)}/alert_rule/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_alert(
        self,
        cluster_id: str,
        request: main_models.StopAlertRequest,
    ) -> main_models.StopAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_alert_with_options(cluster_id, request, headers, runtime)

    async def stop_alert_async(
        self,
        cluster_id: str,
        request: main_models.StopAlertRequest,
    ) -> main_models.StopAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_alert_with_options_async(cluster_id, request, headers, runtime)

    def sync_cluster_node_pool_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SyncClusterNodePoolResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'SyncClusterNodePool',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/sync_nodepools',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncClusterNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_cluster_node_pool_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SyncClusterNodePoolResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'SyncClusterNodePool',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/sync_nodepools',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncClusterNodePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_cluster_node_pool(
        self,
        cluster_id: str,
    ) -> main_models.SyncClusterNodePoolResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.sync_cluster_node_pool_with_options(cluster_id, headers, runtime)

    async def sync_cluster_node_pool_async(
        self,
        cluster_id: str,
    ) -> main_models.SyncClusterNodePoolResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.sync_cluster_node_pool_with_options_async(cluster_id, headers, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['region_id'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            body['resource_ids'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['resource_type'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/tags',
            method = 'PUT',
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
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['region_id'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            body['resource_ids'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['resource_type'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/tags',
            method = 'PUT',
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

    def un_install_cluster_addons_with_options(
        self,
        cluster_id: str,
        request: main_models.UnInstallClusterAddonsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnInstallClusterAddonsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.to_array(request.addons)
        )
        params = open_api_util_models.Params(
            action = 'UnInstallClusterAddons',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/uninstall',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnInstallClusterAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_install_cluster_addons_with_options_async(
        self,
        cluster_id: str,
        request: main_models.UnInstallClusterAddonsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnInstallClusterAddonsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.to_array(request.addons)
        )
        params = open_api_util_models.Params(
            action = 'UnInstallClusterAddons',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/uninstall',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnInstallClusterAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_install_cluster_addons(
        self,
        cluster_id: str,
        request: main_models.UnInstallClusterAddonsRequest,
    ) -> main_models.UnInstallClusterAddonsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.un_install_cluster_addons_with_options(cluster_id, request, headers, runtime)

    async def un_install_cluster_addons_async(
        self,
        cluster_id: str,
        request: main_models.UnInstallClusterAddonsRequest,
    ) -> main_models.UnInstallClusterAddonsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.un_install_cluster_addons_with_options_async(cluster_id, request, headers, runtime)

    def untag_resources_with_options(
        self,
        tmp_req: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'resource_ids', 'json')
        if not DaraCore.is_null(tmp_req.tag_keys):
            request.tag_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_keys, 'tag_keys', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['all'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['region_id'] = request.region_id
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['resource_ids'] = request.resource_ids_shrink
        if not DaraCore.is_null(request.resource_type):
            query['resource_type'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys_shrink):
            query['tag_keys'] = request.tag_keys_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/tags',
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
        tmp_req: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'resource_ids', 'json')
        if not DaraCore.is_null(tmp_req.tag_keys):
            request.tag_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_keys, 'tag_keys', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['all'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['region_id'] = request.region_id
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['resource_ids'] = request.resource_ids_shrink
        if not DaraCore.is_null(request.resource_type):
            query['resource_type'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys_shrink):
            query['tag_keys'] = request.tag_keys_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/tags',
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

    def update_cluster_audit_log_config_with_options(
        self,
        clusterid: str,
        request: main_models.UpdateClusterAuditLogConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterAuditLogConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.disable):
            body['disable'] = request.disable
        if not DaraCore.is_null(request.sls_project_name):
            body['sls_project_name'] = request.sls_project_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClusterAuditLogConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(clusterid)}/audit_log',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterAuditLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_audit_log_config_with_options_async(
        self,
        clusterid: str,
        request: main_models.UpdateClusterAuditLogConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterAuditLogConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.disable):
            body['disable'] = request.disable
        if not DaraCore.is_null(request.sls_project_name):
            body['sls_project_name'] = request.sls_project_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClusterAuditLogConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(clusterid)}/audit_log',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterAuditLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster_audit_log_config(
        self,
        clusterid: str,
        request: main_models.UpdateClusterAuditLogConfigRequest,
    ) -> main_models.UpdateClusterAuditLogConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_cluster_audit_log_config_with_options(clusterid, request, headers, runtime)

    async def update_cluster_audit_log_config_async(
        self,
        clusterid: str,
        request: main_models.UpdateClusterAuditLogConfigRequest,
    ) -> main_models.UpdateClusterAuditLogConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_cluster_audit_log_config_with_options_async(clusterid, request, headers, runtime)

    def update_cluster_inspect_config_with_options(
        self,
        cluster_id: str,
        request: main_models.UpdateClusterInspectConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterInspectConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.disabled_check_items):
            body['disabledCheckItems'] = request.disabled_check_items
        if not DaraCore.is_null(request.enabled):
            body['enabled'] = request.enabled
        if not DaraCore.is_null(request.schedule_time):
            body['scheduleTime'] = request.schedule_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClusterInspectConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/inspectConfig',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterInspectConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_inspect_config_with_options_async(
        self,
        cluster_id: str,
        request: main_models.UpdateClusterInspectConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterInspectConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.disabled_check_items):
            body['disabledCheckItems'] = request.disabled_check_items
        if not DaraCore.is_null(request.enabled):
            body['enabled'] = request.enabled
        if not DaraCore.is_null(request.schedule_time):
            body['scheduleTime'] = request.schedule_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClusterInspectConfig',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/inspectConfig',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterInspectConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster_inspect_config(
        self,
        cluster_id: str,
        request: main_models.UpdateClusterInspectConfigRequest,
    ) -> main_models.UpdateClusterInspectConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_cluster_inspect_config_with_options(cluster_id, request, headers, runtime)

    async def update_cluster_inspect_config_async(
        self,
        cluster_id: str,
        request: main_models.UpdateClusterInspectConfigRequest,
    ) -> main_models.UpdateClusterInspectConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_cluster_inspect_config_with_options_async(cluster_id, request, headers, runtime)

    def update_contact_group_for_alert_with_options(
        self,
        cluster_id: str,
        request: main_models.UpdateContactGroupForAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContactGroupForAlertResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_rule_group_name):
            body['alert_rule_group_name'] = request.alert_rule_group_name
        if not DaraCore.is_null(request.contact_group_ids):
            body['contact_group_ids'] = request.contact_group_ids
        if not DaraCore.is_null(request.cr_name):
            body['cr_name'] = request.cr_name
        if not DaraCore.is_null(request.namespace):
            body['namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContactGroupForAlert',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/alert/{DaraURL.percent_encode(cluster_id)}/alert_rule/contact_groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContactGroupForAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_contact_group_for_alert_with_options_async(
        self,
        cluster_id: str,
        request: main_models.UpdateContactGroupForAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContactGroupForAlertResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_rule_group_name):
            body['alert_rule_group_name'] = request.alert_rule_group_name
        if not DaraCore.is_null(request.contact_group_ids):
            body['contact_group_ids'] = request.contact_group_ids
        if not DaraCore.is_null(request.cr_name):
            body['cr_name'] = request.cr_name
        if not DaraCore.is_null(request.namespace):
            body['namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContactGroupForAlert',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/alert/{DaraURL.percent_encode(cluster_id)}/alert_rule/contact_groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContactGroupForAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_contact_group_for_alert(
        self,
        cluster_id: str,
        request: main_models.UpdateContactGroupForAlertRequest,
    ) -> main_models.UpdateContactGroupForAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_contact_group_for_alert_with_options(cluster_id, request, headers, runtime)

    async def update_contact_group_for_alert_async(
        self,
        cluster_id: str,
        request: main_models.UpdateContactGroupForAlertRequest,
    ) -> main_models.UpdateContactGroupForAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_contact_group_for_alert_with_options_async(cluster_id, request, headers, runtime)

    def update_control_plane_log_with_options(
        self,
        cluster_id: str,
        request: main_models.UpdateControlPlaneLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateControlPlaneLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aliuid):
            body['aliuid'] = request.aliuid
        if not DaraCore.is_null(request.components):
            body['components'] = request.components
        if not DaraCore.is_null(request.log_project):
            body['log_project'] = request.log_project
        if not DaraCore.is_null(request.log_ttl):
            body['log_ttl'] = request.log_ttl
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateControlPlaneLog',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/controlplanelog',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateControlPlaneLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_control_plane_log_with_options_async(
        self,
        cluster_id: str,
        request: main_models.UpdateControlPlaneLogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateControlPlaneLogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aliuid):
            body['aliuid'] = request.aliuid
        if not DaraCore.is_null(request.components):
            body['components'] = request.components
        if not DaraCore.is_null(request.log_project):
            body['log_project'] = request.log_project
        if not DaraCore.is_null(request.log_ttl):
            body['log_ttl'] = request.log_ttl
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateControlPlaneLog',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/controlplanelog',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateControlPlaneLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_control_plane_log(
        self,
        cluster_id: str,
        request: main_models.UpdateControlPlaneLogRequest,
    ) -> main_models.UpdateControlPlaneLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_control_plane_log_with_options(cluster_id, request, headers, runtime)

    async def update_control_plane_log_async(
        self,
        cluster_id: str,
        request: main_models.UpdateControlPlaneLogRequest,
    ) -> main_models.UpdateControlPlaneLogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_control_plane_log_with_options_async(cluster_id, request, headers, runtime)

    def update_k8s_cluster_user_config_expire_with_options(
        self,
        cluster_id: str,
        request: main_models.UpdateK8sClusterUserConfigExpireRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sClusterUserConfigExpireResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.expire_hour):
            body['expire_hour'] = request.expire_hour
        if not DaraCore.is_null(request.user):
            body['user'] = request.user
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sClusterUserConfigExpire',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/k8s/{DaraURL.percent_encode(cluster_id)}/user_config/expire',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sClusterUserConfigExpireResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_cluster_user_config_expire_with_options_async(
        self,
        cluster_id: str,
        request: main_models.UpdateK8sClusterUserConfigExpireRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateK8sClusterUserConfigExpireResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.expire_hour):
            body['expire_hour'] = request.expire_hour
        if not DaraCore.is_null(request.user):
            body['user'] = request.user
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateK8sClusterUserConfigExpire',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/k8s/{DaraURL.percent_encode(cluster_id)}/user_config/expire',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateK8sClusterUserConfigExpireResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_cluster_user_config_expire(
        self,
        cluster_id: str,
        request: main_models.UpdateK8sClusterUserConfigExpireRequest,
    ) -> main_models.UpdateK8sClusterUserConfigExpireResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_k8s_cluster_user_config_expire_with_options(cluster_id, request, headers, runtime)

    async def update_k8s_cluster_user_config_expire_async(
        self,
        cluster_id: str,
        request: main_models.UpdateK8sClusterUserConfigExpireRequest,
    ) -> main_models.UpdateK8sClusterUserConfigExpireResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_k8s_cluster_user_config_expire_with_options_async(cluster_id, request, headers, runtime)

    def update_node_pool_component_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.UpdateNodePoolComponentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNodePoolComponentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.disable_rolling):
            body['disableRolling'] = request.disable_rolling
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.node_names):
            body['nodeNames'] = request.node_names
        if not DaraCore.is_null(request.rolling_policy):
            body['rollingPolicy'] = request.rolling_policy
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNodePoolComponent',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}/component',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNodePoolComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_node_pool_component_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.UpdateNodePoolComponentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNodePoolComponentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.disable_rolling):
            body['disableRolling'] = request.disable_rolling
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.node_names):
            body['nodeNames'] = request.node_names
        if not DaraCore.is_null(request.rolling_policy):
            body['rollingPolicy'] = request.rolling_policy
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNodePoolComponent',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}/component',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNodePoolComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_node_pool_component(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.UpdateNodePoolComponentRequest,
    ) -> main_models.UpdateNodePoolComponentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_node_pool_component_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def update_node_pool_component_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.UpdateNodePoolComponentRequest,
    ) -> main_models.UpdateNodePoolComponentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_node_pool_component_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def update_resources_delete_protection_with_options(
        self,
        cluster_id: str,
        request: main_models.UpdateResourcesDeleteProtectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourcesDeleteProtectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.namespace):
            body['namespace'] = request.namespace
        if not DaraCore.is_null(request.resource_type):
            body['resource_type'] = request.resource_type
        if not DaraCore.is_null(request.resources):
            body['resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourcesDeleteProtection',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/resources/protection',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourcesDeleteProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resources_delete_protection_with_options_async(
        self,
        cluster_id: str,
        request: main_models.UpdateResourcesDeleteProtectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourcesDeleteProtectionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.namespace):
            body['namespace'] = request.namespace
        if not DaraCore.is_null(request.resource_type):
            body['resource_type'] = request.resource_type
        if not DaraCore.is_null(request.resources):
            body['resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourcesDeleteProtection',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/resources/protection',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourcesDeleteProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resources_delete_protection(
        self,
        cluster_id: str,
        request: main_models.UpdateResourcesDeleteProtectionRequest,
    ) -> main_models.UpdateResourcesDeleteProtectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_resources_delete_protection_with_options(cluster_id, request, headers, runtime)

    async def update_resources_delete_protection_async(
        self,
        cluster_id: str,
        request: main_models.UpdateResourcesDeleteProtectionRequest,
    ) -> main_models.UpdateResourcesDeleteProtectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_resources_delete_protection_with_options_async(cluster_id, request, headers, runtime)

    def update_template_with_options(
        self,
        template_id: str,
        request: main_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.template):
            body['template'] = request.template
        if not DaraCore.is_null(request.template_type):
            body['template_type'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplate',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/templates/{DaraURL.percent_encode(template_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_with_options_async(
        self,
        template_id: str,
        request: main_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.template):
            body['template'] = request.template
        if not DaraCore.is_null(request.template_type):
            body['template_type'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplate',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/templates/{DaraURL.percent_encode(template_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template(
        self,
        template_id: str,
        request: main_models.UpdateTemplateRequest,
    ) -> main_models.UpdateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_template_with_options(template_id, request, headers, runtime)

    async def update_template_async(
        self,
        template_id: str,
        request: main_models.UpdateTemplateRequest,
    ) -> main_models.UpdateTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_template_with_options_async(template_id, request, headers, runtime)

    def update_user_permissions_with_options(
        self,
        uid: str,
        request: main_models.UpdateUserPermissionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserPermissionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mode):
            query['mode'] = request.mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserPermissions',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/permissions/users/{DaraURL.percent_encode(uid)}/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateUserPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_permissions_with_options_async(
        self,
        uid: str,
        request: main_models.UpdateUserPermissionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserPermissionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mode):
            query['mode'] = request.mode
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserPermissions',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/permissions/users/{DaraURL.percent_encode(uid)}/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateUserPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_permissions(
        self,
        uid: str,
        request: main_models.UpdateUserPermissionsRequest,
    ) -> main_models.UpdateUserPermissionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_user_permissions_with_options(uid, request, headers, runtime)

    async def update_user_permissions_async(
        self,
        uid: str,
        request: main_models.UpdateUserPermissionsRequest,
    ) -> main_models.UpdateUserPermissionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_user_permissions_with_options_async(uid, request, headers, runtime)

    def upgrade_cluster_with_options(
        self,
        cluster_id: str,
        request: main_models.UpgradeClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.component_name):
            body['component_name'] = request.component_name
        if not DaraCore.is_null(request.master_only):
            body['master_only'] = request.master_only
        if not DaraCore.is_null(request.next_version):
            body['next_version'] = request.next_version
        if not DaraCore.is_null(request.rolling_policy):
            body['rolling_policy'] = request.rolling_policy
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeCluster',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/clusters/{DaraURL.percent_encode(cluster_id)}/upgrade',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_cluster_with_options_async(
        self,
        cluster_id: str,
        request: main_models.UpgradeClusterRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.component_name):
            body['component_name'] = request.component_name
        if not DaraCore.is_null(request.master_only):
            body['master_only'] = request.master_only
        if not DaraCore.is_null(request.next_version):
            body['next_version'] = request.next_version
        if not DaraCore.is_null(request.rolling_policy):
            body['rolling_policy'] = request.rolling_policy
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeCluster',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/api/v2/clusters/{DaraURL.percent_encode(cluster_id)}/upgrade',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_cluster(
        self,
        cluster_id: str,
        request: main_models.UpgradeClusterRequest,
    ) -> main_models.UpgradeClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upgrade_cluster_with_options(cluster_id, request, headers, runtime)

    async def upgrade_cluster_async(
        self,
        cluster_id: str,
        request: main_models.UpgradeClusterRequest,
    ) -> main_models.UpgradeClusterResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upgrade_cluster_with_options_async(cluster_id, request, headers, runtime)

    def upgrade_cluster_addons_with_options(
        self,
        cluster_id: str,
        request: main_models.UpgradeClusterAddonsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeClusterAddonsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeClusterAddons',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/upgrade',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeClusterAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_cluster_addons_with_options_async(
        self,
        cluster_id: str,
        request: main_models.UpgradeClusterAddonsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeClusterAddonsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeClusterAddons',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/components/upgrade',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeClusterAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_cluster_addons(
        self,
        cluster_id: str,
        request: main_models.UpgradeClusterAddonsRequest,
    ) -> main_models.UpgradeClusterAddonsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upgrade_cluster_addons_with_options(cluster_id, request, headers, runtime)

    async def upgrade_cluster_addons_async(
        self,
        cluster_id: str,
        request: main_models.UpgradeClusterAddonsRequest,
    ) -> main_models.UpgradeClusterAddonsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upgrade_cluster_addons_with_options_async(cluster_id, request, headers, runtime)

    def upgrade_cluster_nodepool_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.UpgradeClusterNodepoolRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeClusterNodepoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_id):
            body['image_id'] = request.image_id
        if not DaraCore.is_null(request.kubernetes_version):
            body['kubernetes_version'] = request.kubernetes_version
        if not DaraCore.is_null(request.node_names):
            body['node_names'] = request.node_names
        if not DaraCore.is_null(request.rolling_policy):
            body['rolling_policy'] = request.rolling_policy
        if not DaraCore.is_null(request.runtime_type):
            body['runtime_type'] = request.runtime_type
        if not DaraCore.is_null(request.runtime_version):
            body['runtime_version'] = request.runtime_version
        if not DaraCore.is_null(request.use_replace):
            body['use_replace'] = request.use_replace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeClusterNodepool',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}/upgrade',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeClusterNodepoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_cluster_nodepool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.UpgradeClusterNodepoolRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeClusterNodepoolResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_id):
            body['image_id'] = request.image_id
        if not DaraCore.is_null(request.kubernetes_version):
            body['kubernetes_version'] = request.kubernetes_version
        if not DaraCore.is_null(request.node_names):
            body['node_names'] = request.node_names
        if not DaraCore.is_null(request.rolling_policy):
            body['rolling_policy'] = request.rolling_policy
        if not DaraCore.is_null(request.runtime_type):
            body['runtime_type'] = request.runtime_type
        if not DaraCore.is_null(request.runtime_version):
            body['runtime_version'] = request.runtime_version
        if not DaraCore.is_null(request.use_replace):
            body['use_replace'] = request.use_replace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeClusterNodepool',
            version = '2015-12-15',
            protocol = 'HTTPS',
            pathname = f'/clusters/{DaraURL.percent_encode(cluster_id)}/nodepools/{DaraURL.percent_encode(nodepool_id)}/upgrade',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeClusterNodepoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_cluster_nodepool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.UpgradeClusterNodepoolRequest,
    ) -> main_models.UpgradeClusterNodepoolResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upgrade_cluster_nodepool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def upgrade_cluster_nodepool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: main_models.UpgradeClusterNodepoolRequest,
    ) -> main_models.UpgradeClusterNodepoolResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upgrade_cluster_nodepool_with_options_async(cluster_id, nodepool_id, request, headers, runtime)
