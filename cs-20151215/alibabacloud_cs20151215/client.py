# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cs20151215 import models as cs20151215_models
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
        self._signature_algorithm = 'v2'
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def attach_instances_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.AttachInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.AttachInstancesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        if not UtilClient.is_unset(request.is_edge_worker):
            body['is_edge_worker'] = request.is_edge_worker
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.nodepool_id):
            body['nodepool_id'] = request.nodepool_id
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachInstances',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/attach',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.AttachInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_instances_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.AttachInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.AttachInstancesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        if not UtilClient.is_unset(request.is_edge_worker):
            body['is_edge_worker'] = request.is_edge_worker
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.nodepool_id):
            body['nodepool_id'] = request.nodepool_id
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachInstances',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/attach',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.AttachInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_instances(
        self,
        cluster_id: str,
        request: cs20151215_models.AttachInstancesRequest,
    ) -> cs20151215_models.AttachInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attach_instances_with_options(cluster_id, request, headers, runtime)

    async def attach_instances_async(
        self,
        cluster_id: str,
        request: cs20151215_models.AttachInstancesRequest,
    ) -> cs20151215_models.AttachInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.attach_instances_with_options_async(cluster_id, request, headers, runtime)

    def attach_instances_to_node_pool_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.AttachInstancesToNodePoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.AttachInstancesToNodePoolResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachInstancesToNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}/attach',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.AttachInstancesToNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_instances_to_node_pool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.AttachInstancesToNodePoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.AttachInstancesToNodePoolResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachInstancesToNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}/attach',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.AttachInstancesToNodePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_instances_to_node_pool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.AttachInstancesToNodePoolRequest,
    ) -> cs20151215_models.AttachInstancesToNodePoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attach_instances_to_node_pool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def attach_instances_to_node_pool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.AttachInstancesToNodePoolRequest,
    ) -> cs20151215_models.AttachInstancesToNodePoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.attach_instances_to_node_pool_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def cancel_cluster_upgrade_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelClusterUpgradeResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelClusterUpgradeResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelClusterUpgrade',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/upgrade/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.CancelClusterUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_cluster_upgrade_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelClusterUpgradeResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelClusterUpgradeResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelClusterUpgrade',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/upgrade/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.CancelClusterUpgradeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_cluster_upgrade(
        self,
        cluster_id: str,
    ) -> cs20151215_models.CancelClusterUpgradeResponse:
        """
        @deprecated
        
        @return: CancelClusterUpgradeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_cluster_upgrade_with_options(cluster_id, headers, runtime)

    async def cancel_cluster_upgrade_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.CancelClusterUpgradeResponse:
        """
        @deprecated
        
        @return: CancelClusterUpgradeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_cluster_upgrade_with_options_async(cluster_id, headers, runtime)

    def cancel_component_upgrade_with_options(
        self,
        cluster_id: str,
        component_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelComponentUpgradeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelComponentUpgrade',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/{OpenApiUtilClient.get_encode_param(component_id)}/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.CancelComponentUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_component_upgrade_with_options_async(
        self,
        cluster_id: str,
        component_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelComponentUpgradeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelComponentUpgrade',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/{OpenApiUtilClient.get_encode_param(component_id)}/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.CancelComponentUpgradeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_component_upgrade(
        self,
        cluster_id: str,
        component_id: str,
    ) -> cs20151215_models.CancelComponentUpgradeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_component_upgrade_with_options(cluster_id, component_id, headers, runtime)

    async def cancel_component_upgrade_async(
        self,
        cluster_id: str,
        component_id: str,
    ) -> cs20151215_models.CancelComponentUpgradeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_component_upgrade_with_options_async(cluster_id, component_id, headers, runtime)

    def cancel_operation_plan_with_options(
        self,
        plan_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelOperationPlanResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelOperationPlan',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/operation/plans/{OpenApiUtilClient.get_encode_param(plan_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CancelOperationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_operation_plan_with_options_async(
        self,
        plan_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelOperationPlanResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelOperationPlan',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/operation/plans/{OpenApiUtilClient.get_encode_param(plan_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CancelOperationPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_operation_plan(
        self,
        plan_id: str,
    ) -> cs20151215_models.CancelOperationPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_operation_plan_with_options(plan_id, headers, runtime)

    async def cancel_operation_plan_async(
        self,
        plan_id: str,
    ) -> cs20151215_models.CancelOperationPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_operation_plan_with_options_async(plan_id, headers, runtime)

    def cancel_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.CancelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_task(
        self,
        task_id: str,
    ) -> cs20151215_models.CancelTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_task_with_options(task_id, headers, runtime)

    async def cancel_task_async(
        self,
        task_id: str,
    ) -> cs20151215_models.CancelTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_task_with_options_async(task_id, headers, runtime)

    def cancel_workflow_with_options(
        self,
        workflow_name: str,
        request: cs20151215_models.CancelWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelWorkflowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelWorkflow',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/gs/workflow/{OpenApiUtilClient.get_encode_param(workflow_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.CancelWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_workflow_with_options_async(
        self,
        workflow_name: str,
        request: cs20151215_models.CancelWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CancelWorkflowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelWorkflow',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/gs/workflow/{OpenApiUtilClient.get_encode_param(workflow_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.CancelWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_workflow(
        self,
        workflow_name: str,
        request: cs20151215_models.CancelWorkflowRequest,
    ) -> cs20151215_models.CancelWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_workflow_with_options(workflow_name, request, headers, runtime)

    async def cancel_workflow_async(
        self,
        workflow_name: str,
        request: cs20151215_models.CancelWorkflowRequest,
    ) -> cs20151215_models.CancelWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_workflow_with_options_async(workflow_name, request, headers, runtime)

    def check_control_plane_log_enable_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CheckControlPlaneLogEnableResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CheckControlPlaneLogEnable',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/controlplanelog',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CheckControlPlaneLogEnableResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_control_plane_log_enable_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CheckControlPlaneLogEnableResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CheckControlPlaneLogEnable',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/controlplanelog',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CheckControlPlaneLogEnableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_control_plane_log_enable(
        self,
        cluster_id: str,
    ) -> cs20151215_models.CheckControlPlaneLogEnableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_control_plane_log_enable_with_options(cluster_id, headers, runtime)

    async def check_control_plane_log_enable_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.CheckControlPlaneLogEnableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_control_plane_log_enable_with_options_async(cluster_id, headers, runtime)

    def create_autoscaling_config_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateAutoscalingConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateAutoscalingConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cool_down_duration):
            body['cool_down_duration'] = request.cool_down_duration
        if not UtilClient.is_unset(request.daemonset_eviction_for_nodes):
            body['daemonset_eviction_for_nodes'] = request.daemonset_eviction_for_nodes
        if not UtilClient.is_unset(request.expander):
            body['expander'] = request.expander
        if not UtilClient.is_unset(request.gpu_utilization_threshold):
            body['gpu_utilization_threshold'] = request.gpu_utilization_threshold
        if not UtilClient.is_unset(request.max_graceful_termination_sec):
            body['max_graceful_termination_sec'] = request.max_graceful_termination_sec
        if not UtilClient.is_unset(request.min_replica_count):
            body['min_replica_count'] = request.min_replica_count
        if not UtilClient.is_unset(request.recycle_node_deletion_enabled):
            body['recycle_node_deletion_enabled'] = request.recycle_node_deletion_enabled
        if not UtilClient.is_unset(request.scale_down_enabled):
            body['scale_down_enabled'] = request.scale_down_enabled
        if not UtilClient.is_unset(request.scale_up_from_zero):
            body['scale_up_from_zero'] = request.scale_up_from_zero
        if not UtilClient.is_unset(request.scan_interval):
            body['scan_interval'] = request.scan_interval
        if not UtilClient.is_unset(request.skip_nodes_with_local_storage):
            body['skip_nodes_with_local_storage'] = request.skip_nodes_with_local_storage
        if not UtilClient.is_unset(request.skip_nodes_with_system_pods):
            body['skip_nodes_with_system_pods'] = request.skip_nodes_with_system_pods
        if not UtilClient.is_unset(request.unneeded_duration):
            body['unneeded_duration'] = request.unneeded_duration
        if not UtilClient.is_unset(request.utilization_threshold):
            body['utilization_threshold'] = request.utilization_threshold
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAutoscalingConfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/cluster/{OpenApiUtilClient.get_encode_param(cluster_id)}/autoscale/config/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateAutoscalingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_autoscaling_config_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateAutoscalingConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateAutoscalingConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cool_down_duration):
            body['cool_down_duration'] = request.cool_down_duration
        if not UtilClient.is_unset(request.daemonset_eviction_for_nodes):
            body['daemonset_eviction_for_nodes'] = request.daemonset_eviction_for_nodes
        if not UtilClient.is_unset(request.expander):
            body['expander'] = request.expander
        if not UtilClient.is_unset(request.gpu_utilization_threshold):
            body['gpu_utilization_threshold'] = request.gpu_utilization_threshold
        if not UtilClient.is_unset(request.max_graceful_termination_sec):
            body['max_graceful_termination_sec'] = request.max_graceful_termination_sec
        if not UtilClient.is_unset(request.min_replica_count):
            body['min_replica_count'] = request.min_replica_count
        if not UtilClient.is_unset(request.recycle_node_deletion_enabled):
            body['recycle_node_deletion_enabled'] = request.recycle_node_deletion_enabled
        if not UtilClient.is_unset(request.scale_down_enabled):
            body['scale_down_enabled'] = request.scale_down_enabled
        if not UtilClient.is_unset(request.scale_up_from_zero):
            body['scale_up_from_zero'] = request.scale_up_from_zero
        if not UtilClient.is_unset(request.scan_interval):
            body['scan_interval'] = request.scan_interval
        if not UtilClient.is_unset(request.skip_nodes_with_local_storage):
            body['skip_nodes_with_local_storage'] = request.skip_nodes_with_local_storage
        if not UtilClient.is_unset(request.skip_nodes_with_system_pods):
            body['skip_nodes_with_system_pods'] = request.skip_nodes_with_system_pods
        if not UtilClient.is_unset(request.unneeded_duration):
            body['unneeded_duration'] = request.unneeded_duration
        if not UtilClient.is_unset(request.utilization_threshold):
            body['utilization_threshold'] = request.utilization_threshold
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAutoscalingConfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/cluster/{OpenApiUtilClient.get_encode_param(cluster_id)}/autoscale/config/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateAutoscalingConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_autoscaling_config(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateAutoscalingConfigRequest,
    ) -> cs20151215_models.CreateAutoscalingConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_autoscaling_config_with_options(cluster_id, request, headers, runtime)

    async def create_autoscaling_config_async(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateAutoscalingConfigRequest,
    ) -> cs20151215_models.CreateAutoscalingConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_autoscaling_config_with_options_async(cluster_id, request, headers, runtime)

    def create_cluster_with_options(
        self,
        request: cs20151215_models.CreateClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateClusterResponse:
        """
        This topic describes all parameters for creating an ACK cluster. You can create the following types of ACK clusters.
        *   [Create an ACK managed cluster](~~90776~~)
        *   [Create an ACK dedicated cluster](~~197620~~)
        *   [Create an ACK Serverless cluster](~~144246~~)
        *   [Create an ACK Edge cluster](~~128204~~)
        *   [Create an ACK Basic cluster that supports sandboxed containers](~~196321~~)
        *   [Create an ACK Pro cluster that supports sandboxed containers](~~140623~~)
        
        @param request: CreateClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_control_list):
            body['access_control_list'] = request.access_control_list
        if not UtilClient.is_unset(request.addons):
            body['addons'] = request.addons
        if not UtilClient.is_unset(request.api_audiences):
            body['api_audiences'] = request.api_audiences
        if not UtilClient.is_unset(request.charge_type):
            body['charge_type'] = request.charge_type
        if not UtilClient.is_unset(request.cis_enabled):
            body['cis_enabled'] = request.cis_enabled
        if not UtilClient.is_unset(request.cloud_monitor_flags):
            body['cloud_monitor_flags'] = request.cloud_monitor_flags
        if not UtilClient.is_unset(request.cluster_domain):
            body['cluster_domain'] = request.cluster_domain
        if not UtilClient.is_unset(request.cluster_spec):
            body['cluster_spec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cluster_type):
            body['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.container_cidr):
            body['container_cidr'] = request.container_cidr
        if not UtilClient.is_unset(request.controlplane_log_components):
            body['controlplane_log_components'] = request.controlplane_log_components
        if not UtilClient.is_unset(request.controlplane_log_project):
            body['controlplane_log_project'] = request.controlplane_log_project
        if not UtilClient.is_unset(request.controlplane_log_ttl):
            body['controlplane_log_ttl'] = request.controlplane_log_ttl
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.custom_san):
            body['custom_san'] = request.custom_san
        if not UtilClient.is_unset(request.deletion_protection):
            body['deletion_protection'] = request.deletion_protection
        if not UtilClient.is_unset(request.disable_rollback):
            body['disable_rollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.enable_rrsa):
            body['enable_rrsa'] = request.enable_rrsa
        if not UtilClient.is_unset(request.encryption_provider_key):
            body['encryption_provider_key'] = request.encryption_provider_key
        if not UtilClient.is_unset(request.endpoint_public_access):
            body['endpoint_public_access'] = request.endpoint_public_access
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.image_type):
            body['image_type'] = request.image_type
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        if not UtilClient.is_unset(request.ip_stack):
            body['ip_stack'] = request.ip_stack
        if not UtilClient.is_unset(request.is_enterprise_security_group):
            body['is_enterprise_security_group'] = request.is_enterprise_security_group
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.kubernetes_version):
            body['kubernetes_version'] = request.kubernetes_version
        if not UtilClient.is_unset(request.load_balancer_spec):
            body['load_balancer_spec'] = request.load_balancer_spec
        if not UtilClient.is_unset(request.logging_type):
            body['logging_type'] = request.logging_type
        if not UtilClient.is_unset(request.login_password):
            body['login_password'] = request.login_password
        if not UtilClient.is_unset(request.master_auto_renew):
            body['master_auto_renew'] = request.master_auto_renew
        if not UtilClient.is_unset(request.master_auto_renew_period):
            body['master_auto_renew_period'] = request.master_auto_renew_period
        if not UtilClient.is_unset(request.master_count):
            body['master_count'] = request.master_count
        if not UtilClient.is_unset(request.master_instance_charge_type):
            body['master_instance_charge_type'] = request.master_instance_charge_type
        if not UtilClient.is_unset(request.master_instance_types):
            body['master_instance_types'] = request.master_instance_types
        if not UtilClient.is_unset(request.master_period):
            body['master_period'] = request.master_period
        if not UtilClient.is_unset(request.master_period_unit):
            body['master_period_unit'] = request.master_period_unit
        if not UtilClient.is_unset(request.master_system_disk_category):
            body['master_system_disk_category'] = request.master_system_disk_category
        if not UtilClient.is_unset(request.master_system_disk_performance_level):
            body['master_system_disk_performance_level'] = request.master_system_disk_performance_level
        if not UtilClient.is_unset(request.master_system_disk_size):
            body['master_system_disk_size'] = request.master_system_disk_size
        if not UtilClient.is_unset(request.master_system_disk_snapshot_policy_id):
            body['master_system_disk_snapshot_policy_id'] = request.master_system_disk_snapshot_policy_id
        if not UtilClient.is_unset(request.master_vswitch_ids):
            body['master_vswitch_ids'] = request.master_vswitch_ids
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.nat_gateway):
            body['nat_gateway'] = request.nat_gateway
        if not UtilClient.is_unset(request.node_cidr_mask):
            body['node_cidr_mask'] = request.node_cidr_mask
        if not UtilClient.is_unset(request.node_name_mode):
            body['node_name_mode'] = request.node_name_mode
        if not UtilClient.is_unset(request.node_port_range):
            body['node_port_range'] = request.node_port_range
        if not UtilClient.is_unset(request.nodepools):
            body['nodepools'] = request.nodepools
        if not UtilClient.is_unset(request.num_of_nodes):
            body['num_of_nodes'] = request.num_of_nodes
        if not UtilClient.is_unset(request.os_type):
            body['os_type'] = request.os_type
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            body['period_unit'] = request.period_unit
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.pod_vswitch_ids):
            body['pod_vswitch_ids'] = request.pod_vswitch_ids
        if not UtilClient.is_unset(request.profile):
            body['profile'] = request.profile
        if not UtilClient.is_unset(request.proxy_mode):
            body['proxy_mode'] = request.proxy_mode
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not UtilClient.is_unset(request.region_id):
            body['region_id'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['resource_group_id'] = request.resource_group_id
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.security_group_id):
            body['security_group_id'] = request.security_group_id
        if not UtilClient.is_unset(request.service_account_issuer):
            body['service_account_issuer'] = request.service_account_issuer
        if not UtilClient.is_unset(request.service_cidr):
            body['service_cidr'] = request.service_cidr
        if not UtilClient.is_unset(request.service_discovery_types):
            body['service_discovery_types'] = request.service_discovery_types
        if not UtilClient.is_unset(request.snat_entry):
            body['snat_entry'] = request.snat_entry
        if not UtilClient.is_unset(request.soc_enabled):
            body['soc_enabled'] = request.soc_enabled
        if not UtilClient.is_unset(request.ssh_flags):
            body['ssh_flags'] = request.ssh_flags
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.timeout_mins):
            body['timeout_mins'] = request.timeout_mins
        if not UtilClient.is_unset(request.timezone):
            body['timezone'] = request.timezone
        if not UtilClient.is_unset(request.user_ca):
            body['user_ca'] = request.user_ca
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.vpcid):
            body['vpcid'] = request.vpcid
        if not UtilClient.is_unset(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        if not UtilClient.is_unset(request.worker_auto_renew):
            body['worker_auto_renew'] = request.worker_auto_renew
        if not UtilClient.is_unset(request.worker_auto_renew_period):
            body['worker_auto_renew_period'] = request.worker_auto_renew_period
        if not UtilClient.is_unset(request.worker_data_disks):
            body['worker_data_disks'] = request.worker_data_disks
        if not UtilClient.is_unset(request.worker_instance_charge_type):
            body['worker_instance_charge_type'] = request.worker_instance_charge_type
        if not UtilClient.is_unset(request.worker_instance_types):
            body['worker_instance_types'] = request.worker_instance_types
        if not UtilClient.is_unset(request.worker_period):
            body['worker_period'] = request.worker_period
        if not UtilClient.is_unset(request.worker_period_unit):
            body['worker_period_unit'] = request.worker_period_unit
        if not UtilClient.is_unset(request.worker_system_disk_category):
            body['worker_system_disk_category'] = request.worker_system_disk_category
        if not UtilClient.is_unset(request.worker_system_disk_performance_level):
            body['worker_system_disk_performance_level'] = request.worker_system_disk_performance_level
        if not UtilClient.is_unset(request.worker_system_disk_size):
            body['worker_system_disk_size'] = request.worker_system_disk_size
        if not UtilClient.is_unset(request.worker_system_disk_snapshot_policy_id):
            body['worker_system_disk_snapshot_policy_id'] = request.worker_system_disk_snapshot_policy_id
        if not UtilClient.is_unset(request.worker_vswitch_ids):
            body['worker_vswitch_ids'] = request.worker_vswitch_ids
        if not UtilClient.is_unset(request.zone_id):
            body['zone_id'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: cs20151215_models.CreateClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateClusterResponse:
        """
        This topic describes all parameters for creating an ACK cluster. You can create the following types of ACK clusters.
        *   [Create an ACK managed cluster](~~90776~~)
        *   [Create an ACK dedicated cluster](~~197620~~)
        *   [Create an ACK Serverless cluster](~~144246~~)
        *   [Create an ACK Edge cluster](~~128204~~)
        *   [Create an ACK Basic cluster that supports sandboxed containers](~~196321~~)
        *   [Create an ACK Pro cluster that supports sandboxed containers](~~140623~~)
        
        @param request: CreateClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_control_list):
            body['access_control_list'] = request.access_control_list
        if not UtilClient.is_unset(request.addons):
            body['addons'] = request.addons
        if not UtilClient.is_unset(request.api_audiences):
            body['api_audiences'] = request.api_audiences
        if not UtilClient.is_unset(request.charge_type):
            body['charge_type'] = request.charge_type
        if not UtilClient.is_unset(request.cis_enabled):
            body['cis_enabled'] = request.cis_enabled
        if not UtilClient.is_unset(request.cloud_monitor_flags):
            body['cloud_monitor_flags'] = request.cloud_monitor_flags
        if not UtilClient.is_unset(request.cluster_domain):
            body['cluster_domain'] = request.cluster_domain
        if not UtilClient.is_unset(request.cluster_spec):
            body['cluster_spec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cluster_type):
            body['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.container_cidr):
            body['container_cidr'] = request.container_cidr
        if not UtilClient.is_unset(request.controlplane_log_components):
            body['controlplane_log_components'] = request.controlplane_log_components
        if not UtilClient.is_unset(request.controlplane_log_project):
            body['controlplane_log_project'] = request.controlplane_log_project
        if not UtilClient.is_unset(request.controlplane_log_ttl):
            body['controlplane_log_ttl'] = request.controlplane_log_ttl
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.custom_san):
            body['custom_san'] = request.custom_san
        if not UtilClient.is_unset(request.deletion_protection):
            body['deletion_protection'] = request.deletion_protection
        if not UtilClient.is_unset(request.disable_rollback):
            body['disable_rollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.enable_rrsa):
            body['enable_rrsa'] = request.enable_rrsa
        if not UtilClient.is_unset(request.encryption_provider_key):
            body['encryption_provider_key'] = request.encryption_provider_key
        if not UtilClient.is_unset(request.endpoint_public_access):
            body['endpoint_public_access'] = request.endpoint_public_access
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.image_type):
            body['image_type'] = request.image_type
        if not UtilClient.is_unset(request.instances):
            body['instances'] = request.instances
        if not UtilClient.is_unset(request.ip_stack):
            body['ip_stack'] = request.ip_stack
        if not UtilClient.is_unset(request.is_enterprise_security_group):
            body['is_enterprise_security_group'] = request.is_enterprise_security_group
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.kubernetes_version):
            body['kubernetes_version'] = request.kubernetes_version
        if not UtilClient.is_unset(request.load_balancer_spec):
            body['load_balancer_spec'] = request.load_balancer_spec
        if not UtilClient.is_unset(request.logging_type):
            body['logging_type'] = request.logging_type
        if not UtilClient.is_unset(request.login_password):
            body['login_password'] = request.login_password
        if not UtilClient.is_unset(request.master_auto_renew):
            body['master_auto_renew'] = request.master_auto_renew
        if not UtilClient.is_unset(request.master_auto_renew_period):
            body['master_auto_renew_period'] = request.master_auto_renew_period
        if not UtilClient.is_unset(request.master_count):
            body['master_count'] = request.master_count
        if not UtilClient.is_unset(request.master_instance_charge_type):
            body['master_instance_charge_type'] = request.master_instance_charge_type
        if not UtilClient.is_unset(request.master_instance_types):
            body['master_instance_types'] = request.master_instance_types
        if not UtilClient.is_unset(request.master_period):
            body['master_period'] = request.master_period
        if not UtilClient.is_unset(request.master_period_unit):
            body['master_period_unit'] = request.master_period_unit
        if not UtilClient.is_unset(request.master_system_disk_category):
            body['master_system_disk_category'] = request.master_system_disk_category
        if not UtilClient.is_unset(request.master_system_disk_performance_level):
            body['master_system_disk_performance_level'] = request.master_system_disk_performance_level
        if not UtilClient.is_unset(request.master_system_disk_size):
            body['master_system_disk_size'] = request.master_system_disk_size
        if not UtilClient.is_unset(request.master_system_disk_snapshot_policy_id):
            body['master_system_disk_snapshot_policy_id'] = request.master_system_disk_snapshot_policy_id
        if not UtilClient.is_unset(request.master_vswitch_ids):
            body['master_vswitch_ids'] = request.master_vswitch_ids
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.nat_gateway):
            body['nat_gateway'] = request.nat_gateway
        if not UtilClient.is_unset(request.node_cidr_mask):
            body['node_cidr_mask'] = request.node_cidr_mask
        if not UtilClient.is_unset(request.node_name_mode):
            body['node_name_mode'] = request.node_name_mode
        if not UtilClient.is_unset(request.node_port_range):
            body['node_port_range'] = request.node_port_range
        if not UtilClient.is_unset(request.nodepools):
            body['nodepools'] = request.nodepools
        if not UtilClient.is_unset(request.num_of_nodes):
            body['num_of_nodes'] = request.num_of_nodes
        if not UtilClient.is_unset(request.os_type):
            body['os_type'] = request.os_type
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            body['period_unit'] = request.period_unit
        if not UtilClient.is_unset(request.platform):
            body['platform'] = request.platform
        if not UtilClient.is_unset(request.pod_vswitch_ids):
            body['pod_vswitch_ids'] = request.pod_vswitch_ids
        if not UtilClient.is_unset(request.profile):
            body['profile'] = request.profile
        if not UtilClient.is_unset(request.proxy_mode):
            body['proxy_mode'] = request.proxy_mode
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not UtilClient.is_unset(request.region_id):
            body['region_id'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['resource_group_id'] = request.resource_group_id
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.security_group_id):
            body['security_group_id'] = request.security_group_id
        if not UtilClient.is_unset(request.service_account_issuer):
            body['service_account_issuer'] = request.service_account_issuer
        if not UtilClient.is_unset(request.service_cidr):
            body['service_cidr'] = request.service_cidr
        if not UtilClient.is_unset(request.service_discovery_types):
            body['service_discovery_types'] = request.service_discovery_types
        if not UtilClient.is_unset(request.snat_entry):
            body['snat_entry'] = request.snat_entry
        if not UtilClient.is_unset(request.soc_enabled):
            body['soc_enabled'] = request.soc_enabled
        if not UtilClient.is_unset(request.ssh_flags):
            body['ssh_flags'] = request.ssh_flags
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.timeout_mins):
            body['timeout_mins'] = request.timeout_mins
        if not UtilClient.is_unset(request.timezone):
            body['timezone'] = request.timezone
        if not UtilClient.is_unset(request.user_ca):
            body['user_ca'] = request.user_ca
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.vpcid):
            body['vpcid'] = request.vpcid
        if not UtilClient.is_unset(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        if not UtilClient.is_unset(request.worker_auto_renew):
            body['worker_auto_renew'] = request.worker_auto_renew
        if not UtilClient.is_unset(request.worker_auto_renew_period):
            body['worker_auto_renew_period'] = request.worker_auto_renew_period
        if not UtilClient.is_unset(request.worker_data_disks):
            body['worker_data_disks'] = request.worker_data_disks
        if not UtilClient.is_unset(request.worker_instance_charge_type):
            body['worker_instance_charge_type'] = request.worker_instance_charge_type
        if not UtilClient.is_unset(request.worker_instance_types):
            body['worker_instance_types'] = request.worker_instance_types
        if not UtilClient.is_unset(request.worker_period):
            body['worker_period'] = request.worker_period
        if not UtilClient.is_unset(request.worker_period_unit):
            body['worker_period_unit'] = request.worker_period_unit
        if not UtilClient.is_unset(request.worker_system_disk_category):
            body['worker_system_disk_category'] = request.worker_system_disk_category
        if not UtilClient.is_unset(request.worker_system_disk_performance_level):
            body['worker_system_disk_performance_level'] = request.worker_system_disk_performance_level
        if not UtilClient.is_unset(request.worker_system_disk_size):
            body['worker_system_disk_size'] = request.worker_system_disk_size
        if not UtilClient.is_unset(request.worker_system_disk_snapshot_policy_id):
            body['worker_system_disk_snapshot_policy_id'] = request.worker_system_disk_snapshot_policy_id
        if not UtilClient.is_unset(request.worker_vswitch_ids):
            body['worker_vswitch_ids'] = request.worker_vswitch_ids
        if not UtilClient.is_unset(request.zone_id):
            body['zone_id'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: cs20151215_models.CreateClusterRequest,
    ) -> cs20151215_models.CreateClusterResponse:
        """
        This topic describes all parameters for creating an ACK cluster. You can create the following types of ACK clusters.
        *   [Create an ACK managed cluster](~~90776~~)
        *   [Create an ACK dedicated cluster](~~197620~~)
        *   [Create an ACK Serverless cluster](~~144246~~)
        *   [Create an ACK Edge cluster](~~128204~~)
        *   [Create an ACK Basic cluster that supports sandboxed containers](~~196321~~)
        *   [Create an ACK Pro cluster that supports sandboxed containers](~~140623~~)
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_cluster_with_options(request, headers, runtime)

    async def create_cluster_async(
        self,
        request: cs20151215_models.CreateClusterRequest,
    ) -> cs20151215_models.CreateClusterResponse:
        """
        This topic describes all parameters for creating an ACK cluster. You can create the following types of ACK clusters.
        *   [Create an ACK managed cluster](~~90776~~)
        *   [Create an ACK dedicated cluster](~~197620~~)
        *   [Create an ACK Serverless cluster](~~144246~~)
        *   [Create an ACK Edge cluster](~~128204~~)
        *   [Create an ACK Basic cluster that supports sandboxed containers](~~196321~~)
        *   [Create an ACK Pro cluster that supports sandboxed containers](~~140623~~)
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_cluster_with_options_async(request, headers, runtime)

    def create_cluster_node_pool_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateClusterNodePoolResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_scaling):
            body['auto_scaling'] = request.auto_scaling
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        if not UtilClient.is_unset(request.interconnect_config):
            body['interconnect_config'] = request.interconnect_config
        if not UtilClient.is_unset(request.interconnect_mode):
            body['interconnect_mode'] = request.interconnect_mode
        if not UtilClient.is_unset(request.kubernetes_config):
            body['kubernetes_config'] = request.kubernetes_config
        if not UtilClient.is_unset(request.management):
            body['management'] = request.management
        if not UtilClient.is_unset(request.max_nodes):
            body['max_nodes'] = request.max_nodes
        if not UtilClient.is_unset(request.node_config):
            body['node_config'] = request.node_config
        if not UtilClient.is_unset(request.nodepool_info):
            body['nodepool_info'] = request.nodepool_info
        if not UtilClient.is_unset(request.scaling_group):
            body['scaling_group'] = request.scaling_group
        if not UtilClient.is_unset(request.tee_config):
            body['tee_config'] = request.tee_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateClusterNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateClusterNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_node_pool_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateClusterNodePoolResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_scaling):
            body['auto_scaling'] = request.auto_scaling
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        if not UtilClient.is_unset(request.interconnect_config):
            body['interconnect_config'] = request.interconnect_config
        if not UtilClient.is_unset(request.interconnect_mode):
            body['interconnect_mode'] = request.interconnect_mode
        if not UtilClient.is_unset(request.kubernetes_config):
            body['kubernetes_config'] = request.kubernetes_config
        if not UtilClient.is_unset(request.management):
            body['management'] = request.management
        if not UtilClient.is_unset(request.max_nodes):
            body['max_nodes'] = request.max_nodes
        if not UtilClient.is_unset(request.node_config):
            body['node_config'] = request.node_config
        if not UtilClient.is_unset(request.nodepool_info):
            body['nodepool_info'] = request.nodepool_info
        if not UtilClient.is_unset(request.scaling_group):
            body['scaling_group'] = request.scaling_group
        if not UtilClient.is_unset(request.tee_config):
            body['tee_config'] = request.tee_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateClusterNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateClusterNodePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster_node_pool(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateClusterNodePoolRequest,
    ) -> cs20151215_models.CreateClusterNodePoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_cluster_node_pool_with_options(cluster_id, request, headers, runtime)

    async def create_cluster_node_pool_async(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateClusterNodePoolRequest,
    ) -> cs20151215_models.CreateClusterNodePoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_cluster_node_pool_with_options_async(cluster_id, request, headers, runtime)

    def create_edge_machine_with_options(
        self,
        request: cs20151215_models.CreateEdgeMachineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateEdgeMachineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hostname):
            body['hostname'] = request.hostname
        if not UtilClient.is_unset(request.model):
            body['model'] = request.model
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEdgeMachine',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/edge_machines',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateEdgeMachineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_edge_machine_with_options_async(
        self,
        request: cs20151215_models.CreateEdgeMachineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateEdgeMachineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hostname):
            body['hostname'] = request.hostname
        if not UtilClient.is_unset(request.model):
            body['model'] = request.model
        if not UtilClient.is_unset(request.sn):
            body['sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEdgeMachine',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/edge_machines',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateEdgeMachineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_edge_machine(
        self,
        request: cs20151215_models.CreateEdgeMachineRequest,
    ) -> cs20151215_models.CreateEdgeMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_edge_machine_with_options(request, headers, runtime)

    async def create_edge_machine_async(
        self,
        request: cs20151215_models.CreateEdgeMachineRequest,
    ) -> cs20151215_models.CreateEdgeMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_edge_machine_with_options_async(request, headers, runtime)

    def create_kubernetes_trigger_with_options(
        self,
        request: cs20151215_models.CreateKubernetesTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateKubernetesTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.project_id):
            body['project_id'] = request.project_id
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateKubernetesTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/triggers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateKubernetesTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_kubernetes_trigger_with_options_async(
        self,
        request: cs20151215_models.CreateKubernetesTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateKubernetesTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.project_id):
            body['project_id'] = request.project_id
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateKubernetesTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/triggers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateKubernetesTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_kubernetes_trigger(
        self,
        request: cs20151215_models.CreateKubernetesTriggerRequest,
    ) -> cs20151215_models.CreateKubernetesTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_kubernetes_trigger_with_options(request, headers, runtime)

    async def create_kubernetes_trigger_async(
        self,
        request: cs20151215_models.CreateKubernetesTriggerRequest,
    ) -> cs20151215_models.CreateKubernetesTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_kubernetes_trigger_with_options_async(request, headers, runtime)

    def create_template_with_options(
        self,
        request: cs20151215_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        if not UtilClient.is_unset(request.template_type):
            body['template_type'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/templates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: cs20151215_models.CreateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        if not UtilClient.is_unset(request.template_type):
            body['template_type'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/templates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: cs20151215_models.CreateTemplateRequest,
    ) -> cs20151215_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_template_with_options(request, headers, runtime)

    async def create_template_async(
        self,
        request: cs20151215_models.CreateTemplateRequest,
    ) -> cs20151215_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_template_with_options_async(request, headers, runtime)

    def create_trigger_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.project_id):
            body['project_id'] = request.project_id
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/triggers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_trigger_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.CreateTriggerResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.cluster_id):
            body['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.project_id):
            body['project_id'] = request.project_id
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/triggers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.CreateTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_trigger(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateTriggerRequest,
    ) -> cs20151215_models.CreateTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_trigger_with_options(cluster_id, request, headers, runtime)

    async def create_trigger_async(
        self,
        cluster_id: str,
        request: cs20151215_models.CreateTriggerRequest,
    ) -> cs20151215_models.CreateTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_trigger_with_options_async(cluster_id, request, headers, runtime)

    def delete_alert_contact_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteAlertContactResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAlertContact',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/alert/contacts',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_contact_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteAlertContactResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAlertContact',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/alert/contacts',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_contact(self) -> cs20151215_models.DeleteAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_alert_contact_with_options(headers, runtime)

    async def delete_alert_contact_async(self) -> cs20151215_models.DeleteAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_alert_contact_with_options_async(headers, runtime)

    def delete_alert_contact_group_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteAlertContactGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAlertContactGroup',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/alert/contact_groups',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_contact_group_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteAlertContactGroupResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAlertContactGroup',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/alert/contact_groups',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_contact_group(self) -> cs20151215_models.DeleteAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_alert_contact_group_with_options(headers, runtime)

    async def delete_alert_contact_group_async(self) -> cs20151215_models.DeleteAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_alert_contact_group_with_options_async(headers, runtime)

    def delete_cluster_with_options(
        self,
        cluster_id: str,
        tmp_req: cs20151215_models.DeleteClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.DeleteClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.retain_resources):
            request.retain_resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retain_resources, 'retain_resources', 'json')
        query = {}
        if not UtilClient.is_unset(request.keep_slb):
            query['keep_slb'] = request.keep_slb
        if not UtilClient.is_unset(request.retain_all_resources):
            query['retain_all_resources'] = request.retain_all_resources
        if not UtilClient.is_unset(request.retain_resources_shrink):
            query['retain_resources'] = request.retain_resources_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        cluster_id: str,
        tmp_req: cs20151215_models.DeleteClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.DeleteClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.retain_resources):
            request.retain_resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retain_resources, 'retain_resources', 'json')
        query = {}
        if not UtilClient.is_unset(request.keep_slb):
            query['keep_slb'] = request.keep_slb
        if not UtilClient.is_unset(request.retain_all_resources):
            query['retain_all_resources'] = request.retain_all_resources
        if not UtilClient.is_unset(request.retain_resources_shrink):
            query['retain_resources'] = request.retain_resources_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        cluster_id: str,
        request: cs20151215_models.DeleteClusterRequest,
    ) -> cs20151215_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_cluster_with_options(cluster_id, request, headers, runtime)

    async def delete_cluster_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DeleteClusterRequest,
    ) -> cs20151215_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_cluster_with_options_async(cluster_id, request, headers, runtime)

    def delete_cluster_nodepool_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.DeleteClusterNodepoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteClusterNodepoolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClusterNodepool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteClusterNodepoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_nodepool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.DeleteClusterNodepoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteClusterNodepoolResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClusterNodepool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteClusterNodepoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster_nodepool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.DeleteClusterNodepoolRequest,
    ) -> cs20151215_models.DeleteClusterNodepoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_cluster_nodepool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def delete_cluster_nodepool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.DeleteClusterNodepoolRequest,
    ) -> cs20151215_models.DeleteClusterNodepoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_cluster_nodepool_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def delete_cluster_nodes_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DeleteClusterNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteClusterNodesResponse:
        """
        >
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours. - The operation may have unexpected risks. Back up the data before you perform this operation. - When the system removes a node, it sets the status of the node to Unschedulable. - The system removes only worker nodes. It does not remove master nodes.
        
        @param request: DeleteClusterNodesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterNodesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drain_node):
            body['drain_node'] = request.drain_node
        if not UtilClient.is_unset(request.nodes):
            body['nodes'] = request.nodes
        if not UtilClient.is_unset(request.release_node):
            body['release_node'] = request.release_node
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteClusterNodes',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteClusterNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_nodes_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DeleteClusterNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteClusterNodesResponse:
        """
        >
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours. - The operation may have unexpected risks. Back up the data before you perform this operation. - When the system removes a node, it sets the status of the node to Unschedulable. - The system removes only worker nodes. It does not remove master nodes.
        
        @param request: DeleteClusterNodesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterNodesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drain_node):
            body['drain_node'] = request.drain_node
        if not UtilClient.is_unset(request.nodes):
            body['nodes'] = request.nodes
        if not UtilClient.is_unset(request.release_node):
            body['release_node'] = request.release_node
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteClusterNodes',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteClusterNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster_nodes(
        self,
        cluster_id: str,
        request: cs20151215_models.DeleteClusterNodesRequest,
    ) -> cs20151215_models.DeleteClusterNodesResponse:
        """
        >
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours. - The operation may have unexpected risks. Back up the data before you perform this operation. - When the system removes a node, it sets the status of the node to Unschedulable. - The system removes only worker nodes. It does not remove master nodes.
        
        @param request: DeleteClusterNodesRequest
        @return: DeleteClusterNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_cluster_nodes_with_options(cluster_id, request, headers, runtime)

    async def delete_cluster_nodes_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DeleteClusterNodesRequest,
    ) -> cs20151215_models.DeleteClusterNodesResponse:
        """
        >
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours. - The operation may have unexpected risks. Back up the data before you perform this operation. - When the system removes a node, it sets the status of the node to Unschedulable. - The system removes only worker nodes. It does not remove master nodes.
        
        @param request: DeleteClusterNodesRequest
        @return: DeleteClusterNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_cluster_nodes_with_options_async(cluster_id, request, headers, runtime)

    def delete_edge_machine_with_options(
        self,
        edge_machineid: str,
        request: cs20151215_models.DeleteEdgeMachineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteEdgeMachineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEdgeMachine',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/edge_machines/%5Bedge_machineid%5D',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteEdgeMachineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_edge_machine_with_options_async(
        self,
        edge_machineid: str,
        request: cs20151215_models.DeleteEdgeMachineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteEdgeMachineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['force'] = request.force
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEdgeMachine',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/edge_machines/%5Bedge_machineid%5D',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteEdgeMachineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_edge_machine(
        self,
        edge_machineid: str,
        request: cs20151215_models.DeleteEdgeMachineRequest,
    ) -> cs20151215_models.DeleteEdgeMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_edge_machine_with_options(edge_machineid, request, headers, runtime)

    async def delete_edge_machine_async(
        self,
        edge_machineid: str,
        request: cs20151215_models.DeleteEdgeMachineRequest,
    ) -> cs20151215_models.DeleteEdgeMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_edge_machine_with_options_async(edge_machineid, request, headers, runtime)

    def delete_kubernetes_trigger_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteKubernetesTriggerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteKubernetesTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/triggers/revoke/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteKubernetesTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_kubernetes_trigger_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteKubernetesTriggerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteKubernetesTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/triggers/revoke/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteKubernetesTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_kubernetes_trigger(
        self,
        id: str,
    ) -> cs20151215_models.DeleteKubernetesTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_kubernetes_trigger_with_options(id, headers, runtime)

    async def delete_kubernetes_trigger_async(
        self,
        id: str,
    ) -> cs20151215_models.DeleteKubernetesTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_kubernetes_trigger_with_options_async(id, headers, runtime)

    def delete_policy_instance_with_options(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.DeletePolicyInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeletePolicyInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['instance_name'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicyInstance',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/policies/{OpenApiUtilClient.get_encode_param(policy_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DeletePolicyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_instance_with_options_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.DeletePolicyInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeletePolicyInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['instance_name'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicyInstance',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/policies/{OpenApiUtilClient.get_encode_param(policy_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DeletePolicyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_instance(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.DeletePolicyInstanceRequest,
    ) -> cs20151215_models.DeletePolicyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_policy_instance_with_options(cluster_id, policy_name, request, headers, runtime)

    async def delete_policy_instance_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.DeletePolicyInstanceRequest,
    ) -> cs20151215_models.DeletePolicyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_policy_instance_with_options_async(cluster_id, policy_name, request, headers, runtime)

    def delete_template_with_options(
        self,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/templates/{OpenApiUtilClient.get_encode_param(template_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/templates/{OpenApiUtilClient.get_encode_param(template_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        template_id: str,
    ) -> cs20151215_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_template_with_options(template_id, headers, runtime)

    async def delete_template_async(
        self,
        template_id: str,
    ) -> cs20151215_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_template_with_options_async(template_id, headers, runtime)

    def delete_trigger_with_options(
        self,
        cluster_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteTriggerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/triggers/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_trigger_with_options_async(
        self,
        cluster_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeleteTriggerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/triggers/{OpenApiUtilClient.get_encode_param(id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.DeleteTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_trigger(
        self,
        cluster_id: str,
        id: str,
    ) -> cs20151215_models.DeleteTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_trigger_with_options(cluster_id, id, headers, runtime)

    async def delete_trigger_async(
        self,
        cluster_id: str,
        id: str,
    ) -> cs20151215_models.DeleteTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_trigger_with_options_async(cluster_id, id, headers, runtime)

    def deploy_policy_instance_with_options(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.DeployPolicyInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeployPolicyInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.namespaces):
            body['namespaces'] = request.namespaces
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployPolicyInstance',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/policies/{OpenApiUtilClient.get_encode_param(policy_name)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DeployPolicyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_policy_instance_with_options_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.DeployPolicyInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DeployPolicyInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.namespaces):
            body['namespaces'] = request.namespaces
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployPolicyInstance',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/policies/{OpenApiUtilClient.get_encode_param(policy_name)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DeployPolicyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_policy_instance(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.DeployPolicyInstanceRequest,
    ) -> cs20151215_models.DeployPolicyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deploy_policy_instance_with_options(cluster_id, policy_name, request, headers, runtime)

    async def deploy_policy_instance_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.DeployPolicyInstanceRequest,
    ) -> cs20151215_models.DeployPolicyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.deploy_policy_instance_with_options_async(cluster_id, policy_name, request, headers, runtime)

    def descirbe_workflow_with_options(
        self,
        workflow_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescirbeWorkflowResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescirbeWorkflow',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/gs/workflow/{OpenApiUtilClient.get_encode_param(workflow_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescirbeWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def descirbe_workflow_with_options_async(
        self,
        workflow_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescirbeWorkflowResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescirbeWorkflow',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/gs/workflow/{OpenApiUtilClient.get_encode_param(workflow_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescirbeWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def descirbe_workflow(
        self,
        workflow_name: str,
    ) -> cs20151215_models.DescirbeWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.descirbe_workflow_with_options(workflow_name, headers, runtime)

    async def descirbe_workflow_async(
        self,
        workflow_name: str,
    ) -> cs20151215_models.DescirbeWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.descirbe_workflow_with_options_async(workflow_name, headers, runtime)

    def describe_addon_with_options(
        self,
        addon_name: str,
        request: cs20151215_models.DescribeAddonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeAddonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.cluster_version):
            query['cluster_version'] = request.cluster_version
        if not UtilClient.is_unset(request.profile):
            query['profile'] = request.profile
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAddon',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/addons/{OpenApiUtilClient.get_encode_param(addon_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeAddonResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_addon_with_options_async(
        self,
        addon_name: str,
        request: cs20151215_models.DescribeAddonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeAddonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.cluster_version):
            query['cluster_version'] = request.cluster_version
        if not UtilClient.is_unset(request.profile):
            query['profile'] = request.profile
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAddon',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/addons/{OpenApiUtilClient.get_encode_param(addon_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeAddonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_addon(
        self,
        addon_name: str,
        request: cs20151215_models.DescribeAddonRequest,
    ) -> cs20151215_models.DescribeAddonResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_addon_with_options(addon_name, request, headers, runtime)

    async def describe_addon_async(
        self,
        addon_name: str,
        request: cs20151215_models.DescribeAddonRequest,
    ) -> cs20151215_models.DescribeAddonResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_addon_with_options_async(addon_name, request, headers, runtime)

    def describe_addons_with_options(
        self,
        request: cs20151215_models.DescribeAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeAddonsResponse:
        """
        @deprecated
        
        @param request: DescribeAddonsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAddonsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_profile):
            query['cluster_profile'] = request.cluster_profile
        if not UtilClient.is_unset(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.cluster_version):
            query['cluster_version'] = request.cluster_version
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAddons',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/components/metadata',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_addons_with_options_async(
        self,
        request: cs20151215_models.DescribeAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeAddonsResponse:
        """
        @deprecated
        
        @param request: DescribeAddonsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAddonsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_profile):
            query['cluster_profile'] = request.cluster_profile
        if not UtilClient.is_unset(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.cluster_version):
            query['cluster_version'] = request.cluster_version
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAddons',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/components/metadata',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_addons(
        self,
        request: cs20151215_models.DescribeAddonsRequest,
    ) -> cs20151215_models.DescribeAddonsResponse:
        """
        @deprecated
        
        @param request: DescribeAddonsRequest
        @return: DescribeAddonsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_addons_with_options(request, headers, runtime)

    async def describe_addons_async(
        self,
        request: cs20151215_models.DescribeAddonsRequest,
    ) -> cs20151215_models.DescribeAddonsResponse:
        """
        @deprecated
        
        @param request: DescribeAddonsRequest
        @return: DescribeAddonsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_addons_with_options_async(request, headers, runtime)

    def describe_cluster_addon_instance_with_options(
        self,
        cluster_id: str,
        addon_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonInstanceResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAddonInstanceResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterAddonInstance',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/{OpenApiUtilClient.get_encode_param(addon_name)}/instance',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_addon_instance_with_options_async(
        self,
        cluster_id: str,
        addon_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonInstanceResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAddonInstanceResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterAddonInstance',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/{OpenApiUtilClient.get_encode_param(addon_name)}/instance',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_addon_instance(
        self,
        cluster_id: str,
        addon_name: str,
    ) -> cs20151215_models.DescribeClusterAddonInstanceResponse:
        """
        @deprecated
        
        @return: DescribeClusterAddonInstanceResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_addon_instance_with_options(cluster_id, addon_name, headers, runtime)

    async def describe_cluster_addon_instance_async(
        self,
        cluster_id: str,
        addon_name: str,
    ) -> cs20151215_models.DescribeClusterAddonInstanceResponse:
        """
        @deprecated
        
        @return: DescribeClusterAddonInstanceResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_addon_instance_with_options_async(cluster_id, addon_name, headers, runtime)

    def describe_cluster_addon_metadata_with_options(
        self,
        cluster_id: str,
        component_id: str,
        version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonMetadataResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAddonMetadataResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterAddonMetadata',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/{OpenApiUtilClient.get_encode_param(component_id)}/metadata',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_addon_metadata_with_options_async(
        self,
        cluster_id: str,
        component_id: str,
        version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonMetadataResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAddonMetadataResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterAddonMetadata',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/{OpenApiUtilClient.get_encode_param(component_id)}/metadata',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_addon_metadata(
        self,
        cluster_id: str,
        component_id: str,
        version: str,
    ) -> cs20151215_models.DescribeClusterAddonMetadataResponse:
        """
        @deprecated
        
        @return: DescribeClusterAddonMetadataResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_addon_metadata_with_options(cluster_id, component_id, version, headers, runtime)

    async def describe_cluster_addon_metadata_async(
        self,
        cluster_id: str,
        component_id: str,
        version: str,
    ) -> cs20151215_models.DescribeClusterAddonMetadataResponse:
        """
        @deprecated
        
        @return: DescribeClusterAddonMetadataResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_addon_metadata_with_options_async(cluster_id, component_id, version, headers, runtime)

    def describe_cluster_addon_upgrade_status_with_options(
        self,
        cluster_id: str,
        component_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonUpgradeStatusResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAddonUpgradeStatusResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterAddonUpgradeStatus',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/{OpenApiUtilClient.get_encode_param(component_id)}/upgradestatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonUpgradeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_addon_upgrade_status_with_options_async(
        self,
        cluster_id: str,
        component_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonUpgradeStatusResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAddonUpgradeStatusResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterAddonUpgradeStatus',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/{OpenApiUtilClient.get_encode_param(component_id)}/upgradestatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonUpgradeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_addon_upgrade_status(
        self,
        cluster_id: str,
        component_id: str,
    ) -> cs20151215_models.DescribeClusterAddonUpgradeStatusResponse:
        """
        @deprecated
        
        @return: DescribeClusterAddonUpgradeStatusResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_addon_upgrade_status_with_options(cluster_id, component_id, headers, runtime)

    async def describe_cluster_addon_upgrade_status_async(
        self,
        cluster_id: str,
        component_id: str,
    ) -> cs20151215_models.DescribeClusterAddonUpgradeStatusResponse:
        """
        @deprecated
        
        @return: DescribeClusterAddonUpgradeStatusResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_addon_upgrade_status_with_options_async(cluster_id, component_id, headers, runtime)

    def describe_cluster_addons_upgrade_status_with_options(
        self,
        cluster_id: str,
        tmp_req: cs20151215_models.DescribeClusterAddonsUpgradeStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse:
        """
        @deprecated
        
        @param tmp_req: DescribeClusterAddonsUpgradeStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAddonsUpgradeStatusResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.DescribeClusterAddonsUpgradeStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.component_ids):
            request.component_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.component_ids, 'componentIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.component_ids_shrink):
            query['componentIds'] = request.component_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterAddonsUpgradeStatus',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/upgradestatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_addons_upgrade_status_with_options_async(
        self,
        cluster_id: str,
        tmp_req: cs20151215_models.DescribeClusterAddonsUpgradeStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse:
        """
        @deprecated
        
        @param tmp_req: DescribeClusterAddonsUpgradeStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAddonsUpgradeStatusResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.DescribeClusterAddonsUpgradeStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.component_ids):
            request.component_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.component_ids, 'componentIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.component_ids_shrink):
            query['componentIds'] = request.component_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterAddonsUpgradeStatus',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/upgradestatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_addons_upgrade_status(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterAddonsUpgradeStatusRequest,
    ) -> cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse:
        """
        @deprecated
        
        @param request: DescribeClusterAddonsUpgradeStatusRequest
        @return: DescribeClusterAddonsUpgradeStatusResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_addons_upgrade_status_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_addons_upgrade_status_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterAddonsUpgradeStatusRequest,
    ) -> cs20151215_models.DescribeClusterAddonsUpgradeStatusResponse:
        """
        @deprecated
        
        @param request: DescribeClusterAddonsUpgradeStatusRequest
        @return: DescribeClusterAddonsUpgradeStatusResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_addons_upgrade_status_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_addons_version_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonsVersionResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAddonsVersionResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterAddonsVersion',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/version',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonsVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_addons_version_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAddonsVersionResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterAddonsVersionResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterAddonsVersion',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/version',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAddonsVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_addons_version(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterAddonsVersionResponse:
        """
        @deprecated
        
        @return: DescribeClusterAddonsVersionResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_addons_version_with_options(cluster_id, headers, runtime)

    async def describe_cluster_addons_version_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterAddonsVersionResponse:
        """
        @deprecated
        
        @return: DescribeClusterAddonsVersionResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_addons_version_with_options_async(cluster_id, headers, runtime)

    def describe_cluster_attach_scripts_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterAttachScriptsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAttachScriptsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.arch):
            body['arch'] = request.arch
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.nodepool_id):
            body['nodepool_id'] = request.nodepool_id
        if not UtilClient.is_unset(request.options):
            body['options'] = request.options
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeClusterAttachScripts',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/attachscript',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAttachScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_attach_scripts_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterAttachScriptsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterAttachScriptsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.arch):
            body['arch'] = request.arch
        if not UtilClient.is_unset(request.format_disk):
            body['format_disk'] = request.format_disk
        if not UtilClient.is_unset(request.keep_instance_name):
            body['keep_instance_name'] = request.keep_instance_name
        if not UtilClient.is_unset(request.nodepool_id):
            body['nodepool_id'] = request.nodepool_id
        if not UtilClient.is_unset(request.options):
            body['options'] = request.options
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeClusterAttachScripts',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/attachscript',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='string'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterAttachScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_attach_scripts(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterAttachScriptsRequest,
    ) -> cs20151215_models.DescribeClusterAttachScriptsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_attach_scripts_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_attach_scripts_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterAttachScriptsRequest,
    ) -> cs20151215_models.DescribeClusterAttachScriptsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_attach_scripts_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_detail_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterDetailResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterDetail',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_detail_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterDetailResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterDetail',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_detail(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_detail_with_options(cluster_id, headers, runtime)

    async def describe_cluster_detail_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_detail_with_options_async(cluster_id, headers, runtime)

    def describe_cluster_events_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterEvents',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_events_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.task_id):
            query['task_id'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterEvents',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_events(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterEventsRequest,
    ) -> cs20151215_models.DescribeClusterEventsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_events_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_events_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterEventsRequest,
    ) -> cs20151215_models.DescribeClusterEventsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_events_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_logs_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterLogsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterLogs',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_logs_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterLogsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterLogs',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_logs(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_logs_with_options(cluster_id, headers, runtime)

    async def describe_cluster_logs_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterLogsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_logs_with_options_async(cluster_id, headers, runtime)

    def describe_cluster_node_pool_detail_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterNodePoolDetailResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterNodePoolDetail',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterNodePoolDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_node_pool_detail_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterNodePoolDetailResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterNodePoolDetail',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterNodePoolDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_node_pool_detail(
        self,
        cluster_id: str,
        nodepool_id: str,
    ) -> cs20151215_models.DescribeClusterNodePoolDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_node_pool_detail_with_options(cluster_id, nodepool_id, headers, runtime)

    async def describe_cluster_node_pool_detail_async(
        self,
        cluster_id: str,
        nodepool_id: str,
    ) -> cs20151215_models.DescribeClusterNodePoolDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_node_pool_detail_with_options_async(cluster_id, nodepool_id, headers, runtime)

    def describe_cluster_node_pools_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterNodePoolsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterNodePools',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterNodePoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_node_pools_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterNodePoolsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterNodePools',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterNodePoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_node_pools(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterNodePoolsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_node_pools_with_options(cluster_id, headers, runtime)

    async def describe_cluster_node_pools_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterNodePoolsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_node_pools_with_options_async(cluster_id, headers, runtime)

    def describe_cluster_nodes_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterNodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['instanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.nodepool_id):
            query['nodepool_id'] = request.nodepool_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterNodes',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_nodes_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterNodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['instanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.nodepool_id):
            query['nodepool_id'] = request.nodepool_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterNodes',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_nodes(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterNodesRequest,
    ) -> cs20151215_models.DescribeClusterNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_nodes_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_nodes_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterNodesRequest,
    ) -> cs20151215_models.DescribeClusterNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_nodes_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_resources_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterResourcesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterResources',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_resources_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterResourcesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterResources',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_resources(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_resources_with_options(cluster_id, headers, runtime)

    async def describe_cluster_resources_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_resources_with_options_async(cluster_id, headers, runtime)

    def describe_cluster_tasks_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterTasks',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_tasks_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterTasks',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_tasks(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterTasksRequest,
    ) -> cs20151215_models.DescribeClusterTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_tasks_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_tasks_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterTasksRequest,
    ) -> cs20151215_models.DescribeClusterTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_tasks_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_user_kubeconfig_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterUserKubeconfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterUserKubeconfigResponse:
        """
        *\
        ****The default validity period of a kubeconfig file is 3 years. Two months before a kubeconfig file expires, you can renew it in the Container Service for Kubernetes (ACK) console or by calling API operations. After a kubeconfig file is renewed, the secret is valid for 3 years. The previous kubeconfig secret remains valid until expiration. We recommend that you renew your kubeconfig file at the earliest opportunity.
        
        @param request: DescribeClusterUserKubeconfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterUserKubeconfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.temporary_duration_minutes):
            query['TemporaryDurationMinutes'] = request.temporary_duration_minutes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterUserKubeconfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/k8s/{OpenApiUtilClient.get_encode_param(cluster_id)}/user_config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterUserKubeconfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_user_kubeconfig_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterUserKubeconfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterUserKubeconfigResponse:
        """
        *\
        ****The default validity period of a kubeconfig file is 3 years. Two months before a kubeconfig file expires, you can renew it in the Container Service for Kubernetes (ACK) console or by calling API operations. After a kubeconfig file is renewed, the secret is valid for 3 years. The previous kubeconfig secret remains valid until expiration. We recommend that you renew your kubeconfig file at the earliest opportunity.
        
        @param request: DescribeClusterUserKubeconfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterUserKubeconfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.temporary_duration_minutes):
            query['TemporaryDurationMinutes'] = request.temporary_duration_minutes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterUserKubeconfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/k8s/{OpenApiUtilClient.get_encode_param(cluster_id)}/user_config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterUserKubeconfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_user_kubeconfig(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterUserKubeconfigRequest,
    ) -> cs20151215_models.DescribeClusterUserKubeconfigResponse:
        """
        *\
        ****The default validity period of a kubeconfig file is 3 years. Two months before a kubeconfig file expires, you can renew it in the Container Service for Kubernetes (ACK) console or by calling API operations. After a kubeconfig file is renewed, the secret is valid for 3 years. The previous kubeconfig secret remains valid until expiration. We recommend that you renew your kubeconfig file at the earliest opportunity.
        
        @param request: DescribeClusterUserKubeconfigRequest
        @return: DescribeClusterUserKubeconfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_user_kubeconfig_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_user_kubeconfig_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterUserKubeconfigRequest,
    ) -> cs20151215_models.DescribeClusterUserKubeconfigResponse:
        """
        *\
        ****The default validity period of a kubeconfig file is 3 years. Two months before a kubeconfig file expires, you can renew it in the Container Service for Kubernetes (ACK) console or by calling API operations. After a kubeconfig file is renewed, the secret is valid for 3 years. The previous kubeconfig secret remains valid until expiration. We recommend that you renew your kubeconfig file at the earliest opportunity.
        
        @param request: DescribeClusterUserKubeconfigRequest
        @return: DescribeClusterUserKubeconfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_user_kubeconfig_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_v2user_kubeconfig_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterV2UserKubeconfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterV2UserKubeconfigResponse:
        """
        @deprecated
        
        @param request: DescribeClusterV2UserKubeconfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterV2UserKubeconfigResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterV2UserKubeconfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/k8s/{OpenApiUtilClient.get_encode_param(cluster_id)}/user_config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterV2UserKubeconfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_v2user_kubeconfig_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterV2UserKubeconfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterV2UserKubeconfigResponse:
        """
        @deprecated
        
        @param request: DescribeClusterV2UserKubeconfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterV2UserKubeconfigResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterV2UserKubeconfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/k8s/{OpenApiUtilClient.get_encode_param(cluster_id)}/user_config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterV2UserKubeconfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_v2user_kubeconfig(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterV2UserKubeconfigRequest,
    ) -> cs20151215_models.DescribeClusterV2UserKubeconfigResponse:
        """
        @deprecated
        
        @param request: DescribeClusterV2UserKubeconfigRequest
        @return: DescribeClusterV2UserKubeconfigResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_v2user_kubeconfig_with_options(cluster_id, request, headers, runtime)

    async def describe_cluster_v2user_kubeconfig_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeClusterV2UserKubeconfigRequest,
    ) -> cs20151215_models.DescribeClusterV2UserKubeconfigResponse:
        """
        @deprecated
        
        @param request: DescribeClusterV2UserKubeconfigRequest
        @return: DescribeClusterV2UserKubeconfigResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_v2user_kubeconfig_with_options_async(cluster_id, request, headers, runtime)

    def describe_cluster_vuls_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterVulsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterVuls',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/vuls',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterVulsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_vuls_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClusterVulsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeClusterVuls',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/vuls',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClusterVulsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_vuls(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterVulsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_cluster_vuls_with_options(cluster_id, headers, runtime)

    async def describe_cluster_vuls_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeClusterVulsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_cluster_vuls_with_options_async(cluster_id, headers, runtime)

    def describe_clusters_with_options(
        self,
        request: cs20151215_models.DescribeClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClustersResponse:
        """
        @deprecated
        
        @param request: DescribeClustersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClustersResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['clusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusters',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_clusters_with_options_async(
        self,
        request: cs20151215_models.DescribeClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClustersResponse:
        """
        @deprecated
        
        @param request: DescribeClustersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClustersResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['clusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusters',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_clusters(
        self,
        request: cs20151215_models.DescribeClustersRequest,
    ) -> cs20151215_models.DescribeClustersResponse:
        """
        @deprecated
        
        @param request: DescribeClustersRequest
        @return: DescribeClustersResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_clusters_with_options(request, headers, runtime)

    async def describe_clusters_async(
        self,
        request: cs20151215_models.DescribeClustersRequest,
    ) -> cs20151215_models.DescribeClustersResponse:
        """
        @deprecated
        
        @param request: DescribeClustersRequest
        @return: DescribeClustersResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_clusters_with_options_async(request, headers, runtime)

    def describe_clusters_v1with_options(
        self,
        request: cs20151215_models.DescribeClustersV1Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClustersV1Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.profile):
            query['profile'] = request.profile
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClustersV1',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v1/clusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClustersV1Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_clusters_v1with_options_async(
        self,
        request: cs20151215_models.DescribeClustersV1Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeClustersV1Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.profile):
            query['profile'] = request.profile
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClustersV1',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v1/clusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeClustersV1Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_clusters_v1(
        self,
        request: cs20151215_models.DescribeClustersV1Request,
    ) -> cs20151215_models.DescribeClustersV1Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_clusters_v1with_options(request, headers, runtime)

    async def describe_clusters_v1_async(
        self,
        request: cs20151215_models.DescribeClustersV1Request,
    ) -> cs20151215_models.DescribeClustersV1Response:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_clusters_v1with_options_async(request, headers, runtime)

    def describe_edge_machine_active_process_with_options(
        self,
        edge_machineid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEdgeMachineActiveProcessResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeEdgeMachineActiveProcess',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/edge_machines/%5Bedge_machineid%5D/activeprocess',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeEdgeMachineActiveProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_edge_machine_active_process_with_options_async(
        self,
        edge_machineid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEdgeMachineActiveProcessResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeEdgeMachineActiveProcess',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/edge_machines/%5Bedge_machineid%5D/activeprocess',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeEdgeMachineActiveProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_edge_machine_active_process(
        self,
        edge_machineid: str,
    ) -> cs20151215_models.DescribeEdgeMachineActiveProcessResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_edge_machine_active_process_with_options(edge_machineid, headers, runtime)

    async def describe_edge_machine_active_process_async(
        self,
        edge_machineid: str,
    ) -> cs20151215_models.DescribeEdgeMachineActiveProcessResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_edge_machine_active_process_with_options_async(edge_machineid, headers, runtime)

    def describe_edge_machine_models_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEdgeMachineModelsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeEdgeMachineModels',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/edge_machines/models',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeEdgeMachineModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_edge_machine_models_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEdgeMachineModelsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeEdgeMachineModels',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/edge_machines/models',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeEdgeMachineModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_edge_machine_models(self) -> cs20151215_models.DescribeEdgeMachineModelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_edge_machine_models_with_options(headers, runtime)

    async def describe_edge_machine_models_async(self) -> cs20151215_models.DescribeEdgeMachineModelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_edge_machine_models_with_options_async(headers, runtime)

    def describe_edge_machine_tunnel_config_detail_with_options(
        self,
        edge_machineid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEdgeMachineTunnelConfigDetailResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeEdgeMachineTunnelConfigDetail',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/edge_machines/%5Bedge_machineid%5D/tunnelconfig',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeEdgeMachineTunnelConfigDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_edge_machine_tunnel_config_detail_with_options_async(
        self,
        edge_machineid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEdgeMachineTunnelConfigDetailResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeEdgeMachineTunnelConfigDetail',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/edge_machines/%5Bedge_machineid%5D/tunnelconfig',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeEdgeMachineTunnelConfigDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_edge_machine_tunnel_config_detail(
        self,
        edge_machineid: str,
    ) -> cs20151215_models.DescribeEdgeMachineTunnelConfigDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_edge_machine_tunnel_config_detail_with_options(edge_machineid, headers, runtime)

    async def describe_edge_machine_tunnel_config_detail_async(
        self,
        edge_machineid: str,
    ) -> cs20151215_models.DescribeEdgeMachineTunnelConfigDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_edge_machine_tunnel_config_detail_with_options_async(edge_machineid, headers, runtime)

    def describe_edge_machines_with_options(
        self,
        request: cs20151215_models.DescribeEdgeMachinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEdgeMachinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hostname):
            query['hostname'] = request.hostname
        if not UtilClient.is_unset(request.life_state):
            query['life_state'] = request.life_state
        if not UtilClient.is_unset(request.model):
            query['model'] = request.model
        if not UtilClient.is_unset(request.online_state):
            query['online_state'] = request.online_state
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEdgeMachines',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/edge_machines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeEdgeMachinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_edge_machines_with_options_async(
        self,
        request: cs20151215_models.DescribeEdgeMachinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEdgeMachinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hostname):
            query['hostname'] = request.hostname
        if not UtilClient.is_unset(request.life_state):
            query['life_state'] = request.life_state
        if not UtilClient.is_unset(request.model):
            query['model'] = request.model
        if not UtilClient.is_unset(request.online_state):
            query['online_state'] = request.online_state
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEdgeMachines',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/edge_machines',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeEdgeMachinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_edge_machines(
        self,
        request: cs20151215_models.DescribeEdgeMachinesRequest,
    ) -> cs20151215_models.DescribeEdgeMachinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_edge_machines_with_options(request, headers, runtime)

    async def describe_edge_machines_async(
        self,
        request: cs20151215_models.DescribeEdgeMachinesRequest,
    ) -> cs20151215_models.DescribeEdgeMachinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_edge_machines_with_options_async(request, headers, runtime)

    def describe_events_with_options(
        self,
        request: cs20151215_models.DescribeEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEvents',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_events_with_options_async(
        self,
        request: cs20151215_models.DescribeEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.page_number):
            query['page_number'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEvents',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/events',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_events(
        self,
        request: cs20151215_models.DescribeEventsRequest,
    ) -> cs20151215_models.DescribeEventsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_events_with_options(request, headers, runtime)

    async def describe_events_async(
        self,
        request: cs20151215_models.DescribeEventsRequest,
    ) -> cs20151215_models.DescribeEventsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_events_with_options_async(request, headers, runtime)

    def describe_external_agent_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeExternalAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeExternalAgentResponse:
        """
        For more information, see [Register an external Kubernetes cluster](~~121053~~).
        
        @param request: DescribeExternalAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExternalAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_mode):
            query['AgentMode'] = request.agent_mode
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExternalAgent',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/k8s/{OpenApiUtilClient.get_encode_param(cluster_id)}/external/agent/deployment',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeExternalAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_external_agent_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeExternalAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeExternalAgentResponse:
        """
        For more information, see [Register an external Kubernetes cluster](~~121053~~).
        
        @param request: DescribeExternalAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeExternalAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_mode):
            query['AgentMode'] = request.agent_mode
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExternalAgent',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/k8s/{OpenApiUtilClient.get_encode_param(cluster_id)}/external/agent/deployment',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeExternalAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_external_agent(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeExternalAgentRequest,
    ) -> cs20151215_models.DescribeExternalAgentResponse:
        """
        For more information, see [Register an external Kubernetes cluster](~~121053~~).
        
        @param request: DescribeExternalAgentRequest
        @return: DescribeExternalAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_external_agent_with_options(cluster_id, request, headers, runtime)

    async def describe_external_agent_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeExternalAgentRequest,
    ) -> cs20151215_models.DescribeExternalAgentResponse:
        """
        For more information, see [Register an external Kubernetes cluster](~~121053~~).
        
        @param request: DescribeExternalAgentRequest
        @return: DescribeExternalAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_external_agent_with_options_async(cluster_id, request, headers, runtime)

    def describe_kubernetes_version_metadata_with_options(
        self,
        request: cs20151215_models.DescribeKubernetesVersionMetadataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeKubernetesVersionMetadataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.kubernetes_version):
            query['KubernetesVersion'] = request.kubernetes_version
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.profile):
            query['Profile'] = request.profile
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.runtime):
            query['runtime'] = request.runtime
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKubernetesVersionMetadata',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v1/metadata/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeKubernetesVersionMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kubernetes_version_metadata_with_options_async(
        self,
        request: cs20151215_models.DescribeKubernetesVersionMetadataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeKubernetesVersionMetadataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.kubernetes_version):
            query['KubernetesVersion'] = request.kubernetes_version
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.profile):
            query['Profile'] = request.profile
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.runtime):
            query['runtime'] = request.runtime
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKubernetesVersionMetadata',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v1/metadata/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeKubernetesVersionMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kubernetes_version_metadata(
        self,
        request: cs20151215_models.DescribeKubernetesVersionMetadataRequest,
    ) -> cs20151215_models.DescribeKubernetesVersionMetadataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_kubernetes_version_metadata_with_options(request, headers, runtime)

    async def describe_kubernetes_version_metadata_async(
        self,
        request: cs20151215_models.DescribeKubernetesVersionMetadataRequest,
    ) -> cs20151215_models.DescribeKubernetesVersionMetadataResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_kubernetes_version_metadata_with_options_async(request, headers, runtime)

    def describe_node_pool_vuls_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.DescribeNodePoolVulsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeNodePoolVulsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.necessity):
            query['necessity'] = request.necessity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodePoolVuls',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}/vuls',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeNodePoolVulsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_node_pool_vuls_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.DescribeNodePoolVulsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeNodePoolVulsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.necessity):
            query['necessity'] = request.necessity
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodePoolVuls',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}/vuls',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeNodePoolVulsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_node_pool_vuls(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.DescribeNodePoolVulsRequest,
    ) -> cs20151215_models.DescribeNodePoolVulsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_node_pool_vuls_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def describe_node_pool_vuls_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.DescribeNodePoolVulsRequest,
    ) -> cs20151215_models.DescribeNodePoolVulsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_node_pool_vuls_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def describe_policies_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePoliciesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribePolicies',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/policies',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policies_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePoliciesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribePolicies',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/policies',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribePoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policies(self) -> cs20151215_models.DescribePoliciesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_policies_with_options(headers, runtime)

    async def describe_policies_async(self) -> cs20151215_models.DescribePoliciesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_policies_with_options_async(headers, runtime)

    def describe_policy_details_with_options(
        self,
        policy_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePolicyDetailsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribePolicyDetails',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/policies/{OpenApiUtilClient.get_encode_param(policy_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribePolicyDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_details_with_options_async(
        self,
        policy_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePolicyDetailsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribePolicyDetails',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/policies/{OpenApiUtilClient.get_encode_param(policy_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribePolicyDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy_details(
        self,
        policy_name: str,
    ) -> cs20151215_models.DescribePolicyDetailsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_policy_details_with_options(policy_name, headers, runtime)

    async def describe_policy_details_async(
        self,
        policy_name: str,
    ) -> cs20151215_models.DescribePolicyDetailsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_policy_details_with_options_async(policy_name, headers, runtime)

    def describe_policy_governance_in_cluster_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePolicyGovernanceInClusterResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribePolicyGovernanceInCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/policygovernance',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribePolicyGovernanceInClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_governance_in_cluster_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePolicyGovernanceInClusterResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribePolicyGovernanceInCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/policygovernance',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribePolicyGovernanceInClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy_governance_in_cluster(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribePolicyGovernanceInClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_policy_governance_in_cluster_with_options(cluster_id, headers, runtime)

    async def describe_policy_governance_in_cluster_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribePolicyGovernanceInClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_policy_governance_in_cluster_with_options_async(cluster_id, headers, runtime)

    def describe_policy_instances_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribePolicyInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePolicyInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['instance_name'] = request.instance_name
        if not UtilClient.is_unset(request.policy_name):
            query['policy_name'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyInstances',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/policies',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribePolicyInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_instances_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribePolicyInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePolicyInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['instance_name'] = request.instance_name
        if not UtilClient.is_unset(request.policy_name):
            query['policy_name'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyInstances',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/policies',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribePolicyInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy_instances(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribePolicyInstancesRequest,
    ) -> cs20151215_models.DescribePolicyInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_policy_instances_with_options(cluster_id, request, headers, runtime)

    async def describe_policy_instances_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribePolicyInstancesRequest,
    ) -> cs20151215_models.DescribePolicyInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_policy_instances_with_options_async(cluster_id, request, headers, runtime)

    def describe_policy_instances_status_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePolicyInstancesStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribePolicyInstancesStatus',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/policies/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribePolicyInstancesStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_instances_status_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribePolicyInstancesStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribePolicyInstancesStatus',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/policies/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribePolicyInstancesStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy_instances_status(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribePolicyInstancesStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_policy_instances_status_with_options(cluster_id, headers, runtime)

    async def describe_policy_instances_status_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribePolicyInstancesStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_policy_instances_status_with_options_async(cluster_id, headers, runtime)

    def describe_subaccount_k8s_cluster_user_config_with_options(
        self,
        cluster_id: str,
        uid: str,
        request: cs20151215_models.DescribeSubaccountK8sClusterUserConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeSubaccountK8sClusterUserConfigResponse:
        """
        *\
        ****Only Alibaba Cloud accounts can call this API operation.
        
        @param request: DescribeSubaccountK8sClusterUserConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubaccountK8sClusterUserConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.temporary_duration_minutes):
            query['TemporaryDurationMinutes'] = request.temporary_duration_minutes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubaccountK8sClusterUserConfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/k8s/{OpenApiUtilClient.get_encode_param(cluster_id)}/users/{OpenApiUtilClient.get_encode_param(uid)}/user_config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeSubaccountK8sClusterUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_subaccount_k8s_cluster_user_config_with_options_async(
        self,
        cluster_id: str,
        uid: str,
        request: cs20151215_models.DescribeSubaccountK8sClusterUserConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeSubaccountK8sClusterUserConfigResponse:
        """
        *\
        ****Only Alibaba Cloud accounts can call this API operation.
        
        @param request: DescribeSubaccountK8sClusterUserConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSubaccountK8sClusterUserConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.temporary_duration_minutes):
            query['TemporaryDurationMinutes'] = request.temporary_duration_minutes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubaccountK8sClusterUserConfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/k8s/{OpenApiUtilClient.get_encode_param(cluster_id)}/users/{OpenApiUtilClient.get_encode_param(uid)}/user_config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeSubaccountK8sClusterUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_subaccount_k8s_cluster_user_config(
        self,
        cluster_id: str,
        uid: str,
        request: cs20151215_models.DescribeSubaccountK8sClusterUserConfigRequest,
    ) -> cs20151215_models.DescribeSubaccountK8sClusterUserConfigResponse:
        """
        *\
        ****Only Alibaba Cloud accounts can call this API operation.
        
        @param request: DescribeSubaccountK8sClusterUserConfigRequest
        @return: DescribeSubaccountK8sClusterUserConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_subaccount_k8s_cluster_user_config_with_options(cluster_id, uid, request, headers, runtime)

    async def describe_subaccount_k8s_cluster_user_config_async(
        self,
        cluster_id: str,
        uid: str,
        request: cs20151215_models.DescribeSubaccountK8sClusterUserConfigRequest,
    ) -> cs20151215_models.DescribeSubaccountK8sClusterUserConfigResponse:
        """
        *\
        ****Only Alibaba Cloud accounts can call this API operation.
        
        @param request: DescribeSubaccountK8sClusterUserConfigRequest
        @return: DescribeSubaccountK8sClusterUserConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_subaccount_k8s_cluster_user_config_with_options_async(cluster_id, uid, request, headers, runtime)

    def describe_task_info_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeTaskInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeTaskInfo',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_task_info_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeTaskInfoResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeTaskInfo',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_task_info(
        self,
        task_id: str,
    ) -> cs20151215_models.DescribeTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_task_info_with_options(task_id, headers, runtime)

    async def describe_task_info_async(
        self,
        task_id: str,
    ) -> cs20151215_models.DescribeTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_task_info_with_options_async(task_id, headers, runtime)

    def describe_template_attribute_with_options(
        self,
        template_id: str,
        request: cs20151215_models.DescribeTemplateAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeTemplateAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_type):
            query['template_type'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplateAttribute',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/templates/{OpenApiUtilClient.get_encode_param(template_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeTemplateAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_template_attribute_with_options_async(
        self,
        template_id: str,
        request: cs20151215_models.DescribeTemplateAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeTemplateAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_type):
            query['template_type'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplateAttribute',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/templates/{OpenApiUtilClient.get_encode_param(template_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeTemplateAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_template_attribute(
        self,
        template_id: str,
        request: cs20151215_models.DescribeTemplateAttributeRequest,
    ) -> cs20151215_models.DescribeTemplateAttributeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_template_attribute_with_options(template_id, request, headers, runtime)

    async def describe_template_attribute_async(
        self,
        template_id: str,
        request: cs20151215_models.DescribeTemplateAttributeRequest,
    ) -> cs20151215_models.DescribeTemplateAttributeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_template_attribute_with_options_async(template_id, request, headers, runtime)

    def describe_templates_with_options(
        self,
        request: cs20151215_models.DescribeTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['page_num'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.template_type):
            query['template_type'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplates',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/templates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_templates_with_options_async(
        self,
        request: cs20151215_models.DescribeTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['page_num'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['page_size'] = request.page_size
        if not UtilClient.is_unset(request.template_type):
            query['template_type'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplates',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/templates',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_templates(
        self,
        request: cs20151215_models.DescribeTemplatesRequest,
    ) -> cs20151215_models.DescribeTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_templates_with_options(request, headers, runtime)

    async def describe_templates_async(
        self,
        request: cs20151215_models.DescribeTemplatesRequest,
    ) -> cs20151215_models.DescribeTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_templates_with_options_async(request, headers, runtime)

    def describe_trigger_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/triggers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_trigger_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/triggers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_trigger(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeTriggerRequest,
    ) -> cs20151215_models.DescribeTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_trigger_with_options(cluster_id, request, headers, runtime)

    async def describe_trigger_async(
        self,
        cluster_id: str,
        request: cs20151215_models.DescribeTriggerRequest,
    ) -> cs20151215_models.DescribeTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_trigger_with_options_async(cluster_id, request, headers, runtime)

    def describe_user_cluster_namespaces_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeUserClusterNamespacesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeUserClusterNamespaces',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/k8s/{OpenApiUtilClient.get_encode_param(cluster_id)}/namespaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeUserClusterNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_cluster_namespaces_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeUserClusterNamespacesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeUserClusterNamespaces',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/k8s/{OpenApiUtilClient.get_encode_param(cluster_id)}/namespaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeUserClusterNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_cluster_namespaces(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeUserClusterNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_user_cluster_namespaces_with_options(cluster_id, headers, runtime)

    async def describe_user_cluster_namespaces_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.DescribeUserClusterNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_user_cluster_namespaces_with_options_async(cluster_id, headers, runtime)

    def describe_user_permission_with_options(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeUserPermissionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeUserPermission',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/permissions/users/{OpenApiUtilClient.get_encode_param(uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeUserPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_permission_with_options_async(
        self,
        uid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeUserPermissionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeUserPermission',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/permissions/users/{OpenApiUtilClient.get_encode_param(uid)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeUserPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_permission(
        self,
        uid: str,
    ) -> cs20151215_models.DescribeUserPermissionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_user_permission_with_options(uid, headers, runtime)

    async def describe_user_permission_async(
        self,
        uid: str,
    ) -> cs20151215_models.DescribeUserPermissionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_user_permission_with_options_async(uid, headers, runtime)

    def describe_user_quota_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeUserQuotaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeUserQuota',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/quota',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_quota_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeUserQuotaResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeUserQuota',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/quota',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeUserQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_quota(self) -> cs20151215_models.DescribeUserQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_user_quota_with_options(headers, runtime)

    async def describe_user_quota_async(self) -> cs20151215_models.DescribeUserQuotaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_user_quota_with_options_async(headers, runtime)

    def describe_workflows_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeWorkflowsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeWorkflows',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/gs/workflows',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeWorkflowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_workflows_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.DescribeWorkflowsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeWorkflows',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/gs/workflows',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.DescribeWorkflowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_workflows(self) -> cs20151215_models.DescribeWorkflowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_workflows_with_options(headers, runtime)

    async def describe_workflows_async(self) -> cs20151215_models.DescribeWorkflowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_workflows_with_options_async(headers, runtime)

    def edge_cluster_add_edge_machine_with_options(
        self,
        clusterid: str,
        edge_machineid: str,
        request: cs20151215_models.EdgeClusterAddEdgeMachineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.EdgeClusterAddEdgeMachineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.expired):
            body['expired'] = request.expired
        if not UtilClient.is_unset(request.nodepool_id):
            body['nodepool_id'] = request.nodepool_id
        if not UtilClient.is_unset(request.options):
            body['options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EdgeClusterAddEdgeMachine',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/%5Bclusterid%5D/attachedgemachine/%5Bedge_machineid%5D',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.EdgeClusterAddEdgeMachineResponse(),
            self.call_api(params, req, runtime)
        )

    async def edge_cluster_add_edge_machine_with_options_async(
        self,
        clusterid: str,
        edge_machineid: str,
        request: cs20151215_models.EdgeClusterAddEdgeMachineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.EdgeClusterAddEdgeMachineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.expired):
            body['expired'] = request.expired
        if not UtilClient.is_unset(request.nodepool_id):
            body['nodepool_id'] = request.nodepool_id
        if not UtilClient.is_unset(request.options):
            body['options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EdgeClusterAddEdgeMachine',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/%5Bclusterid%5D/attachedgemachine/%5Bedge_machineid%5D',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.EdgeClusterAddEdgeMachineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edge_cluster_add_edge_machine(
        self,
        clusterid: str,
        edge_machineid: str,
        request: cs20151215_models.EdgeClusterAddEdgeMachineRequest,
    ) -> cs20151215_models.EdgeClusterAddEdgeMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.edge_cluster_add_edge_machine_with_options(clusterid, edge_machineid, request, headers, runtime)

    async def edge_cluster_add_edge_machine_async(
        self,
        clusterid: str,
        edge_machineid: str,
        request: cs20151215_models.EdgeClusterAddEdgeMachineRequest,
    ) -> cs20151215_models.EdgeClusterAddEdgeMachineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.edge_cluster_add_edge_machine_with_options_async(clusterid, edge_machineid, request, headers, runtime)

    def fix_node_pool_vuls_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.FixNodePoolVulsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.FixNodePoolVulsResponse:
        """
        1.  The Common Vulnerabilities and Exposures (CVE) patching feature is developed based on Security Center. To use this feature, you must purchase the Security Center Ultimate Edition that supports Container Service for Kubernetes (ACK).
        2.  ACK may need to restart nodes to patch certain vulnerabilities. ACK drains a node before the node restarts. Make sure that the ACK cluster has sufficient idle nodes to host the pods evicted from the trained nodes. For example, you can scale out a node pool before you patch vulnerabilities for the nodes in the node pool.
        3.  Security Center ensures the compatibility of CVE patches. We recommend that you check the compatibility of a CVE patch with your application before you install the patch. You can pause or cancel a CVE patching task anytime.
        4.  CVE patching is a progressive task that consists of multiple batches. After you pause or cancel a CVE patching task, ACK continues to process the dispatched batches. Only the batches that have not been dispatched are paused or canceled.
        
        @param request: FixNodePoolVulsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FixNodePoolVulsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_restart):
            body['auto_restart'] = request.auto_restart
        if not UtilClient.is_unset(request.nodes):
            body['nodes'] = request.nodes
        if not UtilClient.is_unset(request.rollout_policy):
            body['rollout_policy'] = request.rollout_policy
        if not UtilClient.is_unset(request.vuls):
            body['vuls'] = request.vuls
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FixNodePoolVuls',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}/vuls/fix',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.FixNodePoolVulsResponse(),
            self.call_api(params, req, runtime)
        )

    async def fix_node_pool_vuls_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.FixNodePoolVulsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.FixNodePoolVulsResponse:
        """
        1.  The Common Vulnerabilities and Exposures (CVE) patching feature is developed based on Security Center. To use this feature, you must purchase the Security Center Ultimate Edition that supports Container Service for Kubernetes (ACK).
        2.  ACK may need to restart nodes to patch certain vulnerabilities. ACK drains a node before the node restarts. Make sure that the ACK cluster has sufficient idle nodes to host the pods evicted from the trained nodes. For example, you can scale out a node pool before you patch vulnerabilities for the nodes in the node pool.
        3.  Security Center ensures the compatibility of CVE patches. We recommend that you check the compatibility of a CVE patch with your application before you install the patch. You can pause or cancel a CVE patching task anytime.
        4.  CVE patching is a progressive task that consists of multiple batches. After you pause or cancel a CVE patching task, ACK continues to process the dispatched batches. Only the batches that have not been dispatched are paused or canceled.
        
        @param request: FixNodePoolVulsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FixNodePoolVulsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_restart):
            body['auto_restart'] = request.auto_restart
        if not UtilClient.is_unset(request.nodes):
            body['nodes'] = request.nodes
        if not UtilClient.is_unset(request.rollout_policy):
            body['rollout_policy'] = request.rollout_policy
        if not UtilClient.is_unset(request.vuls):
            body['vuls'] = request.vuls
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FixNodePoolVuls',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}/vuls/fix',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.FixNodePoolVulsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fix_node_pool_vuls(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.FixNodePoolVulsRequest,
    ) -> cs20151215_models.FixNodePoolVulsResponse:
        """
        1.  The Common Vulnerabilities and Exposures (CVE) patching feature is developed based on Security Center. To use this feature, you must purchase the Security Center Ultimate Edition that supports Container Service for Kubernetes (ACK).
        2.  ACK may need to restart nodes to patch certain vulnerabilities. ACK drains a node before the node restarts. Make sure that the ACK cluster has sufficient idle nodes to host the pods evicted from the trained nodes. For example, you can scale out a node pool before you patch vulnerabilities for the nodes in the node pool.
        3.  Security Center ensures the compatibility of CVE patches. We recommend that you check the compatibility of a CVE patch with your application before you install the patch. You can pause or cancel a CVE patching task anytime.
        4.  CVE patching is a progressive task that consists of multiple batches. After you pause or cancel a CVE patching task, ACK continues to process the dispatched batches. Only the batches that have not been dispatched are paused or canceled.
        
        @param request: FixNodePoolVulsRequest
        @return: FixNodePoolVulsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.fix_node_pool_vuls_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def fix_node_pool_vuls_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.FixNodePoolVulsRequest,
    ) -> cs20151215_models.FixNodePoolVulsResponse:
        """
        1.  The Common Vulnerabilities and Exposures (CVE) patching feature is developed based on Security Center. To use this feature, you must purchase the Security Center Ultimate Edition that supports Container Service for Kubernetes (ACK).
        2.  ACK may need to restart nodes to patch certain vulnerabilities. ACK drains a node before the node restarts. Make sure that the ACK cluster has sufficient idle nodes to host the pods evicted from the trained nodes. For example, you can scale out a node pool before you patch vulnerabilities for the nodes in the node pool.
        3.  Security Center ensures the compatibility of CVE patches. We recommend that you check the compatibility of a CVE patch with your application before you install the patch. You can pause or cancel a CVE patching task anytime.
        4.  CVE patching is a progressive task that consists of multiple batches. After you pause or cancel a CVE patching task, ACK continues to process the dispatched batches. Only the batches that have not been dispatched are paused or canceled.
        
        @param request: FixNodePoolVulsRequest
        @return: FixNodePoolVulsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.fix_node_pool_vuls_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def get_cluster_addon_instance_with_options(
        self,
        cluster_id: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetClusterAddonInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetClusterAddonInstance',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/addon_instances/{OpenApiUtilClient.get_encode_param(instance_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.GetClusterAddonInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_addon_instance_with_options_async(
        self,
        cluster_id: str,
        instance_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetClusterAddonInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetClusterAddonInstance',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/addon_instances/{OpenApiUtilClient.get_encode_param(instance_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.GetClusterAddonInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_addon_instance(
        self,
        cluster_id: str,
        instance_name: str,
    ) -> cs20151215_models.GetClusterAddonInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_addon_instance_with_options(cluster_id, instance_name, headers, runtime)

    async def get_cluster_addon_instance_async(
        self,
        cluster_id: str,
        instance_name: str,
    ) -> cs20151215_models.GetClusterAddonInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cluster_addon_instance_with_options_async(cluster_id, instance_name, headers, runtime)

    def get_cluster_check_with_options(
        self,
        cluster_id: str,
        check_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetClusterCheckResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetClusterCheck',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/checks/{OpenApiUtilClient.get_encode_param(check_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.GetClusterCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_check_with_options_async(
        self,
        cluster_id: str,
        check_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetClusterCheckResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetClusterCheck',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/checks/{OpenApiUtilClient.get_encode_param(check_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.GetClusterCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_check(
        self,
        cluster_id: str,
        check_id: str,
    ) -> cs20151215_models.GetClusterCheckResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_check_with_options(cluster_id, check_id, headers, runtime)

    async def get_cluster_check_async(
        self,
        cluster_id: str,
        check_id: str,
    ) -> cs20151215_models.GetClusterCheckResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cluster_check_with_options_async(cluster_id, check_id, headers, runtime)

    def get_kubernetes_trigger_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.GetKubernetesTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetKubernetesTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetKubernetesTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/triggers/{OpenApiUtilClient.get_encode_param(cluster_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.GetKubernetesTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_kubernetes_trigger_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.GetKubernetesTriggerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetKubernetesTriggerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.action):
            query['action'] = request.action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetKubernetesTrigger',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/triggers/{OpenApiUtilClient.get_encode_param(cluster_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='array'
        )
        return TeaCore.from_map(
            cs20151215_models.GetKubernetesTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_kubernetes_trigger(
        self,
        cluster_id: str,
        request: cs20151215_models.GetKubernetesTriggerRequest,
    ) -> cs20151215_models.GetKubernetesTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_kubernetes_trigger_with_options(cluster_id, request, headers, runtime)

    async def get_kubernetes_trigger_async(
        self,
        cluster_id: str,
        request: cs20151215_models.GetKubernetesTriggerRequest,
    ) -> cs20151215_models.GetKubernetesTriggerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_kubernetes_trigger_with_options_async(cluster_id, request, headers, runtime)

    def get_upgrade_status_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetUpgradeStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUpgradeStatus',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/upgrade/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.GetUpgradeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upgrade_status_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GetUpgradeStatusResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUpgradeStatus',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/upgrade/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.GetUpgradeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upgrade_status(
        self,
        cluster_id: str,
    ) -> cs20151215_models.GetUpgradeStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_upgrade_status_with_options(cluster_id, headers, runtime)

    async def get_upgrade_status_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.GetUpgradeStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_upgrade_status_with_options_async(cluster_id, headers, runtime)

    def grant_permissions_with_options(
        self,
        uid: str,
        request: cs20151215_models.GrantPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GrantPermissionsResponse:
        """
        ***\
        *   Make sure that you have granted the RAM user at least read-only permissions on the desired ACK clusters in the RAM console. Otherwise, the `ErrorRamPolicyConfig` error code is returned. For more information about how to authorize a RAM user by attaching RAM policies, see [Create a custom RAM policy](~~86485~~).
        *   If you use a RAM user to call this API operation, make sure that the RAM user is authorized to modify the permissions of other RAM users on the desired ACK clusters. Otherwise, the `StatusForbidden` or `ForbiddenGrantPermissions` error code is returned. For more information, see [Use a RAM user to grant RBAC permissions to other RAM users](~~119035~~).
        *   This operation overwrites the permissions that have been granted to the specified RAM user. When you call this operation, make sure that the required permissions are included.
        
        @param request: GrantPermissionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantPermissionsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='GrantPermissions',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/permissions/users/{OpenApiUtilClient.get_encode_param(uid)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.GrantPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_permissions_with_options_async(
        self,
        uid: str,
        request: cs20151215_models.GrantPermissionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.GrantPermissionsResponse:
        """
        ***\
        *   Make sure that you have granted the RAM user at least read-only permissions on the desired ACK clusters in the RAM console. Otherwise, the `ErrorRamPolicyConfig` error code is returned. For more information about how to authorize a RAM user by attaching RAM policies, see [Create a custom RAM policy](~~86485~~).
        *   If you use a RAM user to call this API operation, make sure that the RAM user is authorized to modify the permissions of other RAM users on the desired ACK clusters. Otherwise, the `StatusForbidden` or `ForbiddenGrantPermissions` error code is returned. For more information, see [Use a RAM user to grant RBAC permissions to other RAM users](~~119035~~).
        *   This operation overwrites the permissions that have been granted to the specified RAM user. When you call this operation, make sure that the required permissions are included.
        
        @param request: GrantPermissionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantPermissionsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='GrantPermissions',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/permissions/users/{OpenApiUtilClient.get_encode_param(uid)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.GrantPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_permissions(
        self,
        uid: str,
        request: cs20151215_models.GrantPermissionsRequest,
    ) -> cs20151215_models.GrantPermissionsResponse:
        """
        ***\
        *   Make sure that you have granted the RAM user at least read-only permissions on the desired ACK clusters in the RAM console. Otherwise, the `ErrorRamPolicyConfig` error code is returned. For more information about how to authorize a RAM user by attaching RAM policies, see [Create a custom RAM policy](~~86485~~).
        *   If you use a RAM user to call this API operation, make sure that the RAM user is authorized to modify the permissions of other RAM users on the desired ACK clusters. Otherwise, the `StatusForbidden` or `ForbiddenGrantPermissions` error code is returned. For more information, see [Use a RAM user to grant RBAC permissions to other RAM users](~~119035~~).
        *   This operation overwrites the permissions that have been granted to the specified RAM user. When you call this operation, make sure that the required permissions are included.
        
        @param request: GrantPermissionsRequest
        @return: GrantPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.grant_permissions_with_options(uid, request, headers, runtime)

    async def grant_permissions_async(
        self,
        uid: str,
        request: cs20151215_models.GrantPermissionsRequest,
    ) -> cs20151215_models.GrantPermissionsResponse:
        """
        ***\
        *   Make sure that you have granted the RAM user at least read-only permissions on the desired ACK clusters in the RAM console. Otherwise, the `ErrorRamPolicyConfig` error code is returned. For more information about how to authorize a RAM user by attaching RAM policies, see [Create a custom RAM policy](~~86485~~).
        *   If you use a RAM user to call this API operation, make sure that the RAM user is authorized to modify the permissions of other RAM users on the desired ACK clusters. Otherwise, the `StatusForbidden` or `ForbiddenGrantPermissions` error code is returned. For more information, see [Use a RAM user to grant RBAC permissions to other RAM users](~~119035~~).
        *   This operation overwrites the permissions that have been granted to the specified RAM user. When you call this operation, make sure that the required permissions are included.
        
        @param request: GrantPermissionsRequest
        @return: GrantPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.grant_permissions_with_options_async(uid, request, headers, runtime)

    def install_cluster_addons_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.InstallClusterAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.InstallClusterAddonsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='InstallClusterAddons',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/install',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.InstallClusterAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_cluster_addons_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.InstallClusterAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.InstallClusterAddonsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='InstallClusterAddons',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/install',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.InstallClusterAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_cluster_addons(
        self,
        cluster_id: str,
        request: cs20151215_models.InstallClusterAddonsRequest,
    ) -> cs20151215_models.InstallClusterAddonsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_cluster_addons_with_options(cluster_id, request, headers, runtime)

    async def install_cluster_addons_async(
        self,
        cluster_id: str,
        request: cs20151215_models.InstallClusterAddonsRequest,
    ) -> cs20151215_models.InstallClusterAddonsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.install_cluster_addons_with_options_async(cluster_id, request, headers, runtime)

    def list_addons_with_options(
        self,
        request: cs20151215_models.ListAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListAddonsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.cluster_version):
            query['cluster_version'] = request.cluster_version
        if not UtilClient.is_unset(request.profile):
            query['profile'] = request.profile
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddons',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/addons',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ListAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addons_with_options_async(
        self,
        request: cs20151215_models.ListAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListAddonsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_spec):
            query['cluster_spec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cluster_type):
            query['cluster_type'] = request.cluster_type
        if not UtilClient.is_unset(request.cluster_version):
            query['cluster_version'] = request.cluster_version
        if not UtilClient.is_unset(request.profile):
            query['profile'] = request.profile
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddons',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/addons',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ListAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_addons(
        self,
        request: cs20151215_models.ListAddonsRequest,
    ) -> cs20151215_models.ListAddonsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_addons_with_options(request, headers, runtime)

    async def list_addons_async(
        self,
        request: cs20151215_models.ListAddonsRequest,
    ) -> cs20151215_models.ListAddonsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_addons_with_options_async(request, headers, runtime)

    def list_cluster_addon_instances_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListClusterAddonInstancesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListClusterAddonInstances',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/addon_instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ListClusterAddonInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_addon_instances_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListClusterAddonInstancesResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListClusterAddonInstances',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/addon_instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ListClusterAddonInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_addon_instances(
        self,
        cluster_id: str,
    ) -> cs20151215_models.ListClusterAddonInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_cluster_addon_instances_with_options(cluster_id, headers, runtime)

    async def list_cluster_addon_instances_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.ListClusterAddonInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_cluster_addon_instances_with_options_async(cluster_id, headers, runtime)

    def list_cluster_checks_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.ListClusterChecksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListClusterChecksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterChecks',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/checks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ListClusterChecksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_checks_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ListClusterChecksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListClusterChecksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterChecks',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/checks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ListClusterChecksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_checks(
        self,
        cluster_id: str,
        request: cs20151215_models.ListClusterChecksRequest,
    ) -> cs20151215_models.ListClusterChecksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_cluster_checks_with_options(cluster_id, request, headers, runtime)

    async def list_cluster_checks_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ListClusterChecksRequest,
    ) -> cs20151215_models.ListClusterChecksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_cluster_checks_with_options_async(cluster_id, request, headers, runtime)

    def list_operation_plans_with_options(
        self,
        request: cs20151215_models.ListOperationPlansRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListOperationPlansResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOperationPlans',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/operation/plans',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ListOperationPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_operation_plans_with_options_async(
        self,
        request: cs20151215_models.ListOperationPlansRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListOperationPlansResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['cluster_id'] = request.cluster_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOperationPlans',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/operation/plans',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ListOperationPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_operation_plans(
        self,
        request: cs20151215_models.ListOperationPlansRequest,
    ) -> cs20151215_models.ListOperationPlansResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_operation_plans_with_options(request, headers, runtime)

    async def list_operation_plans_async(
        self,
        request: cs20151215_models.ListOperationPlansRequest,
    ) -> cs20151215_models.ListOperationPlansResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_operation_plans_with_options_async(request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: cs20151215_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListTagResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'resource_ids', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['next_token'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['resource_ids'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resource_type'] = request.resource_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: cs20151215_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ListTagResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'resource_ids', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['next_token'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['resource_ids'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resource_type'] = request.resource_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: cs20151215_models.ListTagResourcesRequest,
    ) -> cs20151215_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: cs20151215_models.ListTagResourcesRequest,
    ) -> cs20151215_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def migrate_cluster_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.MigrateClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.MigrateClusterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.oss_bucket_endpoint):
            body['oss_bucket_endpoint'] = request.oss_bucket_endpoint
        if not UtilClient.is_unset(request.oss_bucket_name):
            body['oss_bucket_name'] = request.oss_bucket_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MigrateCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/migrate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.MigrateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_cluster_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.MigrateClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.MigrateClusterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.oss_bucket_endpoint):
            body['oss_bucket_endpoint'] = request.oss_bucket_endpoint
        if not UtilClient.is_unset(request.oss_bucket_name):
            body['oss_bucket_name'] = request.oss_bucket_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MigrateCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/migrate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.MigrateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_cluster(
        self,
        cluster_id: str,
        request: cs20151215_models.MigrateClusterRequest,
    ) -> cs20151215_models.MigrateClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.migrate_cluster_with_options(cluster_id, request, headers, runtime)

    async def migrate_cluster_async(
        self,
        cluster_id: str,
        request: cs20151215_models.MigrateClusterRequest,
    ) -> cs20151215_models.MigrateClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.migrate_cluster_with_options_async(cluster_id, request, headers, runtime)

    def modify_cluster_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyClusterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_control_list):
            body['access_control_list'] = request.access_control_list
        if not UtilClient.is_unset(request.api_server_eip):
            body['api_server_eip'] = request.api_server_eip
        if not UtilClient.is_unset(request.api_server_eip_id):
            body['api_server_eip_id'] = request.api_server_eip_id
        if not UtilClient.is_unset(request.cluster_name):
            body['cluster_name'] = request.cluster_name
        if not UtilClient.is_unset(request.deletion_protection):
            body['deletion_protection'] = request.deletion_protection
        if not UtilClient.is_unset(request.enable_rrsa):
            body['enable_rrsa'] = request.enable_rrsa
        if not UtilClient.is_unset(request.ingress_domain_rebinding):
            body['ingress_domain_rebinding'] = request.ingress_domain_rebinding
        if not UtilClient.is_unset(request.ingress_loadbalancer_id):
            body['ingress_loadbalancer_id'] = request.ingress_loadbalancer_id
        if not UtilClient.is_unset(request.instance_deletion_protection):
            body['instance_deletion_protection'] = request.instance_deletion_protection
        if not UtilClient.is_unset(request.maintenance_window):
            body['maintenance_window'] = request.maintenance_window
        if not UtilClient.is_unset(request.operation_policy):
            body['operation_policy'] = request.operation_policy
        if not UtilClient.is_unset(request.resource_group_id):
            body['resource_group_id'] = request.resource_group_id
        if not UtilClient.is_unset(request.system_events_logging):
            body['system_events_logging'] = request.system_events_logging
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyClusterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_control_list):
            body['access_control_list'] = request.access_control_list
        if not UtilClient.is_unset(request.api_server_eip):
            body['api_server_eip'] = request.api_server_eip
        if not UtilClient.is_unset(request.api_server_eip_id):
            body['api_server_eip_id'] = request.api_server_eip_id
        if not UtilClient.is_unset(request.cluster_name):
            body['cluster_name'] = request.cluster_name
        if not UtilClient.is_unset(request.deletion_protection):
            body['deletion_protection'] = request.deletion_protection
        if not UtilClient.is_unset(request.enable_rrsa):
            body['enable_rrsa'] = request.enable_rrsa
        if not UtilClient.is_unset(request.ingress_domain_rebinding):
            body['ingress_domain_rebinding'] = request.ingress_domain_rebinding
        if not UtilClient.is_unset(request.ingress_loadbalancer_id):
            body['ingress_loadbalancer_id'] = request.ingress_loadbalancer_id
        if not UtilClient.is_unset(request.instance_deletion_protection):
            body['instance_deletion_protection'] = request.instance_deletion_protection
        if not UtilClient.is_unset(request.maintenance_window):
            body['maintenance_window'] = request.maintenance_window
        if not UtilClient.is_unset(request.operation_policy):
            body['operation_policy'] = request.operation_policy
        if not UtilClient.is_unset(request.resource_group_id):
            body['resource_group_id'] = request.resource_group_id
        if not UtilClient.is_unset(request.system_events_logging):
            body['system_events_logging'] = request.system_events_logging
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterRequest,
    ) -> cs20151215_models.ModifyClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_with_options(cluster_id, request, headers, runtime)

    async def modify_cluster_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterRequest,
    ) -> cs20151215_models.ModifyClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_cluster_with_options_async(cluster_id, request, headers, runtime)

    def modify_cluster_addon_with_options(
        self,
        cluster_id: str,
        component_id: str,
        request: cs20151215_models.ModifyClusterAddonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyClusterAddonResponse:
        """
        You can use this API operation to modify the components in a Container Service for Kubernetes (ACK) cluster or the control plane components in an ACK Pro cluster.
        *   To query the customizable parameters of a component, call the `DescribeClusterAddonMetadata` API operation. For more information, see [Query the metadata of a specified component version](https://www.alibabacloud.com/help/zh/container-service-for-kubernetes/latest/query).
        *   For more information about the customizable parameters of control plane components in ACK Pro clusters, see [Customize the parameters of control plane components in ACK Pro clusters](https://www.alibabacloud.com/help/zh/container-service-for-kubernetes/latest/customize-control-plane-parameters-for-a-professional-kubernetes-cluster).
        After you call this operation, the component may be redeployed and restarted. We recommend that you assess the impact before you call this operation.
        
        @param request: ModifyClusterAddonRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterAddonResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterAddon',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/{OpenApiUtilClient.get_encode_param(component_id)}/config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterAddonResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_addon_with_options_async(
        self,
        cluster_id: str,
        component_id: str,
        request: cs20151215_models.ModifyClusterAddonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyClusterAddonResponse:
        """
        You can use this API operation to modify the components in a Container Service for Kubernetes (ACK) cluster or the control plane components in an ACK Pro cluster.
        *   To query the customizable parameters of a component, call the `DescribeClusterAddonMetadata` API operation. For more information, see [Query the metadata of a specified component version](https://www.alibabacloud.com/help/zh/container-service-for-kubernetes/latest/query).
        *   For more information about the customizable parameters of control plane components in ACK Pro clusters, see [Customize the parameters of control plane components in ACK Pro clusters](https://www.alibabacloud.com/help/zh/container-service-for-kubernetes/latest/customize-control-plane-parameters-for-a-professional-kubernetes-cluster).
        After you call this operation, the component may be redeployed and restarted. We recommend that you assess the impact before you call this operation.
        
        @param request: ModifyClusterAddonRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterAddonResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterAddon',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/{OpenApiUtilClient.get_encode_param(component_id)}/config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterAddonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_addon(
        self,
        cluster_id: str,
        component_id: str,
        request: cs20151215_models.ModifyClusterAddonRequest,
    ) -> cs20151215_models.ModifyClusterAddonResponse:
        """
        You can use this API operation to modify the components in a Container Service for Kubernetes (ACK) cluster or the control plane components in an ACK Pro cluster.
        *   To query the customizable parameters of a component, call the `DescribeClusterAddonMetadata` API operation. For more information, see [Query the metadata of a specified component version](https://www.alibabacloud.com/help/zh/container-service-for-kubernetes/latest/query).
        *   For more information about the customizable parameters of control plane components in ACK Pro clusters, see [Customize the parameters of control plane components in ACK Pro clusters](https://www.alibabacloud.com/help/zh/container-service-for-kubernetes/latest/customize-control-plane-parameters-for-a-professional-kubernetes-cluster).
        After you call this operation, the component may be redeployed and restarted. We recommend that you assess the impact before you call this operation.
        
        @param request: ModifyClusterAddonRequest
        @return: ModifyClusterAddonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_addon_with_options(cluster_id, component_id, request, headers, runtime)

    async def modify_cluster_addon_async(
        self,
        cluster_id: str,
        component_id: str,
        request: cs20151215_models.ModifyClusterAddonRequest,
    ) -> cs20151215_models.ModifyClusterAddonResponse:
        """
        You can use this API operation to modify the components in a Container Service for Kubernetes (ACK) cluster or the control plane components in an ACK Pro cluster.
        *   To query the customizable parameters of a component, call the `DescribeClusterAddonMetadata` API operation. For more information, see [Query the metadata of a specified component version](https://www.alibabacloud.com/help/zh/container-service-for-kubernetes/latest/query).
        *   For more information about the customizable parameters of control plane components in ACK Pro clusters, see [Customize the parameters of control plane components in ACK Pro clusters](https://www.alibabacloud.com/help/zh/container-service-for-kubernetes/latest/customize-control-plane-parameters-for-a-professional-kubernetes-cluster).
        After you call this operation, the component may be redeployed and restarted. We recommend that you assess the impact before you call this operation.
        
        @param request: ModifyClusterAddonRequest
        @return: ModifyClusterAddonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_cluster_addon_with_options_async(cluster_id, component_id, request, headers, runtime)

    def modify_cluster_configuration_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyClusterConfigurationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.customize_config):
            body['customize_config'] = request.customize_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterConfiguration',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/configuration',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_configuration_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterConfigurationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyClusterConfigurationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.customize_config):
            body['customize_config'] = request.customize_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterConfiguration',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/configuration',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_configuration(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterConfigurationRequest,
    ) -> cs20151215_models.ModifyClusterConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_configuration_with_options(cluster_id, request, headers, runtime)

    async def modify_cluster_configuration_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterConfigurationRequest,
    ) -> cs20151215_models.ModifyClusterConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_cluster_configuration_with_options_async(cluster_id, request, headers, runtime)

    def modify_cluster_node_pool_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ModifyClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyClusterNodePoolResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_scaling):
            body['auto_scaling'] = request.auto_scaling
        if not UtilClient.is_unset(request.concurrency):
            body['concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.kubernetes_config):
            body['kubernetes_config'] = request.kubernetes_config
        if not UtilClient.is_unset(request.management):
            body['management'] = request.management
        if not UtilClient.is_unset(request.nodepool_info):
            body['nodepool_info'] = request.nodepool_info
        if not UtilClient.is_unset(request.scaling_group):
            body['scaling_group'] = request.scaling_group
        if not UtilClient.is_unset(request.tee_config):
            body['tee_config'] = request.tee_config
        if not UtilClient.is_unset(request.update_nodes):
            body['update_nodes'] = request.update_nodes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_node_pool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ModifyClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyClusterNodePoolResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_scaling):
            body['auto_scaling'] = request.auto_scaling
        if not UtilClient.is_unset(request.concurrency):
            body['concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.kubernetes_config):
            body['kubernetes_config'] = request.kubernetes_config
        if not UtilClient.is_unset(request.management):
            body['management'] = request.management
        if not UtilClient.is_unset(request.nodepool_info):
            body['nodepool_info'] = request.nodepool_info
        if not UtilClient.is_unset(request.scaling_group):
            body['scaling_group'] = request.scaling_group
        if not UtilClient.is_unset(request.tee_config):
            body['tee_config'] = request.tee_config
        if not UtilClient.is_unset(request.update_nodes):
            body['update_nodes'] = request.update_nodes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterNodePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_node_pool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ModifyClusterNodePoolRequest,
    ) -> cs20151215_models.ModifyClusterNodePoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_node_pool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def modify_cluster_node_pool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ModifyClusterNodePoolRequest,
    ) -> cs20151215_models.ModifyClusterNodePoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_cluster_node_pool_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def modify_cluster_tags_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyClusterTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='ModifyClusterTags',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_tags_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterTagsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyClusterTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='ModifyClusterTags',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyClusterTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_tags(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterTagsRequest,
    ) -> cs20151215_models.ModifyClusterTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_tags_with_options(cluster_id, request, headers, runtime)

    async def modify_cluster_tags_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ModifyClusterTagsRequest,
    ) -> cs20151215_models.ModifyClusterTagsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_cluster_tags_with_options_async(cluster_id, request, headers, runtime)

    def modify_node_pool_node_config_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ModifyNodePoolNodeConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyNodePoolNodeConfigResponse:
        """
        >  Container Service for Kubernetes (ACK) allows you to modify the kubelet configuration of nodes in a node pool. After you modify the kubelet configuration, the new configuration immediately takes effect on existing nodes in the node pool and is automatically applied to newly added nodes.
        
        @param request: ModifyNodePoolNodeConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodePoolNodeConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.kubelet_config):
            body['kubelet_config'] = request.kubelet_config
        if not UtilClient.is_unset(request.rolling_policy):
            body['rolling_policy'] = request.rolling_policy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyNodePoolNodeConfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}/node_config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyNodePoolNodeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_node_pool_node_config_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ModifyNodePoolNodeConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyNodePoolNodeConfigResponse:
        """
        >  Container Service for Kubernetes (ACK) allows you to modify the kubelet configuration of nodes in a node pool. After you modify the kubelet configuration, the new configuration immediately takes effect on existing nodes in the node pool and is automatically applied to newly added nodes.
        
        @param request: ModifyNodePoolNodeConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodePoolNodeConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.kubelet_config):
            body['kubelet_config'] = request.kubelet_config
        if not UtilClient.is_unset(request.rolling_policy):
            body['rolling_policy'] = request.rolling_policy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyNodePoolNodeConfig',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}/node_config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyNodePoolNodeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_node_pool_node_config(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ModifyNodePoolNodeConfigRequest,
    ) -> cs20151215_models.ModifyNodePoolNodeConfigResponse:
        """
        >  Container Service for Kubernetes (ACK) allows you to modify the kubelet configuration of nodes in a node pool. After you modify the kubelet configuration, the new configuration immediately takes effect on existing nodes in the node pool and is automatically applied to newly added nodes.
        
        @param request: ModifyNodePoolNodeConfigRequest
        @return: ModifyNodePoolNodeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_node_pool_node_config_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def modify_node_pool_node_config_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ModifyNodePoolNodeConfigRequest,
    ) -> cs20151215_models.ModifyNodePoolNodeConfigResponse:
        """
        >  Container Service for Kubernetes (ACK) allows you to modify the kubelet configuration of nodes in a node pool. After you modify the kubelet configuration, the new configuration immediately takes effect on existing nodes in the node pool and is automatically applied to newly added nodes.
        
        @param request: ModifyNodePoolNodeConfigRequest
        @return: ModifyNodePoolNodeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_node_pool_node_config_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def modify_policy_instance_with_options(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.ModifyPolicyInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyPolicyInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.instance_name):
            body['instance_name'] = request.instance_name
        if not UtilClient.is_unset(request.namespaces):
            body['namespaces'] = request.namespaces
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPolicyInstance',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/policies/{OpenApiUtilClient.get_encode_param(policy_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyPolicyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_policy_instance_with_options_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.ModifyPolicyInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ModifyPolicyInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.instance_name):
            body['instance_name'] = request.instance_name
        if not UtilClient.is_unset(request.namespaces):
            body['namespaces'] = request.namespaces
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPolicyInstance',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/policies/{OpenApiUtilClient.get_encode_param(policy_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ModifyPolicyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_policy_instance(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.ModifyPolicyInstanceRequest,
    ) -> cs20151215_models.ModifyPolicyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_policy_instance_with_options(cluster_id, policy_name, request, headers, runtime)

    async def modify_policy_instance_async(
        self,
        cluster_id: str,
        policy_name: str,
        request: cs20151215_models.ModifyPolicyInstanceRequest,
    ) -> cs20151215_models.ModifyPolicyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_policy_instance_with_options_async(cluster_id, policy_name, request, headers, runtime)

    def open_ack_service_with_options(
        self,
        request: cs20151215_models.OpenAckServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.OpenAckServiceResponse:
        """
        You can activate ACK by using Alibaba Cloud accounts.
        *   To activate ACK by using RAM users, you need to grant the AdministratorAccess permission to the RAM users.
        
        @param request: OpenAckServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenAckServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenAckService',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/service/open',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.OpenAckServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_ack_service_with_options_async(
        self,
        request: cs20151215_models.OpenAckServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.OpenAckServiceResponse:
        """
        You can activate ACK by using Alibaba Cloud accounts.
        *   To activate ACK by using RAM users, you need to grant the AdministratorAccess permission to the RAM users.
        
        @param request: OpenAckServiceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenAckServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenAckService',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/service/open',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.OpenAckServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_ack_service(
        self,
        request: cs20151215_models.OpenAckServiceRequest,
    ) -> cs20151215_models.OpenAckServiceResponse:
        """
        You can activate ACK by using Alibaba Cloud accounts.
        *   To activate ACK by using RAM users, you need to grant the AdministratorAccess permission to the RAM users.
        
        @param request: OpenAckServiceRequest
        @return: OpenAckServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.open_ack_service_with_options(request, headers, runtime)

    async def open_ack_service_async(
        self,
        request: cs20151215_models.OpenAckServiceRequest,
    ) -> cs20151215_models.OpenAckServiceResponse:
        """
        You can activate ACK by using Alibaba Cloud accounts.
        *   To activate ACK by using RAM users, you need to grant the AdministratorAccess permission to the RAM users.
        
        @param request: OpenAckServiceRequest
        @return: OpenAckServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.open_ack_service_with_options_async(request, headers, runtime)

    def pause_cluster_upgrade_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.PauseClusterUpgradeResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PauseClusterUpgradeResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PauseClusterUpgrade',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/upgrade/pause',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.PauseClusterUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_cluster_upgrade_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.PauseClusterUpgradeResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PauseClusterUpgradeResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PauseClusterUpgrade',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/upgrade/pause',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.PauseClusterUpgradeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_cluster_upgrade(
        self,
        cluster_id: str,
    ) -> cs20151215_models.PauseClusterUpgradeResponse:
        """
        @deprecated
        
        @return: PauseClusterUpgradeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pause_cluster_upgrade_with_options(cluster_id, headers, runtime)

    async def pause_cluster_upgrade_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.PauseClusterUpgradeResponse:
        """
        @deprecated
        
        @return: PauseClusterUpgradeResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.pause_cluster_upgrade_with_options_async(cluster_id, headers, runtime)

    def pause_component_upgrade_with_options(
        self,
        clusterid: str,
        componentid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.PauseComponentUpgradeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PauseComponentUpgrade',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(clusterid)}/components/{OpenApiUtilClient.get_encode_param(componentid)}/pause',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.PauseComponentUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_component_upgrade_with_options_async(
        self,
        clusterid: str,
        componentid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.PauseComponentUpgradeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PauseComponentUpgrade',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(clusterid)}/components/{OpenApiUtilClient.get_encode_param(componentid)}/pause',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.PauseComponentUpgradeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_component_upgrade(
        self,
        clusterid: str,
        componentid: str,
    ) -> cs20151215_models.PauseComponentUpgradeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pause_component_upgrade_with_options(clusterid, componentid, headers, runtime)

    async def pause_component_upgrade_async(
        self,
        clusterid: str,
        componentid: str,
    ) -> cs20151215_models.PauseComponentUpgradeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.pause_component_upgrade_with_options_async(clusterid, componentid, headers, runtime)

    def pause_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.PauseTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PauseTask',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/pause',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.PauseTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.PauseTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='PauseTask',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/pause',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.PauseTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_task(
        self,
        task_id: str,
    ) -> cs20151215_models.PauseTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pause_task_with_options(task_id, headers, runtime)

    async def pause_task_async(
        self,
        task_id: str,
    ) -> cs20151215_models.PauseTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.pause_task_with_options_async(task_id, headers, runtime)

    def remove_cluster_nodes_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.RemoveClusterNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RemoveClusterNodesResponse:
        """
        @deprecated
        ****\
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        *   Unknown errors may occur when you remove nodes. Before you remove nodes, back up the data on the nodes.
        *   Nodes remain in the Unschedulable state when they are being removed.
        *   You can remove only worker nodes. You cannot remove master nodes.
        
        @param request: RemoveClusterNodesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveClusterNodesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drain_node):
            body['drain_node'] = request.drain_node
        if not UtilClient.is_unset(request.nodes):
            body['nodes'] = request.nodes
        if not UtilClient.is_unset(request.release_node):
            body['release_node'] = request.release_node
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveClusterNodes',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodes/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.RemoveClusterNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_cluster_nodes_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.RemoveClusterNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RemoveClusterNodesResponse:
        """
        @deprecated
        ****\
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        *   Unknown errors may occur when you remove nodes. Before you remove nodes, back up the data on the nodes.
        *   Nodes remain in the Unschedulable state when they are being removed.
        *   You can remove only worker nodes. You cannot remove master nodes.
        
        @param request: RemoveClusterNodesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveClusterNodesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.drain_node):
            body['drain_node'] = request.drain_node
        if not UtilClient.is_unset(request.nodes):
            body['nodes'] = request.nodes
        if not UtilClient.is_unset(request.release_node):
            body['release_node'] = request.release_node
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveClusterNodes',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodes/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.RemoveClusterNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_cluster_nodes(
        self,
        cluster_id: str,
        request: cs20151215_models.RemoveClusterNodesRequest,
    ) -> cs20151215_models.RemoveClusterNodesResponse:
        """
        @deprecated
        ****\
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        *   Unknown errors may occur when you remove nodes. Before you remove nodes, back up the data on the nodes.
        *   Nodes remain in the Unschedulable state when they are being removed.
        *   You can remove only worker nodes. You cannot remove master nodes.
        
        @param request: RemoveClusterNodesRequest
        @return: RemoveClusterNodesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_cluster_nodes_with_options(cluster_id, request, headers, runtime)

    async def remove_cluster_nodes_async(
        self,
        cluster_id: str,
        request: cs20151215_models.RemoveClusterNodesRequest,
    ) -> cs20151215_models.RemoveClusterNodesResponse:
        """
        @deprecated
        ****\
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours.
        *   Unknown errors may occur when you remove nodes. Before you remove nodes, back up the data on the nodes.
        *   Nodes remain in the Unschedulable state when they are being removed.
        *   You can remove only worker nodes. You cannot remove master nodes.
        
        @param request: RemoveClusterNodesRequest
        @return: RemoveClusterNodesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_cluster_nodes_with_options_async(cluster_id, request, headers, runtime)

    def remove_node_pool_nodes_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        tmp_req: cs20151215_models.RemoveNodePoolNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RemoveNodePoolNodesResponse:
        """
        *\
        ****\
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours. - The operation may have unexpected risks. Back up the data before you perform this operation. - When the system removes a node, it sets the status of the node to Unschedulable. - The system removes only worker nodes. It does not remove master nodes.
        
        @param tmp_req: RemoveNodePoolNodesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveNodePoolNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.RemoveNodePoolNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'instance_ids', 'json')
        if not UtilClient.is_unset(tmp_req.nodes):
            request.nodes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.nodes, 'nodes', 'json')
        query = {}
        if not UtilClient.is_unset(request.concurrency):
            query['concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.drain_node):
            query['drain_node'] = request.drain_node
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['instance_ids'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.nodes_shrink):
            query['nodes'] = request.nodes_shrink
        if not UtilClient.is_unset(request.release_node):
            query['release_node'] = request.release_node
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveNodePoolNodes',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}/nodes',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.RemoveNodePoolNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_node_pool_nodes_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        tmp_req: cs20151215_models.RemoveNodePoolNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RemoveNodePoolNodesResponse:
        """
        *\
        ****\
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours. - The operation may have unexpected risks. Back up the data before you perform this operation. - When the system removes a node, it sets the status of the node to Unschedulable. - The system removes only worker nodes. It does not remove master nodes.
        
        @param tmp_req: RemoveNodePoolNodesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveNodePoolNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.RemoveNodePoolNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'instance_ids', 'json')
        if not UtilClient.is_unset(tmp_req.nodes):
            request.nodes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.nodes, 'nodes', 'json')
        query = {}
        if not UtilClient.is_unset(request.concurrency):
            query['concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.drain_node):
            query['drain_node'] = request.drain_node
        if not UtilClient.is_unset(request.instance_ids_shrink):
            query['instance_ids'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.nodes_shrink):
            query['nodes'] = request.nodes_shrink
        if not UtilClient.is_unset(request.release_node):
            query['release_node'] = request.release_node
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveNodePoolNodes',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}/nodes',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.RemoveNodePoolNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_node_pool_nodes(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.RemoveNodePoolNodesRequest,
    ) -> cs20151215_models.RemoveNodePoolNodesResponse:
        """
        *\
        ****\
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours. - The operation may have unexpected risks. Back up the data before you perform this operation. - When the system removes a node, it sets the status of the node to Unschedulable. - The system removes only worker nodes. It does not remove master nodes.
        
        @param request: RemoveNodePoolNodesRequest
        @return: RemoveNodePoolNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_node_pool_nodes_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def remove_node_pool_nodes_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.RemoveNodePoolNodesRequest,
    ) -> cs20151215_models.RemoveNodePoolNodesResponse:
        """
        *\
        ****\
        *   When you remove a node, the pods that run on the node are migrated to other nodes. This may cause service interruptions. We recommend that you remove nodes during off-peak hours. - The operation may have unexpected risks. Back up the data before you perform this operation. - When the system removes a node, it sets the status of the node to Unschedulable. - The system removes only worker nodes. It does not remove master nodes.
        
        @param request: RemoveNodePoolNodesRequest
        @return: RemoveNodePoolNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_node_pool_nodes_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def remove_workflow_with_options(
        self,
        workflow_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RemoveWorkflowResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveWorkflow',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/gs/workflow/{OpenApiUtilClient.get_encode_param(workflow_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.RemoveWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_workflow_with_options_async(
        self,
        workflow_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RemoveWorkflowResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveWorkflow',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/gs/workflow/{OpenApiUtilClient.get_encode_param(workflow_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.RemoveWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_workflow(
        self,
        workflow_name: str,
    ) -> cs20151215_models.RemoveWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_workflow_with_options(workflow_name, headers, runtime)

    async def remove_workflow_async(
        self,
        workflow_name: str,
    ) -> cs20151215_models.RemoveWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_workflow_with_options_async(workflow_name, headers, runtime)

    def repair_cluster_node_pool_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.RepairClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RepairClusterNodePoolResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_restart):
            body['auto_restart'] = request.auto_restart
        if not UtilClient.is_unset(request.nodes):
            body['nodes'] = request.nodes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RepairClusterNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}/repair',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.RepairClusterNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def repair_cluster_node_pool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.RepairClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RepairClusterNodePoolResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_restart):
            body['auto_restart'] = request.auto_restart
        if not UtilClient.is_unset(request.nodes):
            body['nodes'] = request.nodes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RepairClusterNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}/repair',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.RepairClusterNodePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def repair_cluster_node_pool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.RepairClusterNodePoolRequest,
    ) -> cs20151215_models.RepairClusterNodePoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.repair_cluster_node_pool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def repair_cluster_node_pool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.RepairClusterNodePoolRequest,
    ) -> cs20151215_models.RepairClusterNodePoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.repair_cluster_node_pool_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def resume_component_upgrade_with_options(
        self,
        clusterid: str,
        componentid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ResumeComponentUpgradeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeComponentUpgrade',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(clusterid)}/components/{OpenApiUtilClient.get_encode_param(componentid)}/resume',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ResumeComponentUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_component_upgrade_with_options_async(
        self,
        clusterid: str,
        componentid: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ResumeComponentUpgradeResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeComponentUpgrade',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(clusterid)}/components/{OpenApiUtilClient.get_encode_param(componentid)}/resume',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ResumeComponentUpgradeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_component_upgrade(
        self,
        clusterid: str,
        componentid: str,
    ) -> cs20151215_models.ResumeComponentUpgradeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_component_upgrade_with_options(clusterid, componentid, headers, runtime)

    async def resume_component_upgrade_async(
        self,
        clusterid: str,
        componentid: str,
    ) -> cs20151215_models.ResumeComponentUpgradeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.resume_component_upgrade_with_options_async(clusterid, componentid, headers, runtime)

    def resume_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ResumeTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeTask',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/resume',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ResumeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ResumeTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeTask',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/resume',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ResumeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_task(
        self,
        task_id: str,
    ) -> cs20151215_models.ResumeTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_task_with_options(task_id, headers, runtime)

    async def resume_task_async(
        self,
        task_id: str,
    ) -> cs20151215_models.ResumeTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.resume_task_with_options_async(task_id, headers, runtime)

    def resume_upgrade_cluster_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ResumeUpgradeClusterResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeUpgradeClusterResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeUpgradeCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/upgrade/resume',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ResumeUpgradeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_upgrade_cluster_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ResumeUpgradeClusterResponse:
        """
        @deprecated
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeUpgradeClusterResponse
        Deprecated
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ResumeUpgradeCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/upgrade/resume',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.ResumeUpgradeClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_upgrade_cluster(
        self,
        cluster_id: str,
    ) -> cs20151215_models.ResumeUpgradeClusterResponse:
        """
        @deprecated
        
        @return: ResumeUpgradeClusterResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.resume_upgrade_cluster_with_options(cluster_id, headers, runtime)

    async def resume_upgrade_cluster_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.ResumeUpgradeClusterResponse:
        """
        @deprecated
        
        @return: ResumeUpgradeClusterResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.resume_upgrade_cluster_with_options_async(cluster_id, headers, runtime)

    def run_cluster_check_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.RunClusterCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RunClusterCheckResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.options):
            body['options'] = request.options
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunClusterCheck',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/checks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.RunClusterCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_cluster_check_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.RunClusterCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.RunClusterCheckResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.options):
            body['options'] = request.options
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunClusterCheck',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/checks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.RunClusterCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_cluster_check(
        self,
        cluster_id: str,
        request: cs20151215_models.RunClusterCheckRequest,
    ) -> cs20151215_models.RunClusterCheckResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_cluster_check_with_options(cluster_id, request, headers, runtime)

    async def run_cluster_check_async(
        self,
        cluster_id: str,
        request: cs20151215_models.RunClusterCheckRequest,
    ) -> cs20151215_models.RunClusterCheckResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_cluster_check_with_options_async(cluster_id, request, headers, runtime)

    def scale_cluster_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ScaleClusterResponse:
        """
        @deprecated
        
        @param request: ScaleClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleClusterResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_monitor_flags):
            body['cloud_monitor_flags'] = request.cloud_monitor_flags
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.disable_rollback):
            body['disable_rollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.login_password):
            body['login_password'] = request.login_password
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        if not UtilClient.is_unset(request.worker_auto_renew):
            body['worker_auto_renew'] = request.worker_auto_renew
        if not UtilClient.is_unset(request.worker_auto_renew_period):
            body['worker_auto_renew_period'] = request.worker_auto_renew_period
        if not UtilClient.is_unset(request.worker_data_disk):
            body['worker_data_disk'] = request.worker_data_disk
        if not UtilClient.is_unset(request.worker_data_disks):
            body['worker_data_disks'] = request.worker_data_disks
        if not UtilClient.is_unset(request.worker_instance_charge_type):
            body['worker_instance_charge_type'] = request.worker_instance_charge_type
        if not UtilClient.is_unset(request.worker_instance_types):
            body['worker_instance_types'] = request.worker_instance_types
        if not UtilClient.is_unset(request.worker_period):
            body['worker_period'] = request.worker_period
        if not UtilClient.is_unset(request.worker_period_unit):
            body['worker_period_unit'] = request.worker_period_unit
        if not UtilClient.is_unset(request.worker_system_disk_category):
            body['worker_system_disk_category'] = request.worker_system_disk_category
        if not UtilClient.is_unset(request.worker_system_disk_size):
            body['worker_system_disk_size'] = request.worker_system_disk_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScaleCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ScaleClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_cluster_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ScaleClusterResponse:
        """
        @deprecated
        
        @param request: ScaleClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleClusterResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_monitor_flags):
            body['cloud_monitor_flags'] = request.cloud_monitor_flags
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.disable_rollback):
            body['disable_rollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.login_password):
            body['login_password'] = request.login_password
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        if not UtilClient.is_unset(request.worker_auto_renew):
            body['worker_auto_renew'] = request.worker_auto_renew
        if not UtilClient.is_unset(request.worker_auto_renew_period):
            body['worker_auto_renew_period'] = request.worker_auto_renew_period
        if not UtilClient.is_unset(request.worker_data_disk):
            body['worker_data_disk'] = request.worker_data_disk
        if not UtilClient.is_unset(request.worker_data_disks):
            body['worker_data_disks'] = request.worker_data_disks
        if not UtilClient.is_unset(request.worker_instance_charge_type):
            body['worker_instance_charge_type'] = request.worker_instance_charge_type
        if not UtilClient.is_unset(request.worker_instance_types):
            body['worker_instance_types'] = request.worker_instance_types
        if not UtilClient.is_unset(request.worker_period):
            body['worker_period'] = request.worker_period
        if not UtilClient.is_unset(request.worker_period_unit):
            body['worker_period_unit'] = request.worker_period_unit
        if not UtilClient.is_unset(request.worker_system_disk_category):
            body['worker_system_disk_category'] = request.worker_system_disk_category
        if not UtilClient.is_unset(request.worker_system_disk_size):
            body['worker_system_disk_size'] = request.worker_system_disk_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScaleCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ScaleClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_cluster(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleClusterRequest,
    ) -> cs20151215_models.ScaleClusterResponse:
        """
        @deprecated
        
        @param request: ScaleClusterRequest
        @return: ScaleClusterResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_cluster_with_options(cluster_id, request, headers, runtime)

    async def scale_cluster_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleClusterRequest,
    ) -> cs20151215_models.ScaleClusterResponse:
        """
        @deprecated
        
        @param request: ScaleClusterRequest
        @return: ScaleClusterResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scale_cluster_with_options_async(cluster_id, request, headers, runtime)

    def scale_cluster_node_pool_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ScaleClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ScaleClusterNodePoolResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScaleClusterNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ScaleClusterNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_cluster_node_pool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ScaleClusterNodePoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ScaleClusterNodePoolResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScaleClusterNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ScaleClusterNodePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_cluster_node_pool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ScaleClusterNodePoolRequest,
    ) -> cs20151215_models.ScaleClusterNodePoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_cluster_node_pool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def scale_cluster_node_pool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.ScaleClusterNodePoolRequest,
    ) -> cs20151215_models.ScaleClusterNodePoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scale_cluster_node_pool_with_options_async(cluster_id, nodepool_id, request, headers, runtime)

    def scale_out_cluster_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleOutClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ScaleOutClusterResponse:
        """
        *\
        ****The ScaleOutCluster API operation is phased out. You must call the node pool-related API operations to manage nodes. If you want to add worker nodes to a Container Service for Kubernetes (ACK) cluster, call the ScaleClusterNodePool API operation. For more information, see [ScaleClusterNodePool](~~184928~~).
        
        @param request: ScaleOutClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleOutClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_monitor_flags):
            body['cloud_monitor_flags'] = request.cloud_monitor_flags
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.login_password):
            body['login_password'] = request.login_password
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        if not UtilClient.is_unset(request.worker_auto_renew):
            body['worker_auto_renew'] = request.worker_auto_renew
        if not UtilClient.is_unset(request.worker_auto_renew_period):
            body['worker_auto_renew_period'] = request.worker_auto_renew_period
        if not UtilClient.is_unset(request.worker_data_disks):
            body['worker_data_disks'] = request.worker_data_disks
        if not UtilClient.is_unset(request.worker_instance_charge_type):
            body['worker_instance_charge_type'] = request.worker_instance_charge_type
        if not UtilClient.is_unset(request.worker_instance_types):
            body['worker_instance_types'] = request.worker_instance_types
        if not UtilClient.is_unset(request.worker_period):
            body['worker_period'] = request.worker_period
        if not UtilClient.is_unset(request.worker_period_unit):
            body['worker_period_unit'] = request.worker_period_unit
        if not UtilClient.is_unset(request.worker_system_disk_category):
            body['worker_system_disk_category'] = request.worker_system_disk_category
        if not UtilClient.is_unset(request.worker_system_disk_size):
            body['worker_system_disk_size'] = request.worker_system_disk_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScaleOutCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ScaleOutClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_out_cluster_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleOutClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ScaleOutClusterResponse:
        """
        *\
        ****The ScaleOutCluster API operation is phased out. You must call the node pool-related API operations to manage nodes. If you want to add worker nodes to a Container Service for Kubernetes (ACK) cluster, call the ScaleClusterNodePool API operation. For more information, see [ScaleClusterNodePool](~~184928~~).
        
        @param request: ScaleOutClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleOutClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_monitor_flags):
            body['cloud_monitor_flags'] = request.cloud_monitor_flags
        if not UtilClient.is_unset(request.count):
            body['count'] = request.count
        if not UtilClient.is_unset(request.cpu_policy):
            body['cpu_policy'] = request.cpu_policy
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.key_pair):
            body['key_pair'] = request.key_pair
        if not UtilClient.is_unset(request.login_password):
            body['login_password'] = request.login_password
        if not UtilClient.is_unset(request.rds_instances):
            body['rds_instances'] = request.rds_instances
        if not UtilClient.is_unset(request.runtime):
            body['runtime'] = request.runtime
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.taints):
            body['taints'] = request.taints
        if not UtilClient.is_unset(request.user_data):
            body['user_data'] = request.user_data
        if not UtilClient.is_unset(request.vswitch_ids):
            body['vswitch_ids'] = request.vswitch_ids
        if not UtilClient.is_unset(request.worker_auto_renew):
            body['worker_auto_renew'] = request.worker_auto_renew
        if not UtilClient.is_unset(request.worker_auto_renew_period):
            body['worker_auto_renew_period'] = request.worker_auto_renew_period
        if not UtilClient.is_unset(request.worker_data_disks):
            body['worker_data_disks'] = request.worker_data_disks
        if not UtilClient.is_unset(request.worker_instance_charge_type):
            body['worker_instance_charge_type'] = request.worker_instance_charge_type
        if not UtilClient.is_unset(request.worker_instance_types):
            body['worker_instance_types'] = request.worker_instance_types
        if not UtilClient.is_unset(request.worker_period):
            body['worker_period'] = request.worker_period
        if not UtilClient.is_unset(request.worker_period_unit):
            body['worker_period_unit'] = request.worker_period_unit
        if not UtilClient.is_unset(request.worker_system_disk_category):
            body['worker_system_disk_category'] = request.worker_system_disk_category
        if not UtilClient.is_unset(request.worker_system_disk_size):
            body['worker_system_disk_size'] = request.worker_system_disk_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScaleOutCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ScaleOutClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_out_cluster(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleOutClusterRequest,
    ) -> cs20151215_models.ScaleOutClusterResponse:
        """
        *\
        ****The ScaleOutCluster API operation is phased out. You must call the node pool-related API operations to manage nodes. If you want to add worker nodes to a Container Service for Kubernetes (ACK) cluster, call the ScaleClusterNodePool API operation. For more information, see [ScaleClusterNodePool](~~184928~~).
        
        @param request: ScaleOutClusterRequest
        @return: ScaleOutClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_out_cluster_with_options(cluster_id, request, headers, runtime)

    async def scale_out_cluster_async(
        self,
        cluster_id: str,
        request: cs20151215_models.ScaleOutClusterRequest,
    ) -> cs20151215_models.ScaleOutClusterResponse:
        """
        *\
        ****The ScaleOutCluster API operation is phased out. You must call the node pool-related API operations to manage nodes. If you want to add worker nodes to a Container Service for Kubernetes (ACK) cluster, call the ScaleClusterNodePool API operation. For more information, see [ScaleClusterNodePool](~~184928~~).
        
        @param request: ScaleOutClusterRequest
        @return: ScaleOutClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scale_out_cluster_with_options_async(cluster_id, request, headers, runtime)

    def scan_cluster_vuls_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ScanClusterVulsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ScanClusterVuls',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/vuls/scan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ScanClusterVulsResponse(),
            self.call_api(params, req, runtime)
        )

    async def scan_cluster_vuls_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.ScanClusterVulsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ScanClusterVuls',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/vuls/scan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.ScanClusterVulsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scan_cluster_vuls(
        self,
        cluster_id: str,
    ) -> cs20151215_models.ScanClusterVulsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scan_cluster_vuls_with_options(cluster_id, headers, runtime)

    async def scan_cluster_vuls_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.ScanClusterVulsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scan_cluster_vuls_with_options_async(cluster_id, headers, runtime)

    def start_alert_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.StartAlertResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartAlert',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/alert/{OpenApiUtilClient.get_encode_param(cluster_id)}/alert_rule/start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.StartAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_alert_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.StartAlertResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartAlert',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/alert/{OpenApiUtilClient.get_encode_param(cluster_id)}/alert_rule/start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.StartAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_alert(
        self,
        cluster_id: str,
    ) -> cs20151215_models.StartAlertResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_alert_with_options(cluster_id, headers, runtime)

    async def start_alert_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.StartAlertResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_alert_with_options_async(cluster_id, headers, runtime)

    def start_workflow_with_options(
        self,
        request: cs20151215_models.StartWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.StartWorkflowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mapping_bam_out_filename):
            body['mapping_bam_out_filename'] = request.mapping_bam_out_filename
        if not UtilClient.is_unset(request.mapping_bam_out_path):
            body['mapping_bam_out_path'] = request.mapping_bam_out_path
        if not UtilClient.is_unset(request.mapping_bucket_name):
            body['mapping_bucket_name'] = request.mapping_bucket_name
        if not UtilClient.is_unset(request.mapping_fastq_first_filename):
            body['mapping_fastq_first_filename'] = request.mapping_fastq_first_filename
        if not UtilClient.is_unset(request.mapping_fastq_path):
            body['mapping_fastq_path'] = request.mapping_fastq_path
        if not UtilClient.is_unset(request.mapping_fastq_second_filename):
            body['mapping_fastq_second_filename'] = request.mapping_fastq_second_filename
        if not UtilClient.is_unset(request.mapping_is_mark_dup):
            body['mapping_is_mark_dup'] = request.mapping_is_mark_dup
        if not UtilClient.is_unset(request.mapping_oss_region):
            body['mapping_oss_region'] = request.mapping_oss_region
        if not UtilClient.is_unset(request.mapping_reference_path):
            body['mapping_reference_path'] = request.mapping_reference_path
        if not UtilClient.is_unset(request.service):
            body['service'] = request.service
        if not UtilClient.is_unset(request.wgs_bucket_name):
            body['wgs_bucket_name'] = request.wgs_bucket_name
        if not UtilClient.is_unset(request.wgs_fastq_first_filename):
            body['wgs_fastq_first_filename'] = request.wgs_fastq_first_filename
        if not UtilClient.is_unset(request.wgs_fastq_path):
            body['wgs_fastq_path'] = request.wgs_fastq_path
        if not UtilClient.is_unset(request.wgs_fastq_second_filename):
            body['wgs_fastq_second_filename'] = request.wgs_fastq_second_filename
        if not UtilClient.is_unset(request.wgs_oss_region):
            body['wgs_oss_region'] = request.wgs_oss_region
        if not UtilClient.is_unset(request.wgs_reference_path):
            body['wgs_reference_path'] = request.wgs_reference_path
        if not UtilClient.is_unset(request.wgs_vcf_out_filename):
            body['wgs_vcf_out_filename'] = request.wgs_vcf_out_filename
        if not UtilClient.is_unset(request.wgs_vcf_out_path):
            body['wgs_vcf_out_path'] = request.wgs_vcf_out_path
        if not UtilClient.is_unset(request.workflow_type):
            body['workflow_type'] = request.workflow_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartWorkflow',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/gs/workflow',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.StartWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_workflow_with_options_async(
        self,
        request: cs20151215_models.StartWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.StartWorkflowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mapping_bam_out_filename):
            body['mapping_bam_out_filename'] = request.mapping_bam_out_filename
        if not UtilClient.is_unset(request.mapping_bam_out_path):
            body['mapping_bam_out_path'] = request.mapping_bam_out_path
        if not UtilClient.is_unset(request.mapping_bucket_name):
            body['mapping_bucket_name'] = request.mapping_bucket_name
        if not UtilClient.is_unset(request.mapping_fastq_first_filename):
            body['mapping_fastq_first_filename'] = request.mapping_fastq_first_filename
        if not UtilClient.is_unset(request.mapping_fastq_path):
            body['mapping_fastq_path'] = request.mapping_fastq_path
        if not UtilClient.is_unset(request.mapping_fastq_second_filename):
            body['mapping_fastq_second_filename'] = request.mapping_fastq_second_filename
        if not UtilClient.is_unset(request.mapping_is_mark_dup):
            body['mapping_is_mark_dup'] = request.mapping_is_mark_dup
        if not UtilClient.is_unset(request.mapping_oss_region):
            body['mapping_oss_region'] = request.mapping_oss_region
        if not UtilClient.is_unset(request.mapping_reference_path):
            body['mapping_reference_path'] = request.mapping_reference_path
        if not UtilClient.is_unset(request.service):
            body['service'] = request.service
        if not UtilClient.is_unset(request.wgs_bucket_name):
            body['wgs_bucket_name'] = request.wgs_bucket_name
        if not UtilClient.is_unset(request.wgs_fastq_first_filename):
            body['wgs_fastq_first_filename'] = request.wgs_fastq_first_filename
        if not UtilClient.is_unset(request.wgs_fastq_path):
            body['wgs_fastq_path'] = request.wgs_fastq_path
        if not UtilClient.is_unset(request.wgs_fastq_second_filename):
            body['wgs_fastq_second_filename'] = request.wgs_fastq_second_filename
        if not UtilClient.is_unset(request.wgs_oss_region):
            body['wgs_oss_region'] = request.wgs_oss_region
        if not UtilClient.is_unset(request.wgs_reference_path):
            body['wgs_reference_path'] = request.wgs_reference_path
        if not UtilClient.is_unset(request.wgs_vcf_out_filename):
            body['wgs_vcf_out_filename'] = request.wgs_vcf_out_filename
        if not UtilClient.is_unset(request.wgs_vcf_out_path):
            body['wgs_vcf_out_path'] = request.wgs_vcf_out_path
        if not UtilClient.is_unset(request.workflow_type):
            body['workflow_type'] = request.workflow_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartWorkflow',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/gs/workflow',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.StartWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_workflow(
        self,
        request: cs20151215_models.StartWorkflowRequest,
    ) -> cs20151215_models.StartWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_workflow_with_options(request, headers, runtime)

    async def start_workflow_async(
        self,
        request: cs20151215_models.StartWorkflowRequest,
    ) -> cs20151215_models.StartWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_workflow_with_options_async(request, headers, runtime)

    def stop_alert_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.StopAlertResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopAlert',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/alert/{OpenApiUtilClient.get_encode_param(cluster_id)}/alert_rule/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.StopAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_alert_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.StopAlertResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopAlert',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/alert/{OpenApiUtilClient.get_encode_param(cluster_id)}/alert_rule/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.StopAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_alert(
        self,
        cluster_id: str,
    ) -> cs20151215_models.StopAlertResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_alert_with_options(cluster_id, headers, runtime)

    async def stop_alert_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.StopAlertResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_alert_with_options_async(cluster_id, headers, runtime)

    def sync_cluster_node_pool_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.SyncClusterNodePoolResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SyncClusterNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/sync_nodepools',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.SyncClusterNodePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_cluster_node_pool_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.SyncClusterNodePoolResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='SyncClusterNodePool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/sync_nodepools',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.SyncClusterNodePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_cluster_node_pool(
        self,
        cluster_id: str,
    ) -> cs20151215_models.SyncClusterNodePoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.sync_cluster_node_pool_with_options(cluster_id, headers, runtime)

    async def sync_cluster_node_pool_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.SyncClusterNodePoolResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.sync_cluster_node_pool_with_options_async(cluster_id, headers, runtime)

    def tag_resources_with_options(
        self,
        request: cs20151215_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['region_id'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            body['resource_ids'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['resource_type'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/tags',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: cs20151215_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['region_id'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            body['resource_ids'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['resource_type'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/tags',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: cs20151215_models.TagResourcesRequest,
    ) -> cs20151215_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: cs20151215_models.TagResourcesRequest,
    ) -> cs20151215_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def un_install_cluster_addons_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.UnInstallClusterAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UnInstallClusterAddonsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.addons)
        )
        params = open_api_models.Params(
            action='UnInstallClusterAddons',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/uninstall',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.UnInstallClusterAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_install_cluster_addons_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UnInstallClusterAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UnInstallClusterAddonsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.addons)
        )
        params = open_api_models.Params(
            action='UnInstallClusterAddons',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/uninstall',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.UnInstallClusterAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_install_cluster_addons(
        self,
        cluster_id: str,
        request: cs20151215_models.UnInstallClusterAddonsRequest,
    ) -> cs20151215_models.UnInstallClusterAddonsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.un_install_cluster_addons_with_options(cluster_id, request, headers, runtime)

    async def un_install_cluster_addons_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UnInstallClusterAddonsRequest,
    ) -> cs20151215_models.UnInstallClusterAddonsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.un_install_cluster_addons_with_options_async(cluster_id, request, headers, runtime)

    def untag_resources_with_options(
        self,
        tmp_req: cs20151215_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UntagResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.UntagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'resource_ids', 'json')
        if not UtilClient.is_unset(tmp_req.tag_keys):
            request.tag_keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_keys, 'tag_keys', 'json')
        query = {}
        if not UtilClient.is_unset(request.all):
            query['all'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['resource_ids'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resource_type'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys_shrink):
            query['tag_keys'] = request.tag_keys_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        tmp_req: cs20151215_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UntagResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = cs20151215_models.UntagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'resource_ids', 'json')
        if not UtilClient.is_unset(tmp_req.tag_keys):
            request.tag_keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_keys, 'tag_keys', 'json')
        query = {}
        if not UtilClient.is_unset(request.all):
            query['all'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['region_id'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['resource_ids'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resource_type'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys_shrink):
            query['tag_keys'] = request.tag_keys_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: cs20151215_models.UntagResourcesRequest,
    ) -> cs20151215_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: cs20151215_models.UntagResourcesRequest,
    ) -> cs20151215_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_contact_group_for_alert_with_options(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateContactGroupForAlertResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateContactGroupForAlert',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/alert/{OpenApiUtilClient.get_encode_param(cluster_id)}/alert_rule/contact_groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.UpdateContactGroupForAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_contact_group_for_alert_with_options_async(
        self,
        cluster_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateContactGroupForAlertResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UpdateContactGroupForAlert',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/alert/{OpenApiUtilClient.get_encode_param(cluster_id)}/alert_rule/contact_groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.UpdateContactGroupForAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_contact_group_for_alert(
        self,
        cluster_id: str,
    ) -> cs20151215_models.UpdateContactGroupForAlertResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_contact_group_for_alert_with_options(cluster_id, headers, runtime)

    async def update_contact_group_for_alert_async(
        self,
        cluster_id: str,
    ) -> cs20151215_models.UpdateContactGroupForAlertResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_contact_group_for_alert_with_options_async(cluster_id, headers, runtime)

    def update_control_plane_log_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateControlPlaneLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateControlPlaneLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliuid):
            body['aliuid'] = request.aliuid
        if not UtilClient.is_unset(request.components):
            body['components'] = request.components
        if not UtilClient.is_unset(request.log_project):
            body['log_project'] = request.log_project
        if not UtilClient.is_unset(request.log_ttl):
            body['log_ttl'] = request.log_ttl
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateControlPlaneLog',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/controlplanelog',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.UpdateControlPlaneLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_control_plane_log_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateControlPlaneLogRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateControlPlaneLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliuid):
            body['aliuid'] = request.aliuid
        if not UtilClient.is_unset(request.components):
            body['components'] = request.components
        if not UtilClient.is_unset(request.log_project):
            body['log_project'] = request.log_project
        if not UtilClient.is_unset(request.log_ttl):
            body['log_ttl'] = request.log_ttl
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateControlPlaneLog',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/controlplanelog',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.UpdateControlPlaneLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_control_plane_log(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateControlPlaneLogRequest,
    ) -> cs20151215_models.UpdateControlPlaneLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_control_plane_log_with_options(cluster_id, request, headers, runtime)

    async def update_control_plane_log_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateControlPlaneLogRequest,
    ) -> cs20151215_models.UpdateControlPlaneLogResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_control_plane_log_with_options_async(cluster_id, request, headers, runtime)

    def update_k8s_cluster_user_config_expire_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateK8sClusterUserConfigExpireRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateK8sClusterUserConfigExpireResponse:
        """
        *\
        ****\
        *   You can call this operation only with an Alibaba Cloud account. - If the kubeconfig file used by your cluster is revoked, the custom validity period of the kubeconfig file is reset. In this case, you need to call this API operation to reconfigure the validity period of the kubeconfig file.
        
        @param request: UpdateK8sClusterUserConfigExpireRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sClusterUserConfigExpireResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.expire_hour):
            body['expire_hour'] = request.expire_hour
        if not UtilClient.is_unset(request.user):
            body['user'] = request.user
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateK8sClusterUserConfigExpire',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/k8s/{OpenApiUtilClient.get_encode_param(cluster_id)}/user_config/expire',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.UpdateK8sClusterUserConfigExpireResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_k8s_cluster_user_config_expire_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateK8sClusterUserConfigExpireRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateK8sClusterUserConfigExpireResponse:
        """
        *\
        ****\
        *   You can call this operation only with an Alibaba Cloud account. - If the kubeconfig file used by your cluster is revoked, the custom validity period of the kubeconfig file is reset. In this case, you need to call this API operation to reconfigure the validity period of the kubeconfig file.
        
        @param request: UpdateK8sClusterUserConfigExpireRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateK8sClusterUserConfigExpireResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.expire_hour):
            body['expire_hour'] = request.expire_hour
        if not UtilClient.is_unset(request.user):
            body['user'] = request.user
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateK8sClusterUserConfigExpire',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/k8s/{OpenApiUtilClient.get_encode_param(cluster_id)}/user_config/expire',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.UpdateK8sClusterUserConfigExpireResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_k8s_cluster_user_config_expire(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateK8sClusterUserConfigExpireRequest,
    ) -> cs20151215_models.UpdateK8sClusterUserConfigExpireResponse:
        """
        *\
        ****\
        *   You can call this operation only with an Alibaba Cloud account. - If the kubeconfig file used by your cluster is revoked, the custom validity period of the kubeconfig file is reset. In this case, you need to call this API operation to reconfigure the validity period of the kubeconfig file.
        
        @param request: UpdateK8sClusterUserConfigExpireRequest
        @return: UpdateK8sClusterUserConfigExpireResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_k8s_cluster_user_config_expire_with_options(cluster_id, request, headers, runtime)

    async def update_k8s_cluster_user_config_expire_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpdateK8sClusterUserConfigExpireRequest,
    ) -> cs20151215_models.UpdateK8sClusterUserConfigExpireResponse:
        """
        *\
        ****\
        *   You can call this operation only with an Alibaba Cloud account. - If the kubeconfig file used by your cluster is revoked, the custom validity period of the kubeconfig file is reset. In this case, you need to call this API operation to reconfigure the validity period of the kubeconfig file.
        
        @param request: UpdateK8sClusterUserConfigExpireRequest
        @return: UpdateK8sClusterUserConfigExpireResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_k8s_cluster_user_config_expire_with_options_async(cluster_id, request, headers, runtime)

    def update_template_with_options(
        self,
        template_id: str,
        request: cs20151215_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        if not UtilClient.is_unset(request.template_type):
            body['template_type'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/templates/{OpenApiUtilClient.get_encode_param(template_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_with_options_async(
        self,
        template_id: str,
        request: cs20151215_models.UpdateTemplateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        if not UtilClient.is_unset(request.template_type):
            body['template_type'] = request.template_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/templates/{OpenApiUtilClient.get_encode_param(template_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.UpdateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template(
        self,
        template_id: str,
        request: cs20151215_models.UpdateTemplateRequest,
    ) -> cs20151215_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_template_with_options(template_id, request, headers, runtime)

    async def update_template_async(
        self,
        template_id: str,
        request: cs20151215_models.UpdateTemplateRequest,
    ) -> cs20151215_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_template_with_options_async(template_id, request, headers, runtime)

    def upgrade_cluster_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.UpgradeClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpgradeClusterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_name):
            body['component_name'] = request.component_name
        if not UtilClient.is_unset(request.master_only):
            body['master_only'] = request.master_only
        if not UtilClient.is_unset(request.next_version):
            body['next_version'] = request.next_version
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/upgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.UpgradeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_cluster_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpgradeClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpgradeClusterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.component_name):
            body['component_name'] = request.component_name
        if not UtilClient.is_unset(request.master_only):
            body['master_only'] = request.master_only
        if not UtilClient.is_unset(request.next_version):
            body['next_version'] = request.next_version
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeCluster',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/api/v2/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/upgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.UpgradeClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_cluster(
        self,
        cluster_id: str,
        request: cs20151215_models.UpgradeClusterRequest,
    ) -> cs20151215_models.UpgradeClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_cluster_with_options(cluster_id, request, headers, runtime)

    async def upgrade_cluster_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpgradeClusterRequest,
    ) -> cs20151215_models.UpgradeClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upgrade_cluster_with_options_async(cluster_id, request, headers, runtime)

    def upgrade_cluster_addons_with_options(
        self,
        cluster_id: str,
        request: cs20151215_models.UpgradeClusterAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpgradeClusterAddonsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='UpgradeClusterAddons',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/upgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.UpgradeClusterAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_cluster_addons_with_options_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpgradeClusterAddonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpgradeClusterAddonsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='UpgradeClusterAddons',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/components/upgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            cs20151215_models.UpgradeClusterAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_cluster_addons(
        self,
        cluster_id: str,
        request: cs20151215_models.UpgradeClusterAddonsRequest,
    ) -> cs20151215_models.UpgradeClusterAddonsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_cluster_addons_with_options(cluster_id, request, headers, runtime)

    async def upgrade_cluster_addons_async(
        self,
        cluster_id: str,
        request: cs20151215_models.UpgradeClusterAddonsRequest,
    ) -> cs20151215_models.UpgradeClusterAddonsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upgrade_cluster_addons_with_options_async(cluster_id, request, headers, runtime)

    def upgrade_cluster_nodepool_with_options(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.UpgradeClusterNodepoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpgradeClusterNodepoolResponse:
        """
        This operation allows you to update the Kubernetes version, OS version, or container runtime version of the nodes in a node pool.
        
        @param request: UpgradeClusterNodepoolRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeClusterNodepoolResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.kubernetes_version):
            body['kubernetes_version'] = request.kubernetes_version
        if not UtilClient.is_unset(request.runtime_type):
            body['runtime_type'] = request.runtime_type
        if not UtilClient.is_unset(request.runtime_version):
            body['runtime_version'] = request.runtime_version
        if not UtilClient.is_unset(request.use_replace):
            body['use_replace'] = request.use_replace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeClusterNodepool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}/upgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.UpgradeClusterNodepoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_cluster_nodepool_with_options_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.UpgradeClusterNodepoolRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cs20151215_models.UpgradeClusterNodepoolResponse:
        """
        This operation allows you to update the Kubernetes version, OS version, or container runtime version of the nodes in a node pool.
        
        @param request: UpgradeClusterNodepoolRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeClusterNodepoolResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_id):
            body['image_id'] = request.image_id
        if not UtilClient.is_unset(request.kubernetes_version):
            body['kubernetes_version'] = request.kubernetes_version
        if not UtilClient.is_unset(request.runtime_type):
            body['runtime_type'] = request.runtime_type
        if not UtilClient.is_unset(request.runtime_version):
            body['runtime_version'] = request.runtime_version
        if not UtilClient.is_unset(request.use_replace):
            body['use_replace'] = request.use_replace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeClusterNodepool',
            version='2015-12-15',
            protocol='HTTPS',
            pathname=f'/clusters/{OpenApiUtilClient.get_encode_param(cluster_id)}/nodepools/{OpenApiUtilClient.get_encode_param(nodepool_id)}/upgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cs20151215_models.UpgradeClusterNodepoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_cluster_nodepool(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.UpgradeClusterNodepoolRequest,
    ) -> cs20151215_models.UpgradeClusterNodepoolResponse:
        """
        This operation allows you to update the Kubernetes version, OS version, or container runtime version of the nodes in a node pool.
        
        @param request: UpgradeClusterNodepoolRequest
        @return: UpgradeClusterNodepoolResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upgrade_cluster_nodepool_with_options(cluster_id, nodepool_id, request, headers, runtime)

    async def upgrade_cluster_nodepool_async(
        self,
        cluster_id: str,
        nodepool_id: str,
        request: cs20151215_models.UpgradeClusterNodepoolRequest,
    ) -> cs20151215_models.UpgradeClusterNodepoolResponse:
        """
        This operation allows you to update the Kubernetes version, OS version, or container runtime version of the nodes in a node pool.
        
        @param request: UpgradeClusterNodepoolRequest
        @return: UpgradeClusterNodepoolResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upgrade_cluster_nodepool_with_options_async(cluster_id, nodepool_id, request, headers, runtime)
